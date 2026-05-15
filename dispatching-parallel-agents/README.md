# Dispatching Parallel Agents — fan-out-to-sub-agents skill

> **Category:** Methodology | **License:** MIT | **Type:** Workflow skill

A skill that recognises when work *can* be split across parallel sub-agents and dispatches it in a single turn, instead of serialising independent tasks. Distilled from `obra/superpowers:dispatching-parallel-agents` and the multi-agent orchestration patterns in `wshobson/agents:conductor`.

## What it is

The default failure mode for capable agents is to run *every* sub-task sequentially — read file A, then read file B, then grep for X — even when the calls share no state and could fan out. This skill flips that default: when 2+ tasks are *truly* independent (no shared mutable state, no order dependency, no dependent values), they go out in one batch.

Three rules govern dispatch:

1. **Independence test.** Before fanning out, the agent states explicitly what each sub-agent owns and confirms that no output of one is an input to another. If that fails, the work stays sequential.
2. **One message, multiple tool calls.** Parallel work is dispatched in a single assistant turn. Splitting fan-out across turns negates the savings.
3. **Each sub-agent gets a self-contained brief.** Sub-agents don't see the parent conversation; the brief must include enough context that the sub-agent can act without follow-up questions.


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


---

## When To Use

- If the work has *any* dependency between sub-tasks — output of A feeds input of B, both write to the same file, one decides whether the other runs — do **not** parallelise. Stay sequential.

## How To Apply

- No install. Behavioural — the agent reads this and adopts the discipline.
- Before dispatching, run the independence test in writing:
- Parallel plan:
- Sub-task A — <one-line goal>; inputs <list>; outputs <list>
- Sub-task B — <one-line goal>; inputs <list>; outputs <list>
- Sub-task C — …
- Independence check:
- No output of A is an input of B/C? ✓

## Watch Outs

- **Serial calls that could be parallel.** Reading three independent files one after the other in three separate turns is the canonical waste this skill exists to prevent.
- **Parallelising work with hidden dependencies.** "Both sub-agents will edit the same config file" is a write-write collision waiting to happen. Run the independence check honestly — if in doubt, sequential.
- **Vague briefs.** "Look at the auth code and report back" wastes a sub-agent. Briefs name files, name questions, name output shape, and cap length.
- **Dispatching without synthesising.** The parent must combine the sub-agent results; pasting raw outputs back is not an answer.
- **Fanning out for cosmetic speed.** Two trivial Reads avoid need sub-agents — direct tool calls in one turn are faster and cheaper. Sub-agent dispatch is for work substantial enough to justify the context cost.
- **Forgetting that sub-agents have no memory.** A sub-agent doesn't see prior turns or the user's preferences. The brief must carry everything the sub-agent needs.
