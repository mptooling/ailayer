# AI Tools & Skills Library

> A curated, living library of the most impactful AI tools — categorised by use case, ranked by adoption, and documented for IT, Marketing, Sales, and C-Level audiences.
>
> **Last updated:** May 2026 | **Tools documented:** 28 | **Next step:** per-tool automation & enablement guides

---

## How to use this library

Each tool has its own folder with two files:

- **`README.md`** — human-oriented documentation: GitHub link & star count, official docs, plain-English summary, related articles, and which AI agents integrate with the tool.
- **`SKILL_PROMPT.md`** — agent-oriented HOW-TO instructions: setup, API patterns, what to do, what to avoid. This is what `ailayer add skill <name>` injects into Claude Code, Codex CLI, or Gemini CLI.

When `SKILL_PROMPT.md` is missing, `ailayer` falls back to `README.md` — but READMEs are documentation, not prompts, so always prefer the dedicated skill file.

---

## 🖥️ AI Coding Assistants

*For IT/engineering teams. Tools that write, complete, review, and refactor code.*

| Tool | Stars | Pricing | Best for |
|---|---|---|---|
| [GitHub Copilot](./github-copilot/README.md) | — (closed source) | $10–39/mo | Enterprise dev teams, GitHub-native workflows |
| [Cursor](./cursor/README.md) | — (closed source) | Free / $20/mo | Deep codebase understanding, model choice |
| [Continue](./continue/README.md) | ⭐ 24,000+ | Free (OSS) | Data privacy, on-prem, model flexibility |
| [Aider](./aider/README.md) | ⭐ 25,000+ | Free (OSS) | Terminal-native, git-integrated, batch refactors |
| [Windsurf](./windsurf/README.md) | — (closed source) | Free / $15/mo | Autonomous multi-step coding agents, enterprise self-hosting |
| [Caveman](./caveman/README.md) | ⭐ 53,000+ | Free (OSS) | Cutting agent output ~75%; multi-agent terse-mode plugin |
| [Claude-Mem](./claude-mem/README.md) | ⭐ 71,000+ | Free (OSS, AGPL-3.0) | Persistent cross-session memory for Claude Code / Gemini CLI / OpenCode |

---

## 🧭 Methodology Skills

*Workflow skills that change *how* the agent works, not what it integrates with. Cross-CLI (Claude Code, Codex CLI, Gemini CLI).*

| Skill | Stars | Pricing | Best for |
|---|---|---|---|
| [Brainstorming](./brainstorming/README.md) | — (this library) | Free (OSS, MIT) | Socratic intent-clarification *before* any creative work — surfaces goals, scope, constraints, and unknowns before code is touched |
| [Verification-before-completion](./verification-before-completion/README.md) | — (this library) | Free (OSS, MIT) | Forbid "done" claims without command-output evidence — run build/lint/typecheck/tests and paste the result before asserting completion |
| [TDD](./tdd/README.md) | — (this library) | Free (OSS, MIT) | Strict red-green-refactor — write a failing test first, the minimum implementation to pass, then refactor. Vertical slices, regression tests as bug defence |
| [Systematic Debugging](./systematic-debugging/README.md) | — (this library) | Free (OSS, MIT) | Reproduce → Isolate → Root-cause → Fix+Defend. Replaces shotgun-fixing with a four-step loop; every fix ships with the regression test that defends it |
| [Writing Plans](./writing-plans/README.md) | — (this library) | Free (OSS, MIT) | Turn a confirmed brief into a numbered phased plan — vertical slices, file lists, test gates, rollback notes. Pairs with Executing Plans |
| [Executing Plans](./executing-plans/README.md) | — (this library) | Free (OSS, MIT) | Drive a written plan one phase at a time with a test gate at each boundary and a confirm-pause before the next phase |

---

## 🤖 AI Agents & Automation

*Cross-functional. Tools for building autonomous agents and workflow automation.*

