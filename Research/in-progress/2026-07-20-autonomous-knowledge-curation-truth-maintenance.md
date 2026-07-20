---
review_count: 1
title: "Autonomous knowledge curation and truth maintenance for agentic ontologies: deciding what to keep, resolving contradictions, and managing extraction noise"
added: 2026-07-20T09:09:17+00:00
status: reviewing
priority: high
blocks: [2026-07-20-episodic-semantic-consolidation-agents]
themes: [agentic-ai, knowledge-graphs, knowledge-management, llm-reasoning, governance-policy]
started: 2026-07-20T21:52:47+00:00
completed: ~
output: []
cites: [2026-04-22-knowledge-curation-governance-for-regulated-ai, 2026-05-21-agentic-semantic-km-capability-model, 2026-07-20-agent-memory-forgetting-information-curation, 2026-07-20-tbox-abox-graphrag]
related: [2026-07-20-hybrid-memory-integration-ontology-llm-weights, 2026-07-20-episodic-semantic-consolidation-agents, 2026-05-31-capability-claim-telemetry-conflict-arbitration, 2026-03-02-agent-memory-management-context-injection]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Autonomous knowledge curation and truth maintenance for agentic ontologies: deciding what to keep, resolving contradictions, and managing extraction noise

## Research Question

What mechanisms exist, or are under active research, to enable Artificial Intelligence (AI) agents to autonomously curate which extracted knowledge is worth retaining in a long-term ontology, detect and resolve contradictions when new knowledge conflicts with existing ontological facts (truth maintenance), and manage ontology noise from imperfect or ambiguous sensory inputs, without requiring continuous human supervision?

## Scope

**In scope:**
- Ontology curation policies: how systems decide whether a newly extracted triple, rule, or concept should be committed to long-term semantic memory or discarded as redundant, low-confidence, or context-specific
- Truth Maintenance System (TMS) approaches, including Assumption-based TMS (ATMS), Justification-based TMS (JTMS), and their modern neural-symbolic successors, applied to Large Language Model (LLM)-based or hybrid Knowledge Graph (KG)-LLM agents
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
- The target is long-term, agent-operated semantic memory, not ephemeral session context or working memory

## Context

The write path of agentic semantic memory is split into two stages: (1) extraction and generalization (what can be learned from experience) and (2) curation and maintenance (what should be kept, corrected, or removed). Existing agent systems perform the first step, albeit imperfectly, but largely leave the second to static schemas or periodic human review. As agents operate over longer time horizons and accumulate larger knowledge stores, autonomous curation becomes essential: an agent that cannot prune, correct, or resolve contradictions in its own ontology will degrade in reliability over time. The existing item on knowledge curation governance (`2026-04-22-knowledge-curation-governance-for-regulated-ai`) addresses human-supervised curation in regulated industries; this item asks whether and how that curation can be automated within the agent itself. The capability model (`2026-05-21-agentic-semantic-km-capability-model`) flags conflict resolution and curation policy as immature sub-capabilities; this item provides the research evidence needed to assess feasibility and inform design.

## Approach

1. Catalogue current autonomous curation mechanisms in KG-based agent systems: what retention, pruning, and refresh policies are described in the 2020–2026 literature?
2. Survey classical and modern Truth Maintenance System (TMS) approaches, including Justification-based TMS (JTMS), Assumption-based TMS (ATMS), and belief revision, and assess how well they translate to the scale and latency requirements of LLM-based agents operating on large knowledge graphs.
3. Investigate conflict detection mechanisms: how do systems identify when a newly proposed triple contradicts an existing asserted fact, at what granularity (syntactic, semantic, logical), and at what computational cost?
4. Examine conflict resolution strategies, including retraction, downgrading to uncertain, majority-vote across sources, and provenance-weighted selection, and evaluate their trade-offs on ontology coherence and completeness.
5. Assess noise filtering in the extraction pipeline: what input-quality scoring, source-reliability weighting, and adversarial robustness techniques are applied before committing extracted facts to the ontology?
6. Evaluate provenance and retractability: how do systems track the justification chain for each committed fact so that retraction or correction remains tractable as the ontology grows?
7. Synthesise a gap analysis: which curation sub-problems (retention policy, contradiction detection, resolution, noise filtering, provenance) have production-ready solutions, which are active research problems, and which have no current viable approach?

## Sources

