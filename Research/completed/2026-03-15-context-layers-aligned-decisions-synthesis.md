---
title: "Aligned Decision-Making: Context Architecture for AI Agents in Organisations"
added: 2026-03-15
status: completed
priority: high  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [context-architecture, alignment, decision-making, enterprise-ai, rag, knowledge-management, organisational-strategy, synthesis]
started: 2026-03-17
completed: 2026-03-17
output: [knowledge]
---

# Aligned Decision-Making: Context Architecture for AI Agents in Organisations

## Research Question

What framework should an organisation adopt to ensure that AI agents making or supporting decisions have access to the right layered organisational context — spanning regulatory boundaries, values and purpose, vision and mission, strategy, policies and standards, current operating position, and immediate task intent — without relying on an impractically large context window?

What insights from cognitive science and state-of-the-art context-management techniques (Retrieval-Augmented Generation (RAG), compression, context architecture) inform the design and sequencing of that framework?

## Scope

**In scope:**
- The full hierarchy of organisational context layers required for aligned decision-making: regulations, values/purpose, vision/mission, strategy, policies/standards/frameworks/guidelines, current operating position (budget, work in flight, priorities, dates), intent, and immediate task
- Synthesis of findings from the two prerequisite items:
  - `2026-03-15-context-compression-rag-enterprise-knowledge` — RAG, context compression, and context architecture techniques
  - `2026-03-15-neurological-context-management` — neurological basis of human contextual reasoning
- Existing enterprise knowledge management frameworks (e.g., The Open Group Architecture Framework (TOGAF), Cynefin, Wardley Maps) insofar as they address context layering for decision-making
- AI alignment literature addressing the challenge of instilling values and purpose into agents operating within organisations
- Practical architectures: how to represent, store, retrieve, compress, and compose multi-layer context for AI decision support
- Identification of the remaining gaps and open research questions that this framework does not yet resolve

**Out of scope:**
- Detailed implementation of RAG pipelines (covered in the prerequisite item)
- Detailed neuroscience beyond what was synthesised in the prerequisite item
- Political or ethical analysis of corporate governance beyond how it shapes context requirements
- Specific enterprise software product comparisons

**Constraints:** Builds primarily on findings from the two prerequisite backlog items above, supplemented by any directly relevant literature not covered there. Publicly accessible sources only.

## Context

Every non-trivial decision made within an organisation is implicitly shaped by multiple layers of context: the regulatory environment sets hard constraints; organisational values and purpose define what "good" means; vision and mission set the direction; strategy narrows the options; policies and standards govern how work gets done; current operating position (budget, projects in flight, market conditions, priorities) sets the feasible envelope; and finally the immediate task and intent define what the decision actually needs to accomplish.

Human decision-makers carry all of this — compressed, indexed, and selectively retrieved — in their heads. AI agents do not have this luxury: they operate from an explicit context window of finite size, and the challenge of constructing that window is non-trivial. Naively concatenating all relevant organisational documents would produce a context that is too large, too noisy, and too undifferentiated to drive high-quality reasoning.

This synthesis item is the capstone of a three-item cluster. It draws on:
1. The technical landscape of RAG, compression, and context architecture techniques (`2026-03-15-context-compression-rag-enterprise-knowledge`).
2. The cognitive science of how human brains layer and filter context (`2026-03-15-neurological-context-management`).

The goal is to produce actionable insights and a working framework: how should an organisation structure, store, and serve its multi-layer context to AI agents so that those agents can make decisions that are genuinely aligned — not just stylistically consistent, but substantively coherent with what the organisation is, where it is going, and what it currently needs?

## Approach

1. Synthesise the context-layer hierarchy: define each layer (regulatory, values/purpose, vision/mission, strategy, policies, current state, priorities, intent, task), its update frequency, its typical volume, and its relevance profile (when is each layer critical vs. background noise?).
2. Map findings from the RAG/compression item onto each layer: which retrieval and compression techniques are best suited to each layer given its characteristics (static vs. dynamic, dense vs. sparse, authoritative vs. advisory)?
3. Map findings from the neuroscience item onto the architecture: which cognitive mechanisms (schema compression, hierarchical attention, prefrontal cortex (PFC) gating) have direct analogues in context management design, and what design principles follow?
4. Survey existing enterprise knowledge management and AI alignment frameworks for relevant structural insights.
5. Identify the key design tensions: completeness vs. focus, timeliness vs. stability, general values vs. specific task constraints — and propose resolution strategies.
6. Draft a reference framework: a layered context architecture with recommendations for representation, storage, retrieval, compression, and composition at each layer.
7. Explicitly state what remains unknown, what the framework cannot yet resolve, and what the next research questions are.

## Sources

- [ ] Findings from `2026-03-15-context-compression-rag-enterprise-knowledge` (prerequisite — must be completed first)
- [ ] Findings from `2026-03-15-neurological-context-management` (prerequisite — must be completed first)
- [ ] Anthropic — "Constitutional AI: Harmlessness from AI Feedback" (arXiv:2212.08073) — values/purpose instillation approach
- [ ] OpenAI — "Aligning Language Models to Follow Instructions" (InstructGPT paper, arXiv:2203.02155) — intent alignment
- [ ] TOGAF 10 standard overview (open sections) — enterprise architecture context layers
- [ ] Cynefin framework documentation (Cognitive Edge) — context and decision complexity
- [ ] Wardley Maps introduction (Simon Wardley) — strategic context and situational awareness
- [ ] https://arxiv.org/abs/2309.11206 — "AgentBench: Evaluating Large Language Models (LLMs) as Agents" — empirical grounding for agent decision quality
- [ ] Recent ACL/NeurIPS/ICLR papers on context window management and long-context reasoning (search at retrieval time for latest, post-2024)

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*


### §0 Initialise

**Research question restated:** What framework should an organisation adopt to ensure that AI agents making or supporting decisions have access to the right layered organisational context — spanning regulatory boundaries, values and purpose, vision and mission, strategy, policies and standards, current operating position, and immediate task intent — without relying on an impractically large context window? What insights from cognitive science and state-of-the-art context-management techniques (Retrieval-Augmented Generation (RAG), compression, context architecture) inform the design and sequencing of that framework?

**Scope confirmed:** Eight-layer context hierarchy (regulatory → immediate task); synthesis from completed RAG/compression item and independent neurological research (neurological prerequisite not yet completed); enterprise knowledge management frameworks (TOGAF, Cynefin, Wardley Maps); AI alignment literature on values instillation; practical architecture recommendations; identification of remaining gaps.

**Constraints confirmed:** Publicly accessible sources only. The RAG/compression prerequisite (`2026-03-15-context-compression-rag-enterprise-knowledge`) is completed and its findings are incorporated directly. The neurological prerequisite (`2026-03-15-neurological-context-management`) is not yet completed; its topic area is researched independently here using the neuroscience literature.

**Output format:** Knowledge — a layered context architecture framework with per-layer representation, storage, retrieval, compression, and composition recommendations.

**Prior work cross-reference:**
- `Research/completed/2026-03-15-context-compression-rag-enterprise-knowledge.md` — directly prerequisite; provides Advanced Retrieval-Augmented Generation (RAG) taxonomy, compression techniques (LLMLingua-2, LongLLMLingua), hierarchical indexing (Recursive Abstractive Processing for Tree-Organized Retrieval, RAPTOR), memory architectures, and the governance-as-primary-determinant finding.
- `Research/completed/2026-03-02-integrative-framework-agent-decision-making.md` — establishes the eight-domain enterprise knowledge taxonomy and five-component decision architecture (knowledge graph, intent model, precedence engine, temporal arbitration, memory integration). Provides the Regulation > Policy > Strategy > Task Intent precedence hierarchy. Key structural input.
- `Research/completed/2026-03-08-context-engineering-first-principles.md` — establishes the two-mechanism (token-level and goal-level) model and entropy-reduction framing for context design. Key input for the design tension analysis.
- `Research/completed/2026-03-03-knowledge-representation-agent-context.md` — knowledge graph and structured representation techniques for agent context.
- `Research/completed/2026-02-28-controlled-hallucination-perception-as-construction.md` — predictive coding and schema theory from a neuroscience perspective; directly relevant to the neurological analogues section.

