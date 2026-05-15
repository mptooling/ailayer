# FastMCP

> **Category:** MCP & Tooling | **Pricing:** Free OSS | **Type:** Python MCP server framework

FastMCP is a Python framework for building MCP servers with higher-level primitives than the raw protocol SDK.

## When To Use

- Use FastMCP when building Python MCP servers for internal APIs, databases, or developer tools.
- Reach for it when you want quick server composition, typed tools, and production-friendly patterns.
- Consider it when converting existing Python services into model-accessible tools.

## Practical Tips

- Keep each tool small, typed, and permission-aware.
- Prefer explicit schemas and docstrings over clever dynamic tool generation.
- Add tests that call tools directly without a model.
- Use auth and deployment patterns before exposing servers beyond local development.

## Watch Outs

- FastMCP makes server creation easy; it does not make every API safe for agents.
- Avoid wrapping dangerous operations without confirmations and audit logs.
- Keep model-facing descriptions accurate and boring.

## Links

- [FastMCP docs](https://gofastmcp.com/)
- [FastMCP GitHub](https://github.com/jlowin/fastmcp)
