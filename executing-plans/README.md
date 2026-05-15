# Executing Plans — phase-by-phase plan-driver skill

> **Category:** Methodology | **License:** MIT | **Type:** Workflow skill

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
- `dispatching-parallel-agents` — fan-out for *independent* phases when the plan supports it.


---

## When To Use

- If there is no plan, this skill does not apply — write one (`writing-plans`) or proceed without phasing.

## How To Apply

- No install. Behavioural — the agent reads this and adopts the discipline. The plan being executed must already be **confirmed** by the user (per `writing-plans`); an unconfirmed plan isn't a contract and shouldn't drive execution.
- Execute one phase per turn. Avoid skip ahead.
- For each phase:
- **State the phase.** Echo the phase title and goal back. This is a sanity check that the executor and the plan are aligned.
- **Implement only that phase.** No peeking ahead. No "while I'm here" edits to other phases. No refactoring outside the phase's file list.
- **Run the test gate.** Use the exact command from the plan. Paste the output:
- $ <test command>
- <output>

## Watch Outs

- **Implementing multiple phases in one turn.** This is the failure mode this skill exists to prevent. Phase boundaries are review boundaries — collapsing them defeats the plan.
- **Pre-implementing phase N+1 "because it's quick."** That's a different change. Park it; the next phase will absorb it cleanly.
- **Skipping the test gate** when "the plan said it should pass." Run it. Paste it.
- **Treating a missed test gate as a planning error without checking.** First re-isolate (per `systematic-debugging`) — sometimes the gate is right and the implementation is wrong.
- **Auto-confirming on the user's behalf.** "Continuing to phase 4 since the previous one passed" is forbidden unless the user explicitly waived the pause.
- **Editing the plan mid-execution.** If reality contradicts the plan, *stop, report, and re-plan*. Don't silently amend.