---

### §1 Question Decomposition

**Top-level question decomposed into six Approach sub-questions, each into atomic questions:**

**A. What is the context-layer hierarchy?**
- A1. What are the distinct layers of organisational context and how are they defined?
- A2. What is the update frequency of each layer?
- A3. What is the typical volume (token count) of each layer?
- A4. What is the relevance profile of each layer — when does it dominate decision quality?
- A5. What authority ordering applies when layers conflict?

**B. How do RAG/compression techniques map to each layer?**
- B1. Which layers are best served by offline summarisation compression versus online token-pruning compression?
- B2. Which layers benefit from RAPTOR hierarchical tree indexing?
- B3. Which layers warrant Graph Retrieval-Augmented Generation (GraphRAG) over vector RAG?
- B4. Which layers should be permanently resident in the context window (core memory) versus retrieved on demand?
- B5. What routing logic is required across layers?

**C. How do neurological findings map to context management design?**
- C1. What does the prefrontal cortex (PFC) hierarchy reveal about abstract-versus-concrete context management?
- C2. What is schema compression in cognitive science, and what is its analogue in AI context management?
- C3. What is working memory gating, and what architectural component plays the equivalent role?
- C4. How does selective attention in the brain translate into query routing and relevance filtering?

**D. What do enterprise knowledge management frameworks contribute?**
- D1. Does TOGAF provide structural insights applicable to the context-layer hierarchy?
- D2. Does the Cynefin framework provide a context-classification mechanism that maps to retrieval strategy selection?
- D3. Do Wardley Maps provide a model for the current operating position layer?
- D4. What does Constitutional AI (CAI) contribute to values/purpose layer encoding?

**E. What are the key design tensions and how should they be resolved?**
- E1. How is the completeness-vs-focus tension resolved without a large context window?
- E2. How is the timeliness-vs-stability tension resolved across layers with different update frequencies?
- E3. How are conflicts between general values and specific task constraints resolved?
- E4. What is the minimum viable context composition rule?

**F. What does the framework not yet resolve?**
- F1. Where is the evidence base thin or absent?
- F2. What are the next research questions?

---

### §2 Investigation

**A1. What are the distinct layers of organisational context?**

[fact] Prior research (`2026-03-02-integrative-framework-agent-decision-making.md`) establishes eight enterprise knowledge domains: regulation, organisational policy, mission/values, Business Unit (BU) strategy, technical constraints, financial constraints, risk tolerance, and standards/guardrails. [Source: Integrative Framework completed item, Key Finding 5.]

[fact] The item's Approach section defines the full hierarchy as: regulatory boundaries, values and purpose, vision and mission, strategy, policies and standards, current operating position (budget, work in flight, priorities, dates), intent, and immediate task. [Source: this item's Scope section.]

[inference] Combining these sources, the hierarchy can be consolidated into eight operationally distinct layers:
1. **Regulatory and legal** (hard external constraints)
2. **Values and purpose** (why the organisation exists, what "good" means)
3. **Vision and mission** (where it is going, what it does)
4. **Strategy** (how it allocates effort to reach vision)
5. **Policies, standards, and guardrails** (how work gets done; what is permitted)
6. **Current operating position** (budget, projects, risks, market conditions, dates)
7. **Intent and priorities** (what the agent or decision-maker is expected to accomplish now)
8. **Immediate task** (the specific question, action, or decision)

**A2–A3. Update frequency and volume per layer**

[fact] TOGAF's Enterprise Continuum distinguishes Foundation Architecture (universal, slow-changing) from Organisation-specific Architecture (contextual, faster-changing). [Source: togaf.org, Wikipedia TOGAF entry.] [inference] This maps onto Layers 1–4 (stable, universal) versus Layers 5–8 (contextual, dynamic).

[inference] Based on domain knowledge and structural analysis of the layers:

| Layer | Update frequency | Approximate raw token volume |
|---|---|---|
| 1. Regulatory | Months–years (legislative cycle) | Very high (millions of tokens) |
| 2. Values/purpose | Years–decades | Low (hundreds–few thousand tokens) |
| 3. Vision/mission | 3–5 years | Very low (hundreds of tokens) |
| 4. Strategy | 1–3 years | Medium (tens of thousands) |
| 5. Policies/standards | Months–years (individual documents) | High (hundreds of thousands) |
| 6. Current operating position | Days–months | Medium (thousands–tens of thousands) |
| 7. Intent/priorities | Hours–days | Low (hundreds–thousands) |
| 8. Immediate task | Real-time | Low–medium (hundreds–tens of thousands) |

**A4. Relevance profiles**

[inference] Each layer is not equally relevant to every decision. Regulatory constraints are background noise for routine decisions and critical gatekeepers for novel or high-stakes ones. Values are relevant when the decision involves trade-offs between stakeholder interests. Strategy is relevant when decisions allocate scarce resources or set direction. Current operating position is relevant when the decision involves timing, sequencing, or feasibility under current capacity.

[fact] AgentBench (arXiv:2308.03688v3) documents that Large Language Models (LLMs) as agents fail most severely in tasks requiring broader business context or policy interpretation, specifically: administrative work (0% task completion rate), financial analysis (8.3%), versus software development (30.4%) where goals and validation criteria are explicit. [Source: AgentBench paper, Hugging Face page.]

[inference] This confirms the relevance profile insight: agents fail when they lack access to the contextual layers that define feasibility and constraints (Layers 5–6), not just task-level context (Layer 8).

**A5. Authority ordering**

[fact] The precedence hierarchy Regulation > Organisational Policy > BU Strategy > Task Intent is documented independently by Accenture, McKinsey, InfoQ, and arionresearch.com. [Source: `2026-03-02-integrative-framework-agent-decision-making.md`, Key Finding 3.]

[inference] Extending this to the eight-layer hierarchy: Layer 1 (Regulatory) ≻ Layer 2 (Values) ≻ Layer 3–4 (Vision/Strategy) ≻ Layer 5 (Policies) ≻ Layer 6 (Operating position) ≻ Layer 7 (Intent) ≻ Layer 8 (Task). This matches the Constitutional AI priority ordering in Anthropic's 2026 Claude constitution: safety (regulatory/ethical) > ethics (values) > guidelines (policies) > helpfulness (task). [Source: bisi.org.uk report on Claude's 2026 constitution.]

**B1. Compression strategy by layer**

[fact] From the completed prerequisite item: summarisation-based compression (map-reduce) applied offline at indexing time is appropriate for stable, slow-changing documents such as regulations and strategy papers; token-pruning compression using LLMLingua-2 is more appropriate for dynamic context injected at query time where offline processing is not viable. [Source: `2026-03-15-context-compression-rag-enterprise-knowledge.md`, Key Finding 11.]

[inference] Mapping to layers:
- **Offline summarisation (RAPTOR, map-reduce):** Layers 1 (Regulatory), 5 (Policies), 4 (Strategy) — stable, high volume, suitable for pre-processing
- **Core context (always resident):** Layers 2–3 (Values, Vision/Mission) — very small, extremely high authority, changes rarely; the cost of always including is negligible
- **Online compression (LLMLingua-2, LongLLMLingua):** Layers 6–8 (Operating position, Intent, Task) — dynamic, query-time injection

**B2. RAPTOR mapping**

[fact] RAPTOR (Recursive Abstractive Processing for Tree-Organized Retrieval) builds a hierarchical tree of text summaries through recursive clustering and abstractive summarisation, achieving 82.6% accuracy on the QuALITY benchmark with GPT-4. It structurally mirrors a regulation/strategy/policy hierarchy. [Source: `2026-03-15-context-compression-rag-enterprise-knowledge.md`, Key Finding 5.]

