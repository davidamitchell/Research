# 2026-05-12 — Add backlog item: RAG document drift and agent behavioral regression

**Source:** GitHub issue — "Follow up research" — the prior completed item `2026-05-12-knowledge-graph-agentic-runtime-dependency` focused on Knowledge Graph serving architecture and failure modes, but missed the owner's actual focus: what happens when the documents agents depend on via Retrieval-Augmented Generation (RAG) change after the agent was built and tested.

**Completed:**

- `Research/backlog/2026-05-12-rag-document-drift-agent-behavior.md` — added from issue; validated research question: *When the source documents indexed in a RAG pipeline change after an agent has been built and tested, what failure modes and behavioral regressions can result in production, and what strategies — covering document versioning, behavioral baseline testing, and deployment governance — exist to detect, measure, and mitigate these regressions?*

**Research-question skill output:**

*Candidate topic:* Agents are built and tested against a specific document corpus; those documents (via RAG) inject content into the context window that drives behavior. What happens when those documents change post-deployment?

*Five-test evaluation:*
- Specific: ✓ — names subject (RAG source documents), evaluation focus (failure modes / regression strategies), and context (post-build document changes)
- Answerable: ✓ — resolvable via published RAG evaluation literature, incident reports, and tooling documentation
- Scoped: ✓ — explicit in/out-of-scope boundaries added; excludes KG architecture (already covered), model weight changes, and RAG architecture selection
- Motivated: ✓ — informs how teams should design, test, and operate agents where document-corpus drift is a known operational risk
- Decomposable: ✓ — five sub-question clusters, each with atomic leaves

*Readiness verdict:* **READY**

*Approach decomposition:*
1. Characterise the propagation mechanism: how does a document change reach the context window?
2. Survey documented failure modes and real-world incidents of document-drift-induced behavioral regressions
3. Evaluate testing/evaluation frameworks (Ragas, TruLens, LangSmith) for corpus-version-aware baseline support
4. Identify mitigation and governance patterns for managing document corpora as versioned dependencies
5. Synthesise lessons from adjacent completed items (KG runtime-dependency, AIBOM runtime-divergence)

## Mini-Retro

1. **Did the process work?** Yes — the issue statement was clear enough to extract all three interaction-protocol answers directly. The research-question skill ran cleanly to a READY verdict.

2. **What slowed down or went wrong?** Nothing material. The prior item's scope (`2026-05-12-knowledge-graph-agentic-runtime-dependency`) was close enough to require careful out-of-scope bounding to avoid duplication, but that was straightforward once the distinction was clear: the prior item covers the KG serving layer; this item covers the document-corpus-as-dependency problem at the retrieval/context-injection level.

3. **What single change would prevent this next time?** Nothing — the research-question skill applied cleanly. The issue statement was specific enough.

4. **Is this a pattern?** The prior item "missed the mark" because its scope was narrowed to Knowledge Graphs specifically. The owner's actual concern is broader and applies to any retrieval-based context injection. This is not a process failure — it was a natural scope refinement as the owner read the completed output. Normal iteration.

5. **Does any documentation need updating?** No.

6. **Do the default instructions need updating?** No.
