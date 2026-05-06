# `SKILL_PROMPT.md` schema

Authoritative spec for the agent-oriented skill files in this library. Every `<tool>/SKILL_PROMPT.md` MUST conform — `ailayer lint skills` enforces it.

The reader is an AI coding agent (Claude Code, Codex CLI, Gemini CLI). The file is its instructions for using one tool/library/methodology. Optimise for **brevity, concrete commands, and clear "do/don't" guidance** — not marketing prose.

---

## File layout

```markdown
---
name: <slug>
description: <one-line summary, ≤120 chars>
category: <category-name>
triggers: [<keyword>, <keyword>, ...]
safety: <low|medium|high>
version: <YYYY-MM-DD>
homepage: <URL>
---

# <Title> skill

<Optional one-paragraph framing — when to reach for this skill, when not.>

## Setup

<Install / auth / one-time configuration. Concrete commands, not vibes.>

## Use

<Day-to-day usage patterns. Common recipes the agent will repeat.>

## Avoid

<Footguns. Things the agent must NOT do, with the reason.>

## Verify

<How the agent confirms its change is correct — exact build/test/lint commands.>
```

---

## Frontmatter

YAML, delimited by `---` lines. Required keys are **errors** (linter exit non-zero). Recommended keys are **warnings**.

| Key | Required? | Type | Constraints |
|---|---|---|---|
| `name` | required | string | Kebab-case slug. **Must equal the parent directory name.** |
| `description` | required | string | One line, ≤120 chars, displayed in `ailayer list skills`. |
| `category` | required | string | One of the canonical categories below. |
| `triggers` | recommended | list[string] | Keywords that should make an agent reach for this skill (e.g. `[postgres, indexing, query-plan]`). |
| `safety` | recommended | enum | `low` (read-only / advisory), `medium` (writes files, runs lint), `high` (deploys, mutates external state, handles secrets). Defaults to `low` if omitted. |
| `version` | optional | date | `YYYY-MM-DD` of last meaningful update. |
| `homepage` | optional | URL | Tool/library website if one exists. |

### Canonical categories

Pick the closest fit. Linter enforces the set.

- `Coding Assistant` — IDE / editor agents (Cursor, Copilot, Continue, Aider, Windsurf, Caveman).
- `Memory` — cross-session memory / context (Claude-Mem, etc.).
- `Agents & Automation` — agent frameworks (LangChain, LangGraph, CrewAI, AutoGPT, n8n).
- `Methodology` — workflow skills (TDD, brainstorming, plans, debugging, verification).
- `Domain` — domain knowledge skills (Postgres, Terraform, OpenAPI, security review, GraphQL, releases).
- `CLI Tooling` — command-line helpers (rg/fd/ast-grep, jq/yq, gh, repomix, difftastic).
- `MCP` — MCP server profiles.
- `Hooks` — hook bundle profiles.
- `Marketplace` — plugin marketplace profiles.
- `Writing` — content / marketing tools.
- `Data` — analytics / BI tools.
- `Other` — escape hatch; prefer something more specific.

---

## Document structure

| Element | Required? | Notes |
|---|---|---|
| H1 title | required | Single `# <Title> skill` heading. Linter errors if missing or duplicated. |
| Framing paragraph | optional | One paragraph between H1 and the first H2. Helps agents decide whether to invoke the skill. |
| `## Setup` | recommended | Linter warns if missing. May be replaced by `## Install` for tools with no auth/config. |
| `## Use` | recommended | Linter warns if missing. May be split into multiple H2s if needed. |
| `## Avoid` | required | Footguns are non-negotiable. Linter errors if missing. |
| `## Verify` | recommended | Linter warns if missing. Advisory skills may legitimately omit it; methodology skills usually have it. |

Section synonyms accepted by the linter (don't add new ones unless the schema is updated):

- `## Setup` ≡ `## Install` ≡ `## Installation`
- `## Use` ≡ `## Usage` ≡ `## How it works in practice` ≡ `## Recipes`
- `## Verify` ≡ `## Verification` ≡ `## Confirm`

---

## Style guidance

Not enforced by the linter, but expected during review.

- **Lead with commands.** "Run `npm install foo` then …" beats "First, install the package."
- **No marketing copy.** The README has it; `SKILL_PROMPT.md` is for the agent.
- **Concrete defaults.** Show the canonical config, not "configure as needed."
- **Cite versions.** "Tested with `foo@2.4.x`." Pin where it matters.
- **Word budget: 200–800 words.** Longer than 800 = consider splitting; shorter than 200 = probably under-specified.
- **No emojis.**

---

## Rendering rules (`ailayer`)

When `ailayer add skill <name>` injects the file:

1. **Frontmatter is stripped before injection** for Claude Code (markdown skills don't expect YAML headers).
2. **For Gemini CLI**, the adapter converts: `description` → TOML `description = "..."`, body → TOML `prompt = """..."""`. The H1 line becomes the first line of `prompt`.
3. **For Codex CLI**, the file is copied verbatim to `~/.codex/skills/<name>/SKILL.md` (frontmatter preserved — Codex skills accept it).
4. The `_ailayer:<label>` section markers used elsewhere don't apply here — skills live in dedicated files, not inside instruction documents.

If you're adding adapter logic, treat this schema as the single source of truth. If a tool's native format conflicts (e.g. a key isn't accepted), the adapter must translate, not the skill author.

---

## Validation: `ailayer lint skills`

Run from the repo root (or anywhere with `AILAYER_LIBRARY` set). Exits non-zero if **any** skill has errors.

```bash
ailayer lint skills            # Lint every skill in the library
ailayer lint skills cursor     # Lint just one
ailayer lint skills --strict   # Treat warnings as errors
```

Output is per-skill and grouped by severity. Errors must be fixed before merge; warnings are best-effort.

### What the linter checks

| Check | Severity |
|---|---|
| `SKILL_PROMPT.md` exists for every library entry | warning |
| Frontmatter is parseable YAML | error |
| `name` matches the directory | error |
| `description` exists and is ≤120 chars | error |
| `category` is in the canonical set | error |
| `triggers` (if present) is a list of strings | error |
| `safety` (if present) is `low`/`medium`/`high` | error |
| H1 title exists exactly once | error |
| `## Avoid` section exists | error |
| `## Setup`/`## Use`/`## Verify` sections (or accepted synonyms) exist | warning |
| Word count between 200–800 | warning |
