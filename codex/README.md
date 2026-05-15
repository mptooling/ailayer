# Codex

> **Category:** AI Coding Assistant | **Pricing:** Paid via OpenAI plans/API usage | **Type:** Proprietary coding agent and CLI

Codex is OpenAI's software engineering agent for editing repositories, running commands, reviewing diffs, and working through coding tasks.

## When To Use

- Use Codex for repository changes that need a coding agent with shell access, file editing, and verification.
- Reach for it when you want a ChatGPT/OpenAI-native workflow for implementation, review, and iterative debugging.
- Use it alongside editor tools when terminal execution and patch review matter more than autocomplete.

## Practical Tips

- Keep prompts tied to concrete files, failing behavior, or acceptance criteria.
- Give Codex the exact verification command when the project has non-obvious test or build steps.
- Use project instructions to capture coding style, architecture boundaries, and destructive-command rules.
- Review generated diffs before merging; treat background execution as assistance, not ownership.

## Watch Outs

- Vibe-coded changes can compile while missing product intent; require user-visible acceptance checks.
- Avoid granting broad write access outside the working repository.
- Keep secrets out of prompts and logs.

## Links

- [OpenAI Codex](https://openai.com/codex/)
- [OpenAI developer docs](https://developers.openai.com/)
