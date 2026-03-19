# 2026-03-19 — Research Loop (adaptive-policy-authorization-compliance)

**Completed:**

Research item:
- `Research/completed/2026-03-16-adaptive-policy-authorization-compliance.md` — completed; the item concludes that Adaptive Policy-Based Authorization aligns directly with the dynamic and attribute-based access-control language in NIST SP 800-53 and materially supports ISO/IEC 27001 access-management controls, but only becomes compliance evidence when it is paired with validation, logging, review, and identity-lifecycle governance. It also finds that current policy engines already provide most of the required technical primitives, while AI-assisted authorization authoring remains a high-risk workflow unless changes pass through human review, automated policy tests, schema validation, and durable audit trails.

Sources consulted:
- https://csrc.nist.gov/publications/detail/sp/800-162/final (NIST definition of Attribute-Based Access Control)
- https://csf.tools/reference/nist-sp-800-53/r5/ac/ac-3/ (NIST SP 800-53 access-enforcement and attribute-based access-control mapping)
- https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/monitoring-cloudtrail.html (Amazon Verified Permissions audit logging and authorization event evidence)

## Mini-Retro

1. **Did the process work?** Yes. The research loop selected the oldest high-priority backlog item, moved it through draft and review, and produced a completed item plus the required session log.
2. **What slowed down or went wrong?** The review workflow surfaced citation-discipline issues that were subtle rather than substantive: sentence-level sourcing in `## Findings`, a title/first-use acronym edge case, and a few unlabeled evaluative conclusions. The workflow's `Run quality review` step also takes several minutes, so each review loop had non-trivial waiting time.
3. **What single change would prevent this next time?** Add a local preflight script that checks `## Findings` for sentence-level labels and explicit URLs before the first draft commit.
4. **Is this a pattern?** Yes. It matches the known recurring review pattern around acronym expansion and citation discipline in research items, and it reinforces that `## Findings` needs the same epistemic rigor as `## Research Skill Output`.
