# Continue

> **Category:** AI Coding Assistant | **Pricing:** Free (open source) | **Type:** Open Source (Apache 2.0)

---

## Repository

- [GitHub — continuedev/continue](https://github.com/continuedev/continue) ⭐ 24,000+

---

## Documentation

- [Official Docs](https://docs.continue.dev/)
- [Getting Started](https://docs.continue.dev/quickstart)
- [Configuration Reference](https://docs.continue.dev/reference/config)
- [Model Providers](https://docs.continue.dev/reference/model-providers)
- [Slash Commands](https://docs.continue.dev/customization/slash-commands)
- [Context Providers](https://docs.continue.dev/customization/context-providers)

---

## Summary

Continue is the leading open-source AI code assistant, designed as a pluggable extension for VS Code and JetBrains. Unlike Copilot or Cursor, Continue lets you connect any LLM backend — OpenAI, Anthropic Claude, local Ollama models, Azure OpenAI, and more — giving teams full control over data privacy and model choice. It supports inline autocomplete, chat, and a rich context system (pull in docs, Jira tickets, files, terminal output). Configuration is done via a simple `config.json`, making it easy for IT teams to standardise across the org. Particularly popular in security-sensitive environments where cloud-based coding tools are restricted.

**Best for:** IT/engineering teams that need model flexibility, data privacy, or want to run AI coding assistance on-premises.

---

## Related Materials

- [Continue blog](https://blog.continue.dev/)
- [Continue Discord community](https://discord.gg/vapESyrFmJ)
- [awesome-cursorrules (compatible)](https://github.com/PatrickJS/awesome-cursorrules)
- [Local LLMs with Continue + Ollama guide](https://docs.continue.dev/walkthroughs/ollama)
- [Best GitHub Copilot Alternatives 2026](https://emergent.sh/learn/best-copilot-alternatives-and-competitors)

---

## AI Agents That Can Use This Tool

| Agent / Framework | How it integrates |
|---|---|
| **Claude Code** | Can be run alongside Continue in the same repo; both can share context via project files |
| **LangChain** | Continue's context providers can feed data from LangChain-indexed vector stores |
| **Ollama** | Continue is the primary IDE frontend for locally running Ollama LLMs |
| **LlamaIndex** | Can connect Continue to LlamaIndex retrieval for RAG-powered code assistance |
| **n8n** | n8n can invoke Continue's slash commands via VS Code CLI extensions |

---

## When To Use

- Use this skill when configuring or scripting the Continue extension for VS Code or JetBrains.
- Set `tabAutocompleteModel` separately from the chat model — autocomplete needs a fast, small model (e.g. `qwen-2.5-coder:1.5b`); chat can use Claude or GPT-4.
- Declare context providers under `contextProviders: [...]`: `code`, `docs`, `git-diff`, `terminal`, `tree`, `url`. Add only what's needed — every provider eats context budget.

## Practical Tips

- Install the IDE extension from the marketplace; configuration lives at `~/.continue/config.json` (or `config.yaml` from v0.9+).
- Pick model providers in `models: [...]` — supports `anthropic`, `openai`, `azure`, `ollama`, `mistral`, `bedrock`. Each entry needs `title`, `provider`, `model`, and `apiKey` (or env var reference like `${ANTHROPIC_API_KEY}`).
- For data-private setups, run Ollama locally and point Continue at `provider: ollama, apiBase: http://localhost:11434`.

## Watch Outs

- Committing `config.json` with raw API keys — use `${ENV_VAR}` references and document required env vars in the repo README.
- Enabling all context providers globally; the LLM context fills with low-signal data and answer quality drops.
- Mixing autocomplete and chat models that have very different tokenisers — completions feel inconsistent.

---

*Last updated: April 2026*
