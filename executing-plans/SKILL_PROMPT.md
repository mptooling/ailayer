---
name: executing-plans
description: Drive a written plan one phase at a time, with a test gate at each boundary and a confirm-pause before the next phase.
category: Methodology
triggers: [execute plan, run plan, phase, implement plan, do, drive plan, phased execution]
safety: low
version: 2026-05-09
homepage: https://github.com/obra/superpowers
---

# Executing-plans skill

Use this skill **whenever the work is driven by a written plan** — typically produced by `writing-plans`, but also applicable to a GitHub issue with a phased checklist, a PRD, or any external artefact that names phases. The skill enforces phase-by-phase execution with a confirm-pause between phases.

If there is no plan, this skill does not apply — write one (`writing-plans`) or proceed without phasing.

## Setup

No install. Behavioural — the agent reads this and adopts the discipline. The plan being executed must already be **confirmed** by the user (per `writing-plans`); an unconfirmed plan isn't a contract and shouldn't drive execution.

## Use

Execute one phase per turn. Never skip ahead.

For each phase:

1. **State the phase.** Echo the phase title and goal back. This is a sanity check that the executor and the plan are aligned.
2. **Implement only that phase.** No peeking ahead. No "while I'm here" edits to other phases. No refactoring outside the phase's file list.
3. **Run the test gate.** Use the exact command from the plan. Paste the output:

   ```text
   $ <test command>
   <output>
   exit: <code>
   ```

4. **Check for collateral damage.** Re-run the broader test suite (or relevant slice). If anything *outside* this phase's scope regressed, that's a planning error — stop, report, decide whether to roll back or amend the plan.
5. **Stop.** Print: `Phase N complete. Confirm to continue to Phase N+1?` Wait for explicit confirmation. Do not proceed.

After all phases pass, run the final verification (per `verification-before-completion`) and report the plan as complete.

When the user explicitly waives the confirm-pause ("just run all phases"), comply — but flag that you're running unsupervised so the user owns the trade-off.

## Avoid

- **Implementing multiple phases in one turn.** This is the failure mode this skill exists to prevent. Phase boundaries are review boundaries — collapsing them defeats the plan.
- **Pre-implementing phase N+1 "because it's quick."** That's a different change. Park it; the next phase will absorb it cleanly.
- **Skipping the test gate** when "the plan said it should pass." Run it. Paste it.
- **Treating a missed test gate as a planning error without checking.** First re-isolate (per `systematic-debugging`) — sometimes the gate is right and the implementation is wrong.
- **Auto-confirming on the user's behalf.** "Continuing to phase 4 since the previous one passed" is forbidden unless the user explicitly waived the pause.
- **Editing the plan mid-execution.** If reality contradicts the plan, *stop, report, and re-plan*. Don't silently amend.
- **Trying to roll back into an inconsistent state.** If a phase mutates external state (DB migration, deploy, file delete) and the rollback is non-trivial, halt and ask before reverting.

## Verify

A plan was executed under this skill if the conversation transcript shows, for every phase:

- The phase title echoed.
- The diff or summary of the changes.
- The test-gate command + output.
- A `Phase N complete. Confirm to continue?` pause.
- An explicit user confirmation before phase N+1.

If any of those is missing for any phase, the discipline broke. Either restart the affected phase, or call out the gap explicitly so the user knows what wasn't reviewed.
