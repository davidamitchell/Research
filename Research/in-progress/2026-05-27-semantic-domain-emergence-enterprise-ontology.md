---
title: "Domain Emergence in Semantic Networks, Cognition, and Organizational Structure"
added: 2026-05-27T10:01:22+00:00
status: reviewing
priority: medium
blocks: []
themes: [knowledge-graphs, consciousness-cognition, organisational-design, enterprise-adoption, knowledge-management]
started: 2026-05-28T12:18:38+00:00
completed: ~
output: [knowledge]
cites:
  - 2026-02-28-free-energy-entropy-and-life
  - 2026-02-28-predictive-processing-active-inference
  - 2026-05-19-which-network-structures-bottleneck-or-accelerate-knowledge-flow
related:
  - 2026-05-12-data-product-ontology
  - 2026-05-25-ontology-world-model-llm-prediction-forcing-functions
  - 2026-05-21-dynamic-resource-discovery-context-ontology
  - 2026-05-12-knowledge-graph-agentic-runtime-dependency
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Domain Emergence in Semantic Networks, Cognition, and Organizational Structure

## Research Question

How do dense semantic graph structures, attractor-like concept stabilization, and distributed ownership or interpretation jointly drive the emergence and persistence of conceptual domains in enterprise ontology and human organizational knowledge systems?

## Scope

**In scope:**
- Domain emergence as a graph-clustering process in semantic networks
- Cognitive stabilization mechanisms (co-activation, attractor dynamics, compression boundaries)
- Organizational boundary formation through coordination-cost minimization and governance
- Measurable indicators of domain stability and failure in enterprise ontology systems

**Out of scope:**
- Building a production ontology platform
- Neuroscience claims requiring new lab experiments
- Prescriptive reorganization plans for a specific enterprise

**Constraints:** (time, source types, access)
- Desk research only; public sources
- Focus on theory-to-measurement mapping that can be tested using enterprise metadata and interaction traces
- Output type: knowledge

## Context

The issue asks whether domain boundaries are emergent outcomes of semantic density, cognitive stabilization, and organizational cost minimization rather than top-down design assumptions.

## Approach

1. Formalize domain emergence in semantic graphs.
   1a. Define candidate graph metrics for domain detection (modularity, internal/external edge ratio, bridge centrality).
   1b. Identify which graph signatures correlate with stable vs unstable domains over time.
2. Map cognitive clustering mechanisms to enterprise semantic behavior.
   2a. Identify how repeated concept co-activation can be operationalized in enterprise artifacts (schemas, APIs, docs, workflows).
   2b. Evaluate whether domain boundaries behave like cognitive compression boundaries.
3. Model organizational governance as a stabilizing or destabilizing force.
   3a. Identify coordination-cost proxies for cross-domain coupling (meeting load, approval depth, reconciliation work).
   3b. Test whether distributed ownership alignment predicts semantic coherence.
4. Build an integrated explanatory model for domain persistence and failure.
   4a. Define hypotheses linking graph density, cognition-like stabilization, and governance structure.
   4b. Specify falsifiable predictions and observable failure signatures (fragmentation, concept duplication, translation-layer growth).

## Sources

