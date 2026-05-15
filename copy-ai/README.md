# Copy.ai

> **Category:** AI Writing & Marketing | **Pricing:** Free / $36/mo (Starter) / $186/mo (Advanced) / Enterprise | **Type:** Closed-source SaaS

---

## Repository

Copy.ai is a closed-source product. API and integration resources:

- [Copy.ai API Docs](https://api.copy.ai/docs)
- [Copy.ai GitHub (community integrations)](https://github.com/CopyAI)

---

## Documentation

- [Official Docs](https://help.copy.ai/)
- [Copy.ai API Reference](https://api.copy.ai/docs)
- [Workflows (GTM automation)](https://www.copy.ai/workflows)
- [Integrations](https://www.copy.ai/integrations)
- [Copy.ai for Sales](https://www.copy.ai/solutions/sales)
- [Pricing](https://www.copy.ai/pricing)

---

## Summary

Copy.ai started as an AI copywriting tool for ads, emails, and social posts, and has evolved into a **Go-To-Market (GTM) AI platform** — automating the entire sales and marketing content pipeline. Its **Workflows** feature lets teams build multi-step AI automations: research a prospect → write personalised outreach → generate follow-up sequences → update CRM. It has one of the largest template libraries for marketing and sales copy (1,000+ templates). Pricing includes a functional free tier, making it accessible to individuals. Copy.ai is positioned as "the AI for revenue teams" — bridging marketing content and sales outreach in one platform.

**Best for:** Sales and Marketing teams needing personalised outreach at scale, content pipelines, and GTM automation without technical overhead.

---

## Related Materials

- [Copy.ai blog](https://www.copy.ai/blog)
- [Copy.ai Workflows overview](https://www.copy.ai/workflows)
- [35+ Best AI Tools for Marketing 2026 — Saasnik](https://saasnik.com/35-best-ai-tools-for-marketing-in-2026/)
- [Best AI Marketing Tools for Startups 2026](https://www.convertmate.io/best/best-ai-marketing-tools-for-startups)
- [Copy.ai vs Jasper comparison](https://www.jasper.ai/vs/copy-ai)
- [15 AI Writing Tools Reviewed 2026 — Guideflow](https://www.guideflow.com/blog/ai-writing-tools-marketers)

---

## AI Agents That Can Use This Tool

| Agent / Framework | How it integrates |
|---|---|
| **Copy.ai Workflows** | Native agent system — autonomous multi-step GTM pipelines (research → write → enrich → send) |
| **Salesforce** | Native integration — generate personalised sales emails from CRM data |
| **HubSpot** | Native integration — trigger content generation from HubSpot contacts and deals |
| **n8n** | Copy.ai API available in n8n for custom automation workflows |
| **Zapier** | Copy.ai Zapier app — connect to 6,000+ tools for triggered content generation |
| **Outreach / Salesloft** | Direct integrations for sales sequence automation |

---

## When To Use

- Use this skill when calling the Copy.ai API to generate content or trigger Workflows from code.
- Endpoint: `POST /workflow/{workflow_id}/run`. Workflow IDs come from the URL of any workflow built in the web UI.
- Body shape: `{ "startVariables": { "<input_name>": "<value>" } }`. Input names are defined per workflow — fetch them with `GET /workflow/{id}` if you don't know them.

## Practical Tips

- Get an API key from the Copy.ai workspace under Settings → API. Send as `x-copy-ai-api-key: <key>` header.
- Base URL: `https://api.copy.ai/api/`. All payloads are JSON.

## Watch Outs

- Embedding Copy.ai keys in client-side code — calls must go through your server.
- Hard-coding workflow IDs across multiple environments; use a config map keyed by env (dev/staging/prod each have their own workspace).
- Polling more than once per second; the API will rate-limit and you'll get HTTP 429.
- Sending raw PII without checking the workspace's data-retention policy first.

---

*Last updated: April 2026*
