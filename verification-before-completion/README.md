# Verification-before-completion — evidence-before-assertions skill

> **Category:** Methodology | **License:** MIT | **Type:** Cross-CLI agent skill (Claude Code, Codex CLI, Gemini CLI)

A short, opinionated skill that forbids "done" claims without **evidence**. Distilled from `obra/superpowers:verification-before-completion` and the long-running engineering wisdom that *AI agents are systematically overconfident*: they will assert that a change is complete, that tests pass, that the build is green — without having actually run the verification commands.

## What it is

When the agent finishes implementing a feature/fix/refactor and is about to say "done," "fixed," "passing," "ready to merge" — this skill forces it to first run the verification commands (build, lint, typecheck, tests) and **paste the actual output** into the conversation. No verification output → no completion claim allowed.

This is the single highest-leverage skill in the public canon according to multiple sources (`obra/superpowers`, the cross-tool research synthesised in `ROADMAP.md`). It directly counters the failure mode where an agent reports success and the user discovers minutes later that the build is broken.

## Why it ships in this library

`superpowers:verification-before-completion` is Claude-Code-only. To get the same discipline in Codex CLI, Gemini CLI, and any future agent that this library targets via `ailayer`, the skill needs a portable, model-agnostic version. That's what's in `SKILL_PROMPT.md`.

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

- `brainstorming` (Phase 2) — produces the success criteria that this skill verifies against.
- `tdd` (Phase 2) — supplies the failing tests that this skill confirms now pass.
- `systematic-debugging` (Phase 2) — required regression test fits naturally in the verification step.

## Which AI agents integrate

Any agent that loads Markdown skills/slash-commands. `ailayer add skill verification-before-completion --tool all` injects it into Claude Code, Codex CLI, and Gemini CLI in one shot.
