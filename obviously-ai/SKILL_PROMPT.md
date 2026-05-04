# Obviously AI skill

Use this skill when calling Obviously AI's REST API to consume already-trained predictive models from code.

## Setup

- Get an API key in the Obviously AI app under Settings → API. Send as `Authorization: Token <key>`.
- Base URL: `https://api.obviously.ai/v1/`. All payloads JSON.
- Models are *trained in the UI*, not via API. Code consumes deployed models — it cannot kick off training.

## Predicting

- Endpoint: `POST /predict/{model_id}/`. Body: `{"data": [{"col_a": v, "col_b": v}, ...]}`. Send rows in arrays; the API supports batch up to ~1000 rows per call.
- Response includes `predictions[i].value`, `predictions[i].probability`, and `predictions[i].explanation` (top features that drove the result). Always pass the explanation through to end users — the platform's value is explainability.
- For categorical targets, response includes `predictions[i].class_probabilities` keyed by class label. Use these for thresholding rather than a single argmax.

## Streaming new data in

- For continuous scoring (e.g. score every new lead): wire the upstream system → webhook → your service → Obviously AI predict. Don't write directly to Obviously's data connectors from code; treat connectors as UI-managed.
- Cache predictions for stable inputs; the API rate-limits at 60 req/min on lower tiers.

## Avoid

- Showing only the predicted value without the per-feature explanation — that defeats the tool's purpose and the user can't sanity-check.
- Sending a column the model wasn't trained on; the API errors out (unlike Akkio which silently drops it).
- Building a feedback loop that retrains by exporting and re-uploading data — use the platform's scheduled retraining instead, configured in the UI.
