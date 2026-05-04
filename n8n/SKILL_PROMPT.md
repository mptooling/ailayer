# n8n skill

Use this skill when triggering or extending n8n workflows from code, or authoring AI-powered workflows.

## Setup

- Self-host: `docker run -it --rm -p 5678:5678 -v ~/.n8n:/home/node/.n8n n8nio/n8n`. Cloud: `n8n.cloud`. Both expose the same REST API.
- Generate an API key in Settings → API. Send as `X-N8N-API-KEY: <key>`. Base URL `<host>/api/v1/`.

## Triggering a workflow

- Build the workflow in the UI; expose it with a Webhook trigger node — the cleanest contract for code-to-n8n calls.
- Call `POST <webhook_url>` with the payload the workflow's first node expects. The webhook URL is shown in the trigger node config.
- For workflows without a webhook, `POST /workflows/{id}/run` (Enterprise) or use `n8n execute --id <id>` from the CLI in self-host setups.

## Authoring AI workflows

- Use the LangChain-family nodes (`AI Agent`, `Chain`, `Memory`, `Vector Store`, `Tool`) under the AI category — they wrap LangChain primitives so you don't write Python.
- Drive an `AI Agent` node with: a chat model (Anthropic/OpenAI), a memory node (Buffer Memory for conversations, Window Memory for fixed context), and a list of tool nodes the agent can call.
- For RAG, chain `Document Loader → Text Splitter → Embeddings → Vector Store`. Reuse the same vector store node in the retriever step downstream.

## Custom nodes

- Scaffold with `npm init n8n-nodes-package`. Implement `description` (the metadata UI uses) and `execute()` (the runtime). Publish to npm; n8n auto-discovers nodes matching `n8n-nodes-*`.
- Prefer extending an existing node over forking n8n core.

## Avoid

- Storing credentials in workflow JSON; always use the Credentials store and reference by ID.
- Webhook-triggered workflows that exceed 5 minutes — n8n returns `504` to the caller. For long jobs, return immediately and notify on completion.
- Treating the AI Agent node as deterministic; pin temperature low and add a "Validate Output" code step before downstream side effects.
- Mixing self-hosted and cloud workflows in one repo without env-specific webhook URLs in config.
