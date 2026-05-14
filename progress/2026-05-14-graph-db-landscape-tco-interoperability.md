# 2026-05-14 -- Complete research item (graph-db-landscape-tco-interoperability)

**Completed:**
- `Research/completed/2026-05-13-graph-db-landscape-tco-interoperability.md` — completed the graph database landscape comparison and concluded that Stardog is the strongest ontology-first fit, Neo4j AuraDB is the best non-semantic fallback, and Amazon Neptune is the strongest Amazon Web Services (AWS)-native dual-model option.
- `learnings.md` — updated Thread 2 with a data-platform corollary showing that semantic interoperability only wins platform selection when it clears the surrounding transaction-cost hurdle.

## Mini-Retro

1. **Did the process work?** Yes. The draft-review loop surfaced real citation and confidence issues early enough to correct them before final completion.
2. **What slowed down or went wrong?** The review workflow's pass state and the actionable failures in its logs did not always align, and `review_count` needed a second trigger before it wrote back reliably.
3. **What single change would prevent this next time?** Document more explicitly that the review log, not the workflow conclusion alone, is the authoritative signal for research-quality fixes.
4. **Is this a pattern?** Yes. Review-state ambiguity has appeared before in this repository's research loop and should be treated as a recurring workflow-readability issue.
5. **Does any documentation need updating?** Not for the research content itself; the learnings register was updated because this item materially strengthened an existing cross-cutting thread.
6. **Do the default instructions need updating?** Not from the research domain content, but the workflow-observability ambiguity is a candidate for a future instructions or workflow note if it recurs again.
