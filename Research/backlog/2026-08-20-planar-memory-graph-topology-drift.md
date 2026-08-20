---
title: "Noise thresholds and topology drift in planar memory graphs"
added: 2026-08-20T07:13:11+00:00
status: backlog
priority: high
blocks: []
themes: [agentic-ai, memory-context, knowledge-graphs, llm-reasoning, benchmarks-eval]
started: ~
completed: ~
output: []
cites: [2026-07-20-tbox-abox-graphrag, 2026-03-03-knowledge-representation-agent-context, 2026-07-20-agent-memory-evaluation-framework]
related: [2026-05-27-semantic-domain-emergence-enterprise-ontology, 2026-03-15-latent-concept-extraction-confluence, 2026-05-02-knowledge-graph-schema-cross-session-research-mcp]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Noise thresholds and topology drift in planar memory graphs

## Research Question

In a two-dimensional (2D) planar memory graph, what threshold of contextual noise causes a bounded entity-extraction schema to stop suppressing Large Language Model (LLM)-driven predicate hallucinations, and how does the resulting topological drift affect the agent's ability to perform spatial-relational reasoning over the graph?

## Scope

**In scope:**
- Planar or otherwise explicitly spatial graph layouts used as an agent-memory representation
- Entity and relation extraction pipelines that constrain what predicates may be written into the graph
- Failure modes where duplicated entities, invented predicates, or misplaced edges accumulate over time
- Effects of extraction noise on downstream path-finding, neighborhood reasoning, and other spatial-relational tasks
- Whether there is an observable or defensible threshold at which local extraction errors become global topology drift

**Out of scope:**
- Three-dimensional or multimodal world-model systems where planar layout is not central to the representation
- General LLM hallucination theory not tied to graph-construction or graph-reasoning behavior
- AWS-specific ontology pipelines, which are covered by separate items in this cluster

**Constraints:** Prioritise empirical GraphRAG, memory-graph, and extraction-evaluation literature from 2023-2026. If no paper provides a direct numeric threshold, the output should identify proxy metrics and threshold-estimation methods instead of inventing one.

## Context

The issue frames a personal planar-memory architecture as vulnerable to accumulated extraction noise, but the prior GraphRAG and memory-evaluation items in the repository do not isolate the point at which local predicate errors stop being recoverable and start corrupting global graph shape. Answering that question would inform whether a planar graph can remain a stable long-horizon memory substrate or needs stronger schema controls, repair passes, or a different representational form.

## Related

- [TBox-driven vs ABox-emergent ontology approaches in GraphRAG systems](https://davidamitchell.github.io/Research/research/2026-07-20-tbox-abox-graphrag.html)
- [Knowledge Representation for Agent Context](https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-representation-agent-context.html)
- [Evaluation frameworks for agentic memory quality, relevance, and retrieval accuracy](https://davidamitchell.github.io/Research/research/2026-07-20-agent-memory-evaluation-framework.html)

## Approach

1. Define the target planar-memory architecture precisely enough to distinguish layout choices from logical graph structure.
2. Identify what counts as contextual noise in this setting: entity ambiguity, alias duplication, invented predicates, misplaced relations, or stale edges.
3. Review bounded-schema extraction approaches and determine which error classes they can and cannot suppress.
4. Investigate metrics for topology drift, such as duplicate-node growth, edge inconsistency, community-fragmentation shift, or degraded path-query accuracy.
5. Synthesize whether planar structure offers enough stiffness for long-horizon memory or whether drift-correction and schema evolution are mandatory.

## Sources

- [ ] [GitHub issue #651: Multiple research questions](https://github.com/davidamitchell/Research/issues/651) — canonical statement of the research request and open-question linkage
- [ ] [TBox-driven vs ABox-emergent ontology approaches in GraphRAG systems](https://davidamitchell.github.io/Research/research/2026-07-20-tbox-abox-graphrag.html) — closest prior repository item on schema-guided versus emergent graph construction
- [ ] [Knowledge Representation for Agent Context](https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-representation-agent-context.html) — prior repository item on graph-based context representations
- [ ] [Domain Emergence in Semantic Networks, Cognition, and Organizational Structure](https://davidamitchell.github.io/Research/research/2026-05-27-semantic-domain-emergence-enterprise-ontology.html) — prior repository item on threshold effects in semantic graph structure
- [ ] [Evaluation frameworks for agentic memory quality, relevance, and retrieval accuracy](https://davidamitchell.github.io/Research/research/2026-07-20-agent-memory-evaluation-framework.html) — prior repository item on how to measure graph-memory failure

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
