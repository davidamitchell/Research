---
review_count: 1
title: "How should identity, delegation chains, and permission scopes be formally modelled in an Artificial Intelligence Bill of Materials (AIBOM) schema to enable end-to-end attribution across agentic Artificial Intelligence (AI) systems?"
added: 2026-05-06T08:52:41+00:00
status: in-progress
priority: high
blocks: [2026-05-06-aibom-identity-attribution-multiagent-practice]
tags: [agentic-ai, identity, security, governance, access-control, delegation, attribution, zero-trust]
started: 2026-05-06T09:51:18+00:00
completed: ~
output: [knowledge]
cites: [2026-04-26-ai-agent-identity-access-management-enterprise, 2026-04-26-access-control-amplification-agentic-operations, 2026-04-26-permission-safe-rag-enterprise-information-architecture, 2026-04-26-agentic-ai-regulatory-preconditions-control-failure-assessment]
related: [2026-03-18-api-context-hubs-rag-mcp]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# How should identity, delegation chains, and permission scopes be formally modelled in an Artificial Intelligence Bill of Materials (AIBOM) schema to enable end-to-end attribution across agentic Artificial Intelligence (AI) systems?

## Research Question

How should identity, delegation, and permission scopes be formally represented in an Artificial Intelligence Bill of Materials (AIBOM) schema to enable end-to-end attribution, "who authorized what", across multi-agent compositions involving human users, orchestrator agents, sub-agents, tools, and model instances, and where do current identity standards, OAuth 2.0, OpenID Connect (OIDC), Secure Production Identity Framework for Everyone (SPIFFE), and zero-trust guidance, succeed or fail when applied to agentic delegation chains?

## Scope

**In scope:**
- Formal modelling of agentic identity types: human user, orchestrator agent, sub-agent, tool or service, model instance, and ambient execution context
- Delegation chain representation: how an authorization granted by a human user propagates through an orchestrator to sub-agents and tools, and how AIBOM should capture this chain
- Permission scope manifests: how the set of authorized operations for each identity should be declared and versioned in AIBOM
- Zero-trust principles applied to agentic flows: treating every agent-to-tool and agent-to-agent call as a request that requires explicit verification
- Analysis of OAuth 2.0 and OIDC delegation, token propagation, and on-behalf-of flows, and their adequacy for agentic multi-hop delegation
- Impersonation and privilege-escalation attack vectors in delegation chains
- Cross-system boundary crossings: when an agent calls an external tool or Retrieval-Augmented Generation (RAG) source outside its original trust domain

**Out of scope:**
- Platform-specific identity implementation details
- Runtime trace capture mechanisms
- Specific enterprise Identity and Access Management (IAM) product evaluations

**Constraints:**
- Must engage with at least two formal identity standards
- Must address multi-agent compositions, not only single-agent scenarios
- Must build explicitly on prior completed repository work about agent identity and governance

## Context

- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html] Prior completed repository work already established that agentic systems need distinct machine identities, that over-privileged delegated access is amplified under automated operation, and that cross-boundary retrieval becomes unsafe when permissions cannot be represented coherently.
- [inference; source: https://csrc.nist.gov/pubs/sp/800/207/final; https://www.rfc-editor.org/rfc/rfc8693; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html] The unresolved design problem is therefore not whether identity matters, but what an AIBOM must declare at design time so that runtime attribution and least-privilege enforcement remain reconstructable across human, agent, tool, and trust-boundary hops.

## Approach

1. **Identity taxonomy for agentic Artificial Intelligence:** define the identity types present in a multi-agent system and map them to existing standards where analogues exist.
2. **Delegation chain modelling:** model how authorization flows through a typical hierarchy: human, orchestrator, sub-agent, tool, external service.
3. **Permission scope manifest design:** propose a schema for declaring, versioning, and auditing the permission scope of each agent and tool in an AIBOM.
4. **Zero-trust application:** analyze what Zero Trust Architecture requires an AIBOM to declare for every hop.
5. **Attribution failure analysis:** document the scenarios in which identity attribution fails even with a well-formed AIBOM.

## Sources

- [x] [National Institute of Standards and Technology (NIST) Special Publication 800-207 Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)
- [x] [Internet Engineering Task Force (IETF) RFC 8693 OAuth 2.0 Token Exchange](https://www.rfc-editor.org/rfc/rfc8693)
- [x] [OpenID Foundation OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html)
- [x] [OpenID Foundation What is OpenID Connect](https://openid.net/developers/how-connect-works/)
- [x] [SPIFFE Overview](https://spiffe.io/docs/latest/spiffe-about/overview/)
- [x] [SPIFFE Concepts](https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/)
- [x] [SPIFFE Specification](https://spiffe.io/docs/latest/spiffe-specs/spiffe/)
- [x] [Microsoft Entra ID On-Behalf-Of flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-on-behalf-of-flow)
- [x] [Model Context Protocol (MCP) Authorization specification](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization/)
- [x] [David Mitchell (2026) AI agent identity and access management enterprise](https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html)
- [x] [David Mitchell (2026) Access control amplification under agentic operations](https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html)
- [x] [David Mitchell (2026) Permission-safe Retrieval-Augmented Generation in enterprise information architectures](https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html)
- [x] [David Mitchell (2026) Agentic Artificial Intelligence regulatory preconditions control failure assessment](https://davidamitchell.github.io/Research/research/2026-04-26-agentic-ai-regulatory-preconditions-control-failure-assessment.html)
- [x] [David Mitchell (2026) Application Programming Interface (API) context hubs, Retrieval-Augmented Generation (RAG), and the Model Context Protocol (MCP)](https://davidamitchell.github.io/Research/research/2026-03-18-api-context-hubs-rag-mcp.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0-5 are the investigation, and Section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: What identity objects, delegation edges, and permission-scope declarations must an Artificial Intelligence Bill of Materials (AIBOM) contain so that a reviewer can reconstruct who authorized an action across human, agent, tool, and model hops?
- Scope: Formal identity modelling, delegation semantics, permission-scope manifests, zero-trust implications, and attribution failure modes across multi-agent systems.
- Constraints: Use formal standards, cover multi-hop delegation, and build on prior completed repository work about machine identity, access amplification, and permission-safe retrieval.
- Output: knowledge.
- Prior completed items reviewed: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html ; https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html ; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html ; https://davidamitchell.github.io/Research/research/2026-04-26-agentic-ai-regulatory-preconditions-control-failure-assessment.html ; https://davidamitchell.github.io/Research/research/2026-03-18-api-context-hubs-rag-mcp.html

### §1 Question Decomposition

- **Root question:** What AIBOM identity model preserves attribution and least privilege across multi-agent execution?
  - **A. Identity taxonomy**
    - A1. Which identity classes are directly supported by current standards?
    - A2. Which identity classes are required by agentic systems even when no single standard names them directly?
  - **B. Delegation-chain semantics**
    - B1. How do OAuth 2.0 Token Exchange and Microsoft Entra On-Behalf-Of distinguish subject and actor?
    - B2. What survives inside tokens, and what must be persisted outside tokens for audit?
  - **C. Permission-scope modelling**
    - C1. What do standards expose for audience, resource, scope, and actor authorization?
    - C2. How should an AIBOM represent effective permissions at each hop?
  - **D. Zero-trust and workload identity**
    - D1. What does Zero Trust Architecture require for each session or hop?
    - D2. What does SPIFFE provide for workload identity and trust-domain crossings?
  - **E. Failure modes**
    - E1. Where do current standards stop short of full attribution?
    - E2. Which control-surface failures must an AIBOM name explicitly even if runtime platforms implement them differently?

### §2 Investigation

#### A. Identity classes that the AIBOM must represent

- [fact; source: https://csrc.nist.gov/pubs/sp/800/207/final] NIST Special Publication 800-207 says authorized subjects can include the combination of user, application or service, and device, which means the standard already treats identity as potentially composite rather than purely human or purely workload.
- [fact; source: https://openid.net/specs/openid-connect-core-1_0.html; https://openid.net/developers/how-connect-works/] OpenID Connect is defined as an identity layer on top of OAuth 2.0 for verifying the identity of the End-User, and the OpenID Foundation explains it as answering the question of the person currently using the browser or mobile app.
- [fact; source: https://spiffe.io/docs/latest/spiffe-about/overview/; https://spiffe.io/docs/latest/spiffe-specs/spiffe/] SPIFFE is a workload-identity framework that bootstraps and issues identity to services across heterogeneous environments and organizational boundaries, and its core primitives are the SPIFFE ID, the SPIFFE Verifiable Identity Document (SVID), and the Workload API.
- [fact; source: https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/] SPIFFE Concepts says an SVID contains a single SPIFFE ID representing the identity of the service presenting it, and the Workload API delivers short-lived credentials plus trust bundles for verification.
- [inference; source: https://csrc.nist.gov/pubs/sp/800/207/final; https://openid.net/specs/openid-connect-core-1_0.html; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html] An AIBOM therefore needs at least six typed identity classes: human principal, agent workload, tool or service workload, model instance, runtime or device context, and trust domain, because no single standard spans all six but current agentic systems rely on all of them.

#### B. Delegation semantics and what tokens do not preserve

- [fact; source: https://www.rfc-editor.org/rfc/rfc8693] RFC 8693 defines delegation as preserving principal A as a distinct actor representing principal B, while impersonation makes A indistinguishable from B within the rights context of the token.
- [fact; source: https://www.rfc-editor.org/rfc/rfc8693] RFC 8693 defines `subject_token` as the party on behalf of whom the request is made, `actor_token` as the acting party, the `act` claim as the representation of delegated actors, and the `may_act` claim as a statement that one party is authorized to act for another.
- [fact; source: https://www.rfc-editor.org/rfc/rfc8693] RFC 8693 permits nested `act` claims to represent a chain of delegation, but it also says prior actors in nested `act` claims are informational only and that access-control decisions must consider only the top-level claims and the current actor.
- [fact; source: https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-on-behalf-of-flow] Microsoft Entra On-Behalf-Of describes delegated token propagation for a web API using an identity other than its own to call another web API, but it says the flow only works for user principals and delegated scopes, not for app-only service principals.
- [fact; source: https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-on-behalf-of-flow] Microsoft Entra also says roles remain attached to the user principal and not to the application operating on the user's behalf, and app-only access must use the client-credentials flow instead.
- [inference; source: https://www.rfc-editor.org/rfc/rfc8693; https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-on-behalf-of-flow; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html] AIBOM delegation modelling must therefore persist the full historical chain outside the runtime token format, because standards preserve only the current authorization decision for enforcement while the complete prior chain is mainly an audit object.

#### C. Permission-scope manifests and effective rights

- [fact; source: https://www.rfc-editor.org/rfc/rfc8693] RFC 8693 says `resource`, `audience`, and `scope` describe the desired rights of the issued token, and it warns that the requested access rights are effectively the Cartesian product of requested scopes across requested target services.
- [fact; source: https://csrc.nist.gov/pubs/sp/800/207/final] NIST Special Publication 800-207 says access should be granted on a per-session basis with the least privileges needed to complete the task and that authentication and authorization are discrete functions performed before a session to an enterprise resource is established.
- [fact; source: https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization/] The Model Context Protocol Authorization specification says authorization-code grant is useful when the client is acting on behalf of a human end user, client-credentials grant is appropriate when the client is another application, and authorization must be included in every HTTP request from client to server.
- [inference; source: https://www.rfc-editor.org/rfc/rfc8693; https://csrc.nist.gov/pubs/sp/800/207/final; https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html] AIBOM permission manifests should be edge-bound, not only node-bound, and should declare at least subject, actor, target resource or audience, allowed operations or scopes, delegation mode, credential class, maximum lifetime, approval requirement, and revocation path.
- [inference; source: https://csrc.nist.gov/pubs/sp/800/207/final; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html] The effective permission set for a delegated hop should be modelled as the intersection of initiator rights, actor rights, and resource policy, because the repository's prior identity item already found that delegated permissions should narrow rather than expand.

#### D. Zero trust, workload identity, and trust-domain crossings

- [fact; source: https://csrc.nist.gov/pubs/sp/800/207/final] Zero Trust Architecture assumes no implicit trust based on network location or asset ownership and focuses on protecting resources rather than network segments.
- [fact; source: https://spiffe.io/docs/latest/spiffe-about/overview/; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/] SPIFFE provides short-lived cryptographic identity documents for workloads and trust bundles for verification, and it explicitly treats heterogeneous and cross-organizational environments as a workload-identity problem.
- [fact; source: https://spiffe.io/docs/latest/spiffe-specs/spiffe/; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/] The SPIFFE Workload API delivers SVIDs and trust bundles but does not itself define end-user delegation semantics or permission scopes; it solves identity issuance and authentication for workloads.
- [fact; source: https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization/] MCP authorization requires OAuth 2.1 style metadata discovery, secure token handling, HTTPS transport, and explicit bearer-token use on every request, and it allows either human-delegated or application-level authorization patterns.
- [inference; source: https://csrc.nist.gov/pubs/sp/800/207/final; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/; https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization/] An AIBOM that claims zero-trust compatibility must therefore declare trust domains, authentication method, attestation or identity-issuance mechanism, enforcement point, and credential-lifecycle policy for every boundary crossing, because identity labels alone do not tell a reviewer how trust is verified.

#### E. Attribution failure modes that current standards leave partially unresolved

- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html; https://davidamitchell.github.io/Research/research/2026-04-26-agentic-ai-regulatory-preconditions-control-failure-assessment.html] Prior completed repository work already showed that over-privileged delegated identities create amplified risk under automated operation, even when the formal control frameworks do not explicitly describe the amplification mechanism.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html] The completed permission-safe Retrieval-Augmented Generation item found that safe retrieval requires either correct permission metadata or live delegated identity, which means cross-domain retrieval hops are attribution-sensitive identity hops rather than mere data-access details.
- [fact; source: https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization/] MCP third-party authorization requires the server to maintain secure mapping between third-party tokens and issued MCP tokens and to manage token lifecycle explicitly, which confirms that tool-boundary token chaining is a first-class provenance problem.
- [inference; source: https://www.rfc-editor.org/rfc/rfc8693; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html; https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html] Attribution commonly fails when the system uses shared service identities, ambient runtime credentials, tool substitution that changes the downstream audience without updating scope intent, or cross-domain retrieval that cannot bind the original human subject to the current workload actor.
- [inference; source: https://www.rfc-editor.org/rfc/rfc8693; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/; https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization/] Current standards succeed at parts of the problem, user identity, delegation syntax, workload identity, or transport-level authorization, but none alone supplies the complete design-time graph needed for end-to-end attribution across agentic systems.

### §3 Reasoning

- [inference; source: https://openid.net/specs/openid-connect-core-1_0.html; https://openid.net/developers/how-connect-works/] OpenID Connect is the most directly applicable reviewed standard for identifying the human principal layer, but it is not a workload-identity model.
- [inference; source: https://www.rfc-editor.org/rfc/rfc8693] RFC 8693 is the most directly applicable reviewed standard for distinguishing delegation from impersonation and for expressing current actor state, but it intentionally limits access-control relevance to the current actor and top-level claims.
- [inference; source: https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/; https://spiffe.io/docs/latest/spiffe-specs/spiffe/] SPIFFE is the most directly applicable reviewed standard for workload identity and trust-domain verification, but it does not define end-user delegation or scope manifests.
- [inference; source: https://www.rfc-editor.org/rfc/rfc8693; https://csrc.nist.gov/pubs/sp/800/207/final; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/; https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization/] The formal AIBOM model must therefore combine identity graph, delegation graph, scope manifests, and trust-boundary metadata because the problem is structurally cross-standard.

### §4 Consistency Check

- [fact; source: https://www.rfc-editor.org/rfc/rfc8693] There is no contradiction between nested `act` claims and the need for external chain persistence, because RFC 8693 explicitly says prior actors are informational only for authorization.
- [fact; source: https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-on-behalf-of-flow; https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization/] There is no contradiction between human-delegated and application-level flows, because Microsoft Entra and MCP both distinguish user-delegated and application identities as separate authorization patterns.
- [inference; source: https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/; https://csrc.nist.gov/pubs/sp/800/207/final] The main design tension is not between standards, but between what runtime tokens optimize for current enforcement and what an AIBOM must optimize for full retrospective attribution.

### §5 Depth and Breadth Expansion

- [technical][inference; source: https://www.rfc-editor.org/rfc/rfc8693; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/] The technical implication is that identity and authorization should be represented as separate but linked objects, because SPIFFE issues identity while RFC 8693 constrains delegated rights.
- [regulatory][inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-agentic-ai-regulatory-preconditions-control-failure-assessment.html; https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html] The governance implication is that an AIBOM without explicit delegation and scope manifests would leave a board or regulator unable to tell whether agentic permissions are narrower than the permissions they amplify.
- [behavioral][inference; source: https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-on-behalf-of-flow; https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization/] The behavioral implication is that teams will otherwise fall back to convenient ambient credentials or broad maker credentials, because those patterns reduce local friction while obscuring actor distinction.
- [architectural][inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html; https://davidamitchell.github.io/Research/research/2026-03-18-api-context-hubs-rag-mcp.html] The architectural implication is that identity modelling must cover not only agent-to-tool calls but also retrieval and protocol surfaces, because context-retrieval and tool-invocation boundaries are also authorization boundaries.

### §6 Synthesis

**Executive summary:**

An AIBOM that can support end-to-end attribution in multi-agent systems should model identity as a typed graph of distinct principals and workload actors linked by explicit delegation edges and bounded permission-scope manifests, not as a flat list of components. [inference; source: https://csrc.nist.gov/pubs/sp/800/207/final; https://www.rfc-editor.org/rfc/rfc8693; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html]

RFC 8693 provides explicit formal semantics for subject, actor, delegation, and impersonation, but it does not itself preserve the whole audit-relevant chain for authorization decisions, so AIBOM must persist full delegation history as a separate design-time artifact. [inference; source: https://www.rfc-editor.org/rfc/rfc8693]

OpenID Connect and Microsoft Entra On-Behalf-Of remain useful for authenticated human delegation, while SPIFFE remains useful for workload identity and trust-domain verification, but neither layer alone captures effective permissions, trust-boundary policy, and cross-hop provenance. [inference; source: https://openid.net/specs/openid-connect-core-1_0.html; https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-on-behalf-of-flow; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/]

The practical AIBOM answer is therefore a six-part schema, identity inventory, delegation chain, permission manifests, trust-boundary crossings, credential policy, and attribution requirements, because current standards solve adjacent slices rather than the whole agentic attribution problem. [inference; source: https://www.rfc-editor.org/rfc/rfc8693; https://csrc.nist.gov/pubs/sp/800/207/final; https://spiffe.io/docs/latest/spiffe-specs/spiffe/; https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization/]

**Key findings:**

1. **An AIBOM should model human principals, agent workloads, tool or service workloads, model instances, runtime contexts, and trust domains as distinct identity classes, because current standards distribute those concepts across end-user identity, workload identity, and zero-trust subject composition rather than collapsing them into one actor type.** ([inference]; high confidence; source: https://csrc.nist.gov/pubs/sp/800/207/final; https://openid.net/specs/openid-connect-core-1_0.html; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html)
2. **RFC 8693 provides explicit concepts that AIBOM can reuse for delegation edges, including subject, actor, authorized actor, delegation, and impersonation, but AIBOM must still persist full prior-hop history separately because nested prior actors are informational only for authorization decisions.** ([inference]; medium confidence; source: https://www.rfc-editor.org/rfc/rfc8693)
3. **OpenID Connect and Microsoft Entra On-Behalf-Of are appropriate for authenticated user-delegated flows, but they do not solve app-only or autonomous multi-hop delegation, so an AIBOM must separate human-identity assertions from workload-identity assertions instead of treating them as one credential class.** ([inference]; high confidence; source: https://openid.net/specs/openid-connect-core-1_0.html; https://openid.net/developers/how-connect-works/; https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-on-behalf-of-flow)
4. **SPIFFE succeeds at issuing short-lived cryptographic workload identities and trust bundles across trust domains, but it does not define end-user delegation or permission scopes, so AIBOM must layer scope manifests and delegation semantics above workload identity rather than expecting SPIFFE alone to supply authorization meaning.** ([inference]; medium confidence; source: https://spiffe.io/docs/latest/spiffe-about/overview/; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/; https://spiffe.io/docs/latest/spiffe-specs/spiffe/)
5. **Permission scopes in an AIBOM should be represented as edge-bound manifests containing target resource or audience, allowed operations, delegation mode, credential class, maximum lifetime, approval requirement, and revocation path, because least privilege is enforced at the hop rather than by the identity label alone.** ([inference]; high confidence; source: https://www.rfc-editor.org/rfc/rfc8693; https://csrc.nist.gov/pubs/sp/800/207/final; https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html)
6. **A zero-trust-compatible AIBOM must declare trust domains, authentication method, attestation or identity-issuance mechanism, enforcement point, and credential-rotation policy for every boundary crossing, because identity inventories without verification-path metadata do not show how trust is actually established at runtime.** ([inference]; high confidence; source: https://csrc.nist.gov/pubs/sp/800/207/final; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/; https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization/)
7. **Attribution fails most predictably when systems rely on shared service identities, ambient runtime credentials, tool substitution that changes downstream audience, or cross-domain retrieval that cannot bind the original human subject to the current workload actor, so those conditions should be named explicitly in the AIBOM failure-mode register.** ([inference]; medium confidence; source: https://www.rfc-editor.org/rfc/rfc8693; https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html; https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization/)
8. **The minimal formal AIBOM schema for this problem is therefore six linked objects, `identities`, `delegations`, `permission_manifests`, `trust_boundary_crossings`, `credential_policies`, and `attribution_requirements`, because no reviewed standard independently covers all six layers needed for auditable multi-agent operation.** ([inference]; medium confidence; source: https://www.rfc-editor.org/rfc/rfc8693; https://csrc.nist.gov/pubs/sp/800/207/final; https://spiffe.io/docs/latest/spiffe-specs/spiffe/; https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] AIBOM needs six distinct identity classes rather than one flat actor type. | https://csrc.nist.gov/pubs/sp/800/207/final; https://openid.net/specs/openid-connect-core-1_0.html; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html | high | Standards divide identity across human, workload, and composite subject layers. |
| [inference] RFC 8693 provides reusable delegation concepts for AIBOM, but prior actors remain informational for authorization and therefore need separate audit persistence. | https://www.rfc-editor.org/rfc/rfc8693 | medium | Direct standard language supports the semantics; the AIBOM reuse step is the inference. |
| [inference] Human-delegated and autonomous flows require separate identity layers in AIBOM. | https://openid.net/specs/openid-connect-core-1_0.html; https://openid.net/developers/how-connect-works/; https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-on-behalf-of-flow | high | OIDC and On-Behalf-Of remain human-centered. |
| [inference] SPIFFE solves workload identity and trust verification, not end-user delegation or scope semantics. | https://spiffe.io/docs/latest/spiffe-about/overview/; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/; https://spiffe.io/docs/latest/spiffe-specs/spiffe/ | medium | Strong evidence for identity scope, weaker because the absence of authorization semantics is inferred from spec boundaries. |
| [inference] Permission scopes should be edge-bound manifests with target, operation, lifetime, and approval metadata. | https://www.rfc-editor.org/rfc/rfc8693; https://csrc.nist.gov/pubs/sp/800/207/final; https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html | high | Combines primary standards with prior repository synthesis. |
| [inference] Zero-trust-compatible AIBOMs must record verification-path metadata at each trust-boundary crossing. | https://csrc.nist.gov/pubs/sp/800/207/final; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/; https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization/ | high | All three sources require explicit verification rather than ambient trust. |
| [inference] Shared credentials, ambient runtime identity, and cross-domain retrieval are first-order attribution failure modes. | https://www.rfc-editor.org/rfc/rfc8693; https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html; https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization/ | medium | Combines standard semantics with adjacent completed-item evidence. |
| [inference] The minimal AIBOM schema requires six linked object groups. | https://www.rfc-editor.org/rfc/rfc8693; https://csrc.nist.gov/pubs/sp/800/207/final; https://spiffe.io/docs/latest/spiffe-specs/spiffe/; https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html | medium | Schema shape is synthetic rather than directly standardized. |

**Assumptions:**

- None.

**Analysis:**

The evidence was weighted toward primary standards where they named formal objects directly, which is why RFC 8693 carries more weight for delegation edges than platform guidance, and why SPIFFE carries more weight for workload identity than OpenID Connect. [inference; source: https://www.rfc-editor.org/rfc/rfc8693; https://spiffe.io/docs/latest/spiffe-specs/spiffe/; https://openid.net/specs/openid-connect-core-1_0.html]

Two rival simplifications were considered and rejected. A runtime-only alternative, storing trace logs without design-time identity manifests, was rejected because RFC 8693 makes prior actors informational only for authorization and the adjacent repository items show that missing permission representation leaves downstream evidence semantically incomplete. [inference; source: https://www.rfc-editor.org/rfc/rfc8693; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html]

The second rival, relying on stronger model quality gates or more frequent human review instead of explicit delegation and scope manifests, was rejected because those controls may reduce misuse probability but they do not create machine-verifiable actor separation or trust-boundary semantics. [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html; https://davidamitchell.github.io/Research/research/2026-04-26-agentic-ai-regulatory-preconditions-control-failure-assessment.html]

The preferred model is therefore not a new identity standard, but a schema-level composition of existing standards into one auditable graph, human identity from OpenID Connect, delegation edges from RFC 8693 style semantics, workload identity from SPIFFE or equivalent, and hop-level enforcement constraints from Zero Trust Architecture and transport-layer authorization. [inference; source: https://openid.net/specs/openid-connect-core-1_0.html; https://www.rfc-editor.org/rfc/rfc8693; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/; https://csrc.nist.gov/pubs/sp/800/207/final; https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization/]

**Risks, gaps, uncertainties:**

- No reviewed standard defines an AIBOM schema directly, so the recommended field grouping is a synthesis rather than a standards-backed canonical format. [inference; source: https://www.rfc-editor.org/rfc/rfc8693; https://csrc.nist.gov/pubs/sp/800/207/final; https://spiffe.io/docs/latest/spiffe-specs/spiffe/]
- SPIFFE documentation is explicit about identity issuance and verification but not about application-layer authorization semantics, so claims about what must be added on top of SPIFFE remain partly inferential. [inference; source: https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/; https://spiffe.io/docs/latest/spiffe-specs/spiffe/]
- Platform-specific audit coverage can still vary even when the AIBOM graph is complete, which means schema completeness does not guarantee uniform downstream telemetry quality. [inference; source: https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-on-behalf-of-flow; https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization/]

**Open questions:**

- What is the smallest interoperable serialization for nested delegation chains that preserves audit history without causing token or manifest bloat?
- How should an AIBOM identify model instances when the same logical model is accessed through multiple hosted endpoints with different trust and logging behavior?
- Which runtime trace fields are the minimum necessary companion to the design-time AIBOM so that a post-incident reviewer can bind intent, delegation, and action together without ambiguity?

### §7 Recursive Review

- Metadata: Prior-work scan completed against adjacent completed items on identity, access amplification, permission-safe retrieval, regulatory control failure, and protocol boundaries.
- Metadata: Acronym audit completed in the document body for Artificial Intelligence (AI), Artificial Intelligence Bill of Materials (AIBOM), OpenID Connect (OIDC), Retrieval-Augmented Generation (RAG), Secure Production Identity Framework for Everyone (SPIFFE), SPIFFE Verifiable Identity Document (SVID), Identity and Access Management (IAM), and Application Programming Interface (API).
- Metadata: Findings and Section 6 use the same substantive claims, confidence levels, and source sets.
- Metadata: Remaining uncertainty is concentrated in schema standardization and platform-specific audit fidelity, not in the underlying need for explicit identity, delegation, and scope objects.

---

## Findings

### Executive Summary

An AIBOM that can support end-to-end attribution in multi-agent systems should model identity as a typed graph of distinct principals and workload actors linked by explicit delegation edges and bounded permission-scope manifests, not as a flat list of components. [inference; source: https://csrc.nist.gov/pubs/sp/800/207/final; https://www.rfc-editor.org/rfc/rfc8693; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html]

RFC 8693 provides explicit formal semantics for subject, actor, delegation, and impersonation, but it does not itself preserve the whole audit-relevant chain for authorization decisions, so AIBOM must persist full delegation history as a separate design-time artifact. [inference; source: https://www.rfc-editor.org/rfc/rfc8693]

OpenID Connect and Microsoft Entra On-Behalf-Of remain useful for authenticated human delegation, while SPIFFE remains useful for workload identity and trust-domain verification, but neither layer alone captures effective permissions, trust-boundary policy, and cross-hop provenance. [inference; source: https://openid.net/specs/openid-connect-core-1_0.html; https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-on-behalf-of-flow; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/]

The practical AIBOM answer is therefore a six-part schema, identity inventory, delegation chain, permission manifests, trust-boundary crossings, credential policy, and attribution requirements, because current standards solve adjacent slices rather than the whole agentic attribution problem. [inference; source: https://www.rfc-editor.org/rfc/rfc8693; https://csrc.nist.gov/pubs/sp/800/207/final; https://spiffe.io/docs/latest/spiffe-specs/spiffe/; https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization/]

### Key Findings

1. **An AIBOM should model human principals, agent workloads, tool or service workloads, model instances, runtime contexts, and trust domains as distinct identity classes, because current standards distribute those concepts across end-user identity, workload identity, and zero-trust subject composition rather than collapsing them into one actor type.** ([inference]; high confidence; source: https://csrc.nist.gov/pubs/sp/800/207/final; https://openid.net/specs/openid-connect-core-1_0.html; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html)
2. **RFC 8693 provides explicit concepts that AIBOM can reuse for delegation edges, including subject, actor, authorized actor, delegation, and impersonation, but AIBOM must still persist full prior-hop history separately because nested prior actors are informational only for authorization decisions.** ([inference]; medium confidence; source: https://www.rfc-editor.org/rfc/rfc8693)
3. **OpenID Connect and Microsoft Entra On-Behalf-Of are appropriate for authenticated user-delegated flows, but they do not solve app-only or autonomous multi-hop delegation, so an AIBOM must separate human-identity assertions from workload-identity assertions instead of treating them as one credential class.** ([inference]; high confidence; source: https://openid.net/specs/openid-connect-core-1_0.html; https://openid.net/developers/how-connect-works/; https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-on-behalf-of-flow)
4. **SPIFFE succeeds at issuing short-lived cryptographic workload identities and trust bundles across trust domains, but it does not define end-user delegation or permission scopes, so AIBOM must layer scope manifests and delegation semantics above workload identity rather than expecting SPIFFE alone to supply authorization meaning.** ([inference]; medium confidence; source: https://spiffe.io/docs/latest/spiffe-about/overview/; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/; https://spiffe.io/docs/latest/spiffe-specs/spiffe/)
5. **Permission scopes in an AIBOM should be represented as edge-bound manifests containing target resource or audience, allowed operations, delegation mode, credential class, maximum lifetime, approval requirement, and revocation path, because least privilege is enforced at the hop rather than by the identity label alone.** ([inference]; high confidence; source: https://www.rfc-editor.org/rfc/rfc8693; https://csrc.nist.gov/pubs/sp/800/207/final; https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html)
6. **A zero-trust-compatible AIBOM must declare trust domains, authentication method, attestation or identity-issuance mechanism, enforcement point, and credential-rotation policy for every boundary crossing, because identity inventories without verification-path metadata do not show how trust is actually established at runtime.** ([inference]; high confidence; source: https://csrc.nist.gov/pubs/sp/800/207/final; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/; https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization/)
7. **Attribution fails most predictably when systems rely on shared service identities, ambient runtime credentials, tool substitution that changes downstream audience, or cross-domain retrieval that cannot bind the original human subject to the current workload actor, so those conditions should be named explicitly in the AIBOM failure-mode register.** ([inference]; medium confidence; source: https://www.rfc-editor.org/rfc/rfc8693; https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html; https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization/)
8. **The minimal formal AIBOM schema for this problem is therefore six linked objects, `identities`, `delegations`, `permission_manifests`, `trust_boundary_crossings`, `credential_policies`, and `attribution_requirements`, because no reviewed standard independently covers all six layers needed for auditable multi-agent operation.** ([inference]; medium confidence; source: https://www.rfc-editor.org/rfc/rfc8693; https://csrc.nist.gov/pubs/sp/800/207/final; https://spiffe.io/docs/latest/spiffe-specs/spiffe/; https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] AIBOM needs six distinct identity classes rather than one flat actor type. | https://csrc.nist.gov/pubs/sp/800/207/final; https://openid.net/specs/openid-connect-core-1_0.html; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html | high | Standards divide identity across human, workload, and composite subject layers. |
| [inference] RFC 8693 provides reusable delegation concepts for AIBOM, but prior actors remain informational for authorization and therefore need separate audit persistence. | https://www.rfc-editor.org/rfc/rfc8693 | medium | Direct standard language supports the semantics; the AIBOM reuse step is the inference. |
| [inference] Human-delegated and autonomous flows require separate identity layers in AIBOM. | https://openid.net/specs/openid-connect-core-1_0.html; https://openid.net/developers/how-connect-works/; https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-on-behalf-of-flow | high | OIDC and OBO remain human-centered. |
| [inference] SPIFFE solves workload identity and trust verification, not end-user delegation or scope semantics. | https://spiffe.io/docs/latest/spiffe-about/overview/; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/; https://spiffe.io/docs/latest/spiffe-specs/spiffe/ | medium | Strong evidence for identity scope, weaker because the absence of authorization semantics is inferred from spec boundaries. |
| [inference] Permission scopes should be edge-bound manifests with target, operation, lifetime, and approval metadata. | https://www.rfc-editor.org/rfc/rfc8693; https://csrc.nist.gov/pubs/sp/800/207/final; https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html | high | Combines primary standards with prior repository synthesis. |
| [inference] Zero-trust-compatible AIBOMs must record verification-path metadata at each trust-boundary crossing. | https://csrc.nist.gov/pubs/sp/800/207/final; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/; https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization/ | high | All three sources require explicit verification rather than ambient trust. |
| [inference] Shared credentials, ambient runtime identity, and cross-domain retrieval are first-order attribution failure modes. | https://www.rfc-editor.org/rfc/rfc8693; https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html; https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization/ | medium | Combines standard semantics with adjacent completed-item evidence. |
| [inference] The minimal AIBOM schema requires six linked object groups. | https://www.rfc-editor.org/rfc/rfc8693; https://csrc.nist.gov/pubs/sp/800/207/final; https://spiffe.io/docs/latest/spiffe-specs/spiffe/; https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html | medium | Schema shape is synthetic rather than directly standardized. |

### Assumptions

- None.

### Analysis

The evidence was weighted toward primary standards where they named formal objects directly, which is why RFC 8693 carries more weight for delegation edges than platform guidance, and why SPIFFE carries more weight for workload identity than OpenID Connect. [inference; source: https://www.rfc-editor.org/rfc/rfc8693; https://spiffe.io/docs/latest/spiffe-specs/spiffe/; https://openid.net/specs/openid-connect-core-1_0.html]

Two rival simplifications were considered and rejected. A runtime-only alternative, storing trace logs without design-time identity manifests, was rejected because RFC 8693 makes prior actors informational only for authorization and the adjacent repository items show that missing permission representation leaves downstream evidence semantically incomplete. [inference; source: https://www.rfc-editor.org/rfc/rfc8693; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html]

The second rival, relying on stronger model quality gates or more frequent human review instead of explicit delegation and scope manifests, was rejected because those controls may reduce misuse probability but they do not create machine-verifiable actor separation or trust-boundary semantics. [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html; https://davidamitchell.github.io/Research/research/2026-04-26-agentic-ai-regulatory-preconditions-control-failure-assessment.html]

The preferred model is therefore not a new identity standard, but a schema-level composition of existing standards into one auditable graph, human identity from OpenID Connect, delegation edges from RFC 8693 style semantics, workload identity from SPIFFE or equivalent, and hop-level enforcement constraints from Zero Trust Architecture and transport-layer authorization. [inference; source: https://openid.net/specs/openid-connect-core-1_0.html; https://www.rfc-editor.org/rfc/rfc8693; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/; https://csrc.nist.gov/pubs/sp/800/207/final; https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization/]

### Risks, Gaps, and Uncertainties

- No reviewed standard defines an AIBOM schema directly, so the recommended field grouping is a synthesis rather than a standards-backed canonical format. [inference; source: https://www.rfc-editor.org/rfc/rfc8693; https://csrc.nist.gov/pubs/sp/800/207/final; https://spiffe.io/docs/latest/spiffe-specs/spiffe/]
- SPIFFE documentation is explicit about identity issuance and verification but not about application-layer authorization semantics, so claims about what must be added on top of SPIFFE remain partly inferential. [inference; source: https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/; https://spiffe.io/docs/latest/spiffe-specs/spiffe/]
- Platform-specific audit coverage can still vary even when the AIBOM graph is complete, which means schema completeness does not guarantee uniform downstream telemetry quality. [inference; source: https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-on-behalf-of-flow; https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization/]

### Open Questions

- What is the smallest interoperable serialization for nested delegation chains that preserves audit history without causing token or manifest bloat?
- How should an AIBOM identify model instances when the same logical model is accessed through multiple hosted endpoints with different trust and logging behavior?
- Which runtime trace fields are the minimum necessary companion to the design-time AIBOM so that a post-incident reviewer can bind intent, delegation, and action together without ambiguity?

---

## Output

- Type: knowledge
- Description: A formal AIBOM identity model should combine typed identity inventory, explicit delegation edges, edge-bound permission manifests, trust-boundary metadata, credential policy, and attribution requirements so that multi-agent authorization remains reconstructable across human, workload, and tool hops. [inference; source: https://www.rfc-editor.org/rfc/rfc8693; https://csrc.nist.gov/pubs/sp/800/207/final; https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/]
- Links:
  - https://www.rfc-editor.org/rfc/rfc8693
  - https://csrc.nist.gov/pubs/sp/800/207/final
  - https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/
