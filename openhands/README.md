# OpenHands

> **Category:** AI Coding Assistant (autonomous agent) | **Pricing:** Free (open source) / paid cloud | **Type:** Open Source (MIT core; `enterprise/` separately licensed)

---

## Repository

- [GitHub — OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) ⭐ 75,000+
- Homepage: [openhands.dev](https://openhands.dev)
- Language: Python (formerly OpenDevin)

---

## Documentation

- [Quick start (Docker / CLI)](https://docs.openhands.dev/usage/getting-started)
- [Software Agent SDK](https://github.com/OpenHands/software-agent-sdk)
- [LLM configuration](https://docs.openhands.dev/usage/llms/llms)
- [Cloud platform](https://www.openhands.dev/)

---

## Summary

OpenHands is an open-source platform for autonomous software-engineering agents that can do what a human developer does: read and write code, run commands in a sandboxed shell, browse the web, and call APIs. Unlike an in-editor completion assistant, an OpenHands agent takes a high-level task ("fix this failing test", "add OAuth login") and drives it to completion across many steps, observing results and self-correcting. It runs locally via Docker or CLI, ships a web UI for interactive sessions, and is model-agnostic through LiteLLM — point it at Claude, GPT, Gemini, or a local model. A managed cloud offering adds hosted sandboxes and team features. The project leads the open SWE-agent benchmarks and is the most-adopted agent in its category.

**Best for:** Engineers who want an autonomous, self-hosted coding agent that executes whole tasks in a sandbox — not just suggests completions — and who want full control over the model and runtime.

---

## Related Materials

- [Claude Code](../claude-code/README.md) — terminal-native autonomous coding; OpenHands is the open, self-hostable counterpart
- [Aider](../aider/README.md) — lighter terminal/git coding agent without a full sandboxed runtime
- [LiteLLM](../litellm/README.md) — the routing layer OpenHands uses for model flexibility
- [Codex](../codex/README.md) — OpenAI-native coding agent

---

## When To Use

- You want an agent that executes end-to-end engineering tasks in an isolated sandbox, with terminal and browser access, rather than inline suggestions.
- You need self-hosting and model choice (Claude, GPT, local) for privacy, cost, or compliance reasons.
- You want to script or embed agentic dev workflows via the Software Agent SDK.

## Practical Tips

- Fastest path: run the Docker image, open the web UI, set your LLM API key, then hand it a scoped task with a clear acceptance check.
- Pair a strong frontier model with OpenHands for planning; weaker models stall on multi-step tasks.
- Scope tasks tightly and give it a way to verify (a failing test, a lint command) — autonomous agents perform best with a built-in success signal.
- Use the SDK when you need to run agents headless in CI or batch, instead of the interactive UI.

## Watch Outs

- Agents execute real commands in the sandbox. Keep it containerized and never grant access to production credentials or unscoped cloud keys.
- Long autonomous runs burn tokens fast; set budgets and watch costs, especially with frontier models.
- The MIT license covers the core; code under `enterprise/` is licensed separately — check before commercial reuse of those parts.
- Quality scales with the underlying model — results on weaker or heavily quantized local models degrade sharply on complex tasks.

---

*Last updated: 2026-05*
