# ailayer

> **Alpha v0.1** — CLI automation layer for agentic coding tools.  
> macOS · Linux · Python 3.10+

`ailayer` injects skills, hooks, MCP server configs, and instruction files into your agentic coding tools — from a single command, across all supported tools at once.

**Supported tools (alpha):**

| Tool | CLI binary | Instruction file | Hooks | MCP | Skills |
|---|---|---|---|---|---|
| Claude Code | `claude` | `CLAUDE.md` | `settings.json` hooks | `settings.json` mcpServers | `~/.claude/commands/*.md` |
| Codex CLI | `codex` | `AGENTS.md` | `config.yaml` hooks | `config.yaml` mcp_servers | via `AGENTS.md` sections |
| Gemini CLI | `gemini` | `GEMINI.md` | `settings.json` hooks | `settings.json` mcpServers | `~/.gemini/commands/*.md` |

Skills are sourced from your `ai_skills_and_tools` library (the parent directory).

---

## Install

```bash
# Option 1 — pipx (recommended, isolated)
pipx install ./ailayer

# Option 2 — pip
pip install ./ailayer --break-system-packages

# Option 3 — editable dev install
pip install -e ./ailayer --break-system-packages
```

Point ailayer at the library (if not auto-detected):

```bash
export AILAYER_LIBRARY=~/ai_skills_and_tools
# or add to ~/.zshrc / ~/.bashrc
```

---

## Usage

### Check status of all tools

```bash
ailayer status
```

### List available skills from the library

```bash
ailayer list skills
ailayer list skills --category "Agents"
```

### List supported tools

```bash
ailayer list tools
```

---

### Add a skill

Install a library skill into a tool's slash-command / instruction system:

```bash
# Add 'langchain' skill to Claude Code globally
ailayer add skill langchain --tool claude

# Add 'crewai' skill to all tools
ailayer add skill crewai --tool all

# Add to a specific project only
ailayer add skill aider --tool claude --no-global --project ./my-project
```

### Add a hook

```bash
# Run ruff before every tool write (pre-hook), all tools
ailayer add hook lint --event pre --command "ruff check ." --tool all

# Run pytest after writes, Claude Code only, match Bash tool
ailayer add hook run-tests --event post --command "pytest -x -q" --tool claude --matcher Bash

# Run a git check before Codex applies changes
ailayer add hook git-status --event pre --command "git status --short" --tool codex
```

### Add an MCP server

```bash
# Add the filesystem MCP to Claude Code
ailayer add mcp filesystem \
  --cmd npx \
  --args "-y,@modelcontextprotocol/server-filesystem" \
  --tool claude

# Add to all tools with an env var
ailayer add mcp my-db \
  --cmd python \
  --args "-m,my_mcp_server" \
  --env "DB_URL=postgresql://localhost/mydb" \
  --tool all
```

### Add a custom instruction

```bash
# From a file
ailayer add instruction python-style --file ./guides/python-style.md --tool all

# Inline
ailayer add instruction api-key-rule \
  --content "Never hard-code API keys. Always use environment variables." \
  --tool claude
```

---

### Remove anything

```bash
ailayer remove skill langchain --tool claude
ailayer remove hook lint --tool all
ailayer remove mcp filesystem --tool claude
ailayer remove instruction python-style --tool all
```

---

## How it works

```
ai_skills_and_tools/
├── INDEX.md
├── langchain/README.md      ← skill content
├── crewai/README.md
├── ...
└── ailayer/                 ← this tool
    ├── pyproject.toml
    └── ailayer/
        ├── main.py          ← CLI entry point (Typer)
        ├── library.py       ← reads skill READMEs from parent dir
        ├── tools/
        │   ├── base.py      ← abstract ToolAdapter
        │   ├── claude_code.py
        │   ├── codex.py
        │   └── gemini.py
        └── commands/
            ├── add.py
            ├── remove.py
            ├── list.py
            └── status.py
```

**Injection is idempotent** — running the same `add` command twice is safe; the second call warns and skips.

**Scope:** `--global` (default) writes to `~/.tool/` config. `--project DIR` writes to the project directory.

**ailayer tracks its injections** using `<!-- ailayer:label -->` markers in markdown files and `_ailayer_name` tags in JSON/YAML configs — making removal clean and reliable.

---

## Roadmap (beta)

- [ ] `ailayer init` — interactive project setup wizard
- [ ] `ailayer sync` — re-sync all installed skills when the library updates
- [ ] Homebrew formula and `curl | sh` installer
- [ ] Plugin system for adding custom tool adapters
- [ ] Shell completions (bash, zsh, fish)

---

## Contributing

PRs welcome. Add a new tool adapter by subclassing `ailayer.tools.base.ToolAdapter` and registering it in `ailayer/tools/__init__.py`.

---

*Purpose Green · ailayer v0.1.0-alpha · April 2026*
