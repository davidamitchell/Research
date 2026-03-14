# 2026-03-14 — Workflow regression: skills submodule/sync + research loop fix

## Session goal

Investigate and fix the workflow regressions described in issue #134:
1. `research-loop.yml` failing mid-run with `git pull --rebase: unstaged changes`.
2. `research-review.yml` referencing a skills git submodule that no longer exists.
3. Clarify the `create-skills-pr.yml` "failure" pattern.

---

## Investigation findings

### Last known-good run

- **Workflow:** Research Loop
- **Run ID:** `22919944624`
- **Date:** 2026-03-10T19:13:58Z
- **Commit SHA:** pre-`ead44c4b`

### First failing run

- **Workflow:** Research Loop
- **Run ID:** `23071272774`
- **Date:** 2026-03-13T21:29:36Z
- **Commit SHA:** `3c00c98b`
- **Failing step:** `Run research loop`
- **Failure excerpt:**
  ```
  error: cannot pull with rebase: You have unstaged changes.
  error: Please commit or stash them.
  ##[error]git pull --rebase failed — possible conflict or network issue. Stopping loop.
  ```

### Regression window

Commits introduced between last-good and first-failing:
- `ead44c4b` — Merge PR #110 (introduced `create-skills-pr.yml` and submodule constraint note)
- `0f99b653` — Merge PR #117
- `8e6b6acf` — Merge PR #118
- `3c00c98b` — Merge PR #119

PR #110 is the top suspect — it included a large research-superpowers session that left the working tree dirty after the Copilot agent's final write step. Specifically: the agent wrote files (progress notes, research items) that it did not commit before the loop's next iteration tried to `git pull --rebase origin main`.

### Root cause (concrete statement)

**Root cause 1 — Research Loop dirty tree:**
The Copilot agent session writes files (e.g. `Research/in-progress/` updates, `progress/` notes) and then either fails to commit them or leaves partial writes. On the next loop iteration, `git pull --rebase origin main` aborts immediately because git cannot rebase over an unclean working tree. The fix is to run `git reset --hard HEAD && git clean -fd` before each `git pull --rebase` to discard any uncommitted artefacts from the previous iteration.

**Root cause 2 — Research Review submodule step:**
On 2026-03-08, `.github/skills/` was converted from a git submodule to a regular tracked directory (commit `b3a122b` introduced `create-skills-pr.yml`, and `progress/2026-03-08-bbc-skill.md` documents the conversion). The `research-review.yml` workflow still had `git submodule update --init .github/skills`, which no longer matches the repo state. This step was a no-op in practice (git has no submodule entry for that path) but caused confusion and would silently fail if `.gitmodules` were ever cleaned up.

**Root cause 3 — `create-skills-pr.yml` "failure" on push:**
The workflow has `on: workflow_dispatch` as its only trigger. The GitHub Actions check-suite mechanism records a workflow run with `conclusion: failure` and `total_jobs: 0` for every push event — this is a GitHub platform artifact, not an actual job failure. No jobs ran; the workflow was never executed on those push events. The workflow itself is correct; this pattern is expected when a `workflow_dispatch`-only workflow is present in a repo that receives frequent pushes.

### Skills model confirmation

- `.github/skills/` is a **regular tracked directory**, not a git submodule.
- `git ls-files --stage .github/skills` shows `100644` (regular blob) entries, not `160000` (gitlink).
- `.gitmodules` does not exist in the repository.
- `sync-skills.yml` uses clone-and-copy semantics, preserving locally-added skills (`bbc-author` and others not in `davidamitchell/Skills`).
- ADR-0002 has been marked superseded to record this.

---

## Changes made

| File | Change |
|---|---|
| `.github/workflows/research-loop.yml` | Added `git reset --hard HEAD && git clean -fd` before `git pull --rebase` in the iteration loop |
| `.github/workflows/research-review.yml` | Replaced `git submodule update --init .github/skills` with a plain `ls .github/skills/` (verifies skill files are present as regular tracked files) |
| `tests/test_research_review.py` | Replaced `test_workflow_initializes_skills_submodule` with `test_workflow_has_skills_available` — now asserts skills are accessible as regular files and that no submodule call is present |
| `docs/adr/0002-agent-skills-submodule.md` | Marked Status: superseded (2026-03-08), added note explaining the conversion |
| `progress/2026-03-14-workflow-regression-fix.md` | This file |

---

## Mini-retro

**What went well:** The GitHub Actions API gave direct access to log output from failing runs. The concrete error message (`cannot pull with rebase: You have unstaged changes`) made root cause 1 unambiguous. The `progress/2026-03-08-bbc-skill.md` note from the previous session was invaluable for confirming the skills model change.

**What slowed down:** The `create-skills-pr.yml` pattern (failure with 0 jobs on every push) required careful reading of the job-level API response to distinguish "GitHub artifact" from "real failure". A README or comment in the workflow header would have saved time.

**Pattern to watch:** Workflows that call `git pull --rebase` mid-job need defensive cleanup before the pull, not just after. Any agent that writes files must either commit them or have its working tree reset before the next pull.
