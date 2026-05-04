# Perplexity skill

Use this skill when calling the Perplexity API for cited, web-grounded answers from code.

## Setup

- Get an API key from `perplexity.ai/settings/api`. Send as `Authorization: Bearer <key>`.
- Base URL: `https://api.perplexity.ai/`. The API mirrors OpenAI's chat-completions shape — most OpenAI client libs work with `base_url` overridden.

## Picking a model

- For live web search: use a `sonar` model (`sonar`, `sonar-pro`, `sonar-reasoning`). These do retrieval automatically — do not bolt on a separate search step.
- For pure reasoning without retrieval, use `sonar-reasoning-pro`. Skip Perplexity entirely if you don't need citations — Claude/GPT-4 are cheaper.

## Calling the API

- `POST /chat/completions` with `{"model": "sonar-pro", "messages": [...]}`. Same role conventions as OpenAI (`system`, `user`, `assistant`).
- The response includes `citations: [...]` — a list of source URLs. Always render these to the user; presenting Perplexity output as un-cited claims throws away the differentiator.
- Use `search_domain_filter: ["domain.com", "-blocked.com"]` to whitelist or exclude sources. Use `search_recency_filter: "month"` for time-bound research.

## Patterns

- For competitive intel or market research, structure the prompt as: "Research X. Output: a markdown report with sections {A, B, C}, each citing at least 2 sources." Specifying the output shape dramatically improves consistency.
- For Q&A inside an agent, treat Perplexity as a single search-tool — the agent calls it once per question, not once per sub-step.
- Cache responses keyed by prompt + filter parameters; results are reasonably stable for 24h on slow-moving topics.

## Avoid

- Streaming with `sonar-reasoning` for short queries — first-token latency is high; just await the full response.
- Trusting a single citation; for high-stakes claims have the agent cross-check with a second query.
- Sending follow-up turns that depend on prior `citations` — Perplexity does not retain them across turns; restate the relevant context in the new prompt.
