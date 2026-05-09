---
name: systematic-debugging
description: Reproduce → Isolate → Root-cause → Fix+Defend. No fix lands without a regression test defending it.
category: Methodology
triggers: [bug, broken, failing test, regression, crash, error, exception, stack trace, used to work, debugging, diagnose, root cause]
safety: low
version: 2026-05-09
homepage: https://github.com/obra/superpowers
---

# Systematic Debugging skill

Use this skill **whenever something is broken** — failing test, runtime error, exception, crash, performance regression, "this used to work." It replaces shotgun-fixing (changing things until the symptom disappears) with a four-step loop that produces fixes that *generalise* and don't quietly regress.

If the symptom is purely cosmetic (typo, missing `;`, formatting), this skill does not apply — fix it directly.

## Setup

No install. The skill is behavioural — the agent reads it and adopts the discipline.

The project's normal test command is the harness for the regression test (step 4). If non-obvious, document it in `CLAUDE.md` / `AGENTS.md` / `GEMINI.md`.

## Use

Run the loop. Do not skip steps. Do not reorder.

### 1. Reproduce

Get the bug to fail **on demand**. Acceptable forms:

- A failing automated test that asserts the misbehaviour. (Strongly preferred.)
- A deterministic repro script.
- An exact sequence of inputs/clicks that fails every time.

Paste the failing output:

```text
$ <command>
<output, last ~20 lines>
exit: 1
```

If you can't reproduce reliably, **stop debugging and report that.** A non-deterministic bug is its own task — investigate flakiness, add observability, retry with logs. Don't pretend.

### 2. Isolate

Reduce the repro to the **minimum trigger**. Techniques:

- **Comment out / delete code** until the bug stops, then add back until it returns. The last-added piece is implicated.
- **`git bisect`** when the bug used to not exist. Note the first-bad commit.
- **Strip inputs** until the smallest input still fails.
- **Disable libraries / features** one at a time.

Report what was removed without affecting the failure, and the minimum that still fails.

### 3. Root-cause

Explain in **one sentence**, grounded in code, *why* the minimum trigger fails. Cite specific lines.

Examples:

- "`getUser()` at `lib/users.ts:42` returns `null` when the user record exists but has `deleted_at` set, and the caller at line 18 dereferences without a null check."
- "The cron at `worker/jobs.ts:90` runs every minute, but the job at `email.ts:33` takes >60s when the queue exceeds ~500 entries, so the next run sees stale state."

If you can't explain *why*, you haven't root-caused — go back to step 2 and isolate further. Speculation is not a cause.

### 4. Fix + Defend

Two artifacts in the same commit (or PR):

- **Fix** — the minimal change that addresses the root cause. Not the symptom; the cause. Avoid drive-by improvements; one bug, one fix.
- **Regression test** — the failing repro from step 1, now passing. It stays in the suite forever.

Run the test. Paste the green result. Run the full relevant test suite to check nothing else regressed. Paste that too.

A fix without a defending test is treated as **incomplete**. If the framework genuinely doesn't support a regression test for this bug (rare — usually means the test is hard, not impossible), say so explicitly and propose an alternative defence (assertion, type, lint rule, runtime check).

## Avoid

- **Skipping reproduction.** "I think I see it" is not a repro. If you can't make it fail on demand, you can't prove it's fixed.
- **"Defensive" fixes that paper over the symptom.** Adding a `?? defaultValue` or `try/catch` without understanding *why* the value is missing or the call threw — that's hiding the bug, not fixing it.
- **Drive-by changes.** A debugging PR that also reformats files / renames things / refactors three modules is uncheckable. One bug, one fix, one regression test.
- **Fix-by-flaky-rerun.** "It passed this time" is not a fix. If the repro is non-deterministic, that's a separate (real) problem.
- **Trusting "it works on my machine."** Pin versions, env vars, OS, locale if any of them might matter. Reproduce on a clean checkout.
- **Closing the bug before the regression test exists.** The test is the closing artifact.
- **Long-distance debugging by guessing.** If you've been thrashing for >15 minutes without isolating, stop and start from step 1 with deeper instrumentation (logs, prints, debugger, time-travel).

## Verify

A debugging session followed this skill if the conversation contains, in order:

1. A fenced block showing the failing repro (red).
2. A short note on what was isolated.
3. A one-sentence root cause citing specific code.
4. A fenced block showing the regression test passing (green).
5. The diff of the fix + the new regression test in the same commit/PR.

If any of those is missing, you skipped a step. Either redo, or call out the gap explicitly so the user owns the trade-off.
