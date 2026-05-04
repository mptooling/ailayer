# GitHub Copilot skill

Use this skill when scripting Copilot CLI calls, configuring Copilot for a repo, or building Copilot Extensions.

## Repo configuration

- Add `.github/copilot-instructions.md` at repo root — Copilot Chat reads it as the system context for every turn in this repo.
- Keep instructions imperative and short: project conventions, build/test commands, and forbidden patterns. Same scope rules as Cursor's `.cursorrules`.
- For per-language rules, also use `.github/instructions/<name>.instructions.md` with frontmatter `applyTo: "**/*.py"` (or other globs). Path-scoped rules load only when relevant files are in context.

## Copilot CLI

- Install: `gh extension install github/gh-copilot`. Requires `gh` authenticated.
- Suggest a command: `gh copilot suggest "convert all png in ./assets to webp"`. Confirm before running — never pipe directly to `bash`.
- Explain a command the user pastes: `gh copilot explain "find . -mtime -1"`. Useful in scripts that surface unfamiliar commands to a user.

## Copilot Extensions

- Build an extension as a GitHub App that handles the `copilot_chat` event. The app receives the user's message + selected file context and responds with markdown.
- Register tools in the extension manifest under `tools: [...]` so Copilot Chat can invoke them. Each tool needs a JSON schema for its parameters — Copilot uses it the same way function-calling does.

## Workspace / Workflows

- For task-from-issue automation, use Copilot Workspace via `gh copilot workspace` (Enterprise only). Treat its PR output like any other AI-generated PR — review every diff before merge.

## Avoid

- Putting secrets or internal URLs in `.github/copilot-instructions.md` — Copilot includes it in prompts that may be logged.
- Using Copilot suggestions verbatim in security-sensitive code (auth, crypto, query construction) without manual review.
- Maintaining duplicate rules in `.cursorrules` and `copilot-instructions.md`; pick one source of truth and symlink or reference.
