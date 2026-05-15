# AGENTS.md

This file provides guidance to Codex when working in this repository.

## Repository Purpose

This repo is a curated library of AI tools, agent skills, and practical workflow tips. Top-level directories each contain a single `README.md` profile. `INDEX.md` is the master catalog grouped by audience and use case.

There is no separate automation product. Treat Markdown content as the product.

## Entry README Format

Each top-level entry should keep category metadata near the top:

`> **Category:** ... | **Type:** ... | **Audience:** ...`

The first normal paragraph should be a concise human-readable summary. Recommended sections are `When To Use`, `Practical Tips`, `Watch Outs`, and `Links`.

For methodology skills, `How To Apply` can replace `Practical Tips` when the entry is about a workflow rather than a vendor tool.

## Editing Rules

- Do not add automation code or package scaffolding unless the product direction changes again.
- Keep entries practical and short.
- Update `INDEX.md` whenever an entry is added, removed, renamed, or recategorized.
- Prefer verified current facts for pricing, star counts, and product availability.
- Preserve useful commands, workflows, and caveats when simplifying an entry.

## Superpowers Workflow

After the library-only refactor, use Superpowers skills as the default collaboration workflow for non-trivial changes:

- `brainstorming`: use before adding new categories, changing taxonomy, or redesigning entry format.
- `writing-plans`: use before broad refactors that touch many entries.
- `verification-before-completion`: use before reporting that documentation cleanup is complete.
- `systematic-debugging`: use when validation scripts, link checks, or generated outputs fail.

Do not reintroduce a separate automation product as part of Superpowers enablement. Superpowers is contributor workflow guidance for maintaining the Markdown library.
