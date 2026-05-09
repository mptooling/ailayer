# Brainstorming — Socratic intent-clarification skill

> **Category:** Methodology | **License:** MIT | **Type:** Cross-CLI agent skill (Claude Code, Codex CLI, Gemini CLI)

A short, opinionated skill that forces an agent to interrogate the user *before* writing code, design, or specs. Distilled from the public canon (`obra/superpowers:brainstorming`, the [Pragmatic Programmer](https://pragprog.com/) "no one knows exactly what they want" rule, and the front-end of GSD/Spec-Kit/BMAD methods) — but kept small enough to compose with any other workflow skill.

## What it is

When a user says *"add feature X"*, *"refactor Y"*, or *"build Z"*, the cheapest way to ship the wrong thing is to start writing it. This skill flips the agent into a question-asking mode for one round before any code is touched. It produces a short brief — goals, scope, constraints, success criteria, edge cases, what exists already — that the user confirms or edits before implementation begins.

The "do this before any creative work" framing is borrowed from the [`superpowers`](https://github.com/obra/superpowers) marketplace: brainstorming is a *gating* skill, not an *invokable* one. Other skills (`writing-plans`, `tdd`, `executing-plans`) chain off its output.

## Why it ships in this library

`superpowers:brainstorming` is only available in Claude Code via the marketplace. To get the same discipline in Codex CLI, Gemini CLI, and other agents that this library targets via `ailayer`, the skill needs a portable, model-agnostic version. That's what's in `SKILL_PROMPT.md`.

## What good looks like

A brainstorming session resembles this rough shape:

1. **Goal** — what does success look like in one sentence?
2. **Scope** — what's explicitly in and out?
3. **Constraints** — language/framework/perf/budget/timeline.
4. **Success criteria** — how do we know it works? (measurable)
5. **Edge cases** — what's the worst input?
6. **Existing surfaces** — what already does part of this?
7. **Open questions** — what does the user not know yet?

Five to ten targeted questions, no more. The skill explicitly forbids writing code, planning files, or proposing implementations until the user signs off on the brief.

## Reference

- [`obra/superpowers/brainstorming`](https://github.com/obra/superpowers) — the canonical Claude Code implementation.
- [`mattpocock/skills/grill-me`](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md) and [`grill-with-docs`](https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md) — a richer variant that also produces a `CONTEXT.md` shared-language document.

## Compose-with

- `writing-plans` (Phase 2) — turns the brief into a phased plan.
- `tdd` (Phase 2) — writes failing tests before implementation.
- `verification-before-completion` (Phase 2) — closes the loop by requiring evidence that success criteria are met.

## Which AI agents integrate

Any agent that loads Markdown skills/slash-commands. `ailayer add skill brainstorming --tool all` injects it into Claude Code, Codex CLI, and Gemini CLI in one shot.
