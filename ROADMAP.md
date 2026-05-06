# Library & ailayer Implementation Roadmap

> A phased PR plan to turn `ai_skills_and_tools` from a vendor catalogue into a productivity-grade skill library that injects cleanly into Claude Code, Codex CLI, and Gemini CLI.
>
> **Last updated:** 2026-05-06 · **Total PRs planned:** 47 · **Current state:** see [Diagnostic findings](#diagnostic-findings)

Each PR below is **independently mergeable** and scoped to ~1 day of work. Dependencies are explicit. Phases are sequencing guidance, not hard gates — if a downstream PR is unblocked, ship it.

---

## Diagnostic findings (research summary, mid-2026)

Four parallel research agents (Claude Code, Codex CLI, Gemini CLI, cross-tool patterns) surfaced the following:

### Foundational bugs in `ailayer` (block everything else)

| # | Layer | Bug | Source of truth |
|---|---|---|---|
| F1 | Codex adapter | Writes `~/.codex/config.yaml`; Codex actually reads `~/.codex/config.toml` | [Codex config reference](https://developers.openai.com/codex/config-reference) |
| F2 | Codex adapter | Hook event aliases `pre_apply`/`post_apply` are wrong — real events are `PreToolUse`/`PostToolUse`/`SessionStart`/`Stop`/`UserPromptSubmit`/`PermissionRequest` | [Codex hooks docs](https://developers.openai.com/codex/hooks) |
| F3 | Codex adapter | Skills injected as `## skill:<name>` blocks in `AGENTS.md` — Codex now has a native skills dir at `~/.codex/skills/<name>/SKILL.md` | [openai/codex#skills](https://github.com/openai/codex) |
| F4 | Gemini adapter | Writes `~/.gemini/commands/<name>.md` for skills — Gemini expects `.toml` files with `description` + `prompt` fields and `{{args}}`/`!{shell}`/`@{file}` injectors | [Gemini custom-commands docs](https://geminicli.com/docs/cli/custom-commands/) |
| F5 | Gemini adapter | Hook event aliases collapse 11+ real events (`BeforeTool`/`AfterTool`/`BeforeAgent`/`AfterAgent`/`BeforeModel`/`AfterModel`/`BeforeToolSelection`/`SessionStart`/`SessionEnd`/`Notification`/`PreCompress`) into 2 (`beforeCommand`/`afterCommand`) | [Gemini hooks reference](https://geminicli.com/docs/hooks/reference/) |
| F6 | Library content | All 22 entries ship a `SKILL_PROMPT.md`, but 21 of 22 lack the frontmatter required by the schema (see `docs/SKILL_PROMPT_SCHEMA.md`); `ailayer lint skills` flags them as errors | linter output, May 2026 |

### Library-content gaps

- **Skill prompts lack metadata**: 21 of 22 `SKILL_PROMPT.md` files have no frontmatter — no machine-readable category, description, triggers, or safety level. `ailayer lint skills` enforces this from PR 11 onward.
- **No methodology skills**: TDD, brainstorming, plans, debugging, verification — none are in the library, only loaded via Claude Code's `superpowers` plugin.
- **No domain skills**: Postgres, Terraform, OpenAPI, security review, GraphQL, release engineering — all unrepresented.
- **No CLI-helper skills**: `rg`/`fd`/`ast-grep`/`gh`/`jq`/`repomix`/`difftastic` — agents lack guided usage.
- **No bundle concept**: every skill installs one at a time; no `ailayer add bundle <name>` for skill packs, hook bundles, or MCP bundles.
- **No statusline / cost tracker**: ccusage isn't profiled or wired.

### Marketplace / MCP gaps

- **Missing marketplace**: `wshobson/agents` (80 plugins, 185 agents, 153 skills) is the largest community collection not yet referenced.
- **Missing high-leverage MCPs**: Datadog, Honeycomb, LaunchDarkly, Linear, Vercel, Figma, Sentry, exa, firecrawl, deepcontext, Snyk.
- **Missing index profile**: `VoltAgent/awesome-agent-skills` (1k+ cross-CLI skills) — the canonical discovery surface.

---

## Phase 0 — Foundation (fix `ailayer` before adding content)

> Without these, anything we add to the library either fails to inject or lands in the wrong file. Ship Phase 0 in order; everything else can parallelize.

### PR 1 — `docs(roadmap): land the diagnostic + PR sequence`

- **Goal:** ship this `ROADMAP.md` so the rest of the work has a shared spec.
- **Scope:** add `ROADMAP.md` (this file); update `INDEX.md` Roadmap section to link to it.
- **Acceptance:** `grep -c "^### PR " ROADMAP.md` ≥ 40; `INDEX.md` references it.
- **Depends on:** none.

### PR 2 — `feat(ailayer/codex): switch config from YAML to TOML`

- **Goal:** Codex CLI reads `~/.codex/config.toml`, not `config.yaml`. Make `CodexAdapter` write the right file.
- **Scope:** replace `_read_yaml`/`_write_yaml` with `_read_toml`/`_write_toml` (use `tomli`/`tomli-w` or stdlib `tomllib` + a writer); update `global_settings_file()` to return `~/.codex/config.toml`; add `tomli-w` to `pyproject.toml`; update `CLAUDE.md` table.
- **Acceptance:** `ailayer add mcp foo --tool codex --cmd echo` writes valid TOML readable by `codex`; `ailayer status` reads it back.
- **Depends on:** PR 1.

### PR 3 — `feat(ailayer/codex): correct hook event aliases`

- **Goal:** Codex hook events `pre`/`post`/`stop`/`notification` map to real Codex events.
- **Scope:** replace `_HOOK_EVENT_ALIASES` in `tools/codex.py` with `pre→PreToolUse`, `post→PostToolUse`, `stop→Stop`, `notification→UserPromptSubmit`, plus `session-start→SessionStart`, `permission→PermissionRequest`. Emit hooks under `[[hooks.<EventName>]]` (or `~/.codex/hooks.json`). Set `[features] codex_hooks = true` automatically.
- **Acceptance:** `ailayer add hook lint --event post --command "ruff ."` produces a `[[hooks.PostToolUse]]` block; `codex` actually fires it.
- **Depends on:** PR 2.

### PR 4 — `feat(ailayer/codex): write skills to ~/.codex/skills/<name>/SKILL.md`

- **Goal:** stop injecting skills as labelled sections in `AGENTS.md`; use Codex's native skills directory.
- **Scope:** rewrite `CodexAdapter.add_skill` / `remove_skill` to mkdir `~/.codex/skills/<name>/` and write `SKILL.md`; preserve `--no-global --project DIR` to write `<proj>/.codex/skills/<name>/SKILL.md`. Migrate any existing `## skill:<name>` blocks out of `AGENTS.md` (one-shot, `ailayer migrate codex-skills`).
- **Acceptance:** `ailayer add skill cursor --tool codex` creates `~/.codex/skills/cursor/SKILL.md`; `codex` lists it under `/skills`.
- **Depends on:** PR 2.

### PR 5 — `feat(ailayer/gemini): write slash-commands as TOML, not Markdown`

- **Goal:** Gemini CLI expects `~/.gemini/commands/<name>.toml`; we currently write `.md`.
- **Scope:** rewrite `GeminiAdapter.add_skill` to emit TOML with `description = "..."` and `prompt = """..."""`; preserve `{{args}}`, `!{shell}`, `@{file}` injectors verbatim from the skill source. Add a small `_skill_md_to_toml` adapter that splits a Markdown skill into description (frontmatter or first paragraph) and prompt (body).
- **Acceptance:** `ailayer add skill cursor --tool gemini` creates `~/.gemini/commands/cursor.toml`; `/commands list` in Gemini CLI shows it.
- **Depends on:** PR 1.

### PR 6 — `feat(ailayer/gemini): support full hook event taxonomy`

- **Goal:** expose Gemini's 11 native hook events instead of collapsing to 2.
- **Scope:** in `tools/gemini.py` replace `_HOOK_EVENT_ALIASES` with a richer mapping covering `BeforeTool`/`AfterTool`/`BeforeAgent`/`AfterAgent`/`BeforeModel`/`AfterModel`/`BeforeToolSelection`/`SessionStart`/`SessionEnd`/`Notification`/`PreCompress`. Allow `--matcher` to pass through as the Gemini `matcher` field. Support `sequential: true` and `timeout` knobs.
- **Acceptance:** `ailayer add hook secret-scrub --event before-tool --matcher write_file --command "..."` produces a valid `BeforeTool` entry with matcher.
- **Depends on:** PR 1.

### PR 7 — `feat(ailayer): bundle commands (skill, hook, mcp packs)`

- **Goal:** `ailayer add bundle <name>` installs N skills/hooks/MCP servers in one shot from a manifest.
- **Scope:** add `bundles/` directory at repo root with TOML manifests (`bundles/methodology.toml`, `bundles/safety-rails.toml`, etc.). Each lists `[[skills]]`, `[[hooks]]`, `[[mcps]]`. Implement `commands/bundle.py` with `add` / `remove` / `list`. Reuse existing `add_skill`/`add_hook`/`add_mcp` adapters per item.
- **Acceptance:** `ailayer add bundle methodology --tool all` installs the canonical 7 methodology skills; `ailayer remove bundle methodology` cleans them up.
- **Depends on:** PR 4, PR 5.

### PR 8 — `feat(ailayer): doctor + sync commands`

- **Goal:** `ailayer doctor` diagnoses installs (missing binaries, broken configs, drift between repo manifests and live config); `ailayer sync <manifest.toml>` declaratively reconciles state.
- **Scope:** new `commands/doctor.py` + `commands/sync.py`. Doctor checks: `claude`/`codex`/`gemini` binaries on PATH, settings files parseable, all `_ailayer_name`-tagged entries map to known skills/hooks. Sync: read a project-level `.ailayer.toml`, install missing items, remove extras.
- **Acceptance:** `ailayer doctor` prints a clean report on a freshly bootstrapped machine; `ailayer sync .ailayer.toml` is idempotent.
- **Depends on:** PR 7.

### PR 9 — `feat(ailayer): tests + CI + ruff`

- **Goal:** end the "no test suite, no CI" state acknowledged in `CLAUDE.md`.
- **Scope:** `tests/` directory with pytest; cover each adapter's add/remove for skill/hook/mcp/instruction across global + project scope. GitHub Actions workflow running `ruff check ailayer/` + `pytest`. Use `tmp_path` fixtures so tests touch no real `~/.claude` etc.
- **Acceptance:** CI green on PR; coverage ≥ 70% on `ailayer/tools/`.
- **Depends on:** PR 2, PR 3, PR 5, PR 6 (so the corrected behaviours are what we lock in).

---

## Phase 1 — Skill content for the existing 22 entries

> Today every entry has a README (vendor profile) but no `SKILL_PROMPT.md` (agent HOW-TO). Fix that systematically. Each PR converts one category.

### PR 10 — `feat(skills): bring AI Coding Assistant SKILL_PROMPT.md into schema`

- **Goal:** add frontmatter and align section structure for the 7 coding-assistant entries' existing skill files.
- **Scope:** edit `cursor/`, `continue/`, `aider/`, `windsurf/`, `github-copilot/`, `caveman/`, `claude-mem/` (claude-mem already done in PR 11). Add YAML frontmatter (`name`, `description`, `category`, `triggers`, `safety`); ensure the required `## Avoid` and recommended `## Setup`/`## Use`/`## Verify` sections exist; rewrite anything that's marketing prose into agent-oriented HOW-TO.
- **Acceptance:** `ailayer lint skills` passes (no errors) for all 7 entries; `ailayer list skills` reads category/description from frontmatter.
- **Depends on:** PR 11 (schema + linter).

### PR 11 — `feat(library): SKILL_PROMPT.md schema + linter`

- **Goal:** lock down the `SKILL_PROMPT.md` format so agents, ailayer, and human reviewers have the same expectation.
- **Scope:** write `docs/SKILL_PROMPT_SCHEMA.md` documenting required frontmatter (`name`, `description`, `category`, `triggers`, `safety`), required sections (`## Setup`, `## Use`, `## Avoid`, `## Verify`), and the `ailayer` skill-prompt rendering rules. Add `ailayer lint skills` (or `scripts/lint_skills.py`) that validates every `<tool>/SKILL_PROMPT.md` against the schema.
- **Acceptance:** schema doc exists; linter passes on at least the AI-coding-assistant entries from PR 10.
- **Depends on:** PR 1.

### PR 12 — `feat(skills): bring Agents/Automation SKILL_PROMPT.md into schema`

- **Goal:** add frontmatter and align section structure for the 5 agent-framework entries.
- **Scope:** edit `langchain/`, `langgraph/`, `crewai/`, `autogpt/`, `n8n/`. Add frontmatter; ensure each captures when to reach for this framework vs alternatives, scaffolding command, minimal "hello agent" pattern, deployment story, common footguns.
- **Acceptance:** `ailayer lint skills` passes for all 5; READMEs unchanged.
- **Depends on:** PR 11.

### PR 13 — `feat(skills): bring Writing/Marketing + Data SKILL_PROMPT.md into schema`

- **Goal:** add frontmatter and align section structure for the remaining 10 entries (Jasper, Copy.ai, Perplexity, Notion AI, Writesonic, Julius, Akkio, Obviously AI, Bardeen, Polymer).
- **Scope:** these are mostly SaaS — skill prompts focus on API/integration patterns, when an agent should call them vs roll its own, and credential handling. Add frontmatter to existing files; rewrite content where marketing prose has crept in.
- **Acceptance:** `ailayer lint skills` passes; INDEX.md categories unchanged.
- **Depends on:** PR 11.

---

## Phase 2 — Methodology skills (the canonical seven)

> These are the highest-leverage skills per all four research streams. Each ships as a *new* top-level entry in the library so it injects via `ailayer add skill <name>`.

### PR 14 — `feat(skills): brainstorming`

- **Goal:** ship a Socratic intent-clarification skill modeled on `obra/superpowers:brainstorming`.
- **Scope:** new `brainstorming/` directory with README + `SKILL_PROMPT.md`. Skill triggers on creative work (new feature, new component); guides the agent to surface goals, constraints, success criteria, and unknowns before writing code.
- **Acceptance:** linter green; `ailayer add skill brainstorming --tool all` installs cleanly to all three CLIs.
- **Depends on:** PR 11.

### PR 15 — `feat(skills): writing-plans + executing-plans pair`

- **Goal:** spec→phased plan→execute-with-checkpoint workflow.
- **Scope:** two entries (`writing-plans/`, `executing-plans/`). Writing produces a numbered phased plan with files-to-touch, test gates, rollback notes; executing drives the plan, pausing at every phase boundary for user confirmation.
- **Acceptance:** linter green; cross-references each other; both install to all CLIs.
- **Depends on:** PR 14.

### PR 16 — `feat(skills): test-driven-development`

- **Goal:** strict red-green-refactor discipline as a skill.
- **Scope:** new `tdd/` entry. Refuses to write impl before failing test; covers Python (pytest), TS (vitest/jest), Go (testing), Rust (cargo test). Cites concrete commands.
- **Acceptance:** linter green; example session in skill doc.
- **Depends on:** PR 11.

### PR 17 — `feat(skills): systematic-debugging`

- **Goal:** Reproduce → Isolate → Root-cause → Fix+Defend workflow.
- **Scope:** new `systematic-debugging/` entry. Blocks shotgun fixes; requires a failing repro before any change; requires a regression test in the same commit as the fix.
- **Acceptance:** linter green.
- **Depends on:** PR 11.

### PR 18 — `feat(skills): verification-before-completion`

- **Goal:** evidence-before-assertions — the single highest-leverage skill in the canon.
- **Scope:** new `verification-before-completion/` entry. Forbids "done" claims without pasting the output of build/test/lint commands. Lists per-language verification commands.
- **Acceptance:** linter green.
- **Depends on:** PR 11.

### PR 19 — `feat(skills): dispatching-parallel-agents + using-git-worktrees`

- **Goal:** fan-out for independent tasks + isolation via worktrees.
- **Scope:** two entries. Parallel-agents covers when to dispatch sub-agents (independent, no shared state) and how to brief them. Worktrees covers `git worktree add` patterns, naming convention, cleanup.
- **Acceptance:** linter green; cross-link.
- **Depends on:** PR 11.

### PR 20 — `feat(bundles): methodology pack`

- **Goal:** `ailayer add bundle methodology` installs PRs 14–19 in one go.
- **Scope:** `bundles/methodology.toml` listing all seven skills.
- **Acceptance:** `ailayer add bundle methodology --tool all` installs cleanly; `ailayer remove bundle methodology` is exact.
- **Depends on:** PR 7, PR 14, PR 15, PR 16, PR 17, PR 18, PR 19.

---

## Phase 3 — Domain skills

> Each is a focused, opinionated, ~200-line skill an agent invokes when the task hits its domain.

### PR 21 — `feat(skills): postgres-best-practices`

- **Goal:** indexing, MVCC/VACUUM, WAL tuning, replication, query plans.
- **Scope:** new `postgres/` entry; lifts patterns from `planetscale/database-skills` and Supabase's pack with attribution.
- **Acceptance:** linter green; references `EXPLAIN (ANALYZE, BUFFERS)` workflow.
- **Depends on:** PR 11.

### PR 22 — `feat(skills): migration-safety`

- **Goal:** zero-downtime DB migrations (NOT NULL backfill, expand-contract, online index, FK changes).
- **Scope:** new `migration-safety/` entry. Companion to PR 21.
- **Acceptance:** linter green.
- **Depends on:** PR 21.

### PR 23 — `feat(skills): terraform-review`

- **Goal:** module conventions, state hygiene, plan-review checklist, drift detection.
- **Scope:** new `terraform/` entry; based on `antonbabenko/terraform-skill`.
- **Acceptance:** linter green.
- **Depends on:** PR 11.

### PR 24 — `feat(skills): security-review`

- **Goal:** OWASP 2025 + ASVS 5.0 review skill driven by `git diff`.
- **Scope:** new `security-review/` entry; pairs with `semgrep` and `gitleaks` invocations.
- **Acceptance:** linter green.
- **Depends on:** PR 11.

### PR 25 — `feat(skills): openapi-authoring`

- **Goal:** spec-first API design (OpenAPI 3.1/3.2), validation, code-gen pipeline.
- **Scope:** new `openapi/` entry.
- **Acceptance:** linter green.
- **Depends on:** PR 11.

### PR 26 — `feat(skills): graphql-schema-review`

- **Goal:** federation, schema review checklist, deprecation discipline.
- **Scope:** new `graphql/` entry; based on Apollo's official skill pack.
- **Acceptance:** linter green.
- **Depends on:** PR 11.

### PR 27 — `feat(skills): release-engineering`

- **Goal:** Conventional Commits → semantic-release → changelog → tag → GitHub release.
- **Scope:** new `release-engineering/` entry; lists `commitlint` + `semantic-release` setup; covers npm/PyPI/Cargo flavours.
- **Acceptance:** linter green.
- **Depends on:** PR 11.

### PR 28 — `feat(bundles): backend pack + ops pack`

- **Goal:** two bundles for stack-shaped installs.
- **Scope:** `bundles/backend.toml` (postgres, migration-safety, openapi, security-review); `bundles/ops.toml` (terraform, release-engineering, plus the hook bundles from Phase 5).
- **Acceptance:** both install cleanly via `ailayer add bundle`.
- **Depends on:** PR 21–27, PR 7.

---

## Phase 4 — CLI tooling skills

> Skills that teach the agent to lean on fast CLIs. Each is short (~100 lines) but pays off every session.

### PR 29 — `feat(skills): cli-search-stack (rg, fd, ast-grep)`

- **Goal:** when to reach for which structural/text search tool; common recipes.
- **Scope:** new `cli-search/` entry. Includes `comby` as honourable mention.
- **Acceptance:** linter green.
- **Depends on:** PR 11.

### PR 30 — `feat(skills): cli-data-stack (jq, yq, dasel, gron)`

- **Goal:** JSON/YAML query and edit recipes; `gron` for grep-friendly JSON.
- **Scope:** new `cli-data/` entry.
- **Acceptance:** linter green.
- **Depends on:** PR 11.

### PR 31 — `feat(skills): gh-cli-recipes`

- **Goal:** PR/issue/release/Actions CLI recipes; `gh pr create`, `gh pr view --json`, `gh run watch`, etc.
- **Scope:** new `gh-cli/` entry.
- **Acceptance:** linter green.
- **Depends on:** PR 11.

### PR 32 — `feat(skills): repomix-cold-start`

- **Goal:** how to use `repomix --compress` to load an unfamiliar repo into the agent's context.
- **Scope:** new `repomix/` entry.
- **Acceptance:** linter green.
- **Depends on:** PR 11.

### PR 33 — `feat(skills): difftastic-and-delta`

- **Goal:** syntax-aware diffs as the agent's default review tool.
- **Scope:** new `diff-stack/` entry; covers `git config` integration.
- **Acceptance:** linter green.
- **Depends on:** PR 11.

---

## Phase 5 — Hook bundles (ready-to-install guardrails)

> Each PR ships a TOML bundle in `bundles/` plus example scripts in `bundles/hooks/`.

### PR 34 — `feat(bundles): safety-rails (PreToolUse Bash + secret-scrub)`

- **Goal:** block `rm -rf /`, `git push --force` to main, and obvious secret patterns before the agent runs them.
- **Scope:** `bundles/safety-rails.toml` plus `bundles/hooks/validate-bash.sh` and `bundles/hooks/secret-scrub.sh`. Wires up to Claude Code `PreToolUse:Bash`, Codex `PreToolUse` matcher `^Bash$`, Gemini `BeforeTool` matcher `run_shell_command`.
- **Acceptance:** install once, three CLIs honour it; deny rule fires on a known-bad input fixture.
- **Depends on:** PR 7, PR 3, PR 6.

### PR 35 — `feat(bundles): auto-format (PostToolUse on Edit/Write)`

- **Goal:** silently keep the tree green via `prettier`/`ruff`/`gofmt`/`rustfmt`.
- **Scope:** `bundles/auto-format.toml` + helper script that detects the file type and dispatches the right formatter.
- **Acceptance:** edits land formatted across all three CLIs.
- **Depends on:** PR 7.

### PR 36 — `feat(bundles): secret-scan-precommit (gitleaks)`

- **Goal:** local pre-commit gitleaks; CI trufflehog `--only-verified`.
- **Scope:** `bundles/secret-scan.toml` plus a `.lefthook.yml` template engineers can drop into their repos.
- **Acceptance:** installs and activates per-tool; `gitleaks` blocks a fixture with a fake AKIA key.
- **Depends on:** PR 7.

### PR 37 — `feat(bundles): verification-gates (Stop hook)`

- **Goal:** Stop hook running `gitleaks` + modified-only tests + `git status -sb` summary.
- **Scope:** `bundles/verification-gates.toml`.
- **Acceptance:** Stop event triggers the chain across all three CLIs.
- **Depends on:** PR 7.

### PR 38 — `feat(skills): ccusage statusline + cost-budget skill`

- **Goal:** real-time cost visibility via `ryoppippi/ccusage` and a skill that reads its output to enforce token budgets.
- **Scope:** new `ccusage/` entry (skill prompt + statusline config snippet for Claude Code, status-line equivalent docs for Codex/Gemini if available).
- **Acceptance:** linter green; documents the JSONL data sources for all three CLIs.
- **Depends on:** PR 11.

---

## Phase 6 — MCP bundles

> Curated, theme-grouped MCP installs. Each bundle defaults to `--tool all` since MCP is a shared concept.

### PR 39 — `feat(bundles): mcp/docs-stack (context7 + exa + firecrawl)`

- **Goal:** version-pinned library docs + LLM-grade web search + scraping.
- **Scope:** `bundles/mcp-docs.toml`. Pins `@upstash/context7-mcp` to a stable version (per the security audit precedent — no `@latest`).
- **Acceptance:** all three CLIs see the servers post-install.
- **Depends on:** PR 7.

### PR 40 — `feat(bundles): mcp/observability-stack`

- **Goal:** Sentry + (Datadog **or** Honeycomb) + LaunchDarkly Observability.
- **Scope:** `bundles/mcp-observability.toml`. Make Datadog/Honeycomb mutually exclusive via a `[choice]` block.
- **Acceptance:** install + remove are clean; doctor flags missing creds.
- **Depends on:** PR 7, PR 8.

### PR 41 — `feat(bundles): mcp/pm-stack (Linear, Atlassian, Notion)`

- **Goal:** issue tracker + docs MCPs.
- **Scope:** `bundles/mcp-pm.toml`.
- **Acceptance:** install clean.
- **Depends on:** PR 7.

### PR 42 — `feat(bundles): mcp/frontend-stack (Playwright, Chrome DevTools, Figma, Vercel)`

- **Goal:** browser automation + design-token + deploy MCPs.
- **Scope:** `bundles/mcp-frontend.toml`. Pin Playwright MCP version.
- **Acceptance:** install clean.
- **Depends on:** PR 7.

---

## Phase 7 — Marketplace + index expansion

> New top-level library entries that profile community marketplaces an engineer would want to know about.

### PR 43 — `feat(library): wshobson/agents profile`

- **Goal:** library entry for the largest community plugin set.
- **Scope:** new `wshobson-agents/` directory with README + `SKILL_PROMPT.md`. Skill prompt covers headline plugins (full-stack-orchestration, comprehensive-review, conductor, security-scanning, incident-response).
- **Acceptance:** linter green; INDEX.md updated.
- **Depends on:** PR 11.

### PR 44 — `feat(library): obra/superpowers-marketplace profile`

- **Goal:** library entry for the canonical methodology marketplace (already enabled in this repo's Claude Code; profile it for completeness).
- **Scope:** new `superpowers/` directory.
- **Acceptance:** linter green.
- **Depends on:** PR 11.

### PR 45 — `feat(library): VoltAgent/awesome-agent-skills index`

- **Goal:** profile the cross-CLI discovery index.
- **Scope:** new `voltagent-skills/` directory.
- **Acceptance:** linter green.
- **Depends on:** PR 11.

---

## Phase 8 — Polish & rollout

### PR 46 — `feat(library): index pages by audience + stack`

- **Goal:** new `INDEX.md` sections grouping skills by stack (TS/Node, Python, Go, Rust) and by role (frontend, backend, infra, data).
- **Scope:** edit `INDEX.md` only; no new tools.
- **Acceptance:** all 22 + new entries grouped; nothing orphaned.
- **Depends on:** Phases 1–7 substantially complete.

### PR 47 — `docs: getting-started recipe per CLI`

- **Goal:** "from zero to a productive setup in 10 minutes" guide for each of the three CLIs.
- **Scope:** `docs/quickstart-claude.md`, `docs/quickstart-codex.md`, `docs/quickstart-gemini.md`. Each is `ailayer add bundle methodology + safety-rails + mcp-docs` plus a CLI-specific tweak.
- **Acceptance:** following each guide on a fresh machine results in a working setup.
- **Depends on:** Phases 0, 2, 5, 6.

---

## Sequencing rationale

- **Phase 0 first, in order.** PRs 2–6 fix injection — without them, every later PR is questionable. PRs 7–9 unlock bundles, doctor/sync, and tests.
- **Phase 1 next, parallel-safe.** PR 11 ships the schema; 10/12/13 can land in any order after that.
- **Phase 2 has the highest per-PR leverage.** Anyone using these skills sees an immediate quality lift. PR 20 (the methodology bundle) is the single most useful artifact in the whole roadmap.
- **Phases 3–4 parallelize.** Domain and CLI skills are independent; pick whichever the user's current stack needs.
- **Phase 5–6 depend on Phase 0 (PR 7).** Hook bundles + MCP bundles are where ailayer's value compounds — one command, three CLIs.
- **Phase 7–8 are taste-driven.** Add when the core is solid.

## Out of scope

- Anything Cursor-/Aider-/Continue-/Cline-/Windsurf-injected: ailayer targets Claude Code / Codex / Gemini only. Profiling those tools as *library entries* is in scope (Phase 1); writing adapters for them is not.
- Building a new skills marketplace. We integrate with existing ones.
- Hosted / SaaS skill registry. Library is git-tracked Markdown by design.

## Tracking

Each PR title above is the literal commit-message subject. Use `gh pr create --title "feat(ailayer/codex): switch config from YAML to TOML"` etc. so the roadmap and PR list stay searchable in lockstep.
