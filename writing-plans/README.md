# Writing Plans — spec-to-phased-plan skill

> **Category:** Methodology | **License:** MIT | **Type:** Workflow skill

A skill that turns a confirmed brief (typically the output of `brainstorming`) into a numbered, phased plan a separate execution session can run against. Distilled from `obra/superpowers:writing-plans`, [`mattpocock/skills:to-prd`](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-prd/SKILL.md), and the multi-step task-management patterns in `wshobson/agents:conductor`.

Pairs with [`executing-plans`](../executing-plans/README.md) — writing produces the plan, executing drives it.

## What it is

Big tasks fail because they're attempted as a blob. The plan-writer breaks the work into phases, each with: files to touch, the failing test that proves the phase is done, rollback notes, and a one-line summary. The plan is a *contract* — once confirmed, the executor follows it phase by phase, pausing for review at each boundary.

The skill is opinionated about three things:

1. **Phases are vertical slices**, not architectural layers. Each phase ships independently usable behaviour.
2. **Each phase has a test gate** that proves it's done. No verification gate → the phase isn't ready to plan.
3. **Plans are written, not implied.** They live in a file (`PLAN.md`, a GitHub issue, etc.) so the executor and any reviewer share the same artefact.


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

- `brainstorming` — produces the brief this skill turns into a plan.
- `executing-plans` — drives the plan with checkpoint reviews.
- `tdd` — each phase's test gate is a TDD red→green pair.


---

## When To Use

- If the work is one phase — a single edit + verification — skip planning and go straight to implementation.

## How To Apply

- No install. The skill is behavioural — the agent reads it and produces a plan in the conversation, then offers to write it to a file.
- Where plans live:
- Long-running work in a repo: `PLAN.md` at the root, or `docs/plans/<slug>.md`.
- Issue-driven work: a GitHub / Linear / Jira issue body.
- Quick session-scoped work: inline in the conversation, no file.
- Produce a plan with this shape:
- PLAN: <one-sentence goal>
- Context:

## Watch Outs

- **Planning in the abstract.** Phrases like "design a robust system for X" are not phases. Be concrete: which files, which functions, which test.
- **Architectural layers as phases.** "Phase 1: types. Phase 2: repository. Phase 3: service. Phase 4: controller. Phase 5: UI." This produces five phases of dead code that all integrate at the end and explode. Vertical slices.
- **More than 9 phases in one plan.** That's not a plan, it's a project. Split it.
- **Optimistic test gates.** "All tests pass" is not a gate; *which* test, on *what* command, asserting *what*. Be specific.
- **Writing the plan and starting to execute in the same turn.** Two skills, two turns. The user signs off between them.
- **Re-planning mid-execution without reverting unfinished phases.** If scope changes, *finish or roll back the current phase first*, then re-plan from the next.
