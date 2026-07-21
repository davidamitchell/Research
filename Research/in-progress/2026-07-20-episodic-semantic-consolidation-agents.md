---
review_count: 1
title: "Episodic-to-semantic memory consolidation in AI agents: techniques for generalizing from experience to durable ontological knowledge"
added: 2026-07-20T09:09:17+00:00
status: reviewing
priority: high
blocks: []
themes: [agentic-ai, memory-context, knowledge-graphs, llm-reasoning, ai-architecture]
started: 2026-07-21T07:48:34+00:00
completed: ~
output: []
cites: [2026-03-02-agent-memory-management-context-injection, 2026-05-21-agentic-semantic-km-capability-model, 2026-07-20-agent-memory-consolidation-episodic-semantic, 2026-07-20-agent-memory-evaluation-framework, 2026-07-20-autonomous-knowledge-curation-truth-maintenance]
related: [2026-07-20-hybrid-memory-integration-ontology-llm-weights, 2026-07-20-autonomous-knowledge-curation-truth-maintenance, 2026-03-15-latent-concept-extraction-confluence, 2026-07-20-tbox-abox-graphrag, 2026-07-20-agent-memory-consolidation-episodic-semantic, 2026-07-20-agent-memory-evaluation-framework]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Episodic-to-semantic memory consolidation in AI agents: techniques for generalizing from experience to durable ontological knowledge

## Research Question

What techniques enable AI agents to reliably generalize from specific episodic experiences (interaction logs, task traces, observed events) to durable semantic memory entries (ontological facts, procedural rules, user-preference generalizations), and how effectively do current systems close the "consolidation gap", the step between "I observed X three times" and "the general rule is Y"?

## Scope

**In scope:**
- Mechanisms used by current Large Language Model (LLM)-based agents to extract semantic generalizations from episodic interaction logs: summarization, clustering, rule induction, and pattern mining
- Autonomous Knowledge Graph (KG) population from experience streams, meaning extraction of entities, relationships, and reusable rules from interaction logs into a graph of typed facts
- Online and continual learning approaches that update an agent's semantic memory incrementally as new episodes accumulate
- Consolidation policies: how systems decide when enough evidence warrants promoting an episodic pattern to a semantic fact, and at what confidence threshold
- Evaluation: benchmarks and metrics used to measure the quality and accuracy of consolidated semantic knowledge
- Comparison of distillation-only approaches, summarization without explicit structure, versus structured generalization, ontology population, rule extraction, or graph updates
- Relevant cognitive-science framing: what human episodic-semantic consolidation research implies for AI agent design, without requiring cognitive fidelity
- Primary literature from 2022 to 2026 spanning agent memory systems, knowledge graph construction, and continual learning

**Out of scope:**
- Fine-tuning or in-weights consolidation, integrating episodic knowledge directly into LLM parameters
- Pure episodic memory retrieval without any generalization step, covered in `2026-03-02-agent-memory-management-context-injection`
- Curation and conflict resolution of already consolidated semantic facts, covered in `2026-07-20-autonomous-knowledge-curation-truth-maintenance`
- The schema-design question of TBox versus ABox, covered in `2026-07-20-tbox-abox-graphrag`

**Constraints:**
- Empirical evidence of generalization quality required; purely conceptual proposals are flagged as `[assumption]`
- Focus on text-based agents and LLM-based systems; robotic or embodied approaches may be cited where directly relevant but are not the primary subject
- Sources are dated 2020 or later because the agent-memory architecture literature is moving quickly

## Context

This item is a companion to the completed architecture study on episodic-to-semantic consolidation for agents, which compared triggers, sleep-time compute, provenance, and intermediate representations, while this item narrows to the generalization techniques themselves, the promotion-policy question, and benchmark design for deciding whether an abstraction is good enough to keep. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-agent-memory-consolidation-episodic-semantic.md]

The earlier agent-memory survey established the consolidation gap between raw trajectories and durable knowledge, and the Semantic Knowledge Management (SKM) capability model marked consolidation policy as an immature sub-capability rather than a solved engineering detail. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-02-agent-memory-management-context-injection.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-21-agentic-semantic-km-capability-model.md]

The completed evaluation-framework item showed that current agent-memory benchmarks separate recall, freshness, conflict handling, and governance, so this item focuses on an even narrower measurement gap: whether a promoted abstraction is the right semantic generalization rather than merely a retrievable memory artifact. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-agent-memory-evaluation-framework.md]

## Approach

1. Survey current episodic-to-semantic transition mechanisms in LLM-agent systems: what prompting, summarization, clustering, and rule-extraction pipelines are described in the 2022 to 2026 literature?
2. Examine autonomous knowledge graph population techniques: how do systems extract entities and relationships from interaction streams to build or extend an ontology without human curation?
3. Investigate consolidation threshold policies: when do systems decide that a pattern seen in episodic memory is strong enough to promote to a semantic fact, and what evidence-quality criteria are used?
4. Assess online continual learning approaches: how do incremental KG construction or memory-update systems handle the trade-off between rapid generalization and premature commitment?
5. Map evaluation benchmarks: what tasks and metrics exist that specifically measure an agent's ability to generalize correctly from episodes rather than merely retrieve past examples?
6. Examine the cognitive-science framing: does the neuroscience of hippocampal-neocortical consolidation offer actionable design principles for the AI consolidation pipeline, or is it mainly motivational context?
7. Synthesize a capability assessment: which sub-steps of the consolidation pipeline, extraction, pattern recognition, promotion decision, and storage format, are currently mature and which remain open research problems?

## Sources

