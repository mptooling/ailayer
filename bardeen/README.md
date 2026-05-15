# Bardeen

> **Category:** AI Data & Analytics / Automation | **Pricing:** Free / $10/mo (Professional) / $20/mo (Business) | **Type:** Closed-source SaaS (Chrome Extension)

---

## Repository

Bardeen is closed source. Community resources:

- [Bardeen GitHub (integrations/examples)](https://github.com/bardeenai)
- [Bardeen community playbooks](https://www.bardeen.ai/playbooks)

---

## Documentation

- [Official Docs](https://www.bardeen.ai/docs)
- [Getting Started](https://www.bardeen.ai/docs/getting-started)
- [AI Web Scraper](https://www.bardeen.ai/features/web-scraper)
- [Integrations (100+)](https://www.bardeen.ai/integrations)
- [Playbook Library](https://www.bardeen.ai/playbooks)
- [Bardeen API](https://www.bardeen.ai/docs/api)
- [Pricing](https://www.bardeen.ai/pricing)

---

## Summary

Bardeen is a browser-based AI automation tool — a Chrome extension that combines **web scraping, data enrichment, and workflow automation** without code. Its key differentiator is that it can see and interact with any website in your browser, making it powerful for scraping data from sites without official APIs (LinkedIn, Crunchbase, Twitter/X, job boards). In 2025, Bardeen expanded with **AI agents** that can autonomously browse the web, extract structured data, and pipe it into your CRM or spreadsheets. Popular use cases: scraping LinkedIn prospects into HubSpot, extracting competitor pricing, enriching leads with company data, and automating repetitive browser workflows. Particularly valuable for Sales and Marketing teams doing research and outreach.

**Best for:** Sales and Marketing teams automating browser-based research tasks; teams needing to extract data from websites without APIs; lead enrichment and competitor monitoring.

---

## Related Materials

- [Bardeen blog](https://www.bardeen.ai/blog)
- [Bardeen use cases: sales automation](https://www.bardeen.ai/use-cases/sales)
- [10 Best AI Data Analytics Tools 2026 — Powerdrill](https://powerdrill.ai/blog/best-ai-data-analytics-tools)
- [35+ Best AI Tools for Marketing 2026 — Saasnik](https://saasnik.com/35-best-ai-tools-for-marketing-in-2026/)
- [Bardeen playbooks library](https://www.bardeen.ai/playbooks) — 100+ pre-built automation templates
- [Bardeen vs Zapier comparison](https://www.bardeen.ai/alternatives/zapier)

---

## AI Agents That Can Use This Tool

| Agent / Framework | How it integrates |
|---|---|
| **Bardeen AI Agent** | Native browser agent — autonomously navigates websites, extracts data, and triggers actions |
| **HubSpot** | Native integration — auto-enrich and create contacts from LinkedIn or web research |
| **Salesforce** | Direct integration — push scraped or enriched data to Salesforce records |
| **Notion** | Send extracted data directly to Notion databases |
| **Airtable** | Native connector for piping scraped data into Airtable bases |
| **Google Sheets** | Most common output — extract web data directly into spreadsheets |
| **Slack** | Notify team channels when Bardeen workflows find relevant data |

---

## When To Use

- Use this skill when triggering Bardeen browser-automation playbooks from code or piping their output into other systems.
- `POST /v1/playbooks/{playbook_id}/run` with a JSON body matching the playbook's declared inputs. The playbook ID is in the playbook's URL.
- Runs are async by default. Either poll `GET /v1/runs/{run_id}` or register a webhook in the playbook config for completion callbacks. Prefer the webhook for any long-running scrape.

## Practical Tips

- Bardeen runs as a Chrome extension; the "agent" lives in the user's browser. Code can only *trigger* and *receive results* — it cannot run playbooks headlessly.
- Generate an API token in the Bardeen web app under Settings → API. Pass as `Authorization: Bearer <token>`.
- All API calls go to `https://api.bardeen.ai/`.

## Watch Outs

- Calling Bardeen for tasks an official API can do (HubSpot, Salesforce, Notion all have direct APIs — use them instead).
- Storing the API token client-side in a browser app; treat it as a server secret.
- Running scrapes against authenticated sites the user is not legally permitted to scrape — check ToS first.

---

*Last updated: April 2026*
