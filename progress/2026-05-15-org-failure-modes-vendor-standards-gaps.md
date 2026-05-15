# 2026-05-15 -- Research Loop (org-failure-modes-vendor-standards-gaps)

**Completed:**

Research item:
- `Research/completed/2026-05-14-org-failure-modes-vendor-standards-gaps.md` -- completed; the item finds that absent or unenforced vendor implementation standards recur as three main failure families: integration and convergence breakdown, security and exit-control failure, and outsourced technical debt. It also shows that the mitigation pattern is accountable standard ownership plus contractual specificity, continuous monitoring, and lifecycle exit control, not a standards document on its own.

Sources consulted:
- https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-134.html (official Morgan Stanley decommissioning enforcement action)
- https://www.nao.org.uk/reports/government-shared-services/ (National Audit Office evidence on failed standardisation and benefits-convergence in shared services)
- https://www.jmis-web.org/articles/1510 (empirical outsourcing study linking standards violations to technical debt remediation difficulty)

## Mini-Retro

1. **Did the process work?** Yes; the research, self-review, and workflow review loop converged on a defensible completed item.
2. **What slowed down or went wrong?** The review workflow surfaced new violations across successive passes, and its success-path annotations still read like failures without checking the final `review_count` and log details together.
3. **What single change would prevent this next time?** Nothing in `research-prompt.md` needs changing from this slice; the faster win is still to make the review workflow surface one unambiguous final verdict.
4. **Is this a pattern?** Yes; ambiguous review-workflow signaling is already a known recurring pattern in this repo.
5. **Does any documentation need updating?** `learnings.md` needed an update, and Thread 2 now includes the vendor-boundary corollary from this item.
6. **Do the default instructions need updating?** No; the current instructions already forced the right checks, and the remaining friction sits in workflow behavior rather than missing guidance.
