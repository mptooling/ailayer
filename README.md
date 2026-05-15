# AI Skills & Tools

> A curated, practical library of AI tools, agent skills, and workflow tips.

Use this repo as a browseable reference. Each directory contains a concise profile that explains when to use a tool or skill, what it is good for, practical tips, and common watch outs.

---

## Browse By Aim

Each row is a directory in this repo. Click the name for the human-readable profile.

### Write code

| Skill | Best used for |
|---|---|
| [github-copilot](./github-copilot/) | GitHub-native coding assistance and repository guidance |
| [cursor](./cursor/) | Deep codebase understanding, scoped rules, and model choice |
| [continue](./continue/) | Local or private coding assistance with flexible model providers |
| [aider](./aider/) | Terminal-native, git-integrated batch refactors |
| [windsurf](./windsurf/) | Autonomous multi-step coding inside an IDE |
| [caveman](./caveman/) | Terse multi-agent output and lower token usage |
| [claude-mem](./claude-mem/) | Persistent cross-session memory for coding agents |

### Methodology skills

| Skill | Best used for |
|---|---|
| [brainstorming](./brainstorming/) | Clarifying intent, scope, constraints, and success criteria before creative work |
| [verification-before-completion](./verification-before-completion/) | Requiring evidence before claiming work is complete |
| [tdd](./tdd/) | Driving features and fixes through red-green-refactor |
| [systematic-debugging](./systematic-debugging/) | Reproducing, isolating, root-causing, and defending bug fixes |
| [writing-plans](./writing-plans/) | Turning a confirmed brief into a phased implementation plan |
| [executing-plans](./executing-plans/) | Working through a written plan with checkpoints |
| [dispatching-parallel-agents](./dispatching-parallel-agents/) | Splitting independent work across parallel agents |
| [using-git-worktrees](./using-git-worktrees/) | Isolating feature work in separate worktrees |

### Build agents and automations

| Skill | Best used for |
|---|---|
| [langchain](./langchain/) | LCEL composition, modern tool binding, and RAG patterns |
| [langgraph](./langgraph/) | Stateful graphs, checkpointers, and human-in-the-loop interrupts |
| [crewai](./crewai/) | Role-based agents, tasks, memory, and tools |
| [autogpt](./autogpt/) | Agent Protocol REST and Forge SDK for custom abilities |
| [n8n](./n8n/) | Webhook triggers, native AI nodes, and custom node packaging |

### Generate content

| Skill | Best used for |
|---|---|
| [jasper](./jasper/) | Brand-voiced campaigns and enterprise marketing content |
| [copy-ai](./copy-ai/) | GTM workflows and personalised outreach pipelines |
| [writesonic](./writesonic/) | SEO articles, Chatsonic, and Botsonic workflows |
| [perplexity](./perplexity/) | Cited, web-grounded research and answers |
| [notion-ai](./notion-ai/) | Notion workspace writing, summaries, and lightweight RAG |

### Work with data

| Skill | Best used for |
|---|---|
| [julius-ai](./julius-ai/) | Conversational data analysis from CSVs and live database connectors |
| [akkio](./akkio/) | Predictive analytics with confidence-aware outputs |
| [obviously-ai](./obviously-ai/) | Explainable no-code predictions |
| [bardeen](./bardeen/) | Browser automation, scraping, and enrichment workflows |
| [polymer](./polymer/) | Dashboards, data flow, and shareable embeds |

Detailed comparisons, pricing notes, and audience quick-reference tables live in [INDEX.md](./INDEX.md).

---

## Adding Or Updating An Entry

1. Create or edit a top-level directory such as `langchain/` or `tdd/`.
2. Keep the entry in one `README.md`.
3. Include category metadata near the top using the existing blockquote style.
4. Add practical sections: `When To Use`, `Practical Tips`, and `Watch Outs`.
5. Add or update the matching row in `INDEX.md`.

## Next Step: Superpowers Enablement

After the library-only refactor is complete, enable the Superpowers workflow as contributor guidance. Superpowers should be documented as a recommended way to work on this repository, not as a product feature of the catalog.

Recommended workflows:

- Use brainstorming before adding a new tool, skill, or tip category.
- Use writing-plans for multi-entry restructures or taxonomy changes.
- Use verification-before-completion before claiming a catalog update is done.
- Use systematic-debugging only when a script, validation command, or generated artifact fails.

## Repo Guides

- [INDEX.md](./INDEX.md) — categorised tool index with pricing, audience, and recommendation notes.
- [docs/CONTRIBUTING.md](./docs/CONTRIBUTING.md) — contribution checklist for library entries.
- [AGENTS.md](./AGENTS.md) — operational guidance for Codex sessions in this repo.
- [CLAUDE.md](./CLAUDE.md) — operational guidance for Claude Code sessions in this repo.

---

*Purpose Green · AI Skills & Tools Library · 2026*
