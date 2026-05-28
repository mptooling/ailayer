# Dify

> **Category:** AI Agents & Automation (LLM app platform) | **Pricing:** Free (open source, self-host) / paid cloud | **Type:** Open Source (modified Apache-2.0 with commercial conditions)

---

## Repository

- [GitHub — langgenius/dify](https://github.com/langgenius/dify) ⭐ 143,000+
- Homepage: [dify.ai](https://dify.ai)
- Language: TypeScript + Python (Docker Compose deploy)

---

## Documentation

- [Self-hosting (Docker Compose)](https://docs.dify.ai/getting-started/install-self-hosted)
- [Workflow & agent building](https://docs.dify.ai/guides/workflow)
- [Knowledge / RAG pipelines](https://docs.dify.ai/guides/knowledge-base)
- [Plugins & tools](https://github.com/langgenius/dify-official-plugins)

---

## Summary

Dify is a low-code platform for building, shipping, and operating LLM applications and agentic workflows. It bundles the pieces most teams otherwise stitch together by hand — a visual workflow/agent builder, RAG knowledge bases with ingestion and retrieval, model management across many providers, prompt orchestration, an API/SDK to embed apps, and built-in observability — into one self-hostable interface. Non-engineers can assemble chatbots, agents, and pipelines visually, while developers drop down to code, custom tools, and the backend API when needed. It's one of the highest-starred AI projects on GitHub and is widely used as an internal "AI app factory."

**Best for:** Teams that want a single platform to design, deploy, and monitor LLM apps and agentic workflows — combining visual building for fast iteration with self-hosting for data control.

---

## Related Materials

- [n8n](../n8n/README.md) — general workflow automation; Dify is LLM-app-specific with native RAG and agent primitives
- [LangChain](../langchain/README.md) / [LangGraph](../langgraph/README.md) — code-first frameworks Dify abstracts into a visual layer
- [Langfuse](../langfuse/README.md) — pairs for deeper LLM tracing if Dify's built-in observability isn't enough
- [Qdrant](../qdrant/README.md) — a vector store Dify can use for its knowledge bases

---

## When To Use

- You want to stand up LLM-powered chatbots, agents, or RAG apps quickly without building orchestration, retrieval, and an admin UI from scratch.
- Mixed teams (PMs, ops, engineers) need to collaborate on the same app — visual for some, API/code for others.
- You need self-hosting for data residency or compliance while keeping a managed-feeling experience.

## Practical Tips

- Self-host with the official Docker Compose stack; budget for the vector DB and Redis/Postgres dependencies it brings.
- Start from a template app, then swap in your knowledge base and model provider before customizing the workflow graph.
- Use the API/SDK to embed a finished Dify app into your product rather than rebuilding the chat UI.
- Keep model keys and provider quotas in Dify's model management so you can switch providers without touching app logic.

## Watch Outs

- License is a *modified* Apache-2.0: commercial use is fine, but running it as a multi-tenant SaaS or rebranding the console requires a commercial license — read the terms before reselling.
- It's an opinionated platform, not a library; deep custom logic can hit the edges of the visual builder and push you back to code/plugins.
- Self-hosting is a multi-container deployment — plan for upgrades, backups, and the moving parts (DB, vector store, workers).
- Fast-moving project; pin versions and test upgrades, as features and schemas change between releases.

---

*Last updated: 2026-05*
