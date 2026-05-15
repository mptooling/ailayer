# LangGraph

> **Category:** AI Agents & Automation | **Pricing:** Free (open source) + LangSmith (paid) | **Type:** Open Source (MIT)

---

## Repository

- [GitHub — langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) ⭐ 24,800+

---

## Documentation

- [Official Docs](https://langchain-ai.github.io/langgraph/)
- [Conceptual Guide](https://langchain-ai.github.io/langgraph/concepts/)
- [Tutorials](https://langchain-ai.github.io/langgraph/tutorials/)
- [How-to Guides](https://langchain-ai.github.io/langgraph/how-tos/)
- [LangGraph Platform (cloud)](https://langchain-ai.github.io/langgraph/cloud/)
- [API Reference](https://langchain-ai.github.io/langgraph/reference/)

---

## Summary

LangGraph is LangChain's framework for building stateful, multi-actor AI applications. It models agent workflows as directed graphs — nodes are agents or functions, edges are transitions. This graph-based architecture unlocks features critical for production: persistence (agents remember state across sessions), human-in-the-loop (pause and resume at any node), parallel execution, subgraphs, and time-travel (replay from any past checkpoint). In early 2026, LangGraph surpassed CrewAI in GitHub star velocity driven by enterprise adoption. It's now the standard choice for complex, production-grade multi-agent systems requiring audit trails and rollback capabilities. Pairs with LangSmith for observability.

**Best for:** Engineering teams building production multi-agent systems that need reliability, state management, human oversight, and full auditability.

---

## Related Materials

- [LangGraph announcement blog](https://blog.langchain.dev/langgraph/)
- [LangGraph vs CrewAI vs AutoGen 2026](https://o-mega.ai/articles/langgraph-vs-crewai-vs-autogen-top-10-agent-frameworks-2026)
- [Top Agentic AI Frameworks 2026 — AlphaMatch](https://www.alphamatch.ai/blog/top-agentic-ai-frameworks-2026)
- [LangGraph human-in-the-loop tutorial](https://langchain-ai.github.io/langgraph/tutorials/introduction/)
- [LangGraph Platform (deployment)](https://langchain-ai.github.io/langgraph/cloud/)
- [Best Open Source Agent Frameworks 2026 — Firecrawl](https://www.firecrawl.dev/blog/best-open-source-agent-frameworks)

---

## AI Agents That Can Use This Tool

| Agent / Framework | How it integrates |
|---|---|
| **Claude** | First-class support via `langchain-anthropic`; recommended model for complex reasoning nodes |
| **GPT-4 / OpenAI** | Default LLM; supports OpenAI tool calling natively |
| **LangChain** | LangGraph is built on top of LangChain; all LangChain tools and chains work as LangGraph nodes |
| **LangSmith** | Native observability — every LangGraph run is traced automatically |
| **CrewAI** | Can be used together — LangGraph handles state, CrewAI handles role-based agent definitions |

---

## When To Use

- Use this skill when building stateful, multi-actor agent applications where you need persistence, human-in-the-loop, or branching control flow.
- Model state as a `TypedDict`. Use `Annotated[list, add_messages]` for conversation history; LangGraph merges automatically.
- Build with `StateGraph(MyState)`. Add nodes with `.add_node("name", fn)` where each `fn(state) -> dict` returns the *delta* to merge into state.

## Practical Tips

- Install: `pip install langgraph langgraph-checkpoint-sqlite langchain-anthropic` (swap the model package as needed).
- Read API keys from env (`ANTHROPIC_API_KEY`, `OPENAI_API_KEY`). For tracing: `LANGCHAIN_TRACING_V2=true`, `LANGCHAIN_API_KEY=...`.

## Watch Outs

- Mutating `state` in-place inside a node — return a delta dict instead.
- Skipping the checkpointer in dev "to keep things simple" — debugging stateless graphs is much harder than debugging stateful ones.
- Mixing LangChain's deprecated `AgentExecutor` with LangGraph nodes; pick one.

---

*Last updated: April 2026*
