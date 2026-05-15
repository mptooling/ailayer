# LiteLLM

> **Category:** Runtime & Retrieval Infrastructure | **Pricing:** Free OSS + enterprise offerings | **Type:** LLM gateway and provider abstraction

LiteLLM is an OpenAI-compatible gateway and SDK for routing requests across many model providers with unified auth, logging, budgets, and fallbacks.

## When To Use

- Use LiteLLM when your app needs model-provider abstraction or centralized model access.
- Reach for it when teams need budgets, routing, retries, and consistent API shape.
- Consider it for multi-provider evaluation, failover, and cost control.

## Practical Tips

- Route by use case: cheap models for extraction, stronger models for reasoning.
- Track cost, latency, and error rate per model and feature.
- Use fallbacks deliberately; silent model swaps can change product behavior.
- Keep provider keys server-side and rotate them normally.

## Watch Outs

- Provider abstraction cannot remove model-specific output differences.
- A gateway becomes critical infrastructure; monitor it like any production dependency.
- Avoid broad proxy access without tenant and user-level controls.

## Links

- [LiteLLM docs](https://docs.litellm.ai/)
- [LiteLLM GitHub](https://github.com/BerriAI/litellm)
