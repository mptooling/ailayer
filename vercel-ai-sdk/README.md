# Vercel AI SDK

> **Category:** AI Agents & Automation | **Pricing:** Free OSS; provider/API usage billed separately | **Type:** TypeScript AI application SDK

Vercel AI SDK is a TypeScript toolkit for building streaming chat, structured generation, tool calling, and AI-powered web app interfaces.

## When To Use

- Use Vercel AI SDK when building AI features in Next.js, React, Svelte, Vue, or TypeScript backends.
- Reach for it when streaming UX, provider abstraction, and tool calling are central.
- Consider it for production web apps that need clean client/server AI integration.

## Practical Tips

- Use provider abstraction to keep model swaps cheap.
- Stream responses for user-facing chat and long-running generation.
- Use structured output helpers when downstream code expects schemas.
- Keep server-side tools permission-checked; never trust the client to decide tool access.

## Watch Outs

- Streaming improves UX but complicates error handling and retries.
- Provider abstraction cannot hide model-specific behavior completely.
- Avoid leaking secrets through client components or browser-visible code.

## Links

- [Vercel AI SDK docs](https://ai-sdk.dev/docs)
- [Vercel AI SDK GitHub](https://github.com/vercel/ai)
