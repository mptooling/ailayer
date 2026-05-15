# DSPy

> **Category:** AI Agents & Automation | **Pricing:** Free OSS | **Type:** Open-source LLM programming and optimization framework

DSPy is a framework for programming LLM pipelines with declarative modules, signatures, optimizers, and evaluation-driven prompt/program compilation.

## When To Use

- Use DSPy when prompt engineering is becoming a brittle manual tuning process.
- Reach for it when you have examples, metrics, and want systematic optimization.
- Consider it for RAG and classification pipelines where measurable quality matters.

## Practical Tips

- Define signatures around task inputs and outputs before optimizing prompts.
- Build a small, representative validation set early.
- Use optimizers only after a baseline pipeline works.
- Track metrics over time; optimized prompts can regress when data or models change.

## Watch Outs

- DSPy needs examples and metrics; without them it adds abstraction without leverage.
- Optimized prompts can overfit weak validation sets.
- Keep generated prompts inspectable for safety-sensitive workflows.

## Links

- [DSPy docs](https://dspy.ai/)
- [DSPy GitHub](https://github.com/stanfordnlp/dspy)
