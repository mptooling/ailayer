# Systematic Debugging — reproduce/isolate/root-cause/defend skill

> **Category:** Methodology | **License:** MIT | **Type:** Workflow skill

A short, opinionated skill that locks an agent into a disciplined debugging loop instead of shotgun-fixing. Distilled from `obra/superpowers:systematic-debugging`, [`mattpocock/skills:diagnose`](https://github.com/mattpocock/skills/blob/main/skills/engineering/diagnose/SKILL.md), and the standard root-cause-analysis canon (Beck, Feathers, Allspaw).

## What it is

When something is broken — failing test, crash, perf regression, "this used to work" — agents tend to start changing things and re-running until it accidentally passes. That produces fixes that don't generalise, hide the real bug, or break something else later.

This skill enforces a four-step loop:

1. **Reproduce** — make the bug fail on demand (failing test, deterministic repro script, exact steps).
2. **Isolate** — reduce the repro to the minimum trigger; bisect, comment-out, simplify.
3. **Root-cause** — explain *why* the minimal trigger fails. No fix until the cause is known.
4. **Fix + Defend** — apply the minimal fix; the failing repro becomes a regression test that ships in the same commit.

The forcing function is the regression test: a fix without a defending test is treated as incomplete.


## What good looks like

A debugging session looks like this:

```text
Repro:    failing test or repro script + exit code
Isolate:  what was removed without changing the failure
Cause:    one-sentence explanation grounded in the code
Fix:      the minimal change
Defense:  the regression test that now passes
```

If any of those five lines is missing or hand-waved, the loop hasn't run.

## Reference

- [`obra/superpowers/systematic-debugging`](https://github.com/obra/superpowers).
- [`mattpocock/skills/diagnose`](https://github.com/mattpocock/skills/blob/main/skills/engineering/diagnose/SKILL.md).
- Michael Feathers, *Working Effectively with Legacy Code* — characterisation tests as a way of pinning behaviour before changing it.
- John Allspaw on *blameless post-mortems* — the same root-cause discipline applied to incidents.

## Compose-with

- `tdd` — the regression test in step 4 is exactly a TDD red→green pair.
- `verification-before-completion` — once the regression test passes, verification closes the loop on the fix.
- `brainstorming` — when the bug is really a misunderstanding of requirements, escalate back to brainstorming rather than fixing the wrong thing.


---

## When To Use

- If the symptom is purely cosmetic (typo, missing `;`, formatting), this skill does not apply — fix it directly.

## How To Apply

- No install. The skill is behavioural — the agent reads it and adopts the discipline.
- The project's normal test command is the harness for the regression test (step 4). If non-obvious, document it in `CLAUDE.md` / `AGENTS.md` / `GEMINI.md`.
- Run the loop. Avoid skip steps. Avoid reorder.
- ### 1. Reproduce
- Get the bug to fail **on demand**. Acceptable forms:
- A failing automated test that asserts the misbehaviour. (Strongly preferred.)
- A deterministic repro script.
- An exact sequence of inputs/clicks that fails every time.

## Watch Outs

- **Skipping reproduction.** "I think I see it" is not a repro. If you can't make it fail on demand, you can't prove it's fixed.
- **"Defensive" fixes that paper over the symptom.** Adding a `?? defaultValue` or `try/catch` without understanding *why* the value is missing or the call threw — that's hiding the bug, not fixing it.
- **Drive-by changes.** A debugging PR that also reformats files / renames things / refactors three modules is uncheckable. One bug, one fix, one regression test.
- **Fix-by-flaky-rerun.** "It passed this time" is not a fix. If the repro is non-deterministic, that's a separate (real) problem.
- **Trusting "it works on my machine."** Pin versions, env vars, OS, locale if any of them might matter. Reproduce on a clean checkout.
- **Closing the bug before the regression test exists.** The test is the closing artifact.