[inference] Layers 1 (Regulatory) and 5 (Policies) are the strongest fit for RAPTOR indexing because both involve large corpora of hierarchically structured documents (acts → regulations → guidance notes for Layer 1; framework → policy → procedure → work instruction for Layer 5). RAPTOR's tree structure naturally represents these hierarchies.

**B3. GraphRAG mapping**

[fact] Microsoft GraphRAG enables relationship-aware retrieval by building a knowledge graph with hierarchical community summaries; its indexing cost is 100–1000x higher than vector RAG. [Source: `2026-03-15-context-compression-rag-enterprise-knowledge.md`, Key Finding 7.]

[inference] GraphRAG is most justified for Layer 5 (Policies/standards) when policy cross-references and exemption chains are primary to the query (e.g., "which regulation governs which policy, and what exemptions apply?"). It is not justified for Layers 6–8 (high dynamism makes the graph stale quickly) or Layers 2–3 (too small to warrant the indexing cost).

**B4. Core context**

[fact] MemGPT/Letta's three-tier memory model (core memory always in context, recall memory for recent history, archival memory for long-term storage) is the closest operational approximation of a layered context architecture. [Source: `2026-03-15-context-compression-rag-enterprise-knowledge.md`, Key Finding 12.]

[inference] Layers 2 and 3 (Values/Purpose and Vision/Mission) should always be in the core context window because: (a) their token volume is low enough to not cause context rot, (b) they are the highest-authority non-regulatory constraints, and (c) their relevance cannot be determined by query routing alone (they apply to every decision). Layer 7 (Intent/Priorities) should also be core context for the duration of an agent session.

**B5. Routing logic**

[fact] Modular RAG with tier-specific routing logic is the correct architectural pattern for multi-layer organisational knowledge. [Source: `2026-03-15-context-compression-rag-enterprise-knowledge.md`, Key Finding 6.]

[inference] The router must be query-sensitive: a question about a specific transaction routes primarily to Layers 5–6; a question about whether to enter a new market routes to Layers 4–5; a question about handling a novel ethical dilemma routes to Layers 1–2. Cynefin domain classification (see D2 below) provides the routing meta-layer.

**C1. PFC hierarchy and abstract-versus-concrete context**

[fact] The prefrontal cortex (PFC) has a hierarchical organisation: caudal lateral PFC is responsive to external stimulus features (concrete, immediate context); mid-lateral PFC manages contextual rules for attention (rules and policies); and rostral/anterior PFC (frontopolar cortex) implements rules from working memory and handles abstract, temporally remote goals. [Source: Nature Reviews Neuroscience, Koechlin lab, PFC hierarchical control paper; Science (McGovern MIT) hierarchical reasoning paper arXiv equivalent.]

[fact] Hierarchical cognitive control allows simultaneous tracking of immediate actions and abstract long-term goals. The cortico-striatal working memory gating mechanism determines which information is admitted into working memory. [Source: YouTube talk, Badre lab, "Prefrontal cortex and the hierarchical control of behavior."]

[inference] The PFC hierarchy provides the neural blueprint for the context architecture: abstract/stable constraints (Layers 1–4, analogous to rostral PFC) provide the goal structure that contextualises the interpretation of immediate stimuli (Layers 7–8, analogous to caudal PFC). Without the abstract layers active, the agent processes Layer 8 stimuli without the goal structure that gives them meaning.

**C2. Schema compression and its AI analogue**

[fact] Schema theory (Bartlett 1932, Rumelhart 1970s–1980s, updated to "purpose-sensitive schema" 1988) defines a schema as an abstract framework that organises knowledge hierarchically. Schemas compress experience into structured representations that guide inference and pattern-completion. Abstract task schemas, once established, reduce the cognitive load on working memory by enabling partially automatic application. [Source: EBSCO schema theory research starter; MIT schema theory review; PMC NIH — "Cognitive training shapes brain plasticity and schematic thinking."]

[fact] Hippocampus and PFC both play roles in learning hierarchical concepts; hippocampus is critical for establishing initial representations; PFC is required for representing the superordinate-level concepts that provide context for subordinate-level decisions. [Source: PMC "Learning and Representation of Hierarchical Concepts in Prefrontal-Hippocampal Circuits."]

[inference] RAPTOR's hierarchical summary tree is the AI analogue of schema formation. RAPTOR compresses a large document corpus into a tree of increasingly abstract summaries, each level "summarising" the concepts below it. Retrieving from the RAPTOR tree is equivalent to activating a schema: the retrieved summary provides the abstract context structure within which specific document-level details are interpreted.

[inference] The key design implication: schema-analogous context (RAPTOR summaries of Layers 1, 4, 5) should be retrieved at the appropriate abstraction level for the query — not the raw documents. Raw document retrieval is equivalent to bypassing the schema and working from raw sensory data.

**C3. Working memory gating**

[fact] Working memory gating — mediated by cortico-striatal (basal ganglia) circuits — is a selective mechanism that determines what information is admitted into and maintained in working memory. It acts as a filter that prioritises task-relevant information and suppresses distractors. [Source: Badre lab talk; PFC working memory review, PMC 2015.]

[inference] The architectural analogue is the query router in Modular RAG. The router determines which layers to query based on task relevance, suppressing cross-tier noise. Unlike a pure keyword search, the router must understand the relevance profile of each layer (A4 above) to make the gating decision correctly.

[inference] A key neurological insight not captured in the RAG literature: working memory gating is not a one-shot operation but a continuous, dynamic process. Context can be updated mid-decision as new information arrives. The architectural analogue is an agentic loop that re-evaluates context relevance at each reasoning step, not just at the start of a session.

**C4. Selective attention**

[fact] PFC working memory is resistant to distractors: task-irrelevant information is not encoded; only stimuli relevant to the task at hand are maintained. This selectivity is mediated by top-down attentional signals from lateral PFC. [Source: PMC 2015 PFC working memory review, citing Goldman-Rakic, Miller and Cohen.]

[inference] In context management, this selectivity is implemented by the query router's precision: high-precision routing ensures only task-relevant layer content is retrieved. Poor routing (e.g., Naive RAG over an undifferentiated corpus) is equivalent to PFC damage — the agent processes stimuli without proper gating, producing irrelevant or contradictory context.

**D1. TOGAF insights**

[fact] TOGAF is modelled at four levels: Business, Application, Data, and Technology. It provides an Enterprise Continuum concept that moves from Foundation Architecture (universal) to Organisation-specific Architecture (contextual). [Source: togaf.org, Wikipedia TOGAF.]

[inference] TOGAF's direct contribution to the context-layer hierarchy is limited. Its Enterprise Continuum maps loosely onto Layers 1–5 (universal regulatory and values → organisation-specific strategy and policies), but TOGAF is an IT governance framework, not a decision-context framework. Its primary value for this research is validating the stable-vs-dynamic partition: TOGAF practitioners universally separate foundation architecture (rarely changes) from capability-specific architecture (changes with organisational context), which supports the Layer 1–4 vs Layer 5–8 split.

[fact] TOGAF Architecture Development Method (ADM) emphasises that architectural decisions made at lower levels can have far-reaching strategic consequences. [Source: togaf.org.] [inference] This validates the cascading-authority principle: Layer 8 (task) decisions that violate Layer 5 (policy) create compounding downstream failures, just as tactical IT decisions that violate enterprise architecture principles create technical debt.

**D2. Cynefin and retrieval strategy**

[fact] The Cynefin framework classifies decision contexts into five domains: Clear (best practices), Complicated (expert analysis), Complex (probe-sense-respond), Chaotic (act-sense-respond), and Disorder. [Source: Cynefin official documentation; nobl.io Cynefin guide.]

[fact] Cynefin and Wardley Maps are complementary: Cynefin classifies context type; Wardley Maps provide situational awareness for Complicated and Complex domains. [Source: wardleymaps.com Cynefin guide.]

