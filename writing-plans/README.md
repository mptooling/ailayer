# Writing Plans — spec-to-phased-plan skill

> **Category:** Methodology | **License:** MIT | **Type:** Cross-CLI agent skill (Claude Code, Codex CLI, Gemini CLI)

A skill that turns a confirmed brief (typically the output of `brainstorming`) into a numbered, phased plan a separate execution session can run against. Distilled from `obra/superpowers:writing-plans`, [`mattpocock/skills:to-prd`](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-prd/SKILL.md), and the multi-step task-management patterns in `wshobson/agents:conductor`.

Pairs with [`executing-plans`](../executing-plans/README.md) — writing produces the plan, executing drives it.

## What it is

Big tasks fail because they're attempted as a blob. The plan-writer breaks the work into phases, each with: files to touch, the failing test that proves the phase is done, rollback notes, and a one-line summary. The plan is a *contract* — once confirmed, the executor follows it phase by phase, pausing for review at each boundary.

The skill is opinionated about three things:

1. **Phases are vertical slices**, not architectural layers. Each phase ships independently usable behaviour.
2. **Each phase has a test gate** that proves it's done. No verification gate → the phase isn't ready to plan.
3. **Plans are written, not implied.** They live in a file (`PLAN.md`, a GitHub issue, etc.) so the executor and any reviewer share the same artefact.

## Why it ships in this library

The `superpowers` and `mattpocock` versions are Claude-Code-only or pack-bound. To get plan→execute discipline portably across Claude Code, Codex CLI, and Gemini CLI via `ailayer`, we need a self-contained, model-agnostic version. That's what's in `SKILL_PROMPT.md`.

## What good looks like

A plan looks like this:

```text
PLAN: <one-sentence goal>

Phase 1 — <slice title>
  Goal: <user-visible outcome>
  Files: <list>
  Test gate: <command + assertion>
  Rollback: <how to undo>

Phase 2 — …
```

Five to nine phases is typical. More than that, the work is too big — split into separate plans. Fewer than two, the work doesn't need a plan.

## Reference

- [`obra/superpowers/writing-plans`](https://github.com/obra/superpowers).
- [`mattpocock/skills/to-prd`](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-prd/SKILL.md).
- [`mattpocock/skills/to-issues`](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-issues/SKILL.md) — same pattern at a finer grain (per-issue rather than per-phase).

## Compose-with

- `brainstorming` (Phase 2) — produces the brief this skill turns into a plan.
- `executing-plans` (Phase 2) — drives the plan with checkpoint reviews.
- `tdd` (Phase 2) — each phase's test gate is a TDD red→green pair.

## Which AI agents integrate

Any agent that loads Markdown skills/slash-commands. `ailayer add skill writing-plans --tool all` injects it into Claude Code, Codex CLI, and Gemini CLI in one shot.
