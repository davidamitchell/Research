---
title: "Evaluation frameworks for agentic memory quality, relevance, and retrieval accuracy"
added: 2026-07-20T09:07:23+00:00
status: backlog
priority: high
blocks: []
themes: [agentic-ai, memory-context, benchmarks-eval, rag-retrieval]
started: ~
completed: ~
output: []
cites: [2026-03-02-agent-memory-management-context-injection, 2026-03-17-ai-memory-systems-rag-neuroscience, 2026-05-02-knowledge-graph-schema-cross-session-research-mcp]
related: [2026-07-20-agent-memory-forgetting-information-curation, 2026-07-20-agent-memory-consolidation-episodic-semantic, 2026-07-20-hybrid-agent-memory-symbolic-connectionist-synchronisation, 2026-07-20-privacy-preserving-agent-long-term-memory]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Evaluation frameworks for agentic memory quality, relevance, and retrieval accuracy

## Research Question

What benchmark suite and metric design best measures the quality, relevance, retrieval accuracy, freshness, and governance correctness of agentic memory systems across heterogeneous tasks?

## Scope

**In scope:**
- Existing long-term memory benchmarks and datasets for conversational or agentic systems, including where they measure recall well and where they fail to capture utility or governance
- Metric design for retrieval correctness, relevance, temporal freshness, provenance fidelity, contradiction handling, latency, and downstream task impact
- How evaluation should differ across memory types: episodic, semantic, procedural, and hybrid graph-based stores
- Whether a unified suite should combine synthetic benchmarks, replay-based evaluation, and in-the-loop task outcome measures
- Failure cases such as privacy leakage, scope contamination, stale-memory retrieval, and over-retention of irrelevant context

**Out of scope:**
- Implementation of a new benchmark harness in this repository
- Memory-architecture design choices except where needed to define what the metric must observe
- General Large Language Model evaluations unrelated to persistent or cross-session memory

**Constraints:** Prioritise public 2024-2026 benchmarks and evaluation papers. Distinguish clearly between metrics that test recall accuracy and metrics that test governance, utility, or safety, because prior repository work found those are often conflated.

## Context

The earlier agent-memory survey found that LongMemEval and LoCoMo provide useful recall benchmarks but do not establish a shared industry standard, and they do not test governance, provenance, or scoping correctness. That leaves the rest of the memory stack hard to compare. This item asks what a truly decision-useful evaluation framework would need to measure before the other items in this cluster can be compared rigorously.

## Approach

1. Catalogue existing memory benchmarks and identify exactly which failure modes each can and cannot detect.
2. Separate memory-quality dimensions: recall, relevance, freshness, provenance, latency, utility, privacy leakage, and scope correctness.
3. Compare benchmark styles: fixed datasets, long-horizon replay, task-based agent evaluation, and human-judged usefulness.
4. Investigate how graph-based and hybrid memory systems are currently evaluated, including whether multi-hop retrieval needs distinct metrics.
5. Synthesize a benchmark framework that could serve as the measuring stick for the curation, consolidation, and hybrid-memory questions in this cluster.

## Sources

- [ ] [LongMemEval](https://arxiv.org/abs/2410.10813) — long-term interactive memory benchmark for chat assistants
- [ ] [LoCoMo benchmark repository](https://github.com/snap-research/LoCoMo) — long conversational memory dataset and evaluation code
- [ ] [GraphRAG-Bench repository](https://github.com/microsoft/graphrag-bench) — benchmark framework for graph-based Retrieval-Augmented Generation systems
- [ ] [Towards Outcome-Oriented, Task-Agnostic Evaluation of AI Agents](https://arxiv.org/pdf/2511.08242) — evaluation framing beyond narrow component metrics
- [ ] [GitHub Blog — Building an agentic memory system for GitHub Copilot](https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/) — production view of validity and freshness as evaluation targets
- [ ] [Mitchell (2026) Agent Memory Management and Context Injection](https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html) — prior corpus baseline on benchmark gaps and memory-quality concerns


## Related

- [Mitchell (2026) Agent Memory Management and Context Injection](https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html)
- [Mitchell (2026) Artificial Intelligence memory systems: Retrieval-Augmented Generation, vendor implementations, and neuroscience foundations](https://davidamitchell.github.io/Research/research/2026-03-17-ai-memory-systems-rag-neuroscience.html)
- [Mitchell (2026) What entity-relation schema and write/query patterns best support cross-session research provenance and concept reuse for an Artificial Intelligence agent using the Model Context Protocol memory server?](https://davidamitchell.github.io/Research/research/2026-05-02-knowledge-graph-schema-cross-session-research-mcp.html)

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
