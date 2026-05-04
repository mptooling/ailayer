# Akkio skill

Use this skill when integrating Akkio's predictive ML models from code (lead scoring, churn, forecasting).

## Setup

- Install the official SDK: `pip install akkio` (Python) or `npm install akkio` (Node).
- Auth via `AKKIO_API_KEY` env var. Generate keys in Akkio's web UI under Settings → API.
- The web UI is the only place to *train* a model. Code is the path to *consume* an already-trained one.

## Calling a deployed model

- Reference a model by its `model_id` (visible in the model's URL after training).
- For row-level prediction: `client.predict(model_id, [{"col1": v, ...}])` — the input dict keys must match the training columns exactly.
- For batch prediction, send arrays of rows in one call rather than looping; latency and cost scale per call, not per row.
- Responses include the predicted value, confidence/probability, and per-feature contribution (`shap_values`). Surface confidence to the caller; never present a low-confidence prediction as fact.

## Data flow

- Push CRM data into Akkio's connectors (HubSpot/Salesforce/Sheets/SQL) for retraining; do not POST raw rows from the agent unless you must.
- For real-time scoring on new records, call `predict` directly. For bulk back-fills, prefer the connector path so model retraining stays in sync.

## Avoid

- Re-training on every prediction call — Akkio bills training compute separately.
- Submitting columns the model wasn't trained on; the API silently drops unknown keys and accuracy degrades.
- Hard-coding a model_id in long-lived code without a fallback if the model is archived. Read it from config.
