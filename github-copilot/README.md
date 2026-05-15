# GitHub Copilot

> **Category:** AI Coding Assistant | **Pricing:** $10–$39/user/mo (Business: $19/user/mo) | **Type:** Closed-source SaaS

---

## Repository

GitHub Copilot is a closed-source product by GitHub (Microsoft). There is no public source repo, but the VS Code extension source is partially visible:

- [GitHub Copilot VS Code Extension (partial)](https://github.com/github/copilot.vim) — Vim/Neovim plugin (open source)
- [GitHub Copilot.vim](https://github.com/github/copilot.vim) ⭐ 8,000+

---

## Documentation

- [Official Docs](https://docs.github.com/en/copilot)
- [Getting Started Guide](https://docs.github.com/en/copilot/getting-started-with-github-copilot)
- [Copilot in the CLI](https://docs.github.com/en/copilot/github-copilot-in-the-cli)
- [Copilot API / Copilot Extensions](https://docs.github.com/en/copilot/building-copilot-extensions)
- [Pricing](https://github.com/features/copilot#pricing)

---

## Summary

GitHub Copilot is the most widely adopted AI code completion tool, used by 1.3M+ paid subscribers and tens of millions of developers. It integrates directly into VS Code, JetBrains IDEs, Neovim, and GitHub.com, offering inline autocomplete, multi-line suggestions, chat assistance, and (in Enterprise tier) codebase-aware answers trained on your private repos. Achieved 85% Python code completion accuracy in independent benchmarks (2026). In 2025–2026 it expanded into autonomous "Copilot Workspace" — end-to-end task planning and PR generation from a single issue.

**Best for:** Enterprise dev teams wanting seamless IDE integration and GitHub workflow continuity.

---

## Related Materials

- [GitHub Copilot research paper (ACM, 2022)](https://dl.acm.org/doi/10.1145/3520312.3534864) — original study on productivity gains
- [GitHub Octoverse 2025 Report](https://octoverse.github.com/) — adoption and impact data
- [Copilot Workspace announcement blog](https://github.blog/2024-04-29-github-copilot-workspace/)
- [Comparison: Copilot vs Cursor vs Codeium (2026)](https://learn.ryzlabs.com/ai-coding-assistants/cursor-vs-github-copilot-vs-codeium-which-ai-tool-is-best-for-python-development-in-2026)
- [WeavAI: Best Copilot Alternatives 2026](https://weavai.app/blog/en/2026/04/25/10-best-github-copilot-alternatives-2026-full-review/)

---

## AI Agents That Can Use This Tool

| Agent / Framework | How it integrates |
|---|---|
| **Claude Code** | Can invoke Copilot-style completions via VS Code agent API; Claude Code operates alongside Copilot in the same IDE |
| **LangChain** | Can call GitHub Copilot APIs via custom tool wrappers for code generation tasks |
| **AutoGPT** | Can use Copilot CLI (`gh copilot suggest`) as a shell tool |
| **n8n** | GitHub node + Copilot CLI integration for automated PR review workflows |
| **CrewAI** | Agents can delegate code-writing tasks to Copilot via GitHub Actions |

---

## When To Use

- Use this skill when scripting Copilot CLI calls, configuring Copilot for a repo, or building Copilot Extensions.
- Add `.github/copilot-instructions.md` at repo root — Copilot Chat reads it as the system context for every turn in this repo.
- Keep instructions imperative and short: project conventions, build/test commands, and forbidden patterns. Same scope rules as Cursor's `.cursorrules`.

## Practical Tips

- Use this skill when scripting Copilot CLI calls, configuring Copilot for a repo, or building Copilot Extensions.
- Add `.github/copilot-instructions.md` at repo root — Copilot Chat reads it as the system context for every turn in this repo.
- Keep instructions imperative and short: project conventions, build/test commands, and forbidden patterns. Same scope rules as Cursor's `.cursorrules`.

## Watch Outs

- Putting secrets or internal URLs in `.github/copilot-instructions.md` — Copilot includes it in prompts that may be logged.
- Using Copilot suggestions verbatim in security-sensitive code (auth, crypto, query construction) without manual review.
- Maintaining duplicate rules in `.cursorrules` and `copilot-instructions.md`; pick one source of truth and symlink or reference.

---

*Last updated: April 2026*
