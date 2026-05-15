# Pydantic AI

> **Category:** AI Agents & Automation | **Pricing:** Free OSS | **Type:** Open-source Python agent framework

Pydantic AI is a Python agent framework from the Pydantic team focused on typed inputs, structured outputs, dependency injection, and testable agent code.

## When To Use

- Use Pydantic AI when Python type safety and structured model outputs are central to the app.
- Reach for it when you want agent behavior to feel like normal typed application code.
- Consider it for production services that need validation, dependency injection, and unit-testable tools.

## Practical Tips

- Model tool inputs and outputs with Pydantic schemas.
- Keep dependencies explicit so agents can be tested with fake services.
- Validate model responses at boundaries instead of trusting JSON-like text.
- Use typed result objects for workflows that feed downstream systems.

## Watch Outs

- Type validation catches shape errors, not bad reasoning.
- Avoid over-modeling early prototypes; start with the minimum schema that protects downstream code.
- Still add evals for task quality and hallucination behavior.

## Links

- [Pydantic AI docs](https://ai.pydantic.dev/)
- [Pydantic AI GitHub](https://github.com/pydantic/pydantic-ai)