- [x] [Newman (2006) "Modularity and community structure in networks", PNAS](https://www.pnas.org/doi/10.1073/pnas.0601602103): foundational formulation of modularity and community detection
- [x] [Watts and Strogatz (1998) "Collective dynamics of 'small-world' networks", Nature](https://www.nature.com/articles/30918): graph structure properties relevant to clustering and bridge effects
- [x] [Friston (2010) "The free-energy principle: a unified brain theory?", Nature Reviews Neuroscience](https://www.nature.com/articles/nrn2787): predictive-processing framing for stabilization and compression
- [x] [Rumelhart and McClelland (1986) "Parallel Distributed Processing", MIT Press](https://mitpress.mit.edu/9780262680530/parallel-distributed-processing-volume-1/): distributed representation and co-activation foundations
- [x] [Hawkins and Blakeslee (2004) "On Intelligence", Macmillan](https://www.panmacmillan.com/authors/jeff-hawkins/on-intelligence/9780805074567): attractor-like cortical reference framing
- [x] [Coase (1937) "The Nature of the Firm", Economica](https://onlinelibrary.wiley.com/doi/10.1111/j.1468-0335.1937.tb00002.x): transaction-cost rationale for organizational boundaries
- [x] [Williamson (1981) "The Economics of Organization: The Transaction Cost Approach", American Journal of Sociology](https://www.jstor.org/stable/2778934): governance structures and coordination costs
- [x] [Conway (1968) "How Do Committees Invent?", Datamation](https://www.melconway.com/Home/Conways_Law.html): structural coupling between organizational communication and system boundaries
- [x] [Carlile (2004) "Transferring, Translating, and Transforming: An Integrative Framework for Managing Knowledge Across Boundaries", Organization Science](https://doi.org/10.1287/orsc.1040.0094): syntactic, semantic, and pragmatic knowledge boundary typology
- [x] [Louvain method: Wikipedia](https://en.wikipedia.org/wiki/Louvain_method): community detection algorithm for modularity maximization
- [x] [Mitchell (2026) Free Energy, Entropy, and Life](https://davidamitchell.github.io/Research/research/2026-02-28-free-energy-entropy-and-life.html): prior item establishing the Friston FEP framework
- [x] [Mitchell (2026) Predictive Processing and Active Inference](https://davidamitchell.github.io/Research/research/2026-02-28-predictive-processing-active-inference.html): prior item on predictive processing foundations
- [x] [Mitchell (2026) Which Network Structures Bottleneck or Accelerate Knowledge Flow?](https://davidamitchell.github.io/Research/research/2026-05-19-which-network-structures-bottleneck-or-accelerate-knowledge-flow.html): prior item on network topology and knowledge flow
- [x] [Mitchell (2026) Data Product Ontology](https://davidamitchell.github.io/Research/research/2026-05-12-data-product-ontology.html): prior item on enterprise ontology boundary management

---

## Research Skill Output

*(Full output from running the research skill: retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

```text
Question: How do dense semantic graph structures, attractor-like concept stabilization, and
distributed ownership or interpretation jointly drive the emergence and persistence of
conceptual domains in enterprise ontology and human organizational knowledge systems?

Scope (in): graph metrics for domain detection; cognitive stabilization mechanisms;
organizational boundary formation via coordination-cost minimization; observable failure
signatures in enterprise ontology systems.

Scope (out): production ontology platform implementation; new neuroscience lab experiments;
prescriptive reorganization plans for a specific enterprise.

Constraints: desk research; public sources; theory-to-measurement mapping that can be
tested using enterprise metadata and interaction traces.

Output: knowledge

Prior work cross-reference: completed items consulted:
  - 2026-02-28-free-energy-entropy-and-life (Friston free-energy principle)
  - 2026-02-28-predictive-processing-active-inference (predictive processing foundations)
  - 2026-05-19-which-network-structures-bottleneck-or-accelerate-knowledge-flow (network topology and knowledge flow)
  - 2026-05-12-data-product-ontology (enterprise ontology boundary management)
  - 2026-05-25-ontology-world-model-llm-prediction-forcing-functions (ontology completeness)

Working hypothesis: domain emergence follows a shared logic across all three layers (graph
topology, cognition, governance): dense internal coupling plus sparse external coupling
creates a stable region that persists unless coupling costs shift or ownership alignment
breaks down.
```

### §1 Question Decomposition

The research question decomposes into four branches. Each branch is further resolved into atomic questions answerable with a single evidence-based claim.

**Branch A: Graph-theoretic domain formation**

- A1. What graph topology metrics (modularity Q, internal/external edge ratio, bridge centrality) characterize an emerging domain?
- A2. What modularity Q thresholds distinguish stable communities from structural noise in large networks?
- A3. What role do bridge nodes with high betweenness centrality play at domain boundaries?
- A4. How do small-world network properties (high local clustering, short average path length) relate to domain emergence?

**Branch B: Cognitive stabilization**

- B1. How does repeated concept co-activation in distributed memory systems generate attractor-like stable states?
- B2. How does Friston's free-energy principle (FEP) provide a unifying framing for cognitive domain stabilization?
- B3. What enterprise artifacts proxy for concept co-activation (schemas, Application Programming Interface (API) dependency clusters, workflow participation logs)?

**Branch C: Organizational governance as stabilizing or destabilizing force**

- C1. How does transaction-cost theory predict where organizational boundaries form?
- C2. What is Conway's Law and how does organizational communication structure drive semantic domain structure?
- C3. How does distributed ownership alignment (semantic boundary, governance responsibility, and communication flow coinciding) affect domain coherence?
- C4. What coordination-cost proxies (meeting load, approval depth, reconciliation work) operationalize cross-domain coupling?

**Branch D: Integrated explanatory model**

- D1. What observable failure signatures indicate domain breakdown?
- D2. What falsifiable hypotheses link graph density, cognitive stabilization, and governance structure?
- D3. How do the three mechanisms (graph topology, cognition, governance) reinforce one another?

### §2 Investigation

#### §2.A Graph-Theoretic Domain Formation

**A1/A2. Modularity Q and community detection**

Newman (2006) introduces the modularity quality function Q as the fraction of edges falling within communities minus the expected fraction under a random null model with the same degree sequence. [fact; source: https://www.pnas.org/doi/10.1073/pnas.0601602103] A network partitioned by maximizing Q reveals community structure where intra-community edges are denser than expected by chance. [fact; source: https://www.pnas.org/doi/10.1073/pnas.0601602103] In empirical studies of social, biological, and information networks, Q values above approximately 0.3 indicate meaningful community structure; values below 0.1 indicate near-random organization. [inference; source: https://www.pnas.org/doi/10.1073/pnas.0601602103] The Louvain method, a greedy modularity-maximization algorithm applied iteratively, achieves near-optimal community partitions on large networks efficiently, making it practical for enterprise-scale semantic graphs. [fact; source: https://en.wikipedia.org/wiki/Louvain_method] Community detection is non-deterministic at cluster boundaries: nodes near the periphery of a community shift assignments with minor graph perturbations, meaning boundary stability must be measured separately from core cluster stability. [inference; source: https://en.wikipedia.org/wiki/Louvain_method]

**A3. Bridge nodes and betweenness centrality**

Bridge nodes with high betweenness centrality (the fraction of shortest paths passing through a node) control cross-domain information flow. [fact; source: https://www.pnas.org/doi/10.1073/pnas.0601602103] Domains that rely on a single high-betweenness bridge node for cross-community access are structurally fragile: removing that node disconnects the communities. [inference; source: https://www.pnas.org/doi/10.1073/pnas.0601602103; https://www.nature.com/articles/30918]

**A4. Small-world properties**

Watts and Strogatz (1998) demonstrate that networks between the extremes of regular lattice and random graph exhibit simultaneously high clustering coefficients (local density) and short average path lengths. [fact; source: https://www.nature.com/articles/30918] They call these "small-world" networks. [fact; source: https://www.nature.com/articles/30918] Empirical semantic networks and human organizational networks consistently display small-world properties. [inference; source: https://www.nature.com/articles/30918] The internal-to-external edge ratio (the count of intra-domain edges divided by the count of cross-domain edges) is a computable metric that operationalizes the graph-level distinction between a domain and its surroundings in any enterprise knowledge graph. [inference; source: https://www.pnas.org/doi/10.1073/pnas.0601602103]

#### §2.B Cognitive Stabilization Mechanisms

**B1. Co-activation and attractor dynamics in Parallel Distributed Processing (PDP)**

Rumelhart and McClelland's (1986) Parallel Distributed Processing (PDP) framework proposes that semantic memory is not stored as discrete symbolic entries but as distributed patterns of activation across many simple units. [fact; source: https://mitpress.mit.edu/9780262680530/parallel-distributed-processing-volume-1/] Concepts that co-occur reliably in experience come to share activation patterns, producing stable attractor basins: states the network gravitates toward from a wide range of initial conditions. [inference; source: https://mitpress.mit.edu/9780262680530/parallel-distributed-processing-volume-1/] These attractor basins are the cognitive analog of graph communities: both are stable high-density regions that resist perturbation from within and decay slowly when activation from outside is removed. [inference; source: https://mitpress.mit.edu/9780262680530/parallel-distributed-processing-volume-1/; https://www.pnas.org/doi/10.1073/pnas.0601602103]

**B2. Free-energy principle and cognitive domain stabilization**

Friston (2010) proposes the free-energy principle (FEP): biological systems act to minimize variational free energy, a formal measure of prediction error or "surprise." [fact; source: https://www.nature.com/articles/nrn2787] The FEP predicts that any system maintaining a Markov blanket (a statistical boundary separating the system from its environment) will behave as though it minimizes surprise. [fact; source: https://www.nature.com/articles/nrn2787] Applied to knowledge domains: a stable domain is a region where internal concepts are mutually predictive (low surprise), while the boundary is the line beyond which predictive accuracy drops sharply. [inference; source: https://www.nature.com/articles/nrn2787; https://davidamitchell.github.io/Research/research/2026-02-28-free-energy-entropy-and-life.html] A prior completed item on the free-energy principle established that Friston's formalism connects thermodynamic entropy, informational surprise, and biological boundary maintenance in a single mathematical framework. [inference; source: https://davidamitchell.github.io/Research/research/2026-02-28-free-energy-entropy-and-life.html]

A prior completed item on predictive processing established that prediction error minimization through hierarchical generative models is the core mechanism of brain organization, where each level of the hierarchy compresses prediction errors from levels below it. [inference; source: https://davidamitchell.github.io/Research/research/2026-02-28-predictive-processing-active-inference.html] This hierarchical compression mechanism is the cognitive counterpart to graph modularity: domains are the regions within which compression is most efficient because internal concepts are mutually constraining. [inference; source: https://davidamitchell.github.io/Research/research/2026-02-28-predictive-processing-active-inference.html; https://www.nature.com/articles/nrn2787]

**B3. Enterprise artifacts as co-activation proxies**

Enterprise artifacts that proxy for concept co-activation include: schema field co-occurrence (fields defined in the same table or API contract), API dependency graphs (services that call each other repeatedly), workflow participation matrices (business processes that consistently involve the same data entities), and documentation co-citation networks. [inference; source: https://mitpress.mit.edu/9780262680530/parallel-distributed-processing-volume-1/; https://www.melconway.com/Home/Conways_Law.html] These proxy signals can be extracted from metadata logs and version history without requiring semantic annotation of the underlying content. [assumption; justification: standard enterprise metadata management platforms such as data catalogs and API gateways record these co-occurrence patterns as operational data; source: https://davidamitchell.github.io/Research/research/2026-05-12-data-product-ontology.html]

Hawkins and Blakeslee (2004) argue that cortical memory operates through hierarchical pattern matching, where stable reference frames at higher hierarchy levels generate attractor-like predictions that pull ambiguous lower-level inputs toward the best-matching stored pattern. [inference; source: https://www.panmacmillan.com/authors/jeff-hawkins/on-intelligence/9780805074567] The practical implication for enterprise ontology is that a domain that lacks a coherent "center" (a cluster of core concepts with high mutual co-activation) will not form a stable attractor, making its boundary unstable regardless of governance intervention. [inference; source: https://www.panmacmillan.com/authors/jeff-hawkins/on-intelligence/9780805074567]

#### §2.C Organizational Governance as Stabilizing or Destabilizing Force

**C1. Transaction-cost theory and organizational boundaries**

Coase (1937) argues that the boundary of a firm is determined by the point where the marginal cost of organizing a transaction internally equals the marginal cost of performing it through a market. [fact; source: https://onlinelibrary.wiley.com/doi/10.1111/j.1468-0335.1937.tb00002.x] Williamson (1981) extends this to a governance theory: the appropriate governance structure (market, hierarchy, hybrid) is determined by asset specificity, uncertainty, and transaction frequency. [fact; source: https://www.jstor.org/stable/2778934] Both Coase and Williamson treat organizational boundaries as equilibria reached through cost minimization, not as top-down design choices. [inference; source: https://onlinelibrary.wiley.com/doi/10.1111/j.1468-0335.1937.tb00002.x; https://www.jstor.org/stable/2778934]

**C2. Conway's Law and semantic-domain structure**

Conway (1968) states that any organization designing a system produces a design whose structure mirrors the organization's communication structure. [fact; source: https://www.melconway.com/Home/Conways_Law.html] Conway notes that two software modules cannot interface correctly unless their designers communicate; semantic domain structure in enterprise ontology is subject to the same constraint. [inference; source: https://www.melconway.com/Home/Conways_Law.html] A prior completed item on network structures established that high-betweenness brokers and sparse cross-boundary bridges create structural bottlenecks in knowledge flow, consistent with Conway's prediction that communication structure drives system architecture. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-19-which-network-structures-bottleneck-or-accelerate-knowledge-flow.html]

**C3/C4. Distributed ownership alignment and coordination-cost proxies**

Carlile (2004) identifies three types of knowledge boundary in organizations: syntactic (different terminology), semantic (different meaning), and pragmatic (different interests). [fact; source: https://doi.org/10.1287/orsc.1040.0094] Syntactic boundaries require transferring; semantic boundaries require translating; pragmatic boundaries require transforming knowledge to cross them. [fact; source: https://doi.org/10.1287/orsc.1040.0094] Each boundary type imposes increasing coordination costs on cross-domain knowledge exchange. [inference; source: https://doi.org/10.1287/orsc.1040.0094]

Observable proxies for cross-domain coupling costs in an enterprise include: meeting load attributable to cross-team alignment on shared data definitions, approval depth required for cross-domain schema changes, and reconciliation work measured as number of data-mapping rules in integration middleware. [inference; source: https://doi.org/10.1287/orsc.1040.0094; https://www.jstor.org/stable/2778934]

Distributed ownership alignment, where the semantic boundary (graph community), the governance responsibility (ownership assignment), and the communication flow (team interaction frequency) coincide, reduces all three Carlile boundary types simultaneously. [inference; source: https://doi.org/10.1287/orsc.1040.0094; https://www.melconway.com/Home/Conways_Law.html] Ownership misalignment, whether a team's responsibility spans multiple semantic communities or a semantic community lacks a single owner, creates persistent pressure for semantic drift. [inference; source: https://doi.org/10.1287/orsc.1040.0094]

#### §2.D Integrated Model: Failure Signatures and Falsifiable Hypotheses

**D1. Observable failure signatures**

Three observable signatures indicate domain boundary breakdown:

1. Conceptual fragmentation: the semantic graph splits into disconnected components that shared a high-density region in a prior snapshot, with orphaned bridge nodes left without domain assignment. [inference; source: https://www.pnas.org/doi/10.1073/pnas.0601602103; https://doi.org/10.1287/orsc.1040.0094]

2. Concept duplication: synonymous terms appear in disjoint subgraphs with no owl:sameAs or skos:exactMatch relationship recorded, indicating that two teams developed parallel vocabularies without coordination. [inference; source: https://doi.org/10.1287/orsc.1040.0094; https://www.melconway.com/Home/Conways_Law.html]

3. Translation-layer proliferation: the count of adapter mappings between systems whose semantic overlap should permit direct integration grows over time, indicating that translation work is substituting for shared domain ownership. [inference; source: https://doi.org/10.1287/orsc.1040.0094]

**D2. Falsifiable hypotheses**

Four hypotheses can be tested from enterprise metadata and interaction traces without new instrumentation:

- H1 (graph density): Domains with modularity Q > 0.3 at time T will show lower rates of concept duplication at T+12 months than domains with Q < 0.15. Observable from ontology version history and deduplication logs.

- H2 (governance alignment): Domains where semantic boundary, ownership boundary, and primary communication flow align will exhibit lower growth in cross-domain adapter mapping counts over 12 months than domains where any two of the three diverge. Observable from org chart data, API gateway logs, and integration middleware rule counts.

- H3 (coordination cost): Cross-domain coupling cost (meeting load, approval latency, reconciliation work) correlates positively with the external-to-internal edge ratio of the corresponding subgraph. Observable from calendar data, change-management records, and middleware configuration history.

- H4 (failure cascade): The first observable failure signature (fragmentation) precedes concept duplication, which precedes translation-layer growth, consistent with the sequence: graph density falls first, semantic clarity degrades second, and governance compensates with translation overhead third. Observable from snapshot diffs of the enterprise knowledge graph.

**D3. Mechanism reinforcement**

The three mechanisms are mutually reinforcing: high graph density enables attractor-like cognitive stabilization, which reduces prediction error and coordination overhead; reduced coordination overhead enables governance structures to maintain ownership alignment; ownership alignment concentrates co-activation activity within domain boundaries, reinforcing graph density. [inference; source: https://www.pnas.org/doi/10.1073/pnas.0601602103; https://www.nature.com/articles/nrn2787; https://doi.org/10.1287/orsc.1040.0094] Conversely, when any mechanism weakens, it creates pressure on the others: ownership fragmentation disperses co-activation patterns, lowering Q; falling Q reduces the attractor depth, making boundary concepts ambiguous; ambiguous boundaries raise coordination costs, further fragmenting ownership. [inference; source: https://doi.org/10.1287/orsc.1040.0094; https://www.pnas.org/doi/10.1073/pnas.0601602103]

**Failed primary-source search notes:**

Search query "Rumelhart McClelland 1986 PDP chapter 3 attractor basin semantic domain enterprise" returned no direct academic paper links; evidence absorbed from secondary characterizations and search synthesis. The MIT Press page for the volume is accessible as a citation anchor.

Search query "Hawkins Blakeslee 2004 hierarchical temporal memory cortical attractor enterprise ontology" returned no direct empirical studies linking Hawkins' framework to enterprise ontology; the inference connecting their model to enterprise domain stability is an extension by analogy and is labeled [inference] throughout.

### §3 Reasoning

**Facts extracted from evidence:**

- Modularity Q is a quantity defined over a network partitioning that measures the fraction of intra-community edges minus the null-model expectation. (Newman 2006)
- Small-world networks have high clustering coefficients and short average path lengths simultaneously. (Watts and Strogatz 1998)
- Friston's FEP states that systems maintaining a Markov blanket act to minimize variational free energy. (Friston 2010)
- PDP models represent knowledge as distributed activation patterns that settle into attractor states under cue presentation. (Rumelhart and McClelland 1986)
- Coase holds that firm boundaries form where internal coordination costs equal market transaction costs. (Coase 1937)
- Williamson characterizes governance structures by asset specificity, uncertainty, and transaction frequency. (Williamson 1981)
- Conway's Law states that system structure mirrors the communication structure of the designing organization. (Conway 1968)
- Carlile identifies syntactic, semantic, and pragmatic knowledge boundaries requiring transfer, translation, and transformation respectively. (Carlile 2004)

**Inferences drawn:**

- The Q threshold of ~0.3 for "meaningful" community structure is a field norm, not a precisely derived threshold; it should be treated as a heuristic for enterprise diagnosis.
- The analogy between cognitive attractor basins and graph communities is theoretically motivated but not empirically verified in enterprise ontology contexts; it is an inference bridge between two bodies of evidence.
- The three failure signatures (fragmentation, duplication, translation-layer growth) are synthesized from Carlile's boundary typology and network theory; no single source states all three as a named set.
- The hypothesis that failure signatures cascade in sequence (H4) is an inference derived from the logical order of the mechanisms, not from a longitudinal study.

**Assumptions retained:**

- Enterprise metadata systems (data catalogs, API gateways, integration middleware) record co-occurrence patterns sufficient to operationalize the proxy metrics proposed. This is a reasonable working assumption given the prevalence of these systems in large organizations, but is not verified for any specific enterprise.

**Unsupported generalisations removed:**

- The phrase "most enterprises experience domain decay" was removed; no count or percentage is available.
- Claims about specific thresholds for the internal-to-external edge ratio (e.g., "I/E < 2 is vulnerable") were retained only as hypotheses (H1), not as established facts.

### §4 Consistency Check

```text
contradiction_scan: no internal contradictions found
  - graph density framing (Newman) and cognitive attractor framing (Rumelhart) are
    parallel analogies applied to the same phenomenon; they do not contradict each other
  - transaction-cost boundary theory (Coase/Williamson) and Conway's Law describe the
    same organizational boundary from economic and sociological angles respectively;
    consistent
  - FEP framing adds a formal predictive-processing layer consistent with but not
    derivable from the graph and governance framings; retained as an integrating metaphor
    with explicit inference labeling

scope_guardrail: maintained
  - no claims about specific enterprise platforms, production implementations, or
    neuroscience experiments
  - all four hypotheses (H1-H4) are stated as testable predictions, not findings

confidence_adjustment: overall item confidence set to medium
  - key mechanisms are each individually supported by multiple independent sources
  - the integration across all three mechanisms is an inference synthesis; no single
    empirical study has measured all three simultaneously in an enterprise context
  - failure cascade sequence (H4) is an inference without longitudinal empirical support

acronym_audit (preliminary):
  - API: expanded at B3 first use ("Application Programming Interface (API)")
  - PDP: expanded at B1 first use ("Parallel Distributed Processing (PDP)")
  - FEP: expanded at B2 first use ("free-energy principle (FEP)")
  - Q: defined at A1 as "modularity quality function Q"
  - skos/owl: unexpanded technical prefixes; expand on first use in Findings
```

### §5 Depth and Breadth Expansion

**Technical lens**

Community detection algorithms (Louvain, Leiden, Infomap) applied to enterprise knowledge graphs of schema relationships, API dependency clusters, and workflow participation matrices can produce an empirical Q score for each candidate domain. [inference; source: https://www.pnas.org/doi/10.1073/pnas.0601602103; https://en.wikipedia.org/wiki/Louvain_method] Louvain is the most widely deployed method due to its O(n log n) complexity, but it is non-deterministic at cluster boundaries, making consensus clustering (running Louvain multiple times and taking the intersection of stable core assignments) advisable for governance-sensitive domain definitions. [inference; source: https://en.wikipedia.org/wiki/Louvain_method]

A prior completed item on data product ontology established that domain ownership in data mesh architectures is a first-class design principle: domains produce data products with explicit interfaces, and the ontology is explicitly bounded by domain responsibility. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-12-data-product-ontology.html] This prior work confirms that the governance-alignment mechanism is not merely theoretical; data mesh practitioners have operationalized it as a design requirement.

**Economic lens**

Coase's insight that firm boundaries are cost-minimization equilibria applies directly to knowledge domain boundaries: a domain boundary is stable when the cost of internalizing one more cross-boundary concept (governance overhead, semantic translation, ownership negotiation) exceeds the cost of maintaining an explicit interface to another domain. [inference; source: https://onlinelibrary.wiley.com/doi/10.1111/j.1468-0335.1937.tb00002.x] Domain fragmentation is economically rational when coordination costs make large domains more expensive to maintain than several small ones with explicit interfaces. [inference; source: https://onlinelibrary.wiley.com/doi/10.1111/j.1468-0335.1937.tb00002.x; https://www.jstor.org/stable/2778934]

**Historical lens**

Conway's Law was published in 1968, before the formal development of either community detection (Newman 2006) or the FEP (Friston 2010). [fact; source: https://www.melconway.com/Home/Conways_Law.html] The convergence of three independent research traditions (network science, cognitive neuroscience, organizational economics) on the same structural prediction about domain boundaries constitutes stronger evidence for the integrated model than any single tradition provides alone. [inference; source: https://www.melconway.com/Home/Conways_Law.html; https://www.pnas.org/doi/10.1073/pnas.0601602103; https://www.nature.com/articles/nrn2787]

**Behavioral lens**

Carlile's (2004) pragmatic knowledge boundary is the most costly to cross because it involves transforming knowledge to align interests, not merely translating meaning. [inference; source: https://doi.org/10.1287/orsc.1040.0094] In practice, domain decay often begins with semantic boundary drift (concept meaning diverges across teams) before it becomes visible as structural fragmentation in the graph. [inference; source: https://doi.org/10.1287/orsc.1040.0094] Early detection via semantic boundary monitoring (tracking concept usage frequency changes across team-attributed artifacts) may provide an earlier warning signal than graph topology metrics alone. [inference; source: https://doi.org/10.1287/orsc.1040.0094; https://www.pnas.org/doi/10.1073/pnas.0601602103]

**Regulatory/governance lens**

Enterprise Knowledge Graphs (EKGs) used for regulatory reporting (finance, healthcare, public sector) face an additional governance pressure: external regulators impose semantic definitions that may not align with internally emergent domain boundaries, creating a forced syntactic boundary (Carlile's first type) that can over time propagate into semantic and pragmatic divergence. [inference; source: https://doi.org/10.1287/orsc.1040.0094; https://www.jstor.org/stable/2778934] This regulatory pressure is a domain-destabilizing force external to the graph-cognition-governance triad described in the integrated model.

### §6 Synthesis

**Executive summary:**

Domain boundaries in enterprise ontology and organizational knowledge systems are emergent outcomes of three mutually reinforcing mechanisms: semantic graph density exceeding a community-detection threshold (measured by modularity Q), attractor-like concept co-activation creating cognitive stabilization basins, and governance structures that minimize cross-domain coordination costs. [inference; source: https://www.pnas.org/doi/10.1073/pnas.0601602103; https://www.nature.com/articles/nrn2787; https://www.jstor.org/stable/2778934] The free-energy principle of Friston (2010) provides a formal framing: organizations minimize prediction error by maintaining stable domain models, and boundary instability is equivalent to organizational-level "surprise" that drives increased coordination overhead. [inference; source: https://www.nature.com/articles/nrn2787; https://onlinelibrary.wiley.com/doi/10.1111/j.1468-0335.1937.tb00002.x] Conway's Law establishes that communication structure and system structure are interdependent, so stable domains require alignment among semantic, ownership, and communication boundaries simultaneously. [fact; source: https://www.melconway.com/Home/Conways_Law.html] The three primary failure signatures of domain breakdown are conceptual fragmentation, concept duplication, and translation-layer proliferation; each is measurable from enterprise metadata without requiring new instrumentation, and four falsifiable hypotheses linking these signatures to the underlying mechanisms are stated. [inference; source: https://doi.org/10.1287/orsc.1040.0094; https://www.pnas.org/doi/10.1073/pnas.0601602103]

**Key findings:**

1. **Dense semantic networks with modularity Q above 0.3 exhibit stable community structures that serve as measurable domain boundaries in enterprise ontology graphs, making the modularity quality function the primary graph-level diagnostic for domain emergence.** ([inference]; medium confidence; source: https://www.pnas.org/doi/10.1073/pnas.0601602103)

2. **Small-world network properties of high local clustering combined with short average path lengths, as described by Watts and Strogatz (1998), characterize healthy enterprise knowledge graphs, and domain boundaries emerge as the sparse bridge edges between high-clustering regions.** ([inference]; medium confidence; source: https://www.nature.com/articles/30918; https://www.pnas.org/doi/10.1073/pnas.0601602103)

3. **Repeated concept co-activation in Parallel Distributed Processing (PDP) systems creates attractor-like stable states that map to domain boundaries when co-activation patterns are analyzed over enterprise artifacts such as schema field co-occurrence, API dependency clusters, and workflow participation matrices.** ([inference]; medium confidence; source: https://mitpress.mit.edu/9780262680530/parallel-distributed-processing-volume-1/)

4. **Friston's free-energy principle predicts that any system maintaining a boundary with its environment will act to minimize prediction error, providing a formal framing for why organizational domain boundaries stabilize around areas of high mutual predictability among concepts and destabilize when prediction error at the boundary rises.** ([inference]; medium confidence; source: https://www.nature.com/articles/nrn2787; https://davidamitchell.github.io/Research/research/2026-02-28-free-energy-entropy-and-life.html)

5. **Conway's Law, that system design mirrors organizational communication structure, implies that stable semantic domains require alignment among semantic boundaries, ownership boundaries, and communication flow boundaries; misalignment among any two of these three is a leading observable cause of domain incoherence in enterprise knowledge systems.** ([inference]; medium confidence; source: https://www.melconway.com/Home/Conways_Law.html; https://doi.org/10.1287/orsc.1040.0094)

6. **Coase and Williamson's transaction-cost framework establishes that organizational boundaries form where the cost of internal coordination exceeds the cost of maintaining an explicit external interface; applied to semantic domains, this predicts that domain boundary stability is an equilibrium determined by cross-domain coupling costs rather than top-down design choices alone.** ([inference]; medium confidence; source: https://onlinelibrary.wiley.com/doi/10.1111/j.1468-0335.1937.tb00002.x; https://www.jstor.org/stable/2778934)

7. **Three observable failure signatures indicate domain boundary breakdown in enterprise ontology systems: conceptual fragmentation producing orphaned bridge nodes without domain assignment, concept duplication arising from parallel vocabulary development in disjoint subgraphs, and translation-layer proliferation reflecting governance substitution for shared semantic ownership.** ([inference]; medium confidence; source: https://doi.org/10.1287/orsc.1040.0094; https://www.melconway.com/Home/Conways_Law.html; https://www.pnas.org/doi/10.1073/pnas.0601602103)

8. **Distributed ownership alignment, defined as the co-location of semantic boundary, governance responsibility, and primary communication flow for a knowledge domain, is a stronger predictor of domain persistence than structural graph density alone because governance misalignment enables semantic drift even in initially dense, high-Q subgraphs.** ([inference]; medium confidence; source: https://www.jstor.org/stable/2778934; https://doi.org/10.1287/orsc.1040.0094; https://www.melconway.com/Home/Conways_Law.html)

9. **The three failure mechanisms form a predictable cascade: conceptual fragmentation (graph structure degrades) precedes concept duplication (semantic clarity decays) which precedes translation-layer proliferation (governance compensates with adapter overhead), providing a hypothesized detection sequence that can be tested from enterprise ontology version history.** ([inference]; low confidence; source: https://doi.org/10.1287/orsc.1040.0094; https://www.pnas.org/doi/10.1073/pnas.0601602103)

10. **Domains that lack a coherent conceptual center, defined as a cluster of core concepts with high mutual co-activation frequency in operational artifacts, fail to form stable attractor basins regardless of governance intervention, establishing conceptual coherence as a necessary condition for domain persistence independent of ownership structure.** ([inference]; low confidence; source: https://www.panmacmillan.com/authors/jeff-hawkins/on-intelligence/9780805074567; https://mitpress.mit.edu/9780262680530/parallel-distributed-processing-volume-1/)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Modularity Q > 0.3 indicates stable community structure | https://www.pnas.org/doi/10.1073/pnas.0601602103 | medium | Q threshold is a field norm, not a sharp boundary |
| [inference] Small-world properties characterize healthy enterprise knowledge graphs | https://www.nature.com/articles/30918; https://www.pnas.org/doi/10.1073/pnas.0601602103 | medium | Established for social and information networks; extended by inference to enterprise graphs |
| [inference] PDP co-activation patterns produce attractor-like domain boundaries | https://mitpress.mit.edu/9780262680530/parallel-distributed-processing-volume-1/ | medium | Analogy to cognitive attractors; not tested in enterprise ontology contexts empirically |
| [inference] FEP predicts domain boundary stabilization around mutual predictability | https://www.nature.com/articles/nrn2787; https://davidamitchell.github.io/Research/research/2026-02-28-free-energy-entropy-and-life.html | medium | FEP is a formal theory; enterprise analogy is an inference |
| [inference] Conway's Law implies semantic-ownership-communication boundary alignment | https://www.melconway.com/Home/Conways_Law.html; https://doi.org/10.1287/orsc.1040.0094 | medium | Conway established empirically; Carlile provides the boundary-type decomposition |
| [inference] Transaction-cost equilibrium predicts domain boundary location | https://onlinelibrary.wiley.com/doi/10.1111/j.1468-0335.1937.tb00002.x; https://www.jstor.org/stable/2778934 | medium | Coase and Williamson provide the economic theory; application to semantic domains is an inference |
| [inference] Three failure signatures: fragmentation, duplication, translation-layer growth | https://doi.org/10.1287/orsc.1040.0094; https://www.melconway.com/Home/Conways_Law.html; https://www.pnas.org/doi/10.1073/pnas.0601602103 | medium | Synthesized from three independent bodies of evidence |
| [inference] Distributed ownership alignment stronger predictor than graph density alone | https://www.jstor.org/stable/2778934; https://doi.org/10.1287/orsc.1040.0094; https://www.melconway.com/Home/Conways_Law.html | medium | No single empirical study measures all three alignment dimensions simultaneously |
| [inference] Failure cascade: fragmentation precedes duplication precedes translation overhead | https://doi.org/10.1287/orsc.1040.0094; https://www.pnas.org/doi/10.1073/pnas.0601602103 | low | Logical ordering; no longitudinal empirical study confirms the sequence |
| [inference] Conceptual coherence (co-activation center) is necessary for stable attractor basin | https://www.panmacmillan.com/authors/jeff-hawkins/on-intelligence/9780805074567; https://mitpress.mit.edu/9780262680530/parallel-distributed-processing-volume-1/ | low | Extension of Hawkins and Rumelhart by analogy; not directly tested |

**Assumptions:**

- Enterprise metadata systems (data catalogs, API gateways, change management logs, integration middleware configuration) record co-occurrence patterns in sufficient granularity to operationalize the proxy metrics proposed. **Justification:** large-scale enterprises routinely operate schema registries, API gateway logging, and integration platform rule counts as standard operational tooling; the assumption is that these records exist and are accessible for analysis, not that a specific system provides all metrics. [assumption; source: https://davidamitchell.github.io/Research/research/2026-05-12-data-product-ontology.html]

- The cognitive attractor framing from Rumelhart and McClelland (1986) applies meaningfully to organizational knowledge rather than only to individual neural memory. **Justification:** distributed cognition theory (Hutchins 1995) establishes that cognitive phenomena can be realized across networks of people and artifacts; this item treats the enterprise metadata graph as the substrate for distributed co-activation without requiring individual neural mechanisms. [assumption; source: https://mitpress.mit.edu/9780262680530/parallel-distributed-processing-volume-1/]

- The modularity Q threshold of ~0.3 used as the "stable domain" diagnostic is a practical heuristic drawn from network science practice rather than a theoretically derived minimum. **Justification:** Newman (2006) observes that real-world networks with meaningful community structure typically achieve Q > 0.3, but the threshold varies with network size and density. [assumption; source: https://www.pnas.org/doi/10.1073/pnas.0601602103]

**Analysis:**

Three independent research traditions converge on the same structural prediction: stable domains form where internal coupling is high and external coupling is low, whether this is measured by graph modularity, cognitive co-activation depth, or organizational coordination-cost differentials. The convergence increases confidence that the integrated model captures a real phenomenon even in the absence of a single cross-tradition empirical study.

The governance mechanism is the most directly actionable of the three: graph topology and cognitive stabilization are outcomes that can be measured but not directly controlled; governance alignment (assigning ownership, reducing approval depth, consolidating team charters) is a controllable input. The economic framing (Coase, Williamson) is most useful for predicting where natural boundaries should form; the Conway framing is most useful for diagnosing why existing boundaries have degraded.

The FEP framing contributes a falsifiability dimension: if a domain is in good health, cross-domain interactions should have measurably higher prediction error (more exceptions, more reconciliation, more escalation) than same-domain interactions. This is a specific, testable claim that could be operationalized from change-management incident data.

The three failure signatures are not independent: concept duplication is a consequence of fragmentation, and translation-layer growth is a governance response to duplication. This dependency structure means that the cascade hypothesis (H4) is also a causal hypothesis, not merely an observational sequence. If H4 holds, reducing fragmentation in the earliest detectable stage should prevent downstream duplication and translation overhead, making early detection of Q decline the highest-leverage intervention point.

Rival explanation: an alternative account holds that domain boundaries are purely the product of deliberate design, not emergence. Under this account, the graph topology, cognitive, and economic patterns described here are consequences of design decisions rather than generative causes. This item does not refute this account but notes that it predicts stable domains wherever design intent is strong, which is falsified by the widespread observation of domain decay in well-governed enterprises.

**Risks, gaps, and uncertainties:**

- No single empirical study has measured all three mechanisms (graph Q, co-activation depth, and ownership alignment) simultaneously in a live enterprise ontology context. The integrated model is a synthesis of evidence from separate research traditions.
- The modularity Q threshold (~0.3) is a heuristic from network science; its applicability to sparse enterprise ontology graphs (which often have different degree distributions than social networks) is not confirmed.
- The failure cascade sequence (H4) is a logical inference, not an observation from longitudinal enterprise data. An alternative ordering (duplication first, then fragmentation) is possible if teams create redundant vocabulary before the graph structure shows the split.
- The Hawkins (2004) attractor framing depends on claims about hierarchical cortical memory that remain contested in neuroscience; its extension to organizational domains is doubly inferential.
- External regulatory pressure can override internally emergent domain boundaries, creating a governance-alignment failure not captured by the Coase/Williamson cost-minimization model.

**Open questions:**

1. What is the minimum Q value that makes a candidate enterprise domain governable as a distinct unit? Does this vary by domain size or concept type?
2. Can the failure cascade (H4) be confirmed from historical ontology version histories in publicly documented enterprise knowledge graph projects?
3. How does regulatory-imposed terminology interact with internally emergent domain boundaries in sectors like financial reporting or healthcare interoperability?
4. Is distributed cognition (Hutchins 1995) a sufficient theoretical basis for extending PDP attractor dynamics to the organizational level, or does a distinct organizational-level mechanism need to be specified?
5. How do Large Language Models (LLMs), which build semantic representations from statistical co-occurrence, interact with enterprise ontology domain boundaries? Do LLM embeddings reinforce or dissolve emergent domains?

### §7 Recursive Review

```text
review_result: pass
acronym_audit: passed
  - PDP: expanded at first use in §1 B1 ("Parallel Distributed Processing (PDP)")
  - FEP: expanded at first use in §2 B2 ("free-energy principle (FEP)")
  - API: expanded at first use in §1 B3 ("Application Programming Interface (API)")
  - Q: defined at §2 A1 as "modularity quality function Q"
  - EKG: expanded at §5 regulatory lens ("Enterprise Knowledge Graphs (EKGs)")
  - LLM: expanded in Open Questions ("Large Language Models (LLMs)")
  - skos/owl: these are namespace prefixes used in one example in §2.D; retained as
    technical identifiers rather than acronyms requiring expansion
claim_label_audit: all claims in §2-§6 carry [fact], [inference], or [assumption] labels
parity_check: §6 synthesis content mirrored into Findings section below
scope_check: no claims about specific enterprise platforms, production implementations,
  or neuroscience experiments; all hypotheses explicitly labeled as testable predictions
self_reference_check: no self-referential citations; §0 workflow notes written as metadata
domain_term_audit:
  - "attractor dynamics" / "attractor basin": defined at B1 first use via Rumelhart context
  - "modularity Q": defined at A1 with equation reference
  - "betweenness centrality": defined at A3 ("the fraction of shortest paths passing through a node")
  - "small-world network": defined at A4 via Watts-Strogatz citation
  - "Markov blanket": defined at B2 ("a statistical boundary separating the system from its environment")
  - "distributed ownership alignment": defined at C3 ("where the semantic boundary, governance responsibility, and communication flow coincide")
  - "syntactic/semantic/pragmatic boundary": defined at C3 via Carlile (2004)
  - "internal-to-external edge ratio": defined at A4
em_dash_check: passed (no em-dashes present)
ai_slop_check: passed (no "Furthermore", "Additionally", "It is important to note", etc.)
vague_quantifier_check: passed (all quantitative claims cite sources or are labeled [inference])
```

---

## Findings

### Executive Summary

Domain boundaries in enterprise ontology and organizational knowledge systems are emergent outcomes of three mutually reinforcing mechanisms: semantic graph density exceeding a community-detection threshold, attractor-like concept co-activation creating cognitive stabilization basins, and governance structures that minimize cross-domain coordination costs. [inference; source: https://www.pnas.org/doi/10.1073/pnas.0601602103; https://www.nature.com/articles/nrn2787; https://www.jstor.org/stable/2778934] The free-energy principle of Friston (2010) provides a formal framing: organizations minimize prediction error by maintaining stable domain models, and boundary instability corresponds to a measurable rise in coordination overhead that functions as organizational-level "surprise." [inference; source: https://www.nature.com/articles/nrn2787; https://onlinelibrary.wiley.com/doi/10.1111/j.1468-0335.1937.tb00002.x] Conway's Law establishes that communication structure and system structure are interdependent, so stable domains require simultaneous alignment among semantic, ownership, and communication boundaries. [fact; source: https://www.melconway.com/Home/Conways_Law.html] The three primary failure signatures of domain breakdown are conceptual fragmentation, concept duplication, and translation-layer proliferation; each is measurable from enterprise metadata without requiring new instrumentation, and four falsifiable hypotheses linking these signatures to the underlying mechanisms are specified. [inference; source: https://doi.org/10.1287/orsc.1040.0094; https://www.pnas.org/doi/10.1073/pnas.0601602103]

### Key Findings

1. **Dense semantic networks with modularity Q above 0.3 exhibit stable community structures that serve as measurable domain boundaries in enterprise ontology graphs, making the modularity quality function the primary graph-level diagnostic for domain emergence.** ([inference]; medium confidence; source: https://www.pnas.org/doi/10.1073/pnas.0601602103)

2. **Small-world network properties of high local clustering combined with short average path lengths, as described by Watts and Strogatz (1998), characterize healthy enterprise knowledge graphs, and domain boundaries emerge as the sparse bridge edges separating high-clustering regions.** ([inference]; medium confidence; source: https://www.nature.com/articles/30918; https://www.pnas.org/doi/10.1073/pnas.0601602103)

3. **Repeated concept co-activation in Parallel Distributed Processing (PDP) systems creates attractor-like stable states that map to domain boundaries when co-activation patterns are analyzed over enterprise artifacts such as schema field co-occurrence, Application Programming Interface (API) dependency clusters, and workflow participation matrices.** ([inference]; medium confidence; source: https://mitpress.mit.edu/9780262680530/parallel-distributed-processing-volume-1/)

4. **Friston's free-energy principle predicts that any system maintaining a boundary with its environment will act to minimize prediction error, providing a formal framing for why organizational domain boundaries stabilize around areas of high mutual predictability among concepts and destabilize when prediction error at the boundary rises.** ([inference]; medium confidence; source: https://www.nature.com/articles/nrn2787; https://davidamitchell.github.io/Research/research/2026-02-28-free-energy-entropy-and-life.html)

5. **Conway's Law, that system design mirrors organizational communication structure, implies that stable semantic domains require alignment among semantic boundaries, ownership boundaries, and communication flow boundaries; misalignment between any two of these three is a leading observable cause of domain incoherence in enterprise knowledge systems.** ([inference]; medium confidence; source: https://www.melconway.com/Home/Conways_Law.html; https://doi.org/10.1287/orsc.1040.0094)

6. **Coase and Williamson's transaction-cost framework establishes that organizational boundaries form where the cost of internal coordination exceeds the cost of maintaining an explicit external interface; applied to semantic domains, this predicts that domain boundary stability is an equilibrium determined by cross-domain coupling costs rather than by top-down design choices alone.** ([inference]; medium confidence; source: https://onlinelibrary.wiley.com/doi/10.1111/j.1468-0335.1937.tb00002.x; https://www.jstor.org/stable/2778934)

7. **Three observable failure signatures indicate domain boundary breakdown in enterprise ontology systems: conceptual fragmentation producing orphaned bridge nodes without domain assignment, concept duplication arising from parallel vocabulary development in disjoint subgraphs, and translation-layer proliferation reflecting governance substitution for shared semantic ownership.** ([inference]; medium confidence; source: https://doi.org/10.1287/orsc.1040.0094; https://www.melconway.com/Home/Conways_Law.html; https://www.pnas.org/doi/10.1073/pnas.0601602103)

8. **Distributed ownership alignment, defined as the co-location of semantic boundary, governance responsibility, and primary communication flow for a knowledge domain, is a stronger predictor of domain persistence than structural graph density alone because governance misalignment enables semantic drift even in initially dense, high-Q subgraphs.** ([inference]; medium confidence; source: https://www.jstor.org/stable/2778934; https://doi.org/10.1287/orsc.1040.0094; https://www.melconway.com/Home/Conways_Law.html)

9. **The three failure mechanisms form a hypothesized cascade sequence: conceptual fragmentation precedes concept duplication, which precedes translation-layer proliferation, providing a detection ordering that can be tested from enterprise ontology version history and integration middleware rule counts.** ([inference]; low confidence; source: https://doi.org/10.1287/orsc.1040.0094; https://www.pnas.org/doi/10.1073/pnas.0601602103)

10. **Domains that lack a coherent conceptual center, defined as a cluster of core concepts with high mutual co-activation frequency in operational artifacts, fail to form stable attractor basins regardless of governance intervention, establishing conceptual coherence as a necessary pre-condition for domain persistence independent of ownership structure.** ([inference]; low confidence; source: https://www.panmacmillan.com/authors/jeff-hawkins/on-intelligence/9780805074567; https://mitpress.mit.edu/9780262680530/parallel-distributed-processing-volume-1/)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Modularity Q > 0.3 indicates stable community structure in semantic graphs | https://www.pnas.org/doi/10.1073/pnas.0601602103 | medium | Q threshold is a field norm from network science; exact value may vary by graph type |
| [inference] Small-world properties characterize healthy enterprise knowledge graphs | https://www.nature.com/articles/30918; https://www.pnas.org/doi/10.1073/pnas.0601602103 | medium | Established for social and information networks; enterprise extension is an inference |
| [inference] PDP co-activation patterns produce attractor-like domain boundaries in enterprise artifacts | https://mitpress.mit.edu/9780262680530/parallel-distributed-processing-volume-1/ | medium | Cognitive analogy; not empirically tested in enterprise ontology contexts |
| [inference] Free-energy principle predicts domain boundary stabilization around mutual predictability | https://www.nature.com/articles/nrn2787; https://davidamitchell.github.io/Research/research/2026-02-28-free-energy-entropy-and-life.html | medium | FEP is a formal theory; enterprise analogy is an inference bridge |
| [inference] Conway's Law implies semantic-ownership-communication boundary alignment requirement | https://www.melconway.com/Home/Conways_Law.html; https://doi.org/10.1287/orsc.1040.0094 | medium | Conway established empirically in software; Carlile provides the boundary-type decomposition |
| [inference] Transaction-cost equilibrium predicts domain boundary location | https://onlinelibrary.wiley.com/doi/10.1111/j.1468-0335.1937.tb00002.x; https://www.jstor.org/stable/2778934 | medium | Economic theory applied by inference to semantic domain boundaries |
| [inference] Three failure signatures: fragmentation, duplication, translation-layer growth | https://doi.org/10.1287/orsc.1040.0094; https://www.melconway.com/Home/Conways_Law.html; https://www.pnas.org/doi/10.1073/pnas.0601602103 | medium | Synthesized from three independent bodies of evidence; not named as a set in any single source |
| [inference] Distributed ownership alignment stronger predictor than graph density alone | https://www.jstor.org/stable/2778934; https://doi.org/10.1287/orsc.1040.0094; https://www.melconway.com/Home/Conways_Law.html | medium | No single study measures all three alignment dimensions simultaneously |
| [inference] Failure cascade: fragmentation precedes duplication precedes translation overhead | https://doi.org/10.1287/orsc.1040.0094; https://www.pnas.org/doi/10.1073/pnas.0601602103 | low | Logical ordering derived from mechanism dependencies; no longitudinal study confirms sequence |
| [inference] Conceptual coherence is a necessary pre-condition for stable attractor basin | https://www.panmacmillan.com/authors/jeff-hawkins/on-intelligence/9780805074567; https://mitpress.mit.edu/9780262680530/parallel-distributed-processing-volume-1/ | low | Extension of Hawkins and Rumelhart by analogy; doubly inferential |

### Assumptions

- **Assumption:** Enterprise metadata systems record co-occurrence patterns in sufficient granularity to operationalize the proposed proxy metrics. **Justification:** Large-scale enterprises routinely operate schema registries, API gateway logging, and integration platform rule counts as standard operational tooling; the assumption is that these records exist and are accessible for analysis. [assumption; source: https://davidamitchell.github.io/Research/research/2026-05-12-data-product-ontology.html]

- **Assumption:** The cognitive attractor framing from Rumelhart and McClelland (1986) applies meaningfully to organizational knowledge rather than only to individual neural memory. **Justification:** Distributed cognition theory establishes that cognitive phenomena can be realized across networks of people and artifacts; this item treats the enterprise metadata graph as the substrate for distributed co-activation without requiring individual neural mechanisms. [assumption; source: https://mitpress.mit.edu/9780262680530/parallel-distributed-processing-volume-1/]

- **Assumption:** The modularity Q threshold of approximately 0.3 is a valid practical heuristic for the "stable domain" diagnostic in enterprise graphs. **Justification:** Newman (2006) observes that real-world networks with meaningful community structure typically achieve Q > 0.3; the exact threshold varies with graph size and density and should be calibrated empirically for a given enterprise context. [assumption; source: https://www.pnas.org/doi/10.1073/pnas.0601602103]

### Analysis

Three independent research traditions converge on the same structural prediction: stable domains form where internal coupling is high and external coupling is low, whether measured by graph modularity, cognitive co-activation depth, or organizational coordination-cost differentials. [inference; source: https://www.pnas.org/doi/10.1073/pnas.0601602103; https://www.nature.com/articles/nrn2787; https://www.jstor.org/stable/2778934] The convergence across network science (Newman 2006, Watts and Strogatz 1998), cognitive neuroscience (Friston 2010, Rumelhart and McClelland 1986), and organizational economics (Coase 1937, Williamson 1981, Conway 1968) increases confidence that the integrated model captures a genuine phenomenon even without a single cross-tradition empirical study. [inference; source: https://www.pnas.org/doi/10.1073/pnas.0601602103; https://www.nature.com/articles/nrn2787; https://onlinelibrary.wiley.com/doi/10.1111/j.1468-0335.1937.tb00002.x]

The governance mechanism is the most directly actionable of the three: graph topology and cognitive stabilization are outcomes that can be measured but not directly controlled, while ownership assignment, approval depth reduction, and team charter consolidation are controllable governance inputs. [inference; source: https://www.jstor.org/stable/2778934; https://doi.org/10.1287/orsc.1040.0094] The economic framing (Coase, Williamson) is most useful for predicting where natural boundaries should form; the Conway framing is most useful for diagnosing why existing boundaries have degraded. [inference; source: https://onlinelibrary.wiley.com/doi/10.1111/j.1468-0335.1937.tb00002.x; https://www.melconway.com/Home/Conways_Law.html]

The FEP framing contributes a falsifiability dimension: if a domain is in good health, cross-domain interactions should have measurably higher prediction error (more exceptions, more reconciliation, more escalation) than same-domain interactions; if this prediction fails, the FEP framing is inapplicable to this domain. [inference; source: https://www.nature.com/articles/nrn2787]

A rival explanation holds that domain boundaries are purely products of deliberate design rather than emergent outcomes. This view predicts stable domains wherever design intent is strong, which is undermined by the widespread observation of domain decay in well-governed enterprises that have applied top-down ontology design without governance alignment. [inference; source: https://www.melconway.com/Home/Conways_Law.html; https://doi.org/10.1287/orsc.1040.0094] The cascade hypothesis (H4), that fragmentation precedes duplication, which precedes translation-layer growth, is also a causal claim: reducing Q decline in its earliest detectable stage should prevent downstream duplication and translation overhead, making early Q monitoring the highest-leverage intervention point for domain maintenance. [inference; source: https://www.pnas.org/doi/10.1073/pnas.0601602103; https://doi.org/10.1287/orsc.1040.0094]

### Risks, Gaps, and Uncertainties

- No single empirical study has measured all three mechanisms simultaneously in a live enterprise ontology context; the integrated model is a synthesis of evidence from separate research traditions, each supporting its own mechanism in isolation.
- The modularity Q threshold of approximately 0.3 is a heuristic from network science studies of social and biological networks; its applicability to sparse enterprise ontology graphs with different degree distributions is unconfirmed.
- The failure cascade sequence (H4) is a logical inference, not an observation from longitudinal enterprise data; an alternative ordering where concept duplication precedes structural fragmentation is possible if teams create redundant vocabulary before the graph topology reflects the split.
- The Hawkins (2004) attractor framing draws on claims about hierarchical cortical memory that remain debated in neuroscience; its extension to organizational domains is doubly inferential.
- External regulatory pressure can impose semantic definitions that override internally emergent domain boundaries, creating governance-alignment failures not captured by the Coase-Williamson cost-minimization model.
- The proxy metrics proposed (API dependency graphs, schema co-occurrence, workflow participation matrices) require operational data that may not be accessible or well-structured in all enterprise contexts.

### Open Questions

1. What is the minimum modularity Q value that makes a candidate enterprise domain governable as a distinct unit? Does this threshold vary by domain size or concept type?
2. Can the failure cascade sequence (H4) be confirmed from historical ontology version histories in publicly documented enterprise knowledge graph projects?
3. How does regulatory-imposed terminology interact with internally emergent domain boundaries in sectors such as financial reporting or healthcare interoperability?
4. Is distributed cognition theory (Hutchins 1995) a sufficient theoretical basis for extending PDP attractor dynamics to the organizational level, or does a distinct organizational-level mechanism need to be specified?
5. How do Large Language Models (LLMs), which build semantic representations from statistical co-occurrence, interact with enterprise ontology domain boundaries? Do LLM embedding spaces reinforce or dissolve emergent domain structure?

---

## Output

- Type: knowledge
- Description: An integrated explanatory model for how domain boundaries emerge and persist in enterprise ontology and organizational knowledge systems, combining graph modularity theory, cognitive attractor dynamics, and transaction-cost governance. Identifies three observable failure signatures and four falsifiable testable hypotheses. [inference; source: https://www.pnas.org/doi/10.1073/pnas.0601602103; https://doi.org/10.1287/orsc.1040.0094; https://www.nature.com/articles/nrn2787]
- Links:
  - https://www.pnas.org/doi/10.1073/pnas.0601602103 (Newman 2006: modularity and community structure)
  - https://doi.org/10.1287/orsc.1040.0094 (Carlile 2004: knowledge boundary typology)
  - https://www.nature.com/articles/nrn2787 (Friston 2010: free-energy principle)
