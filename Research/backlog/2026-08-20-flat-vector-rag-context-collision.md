---
title: "Context collision and relational blindness in flat-vector RAG"
added: 2026-08-20T07:13:11+00:00
status: backlog
priority: high
blocks: []
themes: [rag-retrieval, memory-context, llm-reasoning, knowledge-graphs, benchmarks-eval]
started: ~
completed: ~
output: []
cites: [2026-07-05-vector-rag-to-ontology-kg-rag-migration, 2026-03-15-context-compression-rag-enterprise-knowledge, 2026-05-12-rag-document-drift-agent-behavior]
related: [2026-03-03-knowledge-representation-agent-context, 2026-07-20-hybrid-memory-integration-ontology-llm-weights, 2026-05-20-information-density-filtering-financial-rag]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Context collision and relational blindness in flat-vector RAG

## Research Question

Given that classical flat-vector Retrieval-Augmented Generation (RAG) acts as an external access mechanism rather than a persistent internal memory state, how do contradictory semantic overlaps in top-k retrieval degrade an agent's deterministic reasoning, and in context-collision scenarios is the failure primarily a context-window limit or a deeper inability to resolve structural conflicts without a relational memory layer?

## Scope

**In scope:**
- Classical vector-only RAG systems that retrieve text chunks without an explicit graph or ontology layer
- Contradictory or overlapping retrieval results returned in the same top-k set
- Whether reasoning failures arise from retrieval ambiguity, context-window packing, or the absence of explicit relation structure
- Comparisons between flat-vector, hybrid, and graph-backed retrieval where they illuminate the failure mechanism
- Enterprise and agent-memory settings where persistence, contradiction handling, and multi-hop reasoning matter

**Out of scope:**
- Fine-tuning or model-weight editing as a remedy for RAG ambiguity
- General search-ranking theory not tied to agent reasoning or memory behavior
- Formal ontology design except where it is needed as the comparison point

**Constraints:** Prioritise 2024-2026 public comparisons of vector, hybrid, and graph-backed retrieval. Distinguish clearly between failures caused by retrieval quality, context packing, and reasoning architecture.

## Context

The repository already contains a migration-level comparison between vector RAG and ontology-backed graph retrieval, but this question isolates a narrower baseline failure: whether flat-vector retrieval breaks because too much conflicting text is packed into context or because it lacks a relational state-space that can represent contradiction explicitly. That distinction matters for deciding whether better reranking is enough or whether a structural memory layer is actually required.

## Related

- [Migration trade-offs from vector Retrieval-Augmented Generation to ontology-backed Knowledge Graph RAG](https://davidamitchell.github.io/Research/research/2026-07-05-vector-rag-to-ontology-kg-rag-migration.html)
- [Context Compression and RAG Techniques for Organisational Knowledge](https://davidamitchell.github.io/Research/research/2026-03-15-context-compression-rag-enterprise-knowledge.html)
- [Knowledge Representation for Agent Context](https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-representation-agent-context.html)

## Approach

1. Define context collision operationally: contradictory chunks, semantically similar but structurally incompatible chunks, or stale-versus-current collisions.
2. Review what flat-vector RAG evaluation literature says about contradiction handling, multi-hop failure, and answer instability under overlapping evidence.
3. Investigate whether reranking, context compression, or citation-aware prompting resolves the failure without adding a relational memory layer.
4. Compare those mitigations with graph-backed or hybrid systems that represent entities and relations explicitly.
5. Synthesize when flat-vector RAG is sufficient and when its failure is structural rather than a tunable retrieval parameter.

## Sources

- [ ] [GitHub issue #651: Multiple research questions](https://github.com/davidamitchell/Research/issues/651) — canonical statement of the research request and open-question linkage
- [ ] [Migration trade-offs from vector Retrieval-Augmented Generation to ontology-backed Knowledge Graph RAG](https://davidamitchell.github.io/Research/research/2026-07-05-vector-rag-to-ontology-kg-rag-migration.html) — closest prior repository item on vector-versus-graph retrieval trade-offs
- [ ] [Context Compression and RAG Techniques for Organisational Knowledge](https://davidamitchell.github.io/Research/research/2026-03-15-context-compression-rag-enterprise-knowledge.html) — prior repository item on flat RAG constraints and mitigations
- [ ] [Knowledge Representation for Agent Context](https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-representation-agent-context.html) — prior repository item on structural memory alternatives
- [ ] [When Retrieval-Augmented Generation source documents change after agent build and test](https://davidamitchell.github.io/Research/research/2026-05-12-rag-document-drift-agent-behavior.html) — prior repository item on stale-context and contradiction risk

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
