# Using Git Worktrees — isolated-workspace skill

> **Category:** Methodology | **License:** MIT | **Type:** Workflow skill

A skill that pushes the agent to create a dedicated git worktree before starting feature work, instead of mutating the current checkout. Distilled from `obra/superpowers:using-git-worktrees` and the worktree conventions in `mattpocock/skills:engineering`.

## What it is

A worktree is a second checkout of the same repository, attached to its own branch and its own directory, sharing the underlying `.git`. The agent works in `../<repo>-<feature>/` while the user keeps the main checkout pristine — no half-finished edits, no accidentally-staged migrations, no "wait, what branch am I on?"

The skill is opinionated about three things:

1. **Worktree before code.** Any non-trivial feature gets its own worktree at the start. After the fact is too late — the main checkout already drifted.
2. **One worktree per feature branch.** Worktrees are cheap; reusing one for two unrelated branches defeats the isolation.
3. **Clean up when done.** A merged branch's worktree is dead weight. `git worktree remove` is part of the "finishing a branch" flow, not an afterthought.


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

- `writing-plans` — set up the worktree before executing the plan, so each phase commits from an isolated checkout.
- `executing-plans` — phase-by-phase execution lives inside the worktree.
- `dispatching-parallel-agents` — when parallel agents touch the same repo, give each its own worktree to avoid write-write collisions.
- `finishing-a-development-branch` — owns the worktree teardown step.


---

## When To Use

- If the change is a one-line edit or a docs-only fix, skip the worktree — the overhead exceeds the benefit. For everything else, worktree first.

## How To Apply

- Worktrees are a native git feature (≥ 2.5). No install. Conventions:
- Worktree path: sibling directory named `../<repo>-<slug>` where `<slug>` matches the branch (e.g. branch `feat/billing` → `../myrepo-feat-billing`).
- Branch naming: `feat/...`, `fix/...`, `chore/...`, `refactor/...` — match the repo's existing convention.
- Base branch: usually `main` (or whichever branch the user names).
- Before touching code on a new feature:
- git worktree add ../<repo>-<slug> -b <branch> <base>
- cd ../<repo>-<slug>
- Then do all feature work in the new directory. The main checkout stays at whatever branch the user had — clean, free for unrelated edits, free for the user to keep using.

## Watch Outs

- **Starting feature work in the main checkout, then `git checkout -b` after the fact.** The branch carries whatever uncommitted state was lying around, and the main checkout is no longer clean. Worktree *first*.
- **Reusing one worktree for two unrelated branches.** Defeats the isolation; the next `git stash` accident wipes both. One worktree per active branch.
- **Worktree paths inside the main checkout** (e.g. `./subdir/worktree`). Tools that walk the tree (test runners, linters, build systems) get confused. Use a sibling directory.
- **Forgetting to remove a worktree after merge.** Dead weight accumulates; old worktrees become misleading "live" copies. Removal is part of finishing the branch.
- **`rm -rf <worktree>` to clean up.** Leaves a stale entry in `.git/worktrees/`. Use `git worktree remove` (and `git worktree prune` if the directory is already gone).
- **Worktree-hopping mid-task.** Switching back to the main checkout to "just check one thing" tends to bleed edits across branches. Stay in the worktree until the phase is done; if you must check the main, do it read-only.
