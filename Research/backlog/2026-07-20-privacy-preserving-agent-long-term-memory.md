---
title: "Privacy-preserving long-term memory for Artificial Intelligence agents"
added: 2026-07-20T09:07:23+00:00
status: backlog
priority: high
blocks: []
themes: [agentic-ai, memory-context, security-risk, governance-policy]
started: ~
completed: ~
output: []
cites: [2026-03-02-agent-memory-management-context-injection, 2026-03-17-ai-memory-systems-rag-neuroscience, 2026-04-22-knowledge-curation-governance-for-regulated-ai, 2026-05-06-aibom-effectiveness-risk-mitigation-limits]
related: [2026-07-20-agent-memory-forgetting-information-curation, 2026-07-20-hybrid-agent-memory-symbolic-connectionist-synchronisation, 2026-07-20-agent-memory-evaluation-framework, 2026-04-26-permission-safe-rag-enterprise-information-architecture]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Privacy-preserving long-term memory for Artificial Intelligence agents

## Research Question

How can Artificial Intelligence (AI) agents preserve the utility of long-term memory for personalisation and historical context while enforcing privacy, security, and data-sovereignty controls strong enough to prevent sensitive-data leakage, unsafe recall, or non-compliant retention?

## Scope

**In scope:**
- Memory scoping, access control, retention, deletion, redaction, encryption, auditability, and user or operator override mechanisms for persistent agent memory
- How privacy and security constraints differ across episodic traces, semantic summaries, profile facts, and shared organisational knowledge
- Product and architecture patterns for safe recall, memory editing, portability, and separation between private and shared memory surfaces
- Threat models directly tied to persistent memory: leakage through retrieval, over-broad recall, unsafe tool exposure, and retention of regulated or sensitive data
- Practical trade-offs between utility, convenience, governance, and data-minimisation in production agent systems

**Out of scope:**
- General model-safety topics unrelated to long-term memory persistence
- Detailed legal advice for any one jurisdiction beyond extracting design-relevant privacy and security principles
- Purely transient session context that is never persisted beyond the active interaction

**Constraints:** Use public 2024-2026 sources with implementation detail where possible. Distinguish between official product documentation, advocacy or policy analysis, and vendor marketing claims, because privacy assurances vary widely by source type.

## Context

The repository's prior memory work repeatedly identified governance and portability as unresolved risks: persistent memory is valuable precisely because it survives across sessions, but that also makes it a durable attack and compliance surface. This item focuses the cross-cutting question that sits underneath every long-term-memory design choice in the cluster: how to keep the benefit of continuity without creating a sensitive-data trap or an unsafe recall channel.

## Approach

1. Map the main privacy and security control surfaces for persistent memory: collection, storage, retrieval, sharing, editing, and deletion.
2. Compare official user-control and retention models across major memory-enabled products and open architectures.
3. Identify memory-specific threat models such as prompt-injected recall, cross-tenant leakage, stale sensitive facts, and over-broad graph traversal.
4. Examine architectural mitigations: scoped namespaces, encryption, redaction, policy-gated retrieval, provenance-aware sharing, and explicit forgetting.
5. Produce design guidance for long-term memory systems that balances utility with privacy-preserving and security-preserving constraints.

## Sources

- [ ] [New America / Open Technology Institute — AI Agents and Memory: Privacy and Power in MCP](https://www.newamerica.org/oti/briefs/ai-agents-and-memory/) — policy analysis of persistent memory risks and portability concerns
- [ ] [GitHub Docs — Copilot Memory](https://docs.github.com/en/copilot/concepts/agents/copilot-memory) — repository-scoped memory controls, citations, and retention behaviour
- [ ] [OpenAI Help — Memory in ChatGPT](https://help.openai.com/en/articles/8590148-memory-in-chatgpt-remembering-what-you-chat-about) — user controls for personal memory and temporary chats
- [ ] [Google Gemini support — Personal Intelligence](https://support.google.com/gemini?p=mk_pi) — connected-app and personal-context controls
- [ ] [Amazon Web Services Security Blog — The Agentic AI Security Scoping Matrix](https://aws.amazon.com/blogs/security/the-agentic-ai-security-scoping-matrix-a-framework-for-securing-autonomous-ai-systems/) — security control framing for agent autonomy and memory operations
- [ ] [Mem0 research](https://mem0.ai/research) — open-system claims on scoped memory and enterprise governance features
- [ ] [Mitchell (2026) Knowledge curation governance as an enterprise AI capability in regulated financial institutions](https://davidamitchell.github.io/Research/research/2026-04-22-knowledge-curation-governance-for-regulated-ai.html) — prior corpus baseline on governance, audit, and correction loops


## Related

- [Mitchell (2026) Agent Memory Management and Context Injection](https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html)
- [Mitchell (2026) Knowledge curation governance as an enterprise AI capability in regulated financial institutions](https://davidamitchell.github.io/Research/research/2026-04-22-knowledge-curation-governance-for-regulated-ai.html)
- [Mitchell (2026) Permission-safe Retrieval-Augmented Generation in enterprise information architectures: technical constraints, architectural options, and failure modes at scale](https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html)

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

-

### §1 Question Decomposition

-

### §2 Investigation

-

### §3 Reasoning

-

### §4 Consistency Check

-

### §5 Depth and Breadth Expansion

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

-

### Open Questions

-

---

## Output

*(Fill in when completing — what was produced as a result of this research?)*

- Type: # skill | tool | agent | knowledge | backlog-item
- Description:
- Links:
