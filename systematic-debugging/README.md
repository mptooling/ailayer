# Systematic Debugging — reproduce/isolate/root-cause/defend skill

> **Category:** Methodology | **License:** MIT | **Type:** Cross-CLI agent skill (Claude Code, Codex CLI, Gemini CLI)

A short, opinionated skill that locks an agent into a disciplined debugging loop instead of shotgun-fixing. Distilled from `obra/superpowers:systematic-debugging`, [`mattpocock/skills:diagnose`](https://github.com/mattpocock/skills/blob/main/skills/engineering/diagnose/SKILL.md), and the standard root-cause-analysis canon (Beck, Feathers, Allspaw).

## What it is

When something is broken — failing test, crash, perf regression, "this used to work" — agents tend to start changing things and re-running until it accidentally passes. That produces fixes that don't generalise, hide the real bug, or break something else later.

This skill enforces a four-step loop:

1. **Reproduce** — make the bug fail on demand (failing test, deterministic repro script, exact steps).
2. **Isolate** — reduce the repro to the minimum trigger; bisect, comment-out, simplify.
3. **Root-cause** — explain *why* the minimal trigger fails. No fix until the cause is known.
4. **Fix + Defend** — apply the minimal fix; the failing repro becomes a regression test that ships in the same commit.

The forcing function is the regression test: a fix without a defending test is treated as incomplete.

## Why it ships in this library

`obra/superpowers:systematic-debugging` is Claude-Code-only. `mattpocock/skills:diagnose` ships in the broader `mattpocock/skills` pack. To get the discipline portably across Claude Code, Codex CLI, and Gemini CLI via `ailayer`, the skill needs a self-contained, language-agnostic version. That's what's in `SKILL_PROMPT.md`.

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

- `tdd` (Phase 2) — the regression test in step 4 is exactly a TDD red→green pair.
- `verification-before-completion` (Phase 2) — once the regression test passes, verification closes the loop on the fix.
- `brainstorming` — when the bug is really a misunderstanding of requirements, escalate back to brainstorming rather than fixing the wrong thing.

## Which AI agents integrate

Any agent that loads Markdown skills/slash-commands. `ailayer add skill systematic-debugging --tool all` injects it into Claude Code, Codex CLI, and Gemini CLI in one shot.
