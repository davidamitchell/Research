# 2026-05-09 -- Remove misplaced files from Research/backlog/

**Completed:**
- Deleted 9 files incorrectly placed in `Research/backlog/` by the previous session:
  - `2026-05-09-citation-standards-and-ci-enforcement.md`
  - `2026-05-09-gh-pages-item-metadata-panel.md`
  - `2026-05-09-gh-pages-synthesis-candidates-page.md`
  - `2026-05-09-research-question-skill-evaluation.md`
  - `2026-05-09-research-reviewer-skill-evaluation.md`
  - `2026-05-09-root-cause-repeated-content.md`
  - `2026-05-09-structural-audit-completed-items.md`
  - `2026-05-09-synthesis-peer-review-quality-demonstration.md`
  - `2026-05-09-tag-conformance-zero-promotion-candidates.md`
- These are repo-improvement tasks (W-0060–W-0068) and correctly belong only in `BACKLOG.md`.
- `Research/backlog/` is for research topics to investigate. The `.gitkeep` is preserved.

## Mini-Retro

1. **Did the process work?** No — the previous session confused the two backlogs.
2. **What slowed down or went wrong?** The previous task said "add backlog items" without specifying *which* backlog. The session applied the `research-question` skill process and placed everything in `Research/backlog/` by default, ignoring that the items were clearly repo-improvement work (output: `[tool]`, topics: GH Pages, CI enforcement, corpus audit).
3. **What single change would prevent this next time?** The agent instructions already state this clearly: *"Keep research backlog (`Research/backlog/`) separate from repo improvement backlog (`BACKLOG.md`). One is about *what to research*; the other is about *improvements to this repo's code and structure*."* The previous session failed to apply this rule. No instruction change is needed — the rule exists.
4. **Is this a pattern?** Yes. Any time a task says "add to backlog" without specifying which one, there is a risk of placing repo-improvement items in `Research/backlog/`. The discriminator is simple: if the item's output is `[tool]`, `[agent]`, or `[knowledge]` about the *repo itself* (not about an external research topic), it belongs in `BACKLOG.md`.
