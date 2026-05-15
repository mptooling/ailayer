# Braintrust

> **Category:** Evals & Observability | **Pricing:** Free tier + paid SaaS | **Type:** Evaluation and observability platform

Braintrust is an AI evaluation and observability platform for testing prompts, datasets, agents, tools, and production traces.

## When To Use

- Use Braintrust when evals need to be part of CI/CD and release decisions.
- Reach for it when debugging agent traces, comparing models, and monitoring regressions.
- Consider it for teams that want hosted experiment tracking plus production observability.

## Practical Tips

- Build small, high-signal datasets from real user failures.
- Score outputs with a mix of deterministic checks, model judges, and human review.
- Gate risky prompt/model changes with eval thresholds.
- Keep production traces tied back to prompts, models, tool calls, and deploy versions.

## Watch Outs

- LLM-as-judge scores are useful signals, not objective truth.
- Weak datasets make polished dashboards misleading.
- Do not log secrets or sensitive user data without redaction.

## Links

- [Braintrust docs](https://www.braintrust.dev/docs)
- [Braintrust GitHub](https://github.com/braintrustdata/braintrust)
