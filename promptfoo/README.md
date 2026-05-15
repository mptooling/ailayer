# promptfoo

> **Category:** Evals & Observability | **Pricing:** Free OSS + paid cloud | **Type:** Prompt and model evaluation CLI

promptfoo is an open-source CLI and framework for testing prompts, comparing models, red-teaming outputs, and running LLM eval suites.

## When To Use

- Use promptfoo when you need lightweight, file-based prompt and model regression tests.
- Reach for it when comparing providers, prompts, tools, and guardrail behavior.
- Consider it for security and jailbreak testing in CI.

## Practical Tips

- Store eval cases next to the feature they protect.
- Use assertions for exact business rules and model-graded checks for subjective quality.
- Compare models with identical prompts and test inputs.
- Add red-team cases for prompt injection, data leakage, and unsafe tool use.

## Watch Outs

- Eval YAML can become hard to maintain if every edge case is added without grouping.
- Model-graded tests should be reviewed periodically.
- Avoid running expensive broad suites on every tiny edit.

## Links

- [promptfoo docs](https://www.promptfoo.dev/docs/)
- [promptfoo GitHub](https://github.com/promptfoo/promptfoo)
