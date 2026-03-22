# 2026-03-22 — Research Loop (tracking-work-across-systems)

**Completed:**

Research item:
- `Research/completed/2026-03-15-tracking-work-across-systems.md` — completed; the item concludes that end-to-end work tracing is feasible only as a provenance graph built from multiple local identifiers, web links, and event records rather than from any single cross-system identifier. It finds that issue-to-code-to-build joins are the strongest native links, while document origins, incidents, and data-platform lineage require a mix of explicit metadata, event instrumentation, and confidence-bearing graph edges.

Sources consulted:
- https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github (Azure Boards links work items to GitHub commits, pull requests, branches, and builds)
- https://docs.github.com/en/rest/deployments/deployments (GitHub deployments and deployment-status events for release traceability)
- https://openlineage.io/docs/spec/object-model/ (OpenLineage core entities and event model for data-job provenance)

## Mini-Retro

1. **Did the process work?** Yes. The research loop, self-review, and repository review workflow surfaced distinct quality issues in sequence and produced a materially stronger final item.
2. **What slowed down or went wrong?** The review workflow took time to complete, and several originally listed source links had drifted or changed product positioning, which required replacing or reclassifying evidence during the write-up.
3. **What single change would prevent this next time?** Seed research items with canonical documentation URLs instead of home pages or fragile support links wherever possible.
4. **Is this a pattern?** Yes. It matches the known recurring pattern that source drift and citation-discipline failures are common review blockers for research items.
