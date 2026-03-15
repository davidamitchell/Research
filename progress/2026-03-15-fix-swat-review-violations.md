# Fix SWAT research item review violations

**Date:** 2026-03-15
**File touched:** `Research/completed/2026-03-12-swat-technique-loop-fresh-context.md`

## Task

Fix violations flagged by a research review:
- 6 citation-discipline violations (acronym expansions)
- 4 citation-discipline violations (citations without URLs)
- 3 speculation-control violations ([inference] labels)

## Findings

Carefully reviewed the file against every flagged violation. Most violations were **already addressed** in the file — the review appears to have been conducted against a previous version.

### Genuine violation fixed

**AIES acronym (line 70):** The expansion `AAAI/ACM Conference on AI, Ethics, and Society (AIES)` existed at line 69 but only inside a `[ ]` unchecked (not-accessed) source note. Line 70 — the first active, consulted source entry — used bare `AIES 2025` without expansion. Fixed by expanding at line 70.

### Already addressed (no change made)

| Violation | Status in file |
|---|---|
| CHI expansion | Already expanded at line 71: `ACM Conference on Human Factors in Computing Systems (CHI)` |
| SLA expansion | Already expanded at line 272: `Service Level Agreement (SLA)` |
| NeurIPS expansion | Already expanded at line 362: `Neural Information Processing Systems (NeurIPS)` |
| EMNLP expansion | Already expanded at line 363: `Empirical Methods in Natural Language Processing (EMNLP)` |
| SEO expansion | Already expanded at line 213: `Search Engine Optimization (SEO)` |
| milvus.io URL | Specific full URL present at lines 209, 239, 365, 473 |
| dev.to URL | Specific full URL present at lines 239, 365, 368, 473, 476 |
| letsdatascience.com URL | Specific full URL present at lines 241, 366, 474 |
| minihf.com URL | Specific full URL present at line 386 |
| §5 Behavioural lens [inference] | Already labelled `[inference]` at line 312 |
| §5 Historical lens "Their design" [inference] | Already labelled `[inference]` at line 316 |
| §5 Historical lens LLM optimism bias [inference] | Already labelled `[inference]` at line 316 |

## Change made

```
- [x] SycEval (Fanous et al., AIES 2025) — ...
+ [x] SycEval (Fanous et al., AAAI/ACM Conference on AI, Ethics, and Society (AIES) 2025) — ...
```
