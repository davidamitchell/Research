# 2026-03-18 — fix-rebase-dirty-tree

## What was done

Fixed `error: cannot pull with rebase: You have unstaged changes` that occurs when the
Copilot session crashes mid-write (e.g. 503 GOAWAY) and leaves uncommitted files on disk.
The session logs show `+0 -0` committed changes but the working tree is dirty.

## Changes

### `.github/workflows/research-loop.yml`

Added a working-tree cleanup inside the **failure branch** of the Copilot invocation:

```bash
if ! git diff --quiet || ! git diff --cached --quiet; then
  echo "::warning::Dirty working tree after failed session. Discarding uncommitted changes."
  git checkout -- .
  git clean -fd
fi
```

Placed after `CONSECUTIVE_FAILURES` increment and before the threshold abort check.
The success path (`then` branch) is entirely untouched.

### `tests/test_research_loop.py`

Added `test_failure_branch_cleans_dirty_working_tree` — asserts:
- Both cleanup commands are present in the workflow.
- Both appear after the failure-branch marker (`CONSECUTIVE_FAILURES` increment).
- Both appear before the threshold abort message.
- Both appear after the success-branch marker (`CONSECUTIVE_FAILURES=0`), confirming they
  are not in the success path.

## Test results

35/36 tests pass. The 1 pre-existing failure (`test_workflow_has_job_timeout`) is
unrelated — the workflow timeout was previously changed from 90 to 150 minutes but the
test still asserts 90.

## Mini-Retro

1. **What went well?** Minimal, surgical change. The test precisely encodes the ordering
   invariant rather than just checking string presence.
2. **What was hard?** Nothing — the problem statement was extremely clear with exact line
   numbers and the required code block.
3. **What would prevent this next time?** This fix is the prevention. The root cause
   (crashed session leaving dirty tree) is now handled cleanly in the loop.
4. **Is this a pattern?** Yes — the "crash leaves dirty tree" class of failure. Now
   documented and mitigated.
