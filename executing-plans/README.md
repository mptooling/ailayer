# Executing Plans — phase-by-phase plan-driver skill

> **Category:** Methodology | **License:** MIT | **Type:** Cross-CLI agent skill (Claude Code, Codex CLI, Gemini CLI)

A skill that drives a written plan (typically the output of [`writing-plans`](../writing-plans/README.md)) one phase at a time, pausing at each phase boundary for user confirmation. Distilled from `obra/superpowers:executing-plans` and the multi-agent orchestration patterns in `wshobson/agents:conductor` and `mattpocock/skills:do`.

## What it is

A plan is only useful if the executor follows it. The common failure mode is: agent reads the plan, mentally collapses it, then "implements the whole thing" in one heroic burst — at which point any phase-boundary review is moot. This skill prevents that.

The executor:

1. Reads phase 1 from the plan.
2. Implements **only that phase** (no peeking ahead, no pre-implementing future phases).
3. Runs the test gate and pastes the result.
4. Runs the rollback if anything outside the phase regresses.
5. **Stops** and asks the user to confirm before moving to phase 2.
6. Repeats until the plan is done.

The discipline is the pause. Without it, plans degenerate into long todo lists the agent races through and the user audits in retrospect.

## Why it ships in this library

`obra/superpowers:executing-plans` is Claude-Code-only. The wshobson and mattpocock equivalents ship in their own packs. To get the same discipline portably across Claude Code, Codex CLI, and Gemini CLI via `ailayer`, the skill needs a self-contained, model-agnostic version. That's what's in `SKILL_PROMPT.md`.

## What good looks like

A phase turn looks like this:

```text
Phase N — <title>
  Implementing…
  <diff or summary>

Test gate:
  $ <command>
  <output>
  exit: 0

Phase N complete. Confirm to continue to Phase N+1?
```

The executor never proceeds past the confirmation prompt without an affirmative reply.

## Reference

- [`obra/superpowers/executing-plans`](https://github.com/obra/superpowers).
- [`wshobson/agents:conductor`](https://github.com/wshobson/agents) — same idea, embedded in a multi-agent framework.
- [`mattpocock/skills/to-issues`](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-issues/SKILL.md) — at the per-issue level.

## Compose-with

- `writing-plans` (Phase 2) — produces the plan this skill drives.
- `tdd` (Phase 2) — each phase's test gate is a TDD red→green loop.
- `verification-before-completion` (Phase 2) — gates the final phase before "done."
- `dispatching-parallel-agents` (Phase 2 upcoming) — fan-out for *independent* phases when the plan supports it.

## Which AI agents integrate

Any agent that loads Markdown skills/slash-commands. `ailayer add skill executing-plans --tool all` injects it into Claude Code, Codex CLI, and Gemini CLI in one shot.