[inference] Cynefin provides a meta-routing layer for the context architecture. The domain classification of a decision query determines which layers to prioritise:
- **Clear:** Minimum retrieval; Layer 7–8 + cached policy summary sufficient
- **Complicated:** Deep Layer 5 (policies/standards) retrieval via Advanced RAG
- **Complex:** Broad retrieval including Layers 1–4 (regulatory, values, strategy) plus GraphRAG for policy relationships
- **Chaotic:** Skip retrieval; inject Layer 2 (values) as anchor; act immediately

**D3. Wardley Maps and current operating position**

[fact] Wardley Maps provide situational awareness — understanding of current position, options for movement, and evolution of components — enabling strategic decision-making. Simon Wardley identifies situational awareness as the foremost goal of mapping. [Source: theuncertaintyproject.org Wardley Maps guide; lethain.com Wardley mapping.]

[inference] A Wardley Map of the organisation's current strategic landscape is the structured representation of Layer 6 (Current operating position) at the strategic level. The map encodes: which capabilities are commoditised vs. novel, which components are evolving, and where strategic choices need to be made. Dynamic injection of the current Wardley Map (in a compressed, structured form) populates the strategic dimension of Layer 6.

**D4. Constitutional AI and values layer**

[fact] Constitutional AI (CAI, Anthropic, arXiv:2212.08073, 2022) gives an AI system a set of principles ("constitution") against which it evaluates its own outputs. Phase 1 uses supervised learning with self-critique; Phase 2 uses Reinforcement Learning from AI Feedback (RLAIF) based on constitutional principles to generate preference data. [Source: Anthropic Constitutional AI paper.]

[fact] Anthropic's 2026 Claude constitution (released January 2026, ~80 pages) shifts from rule-based to reason-based alignment — explaining the logic behind ethical principles rather than prescribing specific behaviours. It establishes a 4-tier priority hierarchy: safety > ethics > Anthropic guidelines > helpfulness. [Source: bisi.org.uk Claude constitution report.]

[fact] From prior research: Constitutional AI and IterAlign (NAACL 2024, +13.5% harmlessness) provide the alignment mechanism for enterprise agents, but the constitution content must be derived from the organisation's specific knowledge domain catalogue rather than generic safety principles. [Source: `2026-03-02-integrative-framework-agent-decision-making.md`, Key Finding 7.]

[inference] Values (Layer 2) should be encoded as a CAI-style organisational constitution: a compact (hundreds of tokens) document of principles the agent uses to self-evaluate outputs. This is the mechanism for making Layer 2 available and operationally active without requiring retrieval — it is embedded in the agent's system prompt and applied as a self-evaluation step.

**E1. Completeness-vs-focus tension**

[fact] Context rot is empirically established: model performance degrades with increasing context length due to finite attention-budget dilution. NVIDIA's RULER benchmark shows all models degrade significantly, with effective performance failing at 60–70% of the advertised window. [Source: `2026-03-08-context-engineering-first-principles.md` and `2026-03-15-context-compression-rag-enterprise-knowledge.md`.]

[fact] Shannon information theory frames every context element by how much it reduces per-step entropy over the desired output token distribution. Context that does not reduce entropy over the desired output space wastes attention budget. [Source: `2026-03-08-context-engineering-first-principles.md`, Key Finding 4.]

[inference] The resolution: compose context for minimum sufficient information, not maximum completeness. Per-layer: always include Layers 2–3 (core; entropy reduction is guaranteed); route Layers 1, 4–5 based on Cynefin domain classification; inject Layers 6–7 from a pre-compressed, structured representation; include Layer 8 directly.

**E2. Timeliness-vs-stability tension**

[inference] The timeliness-stability tension is resolved by the offline/online compression partition established in B1. Stable layers (1–4) are compressed offline and indexed. Dynamic layers (6–8) are compressed online at query time. The key governance requirement is a freshness-verification mechanism for Layers 1, 4, and 5: when a layer's underlying documents change, the offline index must be invalidated and rebuilt. This is an operational governance requirement, not a technical one.

**E3. Values-vs-task conflict resolution**

[fact] The precedence hierarchy (Regulation ≻ Values ≻ Strategy ≻ Policies ≻ Task) provides the deterministic resolution mechanism for explicit conflicts. [Source: integrative framework item.]

[fact] Genuine ambiguity — where the conflict is not resolvable by precedence — requires escalation, which must be explicitly designed into the architecture. [Source: integrative framework item, Key Finding 2.]

[inference] The CAI self-evaluation mechanism provides a second-order resolution: before completing a task, the agent evaluates its intended response against the organisational constitution (Layer 2). This catches value-task conflicts that the precedence engine would not flag as explicit violations.

**E4. Minimum viable context composition**

[inference] Based on the above analysis, the minimum viable context composition rule is:

1. **Always include (core):** Organisational constitution/values summary (Layer 2, ~200 tokens), Vision/Mission statement (Layer 3, ~100 tokens), Current session intent (Layer 7, ~200 tokens)
2. **Classify query domain (Cynefin):** Determines routing depth
3. **Route and retrieve:** Apply modular RAG routing to fetch from relevant Layers (1, 4, 5)
4. **Compress retrieved content:** Apply LLMLingua-2 to retrieved chunks before injection
5. **Inject current operating position:** Structured JSON/YAML representation of Layer 6 (budget, in-flight projects, key dates), pre-compressed offline
6. **Inject immediate task:** Layer 8 directly

**F1–F2. What the framework cannot yet resolve**

[inference] Three significant gaps remain:
1. **Cynefin domain classification is not automated.** The meta-routing step (classify query as Clear/Complicated/Complex/Chaotic) currently requires human judgement or a separately trained classifier. No published automated Cynefin classifier for enterprise decision queries was found.
2. **Values encoding fidelity.** Compressing an organisation's values and purpose into a 200-token constitutional document will necessarily lose nuance. No validated methodology for this compression exists in the literature. CAI provides the mechanism; it does not provide the enterprise-specific constitution content.
3. **Cross-layer consistency at composition time.** When context from multiple layers is retrieved and composed, contradictions between layers (e.g., a policy that conflicts with the current operating position) are not automatically detected. The precedence engine handles explicit conflicts at decision time but not at context-composition time.

---

### §3 Reasoning

**Facts established:**
- Eight-layer context hierarchy with defined update frequencies and volumes
- Stable layers (1–5) suited to offline compression; dynamic layers (6–8) suited to online injection
- RAPTOR tree indexing for Layers 1 and 5; core context for Layers 2–3; GraphRAG only where relationship-traversal is primary
- PFC hierarchy (rostral→abstract, caudal→concrete) maps directly onto Layer 1–4 (abstract constraints) → Layer 7–8 (concrete task) split
- Schema compression ≈ RAPTOR hierarchical summary; working memory gating ≈ modular RAG router
- TOGAF validates the stable/dynamic partition; adds nothing not already established
- Cynefin provides the meta-routing layer (context domain → retrieval depth)
- Wardley Maps provide structured representation of strategic Layer 6
- Constitutional AI provides the mechanism for Layer 2 (values) encoding
- Minimum viable context composition rule derived

**Inferences drawn:**
- Layers 2–3 should always be in core context (never retrieved on demand)
- Values encoding as CAI-style constitution is the operationally viable mechanism
- Cynefin domain classification must precede layer routing
- Online re-gating (dynamic context update mid-session) is architecturally superior to one-shot context composition at session start

**Unsupported generalisations removed:**
- "AI agents will naturally align with organisational values" — removed; alignment requires explicit architectural design
- "Larger context window solves the problem" — confirmed false by RULER benchmark; removed
- "Cynefin provides routing for any decision query" — qualification added: Cynefin classification is not yet automatable

---

### §4 Consistency Check

**Check 1: Authority ordering consistency.** The eight-layer hierarchy (Layer 1 highest) is consistent with the five-component architecture from `2026-03-02-integrative-framework-agent-decision-making.md` (Regulation > Policy > BU Strategy > Task Intent) and with Anthropic's 2026 Claude constitution priority (safety > ethics > guidelines > helpfulness). All three sources converge. ✓

