# Writesonic skill

Use this skill when calling Writesonic's API for content generation, SEO articles, or embedding Botsonic chatbots.

## Setup

- API key from `app.writesonic.com` → API. Send as `X-API-KEY: <key>`.
- Base URL: `https://api.writesonic.com/v2/business/content/`. Most generation endpoints accept `engine` (`premium` for GPT-4-class, `economy` for cheaper) and `language` ISO codes.

## Generating content

- Pick the right endpoint per format: `chatsonic` for chat-style/web-grounded answers, `seo-articles-v3` for long-form SEO content, `instant-article-writer-v4` for short blogs, `landing-pages` for landing-page copy.
- For SEO articles: pass `keywords`, `article_title`, `article_intro`, and optionally `article_sections`. Writesonic auto-fills missing pieces but quality drops; provide them when you have them.
- Most endpoints are async. Submit and poll with the returned `job_id` against `/jobs/{job_id}` until `status: SUCCESS`.

## Chatsonic (web-grounded answers)

- Set `enable_google_results: true` for live web search. Pass conversation history as `history_data: [{is_sent, message}]`.
- Image generation flips on with `enable_memory: true` and a prompt that requests an image; output URLs come back in `image` field.

## Botsonic (custom chatbots)

- Bots are trained in the UI on uploaded docs/URLs/sitemaps. Code interacts via two endpoints: `/v1/botsonic/{bot_id}/conversation` to chat, and webhooks (configured in the bot UI) for inbound events.
- Embed on a site with the snippet from the Botsonic dashboard — don't reverse-engineer the embed; the snippet handles auth and CORS.

## Avoid

- Hard-coding `engine: premium` for high-volume jobs — costs add up fast. Default to `economy` and switch up only for customer-facing content.
- Using `seo-articles-v3` without supplying real keywords — the article will be on-topic but unranked.
- Building production chatbots on Botsonic without a fallback to a human; the API has no SLA-grade guarantees.
- Polling job status faster than once every 2s — you will get rate-limited.
