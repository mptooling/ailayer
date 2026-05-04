# Notion AI skill

Use this skill when reading from or writing to a Notion workspace via the official API, including ingesting Notion content for RAG.

## Setup

- Create an internal integration at `notion.so/my-integrations`; copy the secret. Send as `Authorization: Bearer <secret>` and `Notion-Version: 2022-06-28` (or current).
- The integration must be explicitly *shared* with each page or database it should access — do this in the Notion UI's "Connections" menu.
- SDKs: `pip install notion-client` or `npm install @notionhq/client`. Prefer the SDK over raw HTTP for retry handling.

## Reading content

- Fetch a page: `client.pages.retrieve(page_id=...)`. Page IDs are 32-char hex strings; pull them from URLs after the last hyphen and add hyphens at the standard offsets (the SDK accepts both forms).
- For full content, you must walk blocks: `client.blocks.children.list(block_id=...)` paginates. Recurse into block types that have children (toggles, columns, callouts).
- For databases, use `client.databases.query(database_id=..., filter=..., sorts=...)`. Filters use Notion's nested-property schema — read the `properties` of one row first to learn the schema.

## Writing content

- Create pages with explicit parent: `parent={"database_id": ...}` or `{"page_id": ...}`. Properties must match the database schema exactly.
- Append blocks: `client.blocks.children.append(block_id=parent, children=[...])`. Each block is `{type: "paragraph", paragraph: {rich_text: [...]}}` — the schema is verbose; use the SDK's helper builders if available.

## RAG over Notion

- For LangChain: `from langchain_community.document_loaders import NotionDBLoader`. Pass `database_id` and `notion_api_key`; it handles pagination and renders blocks to plain text.
- Re-index incrementally — Notion exposes `last_edited_time` on every page; query for pages newer than your last sync timestamp.

## Avoid

- Hard-coding page IDs across environments; store them in a config map.
- Re-indexing the entire workspace on every cron tick — it's slow and you'll hit the 3 req/s rate limit.
- Embedding the integration secret in client-side code; the API forbids browser-origin requests anyway.
