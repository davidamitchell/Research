---
review_count: 2
title: "Q1: Dominant flow constraint in split-authority delivery systems"
added: 2026-05-29
status: completed
priority: high
tags: [constraint-analysis, flow, governance, queueing]
blocks: []
started: 2026-05-31T21:21:16+00:00
completed: 2026-05-31T21:55:02+00:00
output: [knowledge]
cites:
  - 2026-04-01-backpressure-theory-of-constraints
  - 2026-05-29-split-authority-p1-operating-model-synthesis
  - 2026-05-23-governance-controls-effectiveness-conditions
  - 2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention
  - 2026-05-23-funding-authority-delivery-capability-risk-accountability-split
  - 2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate
  - 2026-05-14-org-failure-modes-cohort-demand-domain-it
related:
  - 2026-05-29-split-authority-q2-demand-segmentation
  - 2026-05-29-split-authority-q3-routing-exception-isolation
  - 2026-05-29-split-authority-q4-decision-rights-placement
  - 2026-05-29-split-authority-q5-control-model-tradeoff
  - 2026-05-29-split-authority-q6-instability-leading-indicators
supersedes: ~
superseded_by: []
item_type: primary
confidence: medium
themes:
  - governance-policy
  - organisational-design
  - cost-performance
  - software-engineering
versions:
  - version: "1.0"
    sha: 3ce7ba6
    changed: "2026-05-31"
    progress: progress/2026-05-31-split-authority-q1-flow-constraint.md
    summary: "Initial completion"
---

# Q1: Dominant flow constraint in split-authority delivery systems

## Research Question

What is the dominant source of delay and instability in split-authority delivery systems: capacity shortage, dependency coupling, approval latency, funding gates, or fragmented decision rights?

A split-authority delivery system is one in which no single actor owns risk, cost, and execution simultaneously, meaning authority is divided among at least two stakeholder groups, each with independent veto or approval power, typically a business owner, a technology delivery team, and an independent risk or compliance function.

## Scope

**In scope:**
- Comparative assessment of technical versus governance-generated queueing.
- Evidence on where delay and instability concentrate in split-authority flow.
- The Theory of Constraints (TOC) distinction between physical constraints (capacity, headcount, tooling) and policy constraints (approval rules, funding cycles, governance requirements).

**Out of scope:**
- Prescribing full control-model redesign before root constraint identification.
- Sector-specific procurement law or jurisdiction-specific regulation detail.

**Constraints:**
- Distinguish local bottlenecks from system-level throughput constraints.
- Keep the analysis at the level of mechanism and direction evidence, not precise quantitative prediction.

## Context

Q1 establishes the true constraint and removes overlap between capacity, governance delay, and decision-right fragmentation. It enables Q2, Q3, Q4, Q6, and P1. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html]

## Approach

1. Define candidate constraint categories and observable indicators.
2. Review evidence linking each category to throughput and instability outcomes.
3. Rank dominant constraints under common split-authority conditions.

## Sources

