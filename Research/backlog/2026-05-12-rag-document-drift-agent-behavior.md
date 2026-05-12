---
title: "When Retrieval-Augmented Generation source documents change after agent build and test, what failure modes and behavioral regressions arise, and what strategies exist to detect, measure, and mitigate them?"
added: 2026-05-12T11:03:22+00:00
status: backlog
priority: high
blocks: []
tags: [agentic-ai, rag, llm, evaluation, context-engineering]
started: ~
completed: ~
output: []
cites:
  - 2026-05-12-knowledge-graph-agentic-runtime-dependency
  - 2026-04-29-knowledge-scaffolding-context-engineering
related:
  - 2026-05-12-knowledge-graph-agentic-runtime-dependency
  - 2026-05-12-knowledge-graph-lifecycle-management-agentic
  - 2026-04-29-knowledge-scaffolding-context-engineering
  - 2026-05-06-aibom-runtime-generation-divergence-theory
  - 2026-03-08-servicenow-ai-knowledge-rag-agents
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# When Retrieval-Augmented Generation source documents change after agent build and test, what failure modes and behavioral regressions arise, and what strategies exist to detect, measure, and mitigate them?

## Research Question

When the source documents indexed in a Retrieval-Augmented Generation (RAG) pipeline change after an agent has been built and tested, what failure modes and behavioral regressions can result in production, and what strategies — covering document versioning, behavioral baseline testing, and deployment governance — exist to detect, measure, and mitigate these regressions?

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

Agents are typically built and tested against a specific snapshot of the documents they will query at runtime. Those documents — via Retrieval-Augmented Generation (RAG) or other retrieval methods — inject content into the context window that informs or drives agent decisions. Once deployed, those documents continue to change as knowledge is updated, policies are revised, or product content evolves. The documents are effectively a runtime dependency whose version at test time may diverge significantly from the version encountered in production. This research informs how teams should design, test, and operate agents where document-corpus drift is a known operational risk.

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

## Sources

- [ ] [Lewis et al. (2020) Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) — foundational RAG architecture paper; establishes the retrieval-to-context-window mechanism
- [ ] [Gao et al. (2024) Retrieval-Augmented Generation for Large Language Models: A Survey](https://arxiv.org/abs/2312.10997) — comprehensive survey covering modular RAG variants and known failure modes
- [ ] [Es et al. (2023) RAGAS: Automated Evaluation of Retrieval Augmented Generation](https://arxiv.org/abs/2309.15217) — the Ragas evaluation framework paper; covers faithfulness, answer relevancy, and context precision metrics
- [ ] [Ragas Documentation](https://docs.ragas.io/en/stable/) — current framework docs; relevant to corpus-version-aware evaluation support
- [ ] [LangSmith Evaluation Documentation](https://docs.smith.langchain.com/evaluation) — covers dataset-based regression testing and comparison runs for RAG pipelines
- [ ] [TruLens Documentation](https://www.trulens.org/docs/) — RAG triad (context relevance, groundedness, answer relevance) evaluation; relevant to detecting drift

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
