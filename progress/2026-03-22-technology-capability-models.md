# 2026-03-22 — Research Loop (technology-capability-models)

**Completed:**

Research item:
- `Research/completed/2026-03-21-technology-capability-models.md` — completed; the research found that no single surveyed public framework provides an enterprise-wide technical capability taxonomy, maturity model, and operational traceability layer at once. The strongest answer is a layered stack: a TOGAF-style backbone for implementation-agnostic capability structure, IT Capability Maturity Framework (IT-CMF) for maturity assessment, and ServiceNow Common Service Data Model (CSDM) for operational traceability, with domain, security, and engineering frameworks used as overlays.

Sources consulted:
- https://www.opengroup.org/togaf (The Open Group TOGAF framework and reference-model material)
- https://ivi.ie/it-capability-maturity-framework/ (Innovation Value Institute overview of IT-CMF capabilities, assessments, and roadmaps)
- https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-csdm-data-modelling.md (prior repository work establishing CSDM as a traceability model rather than a taxonomy)

## Mini-Retro

1. **Did the process work?** Yes. The research-loop sequence worked end-to-end, and the review workflow surfaced real claim-classification issues that were worth fixing rather than just formatting noise.
2. **What slowed down or went wrong?** The main slowdowns were partially inaccessible official framework pages and the first review pass, which caught comparative judgments that needed to be labeled as inferences instead of facts.
3. **What single change would prevent this next time?** A pre-review check that searches specifically for comparative words such as "best," "strongest," and "most defensible" in `[fact]` claims would have prevented the first-pass review failures.
4. **Is this a pattern?** Yes. It matches the repository's known review pattern that comparative or recommendation-shaped claims must be clearly marked as `[inference]` and supported with explicit source discipline.
