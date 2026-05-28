# Matt Pocock — Skills for Real Engineers

> **Category:** Methodology Skills (collection) | **Type:** Open Source (MIT) skill pack | **Audience:** Engineers using Claude Code and other coding agents

---

## Repository

- [GitHub — mattpocock/skills](https://github.com/mattpocock/skills) ⭐ 109,000+
- Author: Matt Pocock — "Skills for Real Engineers. Straight from my `.claude` directory."
- License: MIT

---

## Summary

A curated, opinionated collection of agent skills pulled straight from Matt Pocock's own `.claude` setup, aimed at real engineering work rather than quick prototyping. The skills target four recurring failure modes of coding agents — misalignment with intent, verbose output, buggy code, and architectural decay — and counter them with shared domain language, tight feedback loops, small deliberate steps, and continuous design investment. They're model-agnostic and work with Claude Code and similar agents. Notable engineering skills include `grill-with-docs` (clarify requirements into a shared-language `CONTEXT.md`), `tdd`, `diagnose` (structured debugging loop), `improve-codebase-architecture`, and `to-prd` / `to-issues` (turn context into specs and trackable issues). Productivity skills include `grill-me` (intensive plan interrogation), `caveman` (token-compressed communication), `handoff` (document a session for the next agent), and `write-a-skill`.

**Best for:** Teams that want a battle-tested, ready-to-install set of workflow skills covering planning, requirements, TDD, debugging, and architecture — installable in one command rather than authored from scratch.

---

## Related Materials

This library's methodology skills overlap with and cross-reference several skills here; use this collection for the broader, regularly-updated source:

- [Brainstorming](../brainstorming/README.md) — compare with `grill-me` / `grill-with-docs`
- [TDD](../tdd/README.md) — compare with this pack's `tdd`
- [Systematic Debugging](../systematic-debugging/README.md) — compare with `diagnose`
- [Writing Plans](../writing-plans/README.md) / [Executing Plans](../executing-plans/README.md) — compare with `to-prd` / `to-issues`
- [Caveman](../caveman/README.md) — the same token-compression idea as this pack's `caveman`
- [Everything Claude Code](../everything-claude-code/README.md) — another multi-skill collection for coding agents

---

## When To Use

- You want a vetted, install-ready set of workflow skills instead of writing your own for planning, requirements, TDD, debugging, and architecture.
- Your agent sessions suffer from misalignment, verbosity, bugs, or architectural drift, and you want skills designed specifically to counter those.
- You want a shared, opinionated baseline across a team that you can selectively adopt.

## How To Apply

- Install selectively: `npx skills@latest add mattpocock/skills`, pick the skills you actually need, then run `/setup-matt-pocock-skills` to wire up issue tracking, triage labels, and docs locations.
- Lead with `grill-with-docs` on new work so the agent and you agree on domain language and a `CONTEXT.md` before code is written.
- Pair `to-prd` → `to-issues` to go from a conversation to a spec to grabbable issues; use `tdd` and `diagnose` during implementation.
- Use `handoff` at the end of a long session so the next agent (or you, tomorrow) starts with full context.
- Treat it as a source to learn from: read a `SKILL.md` to see how a well-structured skill is written, then adapt rather than copy wholesale.

## Watch Outs

- Opinionated by design — these encode one engineer's preferred workflow; review each skill before standardizing it across a team.
- Skills under `deprecated/` and `in-progress/` are unfinished or superseded; stick to `engineering/`, `productivity/`, and `misc/` for production use.
- Overlap with this library's own methodology skills and with Everything Claude Code; installing everything can duplicate behavior — pick one source per workflow.
- `setup-` and git-guardrail skills touch repo config and hooks; review what they change before running on a real repository.
- Fast-moving personal repo; pin or re-review after pulling updates, as skills are added, renamed, and deprecated frequently.

---

## Links

- [GitHub — mattpocock/skills](https://github.com/mattpocock/skills)
- [`skills` CLI install](https://github.com/mattpocock/skills#installation)
- [Engineering skills](https://github.com/mattpocock/skills/tree/main/skills/engineering)
- [Productivity skills](https://github.com/mattpocock/skills/tree/main/skills/productivity)

---

*Last updated: 2026-05*
