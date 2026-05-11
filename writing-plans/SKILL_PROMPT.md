---
name: writing-plans
description: Turn a confirmed brief into a numbered phased plan with file lists, test gates, and rollback notes.
category: Methodology
triggers: [plan, planning, phase, breakdown, decompose, prd, spec, multi-step, implementation plan]
safety: low
version: 2026-05-09
homepage: https://github.com/obra/superpowers
---

# Writing-plans skill

Use this skill **after a brief is confirmed and before writing code** for any task that won't fit in a single short edit. The output is a written, phased plan that an execution session (or a sub-agent, or another engineer) can run against without re-deriving intent.

If the work is one phase — a single edit + verification — skip planning and go straight to implementation.

## Setup

No install. The skill is behavioural — the agent reads it and produces a plan in the conversation, then offers to write it to a file.

Where plans live:

- Long-running work in a repo: `PLAN.md` at the root, or `docs/plans/<slug>.md`.
- Issue-driven work: a GitHub / Linear / Jira issue body.
- Quick session-scoped work: inline in the conversation, no file.

## Use

Produce a plan with this shape:

```text
PLAN: <one-sentence goal>

Context:
- Brief / spec link
- Constraints (deadlines, budgets, non-negotiables)
- What the executor MUST NOT do

Phase 1 — <vertical-slice title>
  Goal: <one-line user-visible outcome>
  Files: <comma-separated list of files to create/modify>
  Test gate: <exact command + expected pass>
  Rollback: <how to undo this phase if Phase 2 surfaces a problem>

Phase 2 — …
…
Phase N — Verify and ship
  Goal: full verification suite + docs/changelog updates
  Files: README, CHANGELOG, etc.
  Test gate: full test suite green; lint clean; typecheck clean
  Rollback: revert merge
```

Rules for phases:

- **Vertical slices, not horizontal layers.** Each phase delivers user-visible behaviour. "Add database column" is not a phase; "feature X works for users with property Y" is.
- **5–9 phases**, typically. More than 9 → split into multiple plans (or rethink scope). Fewer than 2 → no plan needed.
- **Every phase has a test gate.** The exact command + the assertion it proves. Not "tests pass" but "`pnpm vitest run path/to/foo` passes the new `should X` case."
- **Every phase has a rollback note.** "Revert this commit" is fine when honest; "revert + drop column" is required when DB migration is irreversible.
- **List files explicitly.** A reviewer should be able to predict the diff.

After producing the plan, **ask the user to confirm or edit it.** Do not start executing. The plan is a contract; an unconfirmed contract isn't a contract.

## Avoid

- **Planning in the abstract.** Phrases like "design a robust system for X" are not phases. Be concrete: which files, which functions, which test.
- **Architectural layers as phases.** "Phase 1: types. Phase 2: repository. Phase 3: service. Phase 4: controller. Phase 5: UI." This produces five phases of dead code that all integrate at the end and explode. Vertical slices.
- **More than 9 phases in one plan.** That's not a plan, it's a project. Split it.
- **Optimistic test gates.** "All tests pass" is not a gate; *which* test, on *what* command, asserting *what*. Be specific.
- **Writing the plan and starting to execute in the same turn.** Two skills, two turns. The user signs off between them.
- **Re-planning mid-execution without reverting unfinished phases.** If scope changes, *finish or roll back the current phase first*, then re-plan from the next.
- **Burying constraints in prose.** Put hard constraints in a top-level "Context: MUST NOT" list so the executor can't miss them.

## Verify

A plan is well-formed if a reader who hasn't seen the brief can answer:

- What's the goal in one sentence?
- How many phases? Each one a vertical slice?
- For phase N: which files, which test command, how to roll back?
- What is explicitly out of scope?

If any of those is fuzzy, revise the plan before handing it to the executor.
