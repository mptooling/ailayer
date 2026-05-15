# Notion AI

> **Category:** AI Writing & Marketing | **Pricing:** $10/mo add-on (on top of Notion plan) / Enterprise | **Type:** Closed-source SaaS

---

## Repository

Notion AI is a closed-source product. API resources:

- [Notion API (official)](https://github.com/makenotion/notion-sdk-js) ⭐ 4,500+ (official JS SDK)
- [Notion API Python SDK](https://github.com/ramnes/notion-sdk-py) ⭐ 1,800+

---

## Documentation

- [Notion AI Overview](https://www.notion.com/product/ai)
- [Notion API Docs](https://developers.notion.com/)
- [Notion AI Help Center](https://www.notion.com/help/guides/notion-ai-for-beginners)
- [Notion for Teams](https://www.notion.com/teams)
- [Enterprise & Security](https://www.notion.com/enterprise)
- [Pricing](https://www.notion.com/pricing)

---

## Summary

Notion AI is the AI layer built directly into Notion — the workspace platform used by 35M+ teams worldwide. It enables users to draft documents, summarise meeting notes, translate content, generate action items from transcripts, and search across the entire Notion workspace using natural language ("Q2 on-call decisions"). In 2025, Notion AI expanded into **AI connectors** — pulling in live data from Slack, Google Drive, and GitHub into Notion AI answers. Unlike standalone writing tools, Notion AI's value is contextual: it knows your team's existing docs, projects, and processes. Key for Marketing and C-Level who already live in Notion and want AI without context-switching.

**Best for:** Teams already on Notion wanting AI embedded in their workflow; internal comms, meeting summaries, knowledge management, and cross-team documentation.

---

## Related Materials

- [Notion AI changelog](https://www.notion.com/releases/ai)
- [Notion AI connectors announcement](https://www.notion.com/blog/ai-connectors)
- [Best AI Writing Tools 2026 — ToolChase](https://toolchase.com/blog/best-ai-writing-tools-2026/)
- [Notion API documentation](https://developers.notion.com/)
- [Notion AI for marketing teams — guide](https://www.notion.com/use-case/marketing)
- [35+ Best AI Tools for Marketing 2026 — Saasnik](https://saasnik.com/35-best-ai-tools-for-marketing-in-2026/)

---

## AI Agents That Can Use This Tool

| Agent / Framework | How it integrates |
|---|---|
| **Notion AI (native)** | Built-in AI agents for document drafting, summarisation, translation, and Q&A |
| **n8n** | Notion node in n8n — read/write pages and databases; combine with AI nodes |
| **LangChain** | `langchain-community` Notion loader — index Notion pages for RAG pipelines |
| **Zapier** | Notion + Zapier integration for triggering AI-enriched workflows from Notion events |
| **Claude / GPT-4** | Via Notion API — Claude or GPT-4 can read and write Notion pages as part of agent workflows |

---

## When To Use

- Use this skill when reading from or writing to a Notion workspace via the official API, including ingesting Notion content for RAG.
- Fetch a page: `client.pages.retrieve(page_id=...)`. Page IDs are 32-char hex strings; pull them from URLs after the last hyphen and add hyphens at the standard offsets (the SDK accepts both forms).
- For full content, you must walk blocks: `client.blocks.children.list(block_id=...)` paginates. Recurse into block types that have children (toggles, columns, callouts).

## Practical Tips

- Create an internal integration at `notion.so/my-integrations`; copy the secret. Send as `Authorization: Bearer <secret>` and `Notion-Version: 2022-06-28` (or current).
- The integration must be explicitly *shared* with each page or database it should access — do this in the Notion UI's "Connections" menu.
- SDKs: `pip install notion-client` or `npm install @notionhq/client`. Prefer the SDK over raw HTTP for retry handling.

## Watch Outs

- Hard-coding page IDs across environments; store them in a config map.
- Re-indexing the entire workspace on every cron tick — it's slow and you'll hit the 3 req/s rate limit.
- Embedding the integration secret in client-side code; the API forbids browser-origin requests anyway.

---

*Last updated: April 2026*
