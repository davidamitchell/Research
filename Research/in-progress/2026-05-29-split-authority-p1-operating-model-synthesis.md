---
review_count: 2
title: "Operating model synthesis for split-authority delivery systems"
added: 2026-05-29
status: reviewing
priority: high
tags: [operating-model, governance, throughput, delivery-risk]
blocks: [2026-05-29-split-authority-q1-flow-constraint, 2026-05-29-split-authority-q2-demand-segmentation, 2026-05-29-split-authority-q3-routing-exception-isolation, 2026-05-29-split-authority-q4-decision-rights-placement, 2026-05-29-split-authority-q5-control-model-tradeoff, 2026-05-29-split-authority-q6-instability-leading-indicators]
started: 2026-05-30T03:10:30+00:00
completed: ~
output: [knowledge]
cites:
  - 2026-04-01-backpressure-theory-of-constraints
  - 2026-05-09-build-vs-improve-throughput-tradeoff
  - 2026-05-14-org-failure-modes-project-demand-product-it
  - 2026-05-14-org-failure-modes-cohort-demand-domain-it
  - 2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate
  - 2026-05-16-governance-structures-build-mode-without-full-accountability-colocation
  - 2026-05-16-variance-control-comparison-across-delivery-modes
  - 2026-05-16-do-mode-demand-persistence-and-build-mode-displacement
  - 2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance
  - 2026-05-23-governance-controls-effectiveness-conditions
  - 2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention
related:
  - 2026-05-23-governance-reform-leadership-failure
  - 2026-04-22-enterprise-ai-platform-operating-models
supersedes: ~
superseded_by: []
item_type: synthesis
confidence: medium
themes:
  - governance-policy
  - organisational-design
  - cost-performance
  - enterprise-adoption
  - tools-infrastructure
versions: []
---

# Operating model synthesis for split-authority delivery systems

## Research Question

What operating model improves throughput while reducing delivery risk in a split-authority environment, where "split-authority environment" means a delivery context in which authority is divided among at least two stakeholder groups with independent veto or approval power, typically a business owner, a technology delivery team, and an independent risk or compliance function?

## Scope

**In scope:**
- Synthesis of answers from Q1-Q6 topic areas into one operating model recommendation, drawing on completed repository items that address the same questions.
- Throughput-risk trade-offs for governance, queueing, delegation, and escalation choices.
- Decision-ready design principles that preserve control without queue explosion.

**Out of scope:**
- Company-specific transformation plans or tool-vendor implementation details.
- Running primary investigations on topics not already addressed in completed repository items or the foundational sources listed here.

**Constraints:**
- This is a synthesis item; major claims must be traceable to completed repository items or externally cited sources.
- Separate evidence-backed claims from analogy-driven heuristics.
- Q1-Q6 dependency items are in backlog and have not been completed; this synthesis draws on completed repository items that address the same empirical territory.

## Context

