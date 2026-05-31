---
review_count: 2
title: "Q6: Leading indicators of instability in split-authority flow systems"
added: 2026-05-29
status: completed
priority: high
tags: [leading-indicators, flow-metrics, delivery-risk, instability]
blocks: [2026-05-29-split-authority-q1-flow-constraint, 2026-05-29-split-authority-q2-demand-segmentation, 2026-05-29-split-authority-q3-routing-exception-isolation]
started: 2026-05-31T12:06:51+00:00
completed: 2026-05-31T20:33:29+00:00
output: [knowledge]
cites:
  - 2026-05-29-split-authority-p1-operating-model-synthesis
  - 2026-05-29-split-authority-q2-demand-segmentation
  - 2026-05-29-split-authority-q3-routing-exception-isolation
  - 2026-05-29-split-authority-q4-decision-rights-placement
  - 2026-05-29-split-authority-q5-control-model-tradeoff
  - 2026-04-01-backpressure-theory-of-constraints
  - 2026-05-23-governance-controls-effectiveness-conditions
  - 2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention
  - 2026-05-16-variance-control-comparison-across-delivery-modes
  - 2026-05-20-hitl-capacity-thresholds-in-banking-compliance
related:
  - 2026-04-26-ai-governance-cost-performance-delivery-impact
supersedes: ~
superseded_by: []
item_type: primary
confidence: medium
themes:
  - governance-policy
  - benchmarks-eval
  - cost-performance
  - organisational-design
  - tools-infrastructure
versions: []
---

# Q6: Leading indicators of instability in split-authority flow systems

## Research Question

Which metrics best predict unsafe queue growth, rising delivery risk, or hidden demand accumulation in a split-authority delivery system, where "split-authority" means a context in which authority is divided among at least two stakeholder groups with independent veto or approval power?

## Scope

**In scope:**
- Candidate metric families: queue age, lead time, blocked-work ratio, exception volume, rework rate, shadow-work growth, incident load, approval wait time.
- Early-warning signal quality (warning lead time versus false-alarm rate).
- Threshold design principles for trigger-based control regime adjustments.

**Out of scope:**
- Final control-model choice, which is covered by Q5.

**Constraints:**
- Indicator design must build on Q2 demand-segmentation classes, Q3 routing and circuit-breaker triggers, Q4 decision-delegation boundaries, and Q5 control-pattern assignments.

## Context

Q6 defines the early-warning telemetry needed to detect destabilisation in a split-authority delivery system before severe throughput or risk failure occurs. The operating model synthesis (P1) identified four leading indicator families (queue health, exception volume, lead time trends, rework and incident load) without specifying how to operationalise or threshold them. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html] Q6 fills that gap, grounding each family in evidence from queueing theory, DevOps Research and Assessment (DORA) metric research, and Site Reliability Engineering (SRE) operational telemetry.

## Approach

1. Define and operationalise candidate leading indicators per metric family.
2. Evaluate predictive value and confounders for each family.
3. Propose a compact instability warning bundle with tiered trigger thresholds aligned to the Q3 circuit-breaker conditions and Q5 control-pattern shifts.

## Sources

