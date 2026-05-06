"""
`ailayer lint` — validate library content against repository schemas.

  ailayer lint skills [<name>] [--strict]

Validates every `<tool>/SKILL_PROMPT.md` against `docs/SKILL_PROMPT_SCHEMA.md`.
Exits non-zero if any skill has errors. With `--strict`, warnings also fail.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import typer
import yaml

from ailayer.console import console, err, info, ok, warn
from ailayer.library import Skill, get_skill, list_skills

lint_app = typer.Typer(help="Lint library content against schema.")


# ── schema constants ─────────────────────────────────────────────────────────

CANONICAL_CATEGORIES = {
    "Coding Assistant",
    "Memory",
    "Agents & Automation",
    "Methodology",
    "Domain",
    "CLI Tooling",
    "MCP",
    "Hooks",
    "Marketplace",
    "Writing",
    "Data",
    "Other",
}

VALID_SAFETY_LEVELS = {"low", "medium", "high"}

SETUP_SYNONYMS = {"setup", "install", "installation"}
USE_SYNONYMS = {"use", "usage", "how it works in practice", "recipes"}
VERIFY_SYNONYMS = {"verify", "verification", "confirm"}

REQUIRED_FRONTMATTER_KEYS = {"name", "description", "category"}
RECOMMENDED_FRONTMATTER_KEYS = {"triggers", "safety"}

DESCRIPTION_MAX_CHARS = 120
WORD_COUNT_MIN = 200
WORD_COUNT_MAX = 800


# ── result types ─────────────────────────────────────────────────────────────


@dataclass
class LintResult:
    skill_name: str
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def is_clean(self) -> bool:
        return not self.errors and not self.warnings

    @property
    def has_errors(self) -> bool:
        return bool(self.errors)


# ── frontmatter parsing ──────────────────────────────────────────────────────


_FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n(.*)$", re.DOTALL)


def split_frontmatter(text: str) -> tuple[Optional[dict], str]:
    """Return (frontmatter_dict_or_None, body_text). None if no frontmatter."""
    match = _FRONTMATTER_RE.match(text)
    if not match:
        return None, text
    raw, body = match.group(1), match.group(2)
    try:
        data = yaml.safe_load(raw) or {}
        if not isinstance(data, dict):
            return None, text
    except yaml.YAMLError:
        return None, text
    return data, body


# ── section detection ────────────────────────────────────────────────────────


def find_h1_titles(body: str) -> list[str]:
    """Return all H1 (`# `) titles in body."""
    return [
        line[2:].strip()
        for line in body.splitlines()
        if line.startswith("# ") and not line.startswith("## ")
    ]


def find_h2_sections(body: str) -> set[str]:
    """Return lowercased H2 section names in body."""
    out: set[str] = set()
    for line in body.splitlines():
        if line.startswith("## "):
            out.add(line[3:].strip().lower())
    return out


def has_any(sections: set[str], synonyms: set[str]) -> bool:
    return any(s in sections for s in synonyms)


def word_count(body: str) -> int:
    """Approximate word count: split on whitespace, drop fenced code lines."""
    cleaned: list[str] = []
    in_fence = False
    for line in body.splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence:
            cleaned.append(line)
    return sum(len(line.split()) for line in cleaned)


# ── linter ───────────────────────────────────────────────────────────────────


def lint_skill(skill: Skill) -> LintResult:
    result = LintResult(skill_name=skill.name)
    prompt_path = skill.path / "SKILL_PROMPT.md"

    if not prompt_path.exists():
        result.warnings.append(
            "no SKILL_PROMPT.md (ailayer falls back to README — fix in Phase 1)"
        )
        return result

    text = prompt_path.read_text(encoding="utf-8")
    fm, body = split_frontmatter(text)

    # Frontmatter
    if fm is None:
        result.errors.append("frontmatter missing or unparseable")
    else:
        for key in REQUIRED_FRONTMATTER_KEYS:
            if key not in fm:
                result.errors.append(f"frontmatter missing required key: '{key}'")

        # name must equal directory name
        if "name" in fm and fm["name"] != skill.name:
            result.errors.append(
                f"frontmatter name '{fm['name']}' != directory name '{skill.name}'"
            )

        # description ≤ 120 chars
        desc = fm.get("description")
        if desc is not None:
            if not isinstance(desc, str):
                result.errors.append("frontmatter 'description' must be a string")
            elif len(desc) > DESCRIPTION_MAX_CHARS:
                result.errors.append(
                    f"frontmatter 'description' is {len(desc)} chars, max {DESCRIPTION_MAX_CHARS}"
                )

        # category in canonical set
        cat = fm.get("category")
        if cat is not None and cat not in CANONICAL_CATEGORIES:
            result.errors.append(
                f"frontmatter 'category' = '{cat}' is not in the canonical set "
                f"(see docs/SKILL_PROMPT_SCHEMA.md)"
            )

        # triggers must be list[str] if present
        triggers = fm.get("triggers")
        if triggers is not None:
            if not isinstance(triggers, list) or not all(isinstance(t, str) for t in triggers):
                result.errors.append("frontmatter 'triggers' must be a list of strings")

        # safety must be in enum if present
        safety = fm.get("safety")
        if safety is not None and safety not in VALID_SAFETY_LEVELS:
            result.errors.append(
                f"frontmatter 'safety' = '{safety}' must be one of {sorted(VALID_SAFETY_LEVELS)}"
            )

        for key in RECOMMENDED_FRONTMATTER_KEYS:
            if key not in fm:
                result.warnings.append(f"frontmatter missing recommended key: '{key}'")

    # H1 title
    h1s = find_h1_titles(body)
    if len(h1s) == 0:
        result.errors.append("no H1 title (expected `# <Title> skill`)")
    elif len(h1s) > 1:
        result.errors.append(f"multiple H1 titles found ({len(h1s)}); expected exactly one")

    # Sections
    sections = find_h2_sections(body)
    if "avoid" not in sections:
        result.errors.append("missing required section: `## Avoid`")
    if not has_any(sections, SETUP_SYNONYMS):
        result.warnings.append(
            f"missing recommended section: `## Setup` (or {sorted(SETUP_SYNONYMS - {'setup'})})"
        )
    if not has_any(sections, USE_SYNONYMS):
        result.warnings.append(
            f"missing recommended section: `## Use` (or {sorted(USE_SYNONYMS - {'use'})})"
        )
    if not has_any(sections, VERIFY_SYNONYMS):
        result.warnings.append(
            f"missing recommended section: `## Verify` (or {sorted(VERIFY_SYNONYMS - {'verify'})})"
        )

    # Word count
    wc = word_count(body)
    if wc < WORD_COUNT_MIN:
        result.warnings.append(f"word count {wc} below recommended minimum {WORD_COUNT_MIN}")
    elif wc > WORD_COUNT_MAX:
        result.warnings.append(f"word count {wc} above recommended maximum {WORD_COUNT_MAX}")

    return result


# ── reporting ────────────────────────────────────────────────────────────────


def _print_result(result: LintResult) -> None:
    if result.is_clean:
        ok(f"[skill]{result.skill_name}[/skill] — clean")
        return

    if result.has_errors:
        err(f"[skill]{result.skill_name}[/skill] — {len(result.errors)} error(s), "
            f"{len(result.warnings)} warning(s)")
    else:
        warn(f"[skill]{result.skill_name}[/skill] — {len(result.warnings)} warning(s)")

    for e in result.errors:
        console.print(f"    [red]✗[/red] {e}")
    for w in result.warnings:
        console.print(f"    [yellow]![/yellow] {w}")


# ── command ──────────────────────────────────────────────────────────────────


@lint_app.command("skills")
def lint_skills_cmd(
    name: Optional[str] = typer.Argument(None, help="Lint a single skill by name (default: all)."),
    strict: bool = typer.Option(False, "--strict", help="Treat warnings as errors."),
) -> None:
    """Validate SKILL_PROMPT.md files against the schema."""
    if name:
        skill = get_skill(name)
        if skill is None:
            err(f"Skill '{name}' not found in the library.")
            raise typer.Exit(1)
        skills = [skill]
    else:
        skills = list_skills()

    results = [lint_skill(s) for s in skills]
    for r in results:
        _print_result(r)

    n_errors = sum(len(r.errors) for r in results)
    n_warnings = sum(len(r.warnings) for r in results)
    n_clean = sum(1 for r in results if r.is_clean)

    info(
        f"\nSummary: {len(results)} skill(s) checked — "
        f"{n_clean} clean, {n_errors} error(s), {n_warnings} warning(s)."
    )

    fail = n_errors > 0 or (strict and n_warnings > 0)
    raise typer.Exit(1 if fail else 0)