- [x] [Zhong et al. (2024) MemoryBank: Enhancing Large Language Models with Long-Term Memory](https://arxiv.org/abs/2305.10250): forgetting-curve memory updates, event summarization, and user-trait synthesis for long-horizon companion dialogue
- [x] [Park et al. (2023) Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442): importance-scored reflections that turn raw observations into higher-level insights
- [x] [Packer et al. (2023) MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560): hierarchical memory tiers and paging-oriented control, but little explicit semantic-promotion policy
- [x] [Maharana et al. (2024) Evaluating Very Long-Term Conversational Memory of LLM Agents](https://arxiv.org/abs/2402.17753): LoCoMo benchmark for question answering, event summarization, and long-range temporal and causal dialogue memory
- [x] [Modarressi et al. (2023) RET-LLM: Towards a General Read-Write Memory for Large Language Models](https://arxiv.org/abs/2305.14322): triplet extraction and read-write semantic memory for explicit fact storage
- [x] [Cao et al. (2024) LEGO-GraphRAG: Modularizing Graph-based Retrieval-Augmented Generation for Design Space Exploration](https://arxiv.org/abs/2411.05844): modular graph-extraction and subgraph-selection design space for structured semantic memory
- [x] [Wang et al. (2023) A Survey on Large Language Model based Autonomous Agents](https://arxiv.org/abs/2308.11432): broad agent survey that frames memory as one of the four core architectural modules
- [x] [Wu et al. (2024) LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://arxiv.org/abs/2410.10813): five-memory-ability benchmark with explicit knowledge-update and temporal-reasoning axes
- [x] [Anokhin et al. (2024) AriGraph: Learning Knowledge Graph World Models with Episodic Memory for LLM Agents](https://arxiv.org/abs/2407.04363): integrated episodic and semantic memory graph for sequential problem solving
- [x] [Kang et al. (2025) Memory OS of AI Agent](https://arxiv.org/abs/2506.06326): multi-tier memory system with heat-threshold promotion to long-term personal memory
- [x] [Amazon Web Services (AWS) Blog (2026) Build agents to learn from experiences using Amazon Bedrock AgentCore episodic memory](https://aws.amazon.com/blogs/machine-learning/build-agents-to-learn-from-experiences-using-amazon-bedrock-agentcore-episodic-memory/): episode extraction, cross-episodic reflection, and confidence-scored reusable insights in a managed service
- [x] [Jun et al. (2025) A Neural Network Model of Complementary Learning Systems: Pattern Separation and Completion for Continual Learning](https://arxiv.org/abs/2507.11393): dual-store continual-learning model motivated by Complementary Learning Systems (CLS)
- [x] [Sun et al. (2023) Organizing memories for generalization in complementary learning systems](https://colab.ws/articles/10.1038%2Fs41593-023-01382-9): accessible abstract page for a Nature Neuroscience paper arguing that consolidation should be selective and generalization-oriented
- [x] [Anonymous authors (2026) Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers](https://arxiv.org/abs/2603.07670): survey that explicitly names the transition policy from episodic to semantic memory as a current weak point

## Related

- [Mitchell (2026) Episodic-to-semantic memory consolidation architectures for agents](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-agent-memory-consolidation-episodic-semantic.md)
- [Mitchell (2026) Evaluation frameworks for agentic memory quality, relevance, and retrieval accuracy](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-agent-memory-evaluation-framework.md)
- [Mitchell (2026) Autonomous knowledge curation and truth maintenance for agentic ontologies](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-autonomous-knowledge-curation-truth-maintenance.md)
- [Mitchell (2026) TBox-driven vs ABox-emergent ontology approaches in GraphRAG systems](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-tbox-abox-graphrag.md)
- [Mitchell (2026) Agent Memory Management and Context Injection](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-02-agent-memory-management-context-injection.md)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

Question: what techniques enable AI agents to generalize from episodic experiences into durable semantic memory, which promotion policies are actually used, how are those policies evaluated, and what online-learning trade-offs follow from promoting abstractions too early or too late? [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/in-progress/2026-07-20-episodic-semantic-consolidation-agents.md]

Scope: in scope are summarization, clustering, triplet extraction, Knowledge Graph (KG) population, promotion thresholds, continual updates, and benchmark design for semantic generalization quality; out of scope are fine-tuning into model weights, pure episodic retrieval, downstream contradiction management, and TBox versus ABox schema design. [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/in-progress/2026-07-20-episodic-semantic-consolidation-agents.md]

Constraints: this investigation prioritizes 2022 to 2026 primary literature and production engineering reports, requires empirical support where available, and treats purely conceptual proposals as assumptions rather than established results. [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/in-progress/2026-07-20-episodic-semantic-consolidation-agents.md]

Constraint mode: full, because the item is high priority, has a near-duplicate companion item that must be differentiated carefully, and sits upstream of later ontology-curation work. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-agent-memory-consolidation-episodic-semantic.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-autonomous-knowledge-curation-truth-maintenance.md]

Prior-work scan: the completed companion item on episodic-to-semantic memory architectures established the trigger, provenance, and sleep-time-compute landscape, but it did not isolate the narrower question of which generalization techniques are actually used, how strong the promotion threshold is, or which benchmarks measure abstraction quality rather than retrieval quality. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-agent-memory-consolidation-episodic-semantic.md]

The completed evaluation-framework item established that no single benchmark measures recall, freshness, conflict handling, provenance, governance, and downstream task impact together, which is directly relevant because this item asks whether any benchmark isolates semantic-promotion quality itself. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-agent-memory-evaluation-framework.md]

The completed autonomous-curation item is a downstream companion rather than a duplicate, because it studies how to prune or revise semantic facts after promotion, while this item studies the upstream moment at which a system decides to promote an abstraction in the first place. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-autonomous-knowledge-curation-truth-maintenance.md]

### §1 Question Decomposition

1. What generalization techniques are used to transform episodic traces into semantic memory?
   1.1 Which systems use free-text summarization or reflection?
   1.2 Which systems use structured extraction, such as triplets or graph edges?
   1.3 Which systems populate a knowledge graph or world model rather than a summary store?
2. What consolidation-threshold policies are used in practice?
   2.1 Which systems promote memories using explicit thresholds, scores, or schedules?
   2.2 Do any systems publish calibrated evidence thresholds rather than heuristics?
3. How is semantic generalization quality evaluated?
   3.1 What do LoCoMo and LongMemEval measure directly?
   3.2 Do any consulted benchmarks score promotion precision, abstraction correctness, or threshold calibration?
4. What online continual-learning trade-offs appear when semantic promotion happens during or shortly after interaction?
   4.1 What do graph or triplet stores make easier to update than free-text summaries?
   4.2 What failure modes arise from premature commitment or over-compression?
5. What actionable design principles transfer from Complementary Learning Systems (CLS) and recent continual-learning work?

### §2 Investigation

**2.1 Generalization techniques: free-text summarization and reflection.** MemoryBank stores conversation history, events, and user traits, then updates that memory using a forgetting-curve-inspired schedule that reinforces or decays items over time rather than keeping every episode equally salient. [fact; source: https://arxiv.org/abs/2305.10250; https://github.com/zhongwanjun/MemoryBank-SiliconFriend] Its semantic product is mainly a summarized profile of user traits, recalled events, and personality clues, which is useful for personalization but not an explicit rule store or ontology population mechanism. [inference; source: https://arxiv.org/abs/2305.10250; https://github.com/zhongwanjun/MemoryBank-SiliconFriend]

Generative Agents uses a complete stream of timestamped observations and periodically synthesizes higher-level reflections from those observations, meaning the generalization step is an LLM-generated natural-language abstraction rather than a structured fact type. [fact; source: https://arxiv.org/abs/2304.03442] This is genuine semantic promotion, because the reflected statement is more abstract than any one observation, but the representation remains prose and therefore inherits the verification and editability limits of prose memory. [inference; source: https://arxiv.org/abs/2304.03442]

Amazon Bedrock AgentCore's episodic-memory design uses a two-stage transformation from turns to episodes and then from episodes to cross-episodic reflections, where the reusable output is a set of hints, use-case conditions, and a confidence score derived from similar successful past episodes. [fact; source: https://aws.amazon.com/blogs/machine-learning/build-agents-to-learn-from-experiences-using-amazon-bedrock-agentcore-episodic-memory/] This is a more explicit form of pattern induction than MemoryBank or Generative Agents because the system describes reusable strategy extraction across multiple episodes instead of only compressing a local interaction history. [inference; source: https://aws.amazon.com/blogs/machine-learning/build-agents-to-learn-from-experiences-using-amazon-bedrock-agentcore-episodic-memory/]

**2.2 Generalization techniques: structured extraction and knowledge-graph population.** RET-LLM extracts knowledge into triplets of the form `<concept1, relationship, concept2>`, stores them in a read-write memory module, and supports exact and fuzzy retrieval over those structured facts. [fact; source: https://arxiv.org/abs/2305.14322; https://arxiv.org/html/2305.14322] This makes the promoted memory more interpretable, updatable, and aggregatable than a prose summary because each stored unit is already a small semantic assertion rather than an opaque paragraph. [inference; source: https://arxiv.org/abs/2305.14322; https://arxiv.org/html/2305.14322]

AriGraph goes further by constructing and updating a memory graph that integrates episodic and semantic memories while an agent explores a text environment, so the agent's semantic memory is a graph world model rather than a list of summaries. [fact; source: https://arxiv.org/abs/2407.04363] This is the clearest consulted example of autonomous knowledge-graph population from experience streams, although its evidence base comes from text-game environments rather than production coding or research agents. [inference; source: https://arxiv.org/abs/2407.04363]

LEGO-GraphRAG does not itself describe an agent that learns from episodes, but it decomposes graph-based Retrieval-Augmented Generation (RAG) into modular extraction, pruning, and subgraph-selection stages, including node-, edge-, and triple-pruning strategies driven by semantic models or LLM calls. [fact; source: https://arxiv.org/abs/2411.05844; https://arxiv.org/html/2411.05844] That matters here because it shows that graph population and graph selection are separable design choices, so an episodic-to-semantic pipeline can promote structured facts while still varying how aggressively it later compacts or filters them for retrieval. [inference; source: https://arxiv.org/abs/2411.05844; https://arxiv.org/html/2411.05844]

**2.3 Consolidation-threshold policies.** The consulted systems do use explicit promotion signals, but those signals are heuristic rather than statistically calibrated. [inference; source: https://arxiv.org/abs/2304.03442; https://arxiv.org/abs/2305.10250; https://arxiv.org/abs/2506.06326; https://aws.amazon.com/blogs/machine-learning/build-agents-to-learn-from-experiences-using-amazon-bedrock-agentcore-episodic-memory/]

Generative Agents promotes reflection when recent observations accumulate enough importance, MemoryBank updates memory strength using relative significance plus elapsed time, Memory OS promotes mid-term content to long-term memory when a heat score crosses a threshold, and AgentCore creates episodes when a goal is complete and reflection memories after cross-episode comparison, with each reflection carrying a 0.1 to 1.0 confidence score. [fact; source: https://arxiv.org/abs/2304.03442; https://arxiv.org/abs/2305.10250; https://arxiv.org/abs/2506.06326; https://aws.amazon.com/blogs/machine-learning/build-agents-to-learn-from-experiences-using-amazon-bedrock-agentcore-episodic-memory/]

No consulted source publishes a validated evidential threshold of the form "promote after N independent confirming episodes" or a calibration study showing that a promotion score corresponds to a measured probability that the resulting abstraction is correct. [inference; source: https://arxiv.org/abs/2304.03442; https://arxiv.org/abs/2305.10250; https://arxiv.org/abs/2506.06326; https://aws.amazon.com/blogs/machine-learning/build-agents-to-learn-from-experiences-using-amazon-bedrock-agentcore-episodic-memory/; https://arxiv.org/abs/2603.07670]

The 2026 memory survey states the transition policy directly as the hard question, asking when an episodic record should graduate to semantic status and noting that this step is usually handled by explicit developer rules or periodic LLM-driven summarization. [fact; source: https://arxiv.org/abs/2603.07670] This is strong corroboration that the threshold-policy gap is a field-level problem rather than a detail omitted by one paper. [inference; source: https://arxiv.org/abs/2603.07670]

**2.4 Evaluation benchmarks for semantic generalization quality.** LoCoMo evaluates very long-term conversational memory using question answering, event summarization, and multimodal dialogue generation over long synthetic conversations grounded in temporal event graphs. [fact; source: https://arxiv.org/abs/2402.17753; https://aclanthology.org/2024.acl-long.747/; https://github.com/snap-research/LoCoMo] It tests whether a system can answer correctly from long episodic histories and summarize significant events, but it does not score whether a semantic abstraction stored earlier was itself the right abstraction to promote. [inference; source: https://arxiv.org/abs/2402.17753; https://github.com/snap-research/LoCoMo]

LongMemEval evaluates five abilities, information extraction, multi-session reasoning, temporal reasoning, knowledge updates, and abstention, and explicitly criticizes earlier benchmarks such as MemoryBank and LoCoMo for under-testing temporal reasoning, updated facts, assistant-provided information, and large-scale multi-session synthesis. [fact; source: https://arxiv.org/abs/2410.10813; https://arxiv.org/html/2410.10813; https://github.com/xiaowu0162/LongMemEval] LongMemEval is therefore the strongest benchmark lead for this item, because it gets closest to testing whether a memory system uses the newest, contextually correct abstraction rather than merely retrieving an old fact. [inference; source: https://arxiv.org/abs/2410.10813; https://arxiv.org/html/2410.10813]

Even LongMemEval still scores downstream answers and memory recall rather than promotion precision, abstraction granularity, or threshold calibration. [inference; source: https://arxiv.org/abs/2410.10813; https://arxiv.org/html/2410.10813] The completed evaluation-framework item independently reaches the same broader conclusion, that current memory benchmarks measure different slices of behavior and no single suite isolates abstraction quality as a first-class target. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-agent-memory-evaluation-framework.md]

**2.5 Online continual-learning trade-offs.** Structured semantic stores make continual updates easier to localize than prose summaries. [inference; source: https://arxiv.org/abs/2305.14322; https://arxiv.org/abs/2407.04363] RET-LLM's triplets are individually updatable, and AriGraph's graph can integrate new edges and nodes into a world model. [fact; source: https://arxiv.org/abs/2305.14322; https://arxiv.org/abs/2407.04363] LEGO-GraphRAG's modular decomposition suggests that retrieval-time pruning can change without changing the stored graph itself. [inference; source: https://arxiv.org/abs/2411.05844]

The trade-off is that aggressive promotion improves immediate reuse but increases the risk of premature commitment, because an early summary or triplet may discard qualifiers that later episodes would have contradicted or refined. [inference; source: https://arxiv.org/abs/2603.07670; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-autonomous-knowledge-curation-truth-maintenance.md] The autonomous-curation companion item shows why this matters downstream: once a semantic fact exists, conflict detection and retraction become a separate problem that current systems do not solve automatically with the same maturity as the initial promotion step. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-autonomous-knowledge-curation-truth-maintenance.md]

Memory OS reports large gains on LoCoMo from threshold-based promotion into long-term personal memory, but those results show that thresholding can help task performance, not that the chosen threshold is epistemically calibrated or portable across domains. [inference; source: https://arxiv.org/abs/2506.06326; https://github.com/BAI-LAB/MemoryOS]

**2.6 Cognitive-science framing and design implications.** The consulted Complementary Learning Systems literature converges on a dual-store picture: one component encodes distinct episodes quickly and another integrates across experience more slowly to support generalization. [fact; source: https://arxiv.org/abs/2507.11393; https://colab.ws/articles/10.1038%2Fs41593-023-01382-9] Jun et al. implement this idea with a variational autoencoder plus Modern Hopfield network design and show reduced catastrophic forgetting plus an explicit pattern-separation versus pattern-completion dissociation on Split-MNIST. [fact; source: https://arxiv.org/abs/2507.11393]

The more directly actionable insight for agent design is selectivity: the Nature Neuroscience abstract argues that uncontrolled neocortical transfer can overfit and harm generalization, and proposes that memories should consolidate only when doing so helps future generalization. [inference; source: https://colab.ws/articles/10.1038%2Fs41593-023-01382-9] This is conceptually close to the unresolved promotion-policy question in agent memory, because it implies that "store more summaries" is not the right default; the system needs a criterion linked to later usefulness, not only recency or frequency. [inference; source: https://colab.ws/articles/10.1038%2Fs41593-023-01382-9; https://arxiv.org/abs/2603.07670]

### §3 Reasoning

1. Systems that rely on natural-language summaries, such as MemoryBank and Generative Agents, do perform abstraction, but the stored abstraction remains prose and therefore is harder to verify, edit, or compose than structured triplets or graph edges. [inference; source: https://arxiv.org/abs/2305.10250; https://arxiv.org/abs/2304.03442; https://arxiv.org/abs/2305.14322]
2. Systems that extract triplets or maintain graphs, such as RET-LLM and AriGraph, come closer to durable semantic memory in the ontology-building sense because the promoted unit is already a discrete fact or relation rather than a compressed paragraph. [inference; source: https://arxiv.org/abs/2305.14322; https://arxiv.org/abs/2407.04363]
3. The consulted promotion policies are all score-, schedule-, or goal-based heuristics rather than evidence-calibrated thresholds, so the field has mechanisms for deciding when to promote but not strong empirical validation that those decisions are well calibrated. [inference; source: https://arxiv.org/abs/2304.03442; https://arxiv.org/abs/2305.10250; https://arxiv.org/abs/2506.06326; https://aws.amazon.com/blogs/machine-learning/build-agents-to-learn-from-experiences-using-amazon-bedrock-agentcore-episodic-memory/; https://arxiv.org/abs/2603.07670]
4. Current benchmarks mostly test whether a system can recover, update, or reason over memory after storage, not whether the semantic abstraction that entered storage was the right one, which means benchmark maturity lags technique maturity at the promotion-decision step. [inference; source: https://arxiv.org/abs/2402.17753; https://arxiv.org/abs/2410.10813; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-agent-memory-evaluation-framework.md]
5. The strongest transferable principle from Complementary Learning Systems is not biological fidelity but selective replay and selective promotion, meaning that durable semantic storage should be gated by future-usefulness signals rather than by indiscriminate compression of every episode. [inference; source: https://arxiv.org/abs/2507.11393; https://colab.ws/articles/10.1038%2Fs41593-023-01382-9; https://arxiv.org/abs/2603.07670]

### §4 Consistency Check

```text
contradiction_scan: resolved
cross_item_boundary: maintained, this item studies generalization techniques, thresholds, and evaluation; companion items handle architecture comparison, post-promotion curation, and TBox versus ABox schema design
acronym_first_use_scan: passed for LLM, KG, SKM, CLS, RAG
jargon_scan: defined or explained on first use for knowledge graph, continual learning, catastrophic forgetting, and promotion precision
em_dash_scan: passed
```

### §5 Depth and Breadth Expansion

**Technical lens:** The strongest technical split in the evidence is not between "memory" and "no memory" but between unstructured abstraction and structured abstraction. [inference; source: https://arxiv.org/abs/2305.10250; https://arxiv.org/abs/2305.14322; https://arxiv.org/abs/2407.04363] Summary-centric systems compress episodes into prose that is easy for an LLM to reread, while triplet and graph systems preserve explicit relations that are easier to update, traverse, and reuse for multi-hop reasoning. [inference; source: https://arxiv.org/abs/2305.14322; https://arxiv.org/abs/2407.04363; https://arxiv.org/abs/2411.05844]

**Economic lens:** Heuristic thresholds are partly a cost-control device, because promoting every candidate abstraction would force more LLM calls, more storage, and more future retrieval noise. [inference; source: https://arxiv.org/abs/2305.10250; https://arxiv.org/abs/2506.06326; https://aws.amazon.com/blogs/machine-learning/build-agents-to-learn-from-experiences-using-amazon-bedrock-agentcore-episodic-memory/] LEGO-GraphRAG makes this explicit at the graph stage by separating storage from later node-, edge-, or triple-pruning choices, which lets a system spend more compute only when the query needs richer structure. [inference; source: https://arxiv.org/abs/2411.05844; https://arxiv.org/html/2411.05844]

**Historical lens:** The recent agent-memory literature rediscovers a long-standing cognitive distinction between memorizing specific episodes and abstracting reusable knowledge, but it usually implements that distinction with software heuristics rather than with a theory-backed promotion rule. [inference; source: https://arxiv.org/abs/2603.07670; https://colab.ws/articles/10.1038%2Fs41593-023-01382-9] The architectural companion item already mapped trigger types and provenance choices; this item adds that the field still lacks the equivalent of a validated "generalize now" criterion. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-agent-memory-consolidation-episodic-semantic.md]

**Behavioural lens:** LongMemEval and LoCoMo both show that long-horizon dialogue systems struggle with temporal and update-sensitive memory behavior even before the narrower abstraction-quality question is asked. [inference; source: https://arxiv.org/abs/2402.17753; https://arxiv.org/abs/2410.10813] That means a consolidation policy can create two different errors at once, a wrong abstraction and a retrieval burden created by storing too many or too few abstractions, so benchmark design should not treat promotion and retrieval as separable in practice even if they are analytically distinct. [inference; source: https://arxiv.org/abs/2410.10813; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-agent-memory-evaluation-framework.md]

**Regulatory and governance lens:** The downstream truth-maintenance problem becomes harder when upstream promotion discards provenance or uncertainty, because later curation then has less basis for deciding whether a semantic fact should persist. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-autonomous-knowledge-curation-truth-maintenance.md] This strengthens the case for structured abstractions that retain source links, timestamps, and confidence-like metadata even when the system does not yet have a calibrated threshold policy. [inference; source: https://arxiv.org/abs/2305.14322; https://aws.amazon.com/blogs/machine-learning/build-agents-to-learn-from-experiences-using-amazon-bedrock-agentcore-episodic-memory/]

### §6 Synthesis

**Executive summary:**

Current agent-memory systems can generalize from episodes into semantic memory, but they do so mostly with heuristic triggers and weakly validated abstractions rather than with evidence-calibrated promotion policies. [inference; source: https://arxiv.org/abs/2304.03442; https://arxiv.org/abs/2305.10250; https://arxiv.org/abs/2506.06326; https://arxiv.org/abs/2603.07670] Structured generalization techniques, triplets, graphs, and cross-episode reflection records, are more promising than summary-only distillation when the downstream task requires updateable facts, rule reuse, or multi-hop reasoning. [inference; source: https://arxiv.org/abs/2305.14322; https://arxiv.org/abs/2407.04363; https://arxiv.org/abs/2411.05844; https://aws.amazon.com/blogs/machine-learning/build-agents-to-learn-from-experiences-using-amazon-bedrock-agentcore-episodic-memory/] Benchmark maturity lags behind technique maturity, because LoCoMo and LongMemEval test long-horizon memory competence and update handling, but no consulted benchmark directly scores whether the promoted semantic abstraction was the right one to keep. [inference; source: https://arxiv.org/abs/2402.17753; https://arxiv.org/abs/2410.10813; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-agent-memory-evaluation-framework.md] The most actionable cross-domain design lesson from Complementary Learning Systems is selective consolidation for future usefulness, not indiscriminate summarization of every episode. [inference; source: https://arxiv.org/abs/2507.11393; https://colab.ws/articles/10.1038%2Fs41593-023-01382-9]

**Key findings:**

1. MemoryBank and Generative Agents both convert episodic traces into natural-language summaries or reflections, which supports personalization and planning, but this representation keeps semantic memory in prose form rather than as discrete, easily editable semantic facts. ([inference]; medium confidence; source: https://arxiv.org/abs/2305.10250; https://arxiv.org/abs/2304.03442)
2. RET-LLM, AriGraph, and LEGO-GraphRAG show that structured promotion into triplets, graph edges, or modular graph components creates a more updateable and composable semantic memory substrate than summary-only consolidation. ([inference]; medium confidence; source: https://arxiv.org/abs/2305.14322; https://arxiv.org/abs/2407.04363; https://arxiv.org/abs/2411.05844)
3. The explicit promotion thresholds found in the consulted systems are heuristic, importance score, forgetting-curve strength, heat score, or goal-completion plus reflection confidence, rather than calibrated measures of evidential sufficiency. ([inference]; medium confidence; source: https://arxiv.org/abs/2304.03442; https://arxiv.org/abs/2305.10250; https://arxiv.org/abs/2506.06326; https://aws.amazon.com/blogs/machine-learning/build-agents-to-learn-from-experiences-using-amazon-bedrock-agentcore-episodic-memory/)
4. No consulted paper or production report validates a promotion rule such as "store after N independent confirming episodes" or shows that a threshold score maps to a measured probability that the resulting semantic abstraction is correct. ([inference]; medium confidence; source: https://arxiv.org/abs/2304.03442; https://arxiv.org/abs/2305.10250; https://arxiv.org/abs/2506.06326; https://aws.amazon.com/blogs/machine-learning/build-agents-to-learn-from-experiences-using-amazon-bedrock-agentcore-episodic-memory/; https://arxiv.org/abs/2603.07670)
5. LoCoMo and LongMemEval meaningfully test long-horizon memory, temporal reasoning, and knowledge updates, but they evaluate downstream answers and summaries rather than the precision, calibration, or granularity of the earlier semantic-promotion decision itself. ([inference]; high confidence; source: https://arxiv.org/abs/2402.17753; https://arxiv.org/abs/2410.10813; https://github.com/snap-research/LoCoMo; https://github.com/xiaowu0162/LongMemEval)
6. LongMemEval is the strongest consulted benchmark lead for this item because it explicitly adds knowledge-update and abstention tasks and critiques earlier long-memory evaluations for missing updated-fact handling and large-scale multi-session reasoning. ([inference]; medium confidence; source: https://arxiv.org/abs/2410.10813; https://arxiv.org/html/2410.10813; https://github.com/xiaowu0162/LongMemEval)
7. Structured semantic stores make continual updates easier to localize than prose summaries, but they do not remove the risk of premature commitment, because an early triplet or graph edge can still encode the wrong abstraction and later require curation or retraction. ([inference]; medium confidence; source: https://arxiv.org/abs/2305.14322; https://arxiv.org/abs/2407.04363; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-autonomous-knowledge-curation-truth-maintenance.md)
8. The Complementary Learning Systems literature contributes a practical design principle, selective replay and selective consolidation for future usefulness, rather than evidence that current agent systems already implement a biologically grounded promotion policy. ([inference]; medium confidence; source: https://arxiv.org/abs/2507.11393; https://colab.ws/articles/10.1038%2Fs41593-023-01382-9)
9. Distillation-only summarization is not a sufficient replacement for structured consolidation when downstream tasks need rule reuse, contradiction handling, or multi-hop reasoning, because summaries are easier to read back but harder to edit, align, and verify. ([inference]; medium confidence; source: https://arxiv.org/abs/2305.10250; https://arxiv.org/abs/2305.14322; https://arxiv.org/abs/2407.04363; https://arxiv.org/abs/2411.05844)
10. Relative to the companion architecture item, this item's distinctive contribution is to show that the least mature step is not trigger plumbing alone but the absence of validated promotion criteria and abstraction-quality benchmarks for semantic generalization. ([inference]; medium confidence; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-agent-memory-consolidation-episodic-semantic.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-agent-memory-evaluation-framework.md; https://arxiv.org/abs/2410.10813)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] MemoryBank and Generative Agents generalize mainly into prose summaries or reflections | https://arxiv.org/abs/2305.10250; https://arxiv.org/abs/2304.03442 | medium | Two primary papers, same representation class |
| [inference] RET-LLM, AriGraph, and LEGO-GraphRAG support more structured semantic promotion than summary-only systems | https://arxiv.org/abs/2305.14322; https://arxiv.org/abs/2407.04363; https://arxiv.org/abs/2411.05844 | medium | Structured facts or graph elements are discrete update units |
| [inference] Consulted promotion thresholds are heuristic signals such as importance, heat, forgetting strength, or goal completion | https://arxiv.org/abs/2304.03442; https://arxiv.org/abs/2305.10250; https://arxiv.org/abs/2506.06326; https://aws.amazon.com/blogs/machine-learning/build-agents-to-learn-from-experiences-using-amazon-bedrock-agentcore-episodic-memory/ | medium | Multiple systems, no shared calibration study |
| [inference] No consulted source validates an evidentially calibrated promotion threshold | https://arxiv.org/abs/2304.03442; https://arxiv.org/abs/2305.10250; https://arxiv.org/abs/2506.06326; https://aws.amazon.com/blogs/machine-learning/build-agents-to-learn-from-experiences-using-amazon-bedrock-agentcore-episodic-memory/; https://arxiv.org/abs/2603.07670 | medium | Absence-of-evidence claim across consulted set |
| [inference] LoCoMo and LongMemEval test downstream memory competence, not promotion precision itself | https://arxiv.org/abs/2402.17753; https://arxiv.org/abs/2410.10813; https://github.com/snap-research/LoCoMo; https://github.com/xiaowu0162/LongMemEval | high | Multiple benchmark descriptions agree on measured targets |
| [fact] LongMemEval adds knowledge updates and abstention and critiques earlier benchmark coverage | https://arxiv.org/abs/2410.10813; https://arxiv.org/html/2410.10813; https://github.com/xiaowu0162/LongMemEval | medium | Strong direct textual support |
| [inference] Structured semantic stores ease localized updates but do not prevent premature commitment | https://arxiv.org/abs/2305.14322; https://arxiv.org/abs/2407.04363; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-autonomous-knowledge-curation-truth-maintenance.md | medium | Technique evidence plus downstream companion item |
| [inference] Complementary Learning Systems supports selective consolidation for future usefulness | https://arxiv.org/abs/2507.11393; https://colab.ws/articles/10.1038%2Fs41593-023-01382-9 | medium | One artificial model plus one neuroscience abstract |
| [inference] Summary-only distillation is weaker than structured consolidation for rule reuse and multi-hop reasoning | https://arxiv.org/abs/2305.10250; https://arxiv.org/abs/2305.14322; https://arxiv.org/abs/2407.04363; https://arxiv.org/abs/2411.05844 | medium | Cross-system comparison, not head-to-head ablation |
| [inference] This item's distinct contribution is the benchmark-and-threshold gap rather than the trigger taxonomy already covered by the companion architecture item | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-agent-memory-consolidation-episodic-semantic.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-agent-memory-evaluation-framework.md; https://arxiv.org/abs/2410.10813 | medium | Cross-item synthesis claim |

**Assumptions:**

No public benchmark directly scores the correctness of the semantic abstraction at the exact moment of promotion, distinct from later answer quality or retrieval accuracy. [assumption; source: https://arxiv.org/abs/2402.17753; https://arxiv.org/abs/2410.10813] This is justified by the consulted benchmark set for this item and by the completed evaluation-framework companion item, but it remains an assumption because an unreviewed or unconsulted benchmark could exist outside this search. [assumption; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-agent-memory-evaluation-framework.md]

A promotion policy that is calibrated on conversational or text-game episodes will not transfer unchanged to code-repository or research-workflow agents, because the evidence granularity, verification affordances, and error costs differ materially across those domains. [assumption; source: https://arxiv.org/abs/2407.04363; https://aws.amazon.com/blogs/machine-learning/build-agents-to-learn-from-experiences-using-amazon-bedrock-agentcore-episodic-memory/] This is justified by AriGraph operating in text-game environments and AgentCore operating in enterprise workflows, which shows representation ideas can transfer across domains while leaving threshold calibration domain-specific. [assumption; source: https://arxiv.org/abs/2407.04363; https://aws.amazon.com/blogs/machine-learning/build-agents-to-learn-from-experiences-using-amazon-bedrock-agentcore-episodic-memory/]

**Analysis:**

The evidence base supports a clear separation between "can the agent abstract?" and "does the agent know when the abstraction is good enough to keep?" [inference; source: https://arxiv.org/abs/2305.10250; https://arxiv.org/abs/2304.03442; https://arxiv.org/abs/2305.14322; https://arxiv.org/abs/2407.04363] MemoryBank, Generative Agents, RET-LLM, AriGraph, Memory OS, and AgentCore all answer the first question positively, because each one contains an explicit step that turns many local traces into a more reusable representation. [inference; source: https://arxiv.org/abs/2305.10250; https://arxiv.org/abs/2304.03442; https://arxiv.org/abs/2305.14322; https://arxiv.org/abs/2407.04363; https://arxiv.org/abs/2506.06326; https://aws.amazon.com/blogs/machine-learning/build-agents-to-learn-from-experiences-using-amazon-bedrock-agentcore-episodic-memory/] They answer the second question only weakly, because their promotion decisions depend on heuristic signals that are plausible but not benchmarked as calibrated evidence thresholds. [inference; source: https://arxiv.org/abs/2304.03442; https://arxiv.org/abs/2305.10250; https://arxiv.org/abs/2506.06326; https://aws.amazon.com/blogs/machine-learning/build-agents-to-learn-from-experiences-using-amazon-bedrock-agentcore-episodic-memory/; https://arxiv.org/abs/2603.07670]

A plausible rival explanation is that no special consolidation policy is needed at all, because larger context windows and better retrieval can simply keep the raw episodes available and let the model infer the right generalization on demand. [inference; source: https://arxiv.org/abs/2402.17753; https://arxiv.org/abs/2410.10813] The consulted benchmarks do not support that rival strongly, because LoCoMo shows persistent difficulty with long-range temporal and causal integration and LongMemEval reports large performance drops even for long-context systems on sustained interactive memory tasks. [inference; source: https://arxiv.org/abs/2402.17753; https://arxiv.org/abs/2410.10813] Raw retrieval therefore reduces forgetting pressure but does not remove the need for selective abstraction, especially when the downstream system must reuse a rule, update a world model, or compress knowledge for repeated multi-step planning. [inference; source: https://arxiv.org/abs/2305.14322; https://arxiv.org/abs/2407.04363; https://arxiv.org/abs/2603.07670]

This item therefore differs materially from the completed architecture companion. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-agent-memory-consolidation-episodic-semantic.md] The companion item mapped trigger families, provenance, and intermediate representations across architectures; this item shows that the least mature control surface is the semantic-promotion decision rule itself and the lack of a benchmark that scores that decision directly. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-agent-memory-consolidation-episodic-semantic.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-agent-memory-evaluation-framework.md] Put differently, the field has several ways to write semantic memory, but it does not yet have a convincing way to prove that a given write was epistemically justified at the moment it happened. [inference; source: https://arxiv.org/abs/2410.10813; https://arxiv.org/abs/2603.07670]

**Risks, gaps, uncertainties:**

- The benchmark-gap conclusion is based on the consulted benchmark set for this item, not on an exhaustive census of every 2024 to 2026 memory benchmark. [assumption; source: https://arxiv.org/abs/2402.17753; https://arxiv.org/abs/2410.10813]
- Several of the most relevant sources are arXiv preprints or vendor engineering reports rather than long-settled peer-reviewed literature, which is appropriate for a fast-moving topic but lowers confidence in precise effect-size comparisons across systems. [assumption; source: https://arxiv.org/abs/2305.10250; https://arxiv.org/abs/2407.04363; https://aws.amazon.com/blogs/machine-learning/build-agents-to-learn-from-experiences-using-amazon-bedrock-agentcore-episodic-memory/]
- AriGraph provides the clearest autonomous Knowledge Graph example in the consulted set, but its evidence comes from text-game environments rather than repository engineering or enterprise research workflows. [inference; source: https://arxiv.org/abs/2407.04363]
- The selective-consolidation lesson from Complementary Learning Systems is conceptually relevant, but the consulted AI implementations do not yet operationalize it as a validated promotion rule tied to later task utility. [inference; source: https://arxiv.org/abs/2507.11393; https://colab.ws/articles/10.1038%2Fs41593-023-01382-9; https://arxiv.org/abs/2603.07670]

**Open questions:**

- What benchmark would directly score semantic-promotion precision, meaning whether the stored abstraction was the right generalization at the time of promotion rather than merely a useful retrieval artifact later?
- What evidence policy is defensible for promotion in production agents: repeated occurrence, source diversity, counter-example testing, downstream reward, or a composite rule?
- Can a structured semantic memory carry enough provenance, uncertainty, and temporal scope to support later truth maintenance without becoming too expensive to update online?
- Which domains, code agents, research agents, customer-support agents, or game agents, need different threshold calibration because their episodes differ in verifiability and error cost?

### §7 Recursive Review

```text
review_result: pass
acronym_audit: passed (LLM, KG, SKM, CLS, RAG expanded at first use across the document)
claim_label_audit: passed across §§0-6 and all claim-bearing Findings prose
source_url_audit: passed (all source entries and Evidence Map rows contain resolvable URLs)
cross_item_audit: passed (architecture, evaluation, and autonomous-curation companion items cited with GitHub URLs)
parity_check: passed in substance (§6 synthesis claims are mirrored in Findings Executive Summary, Key Findings, Evidence Map, and Analysis)
em_dash_audit: passed
```

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

Current agent-memory systems can generalize from episodes into semantic memory, but they do so mostly with heuristic triggers and weakly validated abstractions rather than with evidence-calibrated promotion policies. [inference; source: https://arxiv.org/abs/2304.03442; https://arxiv.org/abs/2305.10250; https://arxiv.org/abs/2506.06326; https://arxiv.org/abs/2603.07670] Structured generalization techniques, triplets, graphs, and cross-episode reflection records, appear more promising than summary-only distillation when the downstream task requires updateable facts, rule reuse, or multi-hop reasoning. [inference; source: https://arxiv.org/abs/2305.14322; https://arxiv.org/abs/2407.04363; https://arxiv.org/abs/2411.05844; https://aws.amazon.com/blogs/machine-learning/build-agents-to-learn-from-experiences-using-amazon-bedrock-agentcore-episodic-memory/] Benchmark maturity lags behind technique maturity, because LoCoMo and LongMemEval test long-horizon memory competence and update handling, but no consulted benchmark directly scores whether the promoted semantic abstraction was the right one to keep. [inference; source: https://arxiv.org/abs/2402.17753; https://arxiv.org/abs/2410.10813; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-agent-memory-evaluation-framework.md] The most actionable cross-domain design lesson from Complementary Learning Systems is selective consolidation for future usefulness, not indiscriminate summarization of every episode. [inference; source: https://arxiv.org/abs/2507.11393; https://colab.ws/articles/10.1038%2Fs41593-023-01382-9]

### Key Findings

1. MemoryBank and Generative Agents both convert episodic traces into natural-language summaries or reflections, which supports personalization and planning, but this representation keeps semantic memory in prose form rather than as discrete, easily editable semantic facts. ([inference]; medium confidence; source: https://arxiv.org/abs/2305.10250; https://arxiv.org/abs/2304.03442)

2. RET-LLM, AriGraph, and LEGO-GraphRAG show that structured promotion into triplets, graph edges, or modular graph components creates a more updateable and composable semantic memory substrate than summary-only consolidation. ([inference]; medium confidence; source: https://arxiv.org/abs/2305.14322; https://arxiv.org/abs/2407.04363; https://arxiv.org/abs/2411.05844)

3. The explicit promotion thresholds found in the consulted systems are heuristic, importance score, forgetting-curve strength, heat score, or goal-completion plus reflection confidence, rather than calibrated measures of evidential sufficiency. ([inference]; medium confidence; source: https://arxiv.org/abs/2304.03442; https://arxiv.org/abs/2305.10250; https://arxiv.org/abs/2506.06326; https://aws.amazon.com/blogs/machine-learning/build-agents-to-learn-from-experiences-using-amazon-bedrock-agentcore-episodic-memory/)

4. No consulted paper or production report validates a promotion rule such as "store after N independent confirming episodes" or shows that a threshold score maps to a measured probability that the resulting semantic abstraction is correct. ([inference]; medium confidence; source: https://arxiv.org/abs/2304.03442; https://arxiv.org/abs/2305.10250; https://arxiv.org/abs/2506.06326; https://aws.amazon.com/blogs/machine-learning/build-agents-to-learn-from-experiences-using-amazon-bedrock-agentcore-episodic-memory/; https://arxiv.org/abs/2603.07670)

5. LoCoMo and LongMemEval meaningfully test long-horizon memory, temporal reasoning, and knowledge updates, but they evaluate downstream answers and summaries rather than the precision, calibration, or granularity of the earlier semantic-promotion decision itself. ([inference]; high confidence; source: https://arxiv.org/abs/2402.17753; https://arxiv.org/abs/2410.10813; https://github.com/snap-research/LoCoMo; https://github.com/xiaowu0162/LongMemEval)

6. LongMemEval is the strongest consulted benchmark lead for this item because it explicitly adds knowledge-update and abstention tasks and critiques earlier long-memory evaluations for missing updated-fact handling and large-scale multi-session reasoning. ([inference]; medium confidence; source: https://arxiv.org/abs/2410.10813; https://arxiv.org/html/2410.10813; https://github.com/xiaowu0162/LongMemEval)

7. Structured semantic stores make continual updates easier to localize than prose summaries, but they do not remove the risk of premature commitment, because an early triplet or graph edge can still encode the wrong abstraction and later require curation or retraction. ([inference]; medium confidence; source: https://arxiv.org/abs/2305.14322; https://arxiv.org/abs/2407.04363; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-autonomous-knowledge-curation-truth-maintenance.md)

8. The Complementary Learning Systems literature contributes a practical design principle, selective replay and selective consolidation for future usefulness, rather than evidence that current agent systems already implement a biologically grounded promotion policy. ([inference]; medium confidence; source: https://arxiv.org/abs/2507.11393; https://colab.ws/articles/10.1038%2Fs41593-023-01382-9)

9. Distillation-only summarization is not a sufficient replacement for structured consolidation when downstream tasks need rule reuse, contradiction handling, or multi-hop reasoning, because summaries are easier to read back but harder to edit, align, and verify. ([inference]; medium confidence; source: https://arxiv.org/abs/2305.10250; https://arxiv.org/abs/2305.14322; https://arxiv.org/abs/2407.04363; https://arxiv.org/abs/2411.05844)

10. Relative to the companion architecture item, this item's distinctive contribution is to show that the least mature step is not trigger plumbing alone but the absence of validated promotion criteria and abstraction-quality benchmarks for semantic generalization. ([inference]; medium confidence; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-agent-memory-consolidation-episodic-semantic.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-agent-memory-evaluation-framework.md; https://arxiv.org/abs/2410.10813)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] MemoryBank and Generative Agents generalize mainly into prose summaries or reflections | https://arxiv.org/abs/2305.10250; https://arxiv.org/abs/2304.03442 | medium | Two primary papers, same representation class |
| [inference] RET-LLM, AriGraph, and LEGO-GraphRAG support more structured semantic promotion than summary-only systems | https://arxiv.org/abs/2305.14322; https://arxiv.org/abs/2407.04363; https://arxiv.org/abs/2411.05844 | medium | Structured facts or graph elements are discrete update units |
| [inference] Consulted promotion thresholds are heuristic signals such as importance, heat, forgetting strength, or goal completion | https://arxiv.org/abs/2304.03442; https://arxiv.org/abs/2305.10250; https://arxiv.org/abs/2506.06326; https://aws.amazon.com/blogs/machine-learning/build-agents-to-learn-from-experiences-using-amazon-bedrock-agentcore-episodic-memory/ | medium | Multiple systems, no shared calibration study |
| [inference] No consulted source validates an evidentially calibrated promotion threshold | https://arxiv.org/abs/2304.03442; https://arxiv.org/abs/2305.10250; https://arxiv.org/abs/2506.06326; https://aws.amazon.com/blogs/machine-learning/build-agents-to-learn-from-experiences-using-amazon-bedrock-agentcore-episodic-memory/; https://arxiv.org/abs/2603.07670 | medium | Absence-of-evidence claim across consulted set |
| [inference] LoCoMo and LongMemEval test downstream memory competence, not promotion precision itself | https://arxiv.org/abs/2402.17753; https://arxiv.org/abs/2410.10813; https://github.com/snap-research/LoCoMo; https://github.com/xiaowu0162/LongMemEval | high | Multiple benchmark descriptions agree on measured targets |
| [fact] LongMemEval adds knowledge updates and abstention and critiques earlier benchmark coverage | https://arxiv.org/abs/2410.10813; https://arxiv.org/html/2410.10813; https://github.com/xiaowu0162/LongMemEval | medium | Strong direct textual support |
| [inference] Structured semantic stores ease localized updates but do not prevent premature commitment | https://arxiv.org/abs/2305.14322; https://arxiv.org/abs/2407.04363; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-autonomous-knowledge-curation-truth-maintenance.md | medium | Technique evidence plus downstream companion item |
| [inference] Complementary Learning Systems supports selective consolidation for future usefulness | https://arxiv.org/abs/2507.11393; https://colab.ws/articles/10.1038%2Fs41593-023-01382-9 | medium | One artificial model plus one neuroscience abstract |
| [inference] Summary-only distillation is weaker than structured consolidation for rule reuse and multi-hop reasoning | https://arxiv.org/abs/2305.10250; https://arxiv.org/abs/2305.14322; https://arxiv.org/abs/2407.04363; https://arxiv.org/abs/2411.05844 | medium | Cross-system comparison, not head-to-head ablation |
| [inference] This item's distinct contribution is the benchmark-and-threshold gap rather than the trigger taxonomy already covered by the companion architecture item | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-agent-memory-consolidation-episodic-semantic.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-agent-memory-evaluation-framework.md; https://arxiv.org/abs/2410.10813 | medium | Cross-item synthesis claim |

### Assumptions

No public benchmark directly scores the correctness of the semantic abstraction at the exact moment of promotion, distinct from later answer quality or retrieval accuracy. [assumption; source: https://arxiv.org/abs/2402.17753; https://arxiv.org/abs/2410.10813] This is justified by the consulted benchmark set for this item and by the completed evaluation-framework companion item, but it remains an assumption because an unreviewed or unconsulted benchmark could exist outside this search. [assumption; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-agent-memory-evaluation-framework.md]

A promotion policy that is calibrated on conversational or text-game episodes will not transfer unchanged to code-repository or research-workflow agents, because the evidence granularity, verification affordances, and error costs differ materially across those domains. [assumption; source: https://arxiv.org/abs/2407.04363; https://aws.amazon.com/blogs/machine-learning/build-agents-to-learn-from-experiences-using-amazon-bedrock-agentcore-episodic-memory/] This is justified by AriGraph operating in text-game environments and AgentCore operating in enterprise workflows, which shows representation ideas can transfer across domains while leaving threshold calibration domain-specific. [assumption; source: https://arxiv.org/abs/2407.04363; https://aws.amazon.com/blogs/machine-learning/build-agents-to-learn-from-experiences-using-amazon-bedrock-agentcore-episodic-memory/]

### Analysis

The evidence base supports a clear separation between "can the agent abstract?" and "does the agent know when the abstraction is good enough to keep?" [inference; source: https://arxiv.org/abs/2305.10250; https://arxiv.org/abs/2304.03442; https://arxiv.org/abs/2305.14322; https://arxiv.org/abs/2407.04363] MemoryBank, Generative Agents, RET-LLM, AriGraph, Memory OS, and AgentCore all answer the first question positively, because each one contains an explicit step that turns many local traces into a more reusable representation. [inference; source: https://arxiv.org/abs/2305.10250; https://arxiv.org/abs/2304.03442; https://arxiv.org/abs/2305.14322; https://arxiv.org/abs/2407.04363; https://arxiv.org/abs/2506.06326; https://aws.amazon.com/blogs/machine-learning/build-agents-to-learn-from-experiences-using-amazon-bedrock-agentcore-episodic-memory/] They answer the second question only weakly, because their promotion decisions depend on heuristic signals that are plausible but not benchmarked as calibrated evidence thresholds. [inference; source: https://arxiv.org/abs/2304.03442; https://arxiv.org/abs/2305.10250; https://arxiv.org/abs/2506.06326; https://aws.amazon.com/blogs/machine-learning/build-agents-to-learn-from-experiences-using-amazon-bedrock-agentcore-episodic-memory/; https://arxiv.org/abs/2603.07670]

A plausible rival explanation is that no special consolidation policy is needed at all, because larger context windows and better retrieval can simply keep the raw episodes available and let the model infer the right generalization on demand. [inference; source: https://arxiv.org/abs/2402.17753; https://arxiv.org/abs/2410.10813] The consulted benchmarks do not support that rival strongly, because LoCoMo shows persistent difficulty with long-range temporal and causal integration and LongMemEval reports large performance drops even for long-context systems on sustained interactive memory tasks. [inference; source: https://arxiv.org/abs/2402.17753; https://arxiv.org/abs/2410.10813] Raw retrieval therefore reduces forgetting pressure but does not remove the need for selective abstraction, especially when the downstream system must reuse a rule, update a world model, or compress knowledge for repeated multi-step planning. [inference; source: https://arxiv.org/abs/2305.14322; https://arxiv.org/abs/2407.04363; https://arxiv.org/abs/2603.07670]

This item therefore differs materially from the completed architecture companion. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-agent-memory-consolidation-episodic-semantic.md] The companion item mapped trigger families, provenance, and intermediate representations across architectures; this item shows that the least mature control surface is the semantic-promotion decision rule itself and the lack of a benchmark that scores that decision directly. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-agent-memory-consolidation-episodic-semantic.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-agent-memory-evaluation-framework.md] Put differently, the field has several ways to write semantic memory, but it does not yet have a convincing way to prove that a given write was epistemically justified at the moment it happened. [inference; source: https://arxiv.org/abs/2410.10813; https://arxiv.org/abs/2603.07670]

### Risks, Gaps, and Uncertainties

- The benchmark-gap conclusion is based on the consulted benchmark set for this item, not on an exhaustive census of every 2024 to 2026 memory benchmark. [assumption; source: https://arxiv.org/abs/2402.17753; https://arxiv.org/abs/2410.10813]
- Several of the most relevant sources are arXiv preprints or vendor engineering reports rather than long-settled peer-reviewed literature, which is appropriate for a fast-moving topic but lowers confidence in precise effect-size comparisons across systems. [assumption; source: https://arxiv.org/abs/2305.10250; https://arxiv.org/abs/2407.04363; https://aws.amazon.com/blogs/machine-learning/build-agents-to-learn-from-experiences-using-amazon-bedrock-agentcore-episodic-memory/]
- AriGraph provides the clearest autonomous Knowledge Graph example in the consulted set, but its evidence comes from text-game environments rather than repository engineering or enterprise research workflows. [inference; source: https://arxiv.org/abs/2407.04363]
- The selective-consolidation lesson from Complementary Learning Systems is conceptually relevant, but the consulted AI implementations do not yet operationalize it as a validated promotion rule tied to later task utility. [inference; source: https://arxiv.org/abs/2507.11393; https://colab.ws/articles/10.1038%2Fs41593-023-01382-9; https://arxiv.org/abs/2603.07670]

### Open Questions

- What benchmark would directly score semantic-promotion precision, meaning whether the stored abstraction was the right generalization at the time of promotion rather than merely a useful retrieval artifact later?
- What evidence policy is defensible for promotion in production agents: repeated occurrence, source diversity, counter-example testing, downstream reward, or a composite rule?
- Can a structured semantic memory carry enough provenance, uncertainty, and temporal scope to support later truth maintenance without becoming too expensive to update online?
- Which domains, code agents, research agents, customer-support agents, or game agents, need different threshold calibration because their episodes differ in verifiability and error cost?

---

## Output

- Type: knowledge
- Description: This item produces a technique-and-evaluation synthesis showing that current episodic-to-semantic consolidation systems are strongest at generating candidate abstractions and weakest at validating when those abstractions are justified, because benchmark coverage for promotion quality still lags behind benchmark coverage for retrieval and update handling. [inference; source: https://arxiv.org/abs/2410.10813; https://arxiv.org/abs/2603.07670; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-07-20-agent-memory-evaluation-framework.md]
- Links: [LongMemEval](https://arxiv.org/abs/2410.10813), [AriGraph](https://arxiv.org/abs/2407.04363), [Amazon Bedrock AgentCore episodic memory](https://aws.amazon.com/blogs/machine-learning/build-agents-to-learn-from-experiences-using-amazon-bedrock-agentcore-episodic-memory/)
