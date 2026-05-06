---
title: "How should identity, delegation chains, and permission scopes be formally modelled in an AI Bill of Materials (AIBOM) to enable end-to-end attribution across agentic AI systems?"
added: 2026-05-06T08:52:41+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: [2026-05-06-aibom-identity-attribution-multiagent-practice]  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [agentic-ai, identity, security, governance, access-control, delegation, attribution, llm]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
cites: [2026-05-06-aibom-sbom-conceptual-gaps-theory, 2026-04-26-ai-agent-identity-access-management-enterprise, 2026-04-26-agentic-ai-regulatory-preconditions-control-failure-assessment]
related: [2026-05-06-aibom-sbom-conceptual-gaps-theory, 2026-05-06-aibom-identity-attribution-multiagent-practice, 2026-05-06-aibom-effectiveness-risk-mitigation-limits, 2026-04-26-ai-agent-identity-access-management-enterprise]
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# How should identity, delegation chains, and permission scopes be formally modelled in an AI Bill of Materials (AIBOM) to enable end-to-end attribution across agentic AI systems?

## Research Question

How should identity, delegation, and permission scopes be formally represented in an AI Bill of Materials (AIBOM) schema to enable end-to-end attribution — "who authorised what" — across multi-agent compositions involving human users, orchestrator agents, sub-agents, tools, and models, and where do current identity standards (OAuth 2.0, OpenID Connect (OIDC), SPIFFE) succeed or fail when applied to agentic delegation chains?

## Scope

**In scope:**
- Formal modelling of agentic identity types: human user, orchestrator agent, sub-agent, tool/function, model instance, and ambient execution context
- Delegation chain representation: how an authorisation granted by a human user propagates through an orchestrator to sub-agents and tools, and how AIBOM should capture this chain
- Permission scope manifests: how the set of authorised operations for each identity should be declared and versioned in AIBOM
- Zero-trust principles applied to agentic flows: treating every agent-to-tool and agent-to-agent call as an unauthenticated request requiring verification
- Analysis of OAuth 2.0 and OIDC delegation (token propagation, on-behalf-of flows) and their adequacy for agentic multi-hop delegation
- Impersonation and privilege escalation attack vectors in delegation chains
- Cross-system boundary crossings: when an agent calls an external tool or Retrieval-Augmented Generation (RAG) source outside its original trust domain

**Out of scope:**
- Platform-specific identity implementation (covered in `2026-05-06-aibom-identity-attribution-multiagent-practice`)
- Runtime trace capture mechanisms (covered in `2026-05-06-aibom-runtime-generation-divergence-theory`)
- Specific enterprise Identity and Access Management (IAM) product evaluations

**Constraints:**
- Must engage with at least two formal identity standards (OAuth 2.0, OIDC, SPIFFE/SPIRE, or NIST SP 800-207 Zero Trust Architecture)
- Must address multi-agent compositions, not only single-agent scenarios
- Must build explicitly on findings from `2026-04-26-ai-agent-identity-access-management-enterprise`

## Context

Identity and attribution are the hardest unsolved problems in agentic AI security. When an agent acts on behalf of a user, calls another agent, and that sub-agent calls a tool that writes to a database, the audit trail of "who authorised this write" becomes extremely difficult to reconstruct. Traditional Privileged Access Management (PAM) and IAM assume bounded, human-initiated sessions; agentic systems operate in chains that can span systems, organisations, and time horizons without continuous human involvement. Prior research (`2026-04-26-ai-agent-identity-access-management-enterprise`) established what IAM capabilities are needed for enterprise AI agents; this item extends that work to ask how the identity and delegation model should be represented in an AIBOM — i.e., what an AIBOM needs to declare at design time about identity and permission scopes so that runtime attribution becomes possible and auditable.

## Approach

1. **Identity taxonomy for agentic AI:** Define and formalise the identity types present in a multi-agent system. Distinguish between principals (who initiates an action), delegates (who acts on behalf of a principal), and execution contexts (ambient identity attached to an agent runtime). Map to existing standards where analogues exist.

2. **Delegation chain modelling:** Model how authorisation flows through a typical multi-agent hierarchy: human → orchestrator → sub-agent → tool → external API. Identify points where the delegation chain can be broken, forged, or expanded beyond original intent.

3. **Permission scope manifest design:** Propose a schema for declaring, versioning, and auditing the permission scope of each agent and tool in an AIBOM. Evaluate whether OAuth 2.0 scopes, SPIFFE Verifiable Identity Documents (SVID), or a custom schema is most appropriate.

