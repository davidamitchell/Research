# 2026-03-16 — Research Loop (latent-concept-extraction-confluence)

**Completed:**

Research item:
- `Research/completed/2026-03-15-latent-concept-extraction-confluence.md` — completed; BERTopic combined with mREBEL NER (run in parallel) is the recommended dual-extraction architecture for Confluence wikis, with HybridRAG (VDB + KG) outperforming each retrieval approach individually. Knowledge corpus governance—operationalised as four per-chunk metadata fields (provenance, approval status, recency signal, superseded-by KG edge)—is the primary RAG quality determinant, confirmed across three independent research items.

Sources consulted:
- https://arxiv.org/abs/2203.05794 (BERTopic paper — Maarten Grootendorst, the authoritative BERTopic reference)
- https://arxiv.org/abs/2408.04948 (HybridRAG paper — VDB + KG outperforms each individually on information retrieval benchmarks)
- https://huggingface.co/spaces/mteb/leaderboard (MTEB Leaderboard — standard for embedding model selection; `all-mpnet-base-v2` strong general baseline)

## Mini-Retro

1. **Did the process work?** Yes. The structured research skill (§§0–7) produced a well-evidenced item with 12 key findings and a 19-row evidence map. The review workflow passed on first submission, suggesting the acronym audit and sense check were effective.
2. **What slowed down or went wrong?** Context compaction occurred mid-review-watch, requiring the agent to resume from a summary. No data was lost, but the continuity break added a recovery step. Two acronym issues (KG and RAPTOR) were caught during the pre-draft audit and fixed before committing — the checklist worked as designed.
3. **What single change would prevent this next time?** Nothing structural to change; context compaction is a runtime constraint, not a process failure. The acronym audit checklist correctly caught the issues before they reached review.
4. **Is this a pattern?** Context compaction during long research sessions is a recurring pattern (matches the known "long-running session" pattern in this repository). The mitigation is already in place: the session summary enables clean resume. No new pattern to document.
