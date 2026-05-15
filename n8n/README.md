# n8n

> **Category:** AI Agents & Automation | **Pricing:** Free (self-hosted) / $24/mo (Cloud Starter) / Enterprise | **Type:** Open Source (Fair-code, source-available)

---

## Repository

- [GitHub — n8n-io/n8n](https://github.com/n8n-io/n8n) ⭐ 150,000+

---

## Documentation

- [Official Docs](https://docs.n8n.io/)
- [Getting Started](https://docs.n8n.io/getting-started/)
- [AI Nodes & Agents](https://docs.n8n.io/langchain/)
- [Integrations (600+ apps)](https://n8n.io/integrations/)
- [Self-hosting Guide](https://docs.n8n.io/hosting/)
- [n8n API Reference](https://docs.n8n.io/api/)
- [Pricing](https://n8n.io/pricing/)

---

## Summary

n8n is the most starred workflow automation platform on GitHub (150,000+), often called "the Zapier for developers." It provides a visual node-based workflow builder with deep AI integration — natively embedding LangChain's agent capabilities directly in workflows. You can chain together 600+ app integrations (Slack, Gmail, Salesforce, GitHub, databases) and insert AI decision points, LLM calls, or fully autonomous agent sub-workflows at any point. In 2025–2026, n8n positioned itself as "the action layer for AI agents," making it the go-to tool for teams that want to build AI-powered automations without writing a full application. Self-hostable for full data sovereignty.

**Best for:** IT and Marketing/Sales teams building AI-powered automations across their existing tool stack; any team that wants no-code AI workflows with enterprise-grade control.

---

## Related Materials

- [n8n blog](https://blog.n8n.io/)
- [n8n AI/LangChain integration announcement](https://blog.n8n.io/langchain/)
- [n8n community templates](https://n8n.io/workflows/)
- [n8n vs Zapier vs Make comparison](https://blog.n8n.io/n8n-vs-zapier/)
- [AI Agent Frameworks for Solopreneurs 2026](https://f3fundit.com/ai-agent-frameworks-solopreneurs-langchain-crewai-autogpt-n8n-2026/)
- [120+ Agentic AI Tools 2026 — StackOne](https://www.stackone.com/blog/ai-agent-tools-landscape-2026/)

---

## AI Agents That Can Use This Tool

| Agent / Framework | How it integrates |
|---|---|
| **LangChain** | Native LangChain nodes — chains, agents, memory, vector stores all available as n8n nodes |
| **Claude** | Claude API node for LLM calls; supports function calling and tool use |
| **OpenAI / GPT-4** | Deep integration with OpenAI models, assistants, and DALL-E |
| **AutoGPT** | n8n can trigger AutoGPT via HTTP and process structured outputs |
| **CrewAI** | n8n can orchestrate CrewAI crew runs as sub-workflow steps |
| **Zapier / Make** | n8n serves as a self-hosted alternative that can replace both |

---

## When To Use

- Use this skill when triggering or extending n8n workflows from code, or authoring AI-powered workflows.
- Build the workflow in the UI; expose it with a Webhook trigger node — the cleanest contract for code-to-n8n calls.
- Call `POST <webhook_url>` with the payload the workflow's first node expects. The webhook URL is shown in the trigger node config.

## Practical Tips

- Self-host: `docker run -it --rm -p 5678:5678 -v ~/.n8n:/home/node/.n8n n8nio/n8n`. Cloud: `n8n.cloud`. Both expose the same REST API.
- Generate an API key in Settings → API. Send as `X-N8N-API-KEY: <key>`. Base URL `<host>/api/v1/`.

## Watch Outs

- Storing credentials in workflow JSON; always use the Credentials store and reference by ID.
- Webhook-triggered workflows that exceed 5 minutes — n8n returns `504` to the caller. For long jobs, return immediately and notify on completion.
- Treating the AI Agent node as deterministic; pin temperature low and add a "Validate Output" code step before downstream side effects.
- Mixing self-hosted and cloud workflows in one repo without env-specific webhook URLs in config.

---

*Last updated: April 2026*
