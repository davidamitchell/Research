---
title: "Dependency properties and coordination mechanisms over time"
added: 2026-10-23T09:20:04+00:00
status: backlog
priority: medium
blocks: []
themes: [organisational-design, software-engineering, governance-policy, enterprise-adoption, cost-performance]
started: ~
completed: ~
output: []
cites: []
related:
  - 2026-06-13-platform-engineering-innersource-hybrid-standardization
  - 2026-06-13-local-tooling-fragmentation-threshold-measurement
  - 2026-06-13-local-global-optima-knowledge-work-throughput
  - 2026-06-13-standardization-customization-balance-context-ai
  - 2026-06-13-shadow-it-custom-tooling-governance-transition
  - 2026-05-29-split-authority-q4-decision-rights-placement
  - 2026-05-29-split-authority-q1-flow-constraint
  - 2026-05-19-align-strategic-relevance-with-low-effort-knowledge-pathways
  - 2026-03-12-team-size-limits-brooks-dunbar-network-theory
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Dependency properties and coordination mechanisms over time

## Research Question

When many units of work each need a specialist team to do something for them (for example, many product teams each needing a new rule written by a specialist rules team), which properties of that dependency are most predictive of the coordination mechanism that works best, and how should the mechanism change as the dependency's properties change over time? Are any sets of properties strong enough to prescribe the mechanism without further organisational context, and does the answer transfer from teams to software components and to governed decisions?

## Scope

**In scope:**
- The dependency "unit A needs unit B to do work for it" as the unit of analysis, including recurring demand from many units on one specialist unit. This is a dependency on another unit's capacity and priorities, not on a flow of material such as a late data feed.
- Candidate properties of the dependency: recurrence (how often this type of request arrives and from how many units), uncertainty (how well the work can be specified up front), cost of a wrong outcome, required speed, and required certainty of the outcome. The literature may add, merge or drop properties. Cost of a wrong outcome and required certainty describe what sits at the end of the dependency, not the link itself; treat them as a separate group and say so in the findings.
- Candidate mechanisms, including mechanisms that manage the dependency and mechanisms that reshape or remove it:
  - Managing: queue on the specialist unit's backlog; a specialist embedded in each requesting unit; lateral coordination among the embedded specialists (guild, community of practice, liaison roles); a shared decision gate; vertical review through a central function.
  - Reshaping: self-service with guardrails; templates or golden paths; moving decision rights to the requesting units with after-the-fact audit; platform or abstraction layer that commoditises the specialist service.
- The central trade-off: duplication (each embedded specialist solves problems independently, fast, with local knowledge) versus synchronisation (specialists align solutions and extract common patterns, slower, more consistent). Treat it as a dial and ask what sets it.
- Three distinct costs of moving the dial towards synchronisation, to be kept separate:
  1. Time spent synchronising (meetings, alignment, liaison effort).
  2. Convergence cost: rework needed to bring already-divergent implementations into line, which grows with how long units ran duplicated.
  3. Rollout cost: effort and lost delivery capacity when a general solution is adopted across many units, including the problem of identifying which local solution is the general one.
- Time: a regime in which the work must be done now, at volume, with low delivery risk, and there is no time to build or experiment with a shared platform first. Ask whether duplicating first and converging later is a recognised pattern, what it costs, and what conditions make it sound.
- Transfer: whether the same properties predict the mechanism for dependencies between software components (a service needing another service to expose a capability) and between governed decisions. A dependency between two decisions means one decision's output is another's input, or both constrain the same resource or outcome.
- Definitions. "Predictive" means a property reliably shifts which mechanism works best. "Prescribes" means the properties alone determine the mechanism with no further information about the particular organisation.

**Out of scope:**
- Discovering or measuring dependencies in an existing system.
- Restructuring an existing organisation or migrating an existing architecture.
- Dependencies on a flow of material (late feeds, delivery timing), except as contrast.
- Tooling or code for this repository.

