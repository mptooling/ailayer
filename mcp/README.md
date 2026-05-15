# Model Context Protocol

> **Category:** MCP & Tooling | **Pricing:** Open standard | **Type:** Protocol and SDK ecosystem

Model Context Protocol (MCP) standardizes how AI applications expose tools, resources, prompts, and context to models and agents.

## When To Use

- Use MCP when multiple agents or clients need to connect to the same tools and data sources.
- Reach for it when custom one-off tool integrations are multiplying.
- Consider it for developer platforms that need reusable AI-accessible capabilities.

## Practical Tips

- Start with read-only tools before exposing mutations.
- Keep tool names, descriptions, schemas, and error messages clear; the model relies on them for selection.
- Put authentication and authorization inside the server, not only in the client prompt.
- Log tool calls for auditability.

## Watch Outs

- MCP expands agent capability and attack surface at the same time.
- Treat prompt injection through tool outputs as a real threat.
- Avoid registering broad shell or database tools without tight permissions.

## Links

- [MCP docs](https://modelcontextprotocol.io/)
- [MCP GitHub organization](https://github.com/modelcontextprotocol)
