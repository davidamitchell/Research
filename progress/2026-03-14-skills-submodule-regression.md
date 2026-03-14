# 2026-03-14 — Skills submodule regression: issue creation and backlog intake

## Session goal

Investigate the recently introduced regression around skills syncing and submodule consistency causing research-loop and research-review workflow failures. Capture findings as a GitHub issue and backlog item.

## What happened

- Reviewed the failing Research Loop run [`23071272774`](https://github.com/davidamitchell/Research/actions/runs/23071272774/job/67022059312) — confirmed failure: `error: cannot pull with rebase: You have unstaged changes.`
- Scanned recent workflow history to establish the regression window:
  - Last known-good Research Loop: `22919944624` (2026-03-10T19:13:58Z) ✅
  - First failing Research Loop: `22941932204` (2026-03-11T07:38:38Z) ❌
  - Research Review has been failing consistently since at least 2026-03-10.
- Read and compared all three relevant workflow files:
  - `sync-skills.yml` — clone+copy pattern (no submodule operations)
  - `research-review.yml` — `git submodule update --init .github/skills`
  - `research-loop.yml` — `submodules: false` + bare `git pull --rebase origin main`
- Identified the core inconsistency: three workflows make contradictory assumptions about whether `.github/skills` is a git submodule or a plain tracked directory.
- Created [issue #134](https://github.com/davidamitchell/Research/issues/134) assigned to @davidamitchell with full analysis, open questions, investigation checklist, and acceptance criteria.
- Added W-0035 to BACKLOG.md to track the remediation work.

## Mini-retro

**What went well:** All relevant workflow logs and run history were accessible via GitHub Actions API. The inconsistency between the three workflows was clear and concrete — no guessing required once the files were read directly.

**What was harder than expected:** The regression window required scanning five pages of workflow run history to find the last-good loop run. A dedicated status page or per-workflow run history view would have sped this up.

**What to watch:** The `create-skills-pr.yml` workflow is also failing on every push — this may be a separate issue or a symptom of the same root cause. It should be investigated as part of W-0035.

## Files changed

- `BACKLOG.md` — added W-0035
- `progress/2026-03-14-skills-submodule-regression.md` — this file

## GitHub artefacts created

- [Issue #134](https://github.com/davidamitchell/Research/issues/134) — Regression: skills submodule/sync inconsistency causing research-loop and research-review failures (assigned to @davidamitchell)
