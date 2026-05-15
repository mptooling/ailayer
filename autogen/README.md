# AutoGen

> **Category:** AI Agents & Automation | **Pricing:** Free OSS | **Type:** Open-source multi-agent framework

AutoGen is Microsoft's open-source framework for building event-driven, multi-agent AI applications and research prototypes.

## When To Use

- Use AutoGen when exploring multi-agent conversations, agent teams, and complex coordination patterns.
- Reach for it for research-heavy prototypes that need flexible orchestration.
- Consider it when your organization already uses Microsoft AI tooling.

## Practical Tips

- Start with two agents and one concrete task before building a large agent society.
- Define termination conditions and maximum turns up front.
- Log every message and tool call so behavior can be debugged.
- Move stable patterns into deterministic code once the agent flow is understood.

## Watch Outs

- Multi-agent loops can become expensive and hard to reason about.
- More agents do not automatically mean better output.
- Keep human review in the loop for code, security, and business-critical decisions.

## Links

- [AutoGen docs](https://microsoft.github.io/autogen/)
- [AutoGen GitHub](https://github.com/microsoft/autogen)
