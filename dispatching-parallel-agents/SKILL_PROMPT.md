---
name: dispatching-parallel-agents
description: Fan out 2+ truly independent tasks to parallel sub-agents in one turn; never serialise work that has no shared state.
category: Methodology
triggers: [parallel, fan out, dispatch, sub-agent, concurrent, batch, in parallel, multi-agent]
safety: low
version: 2026-05-09
homepage: https://github.com/obra/superpowers
---

# Dispatching-parallel-agents skill

Use this skill **before issuing 2+ tool calls or sub-agent dispatches** whenever the sub-tasks have no shared mutable state and no ordering dependency. The default for capable agents is to serialise; this skill flips that default to parallel — but only after passing the independence test.

If the work has *any* dependency between sub-tasks — output of A feeds input of B, both write to the same file, one decides whether the other runs — do **not** parallelise. Stay sequential.

## Setup

No install. Behavioural — the agent reads this and adopts the discipline.

The host runtime must support multiple tool calls in one assistant turn (Claude Code: parallel tool calls and `Task` / sub-agent dispatch; Codex CLI: concurrent shell calls; Gemini CLI: parallel tool calls). If the runtime does not, fall through to sequential execution.

## Use

Before dispatching, run the independence test in writing:

```text
Parallel plan:
  Sub-task A — <one-line goal>; inputs <list>; outputs <list>
  Sub-task B — <one-line goal>; inputs <list>; outputs <list>
  Sub-task C — …

Independence check:
  - No output of A is an input of B/C? ✓
  - No two sub-tasks write the same file / resource? ✓
  - No sub-task decides whether another runs? ✓
```

If every check is ✓, dispatch all sub-tasks in **one** assistant turn — multiple tool calls in a single message. If any check fails, fall back to sequential.

Each sub-agent gets a **self-contained brief**:

- The goal in one sentence.
- The exact inputs (file paths, IDs, queries) — no "as discussed above."
- The expected output shape (a summary? a diff? a list?).
- A length cap when the result feeds back into the parent context (e.g. "report in under 200 words").
- Hard constraints from the parent task (deadlines, must-not-touch files).

After fan-out, **synthesise** the results in the parent turn. Do not just paste sub-agent outputs back — combine them into a single answer keyed to the original question.

## Avoid

- **Serial calls that could be parallel.** Reading three independent files one after the other in three separate turns is the canonical waste this skill exists to prevent.
- **Parallelising work with hidden dependencies.** "Both sub-agents will edit the same config file" is a write-write collision waiting to happen. Run the independence check honestly — if in doubt, sequential.
- **Vague briefs.** "Look at the auth code and report back" wastes a sub-agent. Briefs name files, name questions, name output shape, and cap length.
- **Dispatching without synthesising.** The parent must combine the sub-agent results; pasting raw outputs back is not an answer.
- **Fanning out for cosmetic speed.** Two trivial Reads do not need sub-agents — direct tool calls in one turn are faster and cheaper. Sub-agent dispatch is for work substantial enough to justify the context cost.
- **Forgetting that sub-agents have no memory.** A sub-agent doesn't see prior turns or the user's preferences. The brief must carry everything the sub-agent needs.

## Verify

A fan-out is well-formed if:

- The independence check was written down before dispatch.
- The dispatch happened in **one** assistant turn (not split across turns).
- Each sub-agent brief is self-contained — readable cold by someone who hasn't seen the parent conversation.
- The parent turn after fan-out synthesises the results rather than pasting them.

If any of those is missing, the discipline broke — and the next fan-out probably should have stayed sequential.
