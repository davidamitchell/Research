# 2026-05-17 -- Add backlog items for AI platform capability research (ai-platform-capabilities)

**Completed:**
- `Research/backlog/2026-05-17-servicenow-ai-control-tower-capabilities.md` — added from issue; validated research question covering the full feature and governance capability set of ServiceNow AI Control Tower
- `Research/backlog/2026-05-17-ms-copilot-studio-capabilities.md` — added from issue; validated research question covering the full feature set of Microsoft Copilot Studio (agent building, RAG, governance, licensing)
- `Research/backlog/2026-05-17-ms-azure-ai-foundry-capabilities.md` — added from issue; validated research question covering the full feature set of Microsoft Azure AI Foundry (model catalogue, fine-tuning, evaluation, deployment, responsible AI)
- `Research/backlog/2026-05-17-aws-bedrock-capabilities.md` — added from issue; validated research question covering the complete AWS Bedrock feature set (models, agents, Knowledge Bases, Guardrails, Flows, customisation)
- `Research/backlog/2026-05-17-aws-bedrock-agentcore-suite-capabilities.md` — added from issue; validated research question covering Amazon Bedrock AgentCore suite (runtime, Gateway, Memory, Identity, Strands Agents SDK)

**Scope decision:** The issue listed five distinct platforms spanning three vendors. Each platform has sufficient scope to warrant a separate research item; grouping them would produce items too broad for thorough investigation by the research loop in a single session. The AgentCore item is marked as blocking on the AWS Bedrock item (so Bedrock core capabilities are understood first) via the `blocks` field.

**Acronyms expanded on first use in all items:** AI (Artificial Intelligence), FM (foundation model), RAG (Retrieval-Augmented Generation), ITSM (IT Service Management), HRSD (Human Resources Service Delivery), CSM (Customer Service Management), DLP (Data Loss Prevention), SDK (Software Development Kit), GA (Generally Available), IAM (Identity and Access Management), VPC (Virtual Private Cloud), RBAC (role-based access control), ML (Machine Learning), OIDC (OpenID Connect), ECS (Elastic Container Service), MCP (Model Context Protocol).

## Mini-Retro

1. **Did the process work?** Yes. The research-question skill applied cleanly to all five platforms. Each item has a validated question, scope, context, decomposed approach, and starting sources with URLs.
2. **What slowed down or went wrong?** Nothing significant. The issue gave clear platform names; the main judgment call was how to divide the scope (per-platform vs per-vendor groupings). Per-platform was the right choice given the research loop processes one item per session.
3. **What single change would prevent this next time?** Nothing to change; the workflow for handling new research request issues is well-established. The only minor gap was confirming whether AgentCore had any existing completed items — it did not, confirming the items are genuinely new.
4. **Is this a pattern?** The multi-platform research request is a recurring pattern. Splitting by platform and adding a `blocks` dependency where vendor context is needed (AgentCore depends on Bedrock) is the right structural response.
5. **Does any documentation need updating?** No. All five items follow the template exactly and use canonical tags from `docs/tag-vocabulary.md`.
6. **Do the default instructions need updating?** No new patterns or hard lessons emerged.
