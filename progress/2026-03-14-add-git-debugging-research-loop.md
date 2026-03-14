# 2026-03-14 — Add Git Debugging to Research Loop

## What was done

Added two git debugging blocks to `.github/workflows/research-loop.yml` to help
diagnose the ghost-dirty-tree problem reported in the issue. The working tree was
appearing dirty to git even though nothing had logically changed, most likely due
to line-ending normalisation (`core.autocrlf`) or file mode changes (`core.fileMode`).

### Changes made

**`.github/workflows/research-loop.yml`**
- Added a pre-rebase debug block before each `git pull --rebase`, logging:
  - `git config core.autocrlf`
  - `git config core.fileMode`
  - `git diff --stat`
  - `git diff`
- Added a post-iteration debug block after each `git push`, logging the same.

**`tests/test_research_loop.py`**
- Added 6 new tests verifying the debug commands are present and correctly
  positioned in the workflow:
  - `test_workflow_logs_git_config_autocrlf_before_rebase`
  - `test_workflow_logs_git_config_filemode_before_rebase`
  - `test_workflow_logs_git_diff_stat_before_rebase`
  - `test_workflow_logs_git_diff_before_rebase`
  - `test_workflow_debug_appears_before_rebase`
  - `test_workflow_debug_appears_after_push`

## Mini-Retro

1. **What went well?** Minimal, surgical change. Tests were straightforward to write
   given existing test patterns. All 35 tests pass; CodeQL clean.

2. **What was tricky?** Initial test for "debug appears after push" used
   string-position heuristic on `core.autocrlf` which failed because the second
   occurrence was not at the expected relative position. Fixed by using a unique
   end-marker string instead.

3. **What single change would prevent this next time?** Use unique marker strings
   in debug blocks so positional tests are unambiguous.

4. **Is this a pattern?** Ghost-dirty-tree is a classic GitHub Actions issue with
   CRLF normalisation. The debug output from the next run should confirm or rule
   out `core.autocrlf` as the cause.
