# Cline

> **Category:** AI Coding Assistant | **Pricing:** Free OSS client; model/API costs vary | **Type:** Open-source VS Code agent

Cline is an open-source autonomous coding agent for VS Code that can edit files, run terminal commands, inspect browser state, and use MCP tools.

## When To Use

- Use Cline when you want a transparent VS Code agent with bring-your-own-model flexibility.
- Reach for it for hands-on agent workflows where approving file changes and terminal actions is part of the loop.
- Prefer it when MCP integrations matter and you want an open extension rather than a closed IDE fork.

## Practical Tips

- Start with strict approval settings for terminal commands and file writes.
- Use project rules to encode test commands, framework conventions, and prohibited operations.
- Pair with local models for privacy-sensitive repos, and frontier models for complex refactors.
- Keep MCP servers minimal and task-specific.

## Watch Outs

- The more tools Cline can call, the more important prompt-injection and permission hygiene become.
- Long runs can accumulate expensive model calls; set budgets and stop conditions.
- Always inspect terminal commands before approval.

## Links

- [Cline website](https://cline.bot/)
- [Cline GitHub](https://github.com/cline/cline)
