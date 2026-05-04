# Copy.ai skill

Use this skill when calling the Copy.ai API to generate content or trigger Workflows from code.

## Setup

- Get an API key from the Copy.ai workspace under Settings → API. Send as `x-copy-ai-api-key: <key>` header.
- Base URL: `https://api.copy.ai/api/`. All payloads are JSON.

## Generating content

- Endpoint: `POST /workflow/{workflow_id}/run`. Workflow IDs come from the URL of any workflow built in the web UI.
- Body shape: `{ "startVariables": { "<input_name>": "<value>" } }`. Input names are defined per workflow — fetch them with `GET /workflow/{id}` if you don't know them.
- Runs are async. Poll `GET /workflow/{id}/run/{run_id}` for `status: "COMPLETE"` and read `output` from the response.
- For one-off completions without a workflow, use the legacy `/copy/{tool_id}` endpoint — but new code should always go through Workflows for consistency.

## GTM / Sales patterns

- Pre-build a workflow per outreach pattern (cold email, follow-up, LinkedIn DM) in the UI. From code, only pass the variable inputs (prospect name, company, hook).
- Chain Copy.ai → CRM update via webhooks: configure the workflow to POST results to your CRM endpoint instead of round-tripping through your service.
- For high-volume use, batch by spawning runs in parallel rather than passing arrays — there is no native batch endpoint.

## Avoid

- Embedding Copy.ai keys in client-side code — calls must go through your server.
- Hard-coding workflow IDs across multiple environments; use a config map keyed by env (dev/staging/prod each have their own workspace).
- Polling more than once per second; the API will rate-limit and you'll get HTTP 429.
- Sending raw PII without checking the workspace's data-retention policy first.
