# CrewAI skill

Use this skill when orchestrating multiple role-based agents that collaborate on a task.

## Setup

- Install with `pip install crewai crewai-tools`. Requires Python ≥ 3.10.
- Set the LLM env var for your provider: `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, or configure `LiteLLM` for local models.

## Modelling a crew

- Define each `Agent` with three fields: `role`, `goal`, `backstory`. Keep them short and concrete — the backstory shapes tone, not behaviour.
- Define each `Task` with `description`, `expected_output`, and the `agent` that owns it. `expected_output` is what gates task completion — write it precisely.
- Compose them into a `Crew(agents=[...], tasks=[...], process=Process.sequential)`. Use `Process.hierarchical` only when one agent should delegate to others; it requires a `manager_llm`.

## Tools

- Pass tools per-agent via `tools=[...]`. Use built-ins from `crewai_tools` (`SerperDevTool`, `FileReadTool`, `CodeInterpreterTool`) before writing custom ones.
- Custom tools subclass `BaseTool` and implement `_run`. Keep tool descriptions imperative — agents pick tools from descriptions.

## Memory and context

- Enable `Crew(memory=True, ...)` to share context across tasks. Configure `embedder=` if you need a non-default embedding model.
- Pass shared inputs at runtime: `crew.kickoff(inputs={"topic": "..."})`. Reference them in task descriptions with `{topic}`.

## Avoid

- Giving every agent every tool — narrow tool lists improve reasoning.
- Vague `expected_output` like "a summary" — agents will keep refining indefinitely.
- Mixing CrewAI with raw LangChain `AgentExecutor`; use LangChain *tools* with CrewAI agents instead.
- Running long crews without `verbose=True` during development — silent loops are nearly impossible to debug.
