# Verification-before-completion — evidence-before-assertions skill

> **Category:** Methodology | **License:** MIT | **Type:** Workflow skill

A short, opinionated skill that forbids "done" claims without **evidence**. Distilled from `obra/superpowers:verification-before-completion` and the long-running engineering wisdom that *AI agents are systematically overconfident*: they will assert that a change is complete, that tests pass, that the build is green — without having actually run the verification commands.

## What it is

When the agent finishes implementing a feature/fix/refactor and is about to say "done," "fixed," "passing," "ready to merge" — this skill forces it to first run the verification commands (build, lint, typecheck, tests) and **paste the actual output** into the conversation. No verification output → no completion claim allowed.

This is the single highest-leverage skill in the public canon according to multiple sources, including `obra/superpowers`. It directly counters the failure mode where an agent reports success and the user discovers minutes later that the build is broken.


## What good looks like

Two pieces:

1. **A verification matrix** that says, for the language/stack at hand, exactly which commands to run before claiming completion (e.g. for TS: `pnpm tsc --noEmit && pnpm lint && pnpm test -- --run`).
2. **A reporting template** that requires the agent to paste:
   - The exact command run.
   - Its exit code.
   - The relevant tail of its output (or full output if short).

Failure mode: a passing-build assertion without command output. The skill explicitly treats that as "not done" and instructs the agent to either run the verification or admit it didn't.

## Reference

- [`obra/superpowers/verification-before-completion`](https://github.com/obra/superpowers) — the canonical Claude Code implementation.
- [`mattpocock/skills/tdd`](https://github.com/mattpocock/skills/blob/main/skills/engineering/tdd/SKILL.md) — overlapping discipline for the test-running half of verification.

## Compose-with

- `brainstorming` — produces the success criteria that this skill verifies against.
- `tdd` — supplies the failing tests that this skill confirms now pass.
- `systematic-debugging` — required regression test fits naturally in the verification step.


---

## When To Use

- Use this skill **before any "done"-shaped claim** — "fixed," "ready to merge," "tests pass," "build green," "feature complete." If you're about to assert that something works, this skill says: prove it with command output.
- The single most common AI-agent failure mode is reporting success without verification. Treat completion claims as a contract: no evidence, no claim.

## How To Apply

- No install — behavioural skill. The agent reads this file and adopts the discipline.
- To make verification reliable, the project should expose the commands a single shell line can run. Document them in the project's `CLAUDE.md` / `AGENTS.md` / `GEMINI.md` if they're non-obvious. Examples:
- TypeScript / Node monorepo: `pnpm tsc --noEmit && pnpm lint && pnpm test -- --run`
- Python: `ruff check . && mypy . && pytest -x -q`
- Go: `go vet ./... && gofmt -l . && go test ./...`
- Rust: `cargo fmt --check && cargo clippy -- -D warnings && cargo test`
- When you're about to claim completion:
- **Identify the verification commands** for what changed. Don't run the full suite if a targeted set is enough — run modified-only tests where the runner supports it.

## Watch Outs

- **Asserting "tests pass" without running them.** This is the failure mode this skill exists to prevent. The most common form is *"the implementation should pass the tests we wrote"* — "should" is not evidence.
- **Pasting only the command without the output.** That's not verification, that's a promise.
- **Trimming the output to remove failures.** If a test failed, show it. The user will figure it out anyway and trust will erode.
- **Claiming partial completion as completion.** "I implemented the feature; the test for the edge case is left for later" → that's *incomplete*, not done. Say so.
- **Skipping verification on "trivial" changes.** Renames break imports. Typo fixes break grep call-sites. One-liners introduce regressions. Run the smallest sensible verification for *every* change.
- **Re-running verification post-completion to "make it look like" the work was checked.** That's theatre. Do it before the claim.
