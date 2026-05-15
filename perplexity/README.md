# Perplexity AI

> **Category:** AI Writing & Marketing (Research) | **Pricing:** Free / $20/mo (Pro) / Enterprise Pro | **Type:** Closed-source SaaS

---

## Repository

Perplexity is closed source. Developer resources:

- [Perplexity API GitHub (examples)](https://github.com/ppl-ai/api-discussion)
- [pplx-api (community wrappers)](https://github.com/topics/perplexity-api)

---

## Documentation

- [Official Docs](https://docs.perplexity.ai/)
- [Perplexity API Reference](https://docs.perplexity.ai/reference/post_chat_completions)
- [Perplexity for Business](https://www.perplexity.ai/business)
- [Supported Models](https://docs.perplexity.ai/docs/model-cards)
- [Pricing](https://www.perplexity.ai/pricing)

---

## Summary

Perplexity AI is an AI-powered answer engine that combines real-time web search with LLM reasoning to produce cited, up-to-date answers. Unlike ChatGPT or Claude (which have training cutoffs), Perplexity retrieves live information from the web and cites every source — making it the tool of choice for research, market analysis, and competitive intelligence. Key features include Deep Research (multi-step research reports), Spaces (team knowledge hubs), Collections (curated research libraries), and a developer API offering "online" model variants with live web access. Used heavily by C-Level and analysts for rapid market research and by marketers for SEO-informed content creation.

**Best for:** Research-intensive roles — market analysis, competitive intelligence, C-Level briefings, and content requiring up-to-date facts with citations.

---

## Related Materials

- [Perplexity blog](https://blog.perplexity.ai/)
- [Perplexity Deep Research announcement](https://blog.perplexity.ai/blog/perplexity-deep-research)
- [Top 10 AI Writing Tools 2026 — TheNextAI](https://www.thenextai.com/blog/top-10-ai-writing-tools-2026/)
- [Best AI Platforms 2026 — Lindy](https://www.lindy.ai/blog/ai-platforms)
- [15 AI Writing Tools for Marketers 2026 — Guideflow](https://www.guideflow.com/blog/ai-writing-tools-marketers)
- [Perplexity API integration guide](https://docs.perplexity.ai/docs/getting-started)

---

## AI Agents That Can Use This Tool

| Agent / Framework | How it integrates |
|---|---|
| **LangChain** | `langchain-community` includes a Perplexity wrapper for online search in agent chains |
| **n8n** | Perplexity API node for real-time web-searched answers in n8n workflows |
| **CrewAI** | CrewAI agents can use Perplexity as a real-time search tool |
| **Claude** | Claude can query Perplexity API results as a tool within agent workflows |
| **AutoGPT** | AutoGPT can use Perplexity as its web search backend instead of Google |

---

## When To Use

- Use this skill when calling the Perplexity API for cited, web-grounded answers from code.
- For live web search: use a `sonar` model (`sonar`, `sonar-pro`, `sonar-reasoning`). These do retrieval automatically — avoid bolt on a separate search step.
- For pure reasoning without retrieval, use `sonar-reasoning-pro`. Skip Perplexity entirely if you don't need citations — Claude/GPT-4 are cheaper.

## Practical Tips

- Get an API key from `perplexity.ai/settings/api`. Send as `Authorization: Bearer <key>`.
- Base URL: `https://api.perplexity.ai/`. The API mirrors OpenAI's chat-completions shape — most OpenAI client libs work with `base_url` overridden.

## Watch Outs

- Streaming with `sonar-reasoning` for short queries — first-token latency is high; just await the full response.
- Trusting a single citation; for high-stakes claims have the agent cross-check with a second query.
- Sending follow-up turns that depend on prior `citations` — Perplexity does not retain them across turns; restate the relevant context in the new prompt.

---

*Last updated: April 2026*
