# Model Context Protocol Servers

> **Category:** MCP & Tooling | **Pricing:** Free OSS | **Type:** Official/community MCP server collection

The Model Context Protocol servers collection provides reusable MCP servers for common systems such as filesystems, GitHub, databases, browsers, and SaaS APIs.

## When To Use

- Use these servers when an existing MCP integration covers the tool you need.
- Reach for them before writing a custom server from scratch.
- Consider them for prototyping agent access to common developer systems.

## Practical Tips

- Prefer official or well-maintained servers for sensitive systems.
- Pin versions for team workflows.
- Review each server's permissions, environment variables, and transport mode.
- Run high-risk servers locally or in isolated environments first.

## Watch Outs

- A server collection is not a trust boundary; each server must be reviewed independently.
- Avoid installing broad filesystem or browser automation servers casually.
- Watch for abandoned servers and stale dependencies.

## Links

- [MCP servers GitHub](https://github.com/modelcontextprotocol/servers)
- [MCP docs](https://modelcontextprotocol.io/)
