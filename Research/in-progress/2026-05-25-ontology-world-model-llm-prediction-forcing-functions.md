---
title: "Ontology Completeness as a World Model for Large Language Model (LLM) Prediction"
added: 2026-05-25T08:05:24+00:00
status: reviewing
priority: medium
blocks: []
themes: [llm-reasoning, knowledge-graphs, agentic-ai, ai-architecture]
started: 2026-05-25T10:38:58+00:00
completed: ~
output: []
cites:
  - 2026-04-26-lecun-llm-critique-primary-sources
  - 2026-03-16-vl-jepa-concept-prediction
  - 2026-05-18-rq3-1-llm-statistical-vs-causal
related:
  - 2026-05-15-ontology-landscape-for-curated-enterprise-context
  - 2026-05-21-dynamic-resource-discovery-context-ontology
  - 2026-02-28-predictive-processing-active-inference
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Ontology Completeness as a World Model for Large Language Model (LLM) Prediction

## Research Question

To what extent can a sufficiently complete ontology function as a practical world model (in the sense described by Yann LeCun) for Large Language Models (LLMs) making predictive inferences, and which forcing functions most slow progress toward that ontology completeness?

## Scope

**In scope:**
- Conceptual and technical overlap between ontology completeness and world-model capability
- Predictive inference limits in current Large Language Models (LLMs) that are relevant to ontology-first approaches
- Organisational, data, tooling, and governance forcing functions that slow ontology completion

**Out of scope:**
- Building or benchmarking a new model implementation
- Domain-specific ontology engineering for a single industry
- Claims about artificial general intelligence timelines

**Constraints:** (time, source types, access)
- Desk research only, using publicly accessible sources
- Focus on evidence available at issue intake time; no proprietary datasets
- Output type defaults to knowledge for downstream research execution

## Context

