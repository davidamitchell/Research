---
title: "Permission-safe Retrieval-Augmented Generation (RAG) in enterprise information architectures: technical constraints, architectural options, and failure modes at scale"
added: 2026-04-26T06:57:01+00:00
status: backlog
priority: high
blocks: [2026-04-26-agentic-ai-foundational-conditions-dependency-ordering]
tags: [rag, access-control, information-architecture, embedding-inference, enterprise-ai, regulated-banking, agentic-ai]
started: ~
completed: ~
output: [knowledge]
---

# Permission-safe Retrieval-Augmented Generation (RAG) in enterprise information architectures: technical constraints, architectural options, and failure modes at scale

## Research Question

What are the technical constraints on permission-safe Retrieval-Augmented Generation (RAG) in an enterprise information architecture with incoherent access controls — collaboration groups created ad hoc, document-store Access Control Lists (ACLs) unaudited, file-level sharing at individual discretion — and what are the architectural options (per-user token delegation, per-security-boundary index partitioning, ACL metadata filtering) with their respective failure modes at enterprise scale, including the embedding inference problem and the permission-change propagation problem?

## Scope

**In scope:**
- Why an incoherent enterprise permission model is a technical blocker for RAG, not merely a governance risk
- The embedding inference problem: whether dense vector embedding models leak information about documents the querying user cannot access through retrieval space geometry regardless of query-time ACL filtering, and what evidence exists from the research literature
- The three main architectural options for permission-safe RAG: per-user token delegation, per-security-boundary index partitioning, and ACL metadata filtering
- Failure modes of each architectural option at enterprise scale, including storage and compute implications of per-user ingestion
- The permission-change propagation problem: how promptly and correctly each architecture responds when user permissions change
- Whether correct query-time ACL filtering is necessary but not sufficient for permission safety, and under what conditions
- Applicable enterprise information architectures: Microsoft 365 and SharePoint Online, Azure AI Search, AWS Bedrock Knowledge Bases
- Relevant academic and technical literature on RAG security and enterprise knowledge retrieval

**Out of scope:**
- General RAG architecture without the permission-safety dimension
- Model safety, hallucination, or output quality issues unrelated to access control
- Cross-tenant data isolation (focus is on per-user isolation within a single tenant)
- The dependency ordering problem (covered by the companion synthesis item)

**Constraints:**
- Distinguish between what can be claimed as a published empirical result versus what is an inference from retrieval-space geometry first principles
- Assess architectural options against a Microsoft 365 / SharePoint Online / Azure AI Search context as the primary use case, with AWS Bedrock as a secondary case
- Sources must be assessable for applicability to a regulated financial institution operating at enterprise scale

## Context

Prior completed research established that governed knowledge curation is a prerequisite for enterprise AI capability in regulated institutions ([Knowledge curation governance as an enterprise AI capability in regulated financial institutions](https://davidamitchell.github.io/Research/research/2026-04-22-knowledge-curation-governance-for-regulated-ai.html)), and that regulatory and standards frameworks require data classification and controlled access before deploying agentic AI ([Regulatory and standards preconditions for deployment of agentic AI systems](https://davidamitchell.github.io/Research/research/2026-04-26-agentic-ai-regulatory-preconditions-control-failure-assessment.html)). The missing piece is the specific technical mechanism by which an incoherent permission model is not merely a governance risk but a technical blocker for safe RAG deployment — and what the architecture options look like when that constraint is taken seriously.

The framing motivation is that an organisation deploying RAG over its enterprise knowledge base while ACLs remain unaudited is not just making a governance choice; it may be making a mathematically indefensible one if embedding models leak permission-relevant information through retrieval space geometry. This question anchors the access-control layer of the broader dependency ordering problem.

## Approach

1. **Establish the technical blocker claim:** Review the literature and vendor documentation on whether RAG access control implementations can correctly enforce permissions they cannot characterise — i.e., whether an incoherent ACL model is a technical precondition failure, not a governance preference.
2. **Investigate the embedding inference problem:** Search the research literature for evidence on whether dense vector embedding models leak information about documents the querying user cannot access through retrieval space geometry; assess whether query-time ACL filtering is sufficient or merely necessary.
3. **Architectural options survey:** For each of the three main options (per-user token delegation, per-security-boundary index partitioning, ACL metadata filtering), describe the mechanism, the security model, the implementation complexity, and the known failure modes.
4. **Scale failure modes:** Assess storage and compute implications of per-user ingestion and per-security-boundary partitioning at enterprise scale (thousands of users, millions of documents, frequent permission changes).
5. **Permission-change propagation:** For each architectural option, assess how the architecture handles permission changes — user added to a group, document reclassified, ACL modified — and what the window of vulnerability is.
6. **Platform-specific assessment:** Assess how Microsoft Azure AI Search (Semantic Ranking, index-level security filtering), AWS Bedrock Knowledge Bases (metadata filtering), and SharePoint Online (permission inheritance) handle each of these problems.
7. **Synthesis:** Produce a decision framework characterising when each architectural option is appropriate and what minimum information architecture preconditions must be satisfied before any RAG deployment is permission-safe.

## Sources

- [ ] [Microsoft Azure AI Search — security filtering for multi-tenant search](https://learn.microsoft.com/en-us/azure/search/search-security-trimming-for-azure-search) — Microsoft documentation on security trimming; primary source for the ACL metadata filtering approach
- [ ] [Microsoft Azure AI Search — security and access controls overview](https://learn.microsoft.com/en-us/azure/search/search-security-overview) — overview of index-level and document-level security models in Azure AI Search
- [ ] [AWS Bedrock Knowledge Bases — security and access control](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-permissions.html) — AWS documentation for Bedrock Knowledge Bases permission model
- [ ] [SharePoint Online — permission inheritance and sharing model](https://learn.microsoft.com/en-us/sharepoint/understanding-permission-levels) — Microsoft documentation on the SharePoint Online permission model that underpins M365 RAG data sources
- [ ] https://arxiv.org/abs/2309.11495 — research on embedding privacy; assess for evidence on whether embedding models leak membership or permission-relevant information
- [ ] https://arxiv.org/abs/2401.05566 — RAG security survey; assess for coverage of access control architectures and known failure modes

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

### Key Findings

1.
2.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

- **Assumption:** ... **Justification:** ...

### Analysis

### Risks, Gaps, and Uncertainties

-

### Open Questions

-

---

## Output

*(Fill in when completing — what was produced as a result of this research?)*

- Type: knowledge
- Description:
- Links:
