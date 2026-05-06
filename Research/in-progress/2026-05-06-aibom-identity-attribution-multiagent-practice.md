---
review_count: 1
title: "How do OAuth 2.0, OpenID Connect, and SPIFFE token propagation work in real multi-agent pipelines, and where does end-to-end attribution break in practice?"
added: 2026-05-06T08:52:41+00:00
status: reviewing
priority: medium  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [agentic-ai, identity, security, access-control, delegation, attribution, llm, governance]
started: 2026-05-06T21:09:53+00:00
completed: ~
output: [knowledge]  # skill | tool | agent | knowledge | backlog-item
cites: [2026-05-06-aibom-identity-delegation-trust-theory, 2026-04-26-ai-agent-identity-access-management-enterprise, 2026-04-26-access-control-amplification-agentic-operations, 2026-04-26-permission-safe-rag-enterprise-information-architecture, 2026-05-06-aibom-platform-observability-control-comparison]
related: [2026-05-06-aibom-identity-delegation-trust-theory, 2026-05-06-aibom-platform-observability-control-comparison, 2026-05-06-aibom-effectiveness-risk-mitigation-limits, 2026-04-26-ai-agent-identity-access-management-enterprise]
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# How do OAuth 2.0, OpenID Connect, and SPIFFE token propagation work in real multi-agent pipelines, and where does end-to-end attribution break in practice?

## Research Question

How do OAuth 2.0 (Open Authorisation), OpenID Connect (OIDC), and SPIFFE (Secure Production Identity Framework for Everyone) token propagation mechanisms work in real multi-agent Artificial Intelligence (AI) pipelines, and where does end-to-end attribution break in practice, specifically across agent-to-agent delegation, agent-to-tool handoffs, and cross-system boundary crossings?

## Scope

**In scope:**
- Practical token propagation patterns for multi-agent systems using OAuth 2.0 on-behalf-of (OBO) flows, OIDC identity tokens, and SPIFFE Verifiable Identity Documents (SVIDs)
- Model Context Protocol (MCP) authorisation in practice: how MCP server-client identity and permission propagation works in real deployments
- Real-world examples of attribution working and failing in documented multi-agent compositions (Amazon Web Services (AWS) Bedrock multi-agent, LangGraph multi-agent, AutoGen, CrewAI)
- Token amplification and privilege escalation attack vectors that arise from delegation chain gaps
- Practical compensating controls for attribution gaps: structured audit logging, token binding, agent attestation receipts
- Assessment of which breakpoints are fixable with current tooling vs. require new standards or platform features

**Out of scope:**
- Theoretical identity model design (covered in `2026-05-06-aibom-identity-delegation-trust-theory`)
- Deep cryptographic protocol analysis of OAuth or OIDC internals
- Enterprise-wide IAM (Identity and Access Management) architecture design

**Constraints:**
- Must address at least two different multi-agent frameworks or platforms
- Must include at least one concrete attack scenario (with source) illustrating attribution failure
- Must build explicitly on the theoretical model from `2026-05-06-aibom-identity-delegation-trust-theory` and the enterprise Identity and Access Management (IAM) findings from `2026-04-26-ai-agent-identity-access-management-enterprise`

## Context

- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html] Prior completed repository work already established the design-time requirement for explicit identity, delegation, and permission modeling, and the enterprise requirement for separate machine identities and end-to-end attribution across users, agents, and downstream systems.
- [inference; source: https://www.rfc-editor.org/rfc/rfc8693; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/; https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html] The unresolved practical question is how much of that ideal survives in real multi-agent execution once delegated OAuth 2.0 tokens, Secure Production Identity Framework for Everyone (SPIFFE) workload identities, Model Context Protocol (MCP) tool calls, and platform trace records meet shared credentials, framework abstractions, and cross-system boundaries.

## Approach

1. **Token propagation patterns, OAuth 2.0 on-behalf-of (OBO):** document how delegated user-token propagation works in practice, where subject and actor survive, and where scope or audience intent is lost.

2. **Token propagation patterns, SPIFFE and SPIFFE Runtime Environment (SPIRE):** document what workload identity can prove about the current service and what it cannot express about human delegation provenance.

3. **Model Context Protocol (MCP) authorisation in practice:** document the current MCP authorization specification and assess whether MCP-based tool calls carry adequate attribution metadata for Artificial Intelligence Bill of Materials (AIBOM) purposes.

4. **Attribution failure case study:** document at least two concrete attribution failure scenarios from real multi-agent frameworks, including shared-credential tool execution and loss of original user context at agent boundaries.

5. **Compensating controls and remediation:** assess structured audit-log enrichment, token binding, workload federation, and receipt-style provenance capture, and separate what is achievable today from what still needs new standards work.

## Sources

- [x] [Internet Engineering Task Force (2020) Request for Comments (RFC) 8693 OAuth 2.0 Token Exchange](https://www.rfc-editor.org/rfc/rfc8693) - primary standard for delegation versus impersonation, `subject_token`, `actor_token`, `act`, `may_act`, and target-scope narrowing.
- [x] [Microsoft (2025) Microsoft identity platform and OAuth 2.0 On-Behalf-Of flow](https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-on-behalf-of-flow) - primary practical documentation for delegated user-token propagation in Microsoft ecosystems.
- [x] [OpenID Foundation (2023) OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html) - primary standard for end-user identity assertions layered on OAuth 2.0.
- [x] [SPIFFE (2025) SPIFFE Overview](https://spiffe.io/docs/latest/spiffe-about/overview/) - primary overview of workload identity, trust domains, and SPIFFE primitives.
- [x] [SPIFFE (2025) SPIFFE Concepts](https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/) - primary details on SPIFFE IDs, SPIFFE Verifiable Identity Documents (SVIDs), trust bundles, and the Workload Application Programming Interface (API).
- [x] [Model Context Protocol (2025) Authorization](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization) - primary MCP authorization specification for Authorization Code, Client Credentials, token handling, and third-party token mapping.
- [x] [Model Context Protocol (2025) Transports](https://modelcontextprotocol.io/specification/2025-03-26/basic/transports) - primary MCP transport specification for HTTP and standard input and standard output (STDIO) credential handling differences.
- [x] [Amazon Web Services (2025) Use multi-agent collaboration with Amazon Bedrock Agents](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html) - primary Bedrock documentation on supervisor and collaborator agent orchestration.
- [x] [Amazon Web Services (2025) Amazon Bedrock agent trace events](https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html) - primary Bedrock documentation on `callerChain`, `collaboratorName`, `sessionId`, and trace payload structure.
- [x] [CrewAI (2025) Collaboration](https://docs.crewai.com/en/concepts/collaboration.md) - primary CrewAI documentation on delegation tools and collaborator messaging.
- [x] [CrewAI (2025) Tools](https://docs.crewai.com/en/concepts/tools.md) - primary CrewAI documentation showing tool execution patterns and shared environment-variable credentials.
- [x] [CrewAI (2025) Large Language Models (LLMs)](https://docs.crewai.com/en/concepts/llms.md) - primary CrewAI documentation showing provider configuration via shared environment variables or runtime configuration.
- [x] [CrewAI (2025) Tools & Integrations](https://docs.crewai.com/en/enterprise/features/tools-and-integrations.md) - primary CrewAI platform documentation on OAuth-connected apps, enterprise tokens, and optional `user_bearer_token` scoping.
- [x] [CrewAI (2025) Agent-to-Agent (A2A) on the CrewAI platform](https://docs.crewai.com/en/enterprise/features/a2a.md) - primary CrewAI platform documentation on agent-to-agent authentication schemes, including OpenID Connect (OIDC), OAuth 2.0, Mutual Transport Layer Security (mTLS), and distributed state.
- [x] [CrewAI (2025) Vertex AI with Workload Identity](https://docs.crewai.com/en/enterprise/guides/vertex-ai-workload-identity-setup.md) - primary CrewAI platform documentation on per-execution OpenID Connect (OIDC) workload identity federation and short-lived credentials.
- [x] [Microsoft (2025) AutoGen Agents](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/agents.html) - primary AutoGen documentation on agent state, tool execution, and message events.
- [x] [Microsoft (2025) AutoGen UserProxyAgent](https://microsoft.github.io/autogen/stable/_modules/autogen_agentchat/agents/_user_proxy_agent.html) - primary AutoGen source documentation on representing a human user and handoff messages.
- [x] [Microsoft (2025) AutoGen Concurrent Agents](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/design-patterns/concurrent-agents.html) - primary AutoGen documentation on direct messaging and delegator-worker patterns.
- [x] [LangChain (2025) Multi-agent systems](https://docs.langchain.com/oss/python/langchain/multi-agent) - primary LangChain documentation on multi-agent patterns and subagents.
- [x] [LangChain (2025) Use subgraphs](https://docs.langchain.com/oss/javascript/langgraph/use-subgraphs) - primary LangGraph documentation showing explicit state mapping between parent and subgraph contexts.
- [x] [OWASP GenAI Security Project (2025) Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) - authoritative security taxonomy covering insecure plugin design and excessive agency.
- [x] [Mitchell (2026) AI agent identity and access management enterprise](https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html) - prior repository item on machine identity, delegation models, and attribution requirements.
- [x] [Mitchell (2026) Access control amplification under agentic operations](https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html) - prior repository item on blast-radius amplification under delegated automation.
- [x] [Mitchell (2026) Permission-safe Retrieval-Augmented Generation in enterprise information architectures](https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html) - prior repository item on cross-boundary retrieval and identity-sensitive access control.
- [x] [Mitchell (2026) How should identity, delegation chains, and permission scopes be formally modelled in an Artificial Intelligence Bill of Materials (AIBOM) schema to enable end-to-end attribution across agentic Artificial Intelligence (AI) systems?](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html) - prior repository item defining the design target this practice item tests.
- [x] [Mitchell (2026) What introspection, export, and control surfaces actually exist across production agentic Artificial Intelligence (AI) platforms?](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-platform-observability-control-comparison.html) - prior repository item on the runtime evidence substrate available from production platforms.

## Related

- [How should identity, delegation chains, and permission scopes be formally modelled in an Artificial Intelligence Bill of Materials (AIBOM) schema to enable end-to-end attribution across agentic Artificial Intelligence (AI) systems?](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html)
- [What identity and access management model is required for Artificial Intelligence (AI) agents and low-code artefacts operating within enterprise systems?](https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html)
- [Access control amplification under agentic operations: whether existing frameworks address the worst-case permission inheritance problem](https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html)
- [What introspection, export, and control surfaces actually exist across production agentic Artificial Intelligence (AI) platforms?](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-platform-observability-control-comparison.html)

---

## Research Skill Output

*(Full output from running the research skill - retained verbatim in the completed item. Sections 0-5 are the investigation, and Section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: How do OAuth 2.0 delegation, OpenID Connect (OIDC) identity assertions, Secure Production Identity Framework for Everyone (SPIFFE) workload identities, and Model Context Protocol (MCP) authorization behave in real multi-agent pipelines, and where does end-to-end attribution break across agent-to-agent, agent-to-tool, and cross-system hops?
- Scope: token propagation patterns, workload identity, MCP authorization, real framework behavior, attribution failure cases, and practical compensating controls across at least two multi-agent frameworks or platforms.
- Constraints: cover at least two frameworks or platforms, include at least one sourced attack scenario, and build explicitly on prior repository work about machine identity, delegation-chain modeling, access-control amplification, permission-safe retrieval, and platform observability.
- Output: knowledge.
- Prior completed items reviewed: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html ; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html ; https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html ; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-platform-observability-control-comparison.html

### §1 Question Decomposition

- **Root question:** Which identity and authorization mechanisms preserve reconstructable attribution across multi-agent execution today, and where do they stop short?
  - **A. User identity and delegated token propagation**
    - A1. What does OpenID Connect (OIDC) actually contribute to a multi-agent chain?
    - A2. What can OAuth 2.0 Token Exchange and on-behalf-of (OBO) flows preserve about subject, actor, audience, and scope?
    - A3. Where do delegated user-token patterns stop working in autonomous or app-only hops?
  - **B. Workload identity**
    - B1. What identity guarantees do SPIFFE IDs and SPIFFE Verifiable Identity Documents (SVIDs) provide?
    - B2. What delegation and permission semantics are absent from SPIFFE alone?
  - **C. MCP tool-boundary authorization**
    - C1. What does MCP standardize for Authorization Code, Client Credentials, and bearer-token handling?
    - C2. What attribution metadata does MCP leave to implementations?
  - **D. Framework behavior in practice**
    - D1. What attribution data do Amazon Bedrock multi-agent traces preserve?
    - D2. How do CrewAI, AutoGen, and LangGraph handle delegation and downstream tool identity by default?
  - **E. Failure modes and controls**
    - E1. Which practical attribution breakpoints create privilege amplification or ambiguous accountability?
    - E2. Which remediations are achievable with current platform features, and which require new standards or schema fields?

### §2 Investigation

#### A. What user-oriented token standards preserve

- [fact; source: https://openid.net/specs/openid-connect-core-1_0.html] OpenID Connect (OIDC) is an identity layer on top of OAuth 2.0 that lets a client verify the identity of the end user and obtain claims about that end user.
- [fact; source: https://www.rfc-editor.org/rfc/rfc8693] RFC 8693 distinguishes impersonation from delegation, defines `subject_token` for the party on behalf of whom a request is made, defines `actor_token` for the acting party, and defines `act` and `may_act` claims for delegated-token semantics.
- [fact; source: https://www.rfc-editor.org/rfc/rfc8693] RFC 8693 says a chain of delegation can be represented by nested `act` claims, but access-control decisions must consider only the top-level claims and the current actor, while prior actors are informational only.
- [fact; source: https://www.rfc-editor.org/rfc/rfc8693] RFC 8693 says the requested rights of a token exchange are effectively the Cartesian product of requested scopes across requested audiences and resources, which increases the chance of over-broad requests if target services are mixed.
- [fact; source: https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-on-behalf-of-flow] Microsoft's on-behalf-of (OBO) flow is explicitly a delegation pattern in which a middle-tier Application Programming Interface (API) uses a user's identity and delegated scopes to call another API.
- [fact; source: https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-on-behalf-of-flow] The Microsoft OBO flow uses delegated scopes only, keeps roles attached to the user principal rather than the application, and does not support app-only service-principal tokens, which must instead use the client-credentials flow.
- [inference; source: https://openid.net/specs/openid-connect-core-1_0.html; https://www.rfc-editor.org/rfc/rfc8693; https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-on-behalf-of-flow] OIDC is necessary for proving who the human principal is, but delegated OAuth 2.0 propagation is still required for downstream authorization, and neither mechanism alone preserves a portable, enforcement-relevant full hop history across a long multi-agent chain.
- [inference; source: https://www.rfc-editor.org/rfc/rfc8693; https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-on-behalf-of-flow; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html] Pure delegated user-token propagation is practical only for human-initiated API chains; once a hop is autonomous, app-only, or long-running without active user context, a separate machine identity and a separate audit record are required.

#### B. What SPIFFE preserves, and what it does not

- [fact; source: https://spiffe.io/docs/latest/spiffe-about/overview/; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/] SPIFFE provides short-lived workload identity through SPIFFE IDs, SPIFFE Verifiable Identity Documents (SVIDs), trust bundles, and the Workload API so workloads can mutually authenticate across heterogeneous environments.
- [fact; source: https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/] A SPIFFE Verifiable Identity Document (SVID) contains a single SPIFFE ID representing the service presenting it.
- [fact; source: https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/] The Workload API can return X.509 or JSON Web Token (JWT) SVIDs, trust bundles, and short-lived rotated credentials without co-deployed application secrets.
- [fact; source: https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/] SPIFFE treats a trust domain as the trust root for a set of workloads whose identity documents can be verified against that domain's root keys.
- [inference; source: https://spiffe.io/docs/latest/spiffe-about/overview/; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html] SPIFFE solves workload authentication and short-lived credential issuance well, but it does not express end-user delegation provenance, permission scope intent, or historical actor chains by itself, so it cannot close the full attribution problem alone.

#### C. What MCP standardizes at the tool boundary

- [fact; source: https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization] MCP authorization for Hypertext Transfer Protocol (HTTP) transports is based on OAuth 2.1, supports both confidential and public clients, and recommends Authorization Code for human end users and Client Credentials for application-to-application access.
- [fact; source: https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization] MCP clients must send `Authorization: Bearer <access-token>` on every authorized HTTP request, and invalid or expired access tokens must receive HTTP 401 responses.
- [fact; source: https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization] MCP servers may support third-party authorization, but they must securely map third-party tokens to issued MCP tokens, validate third-party token status, and manage token lifecycle.
- [fact; source: https://modelcontextprotocol.io/specification/2025-03-26/basic/transports] MCP says standard input and standard output (STDIO) transports should not use the HTTP authorization specification and instead retrieve credentials from the environment.
- [inference; source: https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization; https://modelcontextprotocol.io/specification/2025-03-26/basic/transports] MCP standardizes how a client gets authorized to call a tool server, but it does not define a standard subject-and-actor receipt, delegated-scope manifest, or cross-hop provenance envelope that would let an Artificial Intelligence Bill of Materials (AIBOM) reconstruct who originally authorized a tool action across transports.
- [inference; source: https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization; https://www.rfc-editor.org/rfc/rfc8693] MCP therefore addresses transport authorization, not full delegation-chain semantics, and implementations still need their own audit schema if they want subject, current actor, prior actors, and scope intent to survive tool calls.

#### D. Framework and platform behavior in practice

##### D1. Amazon Bedrock multi-agent collaboration

- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html] Amazon Bedrock multi-agent collaboration uses a supervisor agent that plans, routes, and coordinates one or more collaborator agents, each of which can have its own tools, action groups, knowledge bases, and guardrails.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html] Bedrock trace records expose `agentId`, `agentName`, `collaboratorName`, `agentAliasId`, `agentVersion`, `sessionId`, and `callerChain`, where `callerChain` lists the agent aliases that forwarded the end-user request to the current agent.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html] Bedrock traces also expose prompt text, model-invocation input and output, rationale, action-group inputs, observations, and knowledge-base interactions for traced steps.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html] Bedrock preserves a useful agent-routing chain, but the documented trace schema does not expose an end-user principal identifier, delegated scopes, or a cryptographically bound subject-to-tool receipt, so native tracing is stronger for agent-hop attribution than for human authorization attribution.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://owasp.org/www-project-top-10-for-large-language-model-applications/] A misrouted or maliciously induced collaborator action in Bedrock can therefore be traced to the forwarding agents and session, but not natively proven back to a specific delegated user permission set, which leaves an accountability gap for high-impact downstream actions.

##### D2. CrewAI collaboration and tools

- [fact; source: https://docs.crewai.com/en/concepts/collaboration.md] CrewAI collaboration turns on built-in delegation tools, specifically a delegate-work tool and an ask-question tool, when `allow_delegation=True`.
- [fact; source: https://docs.crewai.com/en/concepts/tools.md; https://docs.crewai.com/en/concepts/llms.md] CrewAI's open-source tool and model examples configure external access through shared environment variables such as `OPENAI_API_KEY` and `SERPER_API_KEY`, which are then used by agent tools and model clients at runtime.
- [fact; source: https://docs.crewai.com/en/enterprise/features/tools-and-integrations.md] The CrewAI platform's integrations are connected through OAuth, use an enterprise integration token for local use, and can optionally scope authentication to a requesting user through `user_bearer_token`; otherwise the deployment falls back to its default bearer token.
- [fact; source: https://docs.crewai.com/en/enterprise/guides/vertex-ai-workload-identity-setup.md] The CrewAI platform can also mint a short-lived OpenID Connect (OIDC) token per execution and exchange it through Google workload identity federation so that a running crew uses short-lived cloud credentials instead of long-lived service-account keys.
- [fact; source: https://docs.crewai.com/en/enterprise/features/a2a.md] The CrewAI platform's agent-to-agent communication supports multiple authentication schemes, including OIDC, OAuth 2.0, Mutual Transport Layer Security (mTLS), enterprise tokens, and API keys.
- [inference; source: https://docs.crewai.com/en/concepts/collaboration.md; https://docs.crewai.com/en/concepts/tools.md; https://docs.crewai.com/en/concepts/llms.md; https://docs.crewai.com/en/enterprise/features/tools-and-integrations.md] CrewAI's default open-source collaboration pattern favors shared runtime credentials and collaboration tools, so without enterprise scoping or workload federation the downstream action is attributable to the crew runtime or deployment token rather than to a specific end user or sub-agent-specific delegated scope.
- [inference; source: https://docs.crewai.com/en/enterprise/features/tools-and-integrations.md; https://docs.crewai.com/en/enterprise/guides/vertex-ai-workload-identity-setup.md; https://docs.crewai.com/en/enterprise/features/a2a.md] CrewAI is also a good example of a practical remediation path, because the platform already exposes per-user OAuth scoping, authenticated agent-to-agent channels, and per-execution workload identity for some cloud calls.

##### D3. AutoGen and LangGraph

- [fact; source: https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/agents.html] AutoGen's `AssistantAgent` is stateful, can use tools, and executes tools directly within the same `run()` call that processes the task.
- [fact; source: https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/agents.html] AutoGen's message examples show `TextMessage(source='user')`, tool-call request and execution events with `source='assistant'`, and tool-call summaries attributed to the assistant agent.
- [fact; source: https://microsoft.github.io/autogen/stable/_modules/autogen_agentchat/agents/_user_proxy_agent.html] AutoGen's `UserProxyAgent` represents a human user in the chat system and returns `TextMessage` or handoff messages, but its documented behavior is about conversation flow rather than downstream authorization propagation.
- [fact; source: https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/design-patterns/concurrent-agents.html] AutoGen concurrent-agent patterns route tasks through direct messages and agent IDs, with a delegator sending subtasks to worker agents and receiving their responses.
- [fact; source: https://docs.langchain.com/oss/python/langchain/multi-agent; https://docs.langchain.com/oss/javascript/langgraph/use-subgraphs] LangChain and LangGraph document subagents, routers, and subgraphs as orchestration patterns, and LangGraph requires explicit state mapping when parent and subgraph schemas differ.
- [inference; source: https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/agents.html; https://microsoft.github.io/autogen/stable/_modules/autogen_agentchat/agents/_user_proxy_agent.html; https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/design-patterns/concurrent-agents.html] In AutoGen, the human can be represented in the conversation, but tool execution is documented as an assistant-side runtime action rather than a delegated end-user token handoff, so downstream tool identity is application-managed rather than framework-native.
- [inference; source: https://docs.langchain.com/oss/python/langchain/multi-agent; https://docs.langchain.com/oss/javascript/langgraph/use-subgraphs] In LangGraph, identity propagation is likewise developer-managed state, because the framework documents how to pass state between subgraphs and agents but does not define a built-in security or delegation model for the user principal across those hops.

#### E. Concrete attribution-failure scenarios and controls

- [fact; source: https://owasp.org/www-project-top-10-for-large-language-model-applications/] OWASP lists insecure plugin design and excessive agency as major Large Language Model (LLM) application risks, specifically warning that unchecked action-taking and insufficient access control create severe downstream security consequences.
- [inference; source: https://docs.crewai.com/en/concepts/tools.md; https://docs.crewai.com/en/concepts/llms.md; https://docs.crewai.com/en/concepts/collaboration.md; https://owasp.org/www-project-top-10-for-large-language-model-applications/] **Case 1, CrewAI shared-key delegation:** if multiple collaborating CrewAI agents use tools backed by shared environment-variable credentials, a compromised or prompt-injected sub-agent can invoke the same downstream capability as its peers, and external logs may show only the shared credential rather than the original user or a least-privilege sub-agent identity.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://owasp.org/www-project-top-10-for-large-language-model-applications/] **Case 2, Bedrock collaborator trace gap:** if a Bedrock supervisor routes a request to a collaborator that invokes a high-impact action group, the native trace can reconstruct the agent forwarding path and session but does not document a bound end-user principal or delegated scope, so post-incident review can see which agent acted without natively proving who authorized the authority surface.
- [inference; source: https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/agents.html; https://microsoft.github.io/autogen/stable/_modules/autogen_agentchat/agents/_user_proxy_agent.html] **Case 3, AutoGen conversation identity split:** if an AutoGen application uses `UserProxyAgent` for human interaction but lets `AssistantAgent` execute tools directly, downstream side effects are operationally tied to the assistant runtime unless the developer explicitly propagates user identity into tool-level credentials or audit records.
- [inference; source: https://www.rfc-editor.org/rfc/rfc8693; https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-platform-observability-control-comparison.html] The practical control stack that works today is a layered one: delegated user tokens for human-initiated API hops, SPIFFE or cloud workload federation for machine hops, edge-bound permission manifests, trace enrichment with subject and current actor, and platform-specific receipts or logs that persist the full historical chain outside the token itself.
- [inference; source: https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization; https://docs.crewai.com/en/enterprise/features/tools-and-integrations.md; https://docs.crewai.com/en/enterprise/guides/vertex-ai-workload-identity-setup.md] What still needs new standards work is a portable delegation-chain receipt for agent-to-tool and agent-to-agent calls, because current standards secure the call itself but do not standardize a reusable artifact that binds user subject, current actor, prior actors, scopes, target resource, and approval context in one verifiable structure.

### §3 Reasoning

- [fact; source: https://openid.net/specs/openid-connect-core-1_0.html; https://www.rfc-editor.org/rfc/rfc8693; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/; https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization] Current standards each solve a different slice of the problem: OIDC proves end-user identity, OAuth 2.0 Token Exchange models delegated access, SPIFFE proves workload identity, and MCP secures tool-server authorization.
- [fact; source: https://www.rfc-editor.org/rfc/rfc8693; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://docs.crewai.com/en/enterprise/features/tools-and-integrations.md] The evidence also shows a recurring structural gap between what is needed for runtime enforcement and what is needed for forensic attribution, because standards and platform traces prioritize the current authorized caller while long delegation history and original-user provenance often survive only in side-channel logs or developer-managed state.
- [inference; source: https://www.rfc-editor.org/rfc/rfc8693; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/agents.html; https://docs.langchain.com/oss/javascript/langgraph/use-subgraphs] Attribution therefore breaks not because identity is absent everywhere, but because each hop preserves a different identity object, human subject, current actor, workload, agent alias, or graph state, without a common receipt that binds them together end to end.
- [inference; source: https://docs.crewai.com/en/enterprise/features/tools-and-integrations.md; https://docs.crewai.com/en/enterprise/guides/vertex-ai-workload-identity-setup.md; https://docs.crewai.com/en/enterprise/features/a2a.md] The practical remediation problem is therefore architectural rather than purely protocol-level: use the right credential type for each hop, narrow it at every boundary, and persist a separate attribution artifact that survives when native tokens or traces do not.
- [assumption; source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://docs.crewai.com/en/concepts/tools.md; https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/agents.html] A production deployment can enrich native traces with user and approval metadata at the application layer even when the underlying framework does not provide that feature directly. Justification: the examined frameworks expose enough message, trace, or integration hooks to attach custom audit metadata, but the quality and portability of that enrichment were not independently tested in this item.

### §4 Consistency Check

- [fact; source: https://www.rfc-editor.org/rfc/rfc8693; https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-on-behalf-of-flow] There is no contradiction between RFC 8693's broader token-exchange model and Microsoft's narrower OBO implementation: RFC 8693 is a generic delegation framework, while Microsoft's implementation deliberately restricts OBO to user principals and delegated scopes.
- [fact; source: https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/; https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization] There is no contradiction between SPIFFE and MCP either, because SPIFFE solves workload authentication while MCP specifies transport-level authorization behavior for tool servers; they operate at different layers.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/agents.html; https://docs.langchain.com/oss/javascript/langgraph/use-subgraphs] The apparent tension between strong trace visibility in some platforms and weak attribution in others resolves once the control surface is separated into agent-hop tracing versus human-authorization tracing: Bedrock documents the first better than the second, while AutoGen and LangGraph mostly leave both to application design.
- [fact; source: https://docs.crewai.com/en/concepts/tools.md; https://docs.crewai.com/en/enterprise/features/tools-and-integrations.md; https://docs.crewai.com/en/enterprise/guides/vertex-ai-workload-identity-setup.md] CrewAI's evidence is internally consistent: open-source examples default to shared runtime credentials, and the enterprise documentation documents explicit mechanisms for replacing those defaults with scoped OAuth or workload federation.
- [inference; source: https://owasp.org/www-project-top-10-for-large-language-model-applications/; https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html] The attack scenarios align with the repository's prior access-amplification work, because the security issue is not merely missing logs but the combination of broad authority surfaces and ambiguous delegation provenance.

### §5 Depth and Breadth Expansion

[fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html; https://owasp.org/www-project-top-10-for-large-language-model-applications/] **Technical lens:** broad shared credentials and missing delegation receipts increase both privilege-amplification risk and post-incident ambiguity.

[inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html; https://docs.crewai.com/en/enterprise/features/tools-and-integrations.md; https://docs.crewai.com/en/enterprise/guides/vertex-ai-workload-identity-setup.md] **Economic lens:** the cheapest path in many frameworks is still shared runtime credentials, but the downstream cost is higher incident-analysis effort, weaker least-privilege enforcement, and more compensating-control engineering.

[inference; source: https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-platform-observability-control-comparison.html] **Operational lens:** attribution quality depends on whether the platform exposes enough event fields to reconstruct authority edges, which makes observability features a first-class security control rather than only a debugging aid.

[inference; source: https://www.rfc-editor.org/rfc/rfc8693; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/; https://docs.crewai.com/en/enterprise/features/a2a.md] **Architectural lens:** the stable design boundary is hybrid, human delegation should stay in delegated tokens, machine delegation should stay in workload identity or machine credentials, and cross-agent hops need a separate receipt or manifest layer.

[inference; source: https://docs.langchain.com/oss/javascript/langgraph/use-subgraphs; https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/design-patterns/concurrent-agents.html] **Behavioral lens:** open orchestration frameworks optimize for flexible state passing and tool composition, which encourages capability growth faster than identity discipline unless developers consciously model identity as part of state and logging.

### §6 Synthesis

*(This section seeds the Findings below.)*

**Executive summary:**

- OAuth 2.0 and OpenID Connect (OIDC) can preserve end-user identity and delegated authorization across human-initiated API hops, but they do not by themselves preserve a portable, enforcement-relevant full attribution chain across autonomous multi-agent systems. [inference; source: https://openid.net/specs/openid-connect-core-1_0.html; https://www.rfc-editor.org/rfc/rfc8693; https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-on-behalf-of-flow]
- Secure Production Identity Framework for Everyone (SPIFFE) and cloud workload-federation patterns solve the machine-identity half of the problem by issuing short-lived workload credentials, but they do not encode end-user delegation provenance or permission intent. [inference; source: https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/; https://docs.crewai.com/en/enterprise/guides/vertex-ai-workload-identity-setup.md]
- In the examined frameworks and platforms, attribution breaks when a tool call or sub-agent hop changes credential type, crosses trust domains, or falls back to shared runtime credentials, because the native trace shows the current caller better than the original authorizer. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://docs.crewai.com/en/concepts/tools.md; https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/agents.html]
- The best current design is hybrid: delegated user tokens for human-initiated hops, workload identity for autonomous hops, explicit edge-bound permission manifests, and enriched audit receipts that persist subject, current actor, target, and scope outside the token itself. [inference; source: https://www.rfc-editor.org/rfc/rfc8693; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/; https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html]

**Key findings:**

- 1. **OpenID Connect (OIDC) and delegated OAuth 2.0 flows preserve human identity and delegated authority only for the active subject and current actor, which makes them useful for user-initiated API chains but insufficient as a full historical attribution record for long multi-agent pipelines.** ([fact]; high confidence; source: https://openid.net/specs/openid-connect-core-1_0.html; https://www.rfc-editor.org/rfc/rfc8693)
- 2. **Microsoft's on-behalf-of (OBO) implementation proves the practical boundary of delegated user-token propagation, because it supports delegated user scopes for middle-tier APIs but explicitly excludes app-only service-principal tokens, which must switch to a machine-oriented credential pattern.** ([fact]; medium confidence; source: https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-on-behalf-of-flow)
- 3. **SPIFFE provides strong short-lived workload identity and trust-domain verification, but because each SPIFFE Verifiable Identity Document (SVID) represents a single presenting workload and not a delegated human chain, SPIFFE alone cannot express who originally authorized a downstream action.** ([inference]; high confidence; source: https://spiffe.io/docs/latest/spiffe-about/overview/; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/)
- 4. **Model Context Protocol (MCP) standardizes how clients authorize to tool servers through Authorization Code or Client Credentials and bearer tokens on every HTTP request, yet it leaves subject-and-actor provenance receipts to implementations rather than defining them as protocol-native artifacts.** ([fact]; high confidence; source: https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization; https://modelcontextprotocol.io/specification/2025-03-26/basic/transports)
- 5. **Amazon Bedrock multi-agent traces preserve valuable agent-routing metadata such as collaborator names, session identifiers, agent versions, and caller chains, but the documented trace schema does not natively bind those records to an end-user principal or delegated scope set.** ([fact]; medium confidence; source: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html)
- 6. **Open-source orchestration frameworks such as CrewAI, AutoGen, and LangGraph treat identity propagation mainly as runtime configuration or application state, so downstream tools are commonly invoked under shared deployment credentials or assistant runtime identity unless developers add explicit per-user or per-hop controls.** ([inference]; medium confidence; source: https://docs.crewai.com/en/concepts/tools.md; https://docs.crewai.com/en/concepts/llms.md; https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/agents.html; https://docs.langchain.com/oss/javascript/langgraph/use-subgraphs)
- 7. **CrewAI's enterprise features show that important parts of the attribution gap are fixable today, because the platform already supports OAuth-scoped integrations, optional `user_bearer_token` user scoping, authenticated agent-to-agent communication, and per-execution workload identity federation.** ([fact]; medium confidence; source: https://docs.crewai.com/en/enterprise/features/tools-and-integrations.md; https://docs.crewai.com/en/enterprise/features/a2a.md; https://docs.crewai.com/en/enterprise/guides/vertex-ai-workload-identity-setup.md)
- 8. **The remaining gap is a portable delegation-chain receipt that survives across frameworks, tools, and trust domains, because current standards secure individual hops well but do not standardize one verifiable artifact containing original subject, current actor, prior actors, scopes, target resource, and approval context.** ([inference]; medium confidence; source: https://www.rfc-editor.org/rfc/rfc8693; https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] OIDC provides end-user identity assertions, while RFC 8693 defines delegated actor semantics and nested `act` history that is not enforcement-relevant beyond the current actor. | https://openid.net/specs/openid-connect-core-1_0.html ; https://www.rfc-editor.org/rfc/rfc8693 | high | User identity plus delegated actor, not full historical enforcement chain |
| [fact] Microsoft's OBO flow supports delegated user scopes for middle-tier APIs and excludes app-only service-principal tokens. | https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-on-behalf-of-flow | medium | Human delegation only |
| [fact] SPIFFE issues short-lived workload identity through a single SPIFFE ID per SVID and trust-domain verification. | https://spiffe.io/docs/latest/spiffe-about/overview/ ; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/ | high | Workload authentication, not end-user delegation |
| [fact] MCP standardizes Authorization Code, Client Credentials, bearer-token usage on every HTTP request, and third-party token mapping requirements. | https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization ; https://modelcontextprotocol.io/specification/2025-03-26/basic/transports | high | Transport authorization layer |
| [fact] Bedrock trace events document collaborator names, caller chains, session IDs, versions, prompts, rationale, and action inputs, but no documented end-user principal field. | https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html ; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html | medium | Strong agent-hop trace, partial human provenance |
| [inference] CrewAI, AutoGen, and LangGraph leave cross-hop identity propagation largely to runtime configuration or application state. | https://docs.crewai.com/en/concepts/tools.md ; https://docs.crewai.com/en/concepts/llms.md ; https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/agents.html ; https://docs.langchain.com/oss/javascript/langgraph/use-subgraphs | medium | Framework flexibility exceeds built-in identity semantics |
| [fact] The CrewAI platform already exposes OAuth-scoped integrations, optional user scoping, multiple authenticated agent-to-agent schemes, and per-execution workload identity federation. | https://docs.crewai.com/en/enterprise/features/tools-and-integrations.md ; https://docs.crewai.com/en/enterprise/features/a2a.md ; https://docs.crewai.com/en/enterprise/guides/vertex-ai-workload-identity-setup.md | medium | Practical remediation features exist |
| [inference] A portable delegation-chain receipt remains unsolved across frameworks and protocols. | https://www.rfc-editor.org/rfc/rfc8693 ; https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html | medium | Standards gap, not only implementation gap |

**Assumptions:**

- [assumption; source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://docs.crewai.com/en/concepts/tools.md; https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/agents.html] Native traces or message events can be enriched with custom application metadata when teams need stronger attribution than the framework provides. Justification: the examined platforms expose enough hooks to attach metadata, but this item did not validate the durability or consistency of those custom extensions.

**Analysis:**

- The evidence weighs most strongly in favor of a split model rather than a single universal credential. [inference; source: https://www.rfc-editor.org/rfc/rfc8693; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/; https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-on-behalf-of-flow]
- Delegated user tokens fit hops where a human is actively authorizing access to downstream APIs, because they preserve user identity, audience, and scope semantics that workload identity does not. [inference; source: https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-on-behalf-of-flow; https://openid.net/specs/openid-connect-core-1_0.html]
- Workload identity fits hops where a task is autonomous, app-only, or long-running, because those hops need a machine identity that can rotate independently of a human session and survive beyond an interactive consent event. [inference; source: https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/; https://docs.crewai.com/en/enterprise/guides/vertex-ai-workload-identity-setup.md]
- The main trade-off is that user delegation provides better human accountability while workload identity provides better runtime durability and least-secret handling, so practical systems need both and must record where the handoff from one model to the other occurred. [inference; source: https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-on-behalf-of-flow; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/; https://www.rfc-editor.org/rfc/rfc8693]
- Bedrock's native trace depth improves incident reconstruction for agent routing, but open-source frameworks offer more flexibility and therefore require more application-layer identity discipline. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://docs.crewai.com/en/concepts/collaboration.md; https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/design-patterns/concurrent-agents.html; https://docs.langchain.com/oss/python/langchain/multi-agent]
- Plausible rival remedies exist, including stronger model-quality gates, more human review, or preserving per-item manual approval for sensitive tools, but those rivals mostly reduce misuse probability rather than solving the provenance problem that appears once a tool call has already crossed a boundary. [inference; source: https://owasp.org/www-project-top-10-for-large-language-model-applications/; https://docs.crewai.com/en/enterprise/features/tools-and-integrations.md; https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html]
- The strongest conclusion is therefore architectural: attribution gaps are partly fixable today with better credential separation, scope narrowing, and audit receipts, while portable cross-framework delegation proof still requires new standardization work. [inference; source: https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization; https://docs.crewai.com/en/enterprise/guides/vertex-ai-workload-identity-setup.md; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html]

**Risks, gaps, uncertainties:**

- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://docs.crewai.com/en/enterprise/features/tools-and-integrations.md] Public documentation may understate platform-specific hooks or internal telemetry fields that enterprise customers can configure but that are not described openly.
- [fact; source: https://docs.crewai.com/en/enterprise/features/tools-and-integrations.md; https://docs.crewai.com/en/enterprise/features/a2a.md] CrewAI's stronger identity controls are concentrated in the platform's enterprise features, so open-source-only deployments still face a larger attribution gap by default.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html] Bedrock's native trace documentation is rich for agent orchestration, but it does not rule out stronger customer-managed user attribution added outside the documented schema.
- [inference; source: https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization] MCP authorization is still evolving, so richer portable provenance fields could emerge without a wholly new protocol if the ecosystem standardizes them.

**Open questions:**

- Should the repository create a follow-on item for a portable delegation-receipt schema that can be embedded in an Artificial Intelligence Bill of Materials (AIBOM) edge record and emitted by Model Context Protocol (MCP), agent-to-agent, and tool-call frameworks?
- Which existing signing or attestation formats could carry subject, current actor, prior actors, target resource, approval state, and scope intent without exposing unnecessary personal data?
- What is the minimum trace field set that Amazon Bedrock, CrewAI, AutoGen, and LangGraph would each need to expose natively for end-user attribution to become reviewable without custom middleware?

### §7 Recursive Review

- Status: complete.
- Confidence assessment: medium, because the key protocol claims are primary-source backed, but several framework-attribution conclusions are inferential and based on documented behavior rather than validated live deployments.
- Sourcing check: each factual or inferential claim in the investigation and Findings is labeled and URL-backed.
- Uncertainty check: residual uncertainty is concentrated in undocumented implementation details and future standard evolution, not in the core protocol boundaries identified above.

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

OAuth 2.0 and OpenID Connect (OIDC) preserve enough identity and authorization context for human-initiated Application Programming Interface (API) delegation, but they do not by themselves preserve a portable, end-to-end attribution chain across autonomous multi-agent systems. [inference; source: https://openid.net/specs/openid-connect-core-1_0.html; https://www.rfc-editor.org/rfc/rfc8693; https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-on-behalf-of-flow]
Secure Production Identity Framework for Everyone (SPIFFE) and cloud workload-federation patterns close the machine-identity problem with short-lived workload credentials, yet they do not encode who originally authorized the work or what user-level scope intent should survive later hops. [inference; source: https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/; https://docs.crewai.com/en/enterprise/guides/vertex-ai-workload-identity-setup.md]
In the examined frameworks and platforms, attribution breaks when a sub-agent or tool call changes credential type, crosses a trust boundary, or falls back to shared runtime credentials, because native traces expose the current caller more clearly than the original authorizer. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://docs.crewai.com/en/concepts/tools.md; https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/agents.html]
The strongest current pattern is hybrid: delegated user tokens for human-initiated hops, workload identity for autonomous hops, explicit edge-bound permission manifests, and a separate audit receipt that persists subject, current actor, target, and scope outside the runtime token. [inference; source: https://www.rfc-editor.org/rfc/rfc8693; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/; https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html]

### Key Findings

1. **OpenID Connect (OIDC) and delegated OAuth 2.0 flows preserve human identity and delegated authority only for the active subject and current actor, which makes them useful for user-initiated API chains but insufficient as a full historical attribution record for long multi-agent pipelines.** ([fact]; high confidence; source: https://openid.net/specs/openid-connect-core-1_0.html; https://www.rfc-editor.org/rfc/rfc8693)
2. **Microsoft's on-behalf-of (OBO) implementation proves the practical boundary of delegated user-token propagation, because it supports delegated user scopes for middle-tier APIs but explicitly excludes app-only service-principal tokens, which must switch to a machine-oriented credential pattern.** ([fact]; medium confidence; source: https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-on-behalf-of-flow)
3. **SPIFFE provides strong short-lived workload identity and trust-domain verification, but because each SPIFFE Verifiable Identity Document (SVID) represents a single presenting workload and not a delegated human chain, SPIFFE alone cannot express who originally authorized a downstream action.** ([inference]; high confidence; source: https://spiffe.io/docs/latest/spiffe-about/overview/; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/)
4. **Model Context Protocol (MCP) standardizes how clients authorize to tool servers through Authorization Code or Client Credentials and bearer tokens on every HTTP request, yet it leaves subject-and-actor provenance receipts to implementations rather than defining them as protocol-native artifacts.** ([fact]; high confidence; source: https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization; https://modelcontextprotocol.io/specification/2025-03-26/basic/transports)
5. **Amazon Bedrock multi-agent traces preserve valuable agent-routing metadata such as collaborator names, session identifiers, agent versions, and caller chains, but the documented trace schema does not natively bind those records to an end-user principal or delegated scope set.** ([fact]; medium confidence; source: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html)
6. **Open-source orchestration frameworks such as CrewAI, AutoGen, and LangGraph treat identity propagation mainly as runtime configuration or application state, so downstream tools are commonly invoked under shared deployment credentials or assistant runtime identity unless developers add explicit per-user or per-hop controls.** ([inference]; medium confidence; source: https://docs.crewai.com/en/concepts/tools.md; https://docs.crewai.com/en/concepts/llms.md; https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/agents.html; https://docs.langchain.com/oss/javascript/langgraph/use-subgraphs)
7. **CrewAI's enterprise features show that important parts of the attribution gap are fixable today, because the platform already supports OAuth-scoped integrations, optional `user_bearer_token` user scoping, authenticated agent-to-agent communication, and per-execution workload identity federation.** ([fact]; medium confidence; source: https://docs.crewai.com/en/enterprise/features/tools-and-integrations.md; https://docs.crewai.com/en/enterprise/features/a2a.md; https://docs.crewai.com/en/enterprise/guides/vertex-ai-workload-identity-setup.md)
8. **The remaining gap is a portable delegation-chain receipt that survives across frameworks, tools, and trust domains, because current standards secure individual hops well but do not standardize one verifiable artifact containing original subject, current actor, prior actors, scopes, target resource, and approval context.** ([inference]; medium confidence; source: https://www.rfc-editor.org/rfc/rfc8693; https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] OIDC provides end-user identity assertions, while RFC 8693 defines delegated actor semantics and nested `act` history that is not enforcement-relevant beyond the current actor. | https://openid.net/specs/openid-connect-core-1_0.html ; https://www.rfc-editor.org/rfc/rfc8693 | high | User identity plus delegated actor, not full historical enforcement chain |
| [fact] Microsoft's OBO flow supports delegated user scopes for middle-tier APIs and excludes app-only service-principal tokens. | https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-on-behalf-of-flow | medium | Human delegation only |
| [fact] SPIFFE issues short-lived workload identity through a single SPIFFE ID per SVID and trust-domain verification. | https://spiffe.io/docs/latest/spiffe-about/overview/ ; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/ | high | Workload authentication, not end-user delegation |
| [fact] MCP standardizes Authorization Code, Client Credentials, bearer-token usage on every HTTP request, and third-party token mapping requirements. | https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization ; https://modelcontextprotocol.io/specification/2025-03-26/basic/transports | high | Transport authorization layer |
| [fact] Bedrock trace events document collaborator names, caller chains, session IDs, versions, prompts, rationale, and action inputs, but no documented end-user principal field. | https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html ; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html | medium | Strong agent-hop trace, partial human provenance |
| [inference] CrewAI, AutoGen, and LangGraph leave cross-hop identity propagation largely to runtime configuration or application state. | https://docs.crewai.com/en/concepts/tools.md ; https://docs.crewai.com/en/concepts/llms.md ; https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/agents.html ; https://docs.langchain.com/oss/javascript/langgraph/use-subgraphs | medium | Framework flexibility exceeds built-in identity semantics |
| [fact] The CrewAI platform already exposes OAuth-scoped integrations, optional user scoping, multiple authenticated agent-to-agent schemes, and per-execution workload identity federation. | https://docs.crewai.com/en/enterprise/features/tools-and-integrations.md ; https://docs.crewai.com/en/enterprise/features/a2a.md ; https://docs.crewai.com/en/enterprise/guides/vertex-ai-workload-identity-setup.md | medium | Practical remediation features exist |
| [inference] A portable delegation-chain receipt remains unsolved across frameworks and protocols. | https://www.rfc-editor.org/rfc/rfc8693 ; https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html | medium | Standards gap, not only implementation gap |

### Assumptions

- **Assumption:** Native traces or message events can be enriched with custom application metadata when teams need stronger attribution than the framework provides. **Justification:** The examined platforms expose enough hooks to attach metadata, but this item did not validate the durability or consistency of those custom extensions. [assumption; source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://docs.crewai.com/en/concepts/tools.md; https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/agents.html]

### Analysis

The evidence weighs most strongly in favor of a split model rather than a single universal credential. [inference; source: https://www.rfc-editor.org/rfc/rfc8693; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/; https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-on-behalf-of-flow]
Delegated user tokens fit hops where a human is actively authorizing access to downstream APIs, because they preserve user identity, audience, and scope semantics that workload identity does not. [inference; source: https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-on-behalf-of-flow; https://openid.net/specs/openid-connect-core-1_0.html]
Workload identity fits hops where a task is autonomous, app-only, or long-running, because those hops need a machine identity that can rotate independently of a human session and survive beyond an interactive consent event. [inference; source: https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/; https://docs.crewai.com/en/enterprise/guides/vertex-ai-workload-identity-setup.md]
The main trade-off is that user delegation provides better human accountability while workload identity provides better runtime durability and least-secret handling, so practical systems need both and must record where the handoff from one model to the other occurred. [inference; source: https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-on-behalf-of-flow; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/; https://www.rfc-editor.org/rfc/rfc8693]
Bedrock's native trace depth improves incident reconstruction for agent routing, but open-source frameworks offer more flexibility and therefore require more application-layer identity discipline. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://docs.crewai.com/en/concepts/collaboration.md; https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/design-patterns/concurrent-agents.html; https://docs.langchain.com/oss/python/langchain/multi-agent]
Plausible rival remedies exist, including stronger model-quality gates, more human review, or preserving per-item manual approval for sensitive tools, but those rivals mostly reduce misuse probability rather than solving the provenance problem that appears once a tool call has already crossed a boundary. [inference; source: https://owasp.org/www-project-top-10-for-large-language-model-applications/; https://docs.crewai.com/en/enterprise/features/tools-and-integrations.md; https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html]
The strongest conclusion is therefore architectural: attribution gaps are partly fixable today with better credential separation, scope narrowing, and audit receipts, while portable cross-framework delegation proof still requires new standardization work. [inference; source: https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization; https://docs.crewai.com/en/enterprise/guides/vertex-ai-workload-identity-setup.md; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html]

### Risks, Gaps, and Uncertainties

- Public documentation may understate platform-specific hooks or internal telemetry fields that enterprise customers can configure but that are not described openly. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://docs.crewai.com/en/enterprise/features/tools-and-integrations.md]
- CrewAI's stronger identity controls are concentrated in the platform's enterprise features, so open-source-only deployments still face a larger attribution gap by default. [fact; source: https://docs.crewai.com/en/enterprise/features/tools-and-integrations.md; https://docs.crewai.com/en/enterprise/features/a2a.md]
- Bedrock's native trace documentation is rich for agent orchestration, but it does not rule out stronger customer-managed user attribution added outside the documented schema. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html]
- MCP authorization is still evolving, so richer portable provenance fields could emerge without a wholly new protocol if the ecosystem standardizes them. [inference; source: https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization]

### Open Questions

- Should the repository create a follow-on item for a portable delegation-receipt schema that can be embedded in an Artificial Intelligence Bill of Materials (AIBOM) edge record and emitted by Model Context Protocol (MCP), agent-to-agent, and tool-call frameworks?
- Which existing signing or attestation formats could carry subject, current actor, prior actors, target resource, approval state, and scope intent without exposing unnecessary personal data?
- What is the minimum trace field set that Amazon Bedrock, CrewAI, AutoGen, and LangGraph would each need to expose natively for end-user attribution to become reviewable without custom middleware?

---

## Output

- Type: knowledge
- Description: Practical assessment of identity propagation, attribution breakpoints, and compensating controls for multi-agent systems, grounded in OAuth 2.0, OpenID Connect (OIDC), Secure Production Identity Framework for Everyone (SPIFFE), Model Context Protocol (MCP), and framework-specific evidence. [inference; source: https://www.rfc-editor.org/rfc/rfc8693; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/; https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization]
- Links:
  - https://www.rfc-editor.org/rfc/rfc8693
  - https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization
  - https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html