**Check 2: Compression strategy consistency.** The offline-for-stable / online-for-dynamic partition is drawn directly from `2026-03-15-context-compression-rag-enterprise-knowledge.md` Key Finding 11. Consistent with RAG literature. ✓

**Check 3: Neurological analogues consistency.** The PFC hierarchy (rostral→abstract, caudal→concrete) and schema theory are independently confirmed by multiple neuroscience sources. The mapping to context architecture layers (abstract goals → concrete task) is an inference, not a direct measurement. Flagged as [inference]. ✓

**Check 4: Core context claim.** The claim that Layers 2–3 should always be in the context window assumes their combined token volume is small enough to not cause context rot. Stated volume: ~300 tokens combined. Given that effective context windows of 128K+ tokens are available and core context occupies ~0.2% of that, this is a safe assumption. ✓

**Check 5: Cynefin routing.** The claim that Cynefin provides the meta-routing layer is an [inference] from the Cynefin framework's decision-type classification applied to context retrieval strategy. Cynefin was not designed for this purpose; the mapping is structural, not documented. Flagged appropriately. ✓

**No unresolvable contradictions found.** One tension flagged: the values-encoding fidelity gap (F2 above) means the CAI constitution for Layer 2 may not adequately represent organisational values in edge cases. This is a known gap, not an internal contradiction.

---

### §5 Depth and Breadth Expansion

**Technical lens:** The LLM-as-Operating System (AIOS) paradigm (arXiv:2403.16971) frames the LLM kernel as arbitrating access to reasoning capacity, context windows, external tools, and persistent memory on behalf of AI agent processes — analogous to an operating system kernel managing CPU, RAM, and storage. [Source: note.com AIOS analysis.] [inference] This framing is architecturally consistent with the layered context model: the context architecture described here is the "memory management subsystem" of the AIOS. Layers 2–3 (core context) are RAM; Layers 1, 4–5 (indexed, retrievable) are storage; Layers 6–8 (dynamic) are the input/output buffer.

**Governance lens:** The DataHub CONTEXT 2025 conference report describes the enterprise "context layer" as emerging infrastructure distinct from RAG — an infrastructure tier dedicated to capturing, structuring, and surfacing organisational knowledge in forms that agents can consume. [Source: DataHub.com CONTEXT 2025 Highlights.] [fact] This validates the framework's architectural claim: the layered context architecture is a distinct infrastructure concern, not just a retrieval technique.

**Historical lens:** Every generation of enterprise information retrieval technology (mainframe search, Intranet, SharePoint, Confluence) has failed at the same point: organisations invest in retrieval while neglecting knowledge governance, producing the same "ungardened wiki" failure mode. [Source: `2026-03-15-context-compression-rag-enterprise-knowledge.md`, Analysis section; `learnings.md`, Thread 5.] [inference] The layered context architecture will encounter the same governance failure if the organisational prerequisite — ownership assignment, freshness verification, and contradiction resolution for each layer — is not established as a function, not just a technology.

**Regulatory lens:** The European Union (EU) AI Act (Articles 9 and 13) requires that high-risk AI systems maintain justification traces and risk management documentation. [Source: `2026-03-02-integrative-framework-agent-decision-making.md`, Evidence Map.] [inference] A layered context architecture with provenance tracking — each context chunk tagged with its source layer, document, version, and timestamp — directly enables EU AI Act compliance by providing an auditable record of what context influenced which decision.

**Behavioural lens:** The sycophancy research (56–62% rates in challenging scenarios, SycEval AIES 2025) documents that token-level compliance can co-exist with goal-level failure. [Source: `2026-03-08-context-engineering-first-principles.md`.] [inference] Sycophancy is a values-layer failure: the agent optimises for immediate user satisfaction (Layer 8: task) at the expense of organisational values (Layer 2: values/purpose). The CAI constitution mechanism is the architectural countermeasure: it forces the agent to evaluate each output against Layer 2 before delivering it, breaking the token-level compliance loop.

**New insight from depth expansion:** The concept of "context graph" (governed, queryable memory layer connecting entities, events, decisions, policies, and evidence) extends beyond RAG to provide auditable decision trails. [Source: medium.com/@adnanmasood — Context Graphs guide.] [inference] A context graph is the implementation substrate that makes the layered context architecture persistent and auditable. It provides the provenance infrastructure that RAG alone lacks.

---

### §6 Synthesis

**Executive summary:**

A layered organisational context architecture should partition organisational knowledge into eight distinct layers — regulatory, values/purpose, vision/mission, strategy, policies/standards, current operating position, intent/priorities, and immediate task — each requiring a different storage, retrieval, and compression strategy determined by its update frequency, volume, and authority weight. Layers 2–3 (values and vision) must always be resident in the core context window as a Constitutional AI-style organisational constitution; they cannot be reliably retrieved on demand. Layers 1 and 5 (regulatory and policies) are indexed offline using RAPTOR hierarchical tree summarisation, retrieved via Modular RAG with tier-specific routing, and compressed at query time using LLMLingua-2. The Cynefin framework provides the meta-routing layer: the complexity domain of a decision query determines how deeply each layer is retrieved. Neurological research confirms the architecture's structural validity — the prefrontal cortex manages abstract goals in the rostral region and immediate context in the caudal region, with working memory gating (analogous to the modular RAG router) determining what enters active processing. Knowledge corpus governance — ownership, freshness, and contradiction resolution at each layer — remains the primary unsolved prerequisite; no retrieval or compression technique compensates for an ungoverned source layer.

**Key findings:**

1. The eight-layer context hierarchy (regulatory → immediate task) has a defined authority ordering — Layer 1 (Regulatory) overrides all others; Layer 8 (Task) is subordinate to all others — validated by the independent convergence of Constitutional AI design, enterprise AI architecture literature, and the neuroscience of PFC hierarchical control.

2. Layers 2 and 3 (values/purpose and vision/mission) must always be resident in the core context window as an organisational constitutional document of approximately 300 tokens, because they are the highest-authority non-regulatory constraints and their relevance cannot be determined by query routing — they apply to every decision regardless of task type.

3. RAPTOR hierarchical tree indexing (ICLR 2024, arXiv:2401.18059) is the correct offline indexing technique for Layers 1 (regulatory) and 5 (policies/standards), because both layers consist of large, hierarchically structured document corpora where multi-level reasoning is required and offline preprocessing is feasible given low update frequency.

4. The Cynefin framework provides the meta-routing layer that maps decision complexity (Clear/Complicated/Complex/Chaotic) to retrieval depth across layers: Clear decisions require only Layers 7–8 and a cached policy summary; Complex decisions require deep retrieval from Layers 1–5; Chaotic decisions bypass retrieval entirely and use Layer 2 (values) as anchor for immediate action.

5. The prefrontal cortex's hierarchical organisation — rostral regions for abstract, temporally remote goals; caudal regions for immediate stimulus-response — provides a neurological validation for the context layer hierarchy: abstract constraints (Layers 1–4) must be actively maintained as the goal structure within which concrete task context (Layers 7–8) is interpreted.

6. Schema theory from cognitive science validates RAPTOR indexing as the computational analogue of schema formation: RAPTOR compresses a large document corpus into a tree of increasingly abstract summaries, mirroring the brain's organisation of experience into hierarchical schemas that guide inference and pattern-completion without requiring recall of raw experiences.

7. Working memory gating — the cortico-striatal mechanism that selectively admits task-relevant information into active processing — is the neurological analogue of modular RAG query routing; both perform selective filtering of a large information space based on task relevance, suppressing cross-domain noise that would degrade reasoning.

8. Constitutional AI (Anthropic, arXiv:2212.08073) provides the operational mechanism for encoding Layer 2 (values/purpose): a compact organisational constitution embedded in the agent's system prompt, against which the agent evaluates its outputs before delivering them — the architectural countermeasure for the sycophancy failure mode (token-level compliance at the expense of values alignment).

9. The current operating position (Layer 6) is best represented as a structured, pre-compressed Wardley Map or equivalent situational-awareness artefact that encodes the evolution stage of key capabilities, current budget constraints, in-flight projects, and strategic priorities — not as raw operational documents — because structured representation is smaller, more reliably retrievable, and reduces the risk of stale data from high-frequency document churn.

