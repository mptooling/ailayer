# Windsurf skill

Use this skill when configuring a repo for Windsurf users or driving Windsurf's Cascade agent from automation.

## Project rules

- Windsurf reads `.windsurf/rules/*.md` (multi-file, scoped) and the legacy `.windsurfrules` (single file). Prefer the multi-file form.
- Each rule file can declare `globs:` and `description:` in YAML frontmatter, identical in spirit to Cursor's `.cursor/rules/*.mdc`.
- Many teams symlink `.windsurf/rules` to `.cursor/rules` to keep one source of truth — only do this if both editors will respect the same rule format on your version.

## Cascade agent patterns

- Cascade is multi-step: it plans, edits, runs commands, reads output, iterates. Write rules that constrain *which commands it may run* — e.g. "Only run `pytest -x -q`. Never run `rm -rf` or modify `.env`."
- Cascade respects a `terminal allow-list` configured in Windsurf settings. For shared repos, document the allowed commands in the rules file so the agent doesn't propose disallowed ones.
- For multi-file refactors, prefer Cascade Write mode over inline edit — it batches edits and presents a single review diff.

## Enterprise / API

- The Cascade API is Enterprise-only. Endpoint and auth come from your enterprise admin; expect Bearer-token auth and a `POST /v1/cascade/run` shape with `{prompt, repo_root, max_steps}`.
- For self-hosted Windsurf, model providers and quotas are configured server-side; client code only needs the token.

## Avoid

- Encoding security policy in rules alone — Cascade is permissive by default. Combine rules with terminal-allow-listing and CI-side guards.
- Letting Cascade run unattended without `max_steps`; it will keep iterating on flaky tests until it hits the model rate limit.
- Maintaining `.windsurfrules` and `.cursor/rules/*.mdc` independently — drift causes confusing differences in agent behaviour across editors.
