# Aider

> **Category:** AI Coding Assistant | **Pricing:** Free (open source) | **Type:** Open Source (Apache 2.0)

---

## Repository

- [GitHub — paul-gauthier/aider](https://github.com/Aider-AI/aider) ⭐ 25,000+

---

## Documentation

- [Official Docs](https://aider.chat/)
- [Getting Started](https://aider.chat/docs/install.html)
- [Supported Models](https://aider.chat/docs/llms.html)
- [Configuration](https://aider.chat/docs/config.html)
- [Scripting Aider](https://aider.chat/docs/scripting.html)
- [Aider in your editor](https://aider.chat/docs/usage/editor.html)

---

## Summary

Aider is a terminal-based AI pair programmer that works directly inside your git repository. You describe a change in plain English, and Aider edits your source files and creates well-scoped git commits automatically. It supports Claude, GPT-4, Gemini, and local models via LiteLLM. Aider's key differentiator is its repo-map — a token-efficient representation of your entire codebase structure that it passes to the LLM, enabling accurate multi-file edits without blowing context windows. It is consistently ranked #1 or #2 among open-source AI coding tools. Particularly powerful for scripted, batch code changes (refactors, adding tests) across large codebases.

**Best for:** Developers who prefer the terminal, want git-native AI coding, or need to automate large-scale refactoring.

---

## Related Materials

- [Aider leaderboard (LLM coding benchmarks)](https://aider.chat/docs/leaderboards/)
- [Aider blog](https://aider.chat/blog/)
- [Scripting Aider for automation](https://aider.chat/docs/scripting.html)
- [Best AI Coding Agents 2026 — MightyBot](https://mightybot.ai/blog/coding-ai-agents-for-accelerating-engineering-workflows/)
- [10 Best Open Source Agent Projects — Flowith](https://flowith.io/blog/10-best-open-source-agent-projects-github-2026/)

---

## AI Agents That Can Use This Tool

| Agent / Framework | How it integrates |
|---|---|
| **Claude Code** | Direct competitor/complement — both operate in terminal with git; can be combined in CI pipelines |
| **AutoGPT** | AutoGPT can call `aider` as a shell command for code-editing subtasks |
| **LangChain** | LangChain agents can invoke Aider via subprocess for file-editing operations |
| **n8n** | n8n can trigger Aider via shell node as part of automated PR workflows |
| **CrewAI** | A CrewAI "developer" agent can delegate file edits to Aider |

---

*Last updated: April 2026*