**Constraints:** Peer-reviewed or primary sources for theory claims. Practitioner sources (for example Team Topologies, platform engineering reports) are admissible as evidence of practice and must be labelled as such. Properties that predict without prescribing, layers that diverge, and findings that a claimed cost has not been measured are all valid outcomes. The item succeeds if it reports where and why. Do not present an unsupported claim as supported; label it as a gap.

## Context

Galbraith (1974) frames organisation design as a choice among strategies for handling task uncertainty: slack resources, self-contained tasks, vertical information systems, and lateral relations, with the choice made on relative cost. Self-contained tasks buy speed by duplicating resources and losing specialisation. Lateral relations add processing capacity at the cost of managerial effort. This item takes the dependency as the primitive and asks how its properties select among the mechanisms, including mechanisms that reshape the dependency rather than manage it.

A first reading of the seed papers found support for the organisation-level trade-off but not for four things this item cares about: that time pressure sets the dial, convergence cost, rollout cost, and the sequence "duplicate now, converge later". Galbraith treats required performance level as a design variable, and Malone and Crowston note that failure rates may be a primary design consideration, so required certainty has partial support. The existing repository items support a qualitative case that duplicated local solutions accrue cost over time and that governance-infrastructure standardisation rises with regulatory exposure, but none quantifies convergence or rollout cost. The research therefore has to look beyond the seed.

## Approach

1. Which dependency properties does the literature treat as decisive for choosing a coordination mechanism, and where do authors conflict? Compare Thompson's interdependence types, Lawrence and Lorsch's differentiation and integration, Van de Ven, Delbecq and Koenig's coordination modes, Malone and Crowston's dependency taxonomy, Tushman and Nadler, and Galbraith's strategies. Produce a table of property sets by author and a candidate merged set. Read primary text where available and record where only a secondary source was accessible. The issue supplied no verified URL for March and Simon (1958); locate a source before relying on that work.
2. What does the evidence say about the duplication versus synchronisation trade-off? For each claim, record whether any source measures or only asserts it: that synchronisation reduces throughput, that required certainty pushes towards synchronisation, that time pressure pushes towards duplication, and that the relationship is non-linear (cheap shared templates versus heavy alignment).
3. Convergence cost: what is known about the cost of reconciling independently developed solutions after the fact (technical debt from duplication, consolidation and standardisation programmes, inner source adoption, merger integration of overlapping systems)? Is there any quantification, and what drives it?
4. Rollout cost: what is known about the cost of adopting a general solution across many teams (diffusion of practices, platform adoption, mandate versus voluntary adoption, migration programmes), and how are teams identified as having the general solution?
5. Sequencing: is there evidence for or against starting with embedded, duplicated specialists and converging later, and for moving from one mechanism to the next as recurrence rises and uncertainty falls? Include maturity models and staged-governance models, and state what each assumes.
6. Do the findings transfer to software components and governed decisions? Test against the architecture literature (Parnas, Simon, Sanchez and Mahoney, Henderson and Clark, Sosa and colleagues) and the governance items in this repository. State for each layer whether the same properties predict the mechanism, with failure cases, and whether managing a dependency at one layer changes the mechanism needed at an adjacent layer (Conway, Colfer and Baldwin, Cataldo and colleagues, Skelton and Pais).
7. Answer with a candidate property set; a mapping from properties to mechanisms and to mechanism changes over time; the evidence grade for each link in the mapping; and an explicit list of claims that remain hypotheses.

**Search plan:** Start from the seed below, then go wider. Follow forward and backward citations from each seed paper; search for work after 2016, including empirical studies in software engineering, platform engineering and governance; search for critiques and contrary evidence, including critiques of contingency theory and the mirroring hypothesis; search outside management and software, including systems engineering, operations research, and the economics of standardisation; and target the gaps named in Context: convergence cost, rollout cost, required certainty, and duplicate-then-converge sequencing. Record why each source added beyond the seed was selected.

