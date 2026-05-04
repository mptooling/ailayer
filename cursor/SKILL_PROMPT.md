# Cursor skill

Use this skill when authoring Cursor-specific project rules or configuring a repo for Cursor users.

## Project rules

- Modern Cursor reads rules from `.cursor/rules/*.mdc` (multiple scoped files) — *prefer this over* the legacy single `.cursorrules` file.
- Each `.mdc` file has YAML frontmatter: `description`, `globs` (file patterns the rule applies to), and `alwaysApply` (boolean). The body is the rule prompt.
- Scope rules tightly with `globs`: a Python style rule with `globs: ["**/*.py"]` will only load when Python files are in context, saving budget for other rules.

## What rules should contain

- Imperative project conventions: "Use `pyproject.toml` for deps, never `requirements.txt`." "All HTTP handlers return `Response[T]`, never raw dicts."
- Pointers to authoritative files: "When editing migrations, read `db/SCHEMA.md` first."
- Forbidden patterns with reasons: "Do not catch `Exception:` — log and re-raise typed errors. Reason: silent failures in prod last quarter."

## What rules should NOT contain

- Marketing copy or tool descriptions ("Cursor is great for...").
- Generic advice the model already knows ("write clean code", "add docstrings").
- Information already discoverable from the code (file paths, function signatures).

## Composer / Agent mode

- For multi-file edits, instruct the user to use Composer (Cmd+I); for single-file edits, inline chat (Cmd+K). Rules apply to both.
- Use `@file`, `@folder`, `@docs`, `@web` references inside chat to pin context — don't rely on the indexer alone for cross-file changes.

## Avoid

- One giant `.cursorrules` file in 2026 — it loads on every prompt regardless of relevance and crowds out file context.
- Encoding security policy *only* in Cursor rules; rules are advisory to the model. Pair with linters and CI checks for anything that must be enforced.
