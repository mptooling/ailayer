# CrewAI

> **Category:** AI Agents & Automation | **Pricing:** Free (open source) + CrewAI Enterprise | **Type:** Open Source (MIT)

---

## Repository

- [GitHub — crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) ⭐ 44,300+

---

## Documentation

- [Official Docs](https://docs.crewai.com/)
- [Getting Started](https://docs.crewai.com/installation)
- [Agents](https://docs.crewai.com/concepts/agents)
- [Tasks](https://docs.crewai.com/concepts/tasks)
- [Tools](https://docs.crewai.com/concepts/tools)
- [Crews & Flows](https://docs.crewai.com/concepts/crews)
- [CrewAI Enterprise](https://www.crewai.com/enterprise)

---

## Summary

CrewAI is a framework for orchestrating multiple AI agents as a "crew" — each agent has a defined role, goal, and backstory, and they collaborate to complete complex tasks. It abstracts away the complexity of multi-agent coordination with a simple, role-based API. You define a `Crew` with `Agents` and `Tasks`, and CrewAI handles communication, task delegation, and output chaining. Unlike LangGraph's graph-based control flow, CrewAI is intentionally higher-level and easier to prototype with. Popular for marketing automation, research pipelines, and customer support workflows. By 2026, CrewAI has 44,000+ GitHub stars and a growing enterprise offering with GUI management and pre-built crew templates.

**Best for:** Teams wanting to prototype role-based AI workflows quickly; marketing and sales automation use cases; business users new to AI agents.

---

## Related Materials

- [CrewAI blog](https://www.crewai.com/blog)
- [Top Agentic AI Frameworks 2026 — AlphaMatch](https://www.alphamatch.ai/blog/top-agentic-ai-frameworks-2026)
- [LangGraph vs CrewAI vs AutoGen 2026](https://o-mega.ai/articles/langgraph-vs-crewai-vs-autogen-top-10-agent-frameworks-2026)
- [CrewAI for marketing automation — guide](https://blog.crewai.com/)
- [awesome-ai-agents-2026](https://github.com/caramaschiHG/awesome-ai-agents-2026)
- [AI Agent Frameworks Compared 2026](https://remoteopenclaw.com/blog/ai-agent-frameworks-compared-2026)

---

## AI Agents That Can Use This Tool

| Agent / Framework | How it integrates |
|---|---|
| **Claude** | Supported LLM backend via `langchain-anthropic`; CrewAI agents can use Claude as their LLM |
| **GPT-4 / OpenAI** | Default LLM; deepest integration for reasoning and function calling |
| **LangChain Tools** | CrewAI agents natively use LangChain tools (web search, code exec, etc.) |
| **n8n** | n8n can trigger CrewAI crew runs via HTTP API |
| **LangGraph** | CrewAI and LangGraph can be combined — CrewAI for role abstraction, LangGraph for state management |

---

*Last updated: April 2026*
