# 2026-05-06 -- Research Loop (aibom-regulatory-eu-ai-act-intersection)

**Completed:**

Research item:
- `Research/completed/2026-05-06-aibom-regulatory-eu-ai-act-intersection.md` -- completed; the item concludes that the European Union (EU) AI Act, National Institute of Standards and Technology (NIST) Artificial Intelligence Risk Management Framework (AI RMF), Australian Prudential Regulation Authority (APRA) CPS 230, and Basel guidance already create a meaningful compliance case for Artificial Intelligence Bill of Materials (AIBOM) as an inventory and dependency-traceability artifact. It also shows that AIBOM cannot stand alone, because training-data evidence, validation, deployer instructions, post-market monitoring, and resilience governance still need companion artifacts outside the bill of materials itself.

Sources consulted:
- https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-4 (European Union AI Act technical-documentation minimum contents)
- https://doi.org/10.6028/NIST.AI.100-1 (NIST AI RMF inventory and component-risk mapping requirements)
- https://www.apra.gov.au/sites/default/files/2023-07/Prudential%20Standard%20CPS%20230%20Operational%20Risk%20Management.pdf (APRA operational-risk, critical-operations, and service-provider requirements)

## Mini-Retro

1. **Did the process work?** Yes. The review loop surfaced the exact weak points, mainly domain-term first-use handling and confidence overstatement, and the item converged after targeted fixes.
2. **What slowed down or went wrong?** The research review workflow auto-passes on the second cycle even when the log still contains `OVERALL: FAIL`, so the decisive signal remained in the log rather than the run conclusion.
3. **What single change would prevent this next time?** Nothing new; the current prompt already warns to trust the log over the workflow conclusion, and that guidance was sufficient once followed closely.
4. **Is this a pattern?** Yes. It matches the existing repository pattern that research-review logs, not workflow success alone, are the source of truth for failures.
