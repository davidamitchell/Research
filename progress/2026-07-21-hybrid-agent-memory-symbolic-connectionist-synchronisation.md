# 2026-07-21 -- Complete research item (hybrid-agent-memory-symbolic-connectionist-synchronisation)

**Completed:**
- `Research/completed/2026-07-20-hybrid-agent-memory-symbolic-connectionist-synchronisation.md` — researched, drafted, passed `research-review.yml`, and completed the item on how production hybrid agent-memory systems keep a symbolic knowledge graph synchronised with an unstructured Large Language Model (LLM) retrieval layer.
- `learnings.md` — added this item as reinforcing evidence under Thread 26 (engineered detect-then-resolve pipelines substitute for classical truth maintenance), confirming the pattern across three shipping systems (Zep, Mem0, Microsoft GraphRAG).

**Findings summary:**
- The load-bearing synchronisation mechanism is a single non-lossy store with incremental, event-triggered writes and a co-located retrieval index, so one write updates both the symbolic and retrieval views.
- Zep/Graphiti uses a bi-temporal model and invalidates superseded edges rather than deleting them (94.8% Deep Memory Retrieval versus MemGPT 93.4%; up to 18.5% higher LongMemEval accuracy at up to 90% lower latency, all vendor-authored).
- Mem0 uses ADD-only extraction, entity linking, and fused semantic, Best-Matching-25 (BM25), and entity retrieval over one accumulating store; its Mem0g graph variant adds ~2 points over text-only.
- Microsoft GraphRAG synchronises via standard-update and fast-update incremental indexing; full rebuild cost scales with corpus size, so full rebuilds are reserved for schema or model changes.
- No surveyed production system runs a formal Truth Maintenance System (TMS); contradiction handling is a purpose-built detect-then-resolve or recency-priority stage.
- All findings held at medium confidence: primary sources are vendor-authored and the benchmarks (per the prior evaluation-framework item) do not establish a shared industry standard or test provenance and scoping.

**Review outcome:** `research-review.yml` ran three times. Pass 1 flagged unexpanded DRIFT/TMS acronyms, unlabelled §6 Synthesis claims, and a cross-item-integration gap (evaluation-framework not cited). Pass 2 flagged overconfident wording ("cannot drift apart", "is prevented") and two missing authoritative definition links (BM25, Leiden). All were genuinely fixed. The final pass returned OVERALL: PASS (review cap 2/2 reached, with content also clean on merit).

## Mini-Retro

1. **Did the process work?** Yes. The research-loop workflow held end to end: research → draft → review → fix → complete. Each review pass surfaced real, fixable quality issues and the item genuinely improved rather than just aging out via the review cap.

2. **What slowed down or went wrong?** Three review passes were needed because each pass surfaced a fresh class of issue the prior self-review missed: (a) acronyms/labels/cross-item integration, (b) overconfident absolutes, (c) authoritative links for non-self-evident domain terms (BM25, Leiden). Also hit the known `research-review.yml` push-race once (pass-1 `review_count` commit failed to land on the first attempt), so the same pass number repeated before the count stuck.

3. **What single change would prevent this next time?** Add a pre-review self-check for two under-covered classes: (i) authoritative-definition links for named algorithms and ranking functions (not just acronym expansion), and (ii) absolute/settled-outcome verbs ("prevents", "cannot", "ensures", "eliminates") on inference claims. Both are now added to the recurring-patterns awareness below.

4. **Is this a pattern?** Yes, two patterns. First, the review push-race is already documented in the Known Recurring Failure Patterns table and recurred here as expected — verify `review_count` actually landed on main before counting a pass. Second, named-algorithm terms (Leiden, BM25) needing an authoritative definition link is a distinct class from acronym expansion and is worth a standing self-review grep.

5. **Does any documentation need updating?** No ADR — this is a routine research-item completion with no architectural change. `learnings.md` Thread 26 updated. Findings format followed the current rules (per-sentence epistemic labels, no full-sentence bold, no em-dashes).

6. **Do the default instructions need updating?** A light, warranted addition: `research-prompt.md` Step 6 self-review should call out (a) authoritative-definition links for named algorithms/ranking functions and (b) an absolute-verb scan for inference claims. Applied this session (see below).
