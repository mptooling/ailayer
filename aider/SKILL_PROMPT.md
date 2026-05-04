# Aider skill

Use this skill when scripting or invoking Aider to make AI-driven edits inside a git repository.

## Setup

- Install with `pip install aider-chat` (or `pipx install aider-chat` for isolation).
- Run only inside a git repo. Aider creates a commit per change; never run it against uncommitted work you want to keep.
- Pick the model with a flag, not env vars: `aider --model claude-sonnet-4-6` or `--model gpt-4o`. API keys come from `ANTHROPIC_API_KEY` / `OPENAI_API_KEY`.

## Interactive use

- List files Aider should consider: `aider path/to/file1.py path/to/file2.py`. Without explicit files, Aider relies on its repo-map and may miss context.
- `/add` and `/drop` adjust the in-context file set during a session. `/run <cmd>` pipes shell output into the chat.
- `/ask` for read-only questions, `/code` for edits, `/architect` for plan-then-apply on hard refactors.

## Scripted / batch use

- Use `--message "..."` for a single non-interactive turn: `aider --message "extract X to module Y" file.py`.
- Use `--yes --no-stream --message-file changes.txt` in CI. Inspect the resulting commit before pushing.
- For repeated runs over many files, write a shell loop that calls `aider --message ...` per file rather than passing dozens of files in one invocation — context budgets blow up otherwise.

## Repo map and context

- Tune context budget with `--map-tokens 1024` (default ~1024). Raise for monorepos, lower if you hit rate limits.
- Commit `.aider.conf.yml` at repo root for shared model and lint settings; commit `.aiderignore` to exclude vendored or generated trees.

## Avoid

- Letting Aider edit files outside the git working tree — it will refuse, do not chase the error.
- Using `--auto-commit no` for automation; the commit-per-change discipline is the safety net.
- Mixing manual edits and an active Aider session on the same file without `/reset` first.
