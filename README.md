# AI Skills & Tools

A curated library of AI tools, paired with **ailayer** — a small CLI that turns each tool's documentation into ready-to-use skills for agentic coding tools (Claude Code, Codex CLI, Gemini CLI).

The library and the CLI live in one repo so they stay in sync: edit a tool's `SKILL_PROMPT.md`, run `ailayer add skill <name>`, and your agent picks up the latest guidance the next time it starts.

---

## What's inside

```
ai_skills_and_tools/
├── INDEX.md                    ← master index, grouped by category
├── README.md                   ← this file
├── CLAUDE.md                   ← repo guide for Claude Code sessions
│
├── langchain/
│   ├── README.md               ← human docs (links, summary, comparisons)
│   └── SKILL_PROMPT.md         ← agent prompt (how to use it in code)
├── crewai/         …
├── aider/          …
├── …  (20 tools total, see INDEX.md)
│
└── ailayer/                    ← the CLI
    ├── pyproject.toml
    ├── README.md               ← ailayer's own docs
    └── ailayer/
        ├── main.py             ← Typer entry point
        ├── library.py          ← reads tool dirs from this repo
        ├── tools/              ← Claude Code / Codex / Gemini adapters
        └── commands/           ← add / remove / list / status
```

The 20 tools are categorised under **AI Coding Assistants**, **AI Agents & Automation**, **AI Writing & Marketing**, and **AI Data & Analytics** — see `INDEX.md` for the full table.

---

## Two files per tool

Each tool directory contains two files with different audiences:

| File | Audience | Content |
|---|---|---|
| `README.md` | Humans browsing the library | Repo links, official docs, plain-English summary, comparisons, integrations |
| `SKILL_PROMPT.md` | The AI agent that will use the tool | Imperative HOW-TO: setup, API patterns, idiomatic usage, what to avoid |

`ailayer add skill <name>` injects the `SKILL_PROMPT.md`. If a tool has none yet, ailayer falls back to its `README.md` — but READMEs are documentation, not prompts, so always prefer a dedicated skill file.

---

## Quickstart

### Install ailayer

```bash
# editable dev install
pip install -e ./ailayer --break-system-packages

# or isolated via pipx
pipx install ./ailayer
```

Optionally pin the library location (auto-detected when running from inside the repo):

```bash
export AILAYER_LIBRARY=~/ai_skills_and_tools
```

### Inject a skill into Claude Code

```bash
ailayer add skill langchain --tool claude         # global, ~/.claude/commands/
ailayer add skill crewai   --tool all             # also installs to Codex + Gemini
ailayer add skill aider    --tool claude --no-global --project ./my-app
```

### Other things ailayer does

```bash
ailayer status                                    # show config state for all 3 tools
ailayer list skills [--category Agents]
ailayer list tools

ailayer add hook lint --event pre  --command "ruff check ." --tool all
ailayer add mcp filesystem --cmd npx --args "-y,@modelcontextprotocol/server-filesystem"
ailayer add instruction python-style --file ./guides/python-style.md

ailayer remove skill langchain --tool claude
```

Full ailayer reference: [`ailayer/README.md`](./ailayer/README.md).

---

## Adding a new tool to the library

1. Create a directory at the repo root: `mkdir my-tool`.
2. Add `README.md` following the pattern of existing tools — first non-header line should be a one-sentence summary; include a `> **Category:** … | **Pricing:** … | **Type:** …` line so the index parser picks it up.
3. Add `SKILL_PROMPT.md` (20–40 lines): short imperative sentences telling an AI agent how to *use* the tool in code. Cover setup, the main API/usage patterns, and a short "Avoid" list.
4. Run `ailayer list skills` to confirm it shows up.
5. Add the tool to the relevant table in `INDEX.md`.

---

## Repo guides

- **[`INDEX.md`](./INDEX.md)** — categorised tool index with stars, pricing, and audience.
- **[`CLAUDE.md`](./CLAUDE.md)** — operational guide for Claude Code sessions in this repo (architecture of `ailayer`, idempotent injection markers, hook-event normalisation).
- **[`ailayer/README.md`](./ailayer/README.md)** — full CLI reference.

---

*Purpose Green · AI Tools Library · 2026*