| Tool | Stars | Pricing | Best for |
|---|---|---|---|
| [LangChain](./langchain/README.md) | ⭐ 126,000+ | Free (OSS) | Production AI apps, RAG pipelines, agent chains |
| [AutoGPT](./autogpt/README.md) | ⭐ 167,000+ | Free (OSS) / Cloud | Autonomous goal-directed agents, no-code platform |
| [n8n](./n8n/README.md) | ⭐ 150,000+ | Free / $24/mo | No-code AI workflow automation, 600+ integrations |
| [CrewAI](./crewai/README.md) | ⭐ 44,300+ | Free (OSS) | Role-based multi-agent teams, marketing/sales workflows |
| [LangGraph](./langgraph/README.md) | ⭐ 24,800+ | Free (OSS) | Production multi-agent systems, stateful orchestration |

---

## ✍️ AI Writing & Marketing

*For Marketing, Sales, and content teams. Tools for creating and scaling content.*

| Tool | Stars | Pricing | Best for |
|---|---|---|---|
| [Jasper](./jasper/README.md) | — (closed source) | $39/mo+ | On-brand enterprise marketing content at scale |
| [Copy.ai](./copy-ai/README.md) | — (closed source) | Free / $36/mo | GTM automation, sales copy, personalised outreach |
| [Perplexity](./perplexity/README.md) | — (closed source) | Free / $20/mo | Research, competitive intel, cited content |
| [Notion AI](./notion-ai/README.md) | — (closed source) | $10/mo add-on | Teams already on Notion, meeting summaries, docs |
| [Writesonic](./writesonic/README.md) | — (closed source) | Free / $16/mo | SEO content, custom chatbots, high-volume writing |

---

## 📊 AI Data & Analytics

*For C-Level, analysts, Sales, and Marketing. Tools for insights without SQL or data science.*

| Tool | Stars | Pricing | Best for |
|---|---|---|---|
| [Julius AI](./julius-ai/README.md) | — (closed source) | Free / $20/mo | Conversational data analysis, scheduled reports |
| [Akkio](./akkio/README.md) | — (closed source) | $49/mo+ | Predictive analytics, lead scoring, churn prediction |
| [Obviously AI](./obviously-ai/README.md) | — (closed source) | $75/mo+ | Explainable ML predictions, no-code forecasting |
| [Bardeen](./bardeen/README.md) | — (closed source) | Free / $10/mo | Browser automation, web scraping, lead enrichment |
| [Polymer](./polymer/README.md) | — (closed source) | Free / $10/mo | Self-serve dashboards, shareable data visualisation |

---

## Audience Quick-Reference

| Role | Recommended tools |
|---|---|
| **IT / Engineering** | GitHub Copilot, Cursor, Continue, Aider, Windsurf, LangChain, LangGraph |
| **Marketing** | Jasper, Copy.ai, Writesonic, Notion AI, Perplexity, n8n, CrewAI |
| **Sales** | Copy.ai, Bardeen, Akkio, Julius AI, Perplexity, n8n |
| **C-Level** | Julius AI, Polymer, Perplexity, Akkio, AutoGPT, Notion AI |
| **All roles** | n8n, Perplexity, Notion AI |

---

## Roadmap

The detailed implementation plan lives in [`ROADMAP.md`](./ROADMAP.md) — 47 PRs across 8 phases, sequenced for `ailayer` adapter fixes first, then methodology / domain / CLI skills, hook + MCP bundles, and marketplace expansion.

Headline goals:

- [ ] Fix `ailayer` adapters (Codex TOML config + correct hook events; Gemini TOML slash-commands + full hook taxonomy) — Phase 0
- [ ] Add `SKILL_PROMPT.md` to all 22 existing entries — Phase 1
- [ ] Ship the methodology pack (TDD, brainstorming, plans, debugging, verification, parallel agents, worktrees) — Phase 2
- [ ] Ship domain skills (Postgres, migrations, Terraform, security review, OpenAPI, GraphQL, release engineering) — Phase 3
- [ ] Ship CLI-tooling skills (rg/fd/ast-grep, jq/yq, gh, repomix, difftastic) — Phase 4
- [ ] Ship hook + MCP bundles (`ailayer add bundle <name>`) — Phases 5–6
- [ ] Profile missing community marketplaces (`wshobson/agents`, `VoltAgent/awesome-agent-skills`) — Phase 7

---

*Built with Purpose Green · AI Tools Library · April 2026*
