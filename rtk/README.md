# RTK (Rust Token Killer)

> **Category:** AI Coding Assistant (CLI proxy) | **Pricing:** Free (open source) | **Type:** Open Source (Apache-2.0)

---

## Repository

- [GitHub — rtk-ai/rtk](https://github.com/rtk-ai/rtk) ⭐ 54,000+
- Homepage: [rtk-ai.app](https://www.rtk-ai.app)
- Language: Rust (single static binary, ~zero dependencies, <10ms overhead per call)

---

## Documentation

- [Installation (Homebrew, Cargo, curl)](https://github.com/rtk-ai/rtk#installation)
- [Quick start & agent init flags](https://github.com/rtk-ai/rtk#quick-start)
- [Architecture notes](https://github.com/rtk-ai/rtk/blob/master/docs/contributing/ARCHITECTURE.md)
- [Troubleshooting guide](https://www.rtk-ai.app/guide/troubleshooting)

---

## Summary

RTK is a CLI proxy that sits between a coding agent and the shell, filtering and compressing the output of common dev commands before it ever reaches the model's context window. The repo claims **60–90% token savings** across a typical Claude Code / Codex / Gemini CLI session, with four reduction strategies applied per command type: smart filtering (drops noise like comments, whitespace, boilerplate), grouping (aggregates files by directory, errors by rule/type), truncation (keeps relevant context, cuts redundancy), and deduplication (collapses repeated log lines with counts). RTK wraps 100+ commands across files (`ls`, `read`, `find`, `grep`, `diff`), git, GitHub CLI, test runners (jest, vitest, pytest, go test, cargo test, rspec, playwright), linters (eslint, biome, tsc, ruff, clippy, golangci-lint, rubocop), package managers, AWS CLI, Docker/Kubernetes, and arbitrary commands via `rtk err <cmd>` or `rtk proxy <cmd>`. After `rtk init`, hook- or plugin-based agents automatically rewrite tool calls (e.g. `git status` → `rtk git status`) so the agent receives compact output without changing its own behavior. Built-in analytics (`rtk gain`) report cumulative token savings per session.

**Best for:** Engineers running long autonomous coding sessions where shell-output volume — repeated `cat`, `grep`, `git diff`, `cargo test`, `pytest`, `tsc`, `docker logs` — dominates context-window pressure and cost.

---

## Related Materials

- [Caveman](../caveman/README.md) — compresses *agent output prose*; complementary to RTK (which compresses *tool output*)
- [Claude-Mem](../claude-mem/README.md) — persistent cross-session memory; another axis of context-window reduction
- [Anthropic — prompt caching docs](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching) — pairs well with output-side compression

---

## AI Agents That Can Use This Tool

| Agent / Framework | How it integrates |
|---|---|
| **Claude Code / GitHub Copilot** | Default: `rtk init -g` writes Bash hook that rewrites tool calls |
| **Gemini CLI** | `rtk init -g --gemini` |
| **Codex CLI (OpenAI)** | `rtk init -g --codex` |
| **Cursor** | `rtk init --agent cursor` |
| **Windsurf** | `rtk init --agent windsurf` |
| **Cline / Roo Code** | `rtk init --agent cline` |
| **Kilo Code, Antigravity, Hermes** | `rtk init --agent <name>` (plugin API for Hermes) |
| **Any shell-using agent** | Manual wrapping: prefix commands with `rtk` (e.g. `rtk git diff`, `rtk pytest`) |

> The Bash hook only intercepts shell commands. Claude Code's native `Read`, `Grep`, `Glob` tools bypass the hook — use `rtk read`, `rtk grep`, `rtk find` explicitly, or steer the agent to shell equivalents, to capture savings there too.

---

## When To Use

- You're burning context on repetitive shell output: `git status`, `git diff`, `cat`/`read` of long files, `cargo test`/`pytest`/`jest` failures buried under noise, verbose AWS/Docker/Kubernetes responses.
- A session frequently hits compaction or runs over budget mid-task and you want a single binary fix rather than per-prompt discipline.
- You want measurable savings (`rtk gain`) to justify cost or context-window decisions to a team.

## Practical Tips

- Install: `brew install rtk`, or `curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/refs/heads/master/install.sh | sh` (Linux/macOS), or `cargo install --git https://github.com/rtk-ai/rtk`.
- After install, run `rtk init -g` (Claude Code default), restart the agent, then verify with `rtk --version` and `rtk gain`.
- Aggressive read mode strips function bodies and keeps signatures only: `rtk read file.rs -l aggressive` — great for letting an agent map a large module without ingesting it whole.
- Use `rtk err <cmd>` and `rtk test <cmd>` as generic wrappers for tools RTK doesn't natively recognize — keeps failure-only output for any test/lint runner.
- Track real impact: run `rtk gain` at the end of a session before claiming the 60–90% number — actual savings depend on which commands dominate the workload.

## Watch Outs

- Hooks only catch Bash-tool invocations. Claude Code's `Read`/`Grep`/`Glob` and analogous built-in tools in other agents bypass RTK silently; savings on those workflows require switching to shell or `rtk read`/`rtk grep`.
- Filtering is lossy by design. Workflows that depend on full, unmodified output (security forensics, byte-exact diffs, debugging the filter itself) should use `rtk proxy <cmd>` for raw passthrough or skip RTK for that step.
- Name collision on crates.io with an unrelated "rtk" (Rust Type Kit). If `rtk gain` errors after `cargo install rtk`, install from the git repo instead.
- Windows: full hook system requires WSL; the bare `.exe` works only when invoked from a real terminal (Command Prompt, PowerShell, Windows Terminal).
- Apache-2.0 licensed and CLI-resident, but it still pre-processes everything your agent reads. Review the filter rules before using on regulated codebases where evidence of what the agent saw matters.

---

*Last updated: 2026-05*
