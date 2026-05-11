---
name: using-git-worktrees
description: Isolate feature work in a git worktree before editing — keeps main clean and parallel branches conflict-free.
category: Methodology
triggers: [worktree, git worktree, branch, isolated workspace, parallel branch, feature branch, new feature]
safety: low
version: 2026-05-09
homepage: https://github.com/obra/superpowers
---

# Using-git-worktrees skill

Use this skill **before starting any non-trivial feature, refactor, or experiment** that will outlive the current turn. A worktree is a second checkout of the same repository on its own branch in its own directory; it lets the agent work without mutating the user's main checkout.

If the change is a one-line edit or a docs-only fix, skip the worktree — the overhead exceeds the benefit. For everything else, worktree first.

## Setup

Worktrees are a native git feature (≥ 2.5). No install. Conventions:

- Worktree path: sibling directory named `../<repo>-<slug>` where `<slug>` matches the branch (e.g. branch `feat/billing` → `../myrepo-feat-billing`).
- Branch naming: `feat/...`, `fix/...`, `chore/...`, `refactor/...` — match the repo's existing convention.
- Base branch: usually `main` (or whichever branch the user names).

## Use

Before touching code on a new feature:

```bash
# from the main checkout
git worktree add ../<repo>-<slug> -b <branch> <base>
cd ../<repo>-<slug>
```

Then do all feature work in the new directory. The main checkout stays at whatever branch the user had — clean, free for unrelated edits, free for the user to keep using.

When the branch is merged (or abandoned):

```bash
git worktree remove ../<repo>-<slug>
git branch -d <branch>            # or -D if abandoned + not merged
```

For parallel feature work — two independent features at once — create two worktrees. They share the underlying `.git` so disk cost is low; the win is that neither branch sees the other's uncommitted state.

When `git worktree add` errors with `already checked out`, the branch is live in another worktree. List them with `git worktree list` and either reuse the existing worktree or pick a different branch name.

## Avoid

- **Starting feature work in the main checkout, then `git checkout -b` after the fact.** The branch carries whatever uncommitted state was lying around, and the main checkout is no longer clean. Worktree *first*.
- **Reusing one worktree for two unrelated branches.** Defeats the isolation; the next `git stash` accident wipes both. One worktree per active branch.
- **Worktree paths inside the main checkout** (e.g. `./subdir/worktree`). Tools that walk the tree (test runners, linters, build systems) get confused. Use a sibling directory.
- **Forgetting to remove a worktree after merge.** Dead weight accumulates; old worktrees become misleading "live" copies. Removal is part of finishing the branch.
- **`rm -rf <worktree>` to clean up.** Leaves a stale entry in `.git/worktrees/`. Use `git worktree remove` (and `git worktree prune` if the directory is already gone).
- **Worktree-hopping mid-task.** Switching back to the main checkout to "just check one thing" tends to bleed edits across branches. Stay in the worktree until the phase is done; if you must check the main, do it read-only.

## Verify

A worktree-driven flow is well-formed if:

- The feature branch was created via `git worktree add -b`, not via in-place `git checkout -b`.
- The agent's working directory for the rest of the feature is the worktree, not the main checkout.
- `git worktree list` after merge no longer shows the feature worktree (cleanup ran).
- Two parallel features → two distinct worktrees, never one shared directory.

If the agent ends up editing the main checkout for feature work, the discipline broke. Stop, stash, set up the worktree, replay the edits there.
