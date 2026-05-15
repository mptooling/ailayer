# Roo Code

> **Category:** AI Coding Assistant | **Pricing:** Free OSS client; model/API costs vary | **Type:** Open-source VS Code agent

Roo Code is an open-source VS Code coding agent descended from the Cline ecosystem, focused on configurable modes, model choice, and autonomous repo work.

## When To Use

- Use Roo Code when you want a VS Code agent with role/mode customization and bring-your-own-model support.
- Reach for it for teams experimenting with specialized agent modes such as architect, code, debug, and review.
- Prefer it when local extension control matters more than a managed cloud coding environment.

## Practical Tips

- Define modes around workflow boundaries: planning, implementation, review, and debugging.
- Keep project rules short and mode-aware so the model gets relevant constraints.
- Use approval gates for command execution and large file edits.
- Compare model providers on real repo tasks instead of synthetic demos.

## Watch Outs

- Too many custom modes can make behavior unpredictable.
- Agent rules are advisory; enforce critical policy with tests, linters, and CI.
- Watch model spend during multi-step loops.

## Links

- [Roo Code website](https://roocode.com/)
- [Roo Code GitHub](https://github.com/RooVetGit/Roo-Code)
