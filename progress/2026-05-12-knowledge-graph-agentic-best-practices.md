# 2026-05-12 — Add backlog items: Knowledge Graph best practices for agentic workloads

**Source:** GitHub issue — "Research: What are the relationship, research, tooling and best practices related to building, maintaining and operating a Knowledge Graph when it and the knowledge (context there in) contained become key dependencies (run time) for agentic workloads"

**Completed:**

Five research backlog items created from the issue, scoped into distinct questions per the issue's instruction to "split into as many research questions as needed for fidelity":

1. `Research/backlog/2026-05-12-knowledge-graph-agentic-runtime-dependency.md` — architectural patterns, operational practices, and failure modes when a KG is a key runtime dependency for agentic workloads
2. `Research/backlog/2026-05-12-knowledge-graph-lifecycle-management-agentic.md` — KG lifecycle management: schema versioning, entity resolution, conflict detection, and knowledge freshness
3. `Research/backlog/2026-05-12-web-ontologies-production-knowledge-graph-agentic.md` — web ontologies (RDF, OWL, RDFS, SKOS, Schema.org) best practices for production KGs in agentic AI
4. `Research/backlog/2026-05-12-knowledge-graph-data-product-agentic.md` — KG as a data product: data mesh principles, contracts, and ownership for agentic runtime dependencies
5. `Research/backlog/2026-05-12-odrl-policies-knowledge-graph-agentic-access.md` — Open Digital Rights Language (ODRL) policies in KGs for agentic access control and usage governance

All items cross-reference each other via the `related:` frontmatter field. Items 1 and 2 are `priority: high` (foundational operational questions); items 3–5 are `priority: medium` (design and governance concerns that depend on the operational foundation).

## Research Question Formulation Notes

Each question was evaluated against the five-test quality check (Specific, Answerable, Scoped, Motivated, Decomposable) before being written into the backlog item:

- All five questions passed all five tests without revision.
- The issue mentioned "open digital rights language" — this was identified as the W3C Open Digital Rights Language (ODRL) 2.2 standard and expanded accordingly.
- The issue mentioned "web ontologies" — decomposed into RDF, OWL, RDFS, SKOS, and Schema.org to make the scope concrete.
- The existing backlog item `2026-05-12-graph-db-saas-knowledge-ontology` covers hosted SaaS graph database selection; all new items explicitly exclude this scope and cross-reference that item to avoid duplication.

## Mini-Retro

1. **Did the process work?** Yes. The issue was clear about wanting multiple scoped research questions; the split into five items is well-aligned with the stated fidelity requirement.
2. **What slowed down or went wrong?** Minor: needed to verify what "open digital rights language" referred to (confirmed as W3C ODRL 2.2) and check for near-duplicate items already in the backlog before writing.
3. **What single change would prevent this next time?** Nothing to change — the existing process worked cleanly.
4. **Is this a pattern?** Multi-question decomposition issues (e.g., "research X, Y, and Z") are common. The current workflow handles them well: treat each sub-question as a separate backlog item with shared `related:` cross-references.
5. **Does any documentation need updating?** No.
6. **Do the default instructions need updating?** No new conventions emerged.