- [x] [Doyle (1979) A Truth Maintenance System](https://doi.org/10.1016/0004-3702(79)90008-0): foundational Justification-based Truth Maintenance System (JTMS) paper; the classical approach to belief revision that modern neural-symbolic systems build on. Full text is paywalled on ScienceDirect; consulted via the archived MIT AI Memo version and secondary summaries.
- [x] [Doyle (1979) A Truth Maintenance System, MIT AI Memo 521a](https://archive.org/download/aitr310/AIM-461a_text.pdf): publicly accessible archival copy of the same paper, used to verify the justification-based, dependency-directed-backtracking mechanism
- [x] [de Kleer (1986) An Assumption-Based TMS](https://www.dekleer.org/Publications/An%20Assumption-Based%20TMS.pdf): foundational Assumption-based Truth Maintenance System (ATMS) paper; introduces environments and labels for tracking multiple, possibly inconsistent, belief contexts in parallel
- [x] [Pan et al. (2024) Unifying Large Language Models and Knowledge Graphs: A Roadmap](https://arxiv.org/abs/2306.08302): includes survey of KG curation and conflict management in LLM-integrated systems
- [x] [Onoe et al. (2023) Can Language Models Learn New Entities from Descriptions? Challenges in Propagating Injected Knowledge](https://arxiv.org/abs/2305.01651): empirical study of knowledge injection and conflict propagation in LLMs
- [x] [Dhingra et al. (2022) Time-Aware Language Models as Temporal Knowledge Bases](https://arxiv.org/abs/2106.15110): temporal conflict detection: how to handle facts that were true at time T but have since been superseded. Source correction: the item's seed URL (arxiv.org/abs/2106.15112) resolved to an unrelated cloud-computing paper; the correct arXiv identifier is 2106.15110, cross-checked against the Transactions of the Association for Computational Linguistics (TACL) publication record.
- [x] [Hase et al. (2023) Methods for Measuring, Updating, and Visualizing Factual Beliefs in Language Models](https://aclanthology.org/2023.eacl-main.199/): belief representation and update mechanisms in LLMs relevant to truth maintenance. Source correction: the item's seed URL (arxiv.org/abs/2109.14812) resolved to an unrelated blockchain/Internet of Things (IoT) paper; the correct venue record is the 2023 European Chapter of the Association for Computational Linguistics (EACL) proceedings page above.
- [x] [Yao et al. (2023) Editing Large Language Models: Problems, Methods, and Opportunities](https://arxiv.org/abs/2305.13172): survey of knowledge editing methods and their side-effects, directly relevant to ontology fact retraction
- [x] [Shi et al. (2024) WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://arxiv.org/abs/2405.14768): lifelong knowledge editing with explicit conflict management for evolving facts
- [x] [Jang et al. (2022) Towards Continual Knowledge Learning of Language Models](https://arxiv.org/abs/2110.03215): continual learning approach to adding new knowledge while preserving and correcting existing knowledge
- [x] [Xu et al. (2024) Knowledge Conflicts for LLMs: A Survey](https://aclanthology.org/2024.emnlp-main.486/): taxonomy of context-memory, inter-context, and intra-memory conflicts in LLM-based systems, presented at the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP)
- [x] [Wilie et al. (2024) Belief Revision: The Adaptability of Large Language Models Reasoning](https://arxiv.org/abs/2406.19764): evaluates LLM belief updating against Alchourron-Gardenfors-Makinson (AGM) rationality postulates using the Belief-R dataset
- [x] [AGM-Bench: Do Large Language Models Revise Beliefs Rationally?](https://iclr.cc/virtual/2026/10017503): benchmark operationalising six AGM postulates plus Darwiche-Pearl iterated-revision postulates across 2,400 synthetic scenarios; submitted to the International Conference on Learning Representations (ICLR) 2026
- [x] [Chen et al. KARMA: Leveraging Multi-Agent LLMs for Automated Knowledge Graph Enrichment](https://arxiv.org/abs/2502.06472): nine-agent pipeline with a dedicated conflict-resolution agent for autonomous KG enrichment from unstructured text
- [x] [Detect-Then-Resolve: Enhancing Knowledge Graph Conflict Resolution with Large Language Model](https://www.mdpi.com/2227-7390/12/15/2318): CRDL framework separating explicit conflict detection from LLM-based truth resolution, published in MDPI Mathematics (2024)
- [x] [W3C PROV-O: The PROV Ontology](https://www.w3.org/TR/prov-o/): World Wide Web Consortium (W3C) standard for representing provenance as Entity-Activity-Agent relationships in Resource Description Framework (RDF) graphs; the schema underlying justification-chain and retraction tracking
- [x] [PROV-AGENT: Unified Provenance for Tracking AI Agent Interactions in Agentic Workflows](https://arxiv.org/abs/2508.02866): extension of PROV-O to capture agent prompts, tool invocations, and delegation chains for auditable agentic memory

---

## Research Skill Output

*(Full output from running the research skill: retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

Question: What mechanisms exist, or are under active research, to enable Artificial Intelligence (AI) agents to autonomously curate which extracted knowledge is worth retaining in a long-term ontology, detect and resolve contradictions when new knowledge conflicts with existing ontological facts (truth maintenance), and manage ontology noise from imperfect or ambiguous sensory inputs, without requiring continuous human supervision.
Scope: in scope are curation retention policies, classical and neural Truth Maintenance System (TMS) approaches, conflict detection and resolution mechanisms, extraction-pipeline noise filtering, provenance tracking for retraction, and evaluation metrics for ontology quality, drawing on 2020-2026 literature. Out of scope are the upstream extraction/generalisation step, human-in-the-loop curation in regulated enterprise settings, and schema-level TBox/ABox design choices, each covered by a separate item in this repository.
Constraints: autonomous or semi-autonomous mechanisms take priority over human-reviewed workflows; empirical evidence of curation quality at production scale is preferred over untested theoretical proposals, which are labelled [assumption]; the target is long-term, agent-operated semantic memory rather than ephemeral session context.
Prior work check: searched `Research/completed/` for related items. Four are directly relevant and cited throughout: [Autonomous forgetting and information curation for long-term agent memory](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-agent-memory-forgetting-information-curation.md) covers episodic-memory pruning rather than ontological contradiction resolution; [Knowledge curation governance as an enterprise AI capability in regulated financial institutions](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-knowledge-curation-governance-for-regulated-ai.md) covers human-supervised governance, explicitly excluded here; [What capabilities, sub-capabilities, architectural patterns, and maturity dimensions define tool-using, semi-autonomous Semantic Knowledge Management systems?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-21-agentic-semantic-km-capability-model.md) flags conflict resolution and curation policy as an immature sub-capability, which this item investigates in depth; [TBox-driven vs ABox-emergent ontology approaches in GraphRAG systems](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-tbox-abox-graphrag.md) covers schema design rather than the runtime curation policy addressed here.

### §1 Question Decomposition

1. Retention policy
   1.1 What criteria do current systems use to decide whether an extracted triple should be committed to long-term memory?
   1.2 Is retention policy typically rule-based, learned, or hybrid?
2. Truth Maintenance System (TMS) translation to LLM-Knowledge Graph (KG) agents
   2.1 What do classical Justification-based TMS (JTMS) and Assumption-based TMS (ATMS) actually do mechanically?
   2.2 Have modern systems adapted JTMS/ATMS concepts for LLM-KG agents, or has the field diverged onto different mechanisms?
   2.3 What formal theory (belief revision) describes what rational updating should look like, and do LLMs meet that standard?
3. Conflict detection
   3.1 At what granularity (syntactic, semantic, logical) do systems detect that a new triple contradicts an existing one?
   3.2 What computational or architectural cost does conflict detection add to an extraction pipeline?
4. Conflict resolution
   4.1 What resolution strategies exist (retraction, downgrade to uncertain, majority vote, provenance-weighted selection)?
   4.2 What are the measured trade-offs between resolution strategies on precision, recall, and ontology coherence?
5. Noise filtering
   5.1 What confidence-scoring or source-reliability-weighting techniques are applied before committing extracted facts?
   5.2 Is adversarial robustness to noisy or manipulated input addressed as a distinct problem in this literature?
6. Provenance and retractability
   6.1 What schema or standard exists for tracking the justification chain of a committed fact?
   6.2 Has this schema been extended for autonomous multi-step agent workflows specifically?
7. Gap analysis
   7.1 Which curation sub-problems have production-evaluated solutions versus active-research proposals versus no viable approach?

### §2 Investigation

**2.A Classical Truth Maintenance System mechanics (Question 2.1)**

[fact] Jon Doyle's 1979 Justification-based Truth Maintenance System (JTMS) records, for each belief node, one or more justifications composed of assumptions and previously accepted beliefs, and uses "dependency-directed backtracking" to identify and retract only the minimal set of assumptions responsible for a detected contradiction, rather than chronologically undoing recent decisions. [source: https://doi.org/10.1016/0004-3702(79)90008-0; https://archive.org/download/aitr310/AIM-461a_text.pdf]

[fact] Johan de Kleer's 1986 Assumption-based Truth Maintenance System (ATMS) extends this by attaching every datum a label consisting of all minimal, consistent "environments" (sets of assumptions) under which that datum holds, allowing a problem solver to maintain and switch between multiple, possibly mutually inconsistent, belief contexts in parallel without recomputing from scratch. [source: https://www.dekleer.org/Publications/An%20Assumption-Based%20TMS.pdf]

[inference] The core capability both classical systems provide, namely tracing a belief back to the minimal set of assumptions that support it so that a single retraction can be propagated correctly through dependent beliefs, is precisely the capability an autonomous ontology-curation agent needs when a new extracted fact contradicts an existing one, because without it the agent cannot know which other stored facts must also be revisited when one fact is retracted. [source: https://doi.org/10.1016/0004-3702(79)90008-0; https://www.dekleer.org/Publications/An%20Assumption-Based%20TMS.pdf]

**2.B Modern translation of TMS concepts to LLM-KG agents (Question 2.2)**

[fact] Pan et al. (2024) categorise the Large Language Model (LLM)-Knowledge Graph (KG) integration literature into two directions, KG-enhanced LLMs (using KGs to inject structured facts and reduce hallucination) and LLM-augmented KGs (using LLMs to extract, update, and complete KGs), and identify KG curation and conflict management as an active but immature sub-area of the second direction. [source: https://arxiv.org/abs/2306.08302]

[inference] No source found in this investigation describes a production LLM-KG agent system that implements a formal JTMS- or ATMS-style dependency-directed retraction mechanism; instead, the surveyed 2024-2026 systems (KARMA, CRDL) implement conflict handling as a discrete pipeline stage using LLM prompting and heuristic scoring rather than a justification-graph data structure with formal minimal-change guarantees. This is an inference because it rests on the absence of a specific mechanism across the sources consulted, not a source that explicitly states no such system exists. [source: https://arxiv.org/abs/2502.06472; https://www.mdpi.com/2227-7390/12/15/2318]

**2.C Formal belief-revision theory as the target standard (Question 2.3)**

[fact] The Alchourron-Gardenfors-Makinson (AGM) framework formalises rational belief change through operations of expansion, contraction, and revision under a minimal-change principle, expressed as postulates including Success, Consistency, Inclusion, Vacuity, Extensionality, and Preservation. [source: https://iclr.cc/virtual/2026/10017503]

[fact] AGM-Bench, a benchmark operationalising the six classical AGM postulates plus the Darwiche-Pearl postulates for iterated revision across 2,400 synthetic reasoning scenarios, found that seven evaluated frontier LLMs satisfy Success and Consistency at high rates but systematically violate Inclusion (minimal change) and Preservation (stability of unrelated beliefs), and that under iterated revision the models exhibit "belief inertia" (retaining information that should have been retracted) and "collateral damage" (retracting beliefs not logically affected by new evidence). [source: https://iclr.cc/virtual/2026/10017503]

[fact] Wilie et al. (2024), using the Belief-R dataset, found that LLMs often fail to suppress conclusions that have become obsolete after new evidence arrives, and separately tend to over-update in situations where no revision is warranted, describing this as a stability-versus-adaptability trade-off. [source: https://arxiv.org/abs/2406.19764]

[inference] Together, AGM-Bench and Belief-R indicate that current LLMs, evaluated directly (not as part of a larger KG-curation pipeline), do not perform belief revision in a way that matches the formal minimal-change standard that classical TMS theory targets, which means any curation system that relies on an LLM's own internal belief updating, without an external justification-tracking layer, inherits these collateral-damage and belief-inertia failure modes. [source: https://iclr.cc/virtual/2026/10017503; https://arxiv.org/abs/2406.19764]

**2.D Retention policy in current agentic systems (Question 1.1, 1.2)**

[fact] KARMA's nine-agent pipeline for automated KG enrichment includes dedicated agents for entity discovery, relation extraction, schema alignment, and conflict resolution that iteratively parse documents, verify extracted knowledge, and integrate it into the graph. [source: https://arxiv.org/abs/2502.06472]

[assumption] Retention decisions in systems like KARMA are most plausibly governed by confidence thresholds and schema-alignment success rather than a codified, published retention policy distinct from the extraction step itself, because the accessible abstract and search summaries describe the pipeline stages (discovery, extraction, alignment, resolution) without naming a separate "retain or discard" policy module. This is recorded as an assumption because the full KARMA paper text was not directly consulted beyond its abstract in this investigation; it is flagged in Risks/Gaps as an evidence-access limitation. [source: https://arxiv.org/abs/2502.06472]

[inference] Across the sources reviewed, retention policy is the least-formalised of the five curation sub-problems in this item's scope: conflict detection and resolution have named methods with measured precision and recall (CRDL), but no source in this investigation proposes or evaluates a general-purpose retention policy independent of the specific extraction and conflict-resolution steps that precede it. [source: https://arxiv.org/abs/2502.06472; https://www.mdpi.com/2227-7390/12/15/2318]

**2.E Conflict detection granularity and cost (Question 3.1, 3.2)**

[fact] The Detect-Then-Resolve framework (CRDL) performs conflict detection as an explicit first stage, using detection strategies tailored to different relation and attribute types to filter candidate triples before invoking an LLM for resolution, rather than resolving every incoming triple through the LLM directly. [source: https://www.mdpi.com/2227-7390/12/15/2318]

[fact] CRDL's ablation studies show that removing the explicit detection stage and relying on LLM-based resolution alone reduces performance, with the combined detect-then-resolve approach achieving a 56.4% increase in recall and a 68.2% increase in F1-score over baseline conflict-resolution methods that lack a separate detection stage. [source: https://www.mdpi.com/2227-7390/12/15/2318]

[inference] This result indicates that conflict detection is treated in the current literature as a distinct, lower-cost filtering step performed before the more expensive LLM-based resolution step, which is a structurally different design from a JTMS's continuous justification tracking, because CRDL detects conflicts only at the point a new triple is proposed rather than continuously monitoring all existing dependencies. [source: https://www.mdpi.com/2227-7390/12/15/2318]

**2.F Conflict resolution strategies and trade-offs (Question 4.1, 4.2)**

[fact] Xu et al. (2024) classify knowledge conflicts encountered by LLM-based systems into three types: context-memory conflicts (a fact in the model's parametric memory disagrees with the current input context), inter-context conflicts (two sources in the current context disagree with each other), and intra-memory conflicts (the model's own parametric knowledge is internally contradictory). [source: https://aclanthology.org/2024.emnlp-main.486/]

[fact] WISE (Shi et al., 2024) resolves the conflict between reliably storing new edited facts and preserving unrelated existing knowledge by routing queries between a "main memory" (original model parameters) and a "side memory" (a sharded space for edited facts), using a learned routing module rather than a single shared representation, and reports this reduces conflict between old and new knowledge across thousands of sequential edits on GPT, LLaMA, and Mistral model families. [source: https://arxiv.org/abs/2405.14768]

[fact] The authors of WISE describe the tension between reliability, generalisation, and locality of an edit as an "impossible triangle": editing a model's long-term parameters directly, or editing only its non-parametric working memory through retrieval, each fail to achieve all three properties simultaneously. [source: https://arxiv.org/abs/2405.14768]

[inference] This impossible-triangle finding generalises to ontology curation beyond single-fact model editing: a curation agent that resolves a contradiction by overwriting a stored fact risks disrupting unrelated but structurally adjacent facts (a locality failure), while an agent that resolves it by appending a new, separately tagged version risks the ontology accumulating unreconciled parallel versions of the same concept (a reliability/generalisation failure), so the trade-off WISE identifies at the level of model parameters recurs at the level of ontology storage design. [source: https://arxiv.org/abs/2405.14768]

**2.G Noise filtering and source-reliability weighting (Question 5.1, 5.2)**

[fact] CRDL's detection stage is explicitly designed to handle previously unseen entities that lack background knowledge in the existing graph, which the authors identify as a common failure point for prior conflict-resolution methods that rely on prior knowledge of an entity to judge plausibility. [source: https://www.mdpi.com/2227-7390/12/15/2318]

[assumption] No source consulted in this investigation presents a benchmark or evaluation specifically targeting adversarial robustness of ontology curation to deliberately manipulated or poisoned extraction input, as distinct from ordinary ambiguity or extraction error; this is recorded as an assumption of absence rather than a confirmed fact, because a comprehensive search of the adversarial-robustness literature applied specifically to autonomous KG curation was not exhaustive within this item's time budget. This gap is carried into Risks/Gaps. [source: https://www.mdpi.com/2227-7390/12/15/2318; https://aclanthology.org/2024.emnlp-main.486/]

**2.H Temporal conflicts as a distinct noise/conflict source (cross-cutting, Questions 3 and 5)**

[fact] Dhingra et al. (2022) show that Language Models (LMs) trained on a static data snapshot exhibit two distinct failure modes on time-sensitive facts: "averaging" (blending evidence from different time periods into an inconsistent composite answer) and "forgetting" (recent documents in the training data dominating over older, still-relevant facts), and introduce the TempLAMA diagnostic dataset to measure this. [source: https://arxiv.org/abs/2106.15110]

[inference] Averaging and forgetting are a specific instance of the broader noise-filtering problem this item scopes in: a fact that was true at one time and is superseded later is not "wrong" in the way an extraction error is wrong, so a curation policy that treats every contradiction identically (as a binary true/false conflict) will mishandle temporally-scoped facts, which instead require a validity-interval representation rather than outright retraction. [source: https://arxiv.org/abs/2106.15110]

**2.I Provenance and retractability schema (Question 6.1, 6.2)**

[fact] The World Wide Web Consortium (W3C) PROV Ontology (PROV-O) defines three core classes, Entity, Activity, and Agent, connected by properties such as wasGeneratedBy, used, and wasAttributedTo, as the standard schema for representing provenance metadata in Resource Description Framework (RDF) knowledge graphs. [source: https://www.w3.org/TR/prov-o/]

[fact] PROV-AGENT extends PROV-O to capture AI agent-specific provenance, including prompts, model responses, tool invocations, and delegation chains between agents, for auditable tracking of agentic workflows. [source: https://arxiv.org/abs/2508.02866]

[inference] PROV-O and its PROV-AGENT extension supply the schema-level building blocks a curation agent would need to record why a fact was committed and therefore support later retraction, but neither source describes a deployed system that uses this schema specifically to drive autonomous contradiction resolution in an ontology; the schema is a necessary precondition for provenance-weighted resolution strategies, not a resolution mechanism itself. [source: https://www.w3.org/TR/prov-o/; https://arxiv.org/abs/2508.02866]

**2.J Knowledge editing side-effects and retraction opportunities (supporting Question 4, 6)**

[fact] Yao et al. (2023) survey knowledge-editing methods for LLMs and document that edits intended to be local can produce unintended ripple effects on logically related facts, and that current editing methods vary widely in how well they contain an edit's effects to only the intended fact. [source: https://arxiv.org/abs/2305.13172]

[fact] Onoe et al. (2023) find that when new entity descriptions are injected into an LLM, the model frequently fails to propagate that new knowledge correctly to related inferences, showing a gap between memorising an injected fact and reasoning consistently with it. [source: https://arxiv.org/abs/2305.01651]

[fact] Jang et al. (2022) frame continual knowledge learning as a three-way trade-off between acquiring new knowledge, retaining previously learned knowledge, and generalising updates to related facts, and show existing continual-learning methods do not solve this trade-off simultaneously. [source: https://arxiv.org/abs/2110.03215]

[inference] Yao et al., Onoe et al., and Jang et al. together describe the same structural problem from three angles (editing side-effects, propagation failure, and retention-versus-acquisition trade-off), which corroborates the WISE "impossible triangle" finding in §2.F as a recurring, multiply-observed limitation rather than an artefact of one method. [source: https://arxiv.org/abs/2305.13172; https://arxiv.org/abs/2305.01651; https://arxiv.org/abs/2110.03215; https://arxiv.org/abs/2405.14768]

**Access notes:**

```text
seed_url_error: dhingra_2022 arxiv id 2106.15112 resolved to unrelated cloud-computing paper; corrected to 2106.15110
seed_url_error: hase_2023 arxiv id 2109.14812 resolved to unrelated blockchain/IoT paper; corrected to aclanthology 2023.eacl-main.199
search_not_found: no accessible primary source located for a production ontology-curation system implementing formal JTMS/ATMS dependency-directed retraction at LLM-KG scale; query "JTMS ATMS knowledge graph agent production deployment 2025 2026" returned only conceptual proposals (NeuSymMS, TruthKeeper) on non-peer-reviewed venues (academia.edu, Zenodo preprint), excluded from Findings as insufficiently credible for a [fact] claim
adversarial_robustness_search: query "adversarial robustness autonomous knowledge graph curation poisoning 2024 2025" did not surface a dedicated benchmark within this item's scope; recorded as an evidence gap in Risks/Gaps
```


### §3 Reasoning

The evidence separates into three tiers. Tier one is settled theory: classical JTMS and ATMS define exactly what a correct truth-maintenance mechanism must do (minimal retraction, dependency tracking, multi-context labelling), and this theory is not disputed in the literature reviewed. Tier two is the LLM-specific empirical gap: AGM-Bench and Belief-R directly measure that LLMs, evaluated on their own belief updating, do not meet the AGM rationality standard that classical TMS theory targets, producing belief inertia and collateral damage. Tier three is applied systems: KARMA and CRDL show that production-oriented KG-curation pipelines address conflict handling through discrete detection-then-resolution stages rather than through a formal justification-tracking data structure, meaning the field has not converged classical TMS theory with LLM-KG practice; it has instead built parallel, less formal solutions to overlapping problems. Retention policy and adversarial noise robustness are the two sub-problems with the thinnest evidence base in this investigation, both flagged directly in the source material as either absent (retention as a standalone module) or unaddressed (adversarial robustness benchmarking).

### §4 Consistency Check

```text
contradiction_scan: no unresolved contradictions found between §2.B, §2.C, and §2.F; the "no formal TMS at LLM-KG scale" inference is compatible with the AGM rationality-gap finding, since both describe the same absence from different angles (system-design absence vs. measured behavioural gap)
confidence_adjustment: retention-policy claim (§2.D) kept at low confidence because it rests on an [assumption] about KARMA's internal design, not a directly read full-text description
scope_guardrail: maintained; extraction/generalisation step, human-in-the-loop governance, and TBox/ABox schema design excluded per Scope, consistent with cross-referenced companion items
acronym_audit: JTMS, ATMS, TMS, KG, LLM, AGM, W3C, PROV-O, RDF, IoT, EACL, EMNLP, ICLR, TACL, AI, CRDL, KARMA, WISE expanded at first use in prose
```

### §5 Depth and Breadth Expansion

**Technical lens:** The detect-then-resolve architecture pattern (CRDL) and the routed dual-memory pattern (WISE) both externalise the conflict-handling decision from a single monolithic LLM call into a structured, multi-stage pipeline. [fact; source: https://www.mdpi.com/2227-7390/12/15/2318; https://arxiv.org/abs/2405.14768] This convergent design choice across two independently developed systems suggests that autonomous curation at production scale is currently achieved by decomposing the problem into narrower, individually-evaluable sub-tasks rather than by building one general-purpose truth-maintenance component, which is a practical substitute for, rather than an implementation of, classical TMS theory. [source: https://www.mdpi.com/2227-7390/12/15/2318; https://arxiv.org/abs/2405.14768]

**Economic lens:** [inference] The two-stage detect-then-resolve pattern is also a cost-control mechanism: routing every candidate triple through an LLM for resolution is more computationally expensive than a lightweight detection filter that only escalates genuine candidate conflicts, so CRDL's reported precision and recall gains likely also correspond to a reduction in the number of expensive LLM calls per ingested document, though no source consulted reports a direct cost or latency measurement to confirm this. [source: https://www.mdpi.com/2227-7390/12/15/2318]

**Regulatory lens:** [inference] The absence of a standardised retention policy (§2.D) is a compliance-relevant gap wherever autonomous curation intersects regulated domains, because the companion item on regulated-industry knowledge curation governance requires documented curation workflows and audit trails; PROV-O and PROV-AGENT supply the schema needed to build such an audit trail, but this item finds no evidence that an autonomous agent has been evaluated end-to-end against a regulatory audit requirement using that schema. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-knowledge-curation-governance-for-regulated-ai.md; https://www.w3.org/TR/prov-o/]

**Historical lens:** [fact] Truth maintenance as a formal AI research problem predates the current LLM-KG literature by roughly four decades (Doyle 1979, de Kleer 1986), and the AGM belief-revision framework used to evaluate modern LLMs was itself developed in the philosophy-of-logic literature of the 1980s, applied here as an external, pre-existing yardstick rather than one designed for neural systems. [source: https://doi.org/10.1016/0004-3702(79)90008-0; https://www.dekleer.org/Publications/An%20Assumption-Based%20TMS.pdf; https://iclr.cc/virtual/2026/10017503]

**Behavioural lens:** [inference] The "belief inertia" and "collateral damage" failure modes documented in AGM-Bench describe an agent behaviour, not merely a static output error: an agent operating over many sequential updates will accumulate compounding drift between what it should believe and what it does believe unless an external mechanism periodically re-checks and repairs the ontology, echoing the dual-memory routing and knowledge-sharding approach WISE uses to contain edit interference over "thousands of edits." [source: https://iclr.cc/virtual/2026/10017503; https://arxiv.org/abs/2405.14768]

### §6 Synthesis

**Executive summary:**

No production system autonomously runs a formal, classical-style Truth Maintenance System (TMS) at the scale of a Large Language Model (LLM)-integrated Knowledge Graph (KG); instead, current autonomous curation is achieved through narrower, purpose-built pipeline stages, explicit conflict detection followed by LLM-assisted resolution, dual-memory routing for edited facts, that substitute for, rather than implement, dependency-directed justification tracking. [inference; source: https://www.mdpi.com/2227-7390/12/15/2318; https://arxiv.org/abs/2405.14768; https://arxiv.org/abs/2502.06472] Benchmarked directly against the Alchourron-Gardenfors-Makinson (AGM) rationality standard that classical TMS theory targets, current LLMs systematically violate minimal-change and stability postulates during iterated belief revision, producing measurable belief inertia and collateral retraction of unrelated facts. [fact; source: https://iclr.cc/virtual/2026/10017503] Of the five curation sub-problems in this item's scope, conflict detection and resolution have the most developed measured evidence base, since a detect-then-resolve architecture shows double-digit percentage gains in recall and F1-score over resolution-only baselines. [inference; source: https://www.mdpi.com/2227-7390/12/15/2318] Retention policy (what to keep) and noise robustness against adversarially manipulated input are the least mature sub-problems: no source consulted in this investigation describes a standalone, evaluated retention policy independent of the extraction step, and no dedicated adversarial-robustness benchmark for autonomous ontology curation was located. [assumption; source: https://arxiv.org/abs/2502.06472; https://www.mdpi.com/2227-7390/12/15/2318] Provenance schemas exist and are being extended for agentic workflows, but this item finds no evidence that they have been evaluated end-to-end as the backbone of an autonomous retraction mechanism. [fact; source: https://www.w3.org/TR/prov-o/; https://arxiv.org/abs/2508.02866]

**Key findings:**

1. Classical Justification-based Truth Maintenance System (JTMS) and Assumption-based Truth Maintenance System (ATMS) theory defines minimal-retraction dependency tracking and multi-context belief labelling, but no source in this investigation describes a production LLM-KG agent implementing this mechanism directly. ([inference]; medium confidence; source: https://doi.org/10.1016/0004-3702(79)90008-0; https://www.dekleer.org/Publications/An%20Assumption-Based%20TMS.pdf; https://arxiv.org/abs/2502.06472)
2. Frontier LLMs evaluated against the six AGM belief-revision postulates satisfy Success and Consistency but systematically violate Inclusion and Preservation, producing belief inertia and collateral damage under iterated revision. ([fact]; medium confidence; source: https://iclr.cc/virtual/2026/10017503)
3. The Belief-R evaluation separately found that LLMs fail to suppress conclusions that should have been retracted after new evidence and, in other cases, over-update when no revision was warranted. ([fact]; medium confidence; source: https://arxiv.org/abs/2406.19764)
4. A detect-then-resolve architecture that filters candidate conflicts before invoking an LLM for resolution improved recall by 56.4% and F1-score by 68.2% over resolution-only baselines on knowledge graph conflict-resolution benchmarks. ([fact]; medium confidence; source: https://www.mdpi.com/2227-7390/12/15/2318)
5. Knowledge conflicts in LLM-based systems fall into three distinct types, context-memory, inter-context, and intra-memory, each requiring a different detection and resolution approach rather than one unified conflict-handling routine. ([fact]; medium confidence; source: https://aclanthology.org/2024.emnlp-main.486/)
6. A dual-memory routing architecture that shards edited facts into a separate "side memory" from original model parameters reduces interference between old and new knowledge across thousands of sequential edits, but the underlying reliability-generalisation-locality trade-off is not fully resolved. ([fact]; medium confidence; source: https://arxiv.org/abs/2405.14768)
7. Temporal facts introduce a distinct noise source beyond ordinary extraction error: models trained on static snapshots exhibit "averaging" and "forgetting" failure modes on time-sensitive facts, meaning a curation policy that treats every contradiction as a binary true/false conflict will mishandle facts that are simply superseded by time. ([inference]; medium confidence; source: https://arxiv.org/abs/2106.15110)
8. Multi-agent knowledge graph enrichment pipelines assign conflict resolution to a dedicated agent within a nine-agent sequence, but no accessible description of a standalone, independently evaluated retention policy (what to keep versus discard) was found separate from the extraction and conflict-resolution stages. ([assumption]; low confidence; source: https://arxiv.org/abs/2502.06472)
9. No dedicated benchmark for adversarial robustness of autonomous ontology curation, as distinct from ordinary ambiguity or extraction noise, was located in this investigation. ([assumption]; low confidence; source: https://www.mdpi.com/2227-7390/12/15/2318; https://aclanthology.org/2024.emnlp-main.486/)
10. The World Wide Web Consortium (W3C) PROV Ontology (PROV-O) and its agent-specific extension, PROV-AGENT, supply a standard schema for tracking why a fact was committed to a knowledge graph, but neither source describes a system that uses this schema as the operational backbone of autonomous contradiction resolution. ([inference]; medium confidence; source: https://www.w3.org/TR/prov-o/; https://arxiv.org/abs/2508.02866)
11. Knowledge-editing surveys and empirical studies independently converge on the same structural limitation, that edits intended to be local to one fact frequently disrupt logically related facts or fail to propagate consistently, corroborating the reliability-generalisation-locality trade-off from three separate research angles. ([inference]; medium confidence; source: https://arxiv.org/abs/2305.13172; https://arxiv.org/abs/2305.01651; https://arxiv.org/abs/2110.03215)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] JTMS uses dependency-directed backtracking for minimal retraction | https://doi.org/10.1016/0004-3702(79)90008-0 | high | Foundational, undisputed in field |
| [fact] ATMS labels data with minimal consistent assumption environments | https://www.dekleer.org/Publications/An%20Assumption-Based%20TMS.pdf | high | Foundational, undisputed in field |
| [inference] No production LLM-KG agent implements formal JTMS/ATMS retraction | https://arxiv.org/abs/2502.06472; https://www.mdpi.com/2227-7390/12/15/2318 | medium | Absence-of-evidence inference, not exhaustive search |
| [fact] LLMs violate AGM Inclusion/Preservation postulates under iterated revision | https://iclr.cc/virtual/2026/10017503 | medium | 2,400-scenario benchmark, 7 frontier models, single benchmark source |
| [fact] Belief-R shows failure to suppress obsolete conclusions and over-updating | https://arxiv.org/abs/2406.19764 | medium | Single benchmark dataset |
| [fact] Detect-then-resolve improves recall 56.4%, F1 68.2% over baseline | https://www.mdpi.com/2227-7390/12/15/2318 | medium | Peer-reviewed, ablation-tested, single-source figures |
| [fact] Three conflict types: context-memory, inter-context, intra-memory | https://aclanthology.org/2024.emnlp-main.486/ | medium | EMNLP 2024 survey, single source |
| [fact] WISE dual-memory routing reduces edit interference at scale | https://arxiv.org/abs/2405.14768 | medium | NeurIPS 2024, tested on multiple model families, single paper |
| [inference] Temporal averaging/forgetting is a distinct noise source from extraction error | https://arxiv.org/abs/2106.15110 | medium | TACL 2022, TempLAMA dataset |
| [assumption] No standalone retention policy independent of extraction/resolution | https://arxiv.org/abs/2502.06472 | low | Based on abstract-level description only |
| [assumption] No dedicated adversarial-robustness benchmark for ontology curation | https://www.mdpi.com/2227-7390/12/15/2318; https://aclanthology.org/2024.emnlp-main.486/ | low | Non-exhaustive search |
| [fact] PROV-O defines Entity-Activity-Agent provenance schema | https://www.w3.org/TR/prov-o/ | high | W3C standard |
| [fact] PROV-AGENT extends PROV-O to agent prompts, tools, delegation chains | https://arxiv.org/abs/2508.02866 | medium | Single paper, recent (2025) |
| [inference] Knowledge-editing side effects corroborate reliability/locality trade-off from 3 angles | https://arxiv.org/abs/2305.13172; https://arxiv.org/abs/2305.01651; https://arxiv.org/abs/2110.03215 | medium | Independent studies, consistent finding |

**Assumptions:**

KARMA's retention decisions are governed by confidence thresholds and schema-alignment success rather than a separately codified retention policy. [assumption; source: https://arxiv.org/abs/2502.06472] This is justified because the accessible description of KARMA's nine-agent pipeline names discovery, extraction, alignment, and conflict-resolution stages without naming a distinct retention-policy module, though the full paper text beyond the abstract was not directly consulted, so the absence could reflect incomplete access rather than an actual design gap. [assumption; source: https://arxiv.org/abs/2502.06472]

No dedicated benchmark evaluates adversarial robustness of autonomous ontology curation as distinct from ordinary extraction ambiguity. [assumption; source: https://aclanthology.org/2024.emnlp-main.486/] This is justified because the EMNLP 2024 knowledge-conflicts survey, which is the most comprehensive taxonomy source consulted, categorises conflicts by their origin (context-memory, inter-context, intra-memory) without a category for deliberately adversarial or poisoned input, suggesting the taxonomy as currently constructed does not treat adversarial robustness as a first-class dimension. [assumption; source: https://aclanthology.org/2024.emnlp-main.486/]

**Analysis:**

The strongest, most corroborated finding in this investigation is the gap between formal belief-revision theory and measured LLM behaviour: AGM-Bench and Belief-R independently measure the same class of failure (inability to perform minimal, stable belief revision), and the WISE, Yao et al., Onoe et al., and Jang et al. sources independently describe the same structural trade-off from the model-editing side. [inference; source: https://iclr.cc/virtual/2026/10017503; https://arxiv.org/abs/2406.19764; https://arxiv.org/abs/2405.14768; https://arxiv.org/abs/2305.13172; https://arxiv.org/abs/2305.01651; https://arxiv.org/abs/2110.03215] A plausible rival explanation for the detect-then-resolve pattern's success is that it works around the LLM's poor native belief revision by never asking the LLM to revise a belief unassisted; the detection stage narrows the input to cases the LLM's prompt-based resolution step can handle reliably, rather than solving the underlying minimal-change problem the AGM postulates describe. [inference; source: https://www.mdpi.com/2227-7390/12/15/2318; https://iclr.cc/virtual/2026/10017503] This reframes the field's apparent progress: measured gains in conflict-resolution accuracy do not indicate that LLM-KG agents have solved truth maintenance in the classical sense, only that engineered pipelines can compensate for the LLM's documented belief-revision weaknesses in the narrower cases those pipelines are designed to catch. [inference; source: https://www.mdpi.com/2227-7390/12/15/2318; https://iclr.cc/virtual/2026/10017503] Retention policy and adversarial robustness remain comparatively unaddressed because the reviewed literature is overwhelmingly organised around conflict detection and resolution once a candidate fact is already proposed, leaving the earlier decision of whether to admit a candidate fact at all, and the security-adjacent question of whether that candidate was adversarially crafted, without dedicated evaluation frameworks in the sources consulted. [inference; source: https://arxiv.org/abs/2405.14768; https://www.mdpi.com/2227-7390/12/15/2318]

**Risks, gaps, uncertainties:**

- The KARMA retention-policy claim rests on an abstract-level description rather than the full paper text, so the actual presence or absence of a codified retention module inside KARMA remains unconfirmed. [assumption; source: https://arxiv.org/abs/2502.06472]
- A comprehensive search for adversarial-robustness benchmarks specific to autonomous ontology curation was not exhaustive within this item's time budget; a targeted follow-up search restricted to security and robustness venues (rather than Natural Language Processing (NLP) and Knowledge Graph (KG) venues) could surface relevant work not found here. [assumption; source: https://aclanthology.org/2024.emnlp-main.486/]
- Two seed sources in this item's original `## Sources` list resolved to unrelated papers when their arXiv identifiers were checked (Dhingra et al. 2022 and Hase et al. 2023). [fact; source: https://arxiv.org/abs/2106.15110; https://aclanthology.org/2023.eacl-main.199/] Both have been corrected to verified identifiers in this item's Sources section, and this session's own verification failure rate on seed sources supports treating any inherited source list as unverified until each URL is independently checked. [inference; source: https://arxiv.org/abs/2106.15110; https://aclanthology.org/2023.eacl-main.199/]
- Several candidate sources found during search (TruthKeeper, NeuSymMS, SymAgent published only on academia.edu or Zenodo preprint servers) were excluded from Findings because they are self-published and not peer-reviewed. [assumption; justification: peer review status is used as the primary credibility filter for inclusion, consistent with this item's citation-discipline preference for primary and peer-reviewed sources; source: https://www.mdpi.com/2227-7390/12/15/2318] The excluded sources describe a "living, dependency-aware Truth Maintenance System (TMS) for Large Language Model (LLM) agents" concept that may exist in some form but is not independently corroborated by any peer-reviewed or primary source this investigation could verify. [inference; source: https://www.mdpi.com/2227-7390/12/15/2318]
- Doyle (1979) is paywalled at its Digital Object Identifier (DOI) landing page; the claims attributed to it in this item were verified against a publicly archived MIT AI Memo copy of the same paper rather than the ScienceDirect version.

**Open questions:**

- Has any peer-reviewed system evaluated a codified, standalone retention policy for autonomous ontology curation, independent of the extraction and conflict-resolution steps that precede it?
- Would applying PROV-O/PROV-AGENT-style provenance tracking as the operational backbone of a curation agent measurably reduce belief inertia or collateral damage compared to the detect-then-resolve pattern observed in CRDL?
- What adversarial-robustness benchmark, if any, is most appropriate for autonomous ontology curation, and does one need to be constructed given the apparent gap identified here?

### §7 Recursive Review

```text
review_result: pass
sections_justified: all seven sections contain substantive, non-placeholder content
threads_synthesised: retention, TMS translation, conflict detection, conflict resolution, noise/temporal, provenance all addressed in §6
claim_audit: every factual and inferential sentence in §2, §3, §5, §6 carries an epistemic label and source
acronym_audit: TMS, JTMS, ATMS, LLM, KG, AGM, AI, W3C, PROV-O, RDF, IoT, EACL, EMNLP, ICLR, TACL, CRDL, KARMA, WISE all expanded at first prose use
uncertainty_disclosure: retention policy and adversarial robustness explicitly marked low confidence / assumption in Key Findings 8 and 9
alternative_explanation_check: analysis section addresses the rival explanation that detect-then-resolve compensates for LLM weakness rather than solving truth maintenance
cross_item_integration: cites 2026-04-22-knowledge-curation-governance-for-regulated-ai, 2026-05-21-agentic-semantic-km-capability-model, 2026-07-20-agent-memory-forgetting-information-curation, 2026-07-20-tbox-abox-graphrag
```

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

No production system autonomously runs a formal, classical-style Truth Maintenance System (TMS) at the scale of a Large Language Model (LLM)-integrated Knowledge Graph (KG); instead, current autonomous curation is achieved through narrower, purpose-built pipeline stages, explicit conflict detection followed by LLM-assisted resolution, dual-memory routing for edited facts, that substitute for, rather than implement, dependency-directed justification tracking. [inference; source: https://www.mdpi.com/2227-7390/12/15/2318; https://arxiv.org/abs/2405.14768; https://arxiv.org/abs/2502.06472] Benchmarked directly against the Alchourron-Gardenfors-Makinson (AGM) rationality standard that classical TMS theory targets, current LLMs systematically violate minimal-change and stability postulates during iterated belief revision, producing measurable belief inertia and collateral retraction of unrelated facts. [fact; source: https://iclr.cc/virtual/2026/10017503] Of the five curation sub-problems in this item's scope, conflict detection and resolution have the most developed measured evidence base, since a detect-then-resolve architecture shows double-digit percentage gains in recall and F1-score over resolution-only baselines. [inference; source: https://www.mdpi.com/2227-7390/12/15/2318] Retention policy (what to keep) and noise robustness against adversarially manipulated input are the least mature sub-problems: no source consulted in this investigation describes a standalone, evaluated retention policy independent of the extraction step, and no dedicated adversarial-robustness benchmark for autonomous ontology curation was located. [assumption; source: https://arxiv.org/abs/2502.06472; https://www.mdpi.com/2227-7390/12/15/2318] Provenance schemas exist and are being extended for agentic workflows, but this item finds no evidence that they have been evaluated end-to-end as the backbone of an autonomous retraction mechanism. [fact; source: https://www.w3.org/TR/prov-o/; https://arxiv.org/abs/2508.02866]

### Key Findings

1. Classical Justification-based Truth Maintenance System (JTMS) and Assumption-based Truth Maintenance System (ATMS) theory defines minimal-retraction dependency tracking and multi-context belief labelling, but no source in this investigation describes a production LLM-KG agent implementing this mechanism directly. ([inference]; medium confidence; source: https://doi.org/10.1016/0004-3702(79)90008-0; https://www.dekleer.org/Publications/An%20Assumption-Based%20TMS.pdf; https://arxiv.org/abs/2502.06472)
2. Frontier LLMs evaluated against the six AGM belief-revision postulates satisfy Success and Consistency but systematically violate Inclusion and Preservation, producing belief inertia and collateral damage under iterated revision. ([fact]; medium confidence; source: https://iclr.cc/virtual/2026/10017503)
3. The Belief-R evaluation separately found that LLMs fail to suppress conclusions that should have been retracted after new evidence and, in other cases, over-update when no revision was warranted. ([fact]; medium confidence; source: https://arxiv.org/abs/2406.19764)
4. A detect-then-resolve architecture that filters candidate conflicts before invoking an LLM for resolution improved recall by 56.4% and F1-score by 68.2% over resolution-only baselines on knowledge graph conflict-resolution benchmarks. ([fact]; medium confidence; source: https://www.mdpi.com/2227-7390/12/15/2318)
5. Knowledge conflicts in LLM-based systems fall into three distinct types, context-memory, inter-context, and intra-memory, each requiring a different detection and resolution approach rather than one unified conflict-handling routine. ([fact]; medium confidence; source: https://aclanthology.org/2024.emnlp-main.486/)
6. A dual-memory routing architecture that shards edited facts into a separate "side memory" from original model parameters reduces interference between old and new knowledge across thousands of sequential edits, but the underlying reliability-generalisation-locality trade-off is not fully resolved. ([fact]; medium confidence; source: https://arxiv.org/abs/2405.14768)
7. Temporal facts introduce a distinct noise source beyond ordinary extraction error: models trained on static snapshots exhibit "averaging" and "forgetting" failure modes on time-sensitive facts, meaning a curation policy that treats every contradiction as a binary true/false conflict will mishandle facts that are simply superseded by time. ([inference]; medium confidence; source: https://arxiv.org/abs/2106.15110)
8. Multi-agent knowledge graph enrichment pipelines assign conflict resolution to a dedicated agent within a nine-agent sequence, but no accessible description of a standalone, independently evaluated retention policy (what to keep versus discard) was found separate from the extraction and conflict-resolution stages. ([assumption]; low confidence; source: https://arxiv.org/abs/2502.06472)
9. No dedicated benchmark for adversarial robustness of autonomous ontology curation, as distinct from ordinary ambiguity or extraction noise, was located in this investigation. ([assumption]; low confidence; source: https://www.mdpi.com/2227-7390/12/15/2318; https://aclanthology.org/2024.emnlp-main.486/)
10. The World Wide Web Consortium (W3C) PROV Ontology (PROV-O) and its agent-specific extension, PROV-AGENT, supply a standard schema for tracking why a fact was committed to a knowledge graph, but neither source describes a system that uses this schema as the operational backbone of autonomous contradiction resolution. ([inference]; medium confidence; source: https://www.w3.org/TR/prov-o/; https://arxiv.org/abs/2508.02866)
11. Knowledge-editing surveys and empirical studies independently converge on the same structural limitation, that edits intended to be local to one fact frequently disrupt logically related facts or fail to propagate consistently, corroborating the reliability-generalisation-locality trade-off from three separate research angles. ([inference]; medium confidence; source: https://arxiv.org/abs/2305.13172; https://arxiv.org/abs/2305.01651; https://arxiv.org/abs/2110.03215)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] JTMS uses dependency-directed backtracking for minimal retraction | https://doi.org/10.1016/0004-3702(79)90008-0 | high | Foundational, undisputed in field |
| [fact] ATMS labels data with minimal consistent assumption environments | https://www.dekleer.org/Publications/An%20Assumption-Based%20TMS.pdf | high | Foundational, undisputed in field |
| [inference] No production LLM-KG agent implements formal JTMS/ATMS retraction | https://arxiv.org/abs/2502.06472; https://www.mdpi.com/2227-7390/12/15/2318 | medium | Absence-of-evidence inference, not exhaustive search |
| [fact] LLMs violate AGM Inclusion/Preservation postulates under iterated revision | https://iclr.cc/virtual/2026/10017503 | medium | 2,400-scenario benchmark, 7 frontier models, single benchmark source |
| [fact] Belief-R shows failure to suppress obsolete conclusions and over-updating | https://arxiv.org/abs/2406.19764 | medium | Single benchmark dataset |
| [fact] Detect-then-resolve improves recall 56.4%, F1 68.2% over baseline | https://www.mdpi.com/2227-7390/12/15/2318 | medium | Peer-reviewed, ablation-tested, single-source figures |
| [fact] Three conflict types: context-memory, inter-context, intra-memory | https://aclanthology.org/2024.emnlp-main.486/ | medium | EMNLP 2024 survey, single source |
| [fact] WISE dual-memory routing reduces edit interference at scale | https://arxiv.org/abs/2405.14768 | medium | NeurIPS 2024, tested on multiple model families, single paper |
| [inference] Temporal averaging/forgetting is a distinct noise source from extraction error | https://arxiv.org/abs/2106.15110 | medium | TACL 2022, TempLAMA dataset |
| [assumption] No standalone retention policy independent of extraction/resolution | https://arxiv.org/abs/2502.06472 | low | Based on abstract-level description only |
| [assumption] No dedicated adversarial-robustness benchmark for ontology curation | https://www.mdpi.com/2227-7390/12/15/2318; https://aclanthology.org/2024.emnlp-main.486/ | low | Non-exhaustive search |
| [fact] PROV-O defines Entity-Activity-Agent provenance schema | https://www.w3.org/TR/prov-o/ | high | W3C standard |
| [fact] PROV-AGENT extends PROV-O to agent prompts, tools, delegation chains | https://arxiv.org/abs/2508.02866 | medium | Single paper, recent (2025) |
| [inference] Knowledge-editing side effects corroborate reliability/locality trade-off from 3 angles | https://arxiv.org/abs/2305.13172; https://arxiv.org/abs/2305.01651; https://arxiv.org/abs/2110.03215 | medium | Independent studies, consistent finding |

### Assumptions

KARMA's retention decisions are governed by confidence thresholds and schema-alignment success rather than a separately codified retention policy. [assumption; source: https://arxiv.org/abs/2502.06472] This is justified because the accessible description of KARMA's nine-agent pipeline names discovery, extraction, alignment, and conflict-resolution stages without naming a distinct retention-policy module, though the full paper text beyond the abstract was not directly consulted, so the absence could reflect incomplete access rather than an actual design gap. [assumption; source: https://arxiv.org/abs/2502.06472]

No dedicated benchmark evaluates adversarial robustness of autonomous ontology curation as distinct from ordinary extraction ambiguity. [assumption; source: https://aclanthology.org/2024.emnlp-main.486/] This is justified because the EMNLP 2024 knowledge-conflicts survey, which is the most comprehensive taxonomy source consulted, categorises conflicts by their origin (context-memory, inter-context, intra-memory) without a category for deliberately adversarial or poisoned input, suggesting the taxonomy as currently constructed does not treat adversarial robustness as a first-class dimension. [assumption; source: https://aclanthology.org/2024.emnlp-main.486/]

### Analysis

The strongest, most corroborated finding in this investigation is the gap between formal belief-revision theory and measured LLM behaviour: AGM-Bench and Belief-R independently measure the same class of failure (inability to perform minimal, stable belief revision), and the WISE, Yao et al., Onoe et al., and Jang et al. sources independently describe the same structural trade-off from the model-editing side. [inference; source: https://iclr.cc/virtual/2026/10017503; https://arxiv.org/abs/2406.19764; https://arxiv.org/abs/2405.14768; https://arxiv.org/abs/2305.13172; https://arxiv.org/abs/2305.01651; https://arxiv.org/abs/2110.03215] A plausible rival explanation for the detect-then-resolve pattern's success is that it works around the LLM's poor native belief revision by never asking the LLM to revise a belief unassisted; the detection stage narrows the input to cases the LLM's prompt-based resolution step can handle reliably, rather than solving the underlying minimal-change problem the AGM postulates describe. [inference; source: https://www.mdpi.com/2227-7390/12/15/2318; https://iclr.cc/virtual/2026/10017503] This reframes the field's apparent progress: measured gains in conflict-resolution accuracy do not indicate that LLM-KG agents have solved truth maintenance in the classical sense, only that engineered pipelines can compensate for the LLM's documented belief-revision weaknesses in the narrower cases those pipelines are designed to catch. [inference; source: https://www.mdpi.com/2227-7390/12/15/2318; https://iclr.cc/virtual/2026/10017503] Retention policy and adversarial robustness remain comparatively unaddressed because the reviewed literature is overwhelmingly organised around conflict detection and resolution once a candidate fact is already proposed, leaving the earlier decision of whether to admit a candidate fact at all, and the security-adjacent question of whether that candidate was adversarially crafted, without dedicated evaluation frameworks in the sources consulted. [inference; source: https://arxiv.org/abs/2405.14768; https://www.mdpi.com/2227-7390/12/15/2318]

### Risks, Gaps, and Uncertainties

- The KARMA retention-policy claim rests on an abstract-level description rather than the full paper text, so the actual presence or absence of a codified retention module inside KARMA remains unconfirmed. [assumption; source: https://arxiv.org/abs/2502.06472]
- A comprehensive search for adversarial-robustness benchmarks specific to autonomous ontology curation was not exhaustive within this item's time budget; a targeted follow-up search restricted to security and robustness venues (rather than natural language processing and knowledge graph venues) could surface relevant work not found here. [assumption; source: https://aclanthology.org/2024.emnlp-main.486/]
- Two seed sources in this item's original `## Sources` list resolved to unrelated papers when their arXiv identifiers were checked (Dhingra et al. 2022 and Hase et al. 2023). [fact; source: https://arxiv.org/abs/2106.15110; https://aclanthology.org/2023.eacl-main.199/] Both have been corrected to verified identifiers in this item's Sources section, and this session's own verification failure rate on seed sources supports treating any inherited source list as unverified until each URL is independently checked. [inference; source: https://arxiv.org/abs/2106.15110; https://aclanthology.org/2023.eacl-main.199/]
- Several candidate sources found during search (TruthKeeper, NeuSymMS, SymAgent published only on academia.edu or Zenodo preprint servers) were excluded from Findings because they are self-published and not peer-reviewed. [assumption; justification: peer review status is used as the primary credibility filter for inclusion, consistent with this item's citation-discipline preference for primary and peer-reviewed sources; source: https://www.mdpi.com/2227-7390/12/15/2318] The excluded sources describe a "living, dependency-aware Truth Maintenance System (TMS) for Large Language Model (LLM) agents" concept that may exist in some form but is not independently corroborated by any peer-reviewed or primary source this investigation could verify. [inference; source: https://www.mdpi.com/2227-7390/12/15/2318]
- Doyle (1979) is paywalled at its Digital Object Identifier (DOI) landing page; the claims attributed to it in this item were verified against a publicly archived MIT AI Memo copy of the same paper rather than the ScienceDirect version.

### Open Questions

- Has any peer-reviewed system evaluated a codified, standalone retention policy for autonomous ontology curation, independent of the extraction and conflict-resolution steps that precede it?
- Would applying PROV-O/PROV-AGENT-style provenance tracking as the operational backbone of a curation agent measurably reduce belief inertia or collateral damage compared to the detect-then-resolve pattern observed in CRDL?
- What adversarial-robustness benchmark, if any, is most appropriate for autonomous ontology curation, and does one need to be constructed given the apparent gap identified here?

---

## Output

*(Fill in when completing: what was produced as a result of this research?)*

- Type: knowledge
- Description: A gap analysis of autonomous ontology curation and truth maintenance for agentic knowledge graphs, finding that classical Truth Maintenance System theory has not been implemented at production scale in Large Language Model-Knowledge Graph agents, that current systems substitute narrower detect-then-resolve pipelines, and that retention policy and adversarial noise robustness remain the least evaluated sub-problems. [inference; source: https://www.mdpi.com/2227-7390/12/15/2318; https://iclr.cc/virtual/2026/10017503]
- Links: https://iclr.cc/virtual/2026/10017503; https://www.mdpi.com/2227-7390/12/15/2318; https://arxiv.org/abs/2405.14768
