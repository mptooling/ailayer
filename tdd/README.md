# Test-Driven Development — red/green/refactor skill

> **Category:** Methodology | **License:** MIT | **Type:** Workflow skill

A short, opinionated skill that locks an agent into the strict red-green-refactor loop. Distilled from `obra/superpowers:test-driven-development`, [`mattpocock/skills/tdd`](https://github.com/mattpocock/skills/blob/main/skills/engineering/tdd/SKILL.md), and the well-trodden Beck/Fowler/Hunt-Thomas TDD canon.

## What it is

Before writing any implementation code for a new feature or bug fix, the agent **must write a failing test**. Then it makes the test pass with the minimum change. Then it refactors. Then it commits. Repeat for the next slice.

This skill is *strict* — it explicitly forbids the common AI-agent failure mode of "I'll write the implementation and the test together," which empirically produces tests that match the buggy implementation rather than the spec.


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
- `systematic-debugging` — bug fixes get a failing regression test as their first move; that test lives forever as the defence.


---

## When To Use

- Use this skill **before writing implementation code** for a new feature or a bug fix. The agent's first move is a failing test — avoid the implementation.
- If the work is purely structural (renames, formatting, type-only refactors with existing tests, doc edits), this skill does not apply.

## How To Apply

- No install. The skill is behavioural — the agent reads it and adopts the discipline.
- The project must expose runnable test commands. If they're non-obvious, capture them in `CLAUDE.md` / `AGENTS.md` / `GEMINI.md`.

| Stack | Test command (modified-only when supported) |
|---|---|
| TypeScript / Node | `pnpm vitest run <path>` or `pnpm jest --findRelatedTests <path>` |
| Python | `pytest -x -q <path>` |
| Go | `go test ./<pkg>` |
| Rust | `cargo test -p <crate> <name>` |

## Watch Outs

- **Writing the test and the implementation in the same edit.** This is the single most common dodge. If the test did not fail, you didn't TDD — you wrote a smoke test that confirms what you already wrote.
- **Tests that mirror the implementation.** A test that reads the same logic back at the impl ("the function returns `result.foo` if `result.foo`") catches nothing. Test the behaviour, not the algorithm.
- **Writing five tests before any code.** That's deferred-TDD — you'll over-specify, then under-implement, then revise tests when reality bites. Stay in the loop.
- **Mocking everything.** Mocks are a tool for boundary tests (HTTP, time, randomness). For business logic, prefer real objects + small fixtures. Tests that mock the thing under test always pass and prove nothing.
- **Trimming the failing output to "save space" in the conversation.** Show the assertion. Show the diff. The user needs to see what failed.
- **Leaving `.skip` / `.only` / `xit` on tests after a session.** Forbidden in committed code. Run `rg "\.only|\.skip|xit\(" --type ts` (adjust per language) before claiming done.
