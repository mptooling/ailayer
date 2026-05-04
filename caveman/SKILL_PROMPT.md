# Caveman skill

Use this skill when installing or driving the `caveman` plugin to put a coding agent into terse, token-reduced response mode.

## Install

- Universal one-liner (auto-detects 30+ agents):
  - macOS / Linux / WSL: `curl -fsSL https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.sh | bash`
  - Windows PowerShell: `irm https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.ps1 | iex`
- Useful flags: `--minimal` (plugin only, no hooks/MCP), `--all` (plugin + hooks + statusline + MCP shrink + per-repo rules), `--dry-run`, `--only <agent>`, `--list`, `--force`.
- Manual per-agent install:
  - Claude Code: `claude plugin marketplace add JuliusBrussee/caveman && claude plugin install caveman@caveman`
  - Gemini CLI: `gemini extensions install https://github.com/JuliusBrussee/caveman`
  - Cursor / Windsurf / Cline / Copilot: `npx skills add JuliusBrussee/caveman -a <cursor|windsurf|cline|github-copilot>`
  - Anything else: `npx skills add JuliusBrussee/caveman` (auto-detect).
- Uninstall: `claude plugin disable caveman` / `gemini extensions uninstall caveman` / `npx skills remove caveman`.

## Activate

- Trigger inside an agent session with `/caveman` (Claude Code, Gemini CLI), `$caveman` (Codex), or any of: "talk like caveman", "caveman mode", "less tokens please".
- Pick intensity at activation: `/caveman lite` (light trim), `/caveman full` (default, ~75% output cut), `/caveman ultra` (maximum compression, fragment-style), `/caveman wenyan` (classical Chinese 文言文 mode).
- Toggle off with `/caveman off` or restart the session.

## Sub-skills (Claude Code)

- `caveman-commit` — write terse, fragment-style commit messages.
- `caveman-review` — one-line code review comments.
- `caveman-compress` — compress an attached doc/diff before sending it on; pairs with the MCP shrink proxy to cut input tokens too.
- `caveman-stats` — print lifetime tokens-saved badge.

## Per-repo auto-start

- Run the installer with `--with-init` (or `--all`) to drop `.cursor/rules/caveman.mdc`, `.windsurf/rules/caveman.md`, `.clinerules/caveman.md`, `.github/copilot-instructions.md`, and `AGENTS.md` into the current repo. The agent will auto-engage caveman mode in that repo only.
- For Claude Code without per-repo init, the plugin's hooks and statusline are global once installed.

## Avoid

- Caveman mode in customer-facing or written-deliverable contexts (PR descriptions for stakeholders, user-facing docs, support replies). The terseness reads as rude outside engineering channels.
- Running `--with-init` in a shared repo without the team's agreement — it commits a coding-style preference into project files.
- Stacking caveman with other prose-style rules; conflicting instructions degrade output. Pick one voice per agent profile.
- Trusting the 75% number for *every* prompt — savings range 22–87% depending on task. Use `caveman-stats` to measure your actual ratio before claiming wins.
