# Jasper

> **Category:** AI Writing & Marketing | **Pricing:** $39/mo (Creator) / $59/mo (Pro) / Enterprise | **Type:** Closed-source SaaS

---

## Repository

Jasper is a closed-source commercial product. No public GitHub repo. Developer resources:

- [Jasper API Documentation](https://developers.jasper.ai/)
- [Jasper GitHub (API SDKs)](https://github.com/jasper-ai)

---

## Documentation

- [Official Docs](https://www.jasper.ai/resources)
- [Jasper API Docs](https://developers.jasper.ai/)
- [Jasper Brand Voice Setup](https://support.jasper.ai/hc/en-us/articles/10362677741835)
- [Jasper Campaigns](https://www.jasper.ai/campaigns)
- [Jasper for Teams](https://www.jasper.ai/teams)
- [Pricing](https://www.jasper.ai/pricing)

---

## Summary

Jasper is the leading AI writing platform purpose-built for enterprise marketing teams. Its core differentiator is **Brand Voice** — you upload brand guidelines, tone documents, and example content, and Jasper generates copy that stays on-brand at scale. Key capabilities include long-form blog writing, ad copy, email campaigns, social media posts, SEO content, and a "Campaigns" feature that generates all content variants for a campaign simultaneously. In 2025–2026, Jasper expanded into AI agents for marketing workflows — autonomously researching, drafting, reviewing, and publishing content pipelines. Used by IBM, Anthropic, HubSpot, and 100,000+ marketing teams.

**Best for:** Marketing teams needing consistent on-brand content at scale; enterprise marketing operations with complex approval workflows.

---

## Related Materials

- [Jasper blog](https://www.jasper.ai/blog)
- [Jasper vs Copy.ai comparison](https://www.jasper.ai/vs/copy-ai)
- [35+ Best AI Tools for Marketing 2026 — Saasnik](https://saasnik.com/35-best-ai-tools-for-marketing-in-2026/)
- [Jasper AI Alternatives 2026](https://www.empler.ai/blog/10-best-jasper-ai-alternatives-2026-cheaper-ai-writing-tools)
- [15 AI Writing Tools for Marketers 2026 — Guideflow](https://www.guideflow.com/blog/ai-writing-tools-marketers)
- [Best AI Writing Tools 2026 — ToolChase](https://toolchase.com/blog/best-ai-writing-tools-2026/)

---

## AI Agents That Can Use This Tool

| Agent / Framework | How it integrates |
|---|---|
| **Jasper AI Agents** | Native agent system (2025) — plans and executes full marketing campaigns autonomously |
| **n8n** | Jasper API integration in n8n for automated content generation pipelines |
| **Zapier** | Jasper has a Zapier integration — trigger content generation from CRM events |
| **HubSpot** | Native HubSpot integration — generate email and landing page copy in-app |
| **Make (Integromat)** | Jasper API available in Make for multi-step content workflows |

---

## When To Use

- Use this skill when calling the Jasper API to generate brand-aligned marketing content from code.
- Endpoint: `POST /commands/run` with `{ "command": "<command_name>", "inputs": {...}, "brand_voice_id": "...", "knowledge_base_ids": [...] }`.
- Common commands: `blog-post-outline`, `email-subject-lines`, `product-description`, `social-media-post`. Full list under `GET /commands`.

## Practical Tips

- Get an API key from Jasper under Account → API. Send as `Authorization: Bearer <key>`. Base URL `https://api.jasper.ai/v1/`.
- Brand Voice and Knowledge Base are *workspace*-level concepts. Configure them in the UI; the API merely references them by ID.

## Watch Outs

- Storing API keys in the front end — Jasper enforces server-side use only.
- Using Jasper for code generation; it's tuned for marketing prose and will produce low-quality code.
- Re-running the same prompt to get variants — pass `n: <int>` to get multiple outputs per call.

---

*Last updated: April 2026*
