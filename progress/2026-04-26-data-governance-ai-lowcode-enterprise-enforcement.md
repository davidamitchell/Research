# 2026-04-26 -- Research Loop (data-governance-ai-lowcode-enterprise-enforcement)

**Completed:**

Research item:
- `Research/completed/2026-04-26-data-governance-ai-lowcode-enterprise-enforcement.md` -- completed; the item concludes that enterprise data governance only becomes enforceable in Artificial Intelligence (AI) and low-code systems when catalog metadata is bound to runtime controls such as authorization, retrieval filtering, connector restriction, and output checks. It shows Microsoft documents a relatively native metadata-to-control chain, while Amazon Web Services (AWS) reaches similar outcomes through a composed pattern across Glue, Lake Formation, and Identity and Access Management (IAM), and it argues that sensitive data needs live checks plus bounded copying rather than catalog-only governance.

Sources consulted:
- https://learn.microsoft.com/en-us/purview/developer/secure-ai-with-purview (Microsoft Purview runtime governance and oversharing controls)
- https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention (Power Platform Data Loss Prevention (DLP) connector and runtime enforcement behavior)
- https://docs.aws.amazon.com/glue/latest/dg/security-lf-enable.html (AWS Glue and Lake Formation enforcement pattern)

## Mini-Retro

1. **Did the process work?** Yes, the research loop produced a usable item, the automated review exposed a few over-strong comparative claims, and the second pass plus final cleanup left the completed item in a materially better state.
2. **What slowed down or went wrong?** The missing `.github/skills/research/SKILL.md` fallback and the need to satisfy the review workflow's whole-document acronym and terminology checks added extra iteration, especially in the title and scope rather than only in Findings.
3. **What single change would prevent this next time?** Nothing new, the existing checklist already covers this if it is applied literally to the whole document, including the title, Research Question, and Scope before the first draft commit.
4. **Is this a pattern?** Yes, it matches the repository's known acronym-expansion and review-discipline pattern rather than revealing a new failure class.