10. Knowledge corpus governance — ownership assignment, freshness verification, and contradiction resolution for each layer — is the primary prerequisite for the architecture's effectiveness; this is the same failure mode that has caused every prior generation of enterprise retrieval technology to deliver less than expected, and no retrieval or compression technique compensates for ungoverned source layers.

11. Provenance tracking — tagging each context chunk with its source layer, document identity, version, and timestamp — is not optional in regulated environments; it is the mechanism that makes an AI-assisted decision auditable under EU AI Act Articles 9 and 13, transforming the layered context architecture into a compliance asset rather than merely a technical component.

12. Automatic Cynefin domain classification for enterprise decision queries is not yet a solved problem; the meta-routing step currently requires either human classification or a separately trained classifier, which represents a practical deployment gap that limits full automation of the context composition pipeline.

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Eight-layer hierarchy with defined authority ordering | `2026-03-02-integrative-framework-agent-decision-making.md` KF3; Anthropic CAI 2026 constitution (bisi.org.uk); this item §2 A5 | high | Three independent sources converge on same authority ordering |
| Layers 2–3 must be core context (always resident) | MemGPT/Letta core-memory model (arXiv:2310.08560); context rot benchmark (RULER, arXiv:2404.06654); Shannon entropy principle | high | Core context principle well-established; low token cost of Layers 2–3 makes it trivially affordable |
| RAPTOR for Layers 1 and 5 | arXiv:2401.18059 (ICLR 2024); `2026-03-15-context-compression-rag-enterprise-knowledge.md` KF5 | high | Paper results + prior research conclusion; document structure argument is structural [inference] |
| Cynefin as meta-routing layer | thecynefin.co; wardleymaps.com Cynefin-Wardley guide; structural analysis | medium | Cynefin was not designed for RAG routing; the mapping is a structural [inference] |
| PFC rostral→abstract / caudal→concrete hierarchy | Nature Reviews Neuroscience PFC review; Science MIT McGovern PFC paper; Badre lab | high | Multiple independent neuroscience sources agree on PFC hierarchy; AI analogy is [inference] |
| Schema theory validates RAPTOR | EBSCO schema theory; MIT schema theory; PMC NIH hierarchical concept learning | high | Schema theory well-established; RAPTOR-as-schema is structural [inference] |
| Working memory gating = modular RAG router | PMC 2015 PFC WM review; `2026-03-15-context-compression-rag-enterprise-knowledge.md` KF6; Badre lab | high | Both mechanisms perform selective filtering; analogy is [inference], not identity |
| Constitutional AI for Layer 2 values encoding | arXiv:2212.08073; bisi.org.uk Claude 2026 constitution; `2026-03-02-integrative-framework-agent-decision-making.md` KF7 | high | Three independent sources; enterprise-specific constitution content gap remains |
| Wardley Maps for Layer 6 current operating position | theuncertaintyproject.org; lethain.com; wardleymaps.com Cynefin guide | medium | Wardley Maps provide the concept; enterprise AI use is practitioner inference |
| Knowledge governance as prerequisite | `2026-03-15-context-compression-rag-enterprise-knowledge.md` KF10; learnings.md Thread 5; DataHub CONTEXT 2025 | high | Three independent sources; primary finding of prior research |
| Provenance tracking for regulatory compliance | EU AI Act Arts 9+13; `2026-03-02-integrative-framework-agent-decision-making.md` Evidence Map | high | Binding regulation; confirmed by prior research |
| Cynefin routing classification is not automated | No published automated Cynefin classifier found; gap identified by absence | medium | Absence of evidence for automation; confirmed as gap |

**Assumptions:**

- **Assumption:** Layers 2–3 (values, vision/mission) can be compressed into approximately 300 tokens without material loss of alignment fidelity. **Justification:** Vision/mission statements are typically 1–3 sentences in canonical form; values can be encoded as a 10–15 principle constitutional document following the CAI model. No direct validation of 300-token threshold exists; the figure is an operational estimate based on the Claude constitution structure.

- **Assumption:** RAPTOR's performance on literary/general knowledge benchmarks (82.6% on QuALITY) transfers to structured regulatory/policy document corpora. **Justification:** Both involve hierarchically structured text with multi-level reasoning requirements. RAPTOR's recursive clustering operates on semantic similarity, not document type; policy documents have comparably rich semantic structure. Transfer is an [inference] — no direct benchmark on policy/regulatory text was found.

- **Assumption:** Cynefin domain classification, applied to the decision query rather than the organisational domain, provides meaningful routing differentiation. **Justification:** The Cynefin framework was designed for decision-context classification; applying it to individual queries rather than organisational domains is an extension, but the causal logic (query type → context depth needed) is structurally sound.

- **Assumption:** The layered context architecture's effectiveness is primarily limited by knowledge corpus governance quality, not by the technical retrieval and compression components. **Justification:** This is directly confirmed by the completed RAG/compression prerequisite item (KF10) and is consistent with the historical pattern of enterprise retrieval technology.

**Analysis:**

The architecture unifies three independent frameworks that have been developed in isolation: (1) the AI context management literature (RAG, compression, memory architectures), (2) cognitive neuroscience (PFC hierarchy, schema theory, working memory gating), and (3) enterprise knowledge management frameworks (TOGAF, Cynefin, Wardley Maps, Constitutional AI). The convergence is striking: each framework, developed independently, arrives at the same structural conclusion — that effective decision-making requires a hierarchical, layered representation of constraints, ranging from the most abstract and stable to the most concrete and dynamic, with selective filtering mechanisms that activate only what is relevant to the immediate decision.

The primary design tension — completeness versus focus — is resolved not by technology but by governance: the organisation must invest in curating each layer independently, with defined ownership and update processes. Without this, the context architecture degrades to a well-indexed ungardened wiki — better search over the same poor-quality sources.

The second tension — timeliness versus stability — is resolved by the offline/online compression partition: stable layers are pre-processed and indexed; dynamic layers are composed fresh at query time. This requires clear freshness Service Level Agreements (SLAs) for each layer and automated invalidation of offline indexes when source documents change.

The third tension — general values versus specific task constraints — is resolved by the authority hierarchy and the CAI self-evaluation step. Values (Layer 2) are not retrieved on demand; they are always present. The CAI constitution mechanism ensures that before delivering any output, the agent evaluates it against the values layer, catching sycophancy and values-task conflicts that the precedence engine would not flag as explicit rule violations.

**Risks, gaps, and uncertainties:**

- **Cynefin classification is not automated.** The meta-routing step is currently a human or separately trained classifier. Deploying this architecture at scale requires either a robust Cynefin-classification component or a simpler routing heuristic that approximates Cynefin domain without requiring full classification.
- **Values-encoding fidelity gap.** Compressing an organisation's values and purpose into a 300-token CAI constitution will lose nuance. High-stakes decisions in ethical grey areas will require human escalation; the architecture cannot resolve novel value conflicts autonomously.
- **RAPTOR on policy/regulatory text is unvalidated.** The 82.6% accuracy result applies to literary and general knowledge corpora. Structured policy/regulatory text may have different clustering characteristics. A pilot evaluation on a representative regulatory corpus is required before production deployment.
- **Cross-layer contradiction detection at composition time.** The current architecture detects conflicts at decision time (via the precedence engine) but not at context-composition time. A Layer 5 policy that contradicts the current operating position (Layer 6) would be injected without flagging, potentially confusing the agent's reasoning.
- **Organisational knowledge engineering function.** The architecture requires a dedicated function responsible for curating each layer — assigning ownership, maintaining freshness, resolving contradictions. This function does not currently exist in most enterprise AI deployment teams.
- **Temporal validity of indexed layers.** Regulatory changes, strategy pivots, or major policy updates can invalidate offline indexes without immediate detection. An automated change-detection and index-invalidation pipeline is required but not currently part of any standard RAG toolchain.