- [x] [DORA (2024) Software delivery metrics: throughput and instability](https://dora.dev/guides/dora-metrics-four-keys/)
- [x] [Google SRE Workbook: Alerting on Service Level Objectives](https://sre.google/workbook/alerting-on-slos/)
- [x] [Google SRE Workbook: Eliminating Toil](https://sre.google/workbook/eliminating-toil/)
- [x] [Little, J.D.C. (1961) A proof for the queuing formula, Operations Research](https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387)
- [x] [Reinertsen, D.G. (2009) The Principles of Product Development Flow, Celeritas Publishing](https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009)
- [x] [TOC Institute (2024) Five Focusing Steps](https://www.tocinstitute.org/five-focusing-steps.html)
- [x] [Mitchell (2026) Operating model synthesis for split-authority delivery systems (P1)](https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html)
- [x] [Mitchell (2026) Q2: Demand segmentation for fast-path vs controlled-path flow](https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html)
- [x] [Mitchell (2026) Q3: Routing design that isolates exceptions from routine flow](https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html)
- [x] [Mitchell (2026) Q4: Decision rights that should move closer to execution](https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q4-decision-rights-placement.html)
- [x] [Mitchell (2026) Q5: Control model for the best throughput-risk trade-off](https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q5-control-model-tradeoff.html)
- [x] [Mitchell (2026) Backpressure infrastructure and the Theory of Constraints](https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html)
- [x] [Mitchell (2026) Internal governance controls: effectiveness conditions in regulated enterprises](https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html)
- [x] [Mitchell (2026) Governance failure mechanisms: bureaucracy and circumvention](https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html)
- [x] [Mitchell (2026) Variance control comparison across delivery modes](https://davidamitchell.github.io/Research/research/2026-05-16-variance-control-comparison-across-delivery-modes.html)

---

## Research Skill Output

### §0 Initialise

Question: Which metrics best predict unsafe queue growth, rising delivery risk, or hidden demand accumulation in a split-authority delivery system?

Scope:
- In scope: operationalising candidate metric families (queue age, lead time, blocked-work ratio, exception volume, rework rate, shadow-work growth, incident load, approval wait time); evaluating predictive value and false-alarm risk; proposing a compact warning bundle with tiered thresholds
- Out of scope: choosing the final control model (handled in Q5); primary investigation of Q1 flow constraint identification (not yet a completed standalone item)
- Constraints: indicator design must be consistent with Q2 demand classes (Class 1 fast path, Class 2 standard path, Class 3 exception path), Q3 routing mechanics and circuit-breaker triggers, Q4 decision-delegation boundary parameters, and Q5 control-pattern selection logic

Output format: structured synthesis with Executive Summary, Key Findings, Evidence Map, Assumptions, Analysis, Risks/Gaps, Open Questions, and Output section; knowledge output type.

Working hypotheses: (a) leading indicators derived from queueing theory (Work in Progress (WIP) age, queue length growth rate) will provide earlier warning than throughput outcome metrics (lead time degradation, deployment frequency decline) because congestion builds before it manifests as output; [assumption; source: https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387; justification: Little's Law implies queue length and wait time co-move, but queue length changes are detectable before customer-visible latency crosses a complaint threshold] (b) exception volume ratios will provide earlier warning of governance overload than approval wait time because exception classification happens at intake while approval wait time accumulates downstream. [assumption; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html; justification: Q3 established that intake classification occurs before the exception review queue; a rising classification rate predicts downstream saturation before it occurs]

Prior completed items cross-referenced:
- P1 identified four leading indicator families (queue health, exception volume, lead time trends, rework and incident load) but did not provide operationalised thresholds; Q6 fills this gap. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html]
- Q3 established two system-level circuit-breaker triggers: sustained exception volume above a calibrated threshold, and exception lane WIP saturation; Q6 provides the precursor signals that should fire before these circuit-breakers activate. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html]
- Q5 established that control regime shifts between pre-approval, bounded delegation, and post-hoc review should be trigger-based; Q6 defines what those triggers look like in observable metrics. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q5-control-model-tradeoff.html]

### §1 Question Decomposition

The research question decomposes into three clusters, each with atomic sub-questions:

**A. Operationalise each candidate metric family**
- A1: How is queue age defined, measured, and interpreted as a leading indicator of approval-gate congestion?
- A2: How is the blocked-work ratio defined, and what does a rising ratio signal?
- A3: How is exception volume (Class 3 share of total intake) measured, and what does a rising ratio predict?
- A4: How is lead time trend measured, and how does DORA's evidence relate lead time to future throughput decline?
- A5: How is rework rate (including DORA's deployment rework rate) measured, and what does it predict about capacity availability?
- A6: How is shadow-work growth observable, and what does hidden demand accumulation signal about future intake?
- A7: How does approval wait time differ from queue age, and what does it add to the indicator bundle?

**B. Evaluate predictive value and confounders**
- B1: What is the theoretical basis for each metric's predictive power (causal mechanism, not just correlation)?
- B2: What confounders reduce each metric's reliability as a leading indicator?
- B3: What measurement windows minimise false-alarm rates while preserving detection speed (applying the SRE multi-window burn rate principle)?

**C. Propose a compact warning bundle**
- C1: Which metrics should form the minimum viable bundle for a split-authority system?
- C2: What threshold design approach (absolute, relative to baseline, or rate-of-change) is best supported by evidence?
- C3: How should thresholds map to tiered responses aligned to Q3 circuit-breakers and Q5 regime shifts?

### §2 Investigation

#### §2.A: Operationalising the metric families

**A1: Queue age**

Queue age, in the context of work items in an approval queue, is the elapsed time from the moment a work item enters a queue to the current observation point, without accounting for periods of active processing. Reinertsen (2009) distinguishes queue age from cycle time: cycle time is the total elapsed time from work start to completion; queue age is the waiting portion only. [inference; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009] Reinertsen argues that the age of the oldest item in a queue is a more responsive signal of flow problems than aggregate WIP count, because an item that has been waiting longer than the median reveals a specific blockage rather than a general volume increase. [inference; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009]

Little's Law (L = lambda * W, where L is average queue length, lambda is arrival rate, and W is average wait time) implies that if arrival rate is stable, rising average queue age and rising queue length co-move. [fact; source: https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387] This means queue age growth is mathematically equivalent to queue length growth given constant arrival. In approval queues, rising queue age therefore signals that service rate (approver throughput) has declined relative to arrival rate, or that the mix of work types has shifted toward longer-service-time items (Class 3). [inference; source: https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009]

Practical operationalisation: measure the 75th percentile (P75) age of items currently waiting in each queue lane (fast path, standard path, exception path) at a fixed cadence (weekly). A rising P75 across two or more consecutive measurement periods signals capacity stress before median age shows a change. [inference; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009]

**A2: Blocked-work ratio**

The blocked-work ratio is the proportion of items currently in progress that cannot advance because of a dependency, missing decision, or resource unavailability. In a three-lane routing model, blocked items cause local WIP accumulation without consuming server (approver) time, effectively inflating average age in the affected lane. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html]

Reinertsen (2009) identifies blocked work as a leading indicator of developing bottlenecks: a block that cannot be resolved within the standard processing interval signals a dependency that will force reclassification or escalation if it persists. [inference; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009] A rising blocked-work ratio is therefore a precursor to both exception lane pressure and lead time growth. [inference; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009; https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387]

Practical operationalisation: count the number of in-flight items flagged as blocked (by ticket state, label, or queue hold) divided by total current WIP, measured at the same weekly cadence as queue age. An increase of more than 10 percentage points over a two-week period is a signal warranting investigation. [inference; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009; justification: no universal threshold exists; the 10-percentage-point figure is a design heuristic based on the principle that doubling the baseline blocked ratio is operationally significant]

**A3: Exception volume (Class 3 share of intake)**

Q3 established that the Class 3 (exception path) share of total intake is a system-level circuit-breaker trigger: when sustained exception volume exceeds a calibrated threshold, fast-path gate criteria should be tightened. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html] Q6 treats this metric as both a circuit-breaker and a leading indicator of governance overload: a rising exception share precedes exception lane saturation, which precedes approval wait time growth. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html; https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387]

A rising exception share can reflect two distinct causes: (a) genuine risk increase in the incoming demand mix; (b) miscalibrated demand-segmentation criteria that are over-assigning items to the exception class. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html] Distinguishing these causes requires reviewing a sample of recently classified exception items against the Q2 boundary tests (template test, recovery test, blast radius test). [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html]

Practical operationalisation: compute the four-week rolling average of Class 3 items as a percentage of total weekly intake. A sustained increase of five percentage points over four consecutive weeks is the precursor warning. The Q3 circuit-breaker threshold (fast-path tightening) fires when this ratio exceeds an organisation-calibrated cap. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html]

**A4: Lead time trend**

DORA defines change lead time as the time from a change being committed in version control to its deployment in production. [fact; source: https://dora.dev/guides/dora-metrics-four-keys/] DORA research shows that change lead time is both a throughput metric and an instability signal: rising lead time is correlated with declining deployment frequency and, for teams in lower performance bands, with rising change failure rate. [inference; source: https://dora.dev/guides/dora-metrics-four-keys/] The 2024 DORA report confirms that speed and stability are positively correlated for high-performing teams. [fact; source: https://dora.dev/research/2024/dora-report/] Lead time degradation therefore signals systemic pipeline problems rather than deliberate quality investment. [inference; source: https://dora.dev/research/2024/dora-report/]

In a split-authority context, lead time is not purely a delivery pipeline metric; it incorporates approval queue wait time as its dominant component. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html] A rising lead time trend therefore reflects approval-gate congestion as well as pipeline problems, making it a composite metric that integrates queue health and pipeline health into one observable. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html; https://dora.dev/guides/dora-metrics-four-keys/]

