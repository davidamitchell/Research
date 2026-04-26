# 2026-04-26 -- Research Loop (ai-lowcode-governance-enforcement-architecture)

**Completed:**

Research item:
- `Research/completed/2026-04-26-ai-lowcode-governance-enforcement-architecture.md` -- completed; the research concludes that enterprise governance enforcement for Artificial Intelligence (AI) and low-code systems has to be layered rather than centralized in one control point. Gateways handle ingress identity and traffic controls, authoritative data systems own final access decisions, orchestration layers constrain tools and promotion, and model runtimes provide semantic safety checks, with canonical policy translation needed to stop drift across layers.

Sources consulted:
- https://csrc.nist.gov/pubs/sp/800/207/final (zero-trust policy decision and enforcement model)
- https://learn.microsoft.com/en-us/azure/api-management/api-management-policies (gateway-layer enforcement controls)
- https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html (model-runtime guardrail controls)

## Mini-Retro

1. **Did the process work?** Yes, the research loop and review workflow converged quickly once the access-note and cross-reference rules were handled explicitly.
2. **What slowed down or went wrong?** The first review pass failed on citation-discipline details around replacement-source notes, and the second surfaced a real frontmatter dependency error plus a missing related-item cross-reference.
3. **What single change would prevent this next time?** Nothing new beyond following the existing prompt more literally on access-note phrasing and related-item sweeps before the first draft commit.
4. **Is this a pattern?** Yes, it matches the known pattern that visible access notes and adjacent completed-item links need tighter discipline than they appear to at first glance, but the current instructions already cover it.
