# LangChain skill

Use this skill when building LLM apps, RAG pipelines, or agent chains in Python or TypeScript.

## Setup

- Install only the packages you need: `pip install langchain-core langchain-anthropic` (or `langchain-openai`). Avoid the umbrella `langchain` package unless you need legacy chains.
- For multi-step or stateful agents, prefer LangGraph: `pip install langgraph`.
- Read `LANGCHAIN_API_KEY`, `ANTHROPIC_API_KEY`, or `OPENAI_API_KEY` from env. Never hard-code keys.

## Building blocks

- Compose chains with the LCEL pipe operator: `prompt | model | parser`. Do not nest `LLMChain` / `SequentialChain` from `langchain.chains` in new code — they are legacy.
- Use `ChatPromptTemplate.from_messages([...])` for prompts, not f-strings on raw model calls.
- For tool-using agents in modern LangChain, call `model.bind_tools([...])` and let the graph route tool calls — do not use the deprecated `initialize_agent` helper.
- For RAG, use `langchain_community.vectorstores` with a real vector DB (Chroma, pgvector, Pinecone). Do not roll cosine similarity by hand.

## LangGraph for agents

- Define state as a `TypedDict`; build a `StateGraph`, add nodes and edges, then `.compile()`.
- Add a `MemorySaver()` checkpointer so runs are resumable; pass `{"configurable": {"thread_id": ...}}` on invoke.
- Use `interrupt_before=[...]` on sensitive nodes for human-in-the-loop approvals.

## Observability

- Instrument with LangSmith by setting `LANGCHAIN_TRACING_V2=true` and `LANGCHAIN_API_KEY`. Do not invent custom logging that duplicates traces.

## Avoid

- Mixing `langchain` legacy classes (`LLMChain`, `AgentExecutor`) with LCEL/LangGraph in the same flow.
- Embedding secrets in prompts or template variables.
- Streaming token-by-token without using the framework's `.stream()` / `astream_events()` — do not poll.
