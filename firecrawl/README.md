# Firecrawl

> **Category:** MCP & Tooling (web data for agents) | **Pricing:** Free (open source, self-host) / paid cloud API | **Type:** Open Source (AGPL-3.0)

---

## Repository

- [GitHub — firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) ⭐ 125,000+
- Homepage: [firecrawl.dev](https://firecrawl.dev)
- Language: TypeScript

---

## Documentation

- [API & SDKs](https://docs.firecrawl.dev/introduction)
- [Self-hosting guide](https://docs.firecrawl.dev/contributing/self-host)
- [Official MCP server](https://github.com/firecrawl/firecrawl-mcp-server)
- [Crawl / scrape / extract endpoints](https://docs.firecrawl.dev/features/scrape)

---

## Summary

Firecrawl turns websites into clean, LLM-ready data through a single API. It scrapes individual pages, crawls entire sites, searches the web, and extracts structured data — returning Markdown or JSON optimized for model context windows instead of raw HTML noise. It handles the hard parts of web ingestion (JavaScript rendering, pagination, anti-bot friction, proxies) so an agent or RAG pipeline gets usable text without a custom scraper per site. Official SDKs (Python, Node) and an MCP server let agents in Cursor, Claude, and other clients pull fresh web content as a tool. It can be self-hosted (AGPL-3.0) or used via the managed cloud, and is the most-starred project in the AI web-data space.

**Best for:** Feeding agents and RAG pipelines with clean, current web content — research, knowledge-base ingestion, and "scrape this site into Markdown" tasks — without building and maintaining scrapers.

---

## Related Materials

- [Browser Use](../browser-use/README.md) — interactive, stateful browser tasks; Firecrawl is for clean bulk scraping/crawling
- [Model Context Protocol](../mcp/README.md) — Firecrawl ships an official MCP server to expose web data as an agent tool
- [LlamaIndex](../llamaindex/README.md) / [LangChain](../langchain/README.md) — common consumers of Firecrawl output in RAG pipelines
- [Qdrant](../qdrant/README.md) — store the embedded Markdown Firecrawl produces

---

## When To Use

- An agent or RAG pipeline needs fresh, clean text from the web and you don't want to maintain per-site scrapers.
- You need to crawl a whole site or docs portal into Markdown for indexing or grounding.
- You want web access exposed to a coding agent as an MCP tool (Cursor, Claude, etc.).

## Practical Tips

- Use `scrape` for one URL, `crawl` for a whole site, `search` for query-driven discovery, and `extract` when you need structured JSON against a schema.
- Add the official MCP server to your agent so it can fetch live pages mid-task instead of relying on stale training data.
- Self-host for sensitive or high-volume workloads; use the cloud API to skip proxy and rendering infrastructure.
- Cache and rate-limit crawls — large sites can return a lot of pages and cost (cloud) or load (self-host).

## Watch Outs

- AGPL-3.0: self-hosting and modifying it inside a network service can trigger source-disclosure obligations — review the license for commercial use, or use the cloud API to sidestep it.
- Respect target sites' robots.txt, ToS, and rate limits; bulk crawling can get you blocked or raise legal/ethical issues.
- Output is cleaned and converted — verify fidelity for cases where exact formatting or every element matters.
- Self-hosting needs the rendering/proxy stack to handle JS-heavy and anti-bot sites; the bare deploy won't match cloud success rates out of the box.

---

*Last updated: 2026-05*
