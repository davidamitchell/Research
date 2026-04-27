# 2026-04-27 -- Research Loop (vendor-platform-governance-constraints-compensating-controls)

**Completed:**

Research item:
- `Research/completed/2026-04-26-vendor-platform-governance-constraints-compensating-controls.md` -- completed; the item concludes that no reviewed vendor provides a complete portable governance layer for regulated multi-platform estates, even when native controls are strong. Microsoft and Amazon Web Services (AWS) expose the deepest native surfaces in this sample, but both still need compensating controls for bypass paths, evidence capture, connected resources, and residency routing, while Salesforce, ServiceNow, UiPath, and OpenAI remain more estate-specific or narrower in governance scope.

Sources consulted:
- https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/governance-security-across-organization (Microsoft guidance on shared AI agent control planes)
- https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html (Amazon Bedrock native guardrail surface)
- https://developers.openai.com/api/docs/guides/your-data (OpenAI data, retention, and governance controls)

## Mini-Retro

1. **Did the process work?** Yes, the research loop worked end to end once the first review pass surfaced the synthesis overreach that needed tightening.
2. **What slowed down or went wrong?** The first draft overstated a comparative vendor-breadth claim and treated the external control-plane response too absolutely, which forced a second wording pass. A transient GitHub workflow dispatch timeout also required a retry before the final review run registered.
3. **What single change would prevent this next time?** Nothing in the repository needs changing from this session; the main prevention is stricter self-audit on comparative claims before the first draft commit.
4. **Is this a pattern?** Yes, it matches the existing recurring pattern about surface evaluation versus external benchmarking and direct source support for comparative claims, so no new pattern entry is needed.
