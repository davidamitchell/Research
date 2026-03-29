# ADR-0011: Git-Index Staging in CLI File-Move Commands

Date: 2026-03-29
Status: Accepted

## Context

The research loop workflow (`research-loop.yml`) runs the Copilot Command Line Interface
(CLI) in an outer shell loop. After each Copilot session, the loop calls
`git push origin main` to propagate the agent's commits to the remote.

In March 2026, the loop began failing on the second iteration with:

```
error: cannot pull with rebase: You have unstaged changes.
error: Please commit or stash them.
```

Root cause: `cmd_start` and `cmd_complete` in `src/research/cli.py` move files between
Research sub-directories using Python file Input/Output (I/O) primitives
(`Path.unlink()` / `Path.write_text()`). They did not update the git index. When the
Copilot agent subsequently committed with `git add <new-file> && git commit`, only the
newly written file was staged — the deletion of the old file was never staged. The old
file therefore remained in HEAD but was absent from disk: an unstaged deletion.

The loop's existing failure-path cleanup (`git reset --hard HEAD && git clean -fd`)
could not fix this on the **success** path, and would have been wrong to apply: on the
success path, `git reset --hard HEAD` would *restore* the deleted file from HEAD, which
is the opposite of the desired outcome.

The same root cause applied to both transitions:
- `cmd_start`: backlog → in-progress (deletes `Research/backlog/X.md`, writes
  `Research/in-progress/X.md`)
- `cmd_complete`: in-progress → completed (deletes `Research/in-progress/X.md`, writes
  `Research/completed/X.md`)

A secondary consequence was discovered: repeated occurrences of this bug could leave
files "stuck" in `Research/in-progress/` on `main` even after their corresponding
`Research/completed/` entry was committed. The next loop run would pick up the stuck
in-progress item, re-run the Copilot session, and attempt to complete it again.

## Decision

### 1. Stage file moves in the Python CLI commands

Add a `_git_add(repo_root, *paths)` helper to `src/research/cli.py`. The helper calls
`git add -- <paths>` via a subprocess with `check=False` so it is always non-fatal.
Calling `git add` on a deleted tracked file stages the deletion; calling it on a new
untracked file stages the addition. Both are required when moving a file between
directories.

`cmd_start` and `cmd_complete` call `_git_add(root.parent, src, dest)` immediately
after the Python file move. This ensures the git index is consistent with the working
tree before the Copilot agent runs its commit. The agent's `git add <new-file> &&
git commit` then captures both the old-file deletion and new-file addition in a single
commit.

`cmd_draft` does not move files (it updates frontmatter in-place) and is unaffected.

In non-git environments (unit tests without a repository), `git add` fails silently
(`check=False`), preserving backward compatibility with the existing test suite.

### 2. Add orphan cleanup to the research loop

Add a pre-iteration step to `research-loop.yml` that removes any
`Research/in-progress/` files that are also present in `Research/completed/`. These are
orphan files left by the old bug; they cannot be processed further (they are already
completed) and must be removed from git to avoid spurious loop iterations.

The cleanup uses `git rm --force` and creates a single cleanup commit only when orphans
are found. This step runs at the start of each iteration, after `git pull --rebase`, so
it sees the current state of `main` before each Copilot session.

## Rejected Alternatives

### Loop-level cleanup on every success path

An alternative would add `git reset --hard HEAD && git clean -fd` (or equivalent) to
the end of each successful iteration. This was rejected because:
- It would discard legitimate staged changes that the Copilot session intended to
  keep but had not yet committed.
- It does not address the root cause — the deletion is still not staged.
- Fixing it at the source (in the Python commands that do the move) is more
  correct and less surprising.

### `git mv` instead of Python file I/O

`git mv <src> <dest>` both moves the file and stages the move atomically. This would
have eliminated the bug without a separate `_git_add` call. It was not chosen because:
- It changes the interface of `cmd_start` and `cmd_complete` in a way that makes
  non-git use (e.g. unit tests) harder — `git mv` requires the file to already be
  tracked.
- The `_git_add` approach keeps the Python I/O and the git staging as separate,
  individually testable concerns.
- `_git_add` with `check=False` is transparently no-op in non-git environments,
  requiring no test-environment adjustments.

### Stash/pop around the rebase

The failing run's Copilot session attempted `git stash && git pull --rebase` to work
around the problem. This was rejected as a permanent fix because:
- It treats the symptom (dirty tree) rather than the cause (staged deletions missing).
- `git stash` on an unstaged deletion saves the deletion in the stash but does not
  commit it; `git stash pop` after the rebase brings it back, still not staged.
- Stash-based recovery is fragile across complex rebase histories.

## Consequences

### Positive
- `cmd_start` and `cmd_complete` now leave the git index consistent with the working
  tree after every file move, regardless of which files the calling agent chooses to
  commit explicitly.
- Agents can commit with a simple `git add <new-file> && git commit` and trust that
  the deletion of the old file is already staged and will be included.
- Two regression tests (`test_cmd_start_leaves_no_unstaged_changes`,
  `test_cmd_complete_leaves_no_unstaged_changes`) prove the invariant using a real git
  repository, preventing silent regressions.
- The orphan cleanup step in the loop prevents stuck in-progress files from
  accumulating and causing spurious Copilot sessions.

### Negative / Trade-offs
- `subprocess` is now imported in `src/research/cli.py`. This is a standard library
  module with no external dependencies, so the dependency surface does not grow.
- The `_git_add` call adds a subprocess invocation to each file move. On a typical
  Actions runner, this is negligible (< 100 ms).

### Neutral
- The `_git_add` helper is silently non-fatal in non-git environments. All existing
  tests (which use `tmp_path` without a git repository) continue to pass unchanged.
  The two new tests use a `git_research_dir` fixture that initialises a real git repo.
- ADR-0004 (autonomous research loop design) and ADR-0007 (reviewing state) are not
  superseded; this ADR records a bug fix, not a design change.
