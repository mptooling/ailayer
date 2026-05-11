# Using Git Worktrees — isolated-workspace skill

> **Category:** Methodology | **License:** MIT | **Type:** Cross-CLI agent skill (Claude Code, Codex CLI, Gemini CLI)

A skill that pushes the agent to create a dedicated git worktree before starting feature work, instead of mutating the current checkout. Distilled from `obra/superpowers:using-git-worktrees` and the worktree conventions in `mattpocock/skills:engineering`.

## What it is

A worktree is a second checkout of the same repository, attached to its own branch and its own directory, sharing the underlying `.git`. The agent works in `../<repo>-<feature>/` while the user keeps the main checkout pristine — no half-finished edits, no accidentally-staged migrations, no "wait, what branch am I on?"

The skill is opinionated about three things:

1. **Worktree before code.** Any non-trivial feature gets its own worktree at the start. After the fact is too late — the main checkout already drifted.
2. **One worktree per feature branch.** Worktrees are cheap; reusing one for two unrelated branches defeats the isolation.
3. **Clean up when done.** A merged branch's worktree is dead weight. `git worktree remove` is part of the "finishing a branch" flow, not an afterthought.

## Why it ships in this library

`obra/superpowers:using-git-worktrees` is Claude-Code-only and tied to a specific worktree-helper tool. The mattpocock conventions live inside a larger engineering pack. To get worktree discipline portably across Claude Code, Codex CLI, and Gemini CLI via `ailayer`, the skill needs a self-contained, model-agnostic version that works with plain `git worktree` commands. That's what's in `SKILL_PROMPT.md`.

## What good looks like

A worktree-creation turn looks like this:

```text
$ git worktree add ../myrepo-feat-billing -b feat/billing
Preparing worktree (new branch 'feat/billing')
HEAD is now at 1a2b3c4 …

Switched working directory: ../myrepo-feat-billing
```

A worktree-cleanup turn (after merge):

```text
$ git worktree remove ../myrepo-feat-billing
$ git branch -d feat/billing
```

A non-example: editing five files on `main` directly, then running `git checkout -b feat/billing` after the fact. The branch carries pre-existing uncommitted state and the main checkout is no longer clean.

## Reference

- [`obra/superpowers/using-git-worktrees`](https://github.com/obra/superpowers).
- [`git-worktree(1)`](https://git-scm.com/docs/git-worktree) — official documentation.
- [`mattpocock/skills:engineering`](https://github.com/mattpocock/skills) — worktree-driven feature flow.

## Compose-with

- `writing-plans` (Phase 2) — set up the worktree before executing the plan, so each phase commits from an isolated checkout.
- `executing-plans` (Phase 2) — phase-by-phase execution lives inside the worktree.
- `dispatching-parallel-agents` (Phase 2) — when parallel agents touch the same repo, give each its own worktree to avoid write-write collisions.
- `finishing-a-development-branch` (Phase 2 upcoming) — owns the worktree teardown step.

## Which AI agents integrate

Any agent with shell access. `ailayer add skill using-git-worktrees --tool all` injects it into Claude Code, Codex CLI, and Gemini CLI in one shot.
