---
title: "How do OAuth 2.0, OpenID Connect, and SPIFFE token propagation work in real multi-agent pipelines — and where does end-to-end attribution break in practice?"
added: 2026-05-06T08:52:41+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: medium  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [agentic-ai, identity, security, access-control, delegation, attribution, llm, governance]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
cites: [2026-05-06-aibom-identity-delegation-trust-theory, 2026-04-26-ai-agent-identity-access-management-enterprise, 2026-04-26-access-control-amplification-agentic-operations]
related: [2026-05-06-aibom-identity-delegation-trust-theory, 2026-05-06-aibom-platform-observability-control-comparison, 2026-05-06-aibom-effectiveness-risk-mitigation-limits, 2026-04-26-ai-agent-identity-access-management-enterprise]
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# How do OAuth 2.0, OpenID Connect, and SPIFFE token propagation work in real multi-agent pipelines — and where does end-to-end attribution break in practice?

## Research Question

How do OAuth 2.0 (Open Authorisation), OpenID Connect (OIDC), and SPIFFE (Secure Production Identity Framework for Everyone) token propagation mechanisms work in real multi-agent AI pipelines — and where does end-to-end attribution break in practice, specifically across agent-to-agent delegation, agent-to-tool handoffs, and cross-system boundary crossings?

## Scope

**In scope:**
- Practical token propagation patterns for multi-agent systems using OAuth 2.0 on-behalf-of (OBO) flows, OIDC identity tokens, and SPIFFE Verifiable Identity Documents (SVIDs)
- Model Context Protocol (MCP) authorisation in practice: how MCP server-client identity and permission propagation works in real deployments
- Real-world examples of attribution working and failing in documented multi-agent compositions (AWS Bedrock multi-agent, LangGraph multi-agent, AutoGen, CrewAI)
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
- Must build explicitly on the theoretical model from `2026-05-06-aibom-identity-delegation-trust-theory` and the enterprise IAM findings from `2026-04-26-ai-agent-identity-access-management-enterprise`

## Context

The theoretical identity and trust model in `2026-05-06-aibom-identity-delegation-trust-theory` defines what an AIBOM should declare about identity and delegation. This practice item asks: given real platform capabilities, how close can you get to that ideal? In practice, multi-agent pipelines routinely encounter attribution gaps: an LLM (Large Language Model) orchestrator calls a tool using a shared service account, a sub-agent inherits an overly broad token from its parent, or a cross-domain API call loses the original user context entirely. Understanding exactly where these breakpoints occur — and which are addressable with OAuth OBO flows, SPIFFE SVIDs, or structured logging — is essential for producing actionable AIBOM recommendations. Prior research in `2026-04-26-ai-agent-identity-access-management-enterprise` established the IAM requirements; this item identifies the practical gap between requirements and current platform reality.

## Approach

1. **Token propagation patterns — OAuth 2.0 OBO:** Document the OAuth 2.0 on-behalf-of flow mechanics and map them to a multi-agent pipeline: user authenticates → orchestrator receives delegated token → sub-agent inherits token → tool called on sub-agent's behalf. Identify where token scope shrinks or is lost.

2. **Token propagation patterns — SPIFFE/SPIRE:** Document how SPIFFE Verifiable Identity Documents (SVIDs) can be used for workload-to-workload identity in multi-agent pipelines. Compare against OAuth OBO in terms of what each mechanism can and cannot express about delegation provenance.

3. **Model Context Protocol (MCP) authorisation in practice:** Document the current MCP authorisation specification and its OAuth 2.0 integration. Assess whether MCP-based tool calls carry adequate attribution metadata for AIBOM purposes.

4. **Attribution failure case study:** Document at least two concrete attribution failure scenarios from real multi-agent frameworks (e.g. CrewAI agent calling a tool with a shared API key, Bedrock multi-agent collaboration losing original user context). Map each failure to the delegation chain model from `2026-05-06-aibom-identity-delegation-trust-theory`.

5. **Compensating controls and remediation:** For each documented failure scenario, assess available compensating controls: structured audit log enrichment, token binding requirements, agent attestation receipts, or MCP authorisation extension proposals. Determine which are achievable today vs. requiring new tooling or standards work.

## Sources

- [ ] [OAuth 2.0 Token Exchange (RFC 8693)](https://www.rfc-editor.org/rfc/rfc8693) — Internet Engineering Task Force (IETF) standard for token exchange and delegation; the primary mechanism for OAuth-based multi-agent delegation
- [ ] [Microsoft Entra ID — On-Behalf-Of Flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-on-behalf-of-flow) — Microsoft documentation for OAuth 2.0 OBO flow; primary practical reference for multi-agent token propagation in Azure/Microsoft ecosystems
- [ ] [Model Context Protocol (MCP) Specification — Authorisation](https://spec.modelcontextprotocol.io/specification/2025-03-26/basic/authorization/) — Anthropic Model Context Protocol (MCP) authorisation specification; emerging standard for agent-to-tool permission propagation
- [ ] [SPIFFE/SPIRE Documentation](https://spiffe.io/docs/latest/spiffe-about/overview/) — SPIFFE/SPIRE specification; workload identity standard applicable to agent-to-agent and agent-to-tool identity in multi-agent pipelines
- [ ] [CrewAI Documentation — Multi-Agent Flows](https://docs.crewai.com/) — CrewAI framework documentation; practical reference for multi-agent delegation patterns and their identity implications
- [ ] [AWS Bedrock — Multi-Agent Collaboration](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html) — AWS Bedrock multi-agent collaboration documentation; primary source for attribution patterns in a managed multi-agent Runtime Environment (RTE)
- [ ] [OWASP Top 10 for Large Language Model Applications — Excessive Agency and Privilege Escalation](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — OWASP LLM Top 10; documents privilege escalation attack patterns directly relevant to attribution failure analysis
- [ ] [AutoGen Documentation — Multi-Agent Conversations](https://microsoft.github.io/autogen/) — Microsoft AutoGen multi-agent framework documentation; second framework reference for attribution failure case study

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
