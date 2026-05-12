---
title: "When Retrieval-Augmented Generation source documents change after agent build and test, what failure modes and behavioral regressions arise, and what dependency and change management practices exist to detect, govern, and mitigate them?"
added: 2026-05-12T11:03:22+00:00
status: backlog
priority: high
blocks: []
tags: [agentic-ai, rag, llm, evaluation, context-engineering, governance, dependency-mapping]
started: ~
completed: ~
output: []
cites:
  - 2026-05-12-knowledge-graph-agentic-runtime-dependency
  - 2026-04-29-knowledge-scaffolding-context-engineering
  - 2026-03-21-dependency-mapping-dotnet-terraform-dynatrace
related:
  - 2026-05-12-knowledge-graph-agentic-runtime-dependency
  - 2026-05-12-knowledge-graph-lifecycle-management-agentic
  - 2026-04-29-knowledge-scaffolding-context-engineering
  - 2026-05-06-aibom-runtime-generation-divergence-theory
  - 2026-05-06-aibom-declared-construction-practice
  - 2026-03-08-servicenow-ai-knowledge-rag-agents
  - 2026-04-27-servicenow-orchestration-agentic-ai-roadmap
  - 2026-03-21-dependency-mapping-dotnet-terraform-dynatrace
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# When Retrieval-Augmented Generation source documents change after agent build and test, what failure modes and behavioral regressions arise, and what dependency and change management practices exist to detect, govern, and mitigate them?

## Research Question

When the source documents indexed in a Retrieval-Augmented Generation (RAG) pipeline change after an agent has been built and tested, what failure modes and behavioral regressions can result in production, and what practices — covering document versioning, behavioral baseline testing, CMDB-style dependency registration of agent-to-document relationships, and ITIL-inspired change management governance — exist to detect, govern, and mitigate these regressions?

## Scope

**In scope:**
- Mechanism by which source-document changes propagate into agent context windows at inference time
- Taxonomy of document change types (wording, factual update, structural change, deletion) and their likelihood of altering retrieved context
- Documented failure modes and behavioral regression categories when RAG source documents change post-deployment
- Evaluation and testing frameworks that support behavioral baselines over document-corpus versions (e.g., Ragas, TruLens, LangSmith)
- Regression-testing patterns applicable to RAG-dependent agents: golden-set evaluations, invariant checking, output comparison
- Document versioning and corpus management approaches: snapshot indices, version-pinned retrieval, change-gated pipeline promotion
- Deployment governance patterns for controlled document-corpus rollouts: canary updates, staged index promotion, review gates
- How software engineering concepts (semantic versioning, contract testing, dependency management) translate to document corpora as dependencies
- **Dependency registration and discovery**: whether and how Configuration Management Database (CMDB) or service-registry patterns can formally record the relationship between a deployed agent and the specific document corpus (or corpus version) it depends on, so that impact of a document change can be assessed before propagation
- **Change management governance**: how Information Technology Infrastructure Library (ITIL) change management concepts — change advisory boards, impact assessment, rollback plans, and authorised change gates — apply to document-corpus updates when those documents are runtime dependencies for production agents; and how platforms such as ServiceNow already surface dependency maps that could be extended to cover agent-to-knowledge-base linkages

**Out of scope:**
- Knowledge Graph-specific runtime architecture — covered in `2026-05-12-knowledge-graph-agentic-runtime-dependency`
- Knowledge Graph lifecycle and schema versioning — covered in `2026-05-12-knowledge-graph-lifecycle-management-agentic`
- Agent model fine-tuning or weight updates (the focus is context/document changes, not model changes)
- RAG system architecture and embedding model selection (covered in adjacent items)
- Non-retrieval-based context injection (e.g., hardcoded system prompts not sourced from documents)

**Constraints:**
- Focus on production or near-production systems; prefer documented case studies, published evaluations, and peer-reviewed research over pure speculation
- Cover both detection (how to know a regression has occurred) and mitigation (how to prevent or recover from it)
- Time horizon: current state of practice (2022–2026)

## Context

Agents are typically built and tested against a specific snapshot of the documents they will query at runtime. Those documents — via Retrieval-Augmented Generation (RAG) or other retrieval methods — inject content into the context window that informs or drives agent decisions. Once deployed, those documents continue to change as knowledge is updated, policies are revised, or product content evolves. The documents are effectively a runtime dependency whose version at test time may diverge significantly from the version encountered in production.

This problem mirrors the challenge ITSM (IT Service Management) tooling was built to solve for infrastructure: a Configuration Management Database (CMDB) records what components a service depends on so that the impact of a change can be assessed before it propagates. Platforms such as ServiceNow already expose dependency maps linking services to their supporting configuration items; the open question is how and whether those same patterns can be extended to link deployed agents to the document corpora they depend on, and how change management governance processes should gate document-corpus updates just as they gate infrastructure changes. This research informs how teams should design, test, and operate agents where document-corpus drift is a known operational risk and where no formal dependency or change management discipline yet covers document-to-agent relationships.

## Approach

1. Characterise the propagation mechanism: how does a document change reach an agent's context window?
   - 1a. Which change types (rewording, factual update, structural rearrangement, deletion) most reliably change what is retrieved and injected?
   - 1b. What is the sensitivity of embedding-based retrieval to each change type, and does it differ from keyword or hybrid retrieval?

2. Survey documented failure modes and real-world incidents where document drift caused agent behavioral regressions.
   - 2a. What categories of behavioral regression (wrong decision, hallucination amplification, altered tool selection, changed reasoning path) are associated with document changes?
   - 2b. Are there published case studies or incident reports of production agents behaving incorrectly after source document updates?

3. Evaluate testing and evaluation frameworks for their ability to detect document-drift-induced regressions.
   - 3a. How do Ragas, TruLens, LangSmith, and comparable tools support corpus-version-aware behavioral baselines?
   - 3b. What regression-testing patterns (golden-set evaluations, output comparison, invariant checking) are applicable and documented in the literature?

4. Identify mitigation and governance patterns for managing document corpora as versioned runtime dependencies.
   - 4a. What versioning approaches (snapshot indices, version-pinned retrieval, corpus changelogs) have been proposed or adopted in practice?
   - 4b. How do software engineering concepts — semantic versioning, contract testing, dependency lock files — translate to document-corpus management?
   - 4c. What deployment governance patterns (canary corpus rollouts, staged index promotion, review gates before propagation) are applicable?

5. Synthesise lessons from adjacent completed research that apply to this problem.
   - 5a. What failure-mode mitigations from the KG runtime-dependency item apply to document-corpus dependencies?
   - 5b. What does the AIBOM (Artificial Intelligence Bill of Materials) runtime-divergence item reveal about tracing which document versions participated in a given agent run?
   - 5c. What does the existing CSDM dependency-mapping item reveal about how service-to-CI linkages are currently modelled, and how far that model needs to be extended to cover agent-to-document relationships?

6. Investigate dependency management and change management patterns for agent-to-document relationships.
   - 6a. How do CMDB and service-registry patterns represent the dependency between a deployed service and its supporting data sources, and how could those patterns be extended to register an agent's dependency on a specific document corpus or corpus version?
   - 6b. What ITIL change management concepts — change authorisation, impact assessment, rollback planning, and post-implementation review — apply directly to document-corpus updates when those documents are known runtime dependencies for production agents?
   - 6c. How does ServiceNow's existing dependency mapping and change management capability model the relationship between knowledge-base articles and the services that consume them, and what gap exists for agentic consumers specifically?
   - 6d. What leading indicators (corpus diff size, semantic delta, affected-agent blast radius) could feed an automated impact-assessment check in a change management gate before a document-corpus update is promoted to production?

## Sources

- [ ] [Lewis et al. (2020) Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) — foundational RAG architecture paper; establishes the retrieval-to-context-window mechanism
- [ ] [Gao et al. (2024) Retrieval-Augmented Generation for Large Language Models: A Survey](https://arxiv.org/abs/2312.10997) — comprehensive survey covering modular RAG variants and known failure modes
- [ ] [Es et al. (2023) RAGAS: Automated Evaluation of Retrieval Augmented Generation](https://arxiv.org/abs/2309.15217) — the Ragas evaluation framework paper; covers faithfulness, answer relevancy, and context precision metrics
- [ ] [Ragas Documentation](https://docs.ragas.io/en/stable/) — current framework docs; relevant to corpus-version-aware evaluation support
- [ ] [LangSmith Evaluation Documentation](https://docs.smith.langchain.com/evaluation) — covers dataset-based regression testing and comparison runs for RAG pipelines
- [ ] [TruLens Documentation](https://www.trulens.org/docs/) — RAG triad (context relevance, groundedness, answer relevance) evaluation; relevant to detecting drift
- [ ] [ITIL 4 Change Enablement Practice Guide](https://www.axelos.com/certifications/itil-service-management/itil-4-foundation) — defines change authorisation, impact assessment, change advisory boards, and rollback planning; the source process model for applying change management to document-corpus updates
- [ ] [ServiceNow Configuration Management Database Documentation](https://docs.servicenow.com/bundle/washingtondc-it-service-management/page/product/configuration-management/concept/c_ITILConfigurationManagement.html) — defines CI (Configuration Item) records, dependency relationships, and impact analysis; the pattern to extend for agent-to-document linkages
- [ ] [ServiceNow Knowledge Management and Search AI Documentation](https://docs.servicenow.com/bundle/washingtondc-it-service-management/page/product/knowledge-management/concept/c_KnowledgeManagement.html) — documents how ServiceNow manages knowledge-base articles and versioning; entry point for gap analysis against agentic consumers

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

- Type: # skill | tool | agent | knowledge | backlog-item
- Description:
- Links:
