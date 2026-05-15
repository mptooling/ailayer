# OpenAI Agents SDK

> **Category:** AI Agents & Automation | **Pricing:** Free SDK; OpenAI API usage billed separately | **Type:** Official SDK

OpenAI Agents SDK is OpenAI's framework for building tool-using agents with handoffs, guardrails, tracing, and production-oriented orchestration.

## When To Use

- Use OpenAI Agents SDK when your agent stack is primarily OpenAI-native.
- Reach for it when you need tool calls, multi-agent handoffs, tracing, and guardrails in one SDK.
- Consider it for production assistants that must coordinate multiple specialist agents.

## Practical Tips

- Design agents around clear responsibilities and explicit handoff criteria.
- Keep tools small, deterministic, and permission-aware.
- Use tracing to debug tool calls and handoffs before adding complexity.
- Add guardrails around user input, tool outputs, and external side effects.

## Watch Outs

- Multi-agent systems can hide simple control-flow bugs behind impressive traces.
- Guardrails reduce risk but do not replace authorization checks in tools.
- Avoid tool functions that can mutate broad external state without confirmation.

## Links

- [OpenAI Agents SDK docs](https://openai.github.io/openai-agents-python/)
- [OpenAI Agents SDK GitHub](https://github.com/openai/openai-agents-python)
