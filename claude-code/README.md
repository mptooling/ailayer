# Claude Code

> **Category:** AI Coding Assistant | **Pricing:** Paid via Anthropic plans/API usage | **Type:** Proprietary CLI and editor agent

Claude Code is Anthropic's agentic coding environment for delegating repository work from the terminal and supported editors.

## When To Use

- Use Claude Code for long-running coding tasks that benefit from repo-wide context, shell access, file edits, and iterative verification.
- Reach for it when you want a terminal-native agent to plan, modify, test, and explain changes in one loop.
- Pair it with project guidance files and narrow permissions for teams that need repeatable engineering behavior.

## Practical Tips

- Keep `AGENTS.md` or `CLAUDE.md` short and operational: commands, architecture notes, test gates, and repo-specific constraints.
- Prefer small, reviewable tasks with explicit verification commands over broad "build this entire app" prompts.
- Use skills, hooks, and MCP integrations only when they reduce repeated setup or improve safety.
- Treat generated code as a pull request from a fast junior engineer: review diffs, run tests, and check security-sensitive paths.

## Watch Outs

- Broad filesystem and shell permissions increase blast radius; scope access to the repository and task.
- Agent success messages are not evidence. Require command output before accepting completion claims.
- Long autonomous runs can drift from intent if the initial task lacks acceptance criteria.

## Links

- [Claude Code docs](https://docs.anthropic.com/en/docs/claude-code)
- [Anthropic docs](https://docs.anthropic.com/)
