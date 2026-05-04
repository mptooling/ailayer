# LangGraph skill

Use this skill when building stateful, multi-actor agent applications where you need persistence, human-in-the-loop, or branching control flow.

## Setup

- Install: `pip install langgraph langgraph-checkpoint-sqlite langchain-anthropic` (swap the model package as needed).
- Read API keys from env (`ANTHROPIC_API_KEY`, `OPENAI_API_KEY`). For tracing: `LANGCHAIN_TRACING_V2=true`, `LANGCHAIN_API_KEY=...`.

## Defining the graph

- Model state as a `TypedDict`. Use `Annotated[list, add_messages]` for conversation history; LangGraph merges automatically.
- Build with `StateGraph(MyState)`. Add nodes with `.add_node("name", fn)` where each `fn(state) -> dict` returns the *delta* to merge into state.
- Wire flow with `.add_edge(a, b)` for unconditional, `.add_conditional_edges(a, router_fn, {"next_a": "node_a", "next_b": "node_b"})` for branching.
- Set `START` and `END` constants as the entry/exit edges. Compile with `.compile(checkpointer=MemorySaver())`.

## Persistence and threads

- Always attach a checkpointer in production (`SqliteSaver.from_conn_string(...)` or `PostgresSaver`). Without it, state is lost on process restart.
- Pass `config={"configurable": {"thread_id": "..."}}` on every `.invoke()` / `.stream()`. Same `thread_id` resumes; new `thread_id` starts fresh.
- Inspect or rewind state: `graph.get_state(config)`, `graph.update_state(config, values)`, `graph.get_state_history(config)`.

## Human-in-the-loop

- Mark sensitive nodes with `interrupt_before=["approve"]` on `.compile(...)`. The graph pauses at that node; resume by re-invoking with the same `thread_id`.
- Surface the pending state to a UI or approval channel — never auto-resume on a timeout.

## Tools and subgraphs

- Bind tools to the model with `model.bind_tools([...])` and route tool-call deltas to a `ToolNode(tools)` for execution.
- Decompose complex flows into subgraphs via `.add_node("sub", subgraph)` — keeps top-level graphs readable and lets you reuse subflows.

## Avoid

- Mutating `state` in-place inside a node — return a delta dict instead.
- Skipping the checkpointer in dev "to keep things simple" — debugging stateless graphs is much harder than debugging stateful ones.
- Mixing LangChain's deprecated `AgentExecutor` with LangGraph nodes; pick one.
