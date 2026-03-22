# 2026-03-22 — Research Loop (dependency-mapping-dotnet-terraform-dynatrace)

**Completed:**

Research item:
- `Research/completed/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.md` — completed; the item concludes that enterprise dependency mapping works best as a composite graph that merges declared code and Terraform edges, observed runtime telemetry, and curated documentation or registry layers. It also finds that locally-running agents are most useful as provenance-preserving orchestrators and reconcilers rather than as generators of unsourced dependency truth.

Sources consulted:
- https://developer.hashicorp.com/terraform/cli/commands/graph (HashiCorp documentation for Terraform dependency graph generation)
- https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape/smartscape-views/service-dependency-graph (Dynatrace service dependency graph documentation)
- https://www.servicenow.com/community/developer-blog/strengthening-csdm-data-foundations-best-practices-lessons/ba-p/3458446 (ServiceNow practitioner guidance on CSDM data quality and governance)

## Mini-Retro

1. **Did the process work?** Yes. The research loop completed end-to-end, including two review passes and the final move to `completed`.
2. **What slowed down or went wrong?** The selected backlog item duplicated an already-completed item, which forced reuse of vetted content and careful handling of the overwrite-on-complete behavior.
3. **What single change would prevent this next time?** Add a duplicate-slug guard before starting backlog items so the loop skips or flags items that already exist in `Research/completed/`.
4. **Is this a pattern?** It looks like an operational pattern worth guarding against in the workflow; it does not match an existing recurring-pattern note in the current instructions.
