# AutoGPT

> **Category:** AI Agents & Automation | **Pricing:** Free (open source) + AutoGPT Platform (cloud) | **Type:** Open Source (MIT)

---

## Repository

- [GitHub — Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) ⭐ 167,000+ (most starred AI agent repo)

---

## Documentation

- [Official Docs](https://docs.agpt.co/)
- [AutoGPT Platform](https://platform.agpt.co/)
- [AutoGPT Agent Protocol](https://agentprotocol.ai/)
- [Self-hosting Guide](https://docs.agpt.co/autogpt/setup/)
- [Forge SDK (build custom agents)](https://docs.agpt.co/forge/getting-started/)
- [REST API Reference](https://docs.agpt.co/server/new_tutorial/)

---

## Summary

AutoGPT pioneered the concept of autonomous AI agents in 2023 and remains the most starred AI agent project on GitHub with 167,000+ stars. It enables GPT-4 / Claude to independently pursue multi-step goals: searching the web, writing files, executing code, and iterating without human prompts for each step. In 2025, AutoGPT transitioned from a monolithic CLI tool to a platform: the **AutoGPT Platform** provides a visual workflow builder (no-code), a marketplace of pre-built agents, and a cloud runtime. The **Forge** SDK lets developers build custom agents that run on the same infrastructure. AutoGPT established the **Agent Protocol** — now an open standard for agent interoperability.

**Best for:** Teams wanting to run autonomous goal-directed AI agents without writing code; developers building on a proven agent infrastructure.

---

## Related Materials

- [AutoGPT blog](https://agpt.co/blog)
- [Agent Protocol specification](https://agentprotocol.ai/)
- [AutoGPT Platform launch post](https://agpt.co/blog/autogpt-platform)
- [AI Agent Frameworks Compared 2026](https://remoteopenclaw.com/blog/ai-agent-frameworks-compared-2026)
- [10 Best Open Source Agent Projects 2026 — Flowith](https://flowith.io/blog/10-best-open-source-agent-projects-github-2026/)
- [Awesome AutoGPT Plugins](https://github.com/Significant-Gravitas/Auto-GPT-Plugins)

---

## AI Agents That Can Use This Tool

| Agent / Framework | How it integrates |
|---|---|
| **GPT-4 / GPT-4o** | Primary LLM backend; AutoGPT was built around OpenAI's function calling |
| **Claude** | Supported as an alternative LLM backend via API key configuration |
| **LangChain** | Many AutoGPT tools are compatible with LangChain's tool interface |
| **n8n** | n8n can trigger AutoGPT agents via HTTP requests and process outputs |
| **CrewAI** | CrewAI can spawn AutoGPT-style autonomous agents as sub-agents |

---

## When To Use

- Use this skill when running or extending AutoGPT for autonomous goal-directed agents.
- Express the goal as a single concrete outcome, not a process: "produce a market-sizing report on X with cited sources" beats "research X."
- Set `ai_role`, `ai_goals` (≤ 5), and `cost_limit` in the agent config. Without a cost limit, runaway agents will burn through API quota.

## Practical Tips

- Self-hosted: `git clone https://github.com/Significant-Gravitas/AutoGPT && cd AutoGPT && docker compose up`. Reads `OPENAI_API_KEY` and `ANTHROPIC_API_KEY` from `.env`.
- Cloud (faster start): use the AutoGPT Platform at `platform.agpt.co` for the no-code workflow builder; expose runs via its REST API.

## Watch Outs

- Letting an agent loop without `cost_limit` or `step_limit`.
- Granting filesystem write access outside the workspace dir; AutoGPT enforces a sandbox — avoid bypass it.
- Mixing the legacy CLI (`run.py`) and the Platform deployment in the same project — pick one.
- Using Claude/GPT-4 with empty system prompts; AutoGPT's planning quality drops sharply without a constrained role.

---

*Last updated: April 2026*