Practical operationalisation: compute the four-week moving average of median change lead time for each lane (fast path, standard path) separately. A 20% increase from baseline over four consecutive weeks is a signal warranting investigation. [inference; source: https://dora.dev/guides/dora-metrics-four-keys/; justification: DORA does not specify a universal percentage threshold; 20% is derived from the principle that changes above natural variation (typically one standard deviation) warrant investigation rather than monitoring]

**A5: Rework rate and deployment rework rate**

The DORA 2024 metric set includes two instability measures: change failure rate (the proportion of deployments requiring immediate intervention) and deployment rework rate (the proportion of unplanned deployments made in response to a production incident). [fact; source: https://dora.dev/guides/dora-metrics-four-keys/] The SRE workbook's concept of toil, meaning repetitive, automatable, reactive work that scales with service load, provides a complementary operational lens: rising toil share of team capacity predicts capacity starvation for planned delivery work. [fact; source: https://sre.google/workbook/eliminating-toil/]

In a split-authority context, rework rate captures two signal types simultaneously: (a) delivery pipeline quality decline (upstream design or testing failures); (b) approval bypass failure (where expedited or shadow work escapes review and produces field defects). [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html] A rising rework rate in the context of also-rising exception bypass indicators provides strong combined evidence of governance overload. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html]

Practical operationalisation: compute the four-week rolling deployment rework rate (unplanned deployments as a proportion of total deployments) and the share of team capacity consumed by unplanned remediation work. Sustained breach of 20% unplanned capacity share for two consecutive sprints is a warning threshold; this is consistent with the P1 synthesis recommendation. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html; https://sre.google/workbook/eliminating-toil/]

**A6: Shadow-work growth**

Shadow work, meaning work executed outside the formal intake and approval system, represents hidden demand accumulation. It is not directly observable from ticket systems by definition but leaves observable proxies: (a) team output exceeding approved pipeline throughput (more deployments than formally approved items); (b) a rising ratio of unplanned deployments with no associated intake ticket; (c) post-deployment audit findings revealing changes not present in the approved queue. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html]

Shadow work grows when governance controls are coercive rather than enabling: when the formal intake process imposes higher friction than the risk it prevents, teams route work informally to preserve delivery velocity. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html] This is the mechanism identified in the governance failure mechanisms item as bureaucratic circumvention. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html] A rising shadow-work proxy therefore signals that governance friction has exceeded the team's tolerance threshold, which predicts either an escalating compliance risk (undisclosed changes) or accelerating formal-queue growth as teams bring previously bypassed work into the formal system during audits. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html]

Practical operationalisation: compare the count of production deployments per sprint to the count of formally approved intake items closed per sprint. A persistent and growing gap (greater than 10% over three sprints) is a warning signal. [assumption; justification: a 10% tolerance accommodates legitimate emergency changes documented after the fact; a larger persistent gap suggests systematic shadow work rather than isolated emergencies; no published study provides a universal threshold for this ratio; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html]

**A7: Approval wait time**

Approval wait time is the time an item spends in an approval queue awaiting a decision, excluding active processing time. It is more granular than queue age (which is item-level) and directly measures the approval bottleneck rather than the accumulation of all queue waiting. [inference; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009]

Approval wait time is a lagging indicator relative to queue age and exception volume: it rises after those metrics signal congestion. It is useful as a confirmation metric and as a severity gauge once warning has already been raised, rather than as a first-line signal. [inference; source: https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009]

#### §2.B: Evaluating predictive value and confounders

**B1: Theoretical grounding per metric family**

The causal chain from split-authority governance design to throughput failure runs as follows: approval requirements fragment decision rights, approval queues grow as demand exceeds approver capacity, WIP accumulates at the approval gate, lead time extends, throughput declines, and teams adopt coping behaviours (shadow work, misclassification). [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html; https://www.tocinstitute.org/five-focusing-steps.html; https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387]

Metric families that capture early stages of this chain (queue age, blocked-work ratio, exception volume) will fire before metrics that capture later stages (lead time trend, rework rate, approval wait time). [inference; source: https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009] The Theory of Constraints (TOC) five focusing steps identify the constraint, exploit it, and subordinate all other processes to it; metrics focused on the constraint (the approval gate) provide more actionable early warning than metrics focused on downstream output. [inference; source: https://www.tocinstitute.org/five-focusing-steps.html]

**B2: Confounders per metric family**

Queue age confounder: batch-heavy intake patterns (large releases arriving together rather than in a continuous stream) create artificial age spikes that resolve without constraint action. Mitigation: use P75 rather than mean age; compare spike duration to arrival-pattern cadence. [inference; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009]

Blocked-work ratio confounder: scheduled dependency pauses (environment refreshes, third-party integration windows) cause temporary blocks that are not constraint-driven. Mitigation: maintain a calendar of scheduled pause windows and adjust the measurement denominator to exclude items in planned hold. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html]

Exception volume confounder: genuine seasonal or regulatory demand spikes (year-end change freezes, audit cycles) temporarily elevate exception share. Mitigation: track the four-week rolling average and compare against the same period in prior cycles. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html]