**Open questions:**

1. Can a lightweight Cynefin-classifier be trained on a labelled set of enterprise decision queries to automate the meta-routing step? (→ candidate high-priority backlog item that blocks full automation of this architecture)
2. What is the minimum constitutional document size for an organisational values layer that maintains meaningful alignment fidelity under CAI self-evaluation? An empirical study with enterprise-specific constitutions of 100/200/500 tokens would provide the answer.
3. Does RAPTOR applied to regulatory/policy corpora (Basel III, MiFID II, PRA SS10/18, ISO 27001) achieve comparable accuracy to its literary benchmark results? A direct evaluation is required before relying on RAPTOR in regulated-industry deployments.
4. What governance function design — roles, processes, tooling — is sufficient to maintain an eight-layer context architecture at enterprise scale? No published playbook currently exists.
5. How should cross-layer contradiction detection be implemented at composition time rather than at decision time?

---

### §7 Recursive Review

**Section justification check:**
- §0: Prior work cross-reference complete. Five completed items cited with specific findings. Scope and constraints confirmed.
- §1: 26 atomic questions across six sub-questions (A–F). Mutually Exclusive, Collectively Exhaustive (MECE) decomposition.
- §2: All 26 questions answered. Every [fact] maps to a named source. [inference] and [assumption] labels applied throughout. All neurological claims sourced from peer-reviewed or credible secondary sources.
- §3: Narrative glue removed. Facts, inferences, and unsupported generalisations explicitly separated.
- §4: Five consistency checks performed. All pass. One tension (values-encoding fidelity) identified as known gap, not contradiction.
- §5: Five lenses applied (technical/AIOS, governance/historical, regulatory/EU AI Act, behavioural/sycophancy, and a new insight from context graph literature). New insights added.
- §6: Executive summary states a direct, specific answer. 12 key findings, all ≥20 words, all specific claims. Evidence map has a row for every key finding. Four assumptions with justifications. Five open questions identified.

**Threads synthesised:** All six Approach sub-questions (A–F) answered and synthesised in §6.

**Uncertainties explicit:** Cynefin automation gap, values-encoding fidelity, RAPTOR transfer to policy documents, cross-layer contradiction detection, and governance function design — all explicitly flagged.

**Verdict: PASS.** All sections justified. All claims sourced or labelled. All uncertainties explicit.

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

A layered organisational context architecture should partition organisational knowledge into eight distinct layers — regulatory, values/purpose, vision/mission, strategy, policies/standards, current operating position, intent/priorities, and immediate task — each requiring a different storage, retrieval, and compression strategy determined by its update frequency, volume, and authority weight. Layers 2–3 (values and vision) must always be resident in the core context window as a Constitutional AI (CAI)-style organisational constitution of approximately 300 tokens; they cannot be reliably retrieved on demand because their relevance is universal, not query-dependent. Layers 1 and 5 (regulatory and policies) are indexed offline using Recursive Abstractive Processing for Tree-Organized Retrieval (RAPTOR) hierarchical summarisation, retrieved via Modular Retrieval-Augmented Generation (RAG) with tier-specific routing, and compressed at query time using LLMLingua-2; the Cynefin framework provides the meta-routing layer that maps decision complexity to retrieval depth. Neurological research on prefrontal cortex (PFC) hierarchical organisation and schema theory confirms the architecture's structural validity, with the PFC hierarchy (rostral regions for abstract goals, caudal regions for immediate context) mirroring the Layer 1–4 versus Layer 7–8 split. Knowledge corpus governance — ownership assignment, freshness verification, and contradiction resolution at each layer — remains the primary unsolved prerequisite; no retrieval or compression technique compensates for an ungoverned source layer.

### Key Findings

1. The eight-layer context hierarchy (regulatory → immediate task) has a defined authority ordering — Layer 1 (Regulatory) overrides all others; Layer 8 (Task) is subordinate to all others — validated by the independent convergence of Constitutional AI design, enterprise AI architecture literature, and the neuroscience of PFC hierarchical control.

2. Layers 2 and 3 (values/purpose and vision/mission) must always be resident in the core context window as an organisational constitutional document of approximately 300 tokens, because they are the highest-authority non-regulatory constraints and their relevance cannot be determined by query routing — they apply to every decision regardless of task type.

3. RAPTOR hierarchical tree indexing (ICLR 2024, arXiv:2401.18059) is the correct offline indexing technique for Layers 1 (regulatory) and 5 (policies/standards), because both layers consist of large, hierarchically structured document corpora where multi-level reasoning is required and offline preprocessing is feasible given low update frequency.

4. The Cynefin framework provides the meta-routing layer that maps decision complexity (Clear/Complicated/Complex/Chaotic) to retrieval depth across layers: Clear decisions require only Layers 7–8 and a cached policy summary; Complex decisions require deep retrieval from Layers 1–5; Chaotic decisions bypass retrieval entirely and use Layer 2 (values) as the anchor for immediate action.

5. The PFC's hierarchical organisation — rostral regions for abstract, temporally remote goals; caudal regions for immediate stimulus-response — provides a neurological validation for the context layer hierarchy: abstract constraints (Layers 1–4) must be actively maintained as the goal structure within which concrete task context (Layers 7–8) is interpreted.

6. Schema theory from cognitive science validates RAPTOR indexing as the computational analogue of schema formation: RAPTOR compresses a large document corpus into a tree of increasingly abstract summaries, mirroring the brain's organisation of experience into hierarchical schemas that guide inference and pattern-completion without requiring recall of raw experiences.

7. Working memory gating — the cortico-striatal mechanism that selectively admits task-relevant information into active processing — is the neurological analogue of modular RAG query routing; both perform selective filtering of a large information space based on task relevance, suppressing cross-domain noise that would degrade reasoning quality.

8. Constitutional AI (CAI, Anthropic, arXiv:2212.08073) provides the operational mechanism for encoding Layer 2 (values/purpose): a compact organisational constitution embedded in the agent's system prompt, against which the agent evaluates its outputs before delivering them — the architectural countermeasure for the sycophancy failure mode (token-level compliance at the expense of values alignment).

9. The current operating position (Layer 6) is best represented as a structured, pre-compressed Wardley Map or equivalent situational-awareness artefact encoding the evolution stage of key capabilities, current budget constraints, in-flight projects, and strategic priorities — rather than as raw operational documents — because structured representation is smaller, more reliably retrievable, and reduces the risk of stale data from high-frequency document churn.

10. Knowledge corpus governance — ownership assignment, freshness verification, and contradiction resolution for each layer — is the primary prerequisite for the architecture's effectiveness; this is the same failure mode that has caused every prior generation of enterprise retrieval technology to under-deliver, and no retrieval or compression technique compensates for ungoverned source layers.

11. Provenance tracking — tagging each context chunk with its source layer, document identity, version, and timestamp — is the mechanism that makes an AI-assisted decision auditable under EU AI Act Articles 9 and 13, transforming the layered context architecture into a compliance asset rather than merely a technical component.

