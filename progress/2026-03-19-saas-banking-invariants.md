# 2026-03-19 — Research Loop (saas-banking-invariants)

**Completed:**

Research item:
- `Research/completed/2026-03-15-saas-banking-invariants.md` — completed; the research found that the real invariants in enterprise banking Software as a Service (SaaS) platforms are vendor-maintained domain models, workflow scaffolding, integration surfaces, and shared operating infrastructure, not turnkey bank-specific outcomes. It also found that Artificial Intelligence (AI)-assisted development narrows the economics gap for bespoke differentiation layers, but migration, integration, governance, training, and assurance costs remain, so the build-versus-buy threshold shifts toward layered architectures rather than reversing outright.

Sources consulted:
- https://www.salesforce.com/products/financial-services-cloud/overview/ (official Salesforce Financial Services Cloud product overview)
- https://www.ncino.com/implementation (official nCino implementation lifecycle and customer-responsibility detail)
- https://github.blog/news-insights/research/the-economic-impact-of-the-ai-powered-developer-lifecycle-and-lessons-from-github-copilot/ (GitHub research on the economic impact of AI-powered software development)

## Mini-Retro

1. **Did the process work?** Yes. The research loop, draft workflow, review-count state machine, and completion command all worked end to end.
2. **What slowed down or went wrong?** The first review pass exposed stricter citation and epistemic-label expectations than the prompt alone made obvious, and the second review run was slow enough to require repeated polling before the repository state updated.
3. **What single change would prevent this next time?** Add a repository-local preflight check for research items that specifically audits sentence-level source URLs and epistemic labels in `## Findings` and high-risk prose sections like `## Context`.
4. **Is this a pattern?** Yes. It matches the existing recurring pattern that acronym expansion and citation discipline are the most common review failure modes; this item showed that sentence-level source binding in summary sections belongs in the same class.