**Read these primary repository items before external searching, and cite those that bear on a claim:**
- `2026-06-13-platform-engineering-innersource-hybrid-standardization`
- `2026-06-13-local-tooling-fragmentation-threshold-measurement`
- `2026-06-13-local-global-optima-knowledge-work-throughput`
- `2026-06-13-standardization-customization-balance-context-ai`
- `2026-06-13-shadow-it-custom-tooling-governance-transition`
- `2026-05-29-split-authority-q4-decision-rights-placement`
- `2026-05-29-split-authority-q1-flow-constraint`
- `2026-05-19-align-strategic-relevance-with-low-effort-knowledge-pathways` (covers Galbraith 1974)
- `2026-03-12-team-size-limits-brooks-dunbar-network-theory`

**Consult if relevant:**
- `2026-05-29-split-authority-q3-routing-exception-isolation`
- `2026-05-29-split-authority-q5-control-model-tradeoff`
- `2026-05-29-split-authority-p1-operating-model-synthesis`
- `2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance`
- `2026-05-23-governance-controls-effectiveness-conditions`
- `2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention`
- `2026-05-19-how-do-formal-governance-structures-distort-cross-department-knowledge-flows`
- `2026-08-17-decision-governance`
- `2026-08-17-cohesive-coherent-organisational-governance`
- `2026-05-23-funding-authority-delivery-capability-risk-accountability-split`
- `2026-05-14-org-failure-modes-split-risk-cost-benefits-accountability`
- `2026-05-14-org-failure-modes-project-demand-product-it`
- `2026-05-14-org-failure-modes-cohort-demand-domain-it`
- `2026-05-14-org-failure-modes-accountability-gaps`
- `2026-08-20-three-zone-interface-feedback-constraints`
- `2026-09-14-modern-technology-platform-taxonomy`
- `2026-10-01-thinnest-viable-internal-platform-standard`
- `2026-10-02-ideal-internal-platform-product-standard`
- `2026-05-21-monolith-vs-cohesive-portfolio-tco`
- `2026-03-12-ai-team-size-strike-team-thesis`
- `2026-05-31-sre-slo-threshold-justification`
- `2026-05-31-formal-methods-interdependent-inputs-feasibility`

## Sources

Seed list. These were supplied as the starting set, not as a boundary on the search. Verify claims against the original where only a bibliographic, abstract, or secondary page is available.

