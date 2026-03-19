# 2026-03-19 — Research Loop (gitagent-declarative-agent-definition)

**Completed:**

Research item:
- `Research/completed/2026-03-16-gitagent-declarative-agent-definition.md` — completed; GitAgent is best treated as a Git-native packaging and governance layer rather than as a runtime replacement for this repository. Across Microsoft 365 Copilot, Amazon Bedrock, Azure Foundry, and OpenAI, declarative agent definition exists at different layers, but Model Context Protocol (MCP) emerged as the strongest interoperability bridge and the repository-specific recommendation is to adopt GitAgent only as a portability/export layer if that need becomes real.

Sources consulted:
- https://raw.githubusercontent.com/open-gitagent/gitagent/main/spec/SPECIFICATION.md (GitAgent specification)
- https://raw.githubusercontent.com/MicrosoftDocs/m365copilot-docs/main/docs/plugin-manifest-2.4.md (Microsoft 365 Copilot plugin manifest and remote MCP support)
- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.html (Amazon Bedrock Agent declarative resource model)

## Mini-Retro

1. **Did the process work?** Yes. The research loop, draft/review cycle, and completion workflow all worked end-to-end, and the second review pass succeeded.
2. **What slowed down or went wrong?** The first review surfaced citation and labeling issues concentrated in the Findings and compact synthesis sections, and the second review hit the cap logic even though its logs still contained some stale violations that I then cleaned up manually before completion.
3. **What single change would prevent this next time?** Add a stricter pre-draft inline check that verifies every compact synthesis bullet has sources at the point of claim and that no self-referential citations remain in recursive-review sections.
4. **Is this a pattern?** Yes. It matches the existing pattern that acronym expansion and citation discipline failures are common in research reviews; this session adds a narrower sub-pattern around compact synthesis sections losing inline citations during rewriting.
