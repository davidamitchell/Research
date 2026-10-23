---
review_count: 1
title: "Dependency properties and coordination mechanisms over time"
added: 2026-10-23T09:20:04+00:00
status: reviewing
priority: medium
blocks: []
themes: [organisational-design, software-engineering, governance-policy, enterprise-adoption, cost-performance]
started: 2026-10-23T09:36:03+00:00
completed: ~
output: []
cites:
  - 2026-06-13-platform-engineering-innersource-hybrid-standardization
  - 2026-06-13-local-tooling-fragmentation-threshold-measurement
  - 2026-06-13-local-global-optima-knowledge-work-throughput
  - 2026-06-13-standardization-customization-balance-context-ai
  - 2026-06-13-shadow-it-custom-tooling-governance-transition
  - 2026-05-29-split-authority-q4-decision-rights-placement
  - 2026-05-29-split-authority-q1-flow-constraint
  - 2026-05-19-align-strategic-relevance-with-low-effort-knowledge-pathways
  - 2026-03-12-team-size-limits-brooks-dunbar-network-theory
related: []
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

Sources added during research:

- [Kruger and Berger (2020) An Empirical Analysis of the Costs of Clone- and Platform-Oriented Software Reuse](https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf): interviews and literature review on reuse costs; selected for convergence-cost evidence.
- [Kapser and Godfrey (2008) Cloning Considered Harmful Considered Harmful: Patterns of Cloning in Software](https://plg.uwaterloo.ca/~migod/papers/2008/emse08-ClonePatterns.pdf): forking and cloning patterns; selected as counter-evidence on duplication.
- [Capraro and Riehle (2016) Inner Source Definition, Benefits, and Challenges](https://dirkriehle.com/wp-content/uploads/2016/12/capraro-riehle-inner-source-definition-benefits-challenges-survey.pdf): survey of inner source; selected for rollout evidence.
- [Staw, Sandelands, and Dutton (1981) Threat-Rigidity Effects in Organizational Behavior](https://eric.ed.gov/?id=EJ255060): selected as rival to the time-pressure hypothesis.
- [Schoonhoven (1981) Problems with Contingency Theory](https://eric.ed.gov/?id=EJ251028): selected as critique of contingency theory.
- [Metz (2016) The Wrong Abstraction](https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction): practitioner opinion on duplication versus abstraction.
- [Team Topologies Key Concepts](https://teamtopologies.com/key-concepts): practitioner source replacing the inaccessible announcement page.
- [DevOps Research and Assessment (DORA) Loosely Coupled Teams](https://dora.dev/capabilities/loosely-coupled-teams/): practitioner research capability page.
- [Van de Ven, Delbecq, and Koenig (1976) Determinants of Coordination Modes within Organizations](https://www.jstor.org/stable/2094477): journal record; secondary summary only was read.
- [March and Simon (1958) Organizations](https://books.google.com/books/about/Organizations.html?id=FbBJEAAAQBAJ): catalogue record only; no claim relies on it.
- [Colfer and Baldwin (2016) The Mirroring Hypothesis working paper](https://www.hbs.edu/ris/download.aspx?name=16-124.pdf): readable copy of the review.
- [Cataldo et al. (2006) Identification of Coordination Requirements](https://patrick.wagstrom.net/publications/Cataldo_2006_IdentificationOfCoordinationRequirements.pdf): readable copy of the paper.
- [Repository item: standardisation and customisation balance](https://davidamitchell.github.io/Research/research/2026-06-13-standardization-customization-balance-context-ai.html): prior completed item.
- [Repository item: local and global optima in knowledge-work throughput](https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html): prior completed item.
- [Repository item: shadow tooling governance transition](https://davidamitchell.github.io/Research/research/2026-06-13-shadow-it-custom-tooling-governance-transition.html): prior completed item.
- [Repository item: split authority decision rights placement](https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q4-decision-rights-placement.html): prior completed item.
- [Repository item: split authority flow constraint](https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q1-flow-constraint.html): prior completed item.
- [Repository item: team size limits and network theory](https://davidamitchell.github.io/Research/research/2026-03-12-team-size-limits-brooks-dunbar-network-theory.html): prior completed item.
- [Repository item: decision governance](https://davidamitchell.github.io/Research/research/2026-08-17-decision-governance.html): prior completed item cited in open questions.

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

Restated question: which properties of the dependency "unit A needs specialist unit B to do work for it" predict the best coordination mechanism, how should the mechanism change over time, do any property sets prescribe the mechanism, and does the answer transfer to software components and governed decisions. The unit of analysis is a dependency on another unit's capacity and priorities, not a flow of material. The output type is `knowledge`. Prior-work scan of completed repository items found nine bearing on this question, listed in the frontmatter, and they are cited with URLs in §2.

Working hypotheses, all unverified at the start of the investigation:

- Recurrence and uncertainty are the strongest predictors of mechanism choice. [assumption; source: https://ideas.repec.org/a/inm/orinte/v4y1974i3p28-36.html]
- Required certainty and cost of a wrong outcome push towards synchronisation. [assumption; source: https://genres.syr.edu/sites/default/files/acmcs94.pdf]
- Time pressure pushes towards duplication, and duplicated solutions can be converged later at a cost that grows with the duration of divergence. [assumption; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]

Terms used in this item:

- Inner source means applying open-source development practices to code shared inside one organisation. [fact; source: https://dirkriehle.com/wp-content/uploads/2016/12/capraro-riehle-inner-source-definition-benefits-challenges-survey.pdf]
- A golden path is a supported, pre-built route for a common engineering task that preserves local agility. [fact; source: https://davidamitchell.github.io/Research/research/2026-06-13-platform-engineering-innersource-hybrid-standardization.html]
- Clone and own means copying a component and modifying the copy. [fact; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]
- The mirroring hypothesis is the claim that the structure of a product tends to match the structure of the organisation that builds it. [fact; source: https://www.hbs.edu/ris/download.aspx?name=16-124.pdf]
- DevOps Research and Assessment (DORA) is a research programme whose capability pages describe practices linked to software delivery performance. [fact; source: https://dora.dev/capabilities/loosely-coupled-teams/]

### §1 Question Decomposition

- Q1 Property sets. Which properties does each of Thompson, Lawrence and Lorsch, Van de Ven and colleagues, Malone and Crowston, Galbraith and Tushman and Nadler treat as decisive?
  - Q1a Which sources could be read in primary text, and which only through secondary pages?
  - Q1b Where do authors conflict, and how does contingency theory itself get criticised?
- Q2 Duplication versus synchronisation. Is each of four claims measured or only asserted: synchronisation reduces throughput, required certainty pushes towards synchronisation, time pressure pushes towards duplication, the relationship is non-linear?
- Q3 Convergence cost. Is the cost of reconciling divergent solutions quantified, and what drives it?
- Q4 Rollout cost. Is the cost of adopting a general solution across many teams quantified, and how is the general solution identified?
- Q5 Sequencing. Is duplicate-then-converge a recognised pattern, and under what conditions is it sound?
- Q6 Transfer. Do the same properties predict the mechanism for software components and governed decisions, and does managing a dependency at one layer change the mechanism needed at an adjacent layer?
- Q7 Answer. Candidate property set, property-to-mechanism mapping, evidence grade per link, and a list of hypotheses.

### §2 Investigation

**Q1 Property sets**

Malone and Crowston define coordination as managing dependencies among activities and pair each dependency type with candidate coordination processes. [fact; source: https://genres.syr.edu/sites/default/files/acmcs94.pdf]

Their Table 1 pairs shared resources with first come first served, priority order, budgets, managerial decision and market-like bidding, and pairs task and subtask dependencies with goal selection and decomposition. [fact; source: https://genres.syr.edu/sites/default/files/acmcs94.pdf]

The same paper summarises organisation theory as three interdependence forms (pooled, sequential, reciprocal, attributed to Thompson) and three mechanisms (standardisation, direct supervision, mutual adjustment). [fact; source: https://genres.syr.edu/sites/default/files/acmcs94.pdf]

Thompson's interdependence forms were read only through a short encyclopedia page. [assumption; source: https://sk.sagepub.com/ency/edvol/embed/encyclopedia-of-management-theory/chpt/technology-interdependence-uncertainty]

Galbraith's abstract states that task uncertainty relates to organisational form and that the argument rests on Simon's theory of cognitive limits. [fact; source: https://ideas.repec.org/a/inm/orinte/v4y1974i3p28-36.html]

The four Galbraith strategies are slack resources, self-contained tasks, vertical information systems and lateral relations, as summarised in a prior repository item. [fact; source: https://davidamitchell.github.io/Research/research/2026-05-19-align-strategic-relevance-with-low-effort-knowledge-pathways.html]

That item places slack and self-contained tasks on the demand-reducing side and vertical systems and lateral relations on the capacity-raising side. [fact; source: https://davidamitchell.github.io/Research/research/2026-05-19-align-strategic-relevance-with-low-effort-knowledge-pathways.html]

A secondary search summary, not the article text, describes Van de Ven, Delbecq and Koenig (1976) as finding that task uncertainty, task interdependence and unit size influence the use of impersonal, personal and group coordination modes. [assumption; source: https://www.jstor.org/stable/2094477]

Access note: only a secondary search summary of the Van de Ven abstract was available; the JSTOR page and a mirror failed to load, so the finding is graded as secondary-summary only. [assumption; source: https://www.jstor.org/stable/2094477]

Lawrence and Lorsch's study of six industrial organisations concluded that performance depends on meeting differentiation and integration requirements, as described on a secondary podcast page. [inference; source: https://www.talkingaboutorganizations.com/e16/]

The merged property set implied by these sources is: interdependence form, uncertainty, unit size, recurrence or volume, and for the shared-resource case the number of requesters. [inference; source: https://genres.syr.edu/sites/default/files/acmcs94.pdf; https://www.jstor.org/stable/2094477]

Malone and Crowston add a design consideration at the far end of the dependency, failure rate, noting that failure rates may be the primary design consideration in distributed computer systems. [fact; source: https://genres.syr.edu/sites/default/files/acmcs94.pdf]

Their queueing comparison found that centralised schemes had lower coordination costs but were more vulnerable to processor failures, decentralised markets were less vulnerable but had high coordination costs, and product hierarchies had low coordination costs but unused capacity. [fact; source: https://genres.syr.edu/sites/default/files/acmcs94.pdf]

Cost of a wrong outcome and required certainty are therefore a distinct group of terminus properties with only partial support. [inference; source: https://genres.syr.edu/sites/default/files/acmcs94.pdf]

Schoonhoven reports, from 17 hospitals, that traditional contingency theory underrepresents the complexity of relations among technological uncertainty, structure and effectiveness. [fact; source: https://eric.ed.gov/?id=EJ251028]

That critique implies that any property set predicts a mechanism only conditionally. [inference; source: https://eric.ed.gov/?id=EJ251028]

Access note: Tushman and Nadler, Burns and Stalker, Duncan and Mintzberg were not read in primary text; the seed URLs are bibliographic or catalogue pages. [assumption; source: https://www.jstor.org/stable/257550]

Access note: March and Simon (1958) was located only as a Google Books record, so no claim here relies on it. [assumption; source: https://books.google.com/books/about/Organizations.html?id=FbBJEAAAQBAJ]

**Q2 Duplication versus synchronisation**

Brooks-style overhead of n(n-1)/2 pairwise links bounds the cost of full lateral coordination among embedded specialists. [inference; source: https://davidamitchell.github.io/Research/research/2026-03-12-team-size-limits-brooks-dunbar-network-theory.html]

Conway observed that coordination among task groups lowers individual productivity but is the only way to consolidate efforts into a unified design. [fact; source: https://blog.acolyer.org/2019/12/13/how-do-committees-invent/]

A prior repository item found that individual task completion rose 33.7% while pull request review time rose 441%, so locally fast work can move the constraint downstream. [fact; source: https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html]

Another prior item found that external change approvals correlate negatively with delivery performance and that a 200-engineer value-stream case showed 97% wait time. [fact; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q1-flow-constraint.html]

Together these measure the cost of synchronisation as waiting, but they measure it for approvals and review rather than for specialist-to-requester dependencies. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q1-flow-constraint.html]

The decision-rights item recommends bounded delegation for high-frequency, reversible decisions with bounded blast radius, because centralising them creates approval-queue latency. [fact; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q4-decision-rights-placement.html]

This supports recurrence together with reversibility as predictors, with required certainty acting as the opposing property. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q4-decision-rights-placement.html]

The standardisation item separates governance-infrastructure standardisation, which rises with regulatory exposure, from task-execution standardisation, which rises with platform maturity and scale. [fact; source: https://davidamitchell.github.io/Research/research/2026-06-13-standardization-customization-balance-context-ai.html]

That is the strongest available support for required certainty pushing towards synchronisation, and it is qualitative. [inference; source: https://davidamitchell.github.io/Research/research/2026-06-13-standardization-customization-balance-context-ai.html]

Staw, Sandelands and Dutton report that threat restricts information processing and control, which they call threat-rigidity. [fact; source: https://eric.ed.gov/?id=EJ255060]

Under that account, pressure could push towards centralised control rather than towards duplication, which is the opposite of the working hypothesis. [inference; source: https://eric.ed.gov/?id=EJ255060]

Search log: time pressure and duplicated local solutions, empirical studies; none found.

Search log: quantified non-linearity between shared templates and heavy alignment; none found.

Team Topologies names three interaction modes, collaboration, X-as-a-Service and facilitation, which map onto embedded, queue or platform, and guild-like mechanisms. [inference; source: https://teamtopologies.com/key-concepts]

Team Topologies is practitioner source material, and the access note is that the seed announcement page returned an access error so the key-concepts page replaces it. [assumption; source: https://teamtopologies.com/key-concepts]

DORA reports that loosely coupled teams can change and deploy without outside permission or fine-grained coordination. [fact; source: https://dora.dev/capabilities/loosely-coupled-teams/]

**Q3 Convergence cost**

Krüger and Berger interviewed 26 practitioners at one large organisation and reviewed 57 publications on reuse costs. [fact; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]

They report that clone and own is readily available, flexible and initially cheap but does not scale with the frequency of reuse and carries high maintenance costs. [fact; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]

They report that re-integrating a short-living clone costs considerably less than a long-living one, and that cost depends on co-evolution of the variant and the platform and on the size of the variant's delta. [fact; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]

Their cost numbers rest on only eight cost estimations, four per strategy, so the quantification is thin and single-organisation. [fact; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]

They also report that migration from clone and own is the most common way organisations adopt platforms. [fact; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]

Kapser and Godfrey find that cloning is often a principled engineering tool, and in an Apache and Gnumeric case study as many as 71% of clones could be considered to have a positive impact on maintainability. [fact; source: https://plg.uwaterloo.ca/~migod/papers/2008/emse08-ClonePatterns.pdf]

That result cautions against treating all duplication as debt. [inference; source: https://plg.uwaterloo.ca/~migod/papers/2008/emse08-ClonePatterns.pdf]

The fragmentation-threshold item names three structural multipliers, tool footprint, shared dependency density and turnover, and states that its proxy metrics are inference. [fact; source: https://davidamitchell.github.io/Research/research/2026-06-13-local-tooling-fragmentation-threshold-measurement.html]

The shadow-tooling item establishes the cost of tacit-knowledge concentration only qualitatively. [fact; source: https://davidamitchell.github.io/Research/research/2026-06-13-shadow-it-custom-tooling-governance-transition.html]

Convergence cost therefore has one partly measured driver, duration and delta of divergence, and no cross-organisation measurement. [inference; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]

**Q4 Rollout cost**

Krüger and Berger report that migration requires re-engineering and affects architecture, organisation structure and process. [fact; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]

Their coordination cost medians were similar between strategies, at 5% versus 7%. [fact; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]

Capraro and Riehle surveyed 43 publications and give a model of inner source plus qualitative benefits and challenges of adoption. [fact; source: https://dirkriehle.com/wp-content/uploads/2016/12/capraro-riehle-inner-source-definition-benefits-challenges-survey.pdf]

The platform-engineering item combines golden paths, inner source and a core with local extension, with golden paths preserving local agility. [fact; source: https://davidamitchell.github.io/Research/research/2026-06-13-platform-engineering-innersource-hybrid-standardization.html]

Search log: measured rollout cost of a general solution across many teams, and selection of the general local solution; none found, one query failed with a gateway error.

**Q5 Sequencing**

Duplicate-then-converge is a recognised pattern, because clone and own to platform migration is the most common adoption path and forking patterns include experimental variation with later incremental migration. [inference; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf; https://plg.uwaterloo.ca/~migod/papers/2008/emse08-ClonePatterns.pdf]

Metz argues that duplication is far cheaper than the wrong abstraction, which is practitioner opinion and not measurement. [fact; source: https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction]

Soundness conditions inferred from the evidence are short divergence, small delta, and a way to identify the general solution later. [inference; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]

Cataldo and colleagues found that coordination requirements were highly volatile and often extended beyond team boundaries, and that the most productive developers changed media use over time. [fact; source: https://patrick.wagstrom.net/publications/Cataldo_2006_IdentificationOfCoordinationRequirements.pdf]

Volatility of the dependency is therefore a property that argues for changing mechanism over time. [inference; source: https://patrick.wagstrom.net/publications/Cataldo_2006_IdentificationOfCoordinationRequirements.pdf]

The decision-rights and platform items each treat the move from local to shared as conditioned on recurrence and maturity, but neither tests the sequence empirically. [inference; source: https://davidamitchell.github.io/Research/research/2026-06-13-platform-engineering-innersource-hybrid-standardization.html; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q4-decision-rights-placement.html]

**Q6 Transfer**

Parnas found that the effectiveness of a modularisation depends on the decomposition criteria and supports flexibility, comprehensibility and shorter development time. [fact; source: https://experts.mcmaster.ca/scholarly-works/2169027]

Simon's near-decomposability argument underlies treating components as separable and carries a caution about analogy. [fact; source: https://www.sfipress.org/21-simon-1962]

Sanchez and Mahoney argue that embedding coordination in fully specified, standardised component interfaces reduces the need for managerial authority across unit interfaces. [fact; source: https://experts.illinois.edu/en/publications/modularity-flexibility-and-knowledge-management-in-product-and-or/]

This is the component-layer analogue of self-service with guardrails and platform commoditisation. [inference; source: https://experts.illinois.edu/en/publications/modularity-flexibility-and-knowledge-management-in-product-and-or/]

Sosa, Eppinger and Rowles studied aircraft engine development and report that boundary effects moderate the effect of interface strength and are contingent on system modularity. [fact; source: https://pubsonline.informs.org/doi/fpi/10.1287/mnsc.1040.0289]

Access note: the Sosa page returned an access error and its abstract was read through a Crossref record. [assumption; source: https://pubsonline.informs.org/doi/fpi/10.1287/mnsc.1040.0289]

Colfer and Baldwin reviewed 142 studies, find mirroring prevalent but not universal, and report that partial mirroring is likely superior in technologically dynamic industries. [fact; source: https://www.hbs.edu/ris/download.aspx?name=16-124.pdf]

They report that firms can break the mirror through modular partitions or relational contracts and that open collaborative projects, mostly software, were not supportive of mirroring. [fact; source: https://www.hbs.edu/ris/download.aspx?name=16-124.pdf]

Cataldo and colleagues found that congruence between coordination requirements and actual coordination activities shortened development time. [fact; source: https://patrick.wagstrom.net/publications/Cataldo_2006_IdentificationOfCoordinationRequirements.pdf]

Together these support transfer to software components for dependency structure and volatility, with the caveat that the evidence concerns mapping dependencies to team communication more than choosing a mechanism per dependency. [inference; source: https://www.hbs.edu/ris/download.aspx?name=16-124.pdf; https://patrick.wagstrom.net/publications/Cataldo_2006_IdentificationOfCoordinationRequirements.pdf]

Transfer to governed decisions rests only on repository items about decision rights and governance queues, and no source in this item tests the properties on decision-to-decision dependencies. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q4-decision-rights-placement.html]

Adjacent-layer effects are supported: Conway states that organising a design team already fixes design decisions, and DORA discusses the Inverse Conway Maneuver, which shapes team structure to produce a desired architecture. [fact; source: https://blog.acolyer.org/2019/12/13/how-do-committees-invent/; https://dora.dev/capabilities/loosely-coupled-teams/]

Search log: Henderson and Clark (1990); publication record only, no claim relies on it.

### §3 Reasoning

1. Properties of the link (recurrence, uncertainty, interdependence form, volatility) and properties of the terminus (cost of wrong outcome, required certainty) come from different literatures and should be reported separately. [inference; source: https://genres.syr.edu/sites/default/files/acmcs94.pdf]
2. The measured costs found concern waiting and re-integration, not the selection of a mechanism for a specialist dependency. [inference; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]
3. Convergence cost has a partly measured driver, and rollout cost has none in the sources found. [inference; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]
4. Because a rival account (threat-rigidity) predicts the opposite of the time-pressure hypothesis, that hypothesis cannot be graded above assumption. [inference; source: https://eric.ed.gov/?id=EJ255060]
5. Transfer to components has partial support for dependency-to-communication mapping, while transfer to decisions has only repository-internal support. [inference; source: https://www.hbs.edu/ris/download.aspx?name=16-124.pdf]

### §4 Consistency Check

```text
contradiction_scan: contradiction_1 partly open, contradiction_2 open
contradiction_1: Kapser and Godfrey (duplication often benign) versus Krüger and Berger (duplication does not scale); partly open; candidate moderators are duration and delta of divergence, clone purpose or type, platform co-evolution and the outcome measured
contradiction_2: time pressure toward duplication versus threat-rigidity toward centralisation; unresolved, kept as hypothesis with rival
confidence_adjustment: all property-to-mechanism links capped at medium
scope_guardrail: maintained
```

### §5 Depth and Breadth Expansion

Technical lens: component dependencies can be commoditised through specified interfaces, which removes the need for per-request coordination. [inference; source: https://experts.illinois.edu/en/publications/modularity-flexibility-and-knowledge-management-in-product-and-or/]

The same lens warns that the right decomposition criteria matter more than the existence of modules. [inference; source: https://experts.mcmaster.ca/scholarly-works/2169027]

Economic lens: Krüger and Berger find platforms need high upfront investment while clone and own is initially cheap, so timing of investment interacts with delivery pressure. [fact; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]

Behavioural lens: threat-rigidity predicts that pressured units restrict information and tighten control, which could make a duplicate-first regime harder to sustain. [inference; source: https://eric.ed.gov/?id=EJ255060]

Regulatory lens: governance-infrastructure standardisation rises with regulatory exposure, so regulated dependencies move towards synchronisation regardless of recurrence. [inference; source: https://davidamitchell.github.io/Research/research/2026-06-13-standardization-customization-balance-context-ai.html]

Historical lens: the property sets date from 1967 to 1994 studies of organisations and have been re-tested mostly in software settings since. [inference; source: https://www.hbs.edu/ris/download.aspx?name=16-124.pdf]

### §6 Synthesis

*(This section seeds the Findings below.)*

Executive summary:

Properties of a specialist dependency predict which coordination mechanism works better, but no property set found prescribes the mechanism without organisational context. [inference; source: https://eric.ed.gov/?id=EJ251028; https://www.hbs.edu/ris/download.aspx?name=16-124.pdf]
High recurrence with reversible, bounded-impact work favours delegation, self-service or standardised interfaces, while high required certainty and regulatory exposure favour synchronisation. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q4-decision-rights-placement.html; https://davidamitchell.github.io/Research/research/2026-06-13-standardization-customization-balance-context-ai.html]
Convergence cost grows with duration and size of divergence in one organisation's cost estimations. [fact; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]
That quantification is thin, which leaves the magnitude of convergence cost unestablished. [inference; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]
Rollout cost and the time-pressure effect were not measured in any source found. [inference; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf; https://eric.ed.gov/?id=EJ255060]
The properties partly transfer to software components and to governed decisions only by inference. [inference; source: https://www.hbs.edu/ris/download.aspx?name=16-124.pdf]

Key findings:

1. The dependency properties found in the literature predict which coordination mechanism works better but none of the property sets reviewed prescribes the mechanism without organisational context, because the contingency critique and the mixed software evidence both show conditional rather than deterministic relationships. ([inference]; medium confidence; source: https://eric.ed.gov/?id=EJ251028; https://www.hbs.edu/ris/download.aspx?name=16-124.pdf)
2. The candidate property set separates link properties (recurrence and number of requesters, uncertainty or specifiability, interdependence form, volatility over time) from terminus properties (cost of a wrong outcome and required certainty), and required speed appears in the sources reviewed only as a hypothesis. ([inference]; medium confidence; source: https://genres.syr.edu/sites/default/files/acmcs94.pdf; https://www.jstor.org/stable/2094477)
3. High recurrence combined with reversible, bounded-impact work favours moving decision rights or execution to the requesting units through bounded delegation, self-service with guardrails or standardised interfaces rather than queueing on the specialist unit. ([inference]; low confidence; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q4-decision-rights-placement.html; https://experts.illinois.edu/en/publications/modularity-flexibility-and-knowledge-management-in-product-and-or/)
4. High required certainty and high regulatory exposure push towards synchronisation, and the support is qualitative: a failure-rate remark and queueing comparison in the coordination literature plus a repository synthesis that governance-infrastructure standardisation rises with regulatory exposure. ([inference]; low confidence; source: https://genres.syr.edu/sites/default/files/acmcs94.pdf; https://davidamitchell.github.io/Research/research/2026-06-13-standardization-customization-balance-context-ai.html)
5. The cited measurements of synchronisation cost in the evidence reviewed are waiting time in approval and review queues, such as a 441% rise in pull request review time and 97% wait time in one value-stream case, although specialist capacity, batch size and queue utilisation also drive such waits. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q1-flow-constraint.html)
6. Convergence cost grows with how long solutions stayed divergent and with the size of the variant's delta, yet the quantification rests on eight cost estimations from one organisation. ([fact]; medium confidence; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf)
7. No source found measures rollout cost of adopting a general solution across many teams or describes how the general local solution is identified, and the nearest evidence is that platform migration requires re-engineering and affects architecture, organisation structure and process. ([inference]; low confidence; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf; https://dirkriehle.com/wp-content/uploads/2016/12/capraro-riehle-inner-source-definition-benefits-challenges-survey.pdf)
8. The claim that time pressure sets the dial towards duplication has no direct empirical support in the sources found, and threat-rigidity research offers a rival prediction that pressure increases centralised control. ([inference]; low confidence; source: https://eric.ed.gov/?id=EJ255060)
9. Duplicate-then-converge is a recognised pattern, since clone and own is the most common route into platforms and forking patterns include experimental variation with later migration, and it is sounder when divergence is short, the delta small and the general solution identifiable later. ([inference]; medium confidence; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf; https://plg.uwaterloo.ca/~migod/papers/2008/emse08-ClonePatterns.pdf)
10. The properties partly transfer to software components, since the mirroring review and coordination-requirements study support mapping dependencies to team communication but not choosing a mechanism per dependency, while transfer to governed decisions rests only on repository items. ([inference]; low confidence; source: https://www.hbs.edu/ris/download.aspx?name=16-124.pdf; https://patrick.wagstrom.net/publications/Cataldo_2006_IdentificationOfCoordinationRequirements.pdf)

Evidence map: see the Evidence Map table under Findings, which carries the same ten rows.

Assumptions:

- Practitioner descriptions of golden paths and team interaction modes are taken as evidence of practice and not of effect size. [assumption; source: https://teamtopologies.com/key-concepts]
- Findings about product teams and software projects are assumed to carry to specialist-service dependencies when the dependency structure is similar. [assumption; source: https://www.hbs.edu/ris/download.aspx?name=16-124.pdf]
- Repository items are taken as accurate summaries of the sources they cite. [assumption; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q1-flow-constraint.html]

Analysis:

Evidence was weighted by whether a source measured or only described a mechanism. [inference; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]
A measured result concerns re-integration cost, which rises with divergence duration and delta, and it comes from one organisation. [fact; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]
Kapser and Godfrey and Krüger and Berger measure different outcomes, maintainability by clone type versus re-integration cost in one organisation, so duration of divergence is one candidate reconciliation alongside clone purpose, platform co-evolution and organisation scale, and none is tested. [inference; source: https://plg.uwaterloo.ca/~migod/papers/2008/emse08-ClonePatterns.pdf; https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]
Rival remedies for the specialist bottleneck are queue prioritisation, embedding, lateral guilds, self-service and platforms, and the sources favour the reshaping options when recurrence is high and the managing options when certainty must be high. [inference; source: https://genres.syr.edu/sites/default/files/acmcs94.pdf; https://davidamitchell.github.io/Research/research/2026-06-13-platform-engineering-innersource-hybrid-standardization.html]
Pairwise lateral links among embedded specialists grow as n(n-1)/2, which limits how far lateral coordination can substitute for a shared solution. [inference; source: https://davidamitchell.github.io/Research/research/2026-03-12-team-size-limits-brooks-dunbar-network-theory.html]
The shadow-tooling and fragmentation items add that duplicated local tooling accrues tacit-knowledge and turnover risk, though only qualitatively. [inference; source: https://davidamitchell.github.io/Research/research/2026-06-13-shadow-it-custom-tooling-governance-transition.html; https://davidamitchell.github.io/Research/research/2026-06-13-local-tooling-fragmentation-threshold-measurement.html]
Because the contingency critique shows property-to-structure relations are more complex than traditional models assume, the mapping is graded medium at best. [inference; source: https://eric.ed.gov/?id=EJ251028]

Risks, gaps, uncertainties:

- Rollout cost and general-solution identification are unmeasured in the sources found. [inference; source: https://dirkriehle.com/wp-content/uploads/2016/12/capraro-riehle-inner-source-definition-benefits-challenges-survey.pdf]
- The time-pressure hypothesis has no direct support and a rival. [inference; source: https://eric.ed.gov/?id=EJ255060]
- The convergence-cost quantification comes from one organisation and eight estimations. [fact; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]
- Van de Ven, Lawrence and Lorsch and Thompson were read only through secondary pages, and Tushman and Nadler, Burns and Stalker, Duncan, Mintzberg, March and Simon and Henderson and Clark were not read in primary text. [inference; source: https://www.jstor.org/stable/2094477; https://www.talkingaboutorganizations.com/e16/]
- Transfer to governed decisions is untested outside repository items. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q4-decision-rights-placement.html]

Open questions:

- How is the general local solution identified among duplicated embedded solutions, and what does adopting it cost? [assumption; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]
- Does required speed predict mechanism choice once recurrence is controlled for? [assumption; source: https://genres.syr.edu/sites/default/files/acmcs94.pdf]
- Do decision-to-decision dependencies show the same property-to-mechanism links as component dependencies? [assumption; source: https://davidamitchell.github.io/Research/research/2026-08-17-decision-governance.html]

### §7 Recursive Review

```text
review_result: pass
acronym_audit: passed
parity_check: passed
label_audit: passed
```

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

Properties of a specialist dependency predict which coordination mechanism works better, but no property set found prescribes the mechanism without organisational context. [inference; source: https://eric.ed.gov/?id=EJ251028; https://www.hbs.edu/ris/download.aspx?name=16-124.pdf]
High recurrence with reversible, bounded-impact work favours delegation, self-service or standardised interfaces, while high required certainty and regulatory exposure favour synchronisation. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q4-decision-rights-placement.html; https://davidamitchell.github.io/Research/research/2026-06-13-standardization-customization-balance-context-ai.html]
Convergence cost grows with duration and size of divergence in one organisation's cost estimations. [fact; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]
That quantification is thin, which leaves the magnitude of convergence cost unestablished. [inference; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]
Rollout cost and the time-pressure effect were not measured in any source found. [inference; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf; https://eric.ed.gov/?id=EJ255060]
The properties partly transfer to software components and to governed decisions only by inference. [inference; source: https://www.hbs.edu/ris/download.aspx?name=16-124.pdf]

### Key Findings

1. The dependency properties found in the literature predict which coordination mechanism works better but none of the property sets reviewed prescribes the mechanism without organisational context, because the contingency critique and the mixed software evidence both show conditional rather than deterministic relationships. ([inference]; medium confidence; source: https://eric.ed.gov/?id=EJ251028; https://www.hbs.edu/ris/download.aspx?name=16-124.pdf)
2. The candidate property set separates link properties (recurrence and number of requesters, uncertainty or specifiability, interdependence form, volatility over time) from terminus properties (cost of a wrong outcome and required certainty), and required speed appears in the sources reviewed only as a hypothesis. ([inference]; medium confidence; source: https://genres.syr.edu/sites/default/files/acmcs94.pdf; https://www.jstor.org/stable/2094477)
3. High recurrence combined with reversible, bounded-impact work favours moving decision rights or execution to the requesting units through bounded delegation, self-service with guardrails or standardised interfaces rather than queueing on the specialist unit. ([inference]; low confidence; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q4-decision-rights-placement.html; https://experts.illinois.edu/en/publications/modularity-flexibility-and-knowledge-management-in-product-and-or/)
4. High required certainty and high regulatory exposure push towards synchronisation, and the support is qualitative: a failure-rate remark and queueing comparison in the coordination literature plus a repository synthesis that governance-infrastructure standardisation rises with regulatory exposure. ([inference]; low confidence; source: https://genres.syr.edu/sites/default/files/acmcs94.pdf; https://davidamitchell.github.io/Research/research/2026-06-13-standardization-customization-balance-context-ai.html)
5. The cited measurements of synchronisation cost in the evidence reviewed are waiting time in approval and review queues, such as a 441% rise in pull request review time and 97% wait time in one value-stream case, although specialist capacity, batch size and queue utilisation also drive such waits. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q1-flow-constraint.html)
6. Convergence cost grows with how long solutions stayed divergent and with the size of the variant's delta, yet the quantification rests on eight cost estimations from one organisation. ([fact]; medium confidence; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf)
7. No source found measures rollout cost of adopting a general solution across many teams or describes how the general local solution is identified, and the nearest evidence is that platform migration requires re-engineering and affects architecture, organisation structure and process. ([inference]; low confidence; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf; https://dirkriehle.com/wp-content/uploads/2016/12/capraro-riehle-inner-source-definition-benefits-challenges-survey.pdf)
8. The claim that time pressure sets the dial towards duplication has no direct empirical support in the sources found, and threat-rigidity research offers a rival prediction that pressure increases centralised control. ([inference]; low confidence; source: https://eric.ed.gov/?id=EJ255060)
9. Duplicate-then-converge is a recognised pattern, since clone and own is the most common route into platforms and forking patterns include experimental variation with later migration, and it is sounder when divergence is short, the delta small and the general solution identifiable later. ([inference]; medium confidence; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf; https://plg.uwaterloo.ca/~migod/papers/2008/emse08-ClonePatterns.pdf)
10. The properties partly transfer to software components, since the mirroring review and coordination-requirements study support mapping dependencies to team communication but not choosing a mechanism per dependency, while transfer to governed decisions rests only on repository items. ([inference]; low confidence; source: https://www.hbs.edu/ris/download.aspx?name=16-124.pdf; https://patrick.wagstrom.net/publications/Cataldo_2006_IdentificationOfCoordinationRequirements.pdf)

### Evidence Map

| Claim | Source | Confidence | Notes (Key Finding (KF) number) |
|---|---|---|---|
| [inference] Properties predict but do not prescribe the mechanism | https://eric.ed.gov/?id=EJ251028; https://www.hbs.edu/ris/download.aspx?name=16-124.pdf | medium | KF1 |
| [inference] Link and terminus properties form separate groups | https://genres.syr.edu/sites/default/files/acmcs94.pdf; https://www.jstor.org/stable/2094477 | medium | KF2; Van de Ven via secondary summary |
| [inference] Recurrence with reversibility favours delegation or self-service | https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q4-decision-rights-placement.html; https://experts.illinois.edu/en/publications/modularity-flexibility-and-knowledge-management-in-product-and-or/ | low | KF3 |
| [inference] Required certainty and regulatory exposure favour synchronisation | https://genres.syr.edu/sites/default/files/acmcs94.pdf; https://davidamitchell.github.io/Research/research/2026-06-13-standardization-customization-balance-context-ai.html | low | KF4; qualitative |
| [inference] Measured synchronisation cost is queue waiting | https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q1-flow-constraint.html | medium | KF5 |
| [fact] Convergence cost grows with duration and delta | https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf | medium | KF6; single organisation |
| [inference] Rollout cost is unmeasured in sources found | https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf; https://dirkriehle.com/wp-content/uploads/2016/12/capraro-riehle-inner-source-definition-benefits-challenges-survey.pdf | low | KF7 |
| [inference] Time pressure toward duplication is unsupported and has a rival | https://eric.ed.gov/?id=EJ255060 | low | KF8 |
| [inference] Duplicate-then-converge is recognised, with conditions | https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf; https://plg.uwaterloo.ca/~migod/papers/2008/emse08-ClonePatterns.pdf | medium | KF9 |
| [inference] Transfer holds for components, only inferred for decisions | https://www.hbs.edu/ris/download.aspx?name=16-124.pdf; https://patrick.wagstrom.net/publications/Cataldo_2006_IdentificationOfCoordinationRequirements.pdf | low | KF10 |

### Assumptions

- Practitioner descriptions of golden paths and team interaction modes are taken as evidence of practice and not of effect size. [assumption; source: https://teamtopologies.com/key-concepts]
- Findings about product teams and software projects are assumed to carry to specialist-service dependencies when the dependency structure is similar. [assumption; source: https://www.hbs.edu/ris/download.aspx?name=16-124.pdf]
- Repository items are taken as accurate summaries of the sources they cite. [assumption; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q1-flow-constraint.html]

### Analysis

Evidence was weighted by whether a source measured or only described a mechanism. [inference; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]
A measured result concerns re-integration cost, which rises with divergence duration and delta, and it comes from one organisation. [fact; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]
Kapser and Godfrey and Krüger and Berger measure different outcomes, maintainability by clone type versus re-integration cost in one organisation, so duration of divergence is one candidate reconciliation alongside clone purpose, platform co-evolution and organisation scale, and none is tested. [inference; source: https://plg.uwaterloo.ca/~migod/papers/2008/emse08-ClonePatterns.pdf; https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]
Rival remedies for the specialist bottleneck are queue prioritisation, embedding, lateral guilds, self-service and platforms, and the sources favour the reshaping options when recurrence is high and the managing options when certainty must be high. [inference; source: https://genres.syr.edu/sites/default/files/acmcs94.pdf; https://davidamitchell.github.io/Research/research/2026-06-13-platform-engineering-innersource-hybrid-standardization.html]
Pairwise lateral links among embedded specialists grow as n(n-1)/2, which limits how far lateral coordination can substitute for a shared solution. [inference; source: https://davidamitchell.github.io/Research/research/2026-03-12-team-size-limits-brooks-dunbar-network-theory.html]
The shadow-tooling and fragmentation items add that duplicated local tooling accrues tacit-knowledge and turnover risk, though only qualitatively. [inference; source: https://davidamitchell.github.io/Research/research/2026-06-13-shadow-it-custom-tooling-governance-transition.html; https://davidamitchell.github.io/Research/research/2026-06-13-local-tooling-fragmentation-threshold-measurement.html]
Because the contingency critique shows property-to-structure relations are more complex than traditional models assume, the mapping is graded medium at best. [inference; source: https://eric.ed.gov/?id=EJ251028]

### Risks, Gaps, and Uncertainties

- Rollout cost and general-solution identification are unmeasured in the sources found. [inference; source: https://dirkriehle.com/wp-content/uploads/2016/12/capraro-riehle-inner-source-definition-benefits-challenges-survey.pdf]
- The time-pressure hypothesis has no direct support and a rival. [inference; source: https://eric.ed.gov/?id=EJ255060]
- The convergence-cost quantification comes from one organisation and eight estimations. [fact; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]
- Van de Ven, Lawrence and Lorsch and Thompson were read only through secondary pages, and Tushman and Nadler, Burns and Stalker, Duncan, Mintzberg, March and Simon and Henderson and Clark were not read in primary text. [inference; source: https://www.jstor.org/stable/2094477; https://www.talkingaboutorganizations.com/e16/]
- Transfer to governed decisions is untested outside repository items. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q4-decision-rights-placement.html]

### Open Questions

- How is the general local solution identified among duplicated embedded solutions, and what does adopting it cost? [assumption; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]
- Does required speed predict mechanism choice once recurrence is controlled for? [assumption; source: https://genres.syr.edu/sites/default/files/acmcs94.pdf]
- Do decision-to-decision dependencies show the same property-to-mechanism links as component dependencies? [assumption; source: https://davidamitchell.github.io/Research/research/2026-08-17-decision-governance.html]

---

## Output

*(Fill in when completing: what was produced as a result of this research?)*

- Type: knowledge
- Description: A candidate property set and an evidence-graded mapping from dependency properties to coordination mechanisms, with convergence cost, rollout cost and time-pressure effects flagged as measured, unmeasured or hypothesis. [inference; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]
- Links: https://genres.syr.edu/sites/default/files/acmcs94.pdf; https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf; https://www.hbs.edu/ris/download.aspx?name=16-124.pdf
