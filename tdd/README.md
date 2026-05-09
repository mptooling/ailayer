# Test-Driven Development — red/green/refactor skill

> **Category:** Methodology | **License:** MIT | **Type:** Cross-CLI agent skill (Claude Code, Codex CLI, Gemini CLI)

A short, opinionated skill that locks an agent into the strict red-green-refactor loop. Distilled from `obra/superpowers:test-driven-development`, [`mattpocock/skills/tdd`](https://github.com/mattpocock/skills/blob/main/skills/engineering/tdd/SKILL.md), and the well-trodden Beck/Fowler/Hunt-Thomas TDD canon.

## What it is

Before writing any implementation code for a new feature or bug fix, the agent **must write a failing test**. Then it makes the test pass with the minimum change. Then it refactors. Then it commits. Repeat for the next slice.

This skill is *strict* — it explicitly forbids the common AI-agent failure mode of "I'll write the implementation and the test together," which empirically produces tests that match the buggy implementation rather than the spec.

## Why it ships in this library

`obra/superpowers:test-driven-development` is Claude-Code-only. `mattpocock/skills/tdd` ships as part of the broader `mattpocock/skills` pack. To get TDD discipline portably across Claude Code, Codex CLI, and Gemini CLI via `ailayer`, the skill needs a self-contained version with explicit per-language commands. That's what's in `SKILL_PROMPT.md`.

## What good looks like

A TDD turn looks like this:

1. **Red** — write a test that asserts the desired behaviour. Run it. Watch it fail. Paste the failure output.
2. **Green** — write the **minimum** code to make it pass. Run the test. Paste the passing output.
3. **Refactor** — clean up only with the test still passing. Re-run. Paste the result.
4. **Commit** — the failing test and its fix go in the same commit (or PR).

Vertical slices, not horizontal layers — one test should drive one user-visible behaviour, not "the validation function exists."

## Reference

- [`obra/superpowers/test-driven-development`](https://github.com/obra/superpowers).
- [`mattpocock/skills/tdd`](https://github.com/mattpocock/skills/blob/main/skills/engineering/tdd/SKILL.md) — particularly strong on what makes a good vs bad test.
- Kent Beck, *Test-Driven Development: By Example*.

## Compose-with

- `brainstorming` — produces the success criteria the first failing test pins down.
- `verification-before-completion` — closes the loop by requiring the green run as evidence of done.
- `systematic-debugging` (Phase 2 upcoming) — bug fixes get a failing regression test as their first move; that test lives forever as the defence.

## Which AI agents integrate

Any agent that loads Markdown skills/slash-commands. `ailayer add skill tdd --tool all` injects it into Claude Code, Codex CLI, and Gemini CLI in one shot.
