# Jasper skill

Use this skill when calling the Jasper API to generate brand-aligned marketing content from code.

## Setup

- Get an API key from Jasper under Account → API. Send as `Authorization: Bearer <key>`. Base URL `https://api.jasper.ai/v1/`.
- Brand Voice and Knowledge Base are *workspace*-level concepts. Configure them in the UI; the API merely references them by ID.

## Generating content

- Endpoint: `POST /commands/run` with `{ "command": "<command_name>", "inputs": {...}, "brand_voice_id": "...", "knowledge_base_ids": [...] }`.
- Common commands: `blog-post-outline`, `email-subject-lines`, `product-description`, `social-media-post`. Full list under `GET /commands`.
- Always pass `brand_voice_id` for any external-facing content; without it, output drifts toward generic LLM tone.
- Long-form runs (`blog-post`, `campaign`) are async — poll `GET /commands/run/{id}` for `status: completed`, then read `output`.

## Campaigns

- Use `POST /campaigns` to generate every variant for a campaign in one call (subject lines, ad copy, social posts, landing-page hero). Inputs: campaign brief + audience + brand voice.
- Iterate by re-running with the previous output's `revision_id` and a delta prompt — do not concatenate outputs and re-prompt as a new run.

## Brand-Voice / KB hygiene

- Keep brand-voice docs short and example-heavy: 2–3 paragraphs of "do" prose plus 5–10 sample sentences beats a 20-page style guide.
- Refresh the Knowledge Base when product names or pricing change; stale KB contents will leak into generated copy.

## Avoid

- Storing API keys in the front end — Jasper enforces server-side use only.
- Using Jasper for code generation; it's tuned for marketing prose and will produce low-quality code.
- Re-running the same prompt to get variants — pass `n: <int>` to get multiple outputs per call.
