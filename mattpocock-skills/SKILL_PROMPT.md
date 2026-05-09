---
name: mattpocock-skills
description: Composable agent skills targeting four failure modes — alignment, verbosity, broken code, and architecture rot.
category: Marketplace
triggers: [grill-me, grill-with-docs, tdd, diagnose, improve-codebase-architecture, zoom-out, to-prd, to-issues, triage, prototype, caveman, mattpocock]
safety: medium
version: 2026-05-09
homepage: https://github.com/mattpocock/skills
---

# mattpocock/skills skill

Use this skill when the user wants to install Matt Pocock's "Skills for Real Engineers" pack, or asks for one of its slash-commands by name (`/grill-me`, `/grill-with-docs`, `/tdd`, `/diagnose`, `/improve-codebase-architecture`, `/zoom-out`, `/to-prd`, `/to-issues`, `/triage`, `/prototype`, `/caveman`, `/git-guardrails-claude-code`, `/setup-pre-commit`).

Targets Claude Code, Codex CLI, OpenCode, and Cursor.

## Install

Run the interactive installer (it asks which skills to take and which agents to install them into):

```bash
npx skills@latest add mattpocock/skills
```

Then, inside the chosen agent, run `/setup-matt-pocock-skills`.

`/setup-matt-pocock-skills` is mandatory — it writes the per-repo config (issue tracker = GitHub / Linear / local files; triage label vocabulary; docs location) that the engineering skills consume. The other engineering skills (`to-issues`, `to-prd`, `triage`, `diagnose`, `tdd`, `improve-codebase-architecture`, `zoom-out`) silently no-op or behave wrongly without it.

Pin a version when stability matters: `npx skills@<version> add mattpocock/skills`.

## Use

Pick the smallest set that maps to the failure mode you're hitting — the skills are designed to compose, not to be installed wholesale.

| Failure mode | Reach for |
|---|---|
| User and agent are talking past each other | `/grill-me` (non-code), `/grill-with-docs` (code; also writes `CONTEXT.md` + ADRs) |
| Agent is too verbose / inconsistent naming | `/grill-with-docs` to build shared `CONTEXT.md` |
| Code doesn't work, no feedback loop | `/tdd` (red-green-refactor), `/diagnose` (debugging discipline) |
| Architecture has decayed | `/improve-codebase-architecture` (run every few days), `/zoom-out` |
| Need a PRD or issues from this conversation | `/to-prd`, `/to-issues` |
| Triaging an issue backlog | `/triage` |
| Want to spike a design before committing | `/prototype` |
| Want token reduction on long sessions | `/caveman` |
| Want to block dangerous git in Claude Code | `/git-guardrails-claude-code` |
| Want pre-commit hygiene (Husky/lint-staged/Prettier/types/tests) | `/setup-pre-commit` |

`/grill-with-docs` is the highest-leverage starter. Run it before any non-trivial change — it produces both alignment and a `CONTEXT.md` that subsequent skills read.

`/improve-codebase-architecture` is intended as a periodic pass, not a one-shot. The author recommends every few days on active codebases.

## Avoid

- **Installing every skill.** The pack is à la carte by design; bulk installs dilute the slash-command namespace and make agents pick wrong skills. Curate.
- **Skipping `/setup-matt-pocock-skills`.** The engineering skills depend on the per-repo config it writes; without it `to-issues`/`triage`/etc. behave unpredictably.
- **Treating these as a replacement for `obra/superpowers` or `wshobson/agents`.** They compose well, they don't substitute. Don't enable all three at once without auditing slash-command name collisions (`/tdd` exists in multiple packs).
- **Using `npx skills@latest`** in unattended/CI contexts. Pin to a version — `npx skills@<x.y.z> add mattpocock/skills` — to get reproducible installs and avoid silent supply-chain drift.
- **Editing the installed skill files in `~/.claude/skills/` directly.** Re-running the installer will overwrite. Fork the repo or copy out before customising.
- **Running `/triage` or `/to-issues` against a private/sensitive issue tracker without confirming the agent's auth scope** — both write to GitHub or Linear, and the agent will use whatever token is present.

## Verify

After install, in the chosen agent:

```text
/setup-matt-pocock-skills        # confirms the per-repo config was written
/grill-me                        # the cheapest sanity check — should start interrogating immediately
```

Confirm the skills landed where expected:

- Claude Code: `~/.claude/skills/<skill>/SKILL.md` (or `~/.claude/commands/<skill>.md` depending on installer mode).
- Codex CLI: `~/.codex/skills/<skill>/SKILL.md`.
- Cursor / OpenCode: per-agent skill directory.

`grep -rl "matt-pocock-skills" ~/.claude ~/.codex 2>/dev/null` to spot all installed artefacts before merging changes.
