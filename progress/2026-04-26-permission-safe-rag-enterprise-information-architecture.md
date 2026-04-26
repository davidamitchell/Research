# 2026-04-26 -- Research Loop (permission-safe-rag-enterprise-information-architecture)

**Completed:**

Research item:
- `Research/completed/2026-04-26-permission-safe-rag-enterprise-information-architecture.md` -- completed; the item concludes that incoherent permissions are a technical blocker for permission-safe Retrieval-Augmented Generation (RAG), not just a governance weakness. It distinguishes live delegated retrieval from copied-index architectures, shows why stale permission propagation is the decisive failure mode in copied corpora, and ties those platform mechanics to published embedding-inversion and retrieval-database membership-inference evidence.

Sources consulted:
- https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/api/ai-services/retrieval/overview (live SharePoint grounding that keeps permissions and governance in place)
- https://learn.microsoft.com/en-us/azure/search/search-indexer-sharepoint-access-control-lists (copied Access Control List ingestion limits and explicit resync requirements)
- https://arxiv.org/abs/2405.20446 (direct evidence that Retrieval-Augmented Generation systems can leak retrieval-database membership)

## Mini-Retro

1. **Did the process work?** Yes. The draft -> review -> fix -> second-pass flow produced a publishable item and caught two precise issues before completion.
2. **What slowed down or went wrong?** Two seeded arXiv identifiers were off-topic for this question, and the first review correctly forced a tighter confidence calibration on the delegated-retrieval claim.
3. **What single change would prevent this next time?** Nothing new beyond the current prompt's existing self-review checklist.
4. **Is this a pattern?** No new pattern. The review findings matched already-known prompt disciplines around source fitness and confidence labeling.
