# 2026-05-09 — Add backlog items from quality and site review (add-quality-site-backlog)

**Completed:**

- `BACKLOG.md` — appended W-0060 through W-0068 (9 new items)
- `Research/backlog/2026-05-09-gh-pages-item-metadata-panel.md` — W-0060: render confidence, item_type, cites, related, superseded_by as structured metadata on item pages
- `Research/backlog/2026-05-09-gh-pages-synthesis-candidates-page.md` — W-0061: synthesis candidates page listing tag-cluster groups (≥3 shared tags)
- `Research/backlog/2026-05-09-tag-conformance-zero-promotion-candidates.md` — W-0062: canonicalise full corpus until tag report shows zero promotion candidates
- `Research/backlog/2026-05-09-structural-audit-completed-items.md` — W-0063: systematic audit and correction of all ~287 completed items; corrections recorded with versions: entries
- `Research/backlog/2026-05-09-root-cause-repeated-content.md` — W-0064: root cause investigation of near-identical content across generated pages and completed items
- `Research/backlog/2026-05-09-research-question-skill-evaluation.md` — W-0065: evaluate research-question skill against 10 past backlog items; correct structural weaknesses in davidamitchell/Skills
- `Research/backlog/2026-05-09-research-reviewer-skill-evaluation.md` — W-0066: evaluate research-reviewer skill + research-review.yml against known-good and known-weak items; fix false passes/failures
- `Research/backlog/2026-05-09-citation-standards-and-ci-enforcement.md` — W-0067: create docs/citation-standards.md; CI blocks PRs with uncited factual claims
- `Research/backlog/2026-05-09-synthesis-peer-review-quality-demonstration.md` — W-0068: end-to-end synthesis demonstrating peer-review quality for at least one topic cluster

**Source:** problem statement from session 2026-05-09 (9 improvement items for site, quality, skills, and synthesis pipeline)

---

## Mini-Retro

1. **Did the process work?** Yes. Each problem-statement item was mapped to a W-number, given a scoped research question, and filed both in BACKLOG.md and as a Research/backlog/ Markdown file using the canonical template.

2. **What slowed down or went wrong?** Confirming the last W-number required checking BACKLOG.md carefully — W-0058 is absent (gap between W-0057 and W-0059), so W-0060 was the correct next number. No other blockers.

3. **What single change would prevent this next time?** A helper command (`python -m src.main backlog next-number`) that prints the next available W-number would eliminate the manual grep step.

4. **Is this a pattern?** Yes — every session that appends to BACKLOG.md requires the same grep-and-count step. It is low friction but worth automating if W-number collisions are a recurring concern (W-number collision is already a known recurring pattern in copilot-instructions.md).

5. **Does any documentation need updating?** No — the instructions already document the W-number collision risk and the mitigation (fetch origin main and inspect last number). No new convention emerged.

6. **Do the default instructions need updating?** No new constraint or lesson emerged that is not already captured.
