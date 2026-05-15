# Obviously AI

> **Category:** AI Data & Analytics | **Pricing:** $75/mo (Starter) / $150/mo (Professional) / Enterprise | **Type:** Closed-source SaaS

---

## Repository

Obviously AI is closed source. No public GitHub repo.

- [Obviously AI API Docs](https://docs.obviously.ai/)

---

## Documentation

- [Official Site](https://www.obviously.ai/)
- [API Documentation](https://docs.obviously.ai/)
- [Getting Started Guide](https://help.obviously.ai/en/)
- [Use Cases](https://www.obviously.ai/use-cases)
- [Integrations](https://www.obviously.ai/integrations)
- [Pricing](https://www.obviously.ai/pricing)

---

## Summary

Obviously AI is a no-code predictive analytics platform that enables non-technical users to build and deploy machine learning models in under 2 minutes. The workflow is: upload a CSV or connect a data source → select the column to predict → click "Run AI" → get a trained model with explanations. Predictions include feature importance charts (which factors drive the outcome most) and natural language explanations of model decisions. Compared to Akkio, Obviously AI places a stronger emphasis on **explainability** and **simplicity** — every prediction comes with a plain-English "why." Popular with sales teams for churn prediction and with operations teams for demand forecasting.

**Best for:** Non-technical business users who need quick, explainable predictions; small-to-mid teams without dedicated data science resources.

---

## Related Materials

- [Obviously AI blog](https://www.obviously.ai/post)
- [Obviously AI vs Akkio comparison](https://julius.ai/articles/julius-ai-alternatives)
- [10 Best AI Data Analytics Tools 2026 — Powerdrill](https://powerdrill.ai/blog/best-ai-data-analytics-tools)
- [Best AI Tools for Data Analysis 2026 — AllAboutAI](https://www.allaboutai.com/best-ai-tools/productivity/data-analysis/)
- [Top 12 AI Tools for Data Analytics 2026 — PixelPlex](https://pixelplex.io/blog/best-ai-for-data-analytics-tools/)
- [Obviously AI use case: churn prediction](https://www.obviously.ai/post/churn-prediction)

---

## AI Agents That Can Use This Tool

| Agent / Framework | How it integrates |
|---|---|
| **Obviously AI native** | Automated ML pipeline — model selection, training, and deployment without code |
| **REST API** | Obviously AI API allows predictions to be embedded in any application or workflow |
| **n8n** | REST API integration for triggering predictions in automated n8n workflows |
| **Zapier** | Obviously AI + Zapier — automatically score new leads or customers as they enter your system |
| **Salesforce** | Sync predictions back to Salesforce fields for sales team visibility |
| **Snowflake / BigQuery** | Native data connectors for enterprise-scale data pipelines |

---

## When To Use

- Use this skill when calling Obviously AI's REST API to consume already-trained predictive models from code.
- Endpoint: `POST /predict/{model_id}/`. Body: `{"data": [{"col_a": v, "col_b": v}, ...]}`. Send rows in arrays; the API supports batch up to ~1000 rows per call.
- Response includes `predictions[i].value`, `predictions[i].probability`, and `predictions[i].explanation` (top features that drove the result). Always pass the explanation through to end users — the platform's value is explainability.

## Practical Tips

- Get an API key in the Obviously AI app under Settings → API. Send as `Authorization: Token <key>`.
- Base URL: `https://api.obviously.ai/v1/`. All payloads JSON.
- Models are *trained in the UI*, not via API. Code consumes deployed models — it cannot kick off training.

## Watch Outs

- Showing only the predicted value without the per-feature explanation — that defeats the tool's purpose and the user can't sanity-check.
- Sending a column the model wasn't trained on; the API errors out (unlike Akkio which silently drops it).
- Building a feedback loop that retrains by exporting and re-uploading data — use the platform's scheduled retraining instead, configured in the UI.

---

*Last updated: April 2026*
