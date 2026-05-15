# DeepEval

> **Category:** Evals & Observability | **Pricing:** Free OSS + Confident AI platform | **Type:** Open-source LLM evaluation framework

DeepEval is an open-source testing framework for LLM systems with metrics for RAG, hallucination, toxicity, summarization, and agent behavior.

## When To Use

- Use DeepEval when you want pytest-style tests for LLM applications.
- Reach for it when building automated regression tests for prompts, RAG, and agents.
- Consider it when metric breadth matters more than hosted observability.

## Practical Tips

- Start with a few critical metrics tied to real failure modes.
- Run evals in CI for prompts or retrieval changes that affect production behavior.
- Use custom metrics when built-in scores do not reflect product quality.
- Keep golden datasets small enough to run frequently.

## Watch Outs

- More metrics can obscure the few that matter.
- LLM judges need calibration against human review.
- Avoid brittle tests that fail on harmless wording changes.

## Links

- [DeepEval docs](https://docs.confident-ai.com/)
- [DeepEval GitHub](https://github.com/confident-ai/deepeval)
