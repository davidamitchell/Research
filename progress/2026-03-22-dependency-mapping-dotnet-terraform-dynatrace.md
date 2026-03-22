# 2026-03-22 — Research Loop (dependency-mapping-dotnet-terraform-dynatrace)

**Completed:**

Research item:
- `Research/completed/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.md` — completed; the research concludes that enterprise dependency mapping is best treated as a composite graph problem, combining declared structure from static code and Terraform analysis, observed behavior from runtime telemetry, and ownership/context from Confluence and ServiceNow Configuration and Service Data Model (CSDM). It also found that locally-running agents are most useful as provenance-preserving orchestrators and reconcilers, not as unsupervised generators of dependency truth.

Sources consulted:
- `https://developer.hashicorp.com/terraform/cli/commands/graph` (HashiCorp documentation for Terraform dependency graph generation)
- `https://docs.dynatrace.com/docs/analyze-explore-automate/smartscape/smartscape-views/service-dependency-graph` (Dynatrace service dependency graph documentation)
- `https://www.servicenow.com/community/developer-blog/strengthening-csdm-data-foundations-best-practices-lessons/ba-p/3458446` (ServiceNow practitioner guidance on CSDM data foundations)

## Mini-Retro

1. **Did the process work?** Yes; the research loop, draft transition, review workflow, and completion workflow all worked end-to-end for a single item.
2. **What slowed down or went wrong?** The first review pass surfaced citation-discipline and repetition issues that required a second pass, and the live Tavily integration test was quota-blocked in this environment.
3. **What single change would prevent this next time?** Add a pre-draft local checklist for URL-level citations, label discipline in evidence maps, and non-duplicative Findings prose so the first review pass is more likely to succeed.
4. **Is this a pattern?** Yes; it matches the repository's known recurring pattern that research reviews most often fail on citation discipline and section-by-section repetition rather than on missing raw research.