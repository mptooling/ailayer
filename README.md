# AI Skills & Tools

> A curated library of AI skills, paired with **`ailayer`** — a CLI that turns each skill into a ready-to-use slash command, hook, or instruction for **Claude Code, Codex CLI, and Gemini CLI**.

Pick a skill. Run `ailayer add skill <name> --tool all`. Your agents now know how to use that tool the way *you* want them to — across every IDE.

---

## Skills, classified by aim

Each row is a directory in this repo. Click the name for the human-readable README; the agent-readable `SKILL_PROMPT.md` lives next to it.

### 🖥️ Write code

| Skill | What it gives the agent |
|---|---|
| [github-copilot](./github-copilot/) | How to use `gh copilot` CLI and author `.github/copilot-instructions.md` |
| [cursor](./cursor/) | How to write modern `.cursor/rules/*.mdc` scoped rules |
| [continue](./continue/) | How to configure `~/.continue/config.json` and slash commands |
| [aider](./aider/) | How to drive Aider interactively or from CI for batch refactors |
| [windsurf](./windsurf/) | How to constrain Windsurf's Cascade agent and its terminal allow-list |
| [caveman](./caveman/) | How to install + invoke the multi-agent caveman plugin (~75% output token cut) |
| [claude-mem](./claude-mem/) | How to install Claude-Mem and query its 3-layer MCP search for cross-session memory |

### 🤖 Build agents and automations

| Skill | What it gives the agent |
|---|---|
| [langchain](./langchain/) | LCEL composition, modern tool binding, RAG patterns |
| [langgraph](./langgraph/) | Stateful graphs, checkpointers, human-in-the-loop interrupts |
| [crewai](./crewai/) | Role-based agents, tasks, memory, tools |
| [autogpt](./autogpt/) | Agent Protocol REST + Forge SDK for custom abilities |
| [n8n](./n8n/) | Webhook triggers, native AI nodes, custom node packaging |

### ✍️ Generate content

| Skill | What it gives the agent |
|---|---|
| [jasper](./jasper/) | Brand-voiced commands and campaigns via the Jasper API |
| [copy-ai](./copy-ai/) | GTM Workflows API for personalised outreach pipelines |
| [writesonic](./writesonic/) | Per-format endpoints (SEO articles, Chatsonic, Botsonic) |
| [perplexity](./perplexity/) | Cited, web-grounded answers via the `sonar` chat-completions API |
| [notion-ai](./notion-ai/) | The official Notion API for read/write and Notion-as-RAG |

### 📊 Work with data

| Skill | What it gives the agent |
|---|---|
| [julius-ai](./julius-ai/) | Conversational data analysis from CSVs and live DB connectors |
| [akkio](./akkio/) | Predict endpoint usage with confidence-aware outputs |
| [obviously-ai](./obviously-ai/) | Predict + always-on explainability pattern |
| [bardeen](./bardeen/) | Browser-automation playbook triggers and scrape rate-limits |
| [polymer](./polymer/) | Dashboard data flow and public/private embed patterns |

> 22 skills today. Detailed comparisons (stars, pricing, integrations) live in [`INDEX.md`](./INDEX.md).

---

## How a skill is structured

Every skill directory ships two files for two audiences:

| File | For | Contents |
|---|---|---|
| `README.md` | Humans browsing the library | Repo links, summary, pricing, comparisons |
| `SKILL_PROMPT.md` | The agent that will *use* the tool | 20–40 lines of imperative HOW-TO — setup, API patterns, what to avoid |

`ailayer add skill <name>` injects `SKILL_PROMPT.md` (falling back to `README.md` only if the skill prompt is missing).

---

## Quickstart

```bash
# 1. Install the CLI
pip install -e ./ailayer --break-system-packages   # or: pipx install ./ailayer

# 2. Inject a skill
ailayer add skill langchain --tool claude          # Claude Code, global
ailayer add skill crewai    --tool all             # Claude + Codex + Gemini
ailayer add skill aider     --tool claude --no-global --project ./my-app

# 3. Inspect what's installed
ailayer status
ailayer list skills
```

Other things `ailayer` can do:

```bash
ailayer add hook lint --event pre --command "ruff check ." --tool all
ailayer add mcp filesystem --cmd npx --args "-y,@modelcontextprotocol/server-filesystem"
ailayer add instruction python-style --file ./guides/python-style.md
ailayer remove skill langchain --tool claude
```

Full CLI reference: **[`ailayer/README.md`](./ailayer/README.md)**.

---

## Adding a new skill

1. `mkdir my-skill` at the repo root.
2. Drop in a `README.md` with a `> **Category:** … | **Pricing:** … | **Type:** …` header line — the index parser uses it.
3. Drop in a `SKILL_PROMPT.md` (20–40 lines, imperative): setup, the main API/usage patterns, a short "Avoid" list. No marketing copy, no descriptions of what the tool *is* — focus on how the agent should *use* it.
4. Run `ailayer list skills` to confirm pickup.
5. Add the skill to the relevant table in this README and in [`INDEX.md`](./INDEX.md).

---

## Repo guides

- **[`INDEX.md`](./INDEX.md)** — categorised tool index with stars, pricing, audience quick-reference.
- **[`ailayer/README.md`](./ailayer/README.md)** — full CLI reference and architecture diagram.
- **[`CLAUDE.md`](./CLAUDE.md)** — operational guide for Claude Code sessions in this repo.

---

*Purpose Green · AI Skills & Tools Library · 2026*