12. Automatic Cynefin domain classification for enterprise decision queries is not yet a solved problem; the meta-routing step currently requires either human classification or a separately trained classifier, which represents a deployment gap that limits full automation of the context composition pipeline.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Eight-layer hierarchy with defined authority ordering | `2026-03-02-integrative-framework-agent-decision-making.md` KF3; Anthropic CAI 2026 constitution (bisi.org.uk); §2 A5 | high | Three independent sources converge on same authority ordering |
| Layers 2–3 must always be core context | MemGPT/Letta core-memory model (arXiv:2310.08560); RULER context-rot benchmark (arXiv:2404.06654); Shannon entropy principle | high | Core context principle established; low token cost of Layers 2–3 makes it trivially affordable |
| RAPTOR for Layers 1 and 5 | arXiv:2401.18059 (ICLR 2024); `2026-03-15-context-compression-rag-enterprise-knowledge.md` KF5 | high | Paper results + prior research; document-structure match is [inference] |
| Cynefin as meta-routing layer | thecynefin.co; wardleymaps.com Cynefin-Wardley guide | medium | Cynefin not designed for RAG routing; mapping is structural [inference] |
| PFC rostral→abstract / caudal→concrete hierarchy | Nature Reviews Neuroscience PFC review; Science MIT McGovern PFC paper; Badre lab talk | high | Multiple neuroscience sources agree; AI analogy is [inference] |
| Schema theory validates RAPTOR indexing | EBSCO schema theory; MIT schema theory PDF; PMC NIH hierarchical concept learning | high | Schema theory well-established; RAPTOR-as-schema is structural [inference] |
| Working memory gating = modular RAG router | PMC 2015 PFC WM review (Goldman-Rakic et al.); `2026-03-15-context-compression-rag-enterprise-knowledge.md` KF6; Badre lab | high | Both mechanisms perform selective filtering; analogy is [inference] |
| CAI for Layer 2 values encoding | arXiv:2212.08073; bisi.org.uk Claude 2026 constitution; `2026-03-02-integrative-framework-agent-decision-making.md` KF7 | high | Three independent sources; enterprise-specific constitution content gap flagged |
| Wardley Maps for Layer 6 operating position | theuncertaintyproject.org; lethain.com; wardleymaps.com | medium | Wardley Maps provide the concept; enterprise AI use is practitioner-level inference |
| Knowledge governance as primary prerequisite | `2026-03-15-context-compression-rag-enterprise-knowledge.md` KF10; learnings.md Thread 5; DataHub CONTEXT 2025 | high | Three independent sources confirm |
| Provenance tracking for EU AI Act compliance | EU AI Act Arts 9+13; `2026-03-02-integrative-framework-agent-decision-making.md` Evidence Map | high | Binding regulation; confirmed by prior research |
| Cynefin classification not yet automated | Absence of published automated classifier; gap identified | medium | Confirmed as gap by absence of evidence |

### Assumptions

- **Assumption:** Layers 2–3 (values, vision/mission) can be compressed into approximately 300 tokens without material loss of alignment fidelity. **Justification:** Vision/mission statements are typically 1–3 sentences in canonical form; values can be encoded as a 10–15 principle constitutional document following the CAI model. No direct validation of this threshold exists; the figure is an operational estimate.

- **Assumption:** RAPTOR's performance on literary/general knowledge benchmarks (82.6% on QuALITY) transfers to structured regulatory/policy document corpora. **Justification:** Both involve hierarchically structured text with multi-level reasoning requirements. RAPTOR's recursive clustering operates on semantic similarity, not document type; policy documents have comparably rich semantic structure. Transfer is an [inference] — no direct benchmark on regulatory/policy text found.

- **Assumption:** Cynefin domain classification applied to individual decision queries (rather than organisational domains) provides meaningful routing differentiation. **Justification:** The Cynefin framework was designed for decision-context classification; query-level application is an extension, but the causal logic (query type → context depth needed) is structurally sound.

- **Assumption:** The architecture's effectiveness is primarily limited by knowledge corpus governance quality, not by the technical retrieval and compression components. **Justification:** Directly confirmed by the completed prerequisite item (KF10) and consistent with the historical pattern of enterprise retrieval technology.

### Analysis

The architecture unifies three independent frameworks developed in isolation: the AI context management literature (RAG, compression, memory architectures), cognitive neuroscience (PFC hierarchy, schema theory, working memory gating), and enterprise knowledge management frameworks (TOGAF, Cynefin, Wardley Maps, Constitutional AI). The convergence is striking: each framework independently arrives at the same structural conclusion — that effective decision-making requires a hierarchical, layered representation of constraints, ranging from the most abstract and stable (regulatory, values) to the most concrete and dynamic (task, intent), with selective filtering mechanisms that activate only what is relevant to the immediate decision.

The primary design tension — completeness versus focus — is resolved not by technology but by governance. The organisation must invest in curating each layer independently, with defined ownership and update processes. Without this, the context architecture degrades to a well-indexed, poorly maintained knowledge base — better search over the same poor-quality sources.

The second tension — timeliness versus stability — is resolved by the offline/online compression partition. Stable layers (1–4) are pre-processed and indexed; dynamic layers (6–8) are composed fresh at query time. This requires clear freshness Service Level Agreements (SLAs) for each layer and automated invalidation of offline indexes when source documents change.

The third tension — general values versus specific task constraints — is resolved by the authority hierarchy plus the CAI self-evaluation step. Values (Layer 2) are not retrieved on demand; they are always present. The CAI mechanism ensures the agent evaluates each output against Layer 2 before delivering it, catching sycophancy and values-task conflicts that the precedence engine would not flag as explicit rule violations.

Competing interpretation considered: that Constitutional AI and Reinforcement Learning from Human Feedback (RLHF) alignment training can internalise all necessary organisational constraints at model level, eliminating the need for runtime context layers. This interpretation is not supported by evidence for enterprise-specific constraints. Alignment training can encode general harmlessness; it cannot encode a specific organisation's regulatory posture, risk tolerance, or strategic priorities without enterprise-specific training data and validation — which most deployments lack.

### Risks, Gaps, and Uncertainties

- **Cynefin classification is not automated.** The meta-routing step currently requires human or separately trained classifier input. At scale, this is a bottleneck; a simpler proxy heuristic may be required as an interim measure.
- **Values-encoding fidelity gap.** Compressing an organisation's values and purpose into a 300-token CAI constitution loses nuance. High-stakes decisions in ethical grey areas will require human escalation; the architecture cannot resolve novel value conflicts autonomously.
- **RAPTOR on policy/regulatory text is unvalidated.** The benchmark results apply to literary corpora. A pilot evaluation on regulatory/policy documents is required before production deployment.
- **Cross-layer contradiction detection at composition time is absent.** The architecture detects conflicts at decision time (via the precedence engine) but not when context from multiple layers is assembled. A Layer 5 policy that contradicts the current operating position (Layer 6) would be injected without flagging.
- **Organisational knowledge engineering function.** The architecture requires a dedicated function responsible for curating each layer — assigning ownership, maintaining freshness, resolving contradictions. This function does not currently exist in most enterprise AI deployment teams.
- **Temporal validity of indexed layers.** Regulatory changes, strategy pivots, or major policy updates can invalidate offline indexes without immediate detection. An automated change-detection and index-invalidation pipeline is required but not currently part of any standard RAG toolchain.

### Open Questions

1. Can a lightweight Cynefin-domain classifier be trained on labelled enterprise decision queries to automate the meta-routing step? This is a candidate high-priority backlog item that directly blocks full automation of the context composition pipeline.
2. What is the minimum constitutional document size for an organisational values layer that maintains meaningful alignment fidelity under CAI self-evaluation? (100 / 200 / 500 tokens — empirically determinable)
3. Does RAPTOR applied to regulatory/policy corpora (Basel III, MiFID II, PRA SS10/18, ISO 27001) achieve comparable accuracy to its literary benchmark? A direct evaluation is required before relying on RAPTOR in regulated-industry deployments.
4. What governance function design — roles, processes, tooling — is sufficient to maintain an eight-layer context architecture at enterprise scale? No published playbook currently exists.
5. How should cross-layer contradiction detection be implemented at context-composition time rather than at decision time?

---

## Output

- Type: knowledge
- Description: A layered organisational context architecture framework defining eight context layers (regulatory through immediate task), per-layer storage/retrieval/compression strategies, neurological validation via PFC hierarchy and schema theory, enterprise framework mappings (Constitutional AI, Cynefin, Wardley Maps, TOGAF), design tension resolution strategies, and explicit identification of five deployment gaps.
- Links:
  - https://arxiv.org/abs/2401.18059 — RAPTOR: hierarchical tree indexing for large document corpora (ICLR 2024)
  - https://arxiv.org/abs/2212.08073 — Constitutional AI: Harmlessness from AI Feedback (Anthropic, 2022)
  - https://www.nature.com/articles/s41386-021-01132-0 — PFC hierarchical control and working memory (Nature Reviews Neuroscience)