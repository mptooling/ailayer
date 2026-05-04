# AI Tools & Skills Library

> A curated, living library of the most impactful AI tools — categorised by use case, ranked by adoption, and documented for IT, Marketing, Sales, and C-Level audiences.
>
> **Last updated:** April 2026 | **Tools documented:** 20 | **Next step:** per-tool automation & enablement guides

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

- [ ] Add automation scripts per tool (setup, API examples)
- [ ] Add internal enablement guides per role
- [ ] Add cost comparison matrix
- [ ] Add security & compliance notes per tool
- [ ] Expand to 40+ tools (second batch)

---

*Built with Purpose Green · AI Tools Library · April 2026*
