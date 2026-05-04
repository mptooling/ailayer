# Bardeen skill

Use this skill when triggering Bardeen browser-automation playbooks from code or piping their output into other systems.

## Setup

- Bardeen runs as a Chrome extension; the "agent" lives in the user's browser. Code can only *trigger* and *receive results* — it cannot run playbooks headlessly.
- Generate an API token in the Bardeen web app under Settings → API. Pass as `Authorization: Bearer <token>`.
- All API calls go to `https://api.bardeen.ai/`.

## Triggering a playbook

- `POST /v1/playbooks/{playbook_id}/run` with a JSON body matching the playbook's declared inputs. The playbook ID is in the playbook's URL.
- Runs are async by default. Either poll `GET /v1/runs/{run_id}` or register a webhook in the playbook config for completion callbacks. Prefer the webhook for any long-running scrape.
- Outputs are returned as structured JSON when the playbook ends with a "Save data" step. If it ends with "Send to Sheets/HubSpot", the data lands there directly — your code shouldn't expect it in the API response.

## Playbook design rules (when authoring through code-gen prompts)

- Always pin selectors with the recorder, not free-form CSS — Bardeen's recorder generates resilient selectors that survive minor DOM changes.
- Add explicit "wait for element" steps before any extraction; pages with skeleton loaders return empty data otherwise.
- For LinkedIn/Twitter scraping, throttle: insert a "Wait 5–10s random" step between rows. Aggressive scraping will get the user's account flagged.

## Avoid

- Calling Bardeen for tasks an official API can do (HubSpot, Salesforce, Notion all have direct APIs — use them instead).
- Storing the API token client-side in a browser app; treat it as a server secret.
- Running scrapes against authenticated sites the user is not legally permitted to scrape — check ToS first.
