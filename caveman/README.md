# Caveman

> **Category:** Coding Methodology | **Pricing:** Free | **Type:** Methodology / mindset (no tool to install)

---

## Repository

Caveman is not a product — it's a coding *methodology*. There is nothing to install. Reference material:

- ["Caveman debugging" — Wikipedia (Tracing)](https://en.wikipedia.org/wiki/Tracing_(software))
- ["The first sign of underengineering" — Sandi Metz on duplication over abstraction](https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction)
- [WET vs DRY discussion](https://overreacted.io/the-wet-codebase/)
- [YAGNI — Martin Fowler](https://martinfowler.com/bliki/Yagni.html)

---

## Documentation

There is no official documentation for "caveman coding" — the philosophy lives in folklore. Closest references:

- ["Rule of Three" (refactoring) — Martin Fowler](https://en.wikipedia.org/wiki/Rule_of_three_(computer_programming))
- [Grug Brained Developer](https://grugbrain.dev/) — same spirit, longer manifesto
- [Print-statement debugging benchmarks vs IDE debuggers](https://www.usenix.org/conference/atc18/presentation/beschastnikh)

---

## Summary

The **caveman** approach is a deliberate rejection of premature abstraction, clever indirection, and speculative generality. Code like a caveman: solve the problem in front of you with the dumbest construct that works, repeat code three times before extracting it, and debug with `print()` until the picture is clear. The intuition: every abstraction is a bet on the future that pays off only if the future arrives in the predicted shape — and it usually doesn't. Junior teams over-abstract because clever code feels productive; senior teams under-abstract because they've paid the cost of someone else's clever code at 3am. "Caveman" is shorthand for keeping the code stupid, the call graph shallow, and the debugger-of-last-resort (a print) always within reach. It is a coding mindset, not a tool — there are no APIs, no SaaS, no integrations.

**Best for:** Engineers who keep getting bitten by premature DRY, design-pattern overuse, or "framework first" instincts; pair-programming with AI agents that love to refactor working code into something "more elegant."

---

## Related Materials

- [Grug Brained Developer](https://grugbrain.dev/) — the canonical modern manifesto in this style
- ["Avoid Premature Abstraction" — Kent C. Dodds](https://kentcdodds.com/blog/aha-programming)
- ["The Wrong Abstraction" — Sandi Metz](https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction)
- ["Programming as Theory Building" — Peter Naur, 1985](https://pages.cs.wisc.edu/~remzi/Naur.pdf)
- ["Worse Is Better" — Richard Gabriel](https://www.dreamsongs.com/RiseOfWorseIsBetter.html)

---

## AI Agents That Can Use This Tool

| Agent / Framework | How it integrates |
|---|---|
| **Claude Code** | Inject as a slash command/skill so Claude defaults to brute-force, no-abstraction edits in this project |
| **Cursor / Windsurf** | Encode in `.cursor/rules/` or `.windsurf/rules/` to constrain refactor-happy agents |
| **GitHub Copilot** | Place in `.github/copilot-instructions.md` to bias suggestions away from premature patterns |
| **Aider** | Pair with `/architect` mode to keep its plans simple before applying them |
| **Any LLM agent** | Works as a system-prompt fragment — no API integration needed |

---

*Last updated: 2026*
