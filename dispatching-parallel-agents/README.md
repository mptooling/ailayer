# Dispatching Parallel Agents — fan-out-to-sub-agents skill

> **Category:** Methodology | **License:** MIT | **Type:** Cross-CLI agent skill (Claude Code, Codex CLI, Gemini CLI)

A skill that recognises when work *can* be split across parallel sub-agents and dispatches it in a single turn, instead of serialising independent tasks. Distilled from `obra/superpowers:dispatching-parallel-agents` and the multi-agent orchestration patterns in `wshobson/agents:conductor`.

## What it is

The default failure mode for capable agents is to run *every* sub-task sequentially — read file A, then read file B, then grep for X — even when the calls share no state and could fan out. This skill flips that default: when 2+ tasks are *truly* independent (no shared mutable state, no order dependency, no dependent values), they go out in one batch.

Three rules govern dispatch:

1. **Independence test.** Before fanning out, the agent states explicitly what each sub-agent owns and confirms that no output of one is an input to another. If that fails, the work stays sequential.
2. **One message, multiple tool calls.** Parallel work is dispatched in a single assistant turn. Splitting fan-out across turns negates the savings.
3. **Each sub-agent gets a self-contained brief.** Sub-agents don't see the parent conversation; the brief must include enough context that the sub-agent can act without follow-up questions.

## Why it ships in this library

The `superpowers` version is Claude-Code-only (it talks specifically about the `Task` / `Agent` tool). The wshobson framework bundles parallel dispatch inside a larger conductor concept. To get the discipline portably across Claude Code, Codex CLI, and Gemini CLI via `ailayer`, the skill needs a self-contained, model-agnostic version — keyed on the *principle* (independent work fans out in one turn) rather than any one tool's sub-agent API. That's what's in `SKILL_PROMPT.md`.

## What good looks like

A parallel-dispatch turn looks like this:

```text
Plan: three independent reads — no shared state, no ordering.

  → sub-agent A: summarise src/auth/*.ts
  → sub-agent B: summarise src/billing/*.ts
  → sub-agent C: list all migrations under db/migrations/

(single turn, three tool calls in parallel)
```

A non-example: "first read auth, then based on what I find, decide whether to read billing." That has an ordering dependency — sequential.

## Reference

- [`obra/superpowers/dispatching-parallel-agents`](https://github.com/obra/superpowers).
- [`wshobson/agents:conductor`](https://github.com/wshobson/agents) — parallel dispatch embedded in a multi-agent framework.
- [`mattpocock/skills:to-issues`](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-issues/SKILL.md) — parallel-friendly issue decomposition.

## Compose-with

- `writing-plans` (Phase 2) — produces the plan whose *independent* phases this skill can fan out.
- `executing-plans` (Phase 2) — drives dependent phases sequentially; defers to this skill for independent ones.
- `using-git-worktrees` (Phase 2) — when parallel agents touch the same repo, isolate each in its own worktree to prevent collisions.

## Which AI agents integrate

Any agent that supports concurrent tool calls or sub-agent dispatch in a single turn. `ailayer add skill dispatching-parallel-agents --tool all` injects it into Claude Code, Codex CLI, and Gemini CLI in one shot.
