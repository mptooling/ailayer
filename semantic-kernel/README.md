# Semantic Kernel

> **Category:** AI Agents & Automation | **Pricing:** Free OSS | **Type:** Open-source AI orchestration SDK

Semantic Kernel is Microsoft's SDK for integrating LLMs, tools, planners, memory, and agent patterns into .NET, Python, and Java applications.

## When To Use

- Use Semantic Kernel when you are building AI features inside enterprise .NET or Microsoft-heavy stacks.
- Reach for it when plugin-style tool orchestration and typed application integration matter.
- Consider it when Azure OpenAI and Microsoft ecosystem support are important.

## Practical Tips

- Treat plugins as normal application boundaries with clear inputs, outputs, and permissions.
- Keep prompts versioned and testable.
- Use planners carefully; deterministic workflows are easier to test when the path is known.
- Integrate with existing logging and telemetry instead of treating the agent as a black box.

## Watch Outs

- Enterprise integration does not remove the need for evals.
- Avoid giving planners unrestricted access to broad plugin sets.
- Keep prompt templates free of secrets and tenant-specific data.

## Links

- [Semantic Kernel docs](https://learn.microsoft.com/en-us/semantic-kernel/)
- [Semantic Kernel GitHub](https://github.com/microsoft/semantic-kernel)