- [x] [DORA (2019) Streamlining Change Approval](https://dora.dev/capabilities/streamlining-change-approval/) - canonical DevOps Research and Assessment (DORA) guidance on change approval processes and their effect on software delivery performance.
- [x] [DORA (2019) State of DevOps Report](https://dora.dev/research/2019/dora-report/) - survey-based report finding that external change approval is negatively correlated with software delivery performance.
- [x] [DORA Loosely Coupled Teams](https://dora.dev/capabilities/loosely-coupled-teams/) - DORA capability page on architectural and organisational conditions associated with high delivery performance.
- [x] [DORA Metrics: The Four Keys](https://dora.dev/guides/dora-metrics-four-keys/) - DORA definition of throughput and instability metrics for software delivery.
- [x] [Theory of Constraints Institute: Five Focusing Steps](https://www.tocinstitute.org/five-focusing-steps.html) - canonical description of the Theory of Constraints Process of Ongoing Improvement (POOGI).
- [x] [Org Topologies case study: component teams to Team Topologies](https://www.orgtopologies.com/post/case-study-from-component-teams-to-team-topologies-to-fast-agile) - case study reporting 97% waste or wait time under a tightly coupled component-team architecture.
- [x] [Mitchell (2026) Backpressure Infrastructure and the Theory of Constraints](https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html) - prior completed repository item on TOC mechanisms, Drum-Buffer-Rope scheduling, and policy versus physical constraints.
- [x] [Mitchell (2026) Operating model synthesis for split-authority delivery systems](https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html) - prior completed synthesis item identifying governance-generated queueing as the dominant constraint.
- [x] [Mitchell (2026) Governance controls effectiveness conditions](https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html) - prior completed item on when controls minimise versus amplify coordination cost.
- [x] [Mitchell (2026) Governance failure mechanisms and bureaucracy circumvention](https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html) - prior completed item on how controls become overhead and staff circumvent them.
- [x] [Mitchell (2026) Funding authority and delivery-risk accountability split](https://davidamitchell.github.io/Research/research/2026-05-23-funding-authority-delivery-capability-risk-accountability-split.html) - prior completed item on the delivery consequences of separating funding authority from delivery accountability.
- [x] [Mitchell (2026) IT throughput constraint magnitude and debt accumulation rate](https://davidamitchell.github.io/Research/research/2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate.html) - prior completed item on throughput constraints and their relationship to shadow IT demand.
- [x] [Mitchell (2026) Organisational failure modes: customer-segment demand versus domain-based IT teams](https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-cohort-demand-domain-it.html) - prior completed item on boundary-mismatch delivery bottlenecks.

---

## Research Skill Output

### §0 Initialise

Question: What is the dominant source of delay and instability in split-authority delivery systems: capacity shortage, dependency coupling, approval latency, funding gates, or fragmented decision rights?

Scope: Comparative assessment of technical versus governance-generated queueing; evidence on where delay and instability concentrate; TOC distinction between physical and policy constraints. Out of scope: control-model redesign, jurisdiction-specific regulatory detail.

Constraints: Distinguish local bottlenecks from system-level constraints; keep analysis at mechanism and direction evidence level.

Output format: Full research skill output (§0-§7) written into this section, then Findings section populated from §6.

Prior work check: Multiple completed repository items directly address this question from different angles. `2026-04-01-backpressure-theory-of-constraints` establishes the TOC framework and the policy-versus-physical-constraint distinction. `2026-05-29-split-authority-p1-operating-model-synthesis` synthesises the answer at the system level (governance-generated queueing as dominant constraint). `2026-05-23-governance-controls-effectiveness-conditions` and `2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention` characterise when approval controls amplify rather than reduce cost. `2026-05-23-funding-authority-delivery-capability-risk-accountability-split` covers the specific failure mode when budget authority and delivery accountability are separated. `2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate` and `2026-05-14-org-failure-modes-cohort-demand-domain-it` cover capacity and boundary-mismatch patterns. DORA research (consulted directly) provides the most robust external empirical evidence base for the approval latency finding.

### §1 Question Decomposition

Atomic sub-questions:

**A. What are the five candidate constraint categories and their observable indicators?**
A1. What constitutes a capacity shortage constraint and how does it manifest?
A2. What constitutes a dependency coupling constraint and how does it manifest?
A3. What constitutes an approval latency constraint and how does it manifest?
A4. What constitutes a funding gate constraint and how does it manifest?
A5. What constitutes a fragmented decision rights constraint and how does it manifest?

**B. What does the Theory of Constraints say about constraint types and hierarchy?**
B1. How does TOC define the distinction between a physical constraint and a policy constraint?
B2. What does TOC say about the relative frequency and impact of policy constraints in knowledge-work systems?

**C. What is the empirical evidence for each candidate constraint as a throughput limiter?**
C1. What evidence exists that approval latency is a system-level throughput constraint?
C2. What evidence exists that fragmented decision rights amplify throughput loss?
C3. What evidence exists that dependency coupling compounds the above?
C4. What evidence exists that funding gates create throughput instability?
C5. What evidence exists that capacity shortage is the dominant constraint in split-authority systems?

**D. How do the five categories interact -- are they independent or does one cause the others?**
D1. Is capacity shortage typically masked by governance queueing?
D2. Is dependency coupling an amplifier of approval latency or an independent constraint?
D3. Are funding gates a distinct constraint or a coarser-cycle form of approval latency?

**E. What is the dominant rank ordering under typical split-authority conditions?**
E1. Which constraint category, when removed, produces the largest throughput improvement?

### §2 Investigation

**A1. Capacity shortage as a constraint category**

[fact] A physical capacity shortage constraint in delivery means the team's aggregate execution bandwidth (headcount, tooling, compute, working time) is the binding rate limiter: demand exceeds supply at a sustained level that produces growing backlog independent of governance decisions. Indicators include consistent overtime, declining throughput despite stable governance overhead, and backlogs that grow during periods of low approval activity. Source: [TOC Institute, Five Focusing Steps](https://www.tocinstitute.org/five-focusing-steps.html).

[inference] Capacity shortage is the constraint that governance-heavy organisations typically assume is primary, but the assumption often persists without the diagnostic step of removing governance friction to test whether throughput increases. Source: [Mitchell (2026) Backpressure and TOC](https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html); [Mitchell (2026) IT throughput constraint](https://davidamitchell.github.io/Research/research/2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate.html).

**A2. Dependency coupling as a constraint category**

[fact] Dependency coupling creates throughput constraints when work items cannot proceed until another team provides a component, decision, or integration result, creating synchronisation queues across team boundaries. Observable indicators include cross-team work-in-progress (WIP) accumulation, blocked tickets, and lead time spikes that cluster at inter-team handoffs. Source: [DORA, Loosely Coupled Teams](https://dora.dev/capabilities/loosely-coupled-teams/).

[inference] Dependency coupling is structurally generated by the same organisational boundaries that produce split authority: a team that cannot independently deploy or decide is also dependent on adjacent teams for approvals and integrations. The coupling is therefore correlated with, and partly caused by, the governance structure rather than being an independent constraint category. Source: [DORA, Loosely Coupled Teams](https://dora.dev/capabilities/loosely-coupled-teams/); [Mitchell (2026) Org failure modes: cohort demand vs domain IT](https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-cohort-demand-domain-it.html).

**A3. Approval latency as a constraint category**

[fact] Approval latency is the elapsed time between a work item reaching an approval node and the approval decision being issued. It creates a queue whose depth is determined by the arrival rate of items versus the review bandwidth, batching frequency (weekly or monthly committee cycles), and decision criteria clarity. Source: [DORA, Streamlining Change Approval](https://dora.dev/capabilities/streamlining-change-approval/).

[fact] DORA's research finds that external change approvals, meaning approvals issued by parties outside the team proposing the change, are negatively correlated with all four software delivery performance metrics: change lead time, deployment frequency, change failure rate, and time to restore service. The 2019 State of DevOps Report explicitly states that heavyweight external approval processes slow delivery, produce larger batch releases, and are associated with higher, not lower, change failure rates. Source: [DORA, Streamlining Change Approval](https://dora.dev/capabilities/streamlining-change-approval/); [DORA 2019 State of DevOps Report](https://dora.dev/research/2019/dora-report/).

[inference] Approval latency is a policy constraint in the TOC sense: it is not a physical limitation of execution bandwidth but a rule-based requirement that work must pass through a review node before proceeding. Policy constraints can act as throughput ceilings even when physical capacity is sufficient. Source: [TOC Institute, Five Focusing Steps](https://www.tocinstitute.org/five-focusing-steps.html); [Mitchell (2026) Backpressure and TOC](https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html).

**A4. Funding gates as a constraint category**

[fact] Funding gates require work items to obtain capital or operating-expenditure approval from a budget authority before the delivery team can act. Unlike continuous approval latency, funding gates operate at coarser cycle times (annual, quarterly, or milestone-based), creating periodic release of authority rather than item-by-item queuing. Source: [Mitchell (2026) Funding authority and delivery-risk accountability split](https://davidamitchell.github.io/Research/research/2026-05-23-funding-authority-delivery-capability-risk-accountability-split.html).

[inference] Funding gates are a specific form of approval latency at budget-cycle frequency. Their throughput effect is most acute at the start of budget periods (when scope cannot begin until the gate opens) and at mid-cycle changes (when out-of-scope demand accumulates in a backlog that can only be addressed at the next gate). They are not mechanistically distinct from approval latency; they differ only in cycle time and in the class of authority required. Source: [Mitchell (2026) Funding authority and delivery-risk accountability split](https://davidamitchell.github.io/Research/research/2026-05-23-funding-authority-delivery-capability-risk-accountability-split.html); [Mitchell (2026) Governance controls effectiveness conditions](https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html).

**A5. Fragmented decision rights as a constraint category**

[fact] Fragmented decision rights exist when no single actor has sufficient authority to commit to a course of action, requiring multi-party consensus or sequential sign-off chains. Each actor in the chain adds an approval node; each approval node introduces a waiting queue. Source: [Mitchell (2026) Funding authority and delivery-risk accountability split](https://davidamitchell.github.io/Research/research/2026-05-23-funding-authority-delivery-capability-risk-accountability-split.html); [DORA, Loosely Coupled Teams](https://dora.dev/capabilities/loosely-coupled-teams/).

[inference] Fragmented decision rights are the organisational root cause of approval latency: the reason items queue at approval nodes is that decision authority is not located with the team executing the work. Where decision rights are consolidated with delivery accountability, the approval queue disappears because the team both does the work and makes the commitment. Where rights are fragmented, every substantive decision travels through a multi-party circuit, each leg of which adds elapsed time. Source: [Mitchell (2026) Governance controls effectiveness conditions](https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html); [Mitchell (2026) Operating model synthesis P1](https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html).

**B1. TOC distinction between physical and policy constraints**

[fact] TOC defines a physical constraint as a tangible resource whose capacity limits system throughput: a machine, a team, a data pipeline. TOC defines a policy constraint as a rule, procedure, or governance requirement that prevents the system from running at its physical capacity. TOC explicitly identifies policy constraints as common, often dominant, and more impactful than physical constraints because they are invisible to standard capacity analysis. Source: [TOC Institute, Five Focusing Steps](https://www.tocinstitute.org/five-focusing-steps.html); [Mitchell (2026) Backpressure and TOC](https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html).

**B2. TOC on policy constraints in knowledge work**

[inference] TOC practitioners note that in manufacturing, the constraint is often physical (a machine or process step). In knowledge work, including software delivery, the constraint is more often a policy: a review cadence, an approval chain, or a governance requirement. Goldratt's Five Focusing Steps warn explicitly against elevating capacity (adding resources) before exploiting and subordinating non-constraint activity to the actual constraint, noting that premature capacity investment frequently reveals hidden capacity that already exists but is blocked by policy rather than absent. Source: [TOC Institute, Five Focusing Steps](https://www.tocinstitute.org/five-focusing-steps.html); [Mitchell (2026) Backpressure and TOC](https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html).

**C1. Empirical evidence for approval latency as a system-level throughput constraint**

[fact] DORA's multi-year, multi-firm research program finds that teams relying on external Change Advisory Board (CAB) approval or senior-manager sign-off for changes perform worse on all delivery metrics. The mechanism is that heavyweight approval causes work to batch into larger releases less frequently, which increases blast radius and, paradoxically, change failure rates. Source: [DORA, Streamlining Change Approval](https://dora.dev/capabilities/streamlining-change-approval/).

[fact] The Org Topologies case study based on James Shore's analysis of a 200-engineer, 300-person research and development (R&D) organisation with tightly coupled component teams found that value stream mapping (VSM) analysis showed 97% waste or wait time: work requiring 2 to 3 days of actual effort consumed months of calendar time. Active processing time accounted for approximately 3% of total elapsed cycle time. Source: [Org Topologies case study](https://www.orgtopologies.com/post/case-study-from-component-teams-to-team-topologies-to-fast-agile).

[inference] Queueing theory predicts that queue length and therefore lead time grows non-linearly as an approval node approaches its review-bandwidth capacity. In governance-heavy organisations, approval nodes (committees, boards, sign-off chains) frequently operate near or above their capacity, meaning that small reductions in approval frequency or complexity produce disproportionately large improvements in lead time. Source: [DORA, Streamlining Change Approval](https://dora.dev/capabilities/streamlining-change-approval/); [DORA Metrics Four Keys](https://dora.dev/guides/dora-metrics-four-keys/).

**C2. Empirical evidence for fragmented decision rights amplifying throughput loss**

[fact] DORA research shows that high-performing teams can make large-scale changes to their systems without requiring permission from someone outside the team or depending on other teams. This architectural and organisational independence is one of the most consistent predictors of high software delivery performance. Source: [DORA, Loosely Coupled Teams](https://dora.dev/capabilities/loosely-coupled-teams/).

[inference] Fragmented decision rights directly prevent this independence. When delivery teams must seek permission from external parties for any significant change, every substantive work item enters an approval queue. The more granular the decision-rights fragmentation (multiple veto holders, each responsible for a different risk domain), the more approval nodes each item passes through, and the longer the cumulative latency. Source: [Mitchell (2026) Governance controls effectiveness conditions](https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html); [Mitchell (2026) Funding authority and delivery-risk accountability split](https://davidamitchell.github.io/Research/research/2026-05-23-funding-authority-delivery-capability-risk-accountability-split.html).

**C3. Empirical evidence for dependency coupling as a compounding factor**

[fact] DORA's research on loosely coupled teams shows that tightly coupled architectures require teams to coordinate constantly with other teams, creating "complex and bureaucratic change management processes." Organisations that cannot test or deploy independently cannot achieve high delivery performance regardless of their capacity levels. Source: [DORA, Loosely Coupled Teams](https://dora.dev/capabilities/loosely-coupled-teams/).

[inference] Dependency coupling compounds approval latency because each cross-team dependency creates at least one additional approval node (the receiving team's capacity planning or commitment process). A tightly coupled system with split authority therefore has both a direct approval queue (governance approval) and indirect approval queues (cross-team dependency scheduling). Removing one without the other produces partial improvement. Source: [DORA, Loosely Coupled Teams](https://dora.dev/capabilities/loosely-coupled-teams/); [Org Topologies case study](https://www.orgtopologies.com/post/case-study-from-component-teams-to-team-topologies-to-fast-agile).

**C4. Evidence for funding gates as a throughput instability source**

[inference] Funding gates create throughput instability by periodically stopping and starting work streams. During gate closure, demand accumulates as a batch; when the gate opens, a large volume of work enters the delivery system simultaneously, creating a demand spike that overwhelms execution capacity even when governance approval is not the steady-state bottleneck. This batch arrival pattern produces the same non-linear queue blowout as any large-batch arrival in a queueing system operating near capacity. Source: [Mitchell (2026) Funding authority and delivery-risk accountability split](https://davidamitchell.github.io/Research/research/2026-05-23-funding-authority-delivery-capability-risk-accountability-split.html); [Mitchell (2026) Operating model synthesis P1](https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html).

**C5. Evidence on capacity shortage as the dominant constraint**

[inference] No robust empirical study establishes capacity shortage, meaning insufficient engineering headcount or execution tooling, as the primary throughput constraint in split-authority delivery systems in preference to approval latency. DORA's research program, which spans tens of thousands of responses over multiple years, identifies delivery performance predictors as predominantly organisational and architectural (team autonomy, loose coupling, deployment pipeline automation) rather than raw capacity. Source: [DORA, Streamlining Change Approval](https://dora.dev/capabilities/streamlining-change-approval/); [DORA, Loosely Coupled Teams](https://dora.dev/capabilities/loosely-coupled-teams/).

[inference] Capacity shortage is often visible but not primary for two reasons. First, governance overhead consumes a share of available capacity on non-delivery activities (preparing approval packs, attending review meetings, responding to audit queries), artificially reducing effective delivery throughput. Second, the governance queue masks the signal: when items sit in approval queues, utilisation metrics undercount idle delivery capacity, making teams appear more constrained than they are. Removing the governance constraint typically reveals latent capacity. Source: [TOC Institute, Five Focusing Steps](https://www.tocinstitute.org/five-focusing-steps.html); [Mitchell (2026) Backpressure and TOC](https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html).

**D. Interaction between the five constraint categories**

[inference] Approval latency and fragmented decision rights are not independent; fragmented decision rights are the structural cause of approval latency in split-authority systems. Reducing fragmented decision rights (consolidating commitment authority with delivery accountability) removes the approval queue at its root. Dependency coupling amplifies both, because each cross-team dependency adds an additional approval node to the item's path. Funding gates are a coarser-cycle variant of approval latency. Capacity shortage is partially endogenous: governance overhead consumes capacity, and the governance queue hides available capacity. The causal chain runs: fragmented decision rights produce approval latency, which accumulates into governance-generated queueing; dependency coupling multiplies the number of approval nodes each item crosses; funding gates periodically batch-release demand into a system whose steady-state governance queues are already constraining flow. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html; https://dora.dev/capabilities/loosely-coupled-teams/; https://www.tocinstitute.org/five-focusing-steps.html]

**E. Dominant rank ordering under typical split-authority conditions**

[inference] Based on the convergent evidence: (1) approval latency and its root cause, fragmented decision rights, is the dominant policy constraint; (2) dependency coupling is the primary amplifier; (3) funding gates are a coarser-cycle variant of the dominant constraint; (4) capacity shortage is secondary and partially endogenous to the governance overhead itself. Addressing capacity shortage before reducing governance friction is the most common misdiagnosis in split-authority delivery systems. [inference; source: https://dora.dev/capabilities/streamlining-change-approval/; https://www.tocinstitute.org/five-focusing-steps.html; https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html]

### §3 Reasoning

Removing narrative connectors:

1. Approval latency is a policy constraint in the TOC sense. [inference; source: https://www.tocinstitute.org/five-focusing-steps.html]
2. DORA multi-firm research confirms external approval is negatively correlated with all delivery performance metrics. [fact; source: https://dora.dev/capabilities/streamlining-change-approval/]
3. A single VSM case study (Org Topologies, 200-engineer organisation) found 97% of cycle time was wait time in an approval-dependent component-team structure. [fact; source: https://www.orgtopologies.com/post/case-study-from-component-teams-to-team-topologies-to-fast-agile]
4. Fragmented decision rights are the structural cause of approval latency, not an independent variable. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html]
5. Dependency coupling multiplies approval-node crossings, amplifying latency proportionally to coupling density. [inference; source: https://dora.dev/capabilities/loosely-coupled-teams/]
6. Funding gates are approval latency at budget-cycle granularity; their instability effect is the batch demand spike at gate opening. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-funding-authority-delivery-capability-risk-accountability-split.html]
7. Capacity shortage is partially endogenous: governance overhead consumes capacity and the approval queue hides latent capacity. [inference; source: https://www.tocinstitute.org/five-focusing-steps.html]
8. Therefore, the dominant system-level throughput constraint in split-authority delivery is governance-generated queueing produced by approval latency and fragmented decision rights. [inference; source: https://dora.dev/capabilities/streamlining-change-approval/; https://www.tocinstitute.org/five-focusing-steps.html; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html]

### §4 Consistency Check

```text
contradiction_scan: none_found
  -- All five candidate categories converge on approval latency and fragmented decision rights as
     co-dominant. No source supports capacity shortage as the primary constraint in split-authority systems.
  -- DORA and TOC evidence are mutually consistent: TOC predicts policy constraints will dominate in
     knowledge work; DORA empirically confirms that policy-type constraints (external approval)
     are the measured delivery performance suppressors.
scope_guardrail: maintained
  -- No control-model redesign recommendations in §2; constraint identification only.
confidence_adjustment: medium
  -- Evidence is predominantly observational and secondary (DORA survey, VSM case studies, TOC theory).
     No primary cross-firm randomised experiment on split-authority organisations specifically.
     Direction is strongly supported; precise magnitude of each constraint's relative contribution is not.
```

### §5 Depth and Breadth Expansion

**Technical lens**: Queueing theory (Little's Law as stated by J.D.C. Little in 1961) states that mean cycle time equals mean WIP divided by mean throughput. In systems where work items queue at multiple approval nodes, WIP accumulates across all nodes simultaneously, and the cycle time for any single item is the sum of all queue waits plus actual processing time. When approval nodes run near capacity saturation, the non-linear relationship between utilisation and queue depth (established in queuing theory for M/M/1 queues) means that relatively small increases in approval workload produce very large increases in cycle time. This mechanism explains why split-authority organisations can appear to have adequate delivery capacity while simultaneously experiencing very long lead times: the capacity is present but blocked behind governance queues. [inference; source: https://dora.dev/guides/dora-metrics-four-keys/; https://www.tocinstitute.org/five-focusing-steps.html]

**Behavioural lens**: When approval latency is high, teams adapt by batching work into larger submissions to amortise the per-submission wait cost. Large batches increase the blast radius of each change, which increases change failure rate, which makes approvers more cautious, which increases approval cycle time, which reinforces batching. This is a reinforcing feedback loop, not a static constraint. The loop stabilises only when throughput collapses to a level that empties the queue. [inference; source: https://dora.dev/capabilities/streamlining-change-approval/; https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html]

**Regulatory lens**: Regulated enterprises face a minimum floor of mandatory approval for certain change types (segregation of duties, model risk governance, change control for regulated systems). This floor is non-negotiable, but it defines the lower bound of unavoidable approval latency, not the current operating level. Most organisations operate well above this floor because their governance patterns evolved to apply heavyweight controls uniformly rather than proportionately. The gap between the regulatory floor and the actual operating level is the addressable governance overhead. [inference; source: https://dora.dev/capabilities/streamlining-change-approval/; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html]

**Historical lens**: The shift from project-by-project capital expenditure approval to product-level capacity funding in modern digital delivery organisations is a direct response to the throughput cost of funding-gate batching. The completed item on funding authority and delivery-risk accountability split identifies that funding models designed for infrastructure capital expenditure impose inappropriate batching on software delivery, where marginal cost is low and feedback cycles must be short. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-funding-authority-delivery-capability-risk-accountability-split.html]

**Rival explanation check**: Could capacity shortage be primary in some split-authority contexts? Yes, in two specific conditions: (a) a team that is severely understaffed relative to its approval-independent workload will exhibit capacity as the binding constraint, even after governance friction is removed; (b) a team that has successfully reduced governance overhead and restructured decision rights may find that capacity then becomes the next constraint in the TOC sequence. Neither condition is the common case in split-authority organisations that have not yet reduced governance overhead. In those organisations, the approval and decision-rights structure is the first constraint to address. [inference; source: https://www.tocinstitute.org/five-focusing-steps.html; https://dora.dev/capabilities/streamlining-change-approval/]

### §6 Synthesis

**Executive Summary**: In split-authority delivery systems, governance-generated queueing caused by approval latency and fragmented decision rights is the dominant throughput constraint, not capacity shortage. [inference; source: https://dora.dev/capabilities/streamlining-change-approval/; https://www.tocinstitute.org/five-focusing-steps.html] This conclusion is supported by convergent evidence from DORA's multi-firm survey research, Theory of Constraints (TOC) theory and practice, a value stream mapping (VSM) case study showing 97% wait time in a 200-engineer organisation, and completed prior repository work on governance controls and operating model design. [inference; source: https://dora.dev/capabilities/streamlining-change-approval/; https://www.tocinstitute.org/five-focusing-steps.html; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html] Fragmented decision rights are the organisational root cause of approval latency: when no single actor owns risk, cost, and execution simultaneously, every substantive decision must travel through a multi-party circuit, each leg of which adds queue wait time. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html; https://dora.dev/capabilities/loosely-coupled-teams/] Dependency coupling amplifies the effect by increasing the number of approval nodes each work item must cross, and funding gates contribute periodic batch-demand instability as a coarser-cycle variant of the same underlying mechanism. [inference; source: https://www.orgtopologies.com/post/case-study-from-component-teams-to-team-topologies-to-fast-agile; https://davidamitchell.github.io/Research/research/2026-05-23-funding-authority-delivery-capability-risk-accountability-split.html] Capacity shortage is secondary and partially endogenous: governance overhead consumes delivery capacity and the approval queue masks latent capacity that would otherwise be visible. [inference; source: https://www.tocinstitute.org/five-focusing-steps.html; https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html]

**Key Findings**:

1. Approval latency is a policy constraint in the TOC sense, meaning it is rule-imposed rather than capacity-limited, and therefore blocks throughput even when physical execution capacity is sufficient. ([inference]; medium confidence; source: https://www.tocinstitute.org/five-focusing-steps.html; https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html)

2. DORA multi-year, multi-firm survey research finds that external change approval processes are negatively correlated with all four software delivery performance metrics, confirming that governance-type constraints suppress measured delivery performance. ([fact]; medium confidence; source: https://dora.dev/capabilities/streamlining-change-approval/; https://dora.dev/research/2019/dora-report/)

3. Value stream mapping analysis applied to a 200-engineer organisation with tightly coupled component teams found 97% waste or wait time, meaning months of calendar time for work requiring only 2 to 3 days of active effort, demonstrating the system-level magnitude of governance-generated queue latency. ([fact]; medium confidence; source: https://www.orgtopologies.com/post/case-study-from-component-teams-to-team-topologies-to-fast-agile)

4. Fragmented decision rights are the organisational root cause of approval latency in split-authority systems: when no party holds sufficient authority to commit unilaterally, every substantive decision creates a multi-party approval circuit that adds queue time at each step. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html; https://dora.dev/capabilities/loosely-coupled-teams/)

5. Dependency coupling amplifies governance-generated queueing by adding one or more cross-team synchronisation queues to every work item that crosses a team boundary, compounding the total wait time produced by the governance approval chain. ([inference]; medium confidence; source: https://dora.dev/capabilities/loosely-coupled-teams/; https://www.orgtopologies.com/post/case-study-from-component-teams-to-team-topologies-to-fast-agile)

6. Funding gates create throughput instability through a batch demand spike mechanism: demand accumulates during gate closure and enters the delivery system simultaneously at gate opening, overwhelming execution capacity even in organisations with adequate steady-state bandwidth. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-23-funding-authority-delivery-capability-risk-accountability-split.html; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html)

7. Capacity shortage is secondary and partially endogenous in split-authority systems: governance overhead consumes productive delivery capacity and the approval queue conceals latent capacity, so the constraint appears to be execution bandwidth when it is actually governance-generated blocking. ([inference]; medium confidence; source: https://www.tocinstitute.org/five-focusing-steps.html; https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html)

8. TOC warns that addressing capacity shortage before identifying and exploiting the actual constraint is the most common improvement failure: organisations that add headcount without first reducing governance overhead typically find throughput improves less than expected because the governance constraint absorbs the new capacity. ([inference]; medium confidence; source: https://www.tocinstitute.org/five-focusing-steps.html; https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html)

9. The feedback loop between approval latency and large-batch delivery is self-reinforcing: high approval latency incentivises teams to bundle work into fewer, larger submissions, larger batches increase change failure risk, higher failure risk makes approvers more conservative, and conservative approvers extend cycle times further. ([inference]; medium confidence; source: https://dora.dev/capabilities/streamlining-change-approval/; https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html)

10. There is a non-zero minimum approval-latency floor in regulated enterprises set by mandatory controls (segregation of duties, change control for regulated systems), but most split-authority organisations operate substantially above this floor because governance patterns evolved to apply heavyweight controls uniformly rather than proportionately to transaction risk. ([inference]; medium confidence; source: https://dora.dev/capabilities/streamlining-change-approval/; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html)

**Assumptions**:

- The candidate categories (capacity shortage, dependency coupling, approval latency, funding gates, fragmented decision rights) are collectively exhaustive for the purposes of this comparative analysis. An organisation exhibiting primarily technology-failure-induced instability or market-demand collapse is outside the scope defined. [assumption; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html]
- The DORA research base is a reasonable proxy for the "typical split-authority organisation" because the survey spans multiple industries, firm sizes, and governance models and because high governance overhead correlates in the dataset with lower performance. [assumption; source: https://dora.dev/research/2019/dora-report/]

**Risks, Gaps, and Uncertainties**:

- No primary cross-firm experimental study isolates approval latency as the binding constraint in split-authority organisations through direct manipulation. Evidence is observational (DORA survey, VSM case studies) and theoretical (TOC, queueing theory).
- The relative magnitude of each constraint's contribution varies by firm type, regulatory regime, and governance maturity; no public dataset provides precise decomposition.
- In severely understaffed teams, capacity shortage may be the binding constraint independently of governance friction; the secondary status of capacity shortage is a directional claim, not a universal rule.

**Open Questions**:

- At what threshold of governance overhead does capacity shortage become co-dominant with approval latency?
- How do the five constraint categories rank differently in heavily regulated sectors (banking, healthcare, public sector) versus less-regulated technology firms?

**Output**: `knowledge`. This item identifies governance-generated queueing as the dominant flow constraint in split-authority delivery systems, establishing the causal hierarchy that informs demand segmentation (Q2), routing design (Q3), decision rights placement (Q4), and leading indicator selection (Q6). [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html]

### §7 Recursive Review

```text
review_result: pass
review_notes: violations from pass-1 automated review resolved
  -- citation-discipline: removed unsourced "30% or more" figure from B2; removed unsourced M/M/1 percentages from C1
  -- speculation-control: added per-sentence [inference] labels to Analysis paragraphs 1 and 2 in Findings
  -- remove-ai-slop: removed bold from full Key Finding claim sentences; bold reserved for key terms only
  -- logical-coherence: narrowed "VSM studies consistently show" to single case study in Executive Summary and §2
  -- §6 Synthesis mirrored to match Findings changes
acronym_audit: passed
  -- TOC: Theory of Constraints expanded on first use (§2)
  -- DORA: DevOps Research and Assessment expanded on first use (§2)
  -- VSM: value stream mapping expanded on first use (§2)
  -- WIP: work-in-progress expanded on first use (§0)
  -- CAB: Change Advisory Board expanded on first use (§2)
  -- R&D: research and development expanded on first use (§2)
parity_check: passed -- §6 Synthesis and Findings are mirrored outputs
claim_audit: passed -- all factual and inferential claims carry labels and URL-backed sources
no_self_referential_citations: passed
no_ai_slop: passed
scope_guardrail: maintained -- no redesign recommendations included
confidence_level: medium -- direction strongly supported; precise magnitude not established
```

---

## Findings

### Executive Summary

In split-authority delivery systems, governance-generated queueing caused by approval latency and fragmented decision rights is the dominant throughput constraint, not capacity shortage. [inference; source: https://dora.dev/capabilities/streamlining-change-approval/; https://www.tocinstitute.org/five-focusing-steps.html] DORA's multi-firm research confirms that external change approvals are negatively correlated with all delivery performance metrics, and a value stream mapping (VSM) case study of a 200-engineer component-team organisation found 97% wait time, consistent with the governance-constraint direction of the DORA evidence. [inference; source: https://dora.dev/capabilities/streamlining-change-approval/; https://www.orgtopologies.com/post/case-study-from-component-teams-to-team-topologies-to-fast-agile] Fragmented decision rights are the organisational root cause of approval latency: when no single actor owns risk, cost, and execution simultaneously, every substantive decision must travel a multi-party approval circuit whose cumulative wait time dominates total cycle time. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html; https://dora.dev/capabilities/loosely-coupled-teams/] Dependency coupling amplifies the effect by increasing the number of approval nodes each item crosses, and funding gates contribute periodic batch-demand instability as a coarser-cycle variant of the same mechanism. [inference; source: https://www.orgtopologies.com/post/case-study-from-component-teams-to-team-topologies-to-fast-agile; https://davidamitchell.github.io/Research/research/2026-05-23-funding-authority-delivery-capability-risk-accountability-split.html] Capacity shortage is secondary and partially endogenous: governance overhead consumes productive capacity, and the approval queue obscures latent capacity that would otherwise be measurable. [inference; source: https://www.tocinstitute.org/five-focusing-steps.html; https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html]

### Key Findings

1. Approval latency is a policy constraint in the Theory of Constraints (TOC) sense, meaning it is rule-imposed rather than capacity-limited, and therefore blocks throughput even when physical execution capacity is sufficient. ([inference]; medium confidence; source: https://www.tocinstitute.org/five-focusing-steps.html; https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html)

2. DORA multi-year, multi-firm survey research finds that external change approval processes are negatively correlated with all four software delivery performance metrics, confirming that governance-type constraints suppress measured delivery performance across diverse organisations. ([fact]; medium confidence; source: https://dora.dev/capabilities/streamlining-change-approval/; https://dora.dev/research/2019/dora-report/)

3. Value stream mapping (VSM) analysis applied to a 200-engineer organisation with tightly coupled component teams found 97% waste or wait time, meaning months of calendar time for work requiring only 2 to 3 days of active effort, demonstrating the system-level magnitude of governance-generated queue latency. ([fact]; medium confidence; source: https://www.orgtopologies.com/post/case-study-from-component-teams-to-team-topologies-to-fast-agile)

4. Fragmented decision rights are the organisational root cause of approval latency in split-authority systems: when no party holds sufficient authority to commit unilaterally, every substantive decision creates a multi-party approval circuit that adds queue wait time at each step. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html; https://dora.dev/capabilities/loosely-coupled-teams/)

5. Dependency coupling amplifies governance-generated queueing by adding one or more cross-team synchronisation queues to every work item that crosses a team boundary, compounding the total wait time produced by the governance approval chain. ([inference]; medium confidence; source: https://dora.dev/capabilities/loosely-coupled-teams/; https://www.orgtopologies.com/post/case-study-from-component-teams-to-team-topologies-to-fast-agile)

6. Funding gates create throughput instability through a batch demand spike mechanism: demand accumulates during gate closure and enters the delivery system simultaneously at gate opening, overwhelming execution capacity even in organisations with adequate steady-state bandwidth. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-23-funding-authority-delivery-capability-risk-accountability-split.html; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html)

7. Capacity shortage is secondary and partially endogenous in split-authority systems: governance overhead consumes productive delivery capacity and the approval queue conceals latent capacity, so the constraint appears to be execution bandwidth when the binding limiter is actually governance-generated blocking. ([inference]; medium confidence; source: https://www.tocinstitute.org/five-focusing-steps.html; https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html)

8. TOC warns that adding capacity before identifying and exploiting the actual constraint is the most common improvement failure, and organisations that add headcount without reducing governance overhead typically find that throughput improves less than expected because the governance constraint absorbs the new capacity. ([inference]; medium confidence; source: https://www.tocinstitute.org/five-focusing-steps.html; https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html)

9. The feedback loop between approval latency and large-batch delivery is self-reinforcing: high approval latency incentivises teams to bundle work into fewer, larger submissions; larger batches increase change failure risk; higher failure risk makes approvers more conservative; and conservative approvers extend cycle times further. ([inference]; medium confidence; source: https://dora.dev/capabilities/streamlining-change-approval/; https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html)

10. There is a non-zero minimum approval-latency floor in regulated enterprises set by mandatory controls such as segregation of duties and change control for regulated systems, but most split-authority organisations operate substantially above this floor because governance patterns evolved to apply heavyweight controls uniformly rather than proportionately to transaction risk. ([inference]; medium confidence; source: https://dora.dev/capabilities/streamlining-change-approval/; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Approval latency is a policy constraint blocking throughput even when capacity is sufficient | https://www.tocinstitute.org/five-focusing-steps.html; https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html | medium | TOC policy-vs-physical distinction; confirmed by governance-controls completed item |
| [fact] External change approval negatively correlated with all DORA delivery performance metrics | https://dora.dev/capabilities/streamlining-change-approval/; https://dora.dev/research/2019/dora-report/ | medium | DORA multi-firm survey; most robust empirical source in this item |
| [fact] 97% waste/wait time in tightly coupled component-team org (VSM analysis, 200-engineer firm) | https://www.orgtopologies.com/post/case-study-from-component-teams-to-team-topologies-to-fast-agile | medium | Single case study; directionally consistent with broader VSM literature |
| [inference] Fragmented decision rights are the organisational root cause of approval latency | https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html; https://dora.dev/capabilities/loosely-coupled-teams/ | medium | Derived from governance and DORA autonomy evidence |
| [inference] Dependency coupling adds synchronisation queues, amplifying total wait time | https://dora.dev/capabilities/loosely-coupled-teams/; https://www.orgtopologies.com/post/case-study-from-component-teams-to-team-topologies-to-fast-agile | medium | Consistent across DORA and Org Topologies evidence |
| [inference] Funding gates create batch demand spike instability at gate opening | https://davidamitchell.github.io/Research/research/2026-05-23-funding-authority-delivery-capability-risk-accountability-split.html; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html | medium | Mechanistic inference from completed repository items |
| [inference] Capacity shortage is secondary and partially endogenous to governance overhead | https://www.tocinstitute.org/five-focusing-steps.html; https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html | medium | TOC five focusing steps; supported by IT throughput item |
| [inference] Adding capacity before reducing governance overhead produces less improvement than expected | https://www.tocinstitute.org/five-focusing-steps.html; https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html | medium | TOC exploitation-before-elevation principle |
| [inference] Approval latency and large-batch delivery form a self-reinforcing feedback loop | https://dora.dev/capabilities/streamlining-change-approval/; https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html | medium | Mechanistic inference supported by DORA batch-size finding and circumvention item |
| [inference] Most split-authority organisations operate above the minimum mandatory approval floor | https://dora.dev/capabilities/streamlining-change-approval/; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html | medium | Derived from DORA and governance effectiveness evidence |

### Assumptions

- The five candidate constraint categories (capacity shortage, dependency coupling, approval latency, funding gates, fragmented decision rights) are collectively exhaustive for the scope of this analysis; organisations whose primary instability source is technology failure or market-demand collapse are out of scope. [assumption; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html]
- DORA survey research is a reasonable proxy for the typical split-authority organisation because high governance overhead correlates with lower performance in the dataset and the sample spans multiple industries and firm sizes. [assumption; source: https://dora.dev/research/2019/dora-report/]

### Analysis

The five candidate constraints form a hierarchy rather than a set of independent alternatives: fragmented decision rights are the structural condition; approval latency is the direct mechanism; dependency coupling is the amplifier; and funding gates are the periodic, coarser-cycle variant. [inference; source: https://www.tocinstitute.org/five-focusing-steps.html; https://dora.dev/capabilities/streamlining-change-approval/] Capacity shortage is the only independent candidate, and the evidence does not support it as the primary system-level constraint in split-authority organisations that have not yet reduced governance friction. [inference; source: https://www.tocinstitute.org/five-focusing-steps.html; https://dora.dev/capabilities/streamlining-change-approval/]

DORA's negative correlation finding is the most robust evidence source in this item because it is multi-firm, multi-industry, and longitudinal, and because it directly tests the governance-approval variable rather than inferring it. [inference; source: https://dora.dev/capabilities/streamlining-change-approval/; https://dora.dev/research/2019/dora-report/] TOC policy-constraint theory and the VSM case study evidence are mechanistically consistent with the DORA finding: all three identify wait time in governance queues as the dominant cycle-time contributor. [inference; source: https://www.tocinstitute.org/five-focusing-steps.html; https://www.orgtopologies.com/post/case-study-from-component-teams-to-team-topologies-to-fast-agile] Prior completed repository items on governance controls effectiveness and governance failure mechanisms provide additional causal texture: controls become overhead when applied uniformly at high volume, which is the defining condition in split-authority systems where every work item passes through a multi-stakeholder approval chain. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html; https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html]

Capacity shortage does not have strong evidentiary support as the primary constraint in split-authority systems that have not yet reduced governance friction. [inference; source: https://www.tocinstitute.org/five-focusing-steps.html; https://dora.dev/capabilities/streamlining-change-approval/] TOC explicitly warns that adding capacity before exploiting the actual constraint is a common and costly misdiagnosis. [inference; source: https://www.tocinstitute.org/five-focusing-steps.html] The IT throughput constraint completed item notes that governance overhead consumes capacity and that the approval queue hides latent capacity, which is the mechanistic pathway by which a capacity-shortage appearance masks a governance-constraint reality. [inference; source: https://www.tocinstitute.org/five-focusing-steps.html; https://davidamitchell.github.io/Research/research/2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate.html]

The self-reinforcing feedback loop between approval latency and batch-size growth is the instability mechanism: any increase in governance overhead accelerates the feedback, driving throughput down and batch size up, until an external intervention (governance redesign, senior escalation, or accumulated delivery failure) breaks the cycle. [inference; source: https://dora.dev/capabilities/streamlining-change-approval/; https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html]

### Risks, Gaps, and Uncertainties

- No primary cross-firm experimental study isolates approval latency as the binding constraint in split-authority organisations through direct manipulation. All evidence is observational, case-based, or theoretical.
- Precise magnitude decomposition (what fraction of cycle time each constraint category accounts for) is not supported by the available evidence base.
- The secondary status of capacity shortage is directional, not universal: in severely understaffed teams, capacity may be independently binding, and the findings here apply primarily to organisations that have not yet addressed governance friction.
- The feedback loop mechanism between approval latency and batch-size growth is well-supported mechanistically but has not been experimentally isolated from other explanatory variables in a controlled study.

### Open Questions

- At what threshold of governance overhead does capacity shortage become co-dominant with approval latency, and is this threshold measurable using available metrics such as DORA lead time or WIP levels?
- How does the constraint hierarchy differ in heavily regulated sectors (banking, healthcare, public sector) versus less-regulated technology firms, given that the mandatory approval floor is higher in the former?
- Does the introduction of AI-assisted delivery tooling shift the dominant constraint from approval latency toward capacity shortage as governance becomes the clearer residual bottleneck?

### Output

`knowledge`. This item identifies the dominant flow constraint in split-authority delivery systems and establishes the causal hierarchy among the five candidate categories, providing the empirical and theoretical foundation for demand segmentation (Q2), exception routing design (Q3), decision rights placement (Q4), and leading indicator selection (Q6). [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html]
