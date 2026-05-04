# Polymer skill

Use this skill when piping data into Polymer dashboards or sharing dashboard links from automated workflows.

## Setup

- Polymer is a UI-first product. There is no public REST API for dashboard creation. Code interacts with Polymer in two ways: by *feeding data sources* and by *embedding/sharing dashboards*.
- Sign in once and connect a data source (Sheets, Airtable, Shopify, CSV upload, or a JDBC database) under Data → Sources.

## Feeding data

- For Google Sheets: write to a sheet from your stack; Polymer pulls it on its scheduled refresh interval (configure in Polymer per source).
- For Airtable: same pattern — your code writes records via the Airtable API, Polymer reads them.
- For one-off CSV ingestion in CI: upload via the web UI; there is no headless upload endpoint.

## Embedding and sharing

- Public dashboards have a stable share URL. Pass the URL through email/Slack/your app — viewers don't need a Polymer account.
- For private embeds (Pro tier), generate a signed iframe URL via the embed settings and serve it with a short TTL token from your backend. Never expose the workspace's master share key client-side.
- PolyAI (the in-product chat) only runs in the dashboard UI. There is no API to pose ad-hoc data questions from code.

## Patterns

- Treat Polymer as the *presentation layer*, not the data layer. Your stack should own the canonical data; Polymer is a view on it.
- For executive-shareable dashboards, set up scheduled email digests inside Polymer — don't poll the dashboard from code.

## Avoid

- Building automation that "creates a dashboard from a CSV programmatically" — there is no such endpoint. Use a templating workflow in the UI and let code only refresh the underlying data.
- Sharing dashboards that aggregate sensitive customer data via the public-link option; switch to private embed instead.
