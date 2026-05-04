# Claude-Mem skill

Use this skill when installing or querying Claude-Mem to give a coding agent persistent memory across sessions.

## Install

- Default (Claude Code): `npx claude-mem install`. Restart Claude Code afterwards — memory from prior sessions appears automatically.
- Gemini CLI: `npx claude-mem install --ide gemini-cli` (auto-detects `~/.gemini`).
- OpenCode: `npx claude-mem install --ide opencode`.
- From inside Claude Code's plugin marketplace: `/plugin marketplace add thedotmack/claude-mem` then `/plugin install claude-mem`.
- OpenClaw gateways: `curl -fsSL https://install.cmem.ai/openclaw.sh | bash`.
- Do **not** rely on `npm install -g claude-mem` — that ships the SDK only and skips the hooks/worker setup.

## System requirements

- Node ≥ 18.
- Bun (auto-installed if missing) — used to manage the worker process.
- `uv` (auto-installed if missing) — Python package manager for the vector store.
- Claude Code recent enough to support plugins.

## How it works in practice

- After install, 5 lifecycle hooks fire automatically (`SessionStart`, `UserPromptSubmit`, `PostToolUse`, `Stop`, `SessionEnd`). No manual capture call is needed.
- A local worker runs on `http://localhost:37777` with a web viewer and 10 search endpoints. If the port is taken, edit `~/.claude-mem/settings.json` before restart.
- Observations land in SQLite with FTS5; semantic search is via a Chroma vector DB.

## Searching memory (the 3-layer workflow)

Always go layer-by-layer — fetching full details up front bloats the context window. The MCP tools enforce the pattern:

1. `search(query="<text>", type="<bugfix|decision|...>", project="...", limit=10)` — returns a compact index of `{id, summary, project, type, timestamp}` (~50–100 tokens per row).
2. `timeline(observation_id=<id>)` *or* `timeline(query="...")` — reconstructs the chronological context around an interesting result.
3. `get_observations(ids=[<id1>, <id2>, ...])` — full details only for the IDs you've already filtered. Always batch IDs in one call; don't loop.

Approximate token savings: ~10× versus naive "fetch everything." If you find yourself calling `get_observations` for more than 5–10 IDs at once, your `search` query was too broad — narrow it.

## Privacy and configuration

- Wrap any sensitive prompt content in `<private>...</private>` tags to exclude it from storage. Defaults are conservative but the tag is the explicit guarantee.
- Settings: `~/.claude-mem/settings.json` (created on first run). Common keys: `CLAUDE_MEM_MODE` (e.g. `code`, `code--zh`, `code--ja`), `worker.port`, `dataDir`, `logLevel`, `context.injection`.
- After changing `CLAUDE_MEM_MODE`, restart the agent.

## Citing past observations

- Reference a memory by its observation ID; the web viewer at `http://localhost:37777/api/observation/{id}` returns the full record. Include the URL in commit messages or PR descriptions when an agent's decision is grounded in past memory.

## Avoid

- Sharing or syncing `~/.claude-mem/` between machines without thinking — it contains the full content of every observed session, including any prompt the user didn't tag `<private>`.
- Long-running queries on huge memory stores without `limit` and `project` filters; the worker will OOM the search process.
- Bypassing `search` and going straight to `get_observations` with hand-picked IDs unless you already know the ID — the index step is the cheap part.
- Deploying a modified Claude-Mem on a network-reachable server without publishing your changes — the AGPL-3.0 license requires it.
