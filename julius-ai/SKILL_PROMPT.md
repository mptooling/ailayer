# Julius AI skill

Use this skill when invoking Julius programmatically for natural-language data analysis, charts, and scheduled reports.

## Setup

- Julius has no official public API. Two paths: (a) the unofficial `julius-ai-api` Python wrapper, (b) Julius for Teams' Slack / scheduled-report integrations triggered from your stack.
- For (a): `pip install julius-ai-api`, authenticate by capturing the session cookie from a logged-in browser session and passing it via `Julius(cookie=...)`. This is unofficial — expect breakage on Julius UI updates.

## Data prep

- Julius accepts CSV, Excel, JSON, Parquet, plus live connectors (Postgres, MySQL, BigQuery, Snowflake, Google Sheets). For analysis from code, the cleanest path is: write the dataframe to a local CSV, upload via the wrapper, then ask questions.
- Column names with spaces or punctuation are kept verbatim — wrap them in backticks in your prompts: `` "Plot `Sale Date` vs `Net Revenue`" ``.

## Asking questions

- Be specific about the output format: "Return a bar chart" or "Return a markdown table" beats open-ended "show me trends." Julius is more reliable when it knows what artefact to produce.
- For repeatable analysis, pin to a specific method: "Run a chi-square test on columns X and Y" rather than "is there a relationship between X and Y?"
- The wrapper returns a `Response` with `text`, `code` (the Python/R Julius generated), and `image_urls`. Cache `code` if you want reproducibility — re-running the prompt will produce different code each time.

## Scheduled reports

- Configure scheduled reports in the UI (Julius for Teams plan). Trigger them via Slack or have them post results to a webhook your stack consumes.

## Avoid

- Sending PII or sensitive data without checking your workspace's data-residency settings — Julius is SaaS, data leaves your infrastructure.
- Treating Julius output as audited analysis; the underlying code is not reviewed. For regulated decisions, surface and review the generated code.
- Building production pipelines on the unofficial wrapper without a fallback — assume it may break on any Julius release.