4. **Zero-trust application:** Analyse what zero-trust architecture principles (never trust, always verify; least-privilege; assume breach) require of an AIBOM's identity model — specifically, what the AIBOM must declare to enable a zero-trust enforcement layer.

5. **Attribution failure analysis:** Document the scenarios in which identity attribution fails even with a well-formed AIBOM: emergent agent behaviour, implicit delegation, tool substitution, and cross-trust-domain boundary crossings.

## Sources

- [ ] [National Institute of Standards and Technology (NIST) Special Publication 800-207: Zero Trust Architecture](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf) — definitive NIST specification for zero-trust architecture; framework for applying zero-trust to agentic delegation chains
- [ ] [OAuth 2.0 Token Exchange (RFC 8693)](https://www.rfc-editor.org/rfc/rfc8693) — Internet Engineering Task Force (IETF) standard for delegation and impersonation token flows; most relevant OAuth mechanism for agentic delegation chains
- [ ] [SPIFFE/SPIRE Specification](https://spiffe.io/docs/latest/spiffe-about/overview/) — Secure Production Identity Framework for Everyone (SPIFFE); workload identity standard with direct applicability to agent-to-agent identity
- [ ] [OpenID Connect Core Specification](https://openid.net/specs/openid-connect-core-1_0.html) — OpenID Connect (OIDC) specification; basis for user identity federation and on-behalf-of flows in agentic systems
- [ ] [Wietse Venema et al. (2023) OAuth 2.0 for Agentic Workflows](https://oauth.net/2/grant-types/) — OAuth grant type reference; needed to understand which OAuth flows apply to agentic delegation
- [ ] [Microsoft Entra ID — On-Behalf-Of Flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-on-behalf-of-flow) — Microsoft documentation for the OAuth 2.0 on-behalf-of (OBO) flow used in multi-tier agentic applications; practical reference
- [ ] [Model Context Protocol (MCP) Specification — Authorisation](https://spec.modelcontextprotocol.io/specification/2025-03-26/basic/authorization/) — Anthropic's Model Context Protocol (MCP) specification section on authorisation; emerging standard for agent-to-tool identity and permission propagation
- [ ] [OWASP Top 10 for Large Language Model Applications — Excessive Agency](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — OWASP LLM Top 10 including excessive agency and privilege escalation patterns directly relevant to delegation chain security

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

Restate the research question. Confirm scope, constraints, and output format.

-

### §1 Question Decomposition

Approach sub-questions broken into atomic questions — each answerable with a single evidence-based claim.

-

### §2 Investigation

Evidence gathered per atomic question. Label each claim: **[fact]**, **[inference]**, or **[assumption]** with source.

-

### §3 Reasoning

Facts, inferences, and assumptions explicitly separated. No unsupported generalisations or narrative leaps.

-

### §4 Consistency Check

Internal contradictions identified and resolved (or explicitly flagged where unresolvable).

-

### §5 Depth and Breadth Expansion

Findings re-examined through relevant lenses (technical, regulatory, economic, historical, behavioural).

-

### §6 Synthesis

*(This section seeds the Findings below.)*

**Executive summary:**

**Key findings:**

**Evidence map:**

**Assumptions:**

**Analysis:**

**Risks, gaps, uncertainties:**

**Open questions:**

### §7 Recursive Review

Final pass: every section justified, all threads synthesised, every claim sourced or labelled, all uncertainties explicit.

-

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

3–5 sentences. What is the answer to the research question? State the key conclusion directly. Write plain prose — no prefix labels. Bind sources as trailing inline citations: `Claim text. [inference; source: https://url]`

### Key Findings

Ordered list. Each finding is a specific, evidence-backed claim with confidence and source as a trailing parenthetical. Use **suffix style** — source at the end of the claim, not at the beginning.

1. **Claim text as a complete sentence.** (high confidence; source: https://url)
2. **Claim text as a complete sentence.** (medium confidence; source: https://url1; https://url2)

Source URLs must exactly match URLs in the `## Sources` section so the generated site can render `Author (Year)` citation links. List the primary source URL(s) from `## Sources` here.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

Explicit assumptions made during the investigation and the justification for each.

- **Assumption:** ... **Justification:** ...

### Analysis

How the evidence was weighed, what trade-offs were identified, and how competing interpretations were resolved.

### Risks, Gaps, and Uncertainties

What is still unknown? Where does the evidence fall short? What could change the conclusion?

-

### Open Questions

Questions that surfaced during research but are out of scope for this item. Each may become a new backlog item.

-

---

## Output

*(Fill in when completing — what was produced as a result of this research?)*

- Type: # skill | tool | agent | knowledge | backlog-item
- Description:
- Links:
