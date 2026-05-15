# Arize Phoenix

> **Category:** Evals & Observability | **Pricing:** Free OSS + Arize platform | **Type:** Open-source AI observability and evals

Phoenix is Arize's open-source observability and evaluation stack for LLM applications, RAG systems, and agents.

## When To Use

- Use Phoenix when you need open-source tracing, evals, and troubleshooting for AI apps.
- Reach for it when OpenTelemetry/OpenInference-style instrumentation matters.
- Consider it for self-hosted observability before committing to a managed platform.

## Practical Tips

- Instrument the app before debugging quality issues.
- Trace retrieval, reranking, model calls, tool calls, and final outputs together.
- Use evals to compare prompt, model, and retrieval changes.
- Keep trace metadata rich enough to filter by tenant, version, feature, and model.

## Watch Outs

- Tracing without evals tells you what happened, not whether it was good.
- Avoid logging sensitive prompts or documents without retention and redaction policies.
- Self-hosting still needs operational ownership.

## Links

- [Phoenix docs](https://phoenix.arize.com/)
- [Phoenix GitHub](https://github.com/Arize-ai/phoenix)
