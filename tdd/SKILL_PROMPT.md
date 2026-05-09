---
name: tdd
description: Strict red-green-refactor — write a failing test first, the minimum impl to pass, then refactor. Vertical slices.
category: Methodology
triggers: [tdd, test-driven, red-green-refactor, failing test, regression test, new feature, bug fix, vertical slice]
safety: low
version: 2026-05-09
homepage: https://github.com/obra/superpowers
---

# Test-Driven Development skill

Use this skill **before writing implementation code** for a new feature or a bug fix. The agent's first move is a failing test — never the implementation.

If the work is purely structural (renames, formatting, type-only refactors with existing tests, doc edits), this skill does not apply.

## Setup

No install. The skill is behavioural — the agent reads it and adopts the discipline.

The project must expose runnable test commands. If they're non-obvious, capture them in `CLAUDE.md` / `AGENTS.md` / `GEMINI.md`. Common defaults:

| Stack | Test command (modified-only when supported) |
|---|---|
| TypeScript / Node | `pnpm vitest run <path>` or `pnpm jest --findRelatedTests <path>` |
| Python | `pytest -x -q <path>` |
| Go | `go test ./<pkg>` |
| Rust | `cargo test -p <crate> <name>` |
| Ruby | `bundle exec rspec <path>` |

Prefer the narrowest runner that still proves the behaviour — full-suite runs at the start of a TDD loop waste minutes.

## Use

For each slice of work, run the loop:

1. **Red.** Write **one** test that captures the next behaviour. Make it specific (assert one outcome, not three). Run it. Paste the failing output:

   ```text
   $ <test command>
   <failure with assertion message>
   exit: 1
   ```

   If the test passes immediately, the test is wrong (or the behaviour already exists). Fix the test before continuing.

2. **Green.** Write the **minimum** implementation that makes the test pass. Resist the urge to also fix the next thing. Run the test. Paste the passing output.

3. **Refactor.** Improve names, dedupe, simplify. **Re-run the test after each refactor step.** If green stays green, continue. If anything breaks, revert that refactor.

4. **Commit.** Failing test + its fix belong in the same commit (or PR). The history should always show a red→green pair.

5. **Next slice.** Repeat for the next behaviour. Don't write three tests in a row before any implementation — that's "test-after," not TDD.

For bug fixes, the failing test is the **regression test**. It stays in the suite forever as the defence against the bug returning.

For new features, write the *narrowest* test that captures the user-visible behaviour. "Render a button" is too broad; "clicking the button submits the form and disables itself" is right-sized.

When the user explicitly asks to skip TDD ("just write the code, I'll write tests later"), comply — but flag the skip in your reply so the user owns the decision.

## Avoid

- **Writing the test and the implementation in the same edit.** This is the single most common dodge. If the test never failed, you didn't TDD — you wrote a smoke test that confirms what you already wrote.
- **Tests that mirror the implementation.** A test that reads the same logic back at the impl ("the function returns `result.foo` if `result.foo`") catches nothing. Test the behaviour, not the algorithm.
- **Writing five tests before any code.** That's deferred-TDD — you'll over-specify, then under-implement, then revise tests when reality bites. Stay in the loop.
- **Mocking everything.** Mocks are a tool for boundary tests (HTTP, time, randomness). For business logic, prefer real objects + small fixtures. Tests that mock the thing under test always pass and prove nothing.
- **Trimming the failing output to "save space" in the conversation.** Show the assertion. Show the diff. The user needs to see what failed.
- **Leaving `.skip` / `.only` / `xit` on tests after a session.** Forbidden in committed code. Run `rg "\.only|\.skip|xit\(" --type ts` (adjust per language) before claiming done.
- **Refactoring while red.** The rule is: only refactor with a green bar. If you need to refactor to make the test pass, you're really doing two things — back out, refactor the now-passing previous slice, then return to red.
- **Skipping TDD on "small" changes.** Renames break imports, typos break grep, one-liners introduce regressions. Run the smallest sensible test for every change.

## Verify

The skill is being followed if, in any non-trivial change, the conversation contains:

- A fenced block showing a failed test run (red).
- Then a fenced block showing the same test passing (green).
- Both before any "done" claim (which is then gated by `verification-before-completion`).

If a task ends with implementation but no failed-test transcript, TDD was skipped. Either re-do under TDD, or be explicit about the skip in the PR description.