A split-authority delivery system is one in which no single actor owns risk, cost, and execution simultaneously. This is the standard operating condition for regulated enterprises, shared-service technology functions, and large-scale product-and-platform organisations. The six sub-questions (Q1 flow constraint, Q2 demand segmentation, Q3 routing and exception isolation, Q4 decision rights placement, Q5 control model trade-offs, Q6 leading indicators) have not yet been answered as standalone completed items. This synthesis draws instead on the body of completed repository items that collectively address the same causal territory. [assumption; source: https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html; https://davidamitchell.github.io/Research/research/2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate.html]

## Approach

1. Consolidate the evidence base from completed repository items into a causal map of throughput and risk in split-authority delivery.
2. Compare candidate operating models against this causal map.
3. Produce a bounded recommendation with guardrails, escalation logic, and warning thresholds.

## Sources

- [x] [Mitchell (2026) Backpressure Infrastructure and the Theory of Constraints](https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html)
- [x] [Mitchell (2026) Build versus improve throughput trade-off](https://davidamitchell.github.io/Research/research/2026-05-09-build-vs-improve-throughput-tradeoff.html)
- [x] [Mitchell (2026) IT throughput capacity as a constraint on unmet operational capability demand accumulation](https://davidamitchell.github.io/Research/research/2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate.html)
- [x] [Mitchell (2026) Governance structures that support investment in delivery capability without one owner for risk, cost, and benefits](https://davidamitchell.github.io/Research/research/2026-05-16-governance-structures-build-mode-without-full-accountability-colocation.html)
- [x] [Mitchell (2026) Variance control comparison across delivery modes](https://davidamitchell.github.io/Research/research/2026-05-16-variance-control-comparison-across-delivery-modes.html)
- [x] [Mitchell (2026) Integrator rights versus risk, cost, benefit co-location governance](https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html)
- [x] [Mitchell (2026) Internal governance controls: effectiveness conditions in regulated enterprises](https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html)
- [x] [Mitchell (2026) Customer-segment demand prioritisation against domain-based IT teams: organisational failure modes](https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-cohort-demand-domain-it.html)
- [x] [Mitchell (2026) Project-demand versus product-IT: organisational failure modes](https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-project-demand-product-it.html)
- [x] [TOC Institute (2024) Five Focusing Steps](https://www.tocinstitute.org/five-focusing-steps.html)
- [x] [Little (1961) A proof for the queuing formula, Operations Research](https://econpapers.repec.org/RePEc:inm:oropre:v:9:y:1961:i:3:p:383-387)
- [x] [DORA (2024) DORA metrics and four keys](https://dora.dev/guides/dora-metrics-four-keys/)
- [x] [DORA (2024) Loosely coupled teams capability](https://dora.dev/capabilities/loosely-coupled-teams/)
- [x] [Skelton and Pais (2019) Team Topologies key concepts](https://teamtopologies.com/key-concepts)
- [x] [Basel Committee on Banking Supervision (2015) BCBS 328 Corporate governance principles](https://www.bis.org/bcbs/publ/d328.pdf)
- [x] [Adler and Borys (1996) Two types of bureaucracy: enabling and coercive, Administrative Science Quarterly](https://eric.ed.gov/?id=EJ525938)
- [x] [MIT CISR (2023) Simplifying decision rights for growth](https://cisr.mit.edu/content/simplifying-decision-rights-growth)
- [x] [Bain and Company (2022) Who does what? Decision accountability](https://www.bain.com/insights/decisions-who-does-what/)
- [x] [Reinertsen (2009) The Principles of Product Development Flow (via ToC completed item)](https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html)

---

## Research Skill Output

### §0 Initialise

Question: What operating model improves throughput while reducing delivery risk in a split-authority environment?

A split-authority environment (defined on first use in Research Question) is the standard condition for large regulated enterprises. Delivery authority is distributed across business owners, technology delivery teams, risk and compliance functions, and sometimes shared-service owners.

Scope: confirmed as bounded to synthesis of completed repository items and foundational flow, governance, and operations literature. Net-new primary investigations not required.

Constraints:
- Claims labelled [fact] require a URL-backed source.
- Claims labelled [inference] are derived from evidence; a source is required.
- Claims labelled [assumption] are not verified; justification is required with nearest URL-backed source.
- Q1-Q6 backlog items have not been completed; this synthesis draws on completed items that address the same empirical territory and treats the Q1-Q6 questions as a structuring frame.
- Output format: structured synthesis with Executive Summary, Key Findings, Evidence Map, Assumptions, Analysis, Risks, Open Questions, and Output section.

### §1 Question Decomposition

The research question decomposes into four atomic questions that map onto the Q1-Q6 territory:

**A. What is the dominant flow constraint in split-authority delivery?**
- A1. Does delay originate primarily from capacity shortage or from governance-generated queueing (approval wait, dependency coordination, fragmented decision rights)?
- A2. How does Work in Progress (WIP, meaning work that has been started but not yet completed) accumulate and damage throughput when governance is the constraint?
- A3. What role does dependency coupling play in converting governance-generated delay into system-wide throughput loss?

**B. How should incoming work be segmented?**
- B1. What criteria distinguish standard, routine, reversible work (suitable for fast-path handling) from exceptional, novel, or high-consequence work (requiring slower controlled review)?
- B2. What minimum set of demand classes supports differentiated control intensity without excessive classification overhead?

**C. What decision rights placement and control model best balances throughput and risk?**
- C1. Which execution decisions (sequencing, scope, local spend, incident response) must sit with delivery teams to reduce approval latency without losing governance outcomes?
- C2. When should pre-approval controls be used versus bounded delegation (delegation within defined guardrails with escalation paths) versus post-hoc review?
- C3. What authority bundle must an integrator hold for governance to be effective without structural co-location of risk, cost, and benefits?

**D. What leading indicators detect destabilisation before severe failure?**
- D1. Which metric families (queue age, WIP, blocked-work ratio, exception volume, lead time, rework rate) reliably predict unsafe queue growth or rising delivery risk?
- D2. What trigger thresholds should shift control regimes between fast-path, standard, and exception handling?

### §2 Investigation

#### A1-A3: Flow constraint identification

**Claim: Governance-generated queueing is the dominant delay source in split-authority delivery, not raw capacity shortage.**

In the Theory of Constraints (ToC), any production system has a single constraint that limits total throughput; relieving non-constraints produces little system-wide improvement. [fact; source: https://www.tocinstitute.org/five-focusing-steps.html] In split-authority environments the constraint is typically not headcount but the serial approval gates, dependency coordination steps, and fragmented decision rights that hold work in queues between approval stages. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate.html; https://dora.dev/capabilities/loosely-coupled-teams/]

The completed repository item on Information Technology (IT) throughput constraint found that throughput loss is driven as much by dependency topology as by raw staffing levels, because tightly coupled architectures and domain-queue handoffs convert operational demand into long waits, release orchestration, and queue growth that central teams cannot clear quickly. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate.html; https://dora.dev/capabilities/loosely-coupled-teams/; https://www.melconway.com/Home/Conways_Law.html]

**Claim: Excess WIP (Work in Progress) lengthens lead time and reduces predictability according to Little's Law.**

Little's Law, first formalised by John Little in 1961, states that the average number of items in a stable queuing system equals the average arrival rate multiplied by the average time each item spends in the system. [fact; source: https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387] When work entry into a delivery system exceeds completion rate, WIP rises, lead time lengthens, and predictability falls. [inference; source: https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387; https://davidamitchell.github.io/Research/research/2026-05-09-build-vs-improve-throughput-tradeoff.html]

**Claim: Conway's Law connects architecture to dependency coupling and queue growth.**

Conway's Law observes that organisations produce systems that mirror their communication structure. [fact; source: https://www.melconway.com/Home/Conways_Law.html] When authority is split across siloed domains, delivery teams inherit the coordination overhead of those boundaries in the form of approval chains, hand-off queues, and cross-team dependencies that all add to WIP and reduce flow. [inference; source: https://www.melconway.com/Home/Conways_Law.html; https://dora.dev/capabilities/loosely-coupled-teams/; https://teamtopologies.com/key-concepts]

#### B1-B2: Demand segmentation

**Claim: Demand should be classified by risk, reversibility, and standardisation, not by organisational origin.**

The completed repository item on organisational failure modes found that when all demand enters a single queue regardless of urgency, complexity, or risk level, high-variance exceptional work blocks routine low-risk work and the effective throughput of the lane falls for everyone. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-cohort-demand-domain-it.html; https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-project-demand-product-it.html] The completed item on delivery-operations mode demand persistence found that demand from delivery-operations activities, such as Business As Usual (BAU) change, incident response, and minor enhancement, persists and accumulates independently of build-mode project demand, and that treating both streams as a single undifferentiated queue is a primary driver of build-mode displacement. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.html]

Site Reliability Engineering (SRE) change management and Software Configuration Management (SCM) practice both use similar classification logic: work that is standard, pre-tested, and reversible travels a fast path; work that is complex, novel, or high-consequence travels a controlled path with deeper review. [inference; source: https://dora.dev/capabilities/loosely-coupled-teams/; https://davidamitchell.github.io/Research/research/2026-05-16-variance-control-comparison-across-delivery-modes.html]

**Claim: Three demand classes are sufficient to differentiate control intensity without excessive classification overhead.**

A three-class segmentation is the minimum viable structure supported by the evidence:
- Class 1 (fast path): standard, reversible, pre-approved template or previously demonstrated work. Handled with post-hoc audit only.
- Class 2 (standard path): routine but non-trivial, limited risk, bounded scope. Handled with lightweight pre-approval or bounded delegation (delegation within defined guardrails with pre-agreed escalation paths).
- Class 3 (exception path): novel, high-consequence, irreversible, or ambiguous. Handled with full pre-approval and expert review. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-16-variance-control-comparison-across-delivery-modes.html; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html; https://dora.dev/capabilities/loosely-coupled-teams/]

#### C1-C3: Decision rights placement and control model

**Claim: High-frequency execution decisions should sit with delivery teams.**

The completed item on integrator rights found that explicit integrator rights become a credible substitute for structural co-location only when one named decision owner can resolve prioritisation, what-versus-how choices, and exception trade-offs without committee ambiguity. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html; https://cisr.mit.edu/content/simplifying-decision-rights-growth]

For high-frequency decisions with limited consequences and high reversibility (daily sequencing, minor scope adjustment, local environment spend, incident response), centralised pre-approval generates approval-queue congestion without a proportionate risk-reduction return. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html; https://www.bain.com/insights/decisions-who-does-what/]

The DevOps Research and Assessment (DORA) loosely coupled teams capability finds that the highest-performing delivery organisations allow teams to make most decisions independently without needing approval from outside the team. [fact; source: https://dora.dev/capabilities/loosely-coupled-teams/]

**Claim: Pre-approval controls should be reserved for novel, high-consequence, or irreversible decisions.**

The completed item on governance controls effectiveness found that internal governance controls are most likely to minimise coordination cost when reserved for transactions with high uncertainty, high consequence, or high relationship-specific investment (investments that lose value outside a focal relationship), because those are the cases where pre-approval error correction is economically justified. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html; https://ageconsearch.umn.edu/record/294665/files/ipr018.pdf]

Controls are enabling (that is, they help staff solve exceptions with authoritative information and intelligible authority) rather than coercive (adding surveillance, repetitive approval, or low-signal checkpoints) when they match risk level. [inference; source: https://eric.ed.gov/?id=EJ525938; https://www.bis.org/bcbs/publ/d328.pdf]

High-volume line-by-line review flips from a coordination aid to overhead, because queue growth, approval latency, and very low effective disagreement or override rate indicate that nominal review is no longer producing meaningful challenge. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html]

**Claim: A named integrator with real authority is necessary for governance without structural co-location.**

The governance structures item found that an integrator without budget leverage and explicit escalation rights remains only a coordinator and is likely to reproduce missing-integrator, queue-fragmentation, and cost-shifting failures. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-16-governance-structures-build-mode-without-full-accountability-colocation.html; https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html]

The minimum viable authority bundle includes: budget-recommendation or budget-gating rights within an approved envelope; benefits reporting mandate; power to convene binding cross-functional review; escalation or veto rights when competing demands would displace protected delivery capacity. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html; https://www.bis.org/bcbs/publ/d328.pdf; https://www.bain.com/insights/decisions-who-does-what/]

Banking supervisory guidance (Basel Committee on Banking Supervision, BCBS 328) requires responsibilities, authority, and reporting lines to be clearly allocated across business lines, management, and control functions, and requires control intensity to be proportionate to the institution's size, complexity, and risk profile. [fact; source: https://www.bis.org/bcbs/publ/d328.pdf]

#### D1-D2: Leading indicators

**Claim: Four metric families predict destabilisation in split-authority flow systems.**

The completed item on build-versus-improve throughput tradeoff identifies DORA's four key metrics (deployment frequency, lead time for changes, change failure rate, and mean time to recovery) as the primary throughput and stability measurement bundle. [fact; source: https://davidamitchell.github.io/Research/research/2026-05-09-build-vs-improve-throughput-tradeoff.html; https://dora.dev/guides/dora-metrics-four-keys/]

For split-authority systems specifically, four families of leading indicators predict queue destabilisation before severe throughput or risk failure:
1. Queue health: WIP age distribution and blocked-work ratio, because rising median age signals approval-gate congestion before lead time visibly degrades. [inference; source: https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387; https://www.tocinstitute.org/five-focusing-steps.html]
2. Exception volume: the ratio of Class 3 (exception path) work to total intake, because a rising exception share signals that either the demand-segmentation criteria are miscalibrated or that risk genuinely increasing. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-16-variance-control-comparison-across-delivery-modes.html]
3. Lead time trends: multi-week moving average of cycle time, because persistent upward trend predicts throughput collapse before individual items appear late. [inference; source: https://dora.dev/guides/dora-metrics-four-keys/; https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387]
4. Rework and incident load: the share of team capacity consumed by incidents, rework, and defect remediation, because rising rework acts as an invisible arrival rate that inflates effective WIP without appearing in intake queues. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-09-build-vs-improve-throughput-tradeoff.html; https://sre.google/workbook/eliminating-toil/]

**Claim: Trigger-based control regime shifts are more defensible than fixed percentage-based allocation rules.**

The build-versus-improve item concludes that the most defensible policy is trigger-based: maintain the current control regime while flow indicators stay within agreed bands, then shift to a more constrained or more permissive regime when indicators persistently breach thresholds. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-09-build-vs-improve-throughput-tradeoff.html; https://dora.dev/guides/dora-metrics-four-keys/]

### §3 Reasoning

Removing narrative glue and unsupported generalisations:

The causal chain in split-authority delivery is: fragmented decision rights and approval gates generate WIP accumulation, WIP accumulation extends lead time (Little's Law), extended lead time reduces predictability and throughput, reduced throughput generates workaround demand accumulation and delivery risk. Adding headcount to non-constraints does not break this chain; only relieving the governance-generated constraint does. [inference; source: https://www.tocinstitute.org/five-focusing-steps.html; https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387; https://davidamitchell.github.io/Research/research/2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate.html]

The operating model intervention must therefore target the governance constraint directly: segment demand to prevent exception contamination of routine flow, delegate high-frequency decisions to delivery teams, reserve pre-approval for genuinely novel or high-consequence decisions, assign a named integrator with real authority, and monitor the four leading indicator families for trigger-based regime adjustment. [inference; source: https://www.tocinstitute.org/five-focusing-steps.html; https://dora.dev/capabilities/loosely-coupled-teams/; https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html; https://dora.dev/guides/dora-metrics-four-keys/]

The recommendation has limits. The evidence base for the exact thresholds that should trigger regime shifts is thinner than the evidence for the causal chain itself. Specific band values must be calibrated to the organisation. [assumption; source: https://dora.dev/research/2025/measurement-frameworks/; https://dora.dev/guides/dora-metrics-four-keys/]

### §4 Consistency Check

```text
contradiction_scan: no contradictions identified across §2 evidence. DORA (DevOps Research and Assessment), ToC, Little's Law, and the governance evidence point consistently toward governance-generated delay as the dominant constraint and toward proportionate delegation as the primary remedy.
scope_guardrail: maintained. No net-new primary investigations outside completed items and foundational sources.
claim_labels: all claims in §2 and §3 carry [fact], [inference], or [assumption] labels.
acronym_check: WIP (Work in Progress) expanded at §1 A2. ToC (Theory of Constraints) expanded at §2 A1. SRE (Site Reliability Engineering) expanded at §2 B1. SCM (Software Configuration Management) expanded at §2 B1. DORA (DevOps Research and Assessment) expanded at §2 C1. BCBS expanded at §2 C3 (Basel Committee on Banking Supervision). DBR (Drum-Buffer-Rope) expanded at §5. EBA (European Banking Authority) expanded at §5. PR not used; LLM not used; API not used.
confidence_alignment: synthesis confidence set to medium because key claims are supported by secondary and inference chains from completed repository items rather than by primary experimental studies specific to split-authority delivery settings.
```

### §5 Depth and Breadth Expansion

**Technical lens:** The three-lane architecture maps to the Drum-Buffer-Rope (DBR) scheduling pattern, where the exception path lane acts as the drum (setting the pace for high-consequence review), the standard path lane carries a buffer (pre-approved bounded delegation with defined escalation triggers), and the fast path acts as the rope (work released only to the degree the downstream constraint allows). [inference; source: https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html; https://www.tocinstitute.org/five-focusing-steps.html]

**Regulatory lens:** Banking supervisory guidance (BCBS 328 and European Banking Authority (EBA) internal governance guidelines) requires that governance structures be proportionate to risk profile and that all material responsibilities have clear owners with escalation paths. These requirements are consistent with the recommended operating model but do not prescribe its exact form; they set minimum conditions for the authority bundle. [fact; source: https://www.bis.org/bcbs/publ/d328.pdf; https://www.eba.europa.eu/sites/default/files/document_library/Publications/Guidelines/2021/1016721/Final%20report%20on%20Guidelines%20on%20internal%20governance%20under%20CRD.pdf]

**Behavioural lens:** Adler and Borys' 1996 distinction between enabling and coercive formalisation (formalisation is the degree to which work processes and procedures are codified) remains the behavioural grounding for the control-intensity design principle. Controls perceived as coercive generate resistance and workaround behaviour; controls perceived as enabling are used and respected. [inference; source: https://eric.ed.gov/?id=EJ525938; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html] The completed item on governance failure mechanisms identifies documented bureaucracy-circumvention patterns, including shadow workflows, informal approval chains, and deliberate mis-classification of work to avoid gate controls, as the primary behavioural consequence of coercive control design; these patterns directly reproduce the throughput fragmentation the operating model is designed to prevent. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html]

**Historical lens:** The project-to-product transition evidence base shows that hybrid governance structures (those that preserve project approval authority inside nominally product-oriented delivery teams) tend to recreate the same queue fragmentation, authority conflict, and throughput penalties that the restructure was intended to solve. This is a recurrent pattern in large-enterprise transformations. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-project-demand-product-it.html; https://info.planview.com/rs/456-QCH-520/images/Planview_2023-Project-to-Product-State-of-the-Industry-Report.pdf]

**Economic lens:** The transaction-cost economics framing (associated with Williamson and Coase) provides the economic justification for the control-intensity gradient: tighter hierarchy (pre-approval) is economically efficient only for transactions with high relationship-specific investment, high uncertainty, or high consequence. For routine low-risk transactions, the coordination cost of pre-approval exceeds its error-reduction value. [inference; source: https://ageconsearch.umn.edu/record/294665/files/ipr018.pdf; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html]

### §6 Synthesis

The operating model that improves throughput while reducing delivery risk in a split-authority environment combines five design principles: (1) identify and protect the dominant governance-generated flow constraint rather than adding capacity to non-constraints; (2) segment incoming demand into three classes by risk, reversibility, and standardisation to prevent exception work from contaminating routine flow; (3) delegate high-frequency execution decisions to delivery teams using bounded delegation, reserving pre-approval only for novel, high-consequence, or irreversible decisions; (4) assign a named integrator with a real authority bundle covering budget-recommendation, prioritisation, escalation, and exception-veto rights; and (5) monitor four leading indicator families (queue health, exception volume, lead time trends, rework and incident load) with trigger-based thresholds that govern control regime shifts. [inference; source: https://www.tocinstitute.org/five-focusing-steps.html; https://dora.dev/capabilities/loosely-coupled-teams/; https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html; https://dora.dev/guides/dora-metrics-four-keys/]

**Key Findings**

1. Governance-generated queueing (approval latency, multi-party coordination, fragmented decision rights) is the dominant flow constraint in split-authority delivery systems; adding headcount to non-constraints does not improve system throughput. ([inference]; medium confidence; source: https://www.tocinstitute.org/five-focusing-steps.html; https://davidamitchell.github.io/Research/research/2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate.html; https://dora.dev/capabilities/loosely-coupled-teams/; https://davidamitchell.github.io/Research/research/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.html)

2. Little's Law implies that excess WIP extends lead time and reduces predictability, so controlling the work entry rate into split-authority queues is a prerequisite for throughput improvement, not just a scheduling convenience. ([inference]; high confidence; source: https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387; https://davidamitchell.github.io/Research/research/2026-05-09-build-vs-improve-throughput-tradeoff.html)

3. A three-class demand segmentation (fast path for standard reversible work, standard path for bounded delegation, exception path for novel high-consequence work) prevents exception contamination of routine flow lanes without creating unsustainable classification overhead. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-16-variance-control-comparison-across-delivery-modes.html; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html)

4. High-frequency execution decisions (daily sequencing, minor scope adjustment, local environment spend, and incident response) should be delegated to delivery teams, because centralised pre-approval of these decisions generates approval-queue congestion without a proportionate risk-reduction return relative to the coordination cost incurred. ([inference]; medium confidence; source: https://dora.dev/capabilities/loosely-coupled-teams/; https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html; https://www.bain.com/insights/decisions-who-does-what/)

5. Pre-approval controls minimise coordination cost only when reserved for transactions with high uncertainty, high consequence, or high relationship-specific investment; applying pre-approval uniformly to all work converts governance from a coordination aid into a throughput constraint and generates workaround behaviour in teams that experience controls as coercive. ([inference]; medium confidence; source: https://ageconsearch.umn.edu/record/294665/files/ipr018.pdf; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html; https://eric.ed.gov/?id=EJ525938; https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html)

6. Banking supervisory guidance requires control intensity to be proportionate to risk profile and all material responsibilities to have named owners with escalation paths, which is structurally consistent with the three-class segmentation and the named-integrator requirement, and sets the minimum standard for the authority bundle. ([fact]; high confidence; source: https://www.bis.org/bcbs/publ/d328.pdf; https://www.eba.europa.eu/sites/default/files/document_library/Publications/Guidelines/2021/1016721/Final%20report%20on%20Guidelines%20on%20internal%20governance%20under%20CRD.pdf)

7. An integrator without budget-recommendation rights, explicit escalation authority, and a benefits-reporting mandate remains only a coordinator and will reproduce queue-fragmentation and cost-shifting failure patterns observed across multiple completed repository items. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-16-governance-structures-build-mode-without-full-accountability-colocation.html; https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html)

8. Conway's Law and Team Topologies research jointly imply that authority fragmentation embeds itself in delivery-system dependency coupling; a governance redesign that does not address team boundary alignment will face recurring re-emergence of the same coordination queues. ([inference]; medium confidence; source: https://www.melconway.com/Home/Conways_Law.html; https://teamtopologies.com/key-concepts; https://dora.dev/capabilities/loosely-coupled-teams/)

9. Four leading indicator families (queue health as WIP age and blocked-work ratio, exception volume as Class 3 share of total intake, lead time trends as multi-week moving average, and rework and incident load as share of capacity consumed by remediation) provide early warning of throughput destabilisation, with rising values in any family signalling that control-regime tightening may be warranted before severe failure occurs. ([inference]; medium confidence; source: https://dora.dev/guides/dora-metrics-four-keys/; https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387; https://sre.google/workbook/eliminating-toil/)

10. Trigger-based control regime adjustments (shifting lanes, tightening or relaxing delegation bounds, escalating to pre-approval) are more defensible than fixed percentage-based rules because they respond to actual flow state rather than to a fixed schedule, which is the same logic as the Theory of Constraints' constraint-elevation step. ([inference]; medium confidence; source: https://www.tocinstitute.org/five-focusing-steps.html; https://davidamitchell.github.io/Research/research/2026-05-09-build-vs-improve-throughput-tradeoff.html; https://dora.dev/guides/dora-metrics-four-keys/)

**Assumptions**

- The dominant flow constraint in a specific organisation's split-authority environment is governance-generated queueing rather than raw capacity; organisations where headcount is genuinely the bottleneck should address the capacity constraint first before redesigning governance. [assumption; source: https://www.tocinstitute.org/five-focusing-steps.html; https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html]
- The three demand classes map to work types that the organisation can distinguish at intake; if work classification is infeasible due to information asymmetry, the segmentation approach requires an intake triage step before the three-lane model is operable. [assumption; source: https://davidamitchell.github.io/Research/research/2026-05-16-variance-control-comparison-across-delivery-modes.html]
- The named integrator can be credibly empowered with budget-recommendation rights in the organisation's governance structure; in organisations where budget authority is entirely held by finance or a central committee, the integrator model would need to be adapted to whatever authority form is available. [assumption; source: https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html; https://www.bis.org/bcbs/publ/d328.pdf]

**Risks and Gaps**

- Threshold values for the four leading indicator families must be calibrated empirically to each organisation; the evidence base does not supply universal trigger numbers. [inference; source: https://dora.dev/research/2025/measurement-frameworks/; https://dora.dev/guides/dora-metrics-four-keys/]
- The Q1-Q6 dependency items have not been completed; this synthesis uses completed repository items as proxies. A future cycle completing Q1-Q6 as primary research items could validate, refine, or contradict these conclusions. [assumption; source: https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html]
- The evidence is strongest on mechanism and direction; it does not supply cross-firm empirical comparisons of operating model variants that would allow confidence to be elevated to high for the synthesis claims. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html]

**Open Questions**

- Which specific WIP-age and exception-volume thresholds best predict irreversible queue collapse in split-authority regulated enterprises?
- What is the minimum viable integrator authority bundle in organisations where budget authority cannot be delegated below a central finance committee?
- How does the three-lane segmentation interact with Artificial Intelligence (AI)-assisted delivery acceleration: do AI throughput gains change the relative proportion of work that reaches exception-path status?

### §7 Recursive Review

```text
review_result: pass
acronym_audit: WIP (Work in Progress) expanded at §1 A2 first narrative prose use. ToC (Theory of Constraints) expanded at §2 A1 first use. IT (Information Technology) expanded at §2 A1. SRE (Site Reliability Engineering) expanded at §2 B1. SCM (Software Configuration Management) expanded at §2 B1. BAU (Business As Usual) expanded at §2 B1. DORA (DevOps Research and Assessment) expanded at §2 C1 first narrative prose use. BCBS (Basel Committee on Banking Supervision) expanded at §2 C3. DBR (Drum-Buffer-Rope) expanded at §5. EBA (European Banking Authority) expanded at §5. AI (Artificial Intelligence) expanded at §6 Open Questions first narrative prose use. Conway's Law: named law, not an initialism; bound to authoritative URL on first use. No bare acronyms found unexpanded at first narrative prose use.
claim_label_audit: all factual and inferential claims carry [fact], [inference], or [assumption] labels with URL-backed sources; §2 C2 causal claim corrected from [fact] to [inference]; §2 B1 healthcare scope narrowed to SRE and SCM only.
parity_check: §6 Key Findings and Findings section Key Findings are mirrored including cross-reference additions to KF1 and KF5.
source_url_audit: all sources carry URL or DOI; no bare source names without URLs; Analysis citation corrected from "all §2 citations collectively" to explicit URL list.
cross_item_audit: do-mode-demand-persistence cited at KF1 and §2 B1; governance-failure-mechanisms-bureaucracy-circumvention cited at KF5 and §5 behavioural lens; both moved from related: to cites: in frontmatter.
bold_audit: Key Findings numbered list items use plain text; bold reserved for claim-label headers and section-subsection labels only.
em_dash_scan: no em-dashes present.
ai_slop_scan: no "Furthermore", "Additionally", "It is important to note", "In conclusion", "Importantly" found.
vague_quantifier_scan: all quantitative claims are bounded inferences or sourced facts; no unsourced "many" or "most" without qualification.
scope_guardrail: maintained; no net-new primary investigations.
```

---

## Findings

### Executive Summary

In a split-authority environment, the dominant flow constraint is governance-generated queueing rather than capacity shortage, and the operating model that most reliably improves throughput while reducing delivery risk combines three design elements: demand segmentation into risk-appropriate lanes, bounded delegation of high-frequency execution decisions to delivery teams, and a named integrator with real budget-recommendation, prioritisation, and escalation authority. [inference; source: https://www.tocinstitute.org/five-focusing-steps.html; https://dora.dev/capabilities/loosely-coupled-teams/; https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html] The key mechanism is proportionate control intensity: pre-approval is reserved for novel or high-consequence decisions, while standard and reversible work travels fast-path lanes with post-hoc audit, and this pattern is structurally consistent with both flow theory and regulatory governance requirements. [inference; source: https://ageconsearch.umn.edu/record/294665/files/ipr018.pdf; https://www.bis.org/bcbs/publ/d328.pdf; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html] Monitoring four leading indicator families (queue health, exception volume, lead time trends, rework and incident load) enables trigger-based control regime shifts that prevent throughput collapse without requiring static control rules. [inference; source: https://dora.dev/guides/dora-metrics-four-keys/; https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387] The confidence level is medium because the synthesis is grounded in mechanism and direction evidence from completed repository items rather than primary cross-firm experimental comparisons of split-authority operating models. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html]

### Key Findings

1. Governance-generated queueing, specifically approval latency, multi-party coordination overhead, and fragmented decision rights, is the dominant flow constraint in split-authority delivery systems, and adding headcount to non-constraints does not improve system-level throughput. ([inference]; medium confidence; source: https://www.tocinstitute.org/five-focusing-steps.html; https://davidamitchell.github.io/Research/research/2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate.html; https://dora.dev/capabilities/loosely-coupled-teams/; https://davidamitchell.github.io/Research/research/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.html)

2. Little's Law implies that excess Work in Progress (WIP) extends lead time and reduces predictability, so controlling the work entry rate into split-authority queues is a prerequisite for throughput improvement rather than a scheduling convenience. ([inference]; high confidence; source: https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387; https://davidamitchell.github.io/Research/research/2026-05-09-build-vs-improve-throughput-tradeoff.html)

3. A three-class demand segmentation that assigns standard reversible work to a fast path with post-hoc audit, routine bounded work to a standard path with lightweight pre-approval or bounded delegation, and novel or high-consequence work to an exception path with full pre-approval, prevents exception work from contaminating routine flow lanes without creating unsustainable classification overhead. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-16-variance-control-comparison-across-delivery-modes.html; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html)

4. High-frequency execution decisions including daily sequencing, minor scope adjustment, local environment spend, and incident response should be delegated to delivery teams because centralised pre-approval of these decisions generates approval-queue congestion without a risk-reduction return proportionate to the coordination cost incurred. ([inference]; medium confidence; source: https://dora.dev/capabilities/loosely-coupled-teams/; https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html; https://www.bain.com/insights/decisions-who-does-what/)

5. Pre-approval controls minimise coordination cost only when reserved for transactions with high uncertainty, high consequence, or high relationship-specific investment; applying pre-approval uniformly to all demand converts governance from a coordination aid into the primary throughput constraint and generates workaround and circumvention behaviour among teams that experience controls as coercive barriers to legitimate work. ([inference]; medium confidence; source: https://ageconsearch.umn.edu/record/294665/files/ipr018.pdf; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html; https://eric.ed.gov/?id=EJ525938; https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html)

6. Banking supervisory guidance requires control intensity to be proportionate to risk profile and all material responsibilities to have named owners with escalation paths, which is structurally consistent with the three-class segmentation and named-integrator requirement and sets the minimum compliance standard for the authority bundle. ([fact]; high confidence; source: https://www.bis.org/bcbs/publ/d328.pdf; https://www.eba.europa.eu/sites/default/files/document_library/Publications/Guidelines/2021/1016721/Final%20report%20on%20Guidelines%20on%20internal%20governance%20under%20CRD.pdf)

7. An integrator without budget-recommendation rights, explicit escalation authority, and a benefits-reporting mandate remains only a coordinator and will reproduce queue-fragmentation and cost-shifting failure patterns observed across multiple completed repository items in this corpus. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-16-governance-structures-build-mode-without-full-accountability-colocation.html; https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html)

8. Conway's Law and Team Topologies research jointly imply that authority fragmentation embeds itself in delivery-system dependency coupling, so a governance redesign that does not address team boundary alignment will face recurring re-emergence of the same coordination queues it was intended to eliminate. ([inference]; medium confidence; source: https://www.melconway.com/Home/Conways_Law.html; https://teamtopologies.com/key-concepts; https://dora.dev/capabilities/loosely-coupled-teams/)

9. Four leading indicator families provide early warning of throughput destabilisation in split-authority systems: queue health as WIP age and blocked-work ratio, exception volume as the Class 3 share of total intake, lead time trends as a multi-week moving average, and rework and incident load as the share of team capacity consumed by remediation activities. ([inference]; medium confidence; source: https://dora.dev/guides/dora-metrics-four-keys/; https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387; https://sre.google/workbook/eliminating-toil/)

10. Trigger-based control regime adjustments, meaning shifts between fast-path, standard, and exception lanes governed by persistent indicator threshold breaches, are more defensible than fixed allocation rules because they respond to actual flow state rather than to a fixed schedule, consistent with the Theory of Constraints constraint-elevation step. ([inference]; medium confidence; source: https://www.tocinstitute.org/five-focusing-steps.html; https://davidamitchell.github.io/Research/research/2026-05-09-build-vs-improve-throughput-tradeoff.html; https://dora.dev/guides/dora-metrics-four-keys/)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Governance-generated queueing is the dominant flow constraint in split-authority delivery. | https://www.tocinstitute.org/five-focusing-steps.html; https://davidamitchell.github.io/Research/research/2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate.html; https://dora.dev/capabilities/loosely-coupled-teams/; https://davidamitchell.github.io/Research/research/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.html | medium | Mechanism strongly evidenced; no primary cross-firm comparison. |
| [inference] Excess WIP extends lead time and reduces predictability per Little's Law. | https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387; https://davidamitchell.github.io/Research/research/2026-05-09-build-vs-improve-throughput-tradeoff.html | high | Classic queueing result; well established. |
| [inference] Three-class demand segmentation prevents exception contamination without unsustainable overhead. | https://davidamitchell.github.io/Research/research/2026-05-16-variance-control-comparison-across-delivery-modes.html; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html | medium | Segmentation logic supported; exact class boundaries need calibration. |
| [inference] High-frequency execution decisions should be delegated to delivery teams. | https://dora.dev/capabilities/loosely-coupled-teams/; https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html; https://www.bain.com/insights/decisions-who-does-what/ | medium | Supported by DORA and decision-rights literature. |
| [inference] Pre-approval minimises coordination cost only for high-uncertainty, high-consequence transactions; uniform pre-approval generates workaround behaviour. | https://ageconsearch.umn.edu/record/294665/files/ipr018.pdf; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html; https://eric.ed.gov/?id=EJ525938; https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html | medium | Transaction-cost logic; enabling vs coercive distinction. |
| [fact] Banking supervisory guidance requires proportionate control intensity and named responsibilities with escalation. | https://www.bis.org/bcbs/publ/d328.pdf; https://www.eba.europa.eu/sites/default/files/document_library/Publications/Guidelines/2021/1016721/Final%20report%20on%20Guidelines%20on%20internal%20governance%20under%20CRD.pdf | high | Direct supervisory requirement. |
| [inference] An integrator without real authority bundle reproduces queue-fragmentation failure. | https://davidamitchell.github.io/Research/research/2026-05-16-governance-structures-build-mode-without-full-accountability-colocation.html; https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html | medium | Supported across multiple completed items. |
| [inference] Authority fragmentation embeds in dependency coupling per Conway's Law. | https://www.melconway.com/Home/Conways_Law.html; https://teamtopologies.com/key-concepts; https://dora.dev/capabilities/loosely-coupled-teams/ | medium | Strongly directional; no controlled comparison. |
| [inference] Four indicator families (queue health, exception volume, lead time trends, rework load) provide early destabilisation warning. | https://dora.dev/guides/dora-metrics-four-keys/; https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387; https://sre.google/workbook/eliminating-toil/ | medium | Indicator logic grounded in DORA, Little, and SRE. |
| [inference] Trigger-based regime shifts are more defensible than fixed allocation rules. | https://www.tocinstitute.org/five-focusing-steps.html; https://davidamitchell.github.io/Research/research/2026-05-09-build-vs-improve-throughput-tradeoff.html; https://dora.dev/guides/dora-metrics-four-keys/ | medium | ToC constraint-elevation logic applied to control regimes. |

### Assumptions

- The dominant flow constraint in a specific organisation's split-authority environment is governance-generated queueing rather than raw capacity. Organisations where headcount is genuinely the bottleneck should address the capacity constraint first before redesigning governance. [assumption; source: https://www.tocinstitute.org/five-focusing-steps.html; https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html]
- The three demand classes map to work types that the organisation can distinguish at intake. If classification is infeasible due to information asymmetry at intake, the segmentation approach requires a dedicated triage step. [assumption; source: https://davidamitchell.github.io/Research/research/2026-05-16-variance-control-comparison-across-delivery-modes.html]
- The named integrator can be credibly empowered with budget-recommendation rights in the organisation's governance structure. In organisations where budget authority is entirely held by a central finance committee, the integrator model would need to be adapted to whatever authority form is available. [assumption; source: https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html; https://www.bis.org/bcbs/publ/d328.pdf]

### Analysis

The causal chain in split-authority delivery runs from fragmented decision rights through approval-gate queueing to WIP accumulation, lead time extension, and throughput loss. [inference; source: https://www.tocinstitute.org/five-focusing-steps.html; https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387; https://davidamitchell.github.io/Research/research/2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate.html] The operating model recommendation directly targets each step in this chain: demand segmentation limits the proportion of work that enters the constrained approval gate; bounded delegation (delegation within defined guardrails with pre-agreed escalation paths) removes high-frequency low-consequence decisions from the constraint entirely; the named integrator prevents authority diffusion from recreating fragmentation; and the indicator bundle provides early warning before the chain reaches failure. [inference; source: https://www.tocinstitute.org/five-focusing-steps.html; https://dora.dev/capabilities/loosely-coupled-teams/; https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html; https://dora.dev/guides/dora-metrics-four-keys/]

A plausible rival model is to increase the pre-approval gate's capacity by adding reviewers rather than redesigning the governance structure. The ToC evidence contradicts this as a complete solution: adding capacity to the constraint can help at the margin, but it does not address the root cause, which is that approval-by-exception (a control pattern where standard work is delegated with post-hoc audit and only exceptional work triggers pre-approval review) and demand segmentation could eliminate most of the queue rather than just widen the bottleneck. [inference; source: https://www.tocinstitute.org/five-focusing-steps.html; https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html]

A second rival model is to rely on stronger model-quality gates or automated testing to reduce delivery risk without changing the governance structure. This is complementary rather than rival: automated gates in the fast path are exactly how Class 1 work achieves acceptable risk at high speed. The recommendation does not exclude automated controls; it assigns them to the appropriate lane. [inference; source: https://dora.dev/guides/dora-metrics-four-keys/; https://davidamitchell.github.io/Research/research/2026-05-16-variance-control-comparison-across-delivery-modes.html]

The evidence weights toward the combined five-principle model because each element addresses a distinct failure mechanism identified across multiple completed repository items, and the elements reinforce each other: demand segmentation only works if the integrator can enforce classification discipline; bounded delegation only works if the indicator bundle detects when thresholds are breached; the trigger-based regime shift only works if the integrator has authority to act. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html; https://davidamitchell.github.io/Research/research/2026-05-16-governance-structures-build-mode-without-full-accountability-colocation.html]

### Risks, Gaps, and Uncertainties

- Threshold values for the four leading indicator families must be calibrated empirically; the evidence base does not supply universal trigger numbers. [inference; source: https://dora.dev/research/2025/measurement-frameworks/; https://dora.dev/guides/dora-metrics-four-keys/]
- The Q1-Q6 dependency items have not been completed as primary research items; this synthesis uses completed repository items as proxies. A future cycle completing Q1-Q6 could validate, refine, or contradict these conclusions. [assumption; source: https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html]
- The evidence base is strongest for mechanism and direction; it does not supply cross-firm empirical comparisons of operating model variants that would support high-confidence claims about outcome magnitudes or transition timelines. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html]
- The three-lane classification requires intake-stage information about work risk and reversibility. In environments where this information is not reliably available at intake, the segmentation model will misroute work and degrade throughput rather than improve it. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-16-variance-control-comparison-across-delivery-modes.html]

### Open Questions

- Which specific WIP-age and exception-volume thresholds best predict irreversible queue collapse in split-authority regulated enterprises?
- What is the minimum viable integrator authority bundle in organisations where budget authority cannot be delegated below a central finance committee?
- How does the three-lane segmentation interact with AI-assisted delivery acceleration: do AI throughput gains shift the proportion of work that reaches exception-path classification?
- Should new backlog items be created for Q1-Q6 to answer the sub-questions as primary research items and validate this synthesis against empirical evidence?

### Output

- Type: knowledge
- Description: Synthesis of flow-theory, governance, and decision-rights evidence into a five-principle operating model for split-authority delivery environments, showing that governance-generated queueing is the dominant constraint and that demand segmentation, bounded delegation, a named integrator, and trigger-based leading indicators form the minimum viable response. [inference; source: https://www.tocinstitute.org/five-focusing-steps.html; https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html]
- Links:
  - https://www.tocinstitute.org/five-focusing-steps.html
  - https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html
  - https://dora.dev/guides/dora-metrics-four-keys/
