# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

This repo is two things at once:

1. **A curated AI tools library** — top-level directories (`langchain/`, `cursor/`, `crewai/`, …) each contain a single `README.md` profiling one AI tool. `INDEX.md` is the master index grouping them by category (Coding Assistants, Agents & Automation, Writing & Marketing, Data & Analytics).
2. **`ailayer/`** — a Python CLI that consumes those READMEs as "skills" and injects them (plus hooks, MCP servers, and instruction blocks) into agentic coding tools (Claude Code, Codex CLI, Gemini CLI).

When editing a tool's `README.md`, you are editing skill content that `ailayer` will inject verbatim into other agents' instruction systems. When editing `ailayer/`, you are editing the injector itself.

## Skill README format

`ailayer/library.py` parses each top-level `<tool>/README.md` to extract metadata. Two conventions matter:

- **Category** is read from a line starting with `> **Category:**` (e.g. `> **Category:** AI Coding Assistant | **Pricing:** ... | **Type:** ...`). If absent, the skill is shown as "Uncategorised".
- **Summary** is the first non-header, non-blockquote, non-`---` line of the README, truncated to 120 chars.

Keep that line near the top and human-readable when editing skill READMEs.

The `ailayer` directory itself is excluded from `list_skills()` — don't add a `README.md` there expecting it to appear as a skill.

## ailayer CLI — common commands

Run from `ailayer/` unless noted. Python ≥ 3.10.

```bash
pip install -e ./ailayer --break-system-packages   # editable dev install (from repo root)
ailayer --version
ailayer status                                      # config state for all 3 tools
ailayer list tools                                  # detection table
ailayer list skills [--category Agents]             # skills from this library
ailayer add skill <name> --tool {claude|codex|gemini|all} [--no-global --project DIR]
ailayer add hook <name> --event {pre|post|stop|notification} --command "..." [--matcher Bash]
ailayer add mcp  <name> --cmd npx --args "-y,@pkg/server" [--env KEY=VAL]
ailayer add instruction <label> {--content TEXT | --file PATH}
ailayer remove {skill|hook|mcp|instruction} <name>  # mirror of add
```

There is currently **no test suite, lint config beyond `tool.ruff` line-length=100 in `pyproject.toml`, and no CI**. To run linting: `ruff check ailayer/`.

The library root for the CLI is resolved in this order: `AILAYER_LIBRARY` env var → `~/.ailayer/config` (`library_path=` line) → walk up from CWD looking for `INDEX.md` → fall back to the package's parent directory (dev convenience). When working on `ailayer` from inside this repo, no env var is needed.

## ailayer architecture

### ToolAdapter pattern

`ailayer/tools/base.py` defines an abstract `ToolAdapter`. Each agentic tool has one concrete subclass:

| Adapter | Slug | Instruction file | Settings file | Skills location |
|---|---|---|---|---|
| `ClaudeCodeAdapter` | `claude` | `~/.claude/CLAUDE.md` or `<proj>/CLAUDE.md` | `~/.claude/settings.json` (JSON) | `~/.claude/commands/<name>.md` |
| `CodexAdapter` | `codex` | `~/.codex/AGENTS.md` or `<proj>/AGENTS.md` | `~/.codex/config.yaml` (YAML) | injected as `## skill:<name>` sections inside `AGENTS.md` (Codex has no native slash-command dir) |
| `GeminiAdapter` | `gemini` | `~/.gemini/GEMINI.md` or `<proj>/GEMINI.md` | `~/.gemini/settings.json` (JSON) | `~/.gemini/commands/<name>.md` |

All three are instantiated and registered in `ailayer/tools/__init__.py` (`_ALL_ADAPTERS`). To add a fourth tool: subclass `ToolAdapter`, implement every `@abstractmethod`, append it to `_ALL_ADAPTERS`. `commands/list.py:list_tools` also has a hard-coded `feature_map` keyed by slug — update it too so the listing prints sensible feature columns.

### Hook event normalisation

Each adapter has a private `_HOOK_EVENT_ALIASES` dict mapping the user-facing flag value (`pre`, `post`, `stop`, `notification`) to the tool's native event name. Native events differ per tool:

- Claude Code: `PreToolUse`, `PostToolUse`, `Stop`, `Notification`
- Codex: `pre_apply`, `post_apply` (no equivalent for `Stop`/`Notification` — both alias to `post_apply`)
- Gemini: `beforeCommand`, `afterCommand` (same collapse)

When changing event names or adding new events, update the alias map and the `feature_map` row in `commands/list.py`.

### Idempotent injection

This is load-bearing — injection must be safe to re-run, and removal must be exact:

- **Markdown sections** (instructions, Codex skills): wrapped with an HTML comment marker `<!-- ailayer:<label> -->` directly above the `## ` heading. `_append_or_create_md` skips if the marker already exists; `_remove_md_section` finds the marker and strips through to the next `## ` heading.
- **JSON/YAML entries** (Claude/Gemini hooks): each injected hook entry carries a `_ailayer_name` field. `add_hook` checks for that name before inserting; `remove_hook` filters by it. MCP servers are keyed by their own name field, so no extra tag is needed there.

Don't bypass these markers — handwritten edits to instruction/settings files that don't include the marker will not be cleanable via `ailayer remove`.

### Scope flags

`--global` (default) targets `~/.<tool>/…`. `--project DIR` flips to project-scope; the helper `_scope` in `commands/add.py` and `commands/remove.py` returns `(global_scope, project_dir)` from the two flags. Codex hooks are global-only regardless of `--project` (they live in `~/.codex/config.yaml`).

### Console output

All user output goes through `ailayer/console.py` helpers (`ok`, `err`, `warn`, `info`) using a Rich theme. Don't `print()` directly — use these so the colour scheme stays consistent and tests (when added) can capture output.
