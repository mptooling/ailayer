# Claude-Mem

> **Category:** AI Coding Assistant (memory plugin) | **Pricing:** Free (open source) | **Type:** Open Source (AGPL-3.0)

---

## Repository

- [GitHub — thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) ⭐ 71,000+
- npm: `claude-mem` (current version 6.5.0)
- Homepage: [claude-mem.ai](https://claude-mem.ai)
- Docs: [docs.claude-mem.ai](https://docs.claude-mem.ai)
- Companion: [OpenClaw integration](https://docs.claude-mem.ai/openclaw-integration)

---

## Documentation

- [Installation Guide](https://docs.claude-mem.ai/installation)
- [Gemini CLI Setup](https://docs.claude-mem.ai/gemini-cli/setup)
- [Search Tools (3-layer workflow)](https://docs.claude-mem.ai/usage/search-tools)
- [Architecture Overview](https://docs.claude-mem.ai/architecture/overview)
- [Hooks Reference (7 lifecycle scripts)](https://docs.claude-mem.ai/architecture/hooks)
- [Worker Service (HTTP API)](https://docs.claude-mem.ai/architecture/worker-service)
- [Database & FTS5 search](https://docs.claude-mem.ai/architecture/database)
- [Configuration](https://docs.claude-mem.ai/configuration)
- [Progressive Disclosure (philosophy)](https://docs.claude-mem.ai/progressive-disclosure)

---

## Summary

Claude-Mem is a persistent memory compression system that gives Claude Code (and Gemini CLI / OpenCode) long-term memory across sessions. It hooks into 5 session lifecycle events (`SessionStart`, `UserPromptSubmit`, `PostToolUse`, `Stop`, `SessionEnd`), captures everything the agent does, compresses observations using Claude's Agent SDK, and re-injects relevant context into future sessions automatically. A local worker service on port 37777 exposes an HTTP API plus a real-time web viewer; observations are stored in SQLite with FTS5 full-text search and a Chroma vector DB for hybrid semantic + keyword retrieval. The agent-facing surface is a `mem-search` skill plus 4 MCP tools that follow a token-efficient **3-layer workflow**: `search` returns a compact index, `timeline` reconstructs chronological context around an observation, and `get_observations` fetches full details only for the IDs you actually need — claimed ~10× token savings versus naive retrieval. Privacy controls include `<private>` tags that exclude content from storage. Multi-language modes (English, Chinese, Japanese, …) are switched via `CLAUDE_MEM_MODE`. AGPL-3.0 — modifications deployed on a network server must be open-sourced.

**Best for:** Engineers running long-lived projects who want context to survive across Claude Code sessions; teams that need auditable, queryable memory of what an agent did and why; anyone hitting context-window limits in long debugging or research arcs.

---

## Related Materials

- [Trendshift listing](https://trendshift.io/repositories/15496)
- [Awesome Claude Code](https://github.com/thedotmack/awesome-claude-code)
- [Architecture Evolution v3 → v5](https://docs.claude-mem.ai/architecture-evolution)
- [Beta Features (Endless Mode)](https://docs.claude-mem.ai/beta-features)
- [Context Engineering primer](https://docs.claude-mem.ai/context-engineering)
- Discord: [discord.gg/J4wttp9vDu](https://discord.com/invite/J4wttp9vDu)
- X: [@Claude_Memory](https://x.com/Claude_Memory)

---

## AI Agents That Can Use This Tool

| Agent / Framework | How it integrates |
|---|---|
| **Claude Code** | Native plugin via `/plugin install claude-mem` or `npx claude-mem install`; wires 5 lifecycle hooks, statusline, and the `mem-search` skill |
| **Gemini CLI** | First-class support via `npx claude-mem install --ide gemini-cli` |
| **OpenCode** | Supported via `npx claude-mem install --ide opencode` |
| **OpenClaw gateways** | One-line installer `curl -fsSL https://install.cmem.ai/openclaw.sh | bash` for persistent memory at the gateway layer |
| **Claude Desktop** | "Claude Desktop Skill" lets you query the same memory store from desktop conversations |
| **MCP-compatible agents** | The 4 search tools (`search`, `timeline`, `get_observations`, …) are exposed via MCP and consumable by any MCP-aware client |

---

*Last updated: 2026-05*
