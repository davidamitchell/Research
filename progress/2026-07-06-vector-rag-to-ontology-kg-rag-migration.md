# 2026-07-06 -- Complete research item: vector-rag-to-ontology-kg-rag-migration

**Completed:**
- `Research/completed/2026-07-05-vector-rag-to-ontology-kg-rag-migration.md` -- full research-loop cycle (start, research, draft, two review passes, complete) on migration trade-offs from vector Retrieval-Augmented Generation (RAG) to ontology-backed Knowledge Graph RAG (KG-RAG).
- Consulted 21 sources across 5 arXiv papers seeded in the item plus 6 additional papers/benchmarks/vendor docs discovered during investigation, and cross-referenced 7 related completed items in `Research/completed/`.
- Key conclusion: KG-RAG migration is justified as an additive hybrid (keep the vector index, add a graph store alongside it) specifically in relationship-dense domains with cross-referencing query patterns (LinkedIn, HybridRAG production/benchmark evidence), not as a universal upgrade (GraphRAG-Bench reports GraphRAG frequently underperforming vanilla RAG outside that condition).
- Updated `learnings.md` Thread 22 (ontology/LLM world-model) with this item's boundary-condition evidence, since it sharpens an existing claim rather than establishing a new cross-cutting theme.

## Review cycle summary

Both automated `research-review.yml` passes returned `OVERALL: FAIL`:

- **Pass 1** flagged: "Leiden algorithm" used without an authoritative source; 24 em-dashes across the item (including in the Sources/Related bullet lists, despite this being the pre-existing repo template convention); all 12 Key Findings using prohibited full-sentence bold; 4 Key Findings (1, 3, 5, 6) assigned "high confidence" while citing only a single source.
- **Pass 2** (after fixing pass-1 issues) flagged: an unlabeled comparative judgment ("weakest-evidenced claim") in Risks/Gaps; systematic mid-sentence bold used for emphasis in the (reformatted) Key Findings and an "Assumption:/Justification:" inline-header bold pattern in Assumptions; Key Finding 2's "high confidence" resting on two sources that both originate from the same Microsoft GraphRAG project, failing the multi-independent-source bar.

Since `review_count` reached the workflow's `max_reviews` (2) after pass 2, no further automated issue was raised. I manually fixed every violation from the pass-2 report before completing the item, rather than treating the review-count ceiling as permission to skip remaining fixes.

## Mini-Retro

1. **Did the process work?** Yes, overall. The research skill's §0-§7 structure produced a well-evidenced, appropriately scoped item, and the prior-work cross-reference and companion-skill checks (citation-discipline, remove-ai-slop, speculation-control, peer-reviewer) caught real quality gaps rather than trivial ones.
2. **What slowed down or went wrong?** Two rounds of self-review before drafting still missed issues the automated reviewer caught: full-sentence bold in Key Findings (my "fix" for pass 1 replaced full-sentence bold with mid-sentence emphasis bold, which pass 2 also flagged, since the rule is "no bold except for a defined term/UI label/identifier", not "shorten the bolded span"), an unlabeled evaluative closing sentence in Risks/Gaps, and a same-project non-independence check on paired citations. Each of these is a specific sub-rule this session under-weighted relative to the broader acronym/citation checks it ran carefully.
3. **What single change would prevent this next time?** Before drafting, run three targeted greps that this session only ran reactively after review failure: (a) `grep -n "^[0-9]\+\. \*\*"` to catch any bold anywhere in a numbered Key Finding, not just full-sentence bold, since the remove-ai-slop rule prohibits bolding statistics or phrases for emphasis, not just entire sentences; (b) `grep -inE "strongest|weakest|most concrete|best evidence"` across Findings to catch unlabeled comparative/evaluative judgments before submission; (c) for every multi-source citation in a "high confidence" claim, explicitly check whether the sources are from the same organisation/project before assigning High.
4. **Is this a pattern?** Partially. The repo's Known Recurring Failure Patterns table already documents several evaluative-language and confidence-calibration patterns; this session's failures (mid-sentence emphasis bold, same-organisation non-independence for High confidence) are close variants of documented patterns but specific enough to warrant their own table rows, added below.
5. **Does any documentation need updating?** Yes -- see the two new table rows added to `.github/copilot-instructions.md` Known Recurring Failure Patterns.
6. **Do the default instructions need updating?** Yes, done in this session (see below).

## Instruction updates applied

Added two rows to the Known Recurring Failure Patterns table in `.github/copilot-instructions.md`:
- Mid-sentence emphasis bold in Key Findings (bolding a statistic or short phrase for emphasis, distinct from full-sentence bold, still violates the Boldface rule).
- High-confidence Key Findings whose multiple cited sources originate from the same organisation or project (not independent enough to clear the multi-independent-source bar for High confidence).
