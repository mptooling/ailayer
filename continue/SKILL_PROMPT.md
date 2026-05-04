# Continue skill

Use this skill when configuring or scripting the Continue extension for VS Code or JetBrains.

## Setup

- Install the IDE extension from the marketplace; configuration lives at `~/.continue/config.json` (or `config.yaml` from v0.9+).
- Pick model providers in `models: [...]` — supports `anthropic`, `openai`, `azure`, `ollama`, `mistral`, `bedrock`. Each entry needs `title`, `provider`, `model`, and `apiKey` (or env var reference like `${ANTHROPIC_API_KEY}`).
- For data-private setups, run Ollama locally and point Continue at `provider: ollama, apiBase: http://localhost:11434`.

## Config patterns

- Set `tabAutocompleteModel` separately from the chat model — autocomplete needs a fast, small model (e.g. `qwen-2.5-coder:1.5b`); chat can use Claude or GPT-4.
- Define team-shared rules under `systemMessage` or as a `customCommand`. Custom commands appear as slash-commands in the chat.
- Declare context providers under `contextProviders: [...]`: `code`, `docs`, `git-diff`, `terminal`, `tree`, `url`. Add only what's needed — every provider eats context budget.

## Slash commands

- Author a custom slash command as `{name, prompt, description}` in `customCommands`. The prompt template can reference `{{{ input }}}` and selected code via `{{{ selection }}}`.
- Common patterns: `/test` to generate unit tests, `/explain` for code walkthroughs, `/review` for code review with a specific rubric.

## Avoid

- Committing `config.json` with raw API keys — use `${ENV_VAR}` references and document required env vars in the repo README.
- Enabling all context providers globally; the LLM context fills with low-signal data and answer quality drops.
- Mixing autocomplete and chat models that have very different tokenisers — completions feel inconsistent.
