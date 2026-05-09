# Matt Pocock — Skills For Real Engineers

> **Category:** Skill Collection | **License:** MIT | **Type:** Agent skill pack (Claude Code, Codex CLI, OpenCode, Cursor)

A curated set of 18 composable skills that target the four common failure modes of agentic coding (misalignment, verbosity, broken code, architectural mud). Authored by [Matt Pocock](https://www.totaltypescript.com/) (Total TypeScript) and shipped from his daily `.claude` directory.

- **GitHub:** [mattpocock/skills](https://github.com/mattpocock/skills) · ⭐ 67,500+
- **Newsletter:** [aihero.dev](https://www.aihero.dev/s/skills-newsletter)
- **License:** MIT

## What it is

Skills for Real Engineers is a counter-position to heavyweight agentic frameworks (GSD, BMAD, Spec-Kit) — the kind that "own the process" and make in-flight bugs hard to resolve. Pocock's skills are deliberately **small, model-agnostic, and composable**. Each one is a self-contained slash-command you can install à la carte.

Headline skills:

- **`/grill-me`** and **`/grill-with-docs`** — the most popular two. Before any code change, force the agent to interrogate you until every branch of the decision tree is resolved. `grill-with-docs` additionally writes shared-language `CONTEXT.md` and ADRs as it goes — addressing both alignment and verbosity in one move.
- **`/tdd`** — disciplined red-green-refactor with explicit guidance on what makes a good vs bad test.
- **`/diagnose`** — reproduce → minimise → hypothesise → instrument → fix → regression-test.
- **`/improve-codebase-architecture`** — periodic refactor pass that finds "deepening opportunities" using `CONTEXT.md` and `docs/adr/`. Recommended every few days.
- **`/zoom-out`** — broader-context request when working on unfamiliar code.
- **`/to-prd`** + **`/to-issues`** — convert the current conversation into a PRD and break it down into independently-grabbable GitHub issues.
- **`/triage`** — state-machine-driven issue triage with role-based labels.
- **`/prototype`** — throwaway prototype first, in either a runnable terminal app (state/business-logic) or several toggleable UI variations.
- **`/caveman`** — ultra-compressed communication mode (~75% token reduction); already profiled separately in this library as [`caveman/`](../caveman/README.md).
- **`/git-guardrails-claude-code`** — installs Claude Code hooks that block `git push --force`, `reset --hard`, `clean`, etc.
- **`/setup-pre-commit`** — Husky + lint-staged + Prettier + typecheck + tests.

Plus six personal/misc skills (`edit-article`, `obsidian-vault`, `migrate-to-shoehorn`, `scaffold-exercises`, `write-a-skill`, etc.) that are valuable but more bespoke.

## Why it's worth installing

The skills are organised around four explicit failure modes documented in the README, each grounded in classics like *The Pragmatic Programmer*, *Domain-Driven Design*, and *A Philosophy of Software Design*:

1. **Misalignment** ("the agent didn't do what I want") → `grill-me`, `grill-with-docs`.
2. **Verbosity** (no shared language, agent uses 20 words where 1 will do) → `CONTEXT.md` workflow built into `grill-with-docs`.
3. **Broken code** (no feedback loop) → `tdd`, `diagnose`.
4. **Ball-of-mud architecture** → `to-prd`, `zoom-out`, `improve-codebase-architecture`.

Each skill is a small Markdown file you can read, fork, and adapt — no opaque framework runtime.

## Install

```bash
# Interactive installer (skills.sh) — pick which skills, pick which agents
npx skills@latest add mattpocock/skills

# Then run the post-install setup inside your agent
/setup-matt-pocock-skills
```

The setup command asks: which issue tracker (GitHub / Linear / local), what triage labels, where to keep generated docs.

Targets: Claude Code, Codex CLI, OpenCode, Cursor (any agent that can load Markdown skills/slash-commands).

## Compared to other collections in this library

| Collection | Stars | Posture | When to reach for it |
|---|---|---|---|
| [obra/superpowers](https://github.com/obra/superpowers) (Phase 7) | high | Opinionated cross-cutting workflow framework | When you want a single coherent culture of TDD + planning + verification |
| [wshobson/agents](https://github.com/wshobson/agents) (Phase 7) | high | Comprehensive plugin set (80 plugins, 153 skills) | Maximum coverage / multi-agent orchestration |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 67k+ | Small, à-la-carte, "real engineering" angle | When you want one or two surgical skills (e.g. `/grill-with-docs`) without buying into a framework |

The three are not mutually exclusive — `mattpocock-skills` composes well alongside the other two.

## Related articles

- [The Pragmatic Programmer (Thomas & Hunt)](https://www.amazon.co.uk/Pragmatic-Programmer-Anniversary-Journey-Mastery/dp/B0833F1T3V) — quoted throughout the README.
- [Domain-Driven Design (Eric Evans)](https://www.amazon.co.uk/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215) — basis for the `CONTEXT.md` shared-language pattern.
- [A Philosophy of Software Design (Ousterhout)](https://www.amazon.co.uk/Philosophy-Software-Design-2nd/dp/173210221X) — drives the `improve-codebase-architecture` skill.

## Which AI agents integrate

Documented support: Claude Code, Codex CLI, OpenCode, Cursor. Skills are plain Markdown so any agent that can load slash-commands or skills will work; `setup-matt-pocock-skills` writes per-repo config that the engineering skills consume.
