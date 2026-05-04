# Caveman

> **Category:** AI Coding Assistant (plugin / agent skill) | **Pricing:** Free (open source) | **Type:** Open Source (MIT)

---

## Repository

- [GitHub — JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) ⭐ 53,000+
- Companion repos: [cavemem](https://github.com/JuliusBrussee/cavemem) (memory) · [cavekit](https://github.com/JuliusBrussee/cavekit) (toolkit)
- Homepage: [getcaveman.dev](https://getcaveman.dev/)

---

## Documentation

- [Install script (one-liner)](https://github.com/JuliusBrussee/caveman#install)
- [Intensity levels: Lite / Full / Ultra / 文言文](https://github.com/JuliusBrussee/caveman#intensity-levels)
- [Caveman skills (commit, review, compress, stats)](https://github.com/JuliusBrussee/caveman#caveman-skills)
- [Benchmarks](https://github.com/JuliusBrussee/caveman#benchmarks)
- [Evals (technical accuracy retention)](https://github.com/JuliusBrussee/caveman#evals)

---

## Summary

Caveman is a multi-agent plugin that flips a coding agent into "caveman mode" — terse, fragment-style responses that cut **~65–75% of output tokens** while keeping technical accuracy. The viral observation it formalises: LLMs respond just as correctly when prompted to drop the connective tissue ("The reason your component is re-rendering is likely because…") and lead with the substance ("New object ref each render. Wrap in `useMemo`."). Caveman packages this as a one-line installer that detects 30+ agents (Claude Code, Codex, Gemini CLI, Cursor, Windsurf, Cline, Copilot, Continue, Aider, Goose, OpenHands, Warp, Replit Agent, …) and wires the right native install for each. On Claude Code it ships a `/caveman` slash command, statusline badge, hooks, and an MCP "shrink" proxy that also compresses *input* tokens (~46% on top of the output savings). Sub-skills include `caveman-commit` (terse commit messages), `caveman-review` (one-line code reviews), `caveman-compress`, and `caveman-stats`. Multiple intensity levels — Lite, Full, Ultra, and 文言文 (classical Chinese) — let you dial how much fluff to drop.

**Best for:** Engineers running long agent sessions where output volume matters (latency, cost, scrollback fatigue); teams standardising on a shared "less talk, more substance" agent voice.

---

## Related Materials

- [getcaveman.dev](https://getcaveman.dev/) — homepage with live demos
- [cavemem](https://github.com/JuliusBrussee/cavemem) — caveman memory layer
- [cavekit](https://github.com/JuliusBrussee/cavekit) — caveman dev toolkit
- [Token-reduction prompt-engineering paper (cited by repo)](https://arxiv.org/abs/2604.00025)
- [Anthropic — Claude Code skills](https://docs.anthropic.com/en/docs/claude-code)

---

## AI Agents That Can Use This Tool

| Agent / Framework | How it integrates |
|---|---|
| **Claude Code** | Native plugin (`claude plugin install caveman@caveman`); `/caveman` slash command, statusline badge, MCP shrink proxy |
| **Codex CLI** | Plugin via the install script; toggle with `$caveman`; auto-start via `.codex/hooks.json` |
| **Gemini CLI** | Extension via `gemini extensions install https://github.com/JuliusBrussee/caveman` |
| **Cursor / Windsurf / Cline / GitHub Copilot** | Skill via `npx skills add JuliusBrussee/caveman -a <profile>`; with `--with-init` writes `.cursor/rules/caveman.mdc` etc. |
| **30+ other agents** | Auto-detected by the universal installer (Aider, Goose, Continue, Roo, Amp, Junie, Warp, Replit Agent, OpenHands, Antigravity, …) |

---

*Last updated: 2026-05*
