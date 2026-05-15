# Mastra

> **Category:** AI Agents & Automation | **Pricing:** Free OSS + cloud services | **Type:** TypeScript agent framework

Mastra is a TypeScript framework for building AI agents, workflows, RAG applications, evals, and tool integrations in JavaScript/TypeScript stacks.

## When To Use

- Use Mastra when your AI app is TypeScript-first and needs agents plus workflows.
- Reach for it for product engineering teams that want AI logic close to web app code.
- Consider it when combining agents, RAG, scheduled workflows, and evals in one framework.

## Practical Tips

- Keep agents and workflows separate: agents decide, workflows coordinate.
- Type tool inputs and outputs so frontend/backend contracts stay clear.
- Add evals while the workflow is still small.
- Use framework primitives before inventing custom orchestration.

## Watch Outs

- TypeScript ergonomics do not make agent behavior deterministic.
- Avoid binding product-critical side effects directly to model output without checks.
- Watch dependency churn in fast-moving AI frameworks.

## Links

- [Mastra docs](https://mastra.ai/docs)
- [Mastra GitHub](https://github.com/mastra-ai/mastra)
