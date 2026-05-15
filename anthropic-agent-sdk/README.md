# Anthropic Agent SDK

> **Category:** AI Agents & Automation | **Pricing:** Free SDK; Anthropic API usage billed separately | **Type:** Official SDK

Claude Agent SDK provides building blocks for Claude-powered agents with tool use, context management, and workflows aligned with Claude Code patterns.

## When To Use

- Use Anthropic Agent SDK when your agent runtime is Claude-centered.
- Reach for it when you need Claude-native tool use, long-context workflows, or coding-agent style orchestration.
- Consider it when you want agent behavior close to the patterns used by Claude Code.

## Practical Tips

- Keep tools narrowly scoped and explicit about side effects.
- Make context construction deliberate; large context windows still need prioritization.
- Use skills or reusable instructions for repeatable domain behavior.
- Build verification steps into any agent that edits files or calls external systems.

## Watch Outs

- Long context can make stale or irrelevant instructions harder to notice.
- Tool use needs normal software authorization and audit trails.
- Avoid assuming Claude Code behavior exactly matches a custom SDK agent.

## Links

- [Claude Agent SDK overview](https://docs.claude.com/en/docs/agent-sdk/overview)
- [Building agents with Claude Agent SDK](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk)
