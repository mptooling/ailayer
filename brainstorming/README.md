# Brainstorming — Socratic intent-clarification skill

> **Category:** Methodology | **License:** MIT | **Type:** Workflow skill

A short, opinionated skill that forces an agent to interrogate the user *before* writing code, design, or specs. Distilled from the public canon (`obra/superpowers:brainstorming`, the [Pragmatic Programmer](https://pragprog.com/) "no one knows exactly what they want" rule, and the front-end of GSD/Spec-Kit/BMAD methods) — but kept small enough to compose with any other workflow skill.

## What it is

When a user says *"add feature X"*, *"refactor Y"*, or *"build Z"*, the cheapest way to ship the wrong thing is to start writing it. This skill flips the agent into a question-asking mode for one round before any code is touched. It produces a short brief — goals, scope, constraints, success criteria, edge cases, what exists already — that the user confirms or edits before implementation begins.

The "do this before any creative work" framing is borrowed from the [`superpowers`](https://github.com/obra/superpowers) marketplace: brainstorming is a *gating* skill, not an *invokable* one. Other skills (`writing-plans`, `tdd`, `executing-plans`) chain off its output.


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

- `writing-plans` — turns the brief into a phased plan.
- `tdd` — writes failing tests before implementation.
- `verification-before-completion` — closes the loop by requiring evidence that success criteria are met.


---

## When To Use

- If the request is mechanical (rename a variable, fix a typo, run a command), skip this skill and proceed.

## How To Apply

- No install — this is a behavioural skill. The agent reads the prompt and switches into question-asking mode. To force invocation, the user can prefix a message with `/brainstorm`, but the skill should fire automatically on any creative-work trigger.
- Run exactly one round of clarifying questions, **before any other action**.
- Ask **5 to 10 targeted questions**, grouped by category. Skip categories that are already answered by context or repo state.
- After the user answers, write a **brief** (≤200 words) summarising the answers in this shape:
- **Goal** — one sentence.
- **In scope** — bullet list.
- **Out of scope** — bullet list.
- **Constraints** — runtime/lang/perf/timeline.

## Watch Outs

- **Skipping straight to implementation** because the request "seems clear." It rarely is. Even *"add a button to do X"* hides assumptions about styling, accessibility, state management, error handling, and analytics that the agent will guess wrong.
- **Asking 20 questions.** Ceiling is 10. Past 10, you're stalling — pick the highest-leverage few.
- **Asking yes/no questions for things with a spectrum of answers.** "Should this be fast?" is a bad question; "What's the latency budget — interactive (<100ms), background (<5s), batch (>1min)?" is a good one.
- **Restating the user's request back at them** as a question. That's not clarification, that's friction.
- **Producing the brief without confirmation.** The brief is a contract; an unconfirmed contract isn't a contract.
- **Re-running brainstorming on the same task.** If scope changes mid-flight, a *short* re-brief is fine. Don't restart from scratch.