- [Galbraith (1974) Organization Design: An Information Processing View](https://ideas.repec.org/a/inm/orinte/v4y1974i3p28-36.html): framing paper; cost-based choice among four strategies.
- [Thompson (1967) Organizations in Action](https://sk.sagepub.com/ency/edvol/embed/encyclopedia-of-management-theory/chpt/technology-interdependence-uncertainty): pooled, sequential, and reciprocal interdependence; secondary page.
- [Lawrence and Lorsch (1967) Organization and Environment](https://en.wikiquote.org/wiki/Paul_R._Lawrence): bibliographic pointer; secondary page.
- [Lawrence and Lorsch (1967) Differentiation and Integration in Complex Organizations](https://www.talkingaboutorganizations.com/e16/): secondary page.
- [Van de Ven, Delbecq, and Koenig (1976) Determinants of Coordination Modes within Organizations](https://pubsonline.informs.org/doi/references/10.1287/mnsc.1060.0526): reference listing; primary text not yet read.
- [Malone and Crowston (1994) The Interdisciplinary Study of Coordination](https://genres.syr.edu/sites/default/files/acmcs94.pdf): dependency types mapped to coordination processes; Association for Computing Machinery (ACM) Computing Surveys.
- [Tushman and Nadler (1978) Information Processing as an Integrating Concept in Organizational Design](https://www.jstor.org/stable/257550): information-processing account of organisational design.
- [Burns and Stalker (1961) The Management of Innovation](<https://en.wikipedia.org/wiki/Tom_Burns_(sociologist)>): bibliographic page only.
- [Duncan (1972) Characteristics of Organizational Environments and Perceived Environmental Uncertainty](https://rasch.org/rmt/rmt194.pdf): secondary page.
- [Mintzberg (1979) The Structuring of Organizations](https://ci.nii.ac.jp/ncid/BA01136657): catalogue record only.
- [Simon (1962) The Architecture of Complexity](https://www.sfipress.org/21-simon-1962): complexity and system decomposition.
- [Parnas (1972) On the Criteria To Be Used in Decomposing Systems into Modules](https://experts.mcmaster.ca/scholarly-works/2169027): software modularity criteria.
- [Conway (1968) How Do Committees Invent?](https://blog.acolyer.org/2019/12/13/how-do-committees-invent/): secondary page.
- [Sanchez and Mahoney (1996) Modularity, Flexibility, and Knowledge Management in Product and Organization Design](https://experts.illinois.edu/en/publications/modularity-flexibility-and-knowledge-management-in-product-and-or/): abstract page.
- [Henderson and Clark (1990) Architectural Innovation](https://dash.harvard.edu/entities/publication/3affcf33-4dea-4371-ab4c-4767380018ab): publication record.
- [Sosa, Eppinger, and Rowles (2004) The Misalignment of Product Architecture and Organizational Structure in Complex Product Development](https://pubsonline.informs.org/doi/fpi/10.1287/mnsc.1040.0289): publication record.
- [Colfer and Baldwin (2016) The Mirroring Hypothesis: Theory, Evidence, and Exceptions](https://dash.harvard.edu/entities/publication/73120379-10f0-6bd4-e053-0100007fdf3b): publication record; not yet read.
- [Cataldo, Wagstrom, Herbsleb, and Carley (2006) Identification of Coordination Requirements](https://doi.org/10.1145/1180875.1180929): coordination requirements; Computer-Supported Cooperative Work (CSCW) 2006.
- [Skelton and Pais (2019) Team Topologies](https://devops.com/it-revolution-announces-new-book-team-topologies-organizing-business-and-technology-teams-for-fast-flow/): practitioner source; announcement page.

## Related

- [Platform engineering and shared/local standardisation](https://davidamitchell.github.io/Research/research/2026-06-13-platform-engineering-innersource-hybrid-standardization.html)
- [Measuring the fragmentation threshold for local tooling](https://davidamitchell.github.io/Research/research/2026-06-13-local-tooling-fragmentation-threshold-measurement.html)
- [Galbraith's information-processing design framing](https://davidamitchell.github.io/Research/research/2026-05-19-align-strategic-relevance-with-low-effort-knowledge-pathways.html)

## Readiness

**READY.** The question passes the specificity, answerability, scope, motivation, and decomposition tests. It identifies the dependency unit and comparative mechanisms, defines evidence-based criteria for answering, bounds the domains and sources, states the design problem it informs, and decomposes the work into seven investigations. This is an intake assessment only; no research has been conducted.

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0–5 cover the investigation; section 6 seeds the Findings section below.)*

### §0 Initialise

Restate the research question. Confirm scope, constraints, and output format.

-

### §1 Question Decomposition

Approach sub-questions broken into atomic questions. Each is answerable with a single evidence-based claim.

-

### §2 Investigation

Evidence gathered per atomic question. Label each claim: **[fact]**, **[inference]**, or **[assumption]** with source.

-

### §3 Reasoning

Facts, inferences, and assumptions explicitly separated. No unsupported generalisations or narrative leaps.

-

### §4 Consistency Check

Internal contradictions identified and resolved (or explicitly flagged where unresolvable).

-

### §5 Depth and Breadth Expansion

Findings re-examined through relevant lenses (technical, regulatory, economic, historical, behavioural).

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

Final pass: every section justified, all threads synthesised, every claim sourced or labelled, all uncertainties explicit.

-

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

3–5 sentences. What is the answer to the research question? State the key conclusion directly. Write plain prose without prefix labels. Bind sources as trailing inline citations: `Claim text. [inference; source: https://url]`

### Key Findings

Ordered list. Each finding is a specific, evidence-backed claim with confidence and source as a trailing parenthetical. Use **suffix style** and put the source at the end of the claim.

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

*(Fill in when completing: what was produced as a result of this research?)*

- Type: # skill | tool | agent | knowledge | backlog-item
- Description:
- Links:
