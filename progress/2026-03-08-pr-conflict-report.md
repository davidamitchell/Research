# Session: PR Conflict and Merge Order Report

**Date:** 2026-03-08  
**Branch:** copilot/report-open-prs-status  
**Task:** Report open PRs, files changed, conflict status, and recommended merge order

---

## Open Pull Requests (as of 2026-03-08)

### PR #57 — `copilot/update-research-backlog-cross-reference`

**Title:** research: add Memory-System backlog cross-references to mobile capture research items  
**State:** Open (not draft)  
**Base SHA:** `f412c94` — **this is NOT current `main`** (`eeb69ab`). Branch was created before PR #56 was merged.

**Files changed (relative to base):**
- `Research/backlog/2026-03-08-chatgpt-actions-memory-integration.md` — Added (files without `## Related` section)
- `Research/backlog/2026-03-08-claude-ios-mcp-remote-integration.md` — Added
- `Research/backlog/2026-03-08-inbox-folder-capture-triage-pattern.md` — Added
- `Research/backlog/2026-03-08-ios-shortcuts-github-api-memory-capture.md` — Added
- `Research/backlog/2026-03-08-lancedb-index-rebuild-from-git.md` — Added
- `Research/backlog/2026-03-08-self-hosted-mcp-server-options.md` — Added
- `Research/backlog/2026-03-08-slack-bot-memory-capture-retrieval.md` — Added
- `Research/backlog/2026-03-08-telegram-bot-memory-capture-retrieval.md` — Added
- `progress/2026-03-08-add-memory-system-cross-references.md` — Added

**Conflicts with `main`:** YES — 8 `add/add` conflicts on all 8 backlog files. PR #56 already merged these files to main; PR #57 tries to re-add them with different (older, no `## Related`) content.  
**Additional regressions if force-merged:**
- CHANGELOG.md would lose the "Research backlog items for mobile memory capture" entry
- `progress/2026-03-08-mobile-memory-capture-backlog.md` (added by PR #56) would be **deleted**
- All 8 backlog files would revert to the version without `## Related` sections

**Conflicts with PR #58:** YES — all 8 backlog files overlap.  
**Recommendation:** **Close without merging.** This PR is superseded by PR #58, which correctly builds on current main.

---

### PR #58 — `copilot/update-research-backlog-cross-reference-again`

**Title:** research: add Memory-System backlog cross-references to mobile capture research items  
**State:** Open (draft)  
**Base SHA:** `eeb69ab` — matches current `main`. Clean base.

**Files changed:**
- `Research/backlog/2026-03-08-chatgpt-actions-memory-integration.md` — Modified (+5 lines: `## Related` + source entry)
- `Research/backlog/2026-03-08-claude-ios-mcp-remote-integration.md` — Modified (+5 lines)
- `Research/backlog/2026-03-08-inbox-folder-capture-triage-pattern.md` — Modified (+5 lines)
- `Research/backlog/2026-03-08-ios-shortcuts-github-api-memory-capture.md` — Modified (+5 lines)
- `Research/backlog/2026-03-08-lancedb-index-rebuild-from-git.md` — Modified (+5 lines)
- `Research/backlog/2026-03-08-self-hosted-mcp-server-options.md` — Modified (+5 lines)
- `Research/backlog/2026-03-08-slack-bot-memory-capture-retrieval.md` — Modified (+5 lines)
- `Research/backlog/2026-03-08-telegram-bot-memory-capture-retrieval.md` — Modified (+5 lines)
- `progress/2026-03-08-memory-system-cross-references.md` — Added (session log)

**Conflicts with `main`:** NO — merges cleanly.  
**Conflicts with PR #57:** YES — same 8 backlog files (but only relevant if #57 were merged first, which it should not be).  
**Conflicts with PR #59:** NO — #59 has no file changes.  
**Caveat:** PR description notes W-XXXX numbers were not verified against the actual `davidamitchell/Memory-System/BACKLOG.md` (repo was inaccessible). Owner should verify titles before merging.  
**Recommendation:** **Merge second** (after closing #57). Verify W-XXXX titles first.

---

### PR #59 — `copilot/clean-up-merge-conflicts`

**Title:** [WIP] Clean up merge conflicts and ensure PRs minimize conflicts  
**State:** Open (draft)  
**Base SHA:** `eeb69ab` — matches current `main`.

**Files changed:** **None** — only contains one commit (`Initial plan`) which is an empty planning commit with no file content.

**Conflicts with `main`:** NO — nothing to conflict.  
**Conflicts with any other PR:** NO — no files touched.  
**Recommendation:** **Close without merging.** The task it was meant to address (resolving conflicts on #57) is better resolved by closing #57 and merging #58 instead. This PR made no progress.

---

### PR #60 — `copilot/report-open-prs-status` (this PR)

**Title:** [WIP] Report open PRs and recommended merge order  
**State:** Open (draft)  
**Base SHA:** `eeb69ab` — matches current `main`.

**Files changed:**
- `progress/2026-03-08-pr-conflict-report.md` — Added (this file)

**Conflicts with `main`:** NO  
**Conflicts with other PRs:** NO (unique progress log file; no overlap with PRs #57–#59)  
**Recommendation:** **Merge first** — reporting task only, no content conflicts.

---

## Conflict Matrix

| PR | vs main | vs #57 | vs #58 | vs #59 | vs #60 |
|---|---|---|---|---|---|
| #57 | ❌ 8 conflicts | — | ❌ 8 files overlap | ✅ | ✅ |
| #58 | ✅ clean | ❌ 8 files overlap | — | ✅ | ✅ |
| #59 | ✅ clean | ✅ | ✅ | — | ✅ |
| #60 | ✅ clean | ✅ | ✅ | ✅ | — |

---

## Recommended Merge Order

| Order | PR | Action | Reason |
|---|---|---|---|
| 1 | #60 | Merge | Reporting task only; no conflicts with anything |
| 2 | #57 | **Close** | Stale base; 8 add/add conflicts with main; would regress CHANGELOG and delete a progress log; superseded by #58 |
| 3 | #59 | **Close** | No file changes; task purpose satisfied by closing #57 and merging #58 |
| 4 | #58 | Merge (after verifying W-XXXX titles) | Clean base; adds `## Related` cross-references correctly; no conflicts |

**Rationale:**
- PR #57 was created before PR #56 (the 8 backlog files) was merged, so it tries to re-create files that already exist on main. It cannot be merged without resolving 8 `add/add` conflicts and would introduce regressions.
- PR #58 is the correct retry: it branches from current main, modifies the existing files rather than re-adding them, and merges cleanly.
- PR #59 has no substance and its stated purpose (resolving #57 conflicts) is moot once #57 is closed.
- PR #60 (this one) adds only a session progress log and has no conflicts.
