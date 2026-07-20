---
title: "Autonomous knowledge curation and truth maintenance for agentic ontologies: deciding what to keep, resolving contradictions, and managing extraction noise"
added: 2026-07-20T09:09:17+00:00
status: backlog
priority: high
blocks: [2026-07-20-episodic-semantic-consolidation-agents]
themes: [agentic-ai, knowledge-graphs, knowledge-management, llm-reasoning, governance-policy]
started: ~
completed: ~
output: []
cites: [2026-04-22-knowledge-curation-governance-for-regulated-ai, 2026-03-02-agent-memory-management-context-injection, 2026-05-21-agentic-semantic-km-capability-model]
related: [2026-07-20-hybrid-memory-integration-ontology-llm-weights, 2026-07-20-episodic-semantic-consolidation-agents, 2026-07-20-tbox-abox-graphrag, 2026-05-31-capability-claim-telemetry-conflict-arbitration]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Autonomous knowledge curation and truth maintenance for agentic ontologies: deciding what to keep, resolving contradictions, and managing extraction noise

## Research Question

What mechanisms exist — or are under active research — to enable AI agents to autonomously curate which extracted knowledge is worth retaining in a long-term ontology, detect and resolve contradictions when new knowledge conflicts with existing ontological facts (truth maintenance), and manage ontology noise from imperfect or ambiguous sensory inputs — without requiring continuous human supervision?

## Scope

**In scope:**
- Ontology curation policies: how systems decide whether a newly extracted triple, rule, or concept should be committed to long-term semantic memory or discarded as redundant, low-confidence, or context-specific
- Truth Maintenance System (TMS) approaches — Assumption-based TMS (ATMS), Justification-based TMS (JTMS), and their modern neural-symbolic successors — applied to LLM-based or hybrid KG-LLM agents
- Conflict detection and resolution: mechanisms for identifying when a newly extracted claim contradicts existing ontological facts and for selecting which representation to retain, retract, or flag as uncertain
- Noise filtering in the extraction pipeline: how ambiguous, vague, or erroneous inputs are prevented from polluting the ontology, including confidence scoring, source reliability weighting, and adversarial robustness
- Provenance tracking needed to support later retraction or revision of a committed fact
- Evaluation: metrics and benchmarks for ontology quality, contradiction rate, precision of retained knowledge, and noise sensitivity
- Primary literature from 2020–2026 covering knowledge graph curation, ontology validation, and truth maintenance in neural-symbolic systems

**Out of scope:**
- The extraction and generalization step that produces candidate knowledge (covered in `2026-07-20-episodic-semantic-consolidation-agents`)
- Human-in-the-loop curation workflows in regulated enterprise settings (covered in `2026-04-22-knowledge-curation-governance-for-regulated-ai`)
- Schema-level ontology design choices (TBox vs ABox, covered in `2026-07-20-tbox-abox-graphrag`)
- Curation as a governance or compliance requirement rather than an autonomous agent capability

**Constraints:**
- Emphasis on autonomous or semi-autonomous mechanisms; approaches requiring substantial human review are secondary evidence, not primary
- Empirical evidence of curation quality at scale preferred; theoretical proposals should be flagged as `[assumption]`
- The target is long-term, agent-operated semantic memory — not ephemeral session context or working memory

## Context

The write path of agentic semantic memory is split into two stages: (1) extraction and generalization (what can be learned from experience) and (2) curation and maintenance (what should be kept, corrected, or removed). Existing agent systems perform the first step, albeit imperfectly, but largely leave the second to static schemas or periodic human review. As agents operate over longer time horizons and accumulate larger knowledge stores, autonomous curation becomes essential — an agent that cannot prune, correct, or resolve contradictions in its own ontology will degrade in reliability over time. The existing item on knowledge curation governance (`2026-04-22-knowledge-curation-governance-for-regulated-ai`) addresses human-supervised curation in regulated industries; this item asks whether and how that curation can be automated within the agent itself. The capability model (`2026-05-21-agentic-semantic-km-capability-model`) flags conflict resolution and curation policy as immature sub-capabilities; this item provides the research evidence needed to assess feasibility and inform design.

## Approach

1. Catalogue current autonomous curation mechanisms in KG-based agent systems — what retention, pruning, and refresh policies are described in the 2020–2026 literature?
2. Survey classical and modern Truth Maintenance System (TMS) approaches — Justification-based TMS (JTMS), Assumption-based TMS (ATMS), belief revision — and assess how well they translate to the scale and latency requirements of LLM-based agents operating on large knowledge graphs.
3. Investigate conflict detection mechanisms — how do systems identify when a newly proposed triple contradicts an existing asserted fact, at what granularity (syntactic, semantic, logical), and at what computational cost?
4. Examine conflict resolution strategies — retraction, downgrading to uncertain, majority-vote across sources, provenance-weighted selection — and evaluate their trade-offs on ontology coherence and completeness.
5. Assess noise filtering in the extraction pipeline — what input-quality scoring, source-reliability weighting, and adversarial robustness techniques are applied before committing extracted facts to the ontology?
6. Evaluate provenance and retractability — how do systems track the justification chain for each committed fact so that retraction or correction remains tractable as the ontology grows?
7. Synthesise a gap analysis: which curation sub-problems (retention policy, contradiction detection, resolution, noise filtering, provenance) have production-ready solutions, which are active research problems, and which have no current viable approach?

## Sources

- [ ] [Doyle (1979) A Truth Maintenance System](https://doi.org/10.1016/0004-3702(79)90008-0) — foundational Justification-based TMS (JTMS) paper; the classical approach to belief revision that modern neural-symbolic systems build on
- [ ] [Pan et al. (2024) Unifying Large Language Models and Knowledge Graphs: A Roadmap](https://arxiv.org/abs/2306.08302) — includes survey of KG curation and conflict management in LLM-integrated systems
- [ ] [Onoe et al. (2023) Can LLMs Learn New Entities from Descriptions? Challenges in Propagating Injected Knowledge](https://arxiv.org/abs/2305.01651) — empirical study of knowledge injection and conflict propagation in LLMs
- [ ] [Dhingra et al. (2022) Time-Aware Language Models as Temporal Knowledge Bases](https://arxiv.org/abs/2106.15112) — temporal conflict detection: how to handle facts that were true at time T but have since been superseded
- [ ] [Hase et al. (2023) Methods for Measuring, Updating, and Visualizing Factual Beliefs in Language Models](https://arxiv.org/abs/2109.14812) — belief representation and update mechanisms in LLMs relevant to truth maintenance
- [ ] [Yao et al. (2023) Editing Large Language Models: Problems, Methods, and Opportunities](https://arxiv.org/abs/2305.13172) — survey of knowledge editing methods and their side-effects, directly relevant to ontology fact retraction
- [ ] [Shi et al. (2024) WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://arxiv.org/abs/2405.14768) — lifelong knowledge editing with explicit conflict management for evolving facts
- [ ] [Jang et al. (2022) Towards Continual Knowledge Learning of Language Models](https://arxiv.org/abs/2110.03215) — continual learning approach to adding new knowledge while preserving and correcting existing knowledge

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

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

### Analysis

### Risks, Gaps, and Uncertainties

-

### Open Questions

-

---

## Output

*(Fill in when completing — what was produced as a result of this research?)*

- Type:
- Description:
- Links:
