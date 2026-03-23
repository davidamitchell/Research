# 2026-03-23 — Move docs/adr to docs-adr

## Task
Resolve issue: Move `docs/adr` to `docs-adr`, update all documentation and references, and delete `docs/issues`.

## Changes Made

- `git mv docs/adr docs-adr` — renamed directory; all 9 ADR files (README + 0001–0009) preserved
- `git rm -r docs/issues` — deleted `docs/issues/issue-consolidation-2026-03-01.md` and its directory
- Updated `docs/adr` → `docs-adr` references in:
  - `README.md`
  - `BACKLOG.md`
  - `.github/copilot-instructions.md` (repo layout tree, ADR instructions, checklist)
  - `CHANGELOG.md`
  - `PROGRESS.md`
  - `docs-adr/0006-standardise-agent-instructions.md`
  - `Research/completed/2026-02-27-indexing-and-tracking-method.md`
  - `Research/completed/2026-02-27-research-output-types.md`
  - `Research/completed/2026-03-03-research-loop-quality-prompt-engineering.md`
  - `progress/2026-03-11-reviewing-state.md`
  - `progress/2026-03-14-add-git-submodule-skills.md`
  - `progress/archive.md`
- Updated `tests/test_research_loop.py` path assertions from `"docs" / "adr"` to `"docs-adr"`

## Verification

- `test_adr_0004_exists` — PASSED
- `test_adr_0004_indexed` — PASSED
- `grep -rn "docs/adr"` — zero matches remaining
