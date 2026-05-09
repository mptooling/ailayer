---
name: verification-before-completion
description: Forbid "done" claims without command-output evidence — run build/lint/typecheck/tests and paste the result.
category: Methodology
triggers: [done, completed, finished, ready, fixed, passing, ship, merge, verification, smoke-test, regression]
safety: low
version: 2026-05-09
homepage: https://github.com/obra/superpowers
---

# Verification-before-completion skill

Use this skill **before any "done"-shaped claim** — "fixed," "ready to merge," "tests pass," "build green," "feature complete." If you're about to assert that something works, this skill says: prove it with command output.

The single most common AI-agent failure mode is reporting success without verification. Treat completion claims as a contract: no evidence, no claim.

## Setup

No install — behavioural skill. The agent reads this file and adopts the discipline.

To make verification reliable, the project should expose the commands a single shell line can run. Document them in the project's `CLAUDE.md` / `AGENTS.md` / `GEMINI.md` if they're non-obvious. Examples:

- TypeScript / Node monorepo: `pnpm tsc --noEmit && pnpm lint && pnpm test -- --run`
- Python: `ruff check . && mypy . && pytest -x -q`
- Go: `go vet ./... && gofmt -l . && go test ./...`
- Rust: `cargo fmt --check && cargo clippy -- -D warnings && cargo test`

## Use

When you're about to claim completion:

1. **Identify the verification commands** for what changed. Don't run the full suite if a targeted set is enough — run modified-only tests where the runner supports it.
2. **Run them.** Capture stdout, stderr, exit code.
3. **Paste the result** into the conversation in a fenced block. Include the command, the exit code, and either the full output (if ≤30 lines) or the relevant tail (if longer).
4. Use this report shape:

   ```text
   $ <command>
   <output, last ~20 lines if long>
   exit: <code>
   ```

5. Only after the report shows a clean exit may you claim completion. If anything fails, treat that as the new task and either fix it or escalate.

When the user *explicitly* asks to skip verification ("just write the code, I'll run tests"), comply — but flag the skip in your reply so the user owns the decision.

For changes that modify success criteria established by `brainstorming`, verification means *those* criteria, not just the build. If the brief said "form submits in <100ms," report a measurement.

## Avoid

- **Asserting "tests pass" without running them.** This is the failure mode this skill exists to prevent. The most common form is *"the implementation should pass the tests we wrote"* — "should" is not evidence.
- **Pasting only the command without the output.** That's not verification, that's a promise.
- **Trimming the output to remove failures.** If a test failed, show it. The user will figure it out anyway and trust will erode.
- **Claiming partial completion as completion.** "I implemented the feature; the test for the edge case is left for later" → that's *incomplete*, not done. Say so.
- **Skipping verification on "trivial" changes.** Renames break imports. Typo fixes break grep call-sites. One-liners introduce regressions. Run the smallest sensible verification for *every* change.
- **Re-running verification post-completion to "make it look like" the work was checked.** That's theatre. Do it before the claim.
- **Hand-waving "the build was green earlier."** Earlier is not now.

## Verify

Meta-verify this skill itself: in the conversation where it's invoked, the completion claim should always be preceded by a fenced output block showing the verification command and its exit code.

If the user's reply to your "done" is *"are you sure? did you run the tests?"*, you skipped this skill.
