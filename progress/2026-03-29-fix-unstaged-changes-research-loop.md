# 2026-03-29 -- Fix: unstaged changes bug in research loop (run 23697727543)

**Session type:** Bug fix

## Root cause

CI run 23697727543 / job 69035750403 failed at step 8 ("Run research loop") with:

```
error: cannot pull with rebase: You have unstaged changes.
error: Please commit or stash them.
```

The failure occurred at the start of **iteration 2**, immediately before `git pull
--rebase origin main`. Tracing through the iteration-1 logs revealed the exact
sequence:

1. The outer bash loop called `python -m src.main research start
   2026-03-28-agent-instruction-loading-and-skills-access.md`, which:
   - Deleted `Research/backlog/<item>.md` from disk (`Path.unlink()`)
   - Wrote `Research/in-progress/<item>.md` to disk (`Path.write_text()`)
   - **Did not update the git index at all.**

2. The Copilot agent ran, completed the research, then called
   `python -m src.main research complete <item>`, which:
   - Wrote `Research/completed/<item>.md` to disk
   - Deleted `Research/in-progress/<item>.md` from disk (`Path.unlink()`)
   - **Did not update the git index at all.**

3. The agent's final commit explicitly named only the files to stage:
   `git add Research/completed/<item>.md learnings.md progress/<item>.md`
   The deletion of `Research/in-progress/<item>.md` was **never staged**.

4. After `git push origin main`, the committed HEAD still tracked
   `Research/in-progress/<item>.md`, but the file no longer existed on disk —
   an unstaged deletion in the working tree.

5. Iteration 2's `git pull --rebase origin main` refused to run because of that
   dirty state.

**Why the existing failure-path cleanup didn't help:** The loop already has
`git reset --hard HEAD && git clean -fd` on the *failure* path. But:
- The Copilot session exited with code 0 (success), so the success path ran.
- `git reset --hard HEAD` on the success path would have *restored* the deleted
  in-progress file (it was still in HEAD), which would be incorrect.

The fix therefore belongs in the root cause, not in the loop's cleanup logic.

## Fix

Updated `src/research/cli.py`:

- Added `_git_add(repo_root, *paths)` helper: calls `git add -- <paths>` with
  `check=False` so it is always non-fatal. On a deleted tracked file, `git add`
  stages the deletion; on a new file, it stages the addition.
- `cmd_start`: calls `_git_add(root.parent, src, dest)` after the Python file
  move, staging both the backlog-file deletion and the in-progress-file addition.
- `cmd_complete`: calls `_git_add(root.parent, src, dest)` after the Python file
  move, staging both the in-progress-file deletion and the completed-file
  addition.

In non-git environments (local tests without a repo) `git add` fails silently
(the subprocess call uses `check=False`), so existing non-git tests are
unaffected.

## Tests

Added two new tests to `tests/test_research_cli.py`:

- `test_cmd_start_leaves_no_unstaged_changes` — initialises a real git repo,
  commits the backlog item, calls `cmd_start`, asserts `git diff --stat` is
  empty.
- `test_cmd_complete_leaves_no_unstaged_changes` — same setup but with
  `cmd_complete`.

Both tests **failed** before the fix and **pass** after.

## Verification

- `make check` (ruff lint + format): all checks passed.
- `python -m pytest tests/ -q`: 192 passed, 1 skipped, 1 pre-existing failure
  (`test_tavily_api_key_is_configured` — no `TAVILY_API_KEY` env var in sandbox).

## Mini-Retro

1. **Did the process work?** Yes. Reading the CI logs showed the exact dirty
   file; comparing the final commit's file list against the cmd_complete
   implementation confirmed the missing `git rm`.
2. **What slowed things down?** Initially had to dig through 1 355 lines of CI
   log to find the right debug block. The pre-existing debug output (core.autocrlf,
   git diff --stat before each rebase) was key to identifying the exact file.
3. **Single change that would prevent this next time?** The fix itself is that
   change — `cmd_start` and `cmd_complete` now stage their own file moves, so
   agents cannot accidentally omit the deletion from their commits.
4. **Is this a pattern?** Yes. Every file-move command that uses Python file I/O
   without git operations is a latent instance of this bug. `cmd_draft` does not
   move files (status-only update), so it is not affected. No other CLI commands
   move files.