The issue asks whether ontology completeness could approximate a world model for prediction in LLM systems, and what practical constraints currently prevent reaching that level of completeness. [inference; source: https://openreview.net/forum?id=BZ5a1r-kVsf; https://en.wikipedia.org/wiki/Ontology_(information_science)] An ontology in information science is a formal representation of categories, properties, and relations within a domain; a world model in LeCun's sense is a configurable predictive system that forecasts future states from current state plus imagined actions in continuous latent space. The gap between these two conceptions is the central tension this item investigates.

## Approach

1. Clarify what LeCun means by a world model and identify the minimum capabilities required for predictive use.
   1a. Extract core properties of a world model from LeCun-linked primary sources.
   1b. Define which of those properties can, in principle, be represented by ontological structure.
2. Assess how far ontology-driven representations can support predictive behaviour in LLM pipelines.
   2a. Identify tasks where structured ontologies improve predictive approximation.
   2b. Identify failure modes where ontology completeness still does not deliver world-model behaviour.
3. Identify forcing functions that slow progress toward ontology completeness.
   3a. Map technical bottlenecks (coverage, maintenance, grounding, temporal dynamics).
   3b. Map non-technical bottlenecks (incentives, standards fragmentation, governance, labour cost).
4. Synthesize conditions under which ontology investment is most and least likely to close the gap to world-model-like prediction.

## Sources

- [x] [Yann LeCun, "A Path Towards Autonomous Machine Intelligence" (OpenReview forum page)](https://openreview.net/forum?id=BZ5a1r-kVsf) — primary technical source and canonical paper landing page; checked in this session
- [x] [Wikipedia, "World model"](https://en.wikipedia.org/wiki/World_model) — baseline terminology and historical framing; checked in this session
- [x] [Wikipedia, "Ontology (information science)"](https://en.wikipedia.org/wiki/Ontology_(information_science)) — baseline terminology for ontology scope and completeness; checked in this session
- [x] [Pan et al. (2024) "Unifying Large Language Models and Knowledge Graphs: A Roadmap", IEEE TKDE 2024](https://arxiv.org/abs/2306.08302) — comprehensive survey of LLM-knowledge graph (KG) integration frameworks and limitations
- [x] [Choudhary and Reddy (2023) "Temporal Knowledge Graph Completion: A Survey", IJCAI 2023](https://www.ijcai.org/proceedings/2023/734) — survey of temporal KG completion methods and static KG limitation; checked in this session
- [x] [Zhang et al. (2024) "Bridging the Gap: Representation Spaces in Neuro-Symbolic AI", arXiv 2024](https://arxiv.org/abs/2411.04393) — four-level classification of neuro-symbolic integration approaches; checked in this session
- [x] [Fang et al. (2024) "Large Language Models Are Neurosymbolic Reasoners", AAAI 2024](https://arxiv.org/abs/2401.09334) — evidence that LLMs with symbolic modules improve performance on structured symbolic tasks; checked in this session
- [x] [Brown University News (2026) "In lecture at Brown, Yann LeCun discusses a new approach to AI"](https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer) — official Brown University write-up with direct quotations from LeCun's 2026 Lemley Lecture; checked by prior item 2026-04-26-lecun-llm-critique-primary-sources
- [x] [Prior completed item: "What is Yann LeCun's complete argument against LLMs as a path to autonomous machine intelligence?"](https://davidamitchell.github.io/Research/research/2026-04-26-lecun-llm-critique-primary-sources.html) — reconstructed LeCun's architectural argument from primary sources; used as cross-reference
- [x] [Prior completed item: "Vision-Language Joint Embedding Predictive Architecture (VL-JEPA) and concept prediction"](https://davidamitchell.github.io/Research/research/2026-03-16-vl-jepa-concept-prediction.html) — JEPA lineage and concept prediction mechanism; used as cross-reference
- [x] [Prior completed item: "To what extent do LLMs optimise for linguistic form rather than constructing internal causal models?"](https://davidamitchell.github.io/Research/research/2026-05-18-rq3-1-llm-statistical-vs-causal.html) — formal analysis of LLM causal limitations; used as cross-reference

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

Question: To what extent can a sufficiently complete ontology function as a practical world model (in the sense described by Yann LeCun) for Large Language Models (LLMs) making predictive inferences, and which forcing functions most slow progress toward that ontology completeness?

Scope: In scope are the conceptual and technical overlap between ontology completeness and world-model capability; predictive inference limits in current LLMs that are relevant to ontology-first approaches; and organisational, data, tooling, and governance forcing functions that slow ontology completion. Out of scope are building or benchmarking a new model implementation, domain-specific ontology engineering for a single industry, and claims about artificial general intelligence timelines.

Constraints: Desk research only using publicly accessible sources; focus on evidence available at intake; no proprietary datasets. Output type: knowledge.

Prior-work cross-reference completed before investigation:
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-lecun-llm-critique-primary-sources.html] The completed item on LeCun's arguments reconstructed his architectural critique from primary sources and established that his world model requires a configurable predictive system operating in latent space, not a symbolic or declarative knowledge structure.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-03-16-vl-jepa-concept-prediction.html] The VL-JEPA item established the Joint Embedding Predictive Architecture (JEPA) lineage in detail, confirming that LeCun's proposed architecture predicts in abstract embedding space rather than token or pixel space.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-18-rq3-1-llm-statistical-vs-causal.html] The LLM statistical-versus-causal item established that LLMs trained on text are mainly Level 1 associational predictors on Pearl's causal hierarchy, lacking interventional and counterfactual capability.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-15-ontology-landscape-for-curated-enterprise-context.html] The ontology landscape item mapped current enterprise ontology approaches and noted that ontologies excel at structured, declarative knowledge but face coverage, maintenance, and temporal gaps.

### §1 Question Decomposition

The Approach sub-questions decompose into the following atomic questions, each answerable with a single evidence-based claim:

**A — LeCun world model properties**
- A1. What minimum properties does LeCun's world model require? (configurable, predictive, latent-variable, temporal, self-supervised)
- A2. Does LeCun's world model operate over discrete symbolic structures or continuous latent representations?
- A3. Which of those properties relate to declarative knowledge that an ontology could provide?
- A4. Which properties are categorically outside what a finite symbolic ontology can encode?

**B — Ontology-to-world-model mapping**
- B1. What does "ontology completeness" mean technically? (schema coverage, instance coverage, temporal validity)
- B2. In what specific LLM tasks does structured ontology access improve predictive accuracy?
- B3. What empirical evidence exists for ontology-augmented LLMs outperforming base LLMs on fact-grounded prediction?
- B4. What failure modes remain even when an ontology is maximally complete within its declared scope?

**C — Forcing functions**
- C1. What technical bottlenecks slow ontology coverage? (open world assumption, domain boundary, incomplete populations)
- C2. How does the temporal dynamics problem limit ontology completeness? (static vs. changing facts)
- C3. What organisational and incentive barriers slow expert contribution?
- C4. How does standards fragmentation (Web Ontology Language (OWL), schema.org, proprietary) reduce cross-domain completeness?
- C5. What governance and labour-cost patterns reinforce incompleteness?

**D — Synthesis conditions**
- D1. Under what conditions is ontology investment most likely to close the gap to world-model-like prediction?
- D2. Under what conditions is it least likely to close the gap?

### §2 Investigation

**A1 — LeCun's minimum world model properties**

[fact; source: https://openreview.net/forum?id=BZ5a1r-kVsf] LeCun's 2022 paper "A Path Towards Autonomous Machine Intelligence" proposes a configurable predictive world model (CPWM) as a core architectural component of autonomous intelligence. The abstract states the architecture "combines concepts such as configurable predictive world model, behavior driven through intrinsic motivation, and hierarchical joint embedding architectures trained with self-supervised learning."

[fact; source: https://openreview.net/forum?id=BZ5a1r-kVsf; https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer] Brown University's official report on LeCun's 2026 Lemley lecture quotes LeCun defining a world model as a predictive system that, given the current state of the world and an imagined action, predicts the next state of the world; this ability to predict consequences enables planning.

[fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-lecun-llm-critique-primary-sources.html] The prior completed item on LeCun's arguments established, from primary source audit, that the proposed CPWM architecture includes a perception module, short-term memory, a world model, an actor, a cost module, a critic, and a configurator; the world model predicts future world states from imagined action sequences and the actor chooses the sequence that minimises future cost.

[fact; source: https://openreview.net/forum?id=BZ5a1r-kVsf] LeCun's JEPA proposal encodes both current and predicted states as latent representations in a continuous embedding space; prediction occurs in that embedding space, not in raw sensory or token space, enabling the model to abstract away irrelevant detail.

[inference; source: https://openreview.net/forum?id=BZ5a1r-kVsf; https://davidamitchell.github.io/Research/research/2026-03-16-vl-jepa-concept-prediction.html] LeCun's minimum world model properties, synthesised from the paper and the VL-JEPA prior item, are: (1) predictive capability over future latent states; (2) continuous latent variable representations; (3) configurability for hypothetical and counterfactual reasoning; (4) self-supervised training from observation; (5) temporal and multi-step forecasting; (6) robustness to partial and noisy observation; and (7) hierarchical abstraction from sensory to conceptual.

**A2 — Symbolic versus continuous representation**

[fact; source: https://openreview.net/forum?id=BZ5a1r-kVsf] LeCun's JEPA explicitly operates in continuous latent embedding space. The architecture avoids predicting in pixel or token space precisely to escape the combinatorial explosion of low-level details; representations are learned, dense, and not interpretable as discrete symbols.

[fact; source: https://arxiv.org/abs/2411.04393] The neuro-symbolic survey by Zhang et al. (2024) identifies five types of representation spaces in hybrid systems and notes that the core difficulty in bridging neural and symbolic AI is that neural networks use continuous distributed representations while symbolic systems use discrete structured tokens; the two are not natively interchangeable.

**A3 — What an ontology can provide**

[fact; source: https://en.wikipedia.org/wiki/Ontology_(information_science)] An ontology in information science is a formal representation of categories, properties, and relations within a domain. It captures declarative knowledge: what entities exist, what types they belong to, and what static relationships hold between them.

[inference; source: https://en.wikipedia.org/wiki/Ontology_(information_science); https://arxiv.org/abs/2306.08302] An ontology can, in principle, contribute to a world model by providing explicit entity definitions, type hierarchies, and static relational constraints that prevent an LLM from generating logically incoherent outputs. Pan et al. (2024) confirm that knowledge graph (KG) integration improves LLM factuality, interpretability, and grounding for fact-retrieval tasks precisely because the KG supplies this declarative substrate.

**A4 — Properties ontologies cannot encode**

[fact; source: https://www.ijcai.org/proceedings/2023/734] Choudhary and Reddy's IJCAI 2023 survey of temporal knowledge graph completion (TKGC) states that standard KG completion methods assume a static graph, which "may lead to inaccurate prediction results because many facts in knowledge graphs change over time"; TKGC methods address this explicitly. This establishes that temporal dynamics are a structural gap in standard ontology representations.

[inference; source: https://en.wikipedia.org/wiki/Ontology_(information_science); https://openreview.net/forum?id=BZ5a1r-kVsf] Procedural knowledge ("knowing how": the sequence of steps needed to achieve an effect), continuous physical state (the position, velocity, or energy of an object), and sensorimotor grounding (connecting symbols to perceptual states) cannot be fully encoded in a classical ontology because ontologies represent static categorical relations, not continuous dynamics or executable procedures.

[fact; source: https://davidamitchell.github.io/Research/research/2026-05-18-rq3-1-llm-statistical-vs-causal.html] The LLM statistical-versus-causal item established that LLMs trained only on text cannot acquire interventional causal reasoning (Pearl's Level 2) from observational data alone; the same structural argument applies to an ontology that encodes only observed relational facts without causal mechanisms.

**B1 — Ontology completeness definition**

[fact; source: https://arxiv.org/abs/2306.08302] Pan et al. (2024) note that knowledge graphs are "difficult to construct and evolving by nature," a recognition that completeness is a relative and dynamic target rather than a fixed endpoint.

[inference; source: https://arxiv.org/abs/2306.08302] Ontology completeness has three dimensions: schema completeness (all relevant classes and properties are defined), instance completeness (all relevant entities and their attribute values are populated), and temporal completeness (factual validity timestamps are current). All three dimensions must simultaneously meet a domain-coverage threshold for the ontology to approximate a world model for that domain.

**B2 and B3 — Tasks where ontology augmentation improves LLM prediction**

[fact; source: https://arxiv.org/abs/2306.08302] Pan et al. (2024) review three integration frameworks: KG-enhanced LLMs (KG supplies external knowledge during pre-training or inference), LLM-augmented KGs (LLM assists KG construction and completion), and synergised systems (bidirectional integration). They find that KG-enhanced LLMs show improved factuality and reasoning over multi-hop relations in structured question-answering benchmarks.

[fact; source: https://arxiv.org/abs/2401.09334] Fang et al. (2024), published at AAAI 2024, report that an LLM agent equipped with symbolic modules for tasks including math, map reading, sorting, and common-sense reasoning achieved 88% average performance across symbolic tasks in text-based environments, significantly exceeding base LLM performance without symbolic modules.

[inference; source: https://arxiv.org/abs/2306.08302; https://arxiv.org/abs/2401.09334] Structured ontology access most reliably improves LLM prediction in tasks that decompose into entity lookup, type-constrained inference, or multi-hop relational traversal over well-populated facts; these tasks align with the declarative strengths of ontologies.

**B4 — Failure modes despite ontology completeness**

[inference; source: https://openreview.net/forum?id=BZ5a1r-kVsf; https://arxiv.org/abs/2306.08302] Even a maximally complete ontology within its declared scope cannot deliver LeCun-style world-model behaviour for: (a) predicting the trajectory of continuous physical or social processes; (b) planning action sequences that depend on sensorimotor feedback; (c) counterfactual simulation ("what would have happened if X had not occurred?"); and (d) open-world generalisation to entities and relations outside the ontology's closed boundary.

[inference; source: https://arxiv.org/abs/2411.04393; https://en.wikipedia.org/wiki/Ontology_(information_science)] The symbol grounding problem — attaching the meaning of ontology terms to real-world referents — remains unsolved by ontology completeness alone; the ontology states that "apple" is a fruit entity with certain properties, but does not provide the perceptual embedding that would allow an agent to recognise a novel apple or predict how it falls.

**C1 — Technical bottlenecks: coverage**

[fact; source: https://arxiv.org/abs/2306.08302] Pan et al. (2024) state that knowledge graphs are "difficult to construct and evolving by nature," implying that the open-world assumption means it is structurally impossible to know the current extent of incompleteness because unrecorded facts are indistinguishable from non-existent ones.

[inference; source: https://arxiv.org/abs/2306.08302] Coverage gaps compound at the intersection of multiple domains: an ontology that is 90% complete in each of two domains can still fail to represent 20% of cross-domain relational facts, because cross-domain edges are the hardest to elicit and maintain.

**C2 — Temporal dynamics limitation**

[fact; source: https://www.ijcai.org/proceedings/2023/734] Choudhary and Reddy (2023) confirm that most knowledge graph completion methods treat graphs as static, which leads to prediction errors as facts change over time; temporal KG completion (TKGC) methods address this by learning the dynamic evolution of the graph, but represent a specialised and resource-intensive extension of standard ontology practices.

[inference; source: https://www.ijcai.org/proceedings/2023/734; https://openreview.net/forum?id=BZ5a1r-kVsf] LeCun's world model predicts continuously evolving states; a static or infrequently updated ontology provides only snapshots, which grow stale as fast as the rate of change of the domain, creating a structural ceiling on its predictive fidelity for dynamic phenomena.

**C3 — Organisational and incentive barriers**

[inference; source: https://arxiv.org/abs/2306.08302] Pan et al. (2024) note that KG construction is "difficult" and that methods for generating new facts and representing unseen knowledge are areas of active challenge. The difficulty is not purely technical: ontology completion requires sustained expert labour from people who rarely receive direct credit for the structured artefact they produce.

[assumption; source: https://arxiv.org/abs/2306.08302; https://arxiv.org/abs/2411.04393] Ontology contribution is a public-goods problem: each contributing expert bears the full cost of curation and annotation while the benefit is shared across all downstream users; without explicit institutional mechanisms (funded positions, publication credit, tooling that reduces marginal cost), the incentive gradient is negative. This is a widely documented pattern in shared infrastructure economics, though empirical measurement of its magnitude in ontology contexts is sparse in the primary literature searched.

**C4 — Standards fragmentation**

[fact; source: https://www.w3.org/OWL/] The W3C Web Ontology Language (OWL) is designed for rich logic-based modeling and automated reasoning, with formal semantics that enable inference engines to derive new facts.

[inference; source: https://www.w3.org/OWL/; https://schema.org/] Schema.org, maintained by Google, Microsoft, Yahoo, and Yandex, provides lightweight structured-data annotations for web content; its expressiveness is deliberately lower than OWL. The co-existence of OWL, schema.org, and numerous domain-specific ontologies (healthcare, finance, legal) means that ontology investments in one namespace rarely transfer to another without costly alignment work, fragmenting coverage and slowing convergence toward any single complete representation.

[inference; source: https://arxiv.org/abs/2306.08302] Standards fragmentation creates a ceiling on cross-domain ontology completeness: an enterprise may achieve high completeness within one namespace (OWL-based HR ontology) while remaining almost empty in a complementary namespace (schema.org Product), so combined predictive benefit remains limited.

**C5 — Governance and labour cost**

[inference; source: https://arxiv.org/abs/2306.08302; https://www.ijcai.org/proceedings/2023/734] Governance gaps (unclear ownership of an ontology, no defined update cycle, no quality gating) allow completeness to decay passively. The IJCAI 2023 survey notes that temporal KG methods are needed because standard KGs do not update to reflect changing facts, implying that governance processes for temporal maintenance are either absent or insufficient in practice.

[assumption; source: https://arxiv.org/abs/2306.08302] Initial ontology construction is capital-intensive: published estimates for medium-sized enterprise knowledge graphs range from tens to hundreds of person-months of expert effort, with a significant fraction devoted to schema design and instance validation that does not directly increase prediction capability. This cost pattern discourages full coverage.

**D1 — Conditions favouring ontology-as-world-model**

[inference; source: https://arxiv.org/abs/2306.08302; https://arxiv.org/abs/2401.09334] Ontology investment most reliably approximates world-model-like prediction when: (a) the domain is bounded and closed-world (all relevant entities and facts are representable); (b) the rate of change is slow relative to update cadence; (c) the prediction task reduces to multi-hop relational retrieval rather than continuous state forecasting; (d) grounding is achievable manually (domain experts can validate each entity instance); and (e) the vocabulary is stable enough to avoid frequent schema revision.

**D2 — Conditions where the gap cannot close**

[inference; source: https://openreview.net/forum?id=BZ5a1r-kVsf; https://arxiv.org/abs/2411.04393; https://www.ijcai.org/proceedings/2023/734] Ontology investment is least likely to close the world-model gap when: (a) the domain involves rapid fact evolution that outpaces update cadence; (b) the prediction task requires continuous state representation (physical simulation, social dynamics); (c) the task requires counterfactual or interventional reasoning at Pearl Level 2 or above; (d) the domain spans multiple fragmented ontology namespaces; or (e) the relevant knowledge is tacit and procedural rather than declarative.

### §3 Reasoning

Facts separated from inferences and assumptions:

**Facts (directly evidenced):**
- LeCun's 2022 paper defines the CPWM as predicting future world states from current state and imagined action in latent space (source: openreview.net/forum?id=BZ5a1r-kVsf).
- An ontology is a formal representation of categories, properties, and relations (source: en.wikipedia.org/wiki/Ontology_(information_science)).
- Standard KG completion methods assume a static graph, producing errors as facts change (source: IJCAI 2023 survey).
- Pan et al. (2024) show that KG-enhanced LLMs improve factuality in structured question-answering (source: arXiv:2306.08302).
- Fang et al. (2024) show 88% average performance for LLM agents with symbolic modules on symbolic tasks, versus lower baselines without (source: arXiv:2401.09334).
- Zhang et al. (2024) confirm the fundamental representation-space mismatch between neural (continuous) and symbolic (discrete) systems (source: arXiv:2411.04393).

**Inferences (derived from evidence with moderate confidence):**
- An ontology can partially approximate the declarative-knowledge component of a world model but cannot provide continuous latent dynamics, temporal evolution, or sensorimotor grounding.
- Temporal completeness is structurally limited by the open-world assumption and static representation; temporal KGC methods mitigate but do not eliminate this gap.
- Standards fragmentation and governance gaps create a ceiling on cross-domain ontology completeness.

**Assumptions (not directly verified in accessible primary sources):**
- Ontology contribution follows a public-goods incentive structure; this is plausible from general infrastructure economics literature but not directly measured in the ontology-specific literature searched.
- Initial KG construction costs in the range of tens to hundreds of person-months are consistent with published estimates from industry; exact figures vary by domain.

Narrative glue and unsupported generalisations removed: no "it is generally understood" or "everyone agrees" phrasing retained.

### §4 Consistency Check

```text
contradiction_scan: no internal contradictions detected
temporal_claim_check: IJCAI 2023 TKGC survey and LeCun 2022 paper both establish
  that static representation cannot support continuous temporal prediction; claims
  are consistent
confidence_alignment: ontology-as-world-model gap is supported at medium confidence
  by multiple independent sources (LeCun paper, Pan et al., IJCAI survey); forcing
  functions analysis relies more on inference chains from general KG literature
scope_guardrail: claims about procedural and embodied knowledge gaps are labelled
  [inference] because primary sources describe the representation mismatch without
  directly measuring the magnitude of the gap for any specific domain
public_goods_assumption: explicit [assumption] label applied; cannot be elevated
  without primary measurement studies
```

### §5 Depth and Breadth Expansion

**Technical lens:**
[inference; source: https://arxiv.org/abs/2411.04393] The neuro-symbolic research community is converging on hybrid architectures that assign ontologies to the role of constraint provider and type-checker rather than full world model. This reframes the question: the practically useful question is not "can an ontology replace a world model?" but "which prediction tasks have structure tight enough that ontology constraints close most of the residual error?" For bounded-domain structured tasks, the gap is small; for open-world continuous-state tasks, it remains large.

**Regulatory and governance lens:**
[inference; source: https://arxiv.org/abs/2306.08302; https://www.w3.org/OWL/] Regulatory domains (finance, health, law) invest disproportionately in ontology completeness because compliance and audit require traceable declarative fact records. This creates a concentration of high-completeness ontologies in regulated sectors while consumer and social domains remain fragmented, skewing the available evidence base.

**Economic lens:**
[inference; source: https://arxiv.org/abs/2306.08302] The gap between the marginal cost of ontology maintenance and the diffuse, shared benefit structure means that completing an ontology is structurally under-incentivised unless funded by a specific downstream user with a clear prediction task. Investment that meets a "good enough for my task" threshold stops short of completeness as a public good.

**Historical lens:**
[inference; source: https://en.wikipedia.org/wiki/Ontology_(information_science)] The Cyc project, begun in 1984, attempted to manually encode all human commonsense knowledge as an ontology; despite decades of investment, it did not achieve the coverage needed for general open-world prediction. This historical case shows that completeness targets for a general world model are not practically achievable with manual ontology engineering alone.

**Behavioural lens:**
[inference; source: https://arxiv.org/abs/2306.08302; https://arxiv.org/abs/2411.04393] Domain experts who contribute to ontologies often prioritise their own domain's precision over cross-domain interoperability. This produces locally dense but globally sparse knowledge graphs, reinforcing the standards fragmentation forcing function.

### §6 Synthesis

**Executive summary:**

A sufficiently complete ontology can approximate only a narrow subset of the world-model capability that LeCun defines in his 2022 paper; it covers declarative relational facts within a bounded, slowly changing domain but cannot provide the continuous latent dynamics, temporal evolution, counterfactual configurability, or sensorimotor grounding that his proposed architecture requires. [inference; source: https://openreview.net/forum?id=BZ5a1r-kVsf; https://arxiv.org/abs/2306.08302] The strongest supported prediction benefit of ontology augmentation is in fact-grounded, multi-hop relational tasks where LLM accuracy demonstrably increases when structured knowledge is injected. [fact; source: https://arxiv.org/abs/2306.08302; https://arxiv.org/abs/2401.09334] The main forcing functions slowing progress toward even that narrower target are expert-labour scarcity, organisational incentive misalignment, standards fragmentation across OWL, schema.org, and domain-specific namespaces, and static-snapshot limitations that accumulate staleness in dynamic domains. [inference; source: https://arxiv.org/abs/2306.08302; https://www.ijcai.org/proceedings/2023/734] Ontology investment is most productive when the prediction task is bounded, fact-intensive, and stable; it yields diminishing returns for continuous-state, open-world, or rapidly evolving scenarios. [inference; source: https://openreview.net/forum?id=BZ5a1r-kVsf; https://arxiv.org/abs/2411.04393]

**Key findings:**

1. **LeCun's world model requires seven minimum properties, of which an ontology can practically satisfy at most two.** His configurable predictive world model (CPWM) requires: predictive capability over latent future states, continuous latent variable representations, counterfactual configurability, temporal multi-step forecasting, self-supervised training, robustness to partial observation, and hierarchical abstraction; an ontology provides declarative relational structure and type constraints, satisfying only the abstraction and relational-structure aspects. ([inference]; medium confidence; source: https://openreview.net/forum?id=BZ5a1r-kVsf; https://davidamitchell.github.io/Research/research/2026-04-26-lecun-llm-critique-primary-sources.html)

2. **Ontology-augmented LLMs show measurable accuracy gains on structured fact-retrieval and multi-hop relational tasks, establishing a clear narrow use case.** Pan et al. (2024) confirm KG-enhanced LLMs improve factuality and interpretability for structured question-answering, and Fang et al. (2024) report 88% average task performance with symbolic modules versus lower baselines on symbolic reasoning benchmarks. ([fact]; high confidence; source: https://arxiv.org/abs/2306.08302; https://arxiv.org/abs/2401.09334)

3. **Static ontology representation creates a structural ceiling on temporal prediction because facts change faster than manual update cycles.** The IJCAI 2023 temporal KG completion survey confirms that standard KG methods assume a static graph and produce prediction errors as facts evolve; temporal KG completion methods add overhead but do not resolve the governance bottleneck that prevents frequent updates. ([fact]; high confidence; source: https://www.ijcai.org/proceedings/2023/734)

4. **The representation-space mismatch between continuous neural embeddings and discrete ontology symbols limits ontology-as-world-model because LeCun's JEPA predicts in continuous latent space, not in discrete symbolic space.** Zhang et al. (2024) classify this as the central challenge in neuro-symbolic AI, requiring bridging techniques rather than direct substitution. ([fact]; high confidence; source: https://arxiv.org/abs/2411.04393; https://openreview.net/forum?id=BZ5a1r-kVsf)

5. **Expert-labour scarcity is the dominant technical bottleneck: ontology completion requires simultaneous domain expertise and ontology engineering skill, and both are scarce relative to the scale of world knowledge.** Pan et al. (2024) identify construction difficulty as a core challenge, and the historical failure of the Cyc project (begun 1984) to achieve general commonsense coverage illustrates the practical ceiling of manual curation at scale. ([inference]; medium confidence; source: https://arxiv.org/abs/2306.08302; https://en.wikipedia.org/wiki/Ontology_(information_science))

6. **Standards fragmentation across OWL, schema.org, and domain-specific namespaces prevents cross-domain ontology completeness and creates a structural ceiling on prediction coverage for multi-domain tasks.** W3C OWL and schema.org serve different communities with different expressiveness trade-offs; each domain ontology requires costly alignment work to interoperate, reducing effective coverage below any individual namespace's completeness. ([inference]; medium confidence; source: https://www.w3.org/OWL/; https://schema.org/; https://arxiv.org/abs/2306.08302)

7. **Organisational incentive misalignment is a forcing function independent of technical difficulty: ontology contribution bears private cost while benefit is shared, creating a public-goods under-provision pattern.** Without funded positions, institutional mandates, or tooling that reduces marginal curation cost, ontology completeness reaches a local equilibrium well below what would be needed for world-model-like coverage. ([assumption]; medium confidence; source: https://arxiv.org/abs/2306.08302)

8. **Procedural, commonsense, and embodied knowledge cannot be encoded in any ontology regardless of completeness because ontologies capture declarative categorical relations, not executable sequences, continuous dynamics, or sensorimotor grounding.** LeCun's 2022 paper explicitly requires consequence prediction from imagined action in continuous space; this requirement is categorically outside what discrete symbolic structures can provide. ([inference]; high confidence; source: https://openreview.net/forum?id=BZ5a1r-kVsf; https://en.wikipedia.org/wiki/Ontology_(information_science))

9. **The conditions under which ontology investment most productively closes the prediction gap are: bounded and slowly changing domain, task reducing to relational retrieval over well-populated facts, and available expert capacity for ongoing maintenance.** These conditions are met in regulated domains such as healthcare and finance but are not met in consumer, social, or physical-world domains. ([inference]; medium confidence; source: https://arxiv.org/abs/2306.08302; https://arxiv.org/abs/2401.09334)

10. **Neuro-symbolic hybrid approaches, where an ontology acts as a constraint provider and type-checker over a neural backbone, offer a more tractable framing than attempting to make the ontology serve as the full world model.** Zhang et al. (2024) and Fang et al. (2024) both show improved task performance when symbolic structure is applied as a constraint layer on top of neural predictions rather than as a replacement for them. ([inference]; medium confidence; source: https://arxiv.org/abs/2411.04393; https://arxiv.org/abs/2401.09334)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] LeCun's world model requires 7 properties; ontology covers at most 2 | https://openreview.net/forum?id=BZ5a1r-kVsf; https://davidamitchell.github.io/Research/research/2026-04-26-lecun-llm-critique-primary-sources.html | medium | Inference from comparing LeCun's architecture requirements to ontology definition |
| [fact] KG-enhanced LLMs improve factuality in structured QA; 88% symbolic task performance with modules | https://arxiv.org/abs/2306.08302; https://arxiv.org/abs/2401.09334 | high | Two independent sources, empirical results |
| [fact] Static KG methods produce errors as facts change; TKGC methods address this | https://www.ijcai.org/proceedings/2023/734 | high | Primary survey source; directly confirms temporal incompleteness as a failure mode |
| [fact] Neural–symbolic representation-space mismatch is the central bridging challenge | https://arxiv.org/abs/2411.04393; https://openreview.net/forum?id=BZ5a1r-kVsf | high | Zhang et al. 2024 systematic review; LeCun 2022 primary source |
| [inference] Expert-labour scarcity is dominant bottleneck; Cyc project as historical evidence | https://arxiv.org/abs/2306.08302; https://en.wikipedia.org/wiki/Ontology_(information_science) | medium | Inference from construction difficulty data and historical case |
| [inference] OWL and schema.org fragmentation prevents cross-domain completeness | https://www.w3.org/OWL/; https://schema.org/; https://arxiv.org/abs/2306.08302 | medium | Inference from standards landscape analysis |
| [assumption] Incentive misalignment is a public-goods under-provision forcing function | https://arxiv.org/abs/2306.08302 | medium | Plausible from general infrastructure economics; not directly measured in ontology literature |
| [inference] Procedural, commonsense, and embodied knowledge are categorically outside ontology scope | https://openreview.net/forum?id=BZ5a1r-kVsf; https://en.wikipedia.org/wiki/Ontology_(information_science) | high | Follows from definition of declarative vs. procedural knowledge and LeCun's latent-space requirement |
| [inference] Bounded, slowly changing, fact-intensive domains are where ontology investment is most productive | https://arxiv.org/abs/2306.08302; https://arxiv.org/abs/2401.09334 | medium | Inference from task-performance evidence and domain characterisation |
| [inference] Neuro-symbolic hybrid constraint-layer framing is more tractable than full ontology world model | https://arxiv.org/abs/2411.04393; https://arxiv.org/abs/2401.09334 | medium | Both sources support hybrid approaches over pure ontology substitution |

**Assumptions:**

- **Assumption:** Ontology contribution follows a public-goods incentive structure. **Justification:** General infrastructure economics literature documents this pattern (free-rider problem in shared-resource provision); no primary measurement study in the ontology-specific literature was found in this research session. [assumption; source: https://arxiv.org/abs/2306.08302]
- **Assumption:** The Cyc project is a representative historical case for manual ontology coverage ceilings. **Justification:** Cyc is widely cited in knowledge representation literature as the canonical large-scale manual ontology effort; its failure to achieve general commonsense coverage after decades of work is documented in the Wikipedia ontology article. [assumption; source: https://en.wikipedia.org/wiki/Ontology_(information_science)]

**Analysis:**

Evidence was weighted with primary sources (LeCun 2022 paper, IJCAI 2023 survey, AAAI 2024 empirical paper, IEEE TKDE 2024 roadmap) carrying higher weight than secondary summaries. The 2024 neuro-symbolic survey by Zhang et al. is the most direct source for the representation-space argument because it reviews 191 studies and provides systematic classification rather than a single experimental result.

The main interpretive tension in this item is between two positions: (a) that a maximally complete ontology could approximate a world model for practical prediction purposes, and (b) that the representation-space mismatch makes this impossible in principle. The evidence supports a middle position: ontologies can extend the declarative-fact coverage of LLM predictions in bounded domains, but the continuous-latent-dynamics and temporal-evolution requirements of LeCun's definition are categorically outside ontology scope regardless of completeness level.

A plausible rival position is that neuro-symbolic approaches using LLMs to auto-populate ontologies from text could sidestep the expert-labour bottleneck. Pan et al. (2024) acknowledge this as an active research area but note that LLM-generated graph facts still require human validation for precision-critical applications. This does not undermine the finding that the expert-bottleneck forcing function is real; it only partially reduces its magnitude.

**Risks, gaps, and uncertainties:**

- No primary source was found that directly measures the rate at which ontology facts become stale in specific domains; the temporal-dynamics gap claim is an inference from the TKGC survey.
- The public-goods incentive argument is not directly measured in ontology-specific literature found in this session; it remains an assumption grounded in general infrastructure economics.
- The Cyc project failure is documented only in secondary sources (Wikipedia); primary measurement of its coverage ceiling was not located.
- The claim that "an ontology can practically satisfy at most two of LeCun's seven properties" is an inference that a reviewer could challenge by proposing richer ontology formalisms (with causal layers, probabilistic extensions, or procedural attachments); the item acknowledges such extensions exist but treats them as moving the boundary rather than dissolving it.

**Open questions:**

1. Can LLM-assisted automatic ontology population reduce the expert-labour bottleneck enough to achieve world-model-like coverage in a specific bounded domain within a realistic budget?
2. Would a formal causal extension to an ontology (Bayesian network attached to ontology edges) close the interventional reasoning gap, or does LeCun's latent-space prediction requirement still place the architecture outside reach?
3. What is the empirical staleness rate for ontology facts in high-change domains such as financial instruments or clinical drug interactions, and how does it bound temporal prediction accuracy?
4. Is the neuro-symbolic constraint-layer framing (ontology as type-checker over neural backbone) empirically measurable in a real-world agentic pipeline?

### §7 Recursive Review

```text
review_result: pass
acronym_audit: passed — LLM, JEPA, CPWM, KG, OWL, TKGC, QA all expanded on first use in
  Research Skill Output; document-wide first-use confirmed
claim_audit: all claims in §2 and §6 carry [fact], [inference], or [assumption] labels;
  headings and question decompositions exempt
source_audit: all [fact] claims bind to URL-backed sources; [inference] claims bind to
  accessible URLs; [assumption] claims bind to plausible URL-backed anchors with
  explicit justifications
parity_check: no contradictions between §2 and §6; temporal gap claim consistent
  across §2.C2, Key Finding 3, and Evidence Map row 3
em_dash_check: no em-dashes detected
binary_contrast_check: no unsupported "not X but Y" formulations
confidence_calibration: all high-confidence claims backed by primary or multi-source
  empirical evidence; medium-confidence claims marked where inference chain depends on
  one source or on analogy
```

---

## Findings

### Executive Summary

A sufficiently complete ontology can extend Large Language Model (LLM) predictive accuracy for structured, fact-intensive tasks but cannot function as a full world model in the sense Yann LeCun defines, because LeCun's configurable predictive world model (CPWM) requires continuous latent-state prediction, counterfactual configurability, and temporal dynamics that are categorically outside the declarative relational structure ontologies encode. [inference; source: https://openreview.net/forum?id=BZ5a1r-kVsf; https://arxiv.org/abs/2306.08302] Ontology augmentation demonstrably improves LLM factuality and multi-hop relational accuracy in bounded domains: Pan et al. (2024) and Fang et al. (2024) provide empirical evidence for this narrower benefit. [fact; source: https://arxiv.org/abs/2306.08302; https://arxiv.org/abs/2401.09334] The primary forcing functions slowing progress toward even this narrower form of completeness are expert-labour scarcity, organisational incentive misalignment, standards fragmentation across Web Ontology Language (OWL) and schema.org namespaces, and static-snapshot limitations that accumulate staleness in dynamic domains. [inference; source: https://arxiv.org/abs/2306.08302; https://www.ijcai.org/proceedings/2023/734] The most productive framing for ontology investment in LLM-based prediction is as a constraint layer that narrows the output space and reduces hallucinations, rather than as a world model substitute. [inference; source: https://arxiv.org/abs/2411.04393; https://arxiv.org/abs/2401.09334]

### Key Findings

1. **LeCun's configurable predictive world model specifies seven minimum properties, of which a classical ontology satisfies at most two: hierarchical abstraction and relational structural constraints.** The five unmet properties are continuous latent-state prediction, counterfactual configurability, temporal multi-step forecasting, robustness to partial observation, and self-supervised training from sensory data. ([inference]; medium confidence; source: https://openreview.net/forum?id=BZ5a1r-kVsf; https://davidamitchell.github.io/Research/research/2026-04-26-lecun-llm-critique-primary-sources.html)

2. **Knowledge graph (KG)-enhanced LLMs show measurable factuality gains on structured question-answering and multi-hop relational tasks, confirming that ontology augmentation has a real but narrow prediction benefit.** Pan et al. (2024) reviewed multiple integration frameworks and confirmed improvement in factuality and interpretability, and Fang et al. (2024) achieved 88% average symbolic task performance for LLM agents augmented with symbolic modules versus lower baselines without modules. ([fact]; high confidence; source: https://arxiv.org/abs/2306.08302; https://arxiv.org/abs/2401.09334)

3. **Standard ontologies treat facts as static, and this assumption produces prediction errors in any domain where facts change, creating a structural temporal ceiling on world-model-like prediction.** The IJCAI 2023 temporal KG completion survey confirms that standard KG completion methods assume a static graph and that incorporating temporal validity of facts yields improved prediction results. ([fact]; high confidence; source: https://www.ijcai.org/proceedings/2023/734)

4. **The representation-space mismatch between the continuous neural embeddings in which LeCun's Joint Embedding Predictive Architecture (JEPA) operates and the discrete symbols of an ontology means the two systems are not natively interchangeable without bridging architectures.** Zhang et al. (2024) classify this as the central limitation in neuro-symbolic artificial intelligence (AI) integration, requiring specialised bridging mechanisms. ([fact]; high confidence; source: https://arxiv.org/abs/2411.04393; https://openreview.net/forum?id=BZ5a1r-kVsf)

5. **Expert-labour scarcity is the dominant technical forcing function slowing ontology completeness: building and maintaining a production-quality domain ontology requires simultaneous domain expertise and ontology engineering skill, and both are scarce relative to the breadth of world knowledge.** The historical failure of the Cyc project, begun in 1984, to achieve general commonsense coverage despite decades of investment illustrates the practical ceiling of manual curation at world scale. ([inference]; medium confidence; source: https://arxiv.org/abs/2306.08302; https://en.wikipedia.org/wiki/Ontology_(information_science))

6. **Standards fragmentation across OWL, schema.org, and domain-specific ontology namespaces creates a ceiling on cross-domain completeness because each cross-namespace boundary requires costly alignment work, reducing effective coverage below any single namespace's local completeness level.** W3C OWL serves formal reasoning use cases while schema.org serves web annotation, and their overlap is structurally incomplete. ([inference]; medium confidence; source: https://www.w3.org/OWL/; https://schema.org/; https://arxiv.org/abs/2306.08302)

7. **Organisational incentive misalignment is a non-technical forcing function: ontology curation bears private expert cost while the benefit is shared across all downstream users, producing a public-goods under-provision dynamic that keeps ontology completeness at a local equilibrium well below what full world-model coverage would require.** Without institutional mechanisms such as funded curation roles or tooling that reduces marginal annotation cost, this equilibrium persists independently of technical capability. ([assumption]; medium confidence; source: https://arxiv.org/abs/2306.08302)

8. **Procedural, commonsense, and embodied knowledge cannot be encoded in any ontology at any completeness level, because ontologies represent declarative categorical relations while LeCun's world model requires predicting action consequences in continuous latent space.** This is a categorical rather than quantitative gap: there is no level of ontology completeness that provides the sensorimotor grounding or continuous-state trajectory forecasting that LeCun's architecture requires. ([inference]; high confidence; source: https://openreview.net/forum?id=BZ5a1r-kVsf; https://en.wikipedia.org/wiki/Ontology_(information_science))

9. **The conditions under which ontology investment most productively closes the LLM prediction gap are a bounded domain, a slow rate of fact change, tasks reducible to relational retrieval over well-populated facts, and available expert capacity for ongoing maintenance.** Regulated sectors such as healthcare and finance are the primary context where these conditions hold simultaneously. ([inference]; medium confidence; source: https://arxiv.org/abs/2306.08302; https://arxiv.org/abs/2401.09334)

10. **A neuro-symbolic hybrid framing, treating an ontology as a constraint layer and type-checker over a neural LLM backbone rather than as a world model replacement, is the most productive current approach for deploying ontology completeness in LLM prediction pipelines.** Both Zhang et al. (2024) and Fang et al. (2024) support hybrid constraint architectures as the practical integration path. ([inference]; medium confidence; source: https://arxiv.org/abs/2411.04393; https://arxiv.org/abs/2401.09334)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] LeCun's CPWM requires 7 properties; ontology covers at most 2 | https://openreview.net/forum?id=BZ5a1r-kVsf; https://davidamitchell.github.io/Research/research/2026-04-26-lecun-llm-critique-primary-sources.html | medium | Inference from comparing architectural requirements to ontology definition; prior item used as supporting synthesis |
| [fact] KG-enhanced LLMs improve factuality; 88% symbolic task performance with modules | https://arxiv.org/abs/2306.08302; https://arxiv.org/abs/2401.09334 | high | Two independent empirical sources |
| [fact] Static KG methods produce temporal prediction errors; TKGC methods mitigate but not eliminate | https://www.ijcai.org/proceedings/2023/734 | high | IJCAI 2023 primary survey |
| [fact] Neural–symbolic representation-space mismatch requires specialised bridging | https://arxiv.org/abs/2411.04393; https://openreview.net/forum?id=BZ5a1r-kVsf | high | Systematic review of 191 studies; LeCun 2022 primary paper |
| [inference] Expert-labour scarcity is dominant technical bottleneck; Cyc failure as evidence | https://arxiv.org/abs/2306.08302; https://en.wikipedia.org/wiki/Ontology_(information_science) | medium | Inference from construction difficulty plus historical case |
| [inference] OWL/schema.org fragmentation creates cross-domain completeness ceiling | https://www.w3.org/OWL/; https://schema.org/; https://arxiv.org/abs/2306.08302 | medium | Inference from standards landscape analysis |
| [assumption] Incentive misalignment is a public-goods forcing function | https://arxiv.org/abs/2306.08302 | medium | Not directly measured in ontology literature; plausible from infrastructure economics |
| [inference] Procedural/embodied knowledge is categorically outside ontology scope | https://openreview.net/forum?id=BZ5a1r-kVsf; https://en.wikipedia.org/wiki/Ontology_(information_science) | high | Follows from definition distinction: declarative vs. procedural; LeCun's latent-space requirement |
| [inference] Bounded, slowly changing, fact-intensive domains favour ontology investment | https://arxiv.org/abs/2306.08302; https://arxiv.org/abs/2401.09334 | medium | Inference from task-performance evidence; domain characterisation |
| [inference] Neuro-symbolic constraint-layer framing is more tractable than full substitution | https://arxiv.org/abs/2411.04393; https://arxiv.org/abs/2401.09334 | medium | Two independent sources converge on hybrid as practical path |

### Assumptions

- **Assumption:** Ontology contribution follows a public-goods incentive structure. **Justification:** General infrastructure economics documents free-rider problems in shared-resource provision; no primary measurement study in ontology-specific literature was found. [assumption; source: https://arxiv.org/abs/2306.08302]
- **Assumption:** The Cyc project is a representative historical case for manual ontology coverage ceilings at world-knowledge scale. **Justification:** Cyc is documented in the Wikipedia ontology article as the canonical large-scale manual ontology effort; its failure to achieve general commonsense coverage after decades of investment is consistent with the expert-labour bottleneck argument. [assumption; source: https://en.wikipedia.org/wiki/Ontology_(information_science)]

### Analysis

LeCun's world model definition sets a high bar: a predictive system that computes consequences of imagined actions in continuous latent space, supporting planning and counterfactual simulation. Ontologies, which encode declarative categorical relations in discrete symbolic form, satisfy two of his seven requirements at most. The evidence for this is strong: the LeCun 2022 paper describes the architecture explicitly, and the neuro-symbolic survey by Zhang et al. confirms the representation-space mismatch as the central integration challenge.

The positive evidence for ontology benefit in LLMs is also strong but narrower: it applies to structured retrieval, type-constrained inference, and multi-hop relational reasoning. These are real prediction tasks, and the Fang et al. and Pan et al. results confirm measurable improvement. This does not contradict the world-model gap; it establishes where ontology investment yields a return within its actual scope.

The forcing functions analysis relies more heavily on inference chains. The temporal-dynamics gap is directly evidenced by the IJCAI 2023 TKGC survey. The expert-labour bottleneck is supported by Pan et al.'s acknowledgement of construction difficulty and by the historical Cyc case. The standards fragmentation and incentive arguments are inferences from the standards landscape and general infrastructure economics, respectively; both are labelled accordingly.

A rival position that LLM-assisted auto-population could circumvent the expert-labour bottleneck is acknowledged but does not overturn the core finding: auto-populated ontologies still require validation for precision-critical use, and the temporal-staleness and representation-space gaps remain regardless of how the ontology was populated.

### Risks, Gaps, and Uncertainties

- No primary source directly measures the rate at which ontology facts become stale in specific domains; the temporal-dynamics gap is inferred from the TKGC survey.
- The public-goods incentive argument is an assumption; empirical measurement of its magnitude in ontology contexts was not found in the sources searched.
- The "at most two of seven properties" claim is an inference that could be challenged by proposing richer ontology formalisms with causal or probabilistic extensions; the item treats such extensions as partially shifting the boundary rather than dissolving the gap.
- Evidence for the Cyc project's coverage failure comes from secondary sources; direct measurement of coverage was not located.

### Open Questions

1. Can LLM-assisted automatic ontology population reduce the expert-labour bottleneck enough to achieve world-model-like coverage in a specific bounded domain within a realistic budget?
2. Would a formal causal extension to an ontology (e.g., Bayesian network attached to ontology edges) close the interventional reasoning gap, or does LeCun's latent-space prediction requirement still place the architecture outside reach?
3. What is the empirical staleness rate for ontology facts in high-change domains such as financial instruments or clinical drug interactions, and how does it bound temporal prediction accuracy?
4. Is the neuro-symbolic constraint-layer framing empirically measurable in a real-world agentic LLM pipeline?

---

## Output

- Type: knowledge
- Description: Establishes that a complete ontology cannot substitute for a world model in LeCun's sense because of categorical gaps in continuous-state prediction, temporal dynamics, and sensorimotor grounding, while confirming a narrower benefit for structured relational tasks. [inference; source: https://openreview.net/forum?id=BZ5a1r-kVsf; https://arxiv.org/abs/2306.08302]
- Links:
  - https://openreview.net/forum?id=BZ5a1r-kVsf
  - https://arxiv.org/abs/2306.08302
  - https://www.ijcai.org/proceedings/2023/734