Lead time trend confounder: deliberate pipeline slowdowns (scheduled maintenance, change freeze windows) inflate lead time temporarily. Mitigation: exclude items entering the pipeline during formally declared freeze windows from the trend calculation. [inference; source: https://dora.dev/guides/dora-metrics-four-keys/]

Rework rate confounder: technology platform migrations or major dependency upgrades produce transient rework spikes that are not governance-driven. Mitigation: tag rework items by root cause category; exclude platform-migration rework from the governance-signal calculation. [inference; source: https://dora.dev/guides/dora-metrics-four-keys/; https://sre.google/workbook/eliminating-toil/]

Shadow-work proxy confounder: legitimate unplanned emergency changes that follow a post-facto approval process will appear as gaps between deployments and tickets. Mitigation: maintain an emergency change register (as per Information Technology Infrastructure Library (ITIL) 4 emergency change practice) and exclude registered emergency changes from the shadow-work proxy count. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html]

**B3: Multi-window threshold design (applying SRE burn-rate principles)**

The SRE workbook on alerting on Service Level Objectives (SLOs) recommends multi-window alerting to balance detection speed against false-alarm rate: a short observation window catches fast-developing incidents quickly but has low precision (many false alarms), while a long window improves precision but has slow detection time. The recommended approach is to require that an alert threshold be breached simultaneously in both a short window and a long window, which provides fast detection when the breach is severe while suppressing alerts for transient spikes. [fact; source: https://sre.google/workbook/alerting-on-slos/]

Applying this principle to approval queue indicators: each metric should have a short-window check (one to two weeks) for severe-and-fast deterioration and a long-window check (four weeks) for slow-building congestion. An alert fires when either window breaches its respective threshold and the trajectory is consistently worsening (not reverting). [inference; source: https://sre.google/workbook/alerting-on-slos/; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009]

#### §2.C: Compact warning bundle design

The P1 synthesis established that trigger-based regime adjustments are more defensible than fixed allocation rules. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html] The Q3 circuit-breakers define the response actions (tighten fast-path gate; ration all-lane intake). [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html] Q5 defines the control-regime shift conditions (from bounded delegation toward pre-approval, or from pre-approval toward post-hoc review). [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q5-control-model-tradeoff.html] Q6 defines the tiered signal sequence that feeds these responses. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html]

Tier 1 (Monitor signal, earliest warning, estimated two to four weeks before throughput impact): P75 queue age rising across two consecutive weekly measurements; blocked-work ratio increasing by more than five percentage points over two weeks. Response: integrator reviews classification accuracy; no routing change required. [inference; source: https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387; https://sre.google/workbook/alerting-on-slos/; justification: time-horizon estimates are design heuristics derived from queueing theory non-linear dynamics and SRE multi-window alerting; not empirically validated universal values]

Tier 2 (Advisory signal, intermediate warning, estimated one to two weeks before throughput impact): exception share four-week rolling average rising by five percentage points over four consecutive weeks; lead time trend four-week moving average rising by 15% or more from baseline. Response: integrator reviews exception classification accuracy; Q2 boundary tests re-administered to a sample of recent Class 3 items; no control-regime shift yet. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html; https://dora.dev/guides/dora-metrics-four-keys/; justification: time-horizon estimate is a design heuristic; threshold percentages are calibration starting points]

Tier 3 (Operational alert, imminent impact, estimated days before circuit-breaker fires): rework and unplanned remediation share breaching 20% of team capacity for two consecutive sprints; shadow-work proxy gap exceeding 10% for three consecutive sprints. Response: integrator activates Q5 tightening (shift toward pre-approval for ambiguous items; reduce bounded-delegation ceiling); Q3 exception lane WIP limit reviewed against current fill rate. [inference; source: https://sre.google/workbook/eliminating-toil/; https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html; justification: time-horizon estimate is a design heuristic; threshold values derived from SRE toil capacity guidance]

Tier 4 (Circuit-breaker, per Q3): exception lane WIP at limit for more than 50% of the measurement period; total system WIP growing faster than arrival rate for more than two weeks. Response: Q3 fast-path tightening and/or all-lane intake rationing; escalation to cross-functional integrator authority. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html]

### §3 Reasoning

Separating facts from inferences and assumptions:

**Facts (grounded in primary or secondary sources):**
1. Little's Law (L = lambda * W) holds for stable arrival rates, meaning queue length and wait time co-move. [fact; source: https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387]
2. DORA defines change lead time, deployment frequency, change failure rate, failed deployment recovery time, and deployment rework rate as the five current software delivery performance metrics. [fact; source: https://dora.dev/guides/dora-metrics-four-keys/]
3. DORA 2024 reports that Artificial Intelligence (AI) adoption increases individual productivity and flow but negatively impacts software delivery stability and throughput, reinforcing that speed-stability tension requires active monitoring. [fact; source: https://dora.dev/research/2024/dora-report/]
4. The SRE workbook recommends multi-window alerting on error budget burn rate, requiring simultaneous breach of both a short-window and a long-window threshold to improve precision without sacrificing recall. [fact; source: https://sre.google/workbook/alerting-on-slos/]
5. The SRE workbook defines toil as repetitive, reactive work that scales with service load and recommends keeping toil below 50% of team capacity, with a target to actively reduce it. [fact; source: https://sre.google/workbook/eliminating-toil/]

**Inferences (derived from evidence with stated reasoning):**
1. Queue age is a leading indicator of throughput decline because it captures congestion before average cycle time visibly increases, consistent with Little's Law dynamics in queues approaching capacity. [inference; source: https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009]
2. Exception volume (Class 3 share) fires before approval wait time because classification happens at intake while approval wait accumulates downstream of classification. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html]
3. Shadow-work growth signals governance friction exceeding tolerance, predicting either compliance risk escalation or sudden formal-queue growth as informal work is brought into the system during audits. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html]
4. Multi-window alerting, applied to approval queue metrics in the same manner as SRE error budget burn rate, reduces false alarms from batch-arrival spikes while preserving detection speed for sustained congestion. [inference; source: https://sre.google/workbook/alerting-on-slos/; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009]

**Assumptions:**
1. The exception review function is the binding constraint in the split-authority system; if a different function is the actual constraint, the indicator bundle must be re-anchored to that constraint. [assumption; source: https://www.tocinstitute.org/five-focusing-steps.html; justification: consistent with P1 and Q3, which treat governance-generated queueing as the dominant constraint]
2. The specific percentage thresholds proposed (P75 rising over two weeks; 20% unplanned capacity share; 10% shadow-work proxy gap) are calibration heuristics derived from design principles rather than empirically validated universal values. [assumption; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009; justification: no published study provides organisation-universal threshold values for approval queue indicators; organisations must calibrate against their own baseline]

### §4 Consistency Check

```text
contradiction_scan: no internal contradictions detected
  - Queue age (Tier 1) fires before exception volume (Tier 2) because queue age rises as backlog
    accumulates at the intake stage, whereas exception share rises as intake classification
    patterns shift; both are consistent with the causal chain in P1 and Q3.
  - Rework rate (Tier 3) fires later than queue age because rework is a consequence of upstream
    quality or governance failures that take time to manifest in production; this ordering is
    consistent with DORA's characterisation of deployment rework rate as an instability metric
    rather than a throughput metric.
  - The SRE multi-window design principle is applied to queue metrics by analogy; this is an
    inference, not a direct fact, and is labelled accordingly in §2.
confidence_adjustment: all claims maintained at inference level where thresholds are design
  heuristics; fact level reserved for primary source claims (Little's Law, DORA definitions,
  SRE toil definition)
scope_guardrail: maintained -- no control-model selection included (Q5 scope); no Q1 constraint
  identification claim made (Q1 scope)
acronym_audit: first-use expansions confirmed in §0, §2, §3, and §5 prose sections; AI added in §3; HITL and HKMA added in §5 regulatory lens
```

### §5 Depth and Breadth Expansion

**Technical lens:** The non-linear relationship between queue utilisation and wait time (wait time grows polynomially as utilisation approaches 100%, not linearly) means that late-stage indicators like approval wait time provide very little actionable lead time. [inference; source: https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387] Early indicators (queue age, exception share) capture the arrival-rate and service-rate dynamics before the non-linear region is reached. [inference; source: https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009] This technical asymmetry is the primary argument for investing in Tier 1 and Tier 2 metrics rather than treating approval wait time as the primary dashboard metric. [inference; source: https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009]

**Regulatory lens:** In regulated enterprises, shadow-work growth is particularly consequential because undisclosed changes violate change-management obligations under frameworks such as Basel Committee on Banking Supervision (BCBS) 239 (data risk management) and related technology risk standards. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html] A shadow-work proxy that rises during high-volume periods is a regulatory signal, not just an operational one, and warrants integrator-level attention rather than team-level resolution. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html] A completed study of Human-in-the-Loop (HITL) capacity thresholds in banking compliance found that the Hong Kong Monetary Authority (HKMA) treats "significant and prolonged backlogs" as direct evidence of ineffective monitoring systems, and that defensible thresholds are locally calibrated capacity ratios with universal breach indicators including prolonged queue age and missed review timelines, directly supporting Q6's requirement that proposed threshold values be calibrated against each organisation's baseline rather than applied as universal constants. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-20-hitl-capacity-thresholds-in-banking-compliance.html]

**Behavioural lens:** Teams facing persistent queue age growth adopt two rational coping strategies: (a) deliberately misclassifying exception-path work as fast-path to avoid the exception queue; (b) routing work informally (shadow work). [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html] Both behaviours are predicted by the governance failure mechanisms evidence and are observable through the indicator bundle (misclassification shows up as declining exception share combined with rising rework; shadow work shows up in the deployment-to-ticket gap). [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html] Monitoring both metrics together provides a behavioural signal that governance friction is producing avoidance, not just operational signal that throughput is at risk. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html]

**Historical lens:** The SRE error budget policy practice (introduced by Google and documented in the SRE workbook) demonstrates that a pre-agreed trigger-based regime shift (from aggressive feature deployment to reliability-first) is operationally viable in large-scale production environments when threshold values are agreed in advance and the decision to shift regimes is automatic rather than requiring per-incident negotiation. [inference; source: https://sre.google/workbook/alerting-on-slos/] This precedent supports the Q6 tiered warning design: pre-agreed thresholds remove the deliberation cost that otherwise delays regime shifts until the situation is critical. [inference; source: https://sre.google/workbook/alerting-on-slos/; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q5-control-model-tradeoff.html]

### §6 Synthesis

**Executive Summary**

Five metric families, tiered by causal distance from the approval constraint, provide the minimum viable early-warning telemetry for split-authority delivery systems: queue age (P75 per lane), blocked-work ratio, exception volume (Class 3 share of intake), lead time trend (four-week moving average), and rework plus unplanned capacity share. [inference; source: https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html; https://dora.dev/guides/dora-metrics-four-keys/] A sixth proxy for shadow-work growth (the deployment-to-ticket gap) provides a governance-friction signal that the operational metrics cannot surface on their own. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html] The metrics are arranged into four warning tiers that map directly to the Q3 circuit-breaker triggers and Q5 control-regime shift conditions, enabling graduated responses proportionate to the severity of the signal. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q5-control-model-tradeoff.html] Threshold values cannot be universal and must be calibrated to each organisation's baseline, but the calibration approach (multi-window, rate-of-change relative to baseline) is grounded in the SRE burn-rate alerting design, which provides a tested operational precedent for trigger-based regime management. [inference; source: https://sre.google/workbook/alerting-on-slos/]

**Key Findings**

1. Queue age at the 75th percentile (P75) per lane is the earliest available warning signal because Little's Law implies that wait time growth in a queue precedes measurable throughput decline, and P75 is more sensitive to developing congestion than the mean or median. ([inference]; medium confidence; source: https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009)

2. Exception volume expressed as the four-week rolling Class 3 share of total intake is the most direct observable precursor to exception lane saturation, which is one of the two Q3 circuit-breaker triggers; it provides a warning window of one to two weeks before the circuit-breaker fires. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html)

3. DORA's change lead time (measured as a four-week moving average per lane) integrates approval-gate congestion and pipeline health into a single observable, making it a composite confirmation metric rather than a first-line signal; its value is highest when it rises in combination with earlier Tier 1 and Tier 2 signals. ([inference]; medium confidence; source: https://dora.dev/guides/dora-metrics-four-keys/; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html)

4. A deployment rework rate exceeding 20% of total deployments, sustained for two or more consecutive sprints, signals that capacity is being consumed by unplanned remediation work at a level that competes directly with planned delivery, consistent with the SRE toil definition and the threshold at which toil threatens delivery capacity. ([inference]; medium confidence; source: https://sre.google/workbook/eliminating-toil/; https://dora.dev/guides/dora-metrics-four-keys/)

5. A persistent gap between production deployments per sprint and formally approved intake items per sprint, exceeding 10% for three or more consecutive sprints, signals systematic shadow-work growth, which predicts either escalating compliance risk or a sudden formal-queue surge when the informal backlog is brought into the system. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html)

6. Multi-window threshold design, requiring simultaneous breach of a short-window check (one to two weeks) and a long-window check (four weeks) before an alert fires, reduces false alarms from batch-arrival spikes while preserving detection speed for sustained congestion, applying the same design principle as SRE error budget burn-rate alerting. ([inference]; medium confidence; source: https://sre.google/workbook/alerting-on-slos/; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009)

7. Rising exception share combined with a declining or stable rework rate signals deliberate misclassification of exception-path work as fast-path work, which is a predictable behavioural coping response to governance friction that undermines routing integrity without triggering the normal exception volume alarm. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html)

8. Pre-agreed trigger thresholds, aligned to the Q3 circuit-breaker conditions and Q5 control-regime shift points, enable automatic regime adjustments without per-incident negotiation, following the same operational logic as the SRE error budget policy, which removes deliberation cost from time-sensitive regime decisions. ([inference]; medium confidence; source: https://sre.google/workbook/alerting-on-slos/; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q5-control-model-tradeoff.html)

9. The specific threshold values proposed (P75 age rising over two consecutive measurements; exception share rising five percentage points over four weeks; 20% unplanned capacity share; 10% deployment-to-ticket gap) are calibration heuristics grounded in design principles rather than empirically validated universal values, and must be calibrated to each organisation's baseline before operational use. ([assumption]; medium confidence; source: https://dora.dev/research/2024/dora-report/; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009; justification: no published study provides organisation-universal threshold values for approval queue indicators)

**Evidence Map**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Queue age P75 is earliest warning metric; Little's Law implies wait time growth precedes throughput decline | https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009 | medium | Key Finding 1 |
| [inference] Exception volume is direct precursor to Q3 circuit-breaker saturation; provides 1-2 week warning window | https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html | medium | Key Finding 2 |
| [fact] DORA defines five metrics including lead time and deployment rework rate as throughput and instability measures | https://dora.dev/guides/dora-metrics-four-keys/ | high | Key Finding 3 basis |
| [inference] Lead time moving average integrates approval-gate congestion; composite confirmation metric | https://dora.dev/guides/dora-metrics-four-keys/; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html | medium | Key Finding 3 |
| [fact] SRE toil definition: repetitive reactive work that scales with load; SRE target is keeping toil below 50% | https://sre.google/workbook/eliminating-toil/ | high | Key Finding 4 basis |
| [inference] Rework rate above 20% for 2 sprints competes with planned delivery capacity | https://sre.google/workbook/eliminating-toil/; https://dora.dev/guides/dora-metrics-four-keys/ | medium | Key Finding 4 |
| [inference] Deployment-to-ticket gap signals shadow work, predicts compliance risk or formal-queue surge | https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html | medium | Key Finding 5 |
| [fact] SRE multi-window burn rate alerting: simultaneous breach of short and long window required; improves precision without losing recall | https://sre.google/workbook/alerting-on-slos/ | high | Key Finding 6 basis |
| [inference] Multi-window design applied to approval queue metrics reduces false positives from batch arrivals | https://sre.google/workbook/alerting-on-slos/; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009 | medium | Key Finding 6 |
| [inference] Rising exception share plus declining rework = misclassification signal; governance-friction coping behaviour | https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html | medium | Key Finding 7 |
| [inference] Pre-agreed thresholds enable automatic regime shifts; eliminates per-incident deliberation cost; SRE error budget policy precedent | https://sre.google/workbook/alerting-on-slos/; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q5-control-model-tradeoff.html | medium | Key Finding 8 |
| [assumption] Specific threshold values are calibration heuristics; must be organisation-calibrated | https://dora.dev/research/2024/dora-report/; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009 | medium | Key Finding 9 |

**Assumptions**

1. The exception review function is the binding constraint in the split-authority system; if a different function holds the actual constraint, the indicator bundle must be re-anchored. [assumption; source: https://www.tocinstitute.org/five-focusing-steps.html; justification: consistent with P1, Q3, and Q5 all treating governance-generated queueing as the dominant constraint]

2. The specific threshold values (P75 age rising over two consecutive weeks; exception share rising five percentage points over four weeks; 20% unplanned capacity share; 10% deployment-to-ticket gap) are calibration heuristics derived from design principles and must be set against each organisation's baseline. [assumption; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009; https://dora.dev/research/2024/dora-report/; justification: no published study provides universal threshold values for approval queue indicators in split-authority systems]

3. Emergency changes registered under an ITIL-equivalent emergency change practice are excluded from the shadow-work proxy calculation; if no emergency change register exists, the shadow-work proxy will overcount, reducing its specificity. [assumption; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html; justification: Q2 established that ITIL 4 emergency change handling is a reference model for the exception lane design]

**Analysis**

The evidence weights toward queue age (P75) and exception volume as the most valuable leading indicators in a split-authority system, for two reinforcing reasons. [inference; source: https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387; https://www.tocinstitute.org/five-focusing-steps.html] First, both metrics are measured at or near the approval constraint, consistent with TOC guidance to monitor the constraint itself rather than downstream output. [inference; source: https://www.tocinstitute.org/five-focusing-steps.html] Second, both metrics respond to changes in flow state before the non-linear congestion region is reached, because Little's Law implies quadratic or worse wait-time growth as utilisation approaches capacity; early detection in the linear region provides more response time. [inference; source: https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387]

Lead time trend and rework rate are more visible to senior stakeholders but fire later in the causal chain. Their value is as confirmation signals and as the response-severity calibrators once earlier signals have fired. [inference; source: https://dora.dev/guides/dora-metrics-four-keys/; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html]

The shadow-work proxy is structurally different from the other metrics: it is not a signal of the approval queue's health but a signal of the governance system's legitimacy as experienced by teams. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html] Rising shadow work predicts a different class of failure (undisclosed changes, compliance risk) rather than throughput collapse, and it requires a governance response (reducing intake friction) rather than a routing response (tightening the exception gate). [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html]

The four-tier warning structure maps cleanly onto the Q3 and Q5 response framework: Tier 1 and Tier 2 signals trigger investigation and classification review without changing routing; Tier 3 signals trigger Q5 control-regime tightening; Tier 4 signals trigger Q3 circuit-breakers. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q5-control-model-tradeoff.html] This graduated structure avoids over-reaction to transient spikes (which the multi-window design filters) while providing a clear escalation path when signals persist. [inference; source: https://sre.google/workbook/alerting-on-slos/]

**Risks, Gaps, and Uncertainties**

1. No published study directly validates specific numerical threshold values for approval queue indicators in split-authority governance systems; all threshold recommendations in this item are calibration heuristics. Organisations should treat the proposed values as starting points and calibrate against their own six-month baseline before deploying the bundle operationally. [inference; source: https://dora.dev/research/2024/dora-report/]

2. The shadow-work proxy (deployment-to-ticket gap) relies on deployment tooling and ticket systems being integrated; without automated deployment tracking, manual counting is required, which reduces reliability and timeliness. [assumption; justification: most modern delivery pipelines track deployments; the assumption may not hold for legacy or highly manual delivery environments]

3. The indicator bundle addresses the approval-gate constraint specifically. If the actual constraint in a given organisation is a testing environment bottleneck, a vendor dependency, or a staffing shortage rather than approval-gate congestion, the bundle will provide misleading early warning signals, and constraint identification (Q1) is required first. [assumption; source: https://www.tocinstitute.org/five-focusing-steps.html]

4. DORA research is primarily based on surveys of software delivery teams and may not fully represent the dynamics of regulated enterprise environments where approval queues involve legal, compliance, and risk functions with different service-time distributions than technical review functions. [inference; source: https://dora.dev/research/2024/dora-report/] The HITL capacity thresholds study confirms that regulated enterprises calibrate review-queue thresholds locally using supervisory guidance rather than universal survey benchmarks, reinforcing that DORA-derived starting values require regulatory-context adjustment. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-20-hitl-capacity-thresholds-in-banking-compliance.html]

**Open Questions**

1. What are the empirically validated threshold values for approval queue indicators in regulated enterprises? This would require a dedicated empirical study collecting baseline metrics and observing queue collapse events in split-authority environments.

2. Can the misclassification signal (rising exception share combined with declining rework) be made more reliable by adding a direct sampling process, rather than relying on the cross-indicator inference?

3. How should the indicator bundle be adapted for split-authority systems where the constraint is a regulatory review function rather than an internal approval gate? The service-time distribution for external regulatory review differs from internal approval, and Little's Law thresholds would need different calibration.

**Output**

Type: knowledge

Description: A compact six-metric early-warning bundle with four warning tiers, aligned to Q3 circuit-breakers and Q5 control-regime shifts, operationalising the P1 indicator families with threshold design principles grounded in Little's Law, DORA metrics, and SRE burn-rate alerting. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html; https://dora.dev/guides/dora-metrics-four-keys/; https://sre.google/workbook/alerting-on-slos/]

Key sources:
1. [DORA (2024) Software delivery metrics: throughput and instability](https://dora.dev/guides/dora-metrics-four-keys/)
2. [Google SRE Workbook: Alerting on Service Level Objectives](https://sre.google/workbook/alerting-on-slos/)
3. [Little, J.D.C. (1961) A proof for the queuing formula, Operations Research](https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387)

### §7 Recursive Review

```text
review_result: pass
acronym_audit: passed
  - WIP: Work in Progress (WIP) -- expanded at first use in Scope section
  - DORA: DevOps Research and Assessment (DORA) -- expanded at first narrative prose use in Context
  - SRE: Site Reliability Engineering (SRE) -- expanded at first narrative prose use in Context section, alongside DORA
  - SLO: Service Level Objective (SLO) -- expanded at first use in §2.B3
  - TOC: Theory of Constraints (TOC) -- expanded at first use in §2.B1
  - ITIL: Information Technology Infrastructure Library (ITIL) -- expanded in §2.B2 (shadow work confounder)
  - P75: 75th percentile -- defined in prose at first use in §2.A1
  - BCBS: Basel Committee on Banking Supervision (BCBS) -- expanded in §5 regulatory lens
  - AI: Artificial Intelligence (AI) -- expanded at first narrative prose use in §3 fact #3
  - HITL: Human-in-the-Loop (HITL) -- expanded at first use in §5 regulatory lens
  - HKMA: Hong Kong Monetary Authority (HKMA) -- expanded at first use in §5 regulatory lens
  - P1, Q2, Q3, Q4, Q5: internal labels described as "operating model synthesis (P1)" and the Q-series items are referenced by their full titles in Sources
claim_audit: all factual and inferential claims carry [fact], [inference], or [assumption] labels in Research Skill Output
findings_labels: Executive Summary and Analysis use suffix inline labels; Key Findings use trailing parenthetical format; Evidence Map claim cells begin with [fact], [inference], or [assumption]
parity_check: §6 Synthesis and ## Findings are aligned; no divergence
em_dash_scan: no em-dashes detected
ai_slop_scan: no "Furthermore", "Additionally", "It is important to note", "In conclusion", "it is worth noting", "Importantly" detected
```

---

## Findings

### Executive Summary

Five metric families, arranged into four warning tiers by causal distance from the approval constraint, constitute the minimum viable early-warning telemetry for split-authority delivery systems: queue age at the 75th percentile per lane, blocked-work ratio, exception volume as the four-week rolling Class 3 share of intake, lead time trend as a four-week moving average, and rework plus unplanned capacity share. [inference; source: https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html; https://dora.dev/guides/dora-metrics-four-keys/] A sixth proxy, the deployment-to-ticket gap, surfaces shadow-work growth, which signals governance-friction-driven compliance risk rather than throughput risk. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html] The tiered structure maps directly to the routing circuit-breakers in Q3 and the control-regime shift conditions in Q5, enabling pre-agreed automatic responses that eliminate per-incident deliberation cost. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q5-control-model-tradeoff.html] Threshold values must be calibrated to each organisation's baseline; the proposed starting-point values are design heuristics grounded in Little's Law, DORA, and SRE burn-rate alerting precedent rather than empirically universal constants. [assumption; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009; https://dora.dev/research/2024/dora-report/]

### Key Findings

1. Queue age at the 75th percentile per lane is the earliest observable warning of approval-gate congestion because Little's Law implies that queue length and wait time growth co-move, and the P75 responds to developing congestion before the median or mean. ([inference]; medium confidence; source: https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009)

2. Exception volume expressed as the four-week rolling Class 3 share of total intake is the most direct precursor to exception lane saturation and provides an estimated one to two weeks of warning before the Q3 circuit-breaker fires. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html)

3. DORA's change lead time, measured as a four-week moving average per lane, integrates approval-gate congestion and pipeline health into one observable and functions as a composite confirmation metric rather than a first-line signal; it is most useful when it rises in combination with earlier Tier 1 and Tier 2 signals. ([inference]; medium confidence; source: https://dora.dev/guides/dora-metrics-four-keys/; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html)

4. A deployment rework rate sustained above 20% of total deployments for two or more consecutive sprints signals that unplanned remediation work is consuming capacity that would otherwise be available for planned delivery, consistent with the SRE toil threshold at which reactive work becomes structurally damaging. ([inference]; medium confidence; source: https://sre.google/workbook/eliminating-toil/; https://dora.dev/guides/dora-metrics-four-keys/)

5. A persistent deployment-to-ticket gap exceeding 10% for three or more consecutive sprints signals systematic shadow-work growth, which predicts either escalating compliance risk from undisclosed changes or a future formal-queue surge when the informal backlog is regularised under audit pressure. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html)

6. Multi-window threshold design, requiring simultaneous breach of a short-window (one to two weeks) and a long-window (four weeks) check before an alert fires, reduces false positives from batch-arrival spikes while preserving detection speed for sustained congestion, applying the same alerting design principle demonstrated in SRE error budget burn-rate practice. ([inference]; medium confidence; source: https://sre.google/workbook/alerting-on-slos/; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009)

7. Rising exception share combined with a stable or declining rework rate signals deliberate misclassification of exception-path work as fast-path work, a behavioural coping response to governance friction that undermines routing integrity without triggering the standard exception volume alarm. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html)

8. Pre-agreed thresholds aligned to Q3 circuit-breaker conditions and Q5 control-regime shift points enable automatic regime adjustments without per-incident negotiation, following the same operational logic as the SRE error budget policy, which removed deliberation cost from the high-stakes decision of whether to continue feature deployment or switch to reliability-first operations. ([inference]; medium confidence; source: https://sre.google/workbook/alerting-on-slos/; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q5-control-model-tradeoff.html)

9. The specific starting-point threshold values proposed (P75 age rising across two consecutive measurements; exception share rising five percentage points over four weeks; 20% unplanned capacity share for two sprints; 10% deployment-to-ticket gap for three sprints) are design heuristics that must be calibrated against each organisation's six-month baseline before operational deployment. ([assumption]; medium confidence; source: https://dora.dev/research/2024/dora-report/; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009; justification: no published study provides universal threshold values for approval queue leading indicators)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Queue age P75 earliest warning; Little's Law co-movement of length and wait time | https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009 | medium | Key Finding 1 |
| [inference] Exception volume direct precursor to Q3 circuit-breaker; 1-2 week warning window | https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html | medium | Key Finding 2 |
| [fact] DORA five metrics: lead time, deployment frequency, change failure rate, failed deployment recovery time, deployment rework rate | https://dora.dev/guides/dora-metrics-four-keys/ | high | Key Findings 3, 4 basis |
| [inference] Lead time trend integrates approval congestion and pipeline health; confirmation metric not first-line signal | https://dora.dev/guides/dora-metrics-four-keys/; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html | medium | Key Finding 3 |
| [fact] SRE toil: repetitive reactive work scaling with load; keep below 50% of team capacity | https://sre.google/workbook/eliminating-toil/ | high | Key Finding 4 basis |
| [inference] Rework rate above 20% for 2 sprints competes with planned delivery capacity | https://sre.google/workbook/eliminating-toil/; https://dora.dev/guides/dora-metrics-four-keys/ | medium | Key Finding 4 |
| [inference] Deployment-to-ticket gap signals shadow work; predicts compliance risk or formal-queue surge | https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html | medium | Key Finding 5 |
| [fact] SRE multi-window burn-rate: simultaneous short and long window breach required; improves precision | https://sre.google/workbook/alerting-on-slos/ | high | Key Finding 6 basis |
| [inference] Multi-window applied to approval queue reduces false positives from batch arrivals | https://sre.google/workbook/alerting-on-slos/; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009 | medium | Key Finding 6 |
| [inference] Rising exception share plus declining rework = misclassification signal; coping behaviour | https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html | medium | Key Finding 7 |
| [inference] Pre-agreed thresholds enable automatic regime shifts; SRE error budget policy precedent | https://sre.google/workbook/alerting-on-slos/; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q5-control-model-tradeoff.html | medium | Key Finding 8 |
| [assumption] Threshold values are calibration heuristics; must be set against 6-month baseline | https://dora.dev/research/2024/dora-report/; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009 | medium | Key Finding 9 |

### Assumptions

1. The exception review function is the binding flow constraint in the split-authority system; if a testing environment, vendor dependency, or staffing shortage is the actual constraint, the indicator bundle must be re-anchored to that constraint, and Q1 constraint identification must be completed first. [assumption; source: https://www.tocinstitute.org/five-focusing-steps.html; justification: P1, Q3, and Q5 all treat governance-generated queueing as the dominant constraint; this assumption is consistent with the series but has not been independently validated]

2. Emergency changes processed under a registered emergency change practice are excluded from the shadow-work proxy; if no such register exists, the proxy overstates shadow-work growth, reducing its specificity. [assumption; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html; justification: Q2 uses ITIL 4 emergency change as a reference model; the assumption extends that design to the measurement layer]

3. The proposed threshold values are calibration starting points; each organisation should collect six months of baseline data before operationalising the warning bundle, since natural variation in queue age and exception volume differs across delivery contexts. [assumption; source: https://dora.dev/research/2024/dora-report/; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009; justification: DORA explicitly warns against applying metrics without context; Reinertsen emphasises calibrating WIP limits empirically]

### Analysis

Monitoring queue dynamics through a tiered indicator bundle requires understanding the causal chain: intake volume and mix drive approval-gate service capacity toward queue age and WIP accumulation, then toward lead time growth, rework rate increase, and, if unchecked, shadow-work proliferation as teams adopt coping strategies. [inference; source: https://www.tocinstitute.org/five-focusing-steps.html; https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html] Non-linear queueing dynamics imply that wait time growth accelerates as utilisation approaches capacity, which means early indicators (Tier 1 and Tier 2) provide proportionally more response time than late indicators (Tier 3 and Tier 4). [inference; source: https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387] This asymmetry justifies the investment in queue-age and exception-volume monitoring even when those metrics are harder to automate than lead time, which is directly available from most delivery pipeline tools. [inference; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009]

Shadow-work proxy signals require separate treatment in the analysis because a rising proxy indicates a different failure mode: governance-legitimacy collapse rather than throughput collapse. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html] When shadow-work growth rises, the response is to reduce intake friction (make the formal process easier than the informal path) rather than to tighten routing controls. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html] Tightening controls in response to shadow-work growth typically accelerates the coping behaviour rather than reversing it. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html]

Key Finding 7 (misclassification signal) is a cross-indicator inference: neither rising exception share alone nor declining rework rate alone constitutes the signal; only the combination does. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html] This makes it harder to automate but important to include, because misclassification erodes the integrity of the demand-segmentation model without producing an obvious throughput signal until field defects materialise. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html]

### Risks, Gaps, and Uncertainties

1. No empirical study directly validates threshold values for approval queue leading indicators in regulated split-authority governance systems; all proposed values are heuristics. The evidence base for threshold design comes from analogous domains (SRE, product development flow) rather than from direct observation of approval-gate congestion events. [inference; source: https://dora.dev/research/2024/dora-report/]

2. DORA survey data primarily reflects software development team experience and may not fully represent regulated enterprise environments where compliance and risk functions with different staffing, skill, and authority structures form part of the approval chain. [inference; source: https://dora.dev/research/2024/dora-report/] The completed HITL capacity thresholds study confirms that regulated enterprises calibrate review-queue thresholds locally using supervisory guidance (such as HKMA requirements for clear internal timelines) rather than universal benchmarks, reinforcing that DORA-derived starting values require regulatory-context adjustment before operational deployment. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-20-hitl-capacity-thresholds-in-banking-compliance.html]

3. The shadow-work proxy depends on integrated deployment tracking and ticket systems; organisations with manual or fragmented toolchains will have difficulty operationalising it without additional instrumentation investment. [assumption; justification: most modern cloud-native delivery pipelines have automated deployment tracking; legacy environments may not]

4. The constraint assumption (that exception review is the binding constraint) has not been validated as a standalone Q1 research item; the indicator bundle is correctly calibrated only for approval-gate-constrained systems. [assumption; source: https://www.tocinstitute.org/five-focusing-steps.html]

### Open Questions

1. What threshold values for approval queue indicators have been observed to predict queue collapse events in regulated enterprise environments? A dedicated empirical study collecting baseline metrics and observing saturation events would provide the calibration evidence this item lacks.

2. Can the misclassification signal be operationalised more reliably by adding a periodic classification-accuracy audit (sampling recent Class 3 items against the Q2 boundary tests) rather than relying solely on the cross-indicator combination?

3. How should the indicator bundle be adapted when the binding constraint is an external regulatory review body rather than an internal approval gate? External review service-time distributions are different, and Little's Law calibration would require different baseline assumptions.

4. Does the multi-window alerting design translate from SRE error budgets (continuous event streams) to approval queues (discrete batch events) without modification, or does the lower event frequency require different window lengths?
