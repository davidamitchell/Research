# 2026-05-16 -- Research Loop (uelgf-live-queryable-knowledge-graph)

**Completed:**

Research item:
- `Research/completed/2026-05-15-uelgf-live-queryable-knowledge-graph.md` -- completed; the item concludes that UELGF should use a hybrid architecture with RDF 1.1 plus a bounded OWL 2 profile as the canonical semantic layer, SHACL for deterministic validation, and an LPG projection for traversal and analytics. It also fixes the confidence-handling question by keeping extraction confidence in provenance-bearing annotations rather than in normative policy truth conditions, and it defines an ingestion model that separates source documents, extracted candidate assertions, and promoted canonical assertions.

Sources consulted:
- https://www.w3.org/TR/rdf11-concepts/ (RDF 1.1 graph and dataset model)
- https://www.w3.org/TR/shacl/ (closed-world validation model for RDF graphs)
- https://www.w3.org/TR/prov-o/ (provenance model for assertions, revisions, and promotion lineage)

## Mini-Retro

1. **Did the process work?** Yes. The review workflow caught real issues, and the item ended in a clean reviewed state after tightening acronym expansion and access-note handling.
2. **What slowed down or went wrong?** The review rules around visible access notes and recursive-review metadata were stricter than the first draft assumed, so the item needed two small review-fix loops.
3. **What single change would prevent this next time?** Nothing new; the existing prompt already warns about acronym expansion and access-note treatment, and this session just needed to follow those rules more literally.
4. **Is this a pattern?** Yes. It matches the repository's known pattern that citation-discipline and acronym/access-note issues are the most common review failures.
