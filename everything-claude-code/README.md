# Everything Claude Code

> **Category:** AI Coding Assistant | **Type:** Open-source agent harness plugin and workflow system | **Audience:** Engineering teams using Claude Code, Codex, OpenCode, Cursor, or similar coding agents

Everything Claude Code (ECC) is an open-source collection of agent skills, hooks, rules, MCP configs, and install workflows for improving day-to-day coding-agent use across Claude Code and other harnesses.

## When To Use

- Use ECC when a team wants repeatable agent workflows for planning, TDD, code review, security checks, context management, and verification.
- Reach for it when Claude Code, Codex, OpenCode, Cursor, or similar agents need shared skills and conventions instead of one-off prompts.
- Consider it for teams standardizing how agents work across languages, repositories, and operator workflows.

## Practical Tips

- Start with the Claude Code plugin path or the manual installer, not both. Stacking install methods can duplicate skills, hooks, and runtime behavior.
- For Claude Code plugin installs, copy only the `rules/` folders you actually need, such as `rules/common` plus one language pack.
- Use the minimal or core profile first if you mainly want skills and rules without broad hook behavior.
- Treat hooks as operational policy: review what they do before enabling them across a team.
- Use ECC as a workflow layer alongside Claude Code, Codex, OpenCode, or Cursor, not as a replacement for reviewing diffs and running tests.

## Watch Outs

- The name is broader than the repo title now suggests. ECC supports multiple harnesses, but it is not an official Anthropic, OpenAI, Cursor, or OpenCode product.
- Public identifiers differ: the GitHub repo is `affaan-m/everything-claude-code`, the Claude plugin identifier is `ecc@ecc`, and the npm package is `ecc-universal`.
- Full installs can be noisy if a team only needs a few workflow skills. Prefer selective install and preview commands where possible.
- Security and memory-related workflows can touch sensitive context; review configs before using them on private repos or regulated data.

## Links

- [Everything Claude Code GitHub](https://github.com/affaan-m/everything-claude-code)
- [ECC website](https://ecc.tools)
- [Claude plugin manifest](https://github.com/affaan-m/everything-claude-code/blob/main/.claude-plugin/plugin.json)
- [Codex plugin manifest](https://github.com/affaan-m/everything-claude-code/blob/main/.codex-plugin/plugin.json)
