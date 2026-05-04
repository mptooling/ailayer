# AutoGPT skill

Use this skill when running or extending AutoGPT for autonomous goal-directed agents.

## Setup

- Self-hosted: `git clone https://github.com/Significant-Gravitas/AutoGPT && cd AutoGPT && docker compose up`. Reads `OPENAI_API_KEY` and `ANTHROPIC_API_KEY` from `.env`.
- Cloud (faster start): use the AutoGPT Platform at `platform.agpt.co` for the no-code workflow builder; expose runs via its REST API.

## Defining a goal

- Express the goal as a single concrete outcome, not a process: "produce a market-sizing report on X with cited sources" beats "research X."
- Set `ai_role`, `ai_goals` (≤ 5), and `cost_limit` in the agent config. Without a cost limit, runaway agents will burn through API quota.
- Use the **Agent Protocol** REST endpoints (`POST /ap/v1/agent/tasks`, `GET /ap/v1/agent/tasks/{id}/steps`) for programmatic control. This is the open standard — code against it instead of AutoGPT-specific routes when possible.

## Custom agents (Forge)

- Scaffold with `./run agent create my-agent`. Implement `task_handler` and `step_handler` in `forge/agent.py`; everything else is wiring.
- Add abilities under `forge/sdk/abilities/`. Each ability is a Python function decorated with `@ability(name=…, description=…, parameters=[…])`. Descriptions are how the planner picks abilities — keep them imperative.
- Persist state via the provided `AgentDB` (SQLite) rather than rolling your own.

## Avoid

- Letting an agent loop without `cost_limit` or `step_limit`.
- Granting filesystem write access outside the workspace dir; AutoGPT enforces a sandbox — do not bypass it.
- Mixing the legacy CLI (`run.py`) and the Platform deployment in the same project — pick one.
- Using Claude/GPT-4 with empty system prompts; AutoGPT's planning quality drops sharply without a constrained role.
