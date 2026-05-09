---
name: brainstorming
description: Socratic intent-clarification before any creative work — surfaces goals, constraints, success criteria, and unknowns.
category: Methodology
triggers: [new feature, new component, refactor, design, spec, brief, brainstorm, scoping, requirements, intent]
safety: low
version: 2026-05-09
homepage: https://github.com/obra/superpowers
---

# Brainstorming skill

Use this skill **before any creative work** — adding a feature, building a component, refactoring a module, designing an API, writing a spec, or modifying user-visible behaviour. The single biggest cause of wasted agent loops is misalignment between what the user *thinks* they asked for and what the agent *thinks* they asked for. This skill closes that gap before code is touched.

If the request is mechanical (rename a variable, fix a typo, run a command), skip this skill and proceed.

## Setup

No install — this is a behavioural skill. The agent reads the prompt and switches into question-asking mode. To force invocation, the user can prefix a message with `/brainstorm`, but the skill should fire automatically on any creative-work trigger.

## Use

Run exactly one round of clarifying questions, **before any other action**.

1. Ask **5 to 10 targeted questions**, grouped by category. Skip categories that are already answered by context or repo state.
2. After the user answers, write a **brief** (≤200 words) summarising the answers in this shape:
   - **Goal** — one sentence.
   - **In scope** — bullet list.
   - **Out of scope** — bullet list.
   - **Constraints** — runtime/lang/perf/timeline.
   - **Success criteria** — measurable.
   - **Edge cases** — what happens on bad input / partial state.
   - **Touches** — files/modules/external surfaces.
3. Ask the user to confirm the brief or edit it. Wait for explicit confirmation.
4. **Only then** proceed to plan or implement.

Question categories (use sparingly — pick the few that matter most):

- **Intent**: "What does success look like?" "What problem are you solving for whom?"
- **Scope**: "What's the smallest version of this that's worth shipping?" "What's deliberately out of scope?"
- **Constraints**: "Any framework/version/runtime/budget/timeline I should know about?"
- **Success criteria**: "How will you know it works? Test? Metric? User confirms?"
- **Edge cases**: "What's the input/state that breaks naive solutions?"
- **Existing surfaces**: "Does anything already do part of this? Where?"
- **Unknowns**: "What aren't you sure about yet?"

A good question opens a branch the user hadn't considered. A bad question asks something the agent could discover by reading the repo for 30 seconds — don't ask those.

## Avoid

- **Skipping straight to implementation** because the request "seems clear." It rarely is. Even *"add a button to do X"* hides assumptions about styling, accessibility, state management, error handling, and analytics that the agent will guess wrong.
- **Asking 20 questions.** Ceiling is 10. Past 10, you're stalling — pick the highest-leverage few.
- **Asking yes/no questions for things with a spectrum of answers.** "Should this be fast?" is a bad question; "What's the latency budget — interactive (<100ms), background (<5s), batch (>1min)?" is a good one.
- **Restating the user's request back at them** as a question. That's not clarification, that's friction.
- **Producing the brief without confirmation.** The brief is a contract; an unconfirmed contract isn't a contract.
- **Re-running brainstorming on the same task.** If scope changes mid-flight, a *short* re-brief is fine. Don't restart from scratch.
- **Brainstorming mechanical work** (renames, typo fixes, single-line changes). Save the ceremony for actual creative work.

## Verify

The skill is "done" when:

1. The user has confirmed (or edited) the brief.
2. The brief is captured in the conversation (or, in long-running sessions, written to a file the next phase can read).
3. The next skill (`writing-plans`, `tdd`, or direct implementation) has the brief as input.

If you find yourself five tool calls into implementation and unsure what success looks like, you skipped this step. Stop and re-brainstorm.
