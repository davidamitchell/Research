---
title: "Q5: Control model for the best throughput-risk trade-off"
added: 2026-05-29
status: reviewing
priority: high
tags: [control-model, governance-patterns, throughput-risk, delegation]
blocks: [2026-05-29-split-authority-q2-demand-segmentation, 2026-05-29-split-authority-q3-routing-exception-isolation, 2026-05-29-split-authority-q4-decision-rights-placement]
started: 2026-05-31T11:29:07+00:00
completed: ~
output: [knowledge]
cites:
  - 2026-05-29-split-authority-q2-demand-segmentation
  - 2026-05-29-split-authority-q3-routing-exception-isolation
  - 2026-05-29-split-authority-q4-decision-rights-placement
  - 2026-05-29-split-authority-p1-operating-model-synthesis
  - 2026-05-23-governance-controls-effectiveness-conditions
  - 2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention
related:
  - 2026-05-20-hitl-capacity-thresholds-in-banking-compliance
  - 2026-04-26-ai-lowcode-risk-tier-classification-controls
  - 2026-04-26-agentic-ai-regulatory-preconditions-control-failure-assessment
supersedes: ~
superseded_by: []
item_type: primary
confidence: medium
themes:
  - governance-policy
  - organisational-design
  - cost-performance
  - enterprise-adoption
  - regulatory-compliance
versions: []
review_count: 1
---

# Q5: Control model for the best throughput-risk trade-off

## Research Question

When should the system use pre-approval, bounded delegation with guardrails, or post-hoc review and exception escalation?

## Scope

**In scope:**
- Comparative evaluation of control regimes under different demand/routing/decision-right conditions.
- Conditions under which controls should tighten or relax.

**Out of scope:**
- Defining leading-indicator bundles (handled in Q6).

**Constraints:**
- Must use Q2, Q3, and Q4 findings as prerequisites.

## Context

Q5 consolidates governance pattern choices into one throughput-risk trade-off problem: preserve control without generating approval-queue explosion. It enables P1. The three control patterns evaluated are pre-approval (a preventive control, requiring authority sign-off before work proceeds), bounded delegation with guardrails (a hybrid control, where authority is pre-delegated within defined parameters with escalation triggers), and post-hoc review and exception escalation (a detective control, where work proceeds and is reviewed after completion or when escalation conditions fire).

## Approach

1. Define control-pattern alternatives and their operating assumptions.
2. Compare queue and risk outcomes across control patterns.
3. Produce a conditional control-selection matrix with escalation rules.

## Sources

- [Google SRE Workbook: Error Budget Policy](https://sre.google/workbook/error-budget-policy/)
- [Google SRE Book: Embracing Risk](https://sre.google/sre-book/embracing-risk/)
- [COSO Internal Control Integrated Framework guidance](https://www.coso.org/guidance-on-ic)
- [Williamson (1979) Transaction-Cost Economics: The Governance of Contractual Relations](https://www.jstor.org/stable/725118)
- [PeopleCert / AXELOS ITIL 4 Change Enablement](https://www.axelos.com/certifications/itil-service-management/what-is-itil)
- [Adler and Borys (1996) Two types of bureaucracy: enabling and coercive](https://eric.ed.gov/?id=EJ525938)
- [Mitchell (2026) Q2: Demand segmentation for fast-path vs controlled-path flow](https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html)
- [Mitchell (2026) Q3: Routing design that isolates exceptions from routine flow](https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html)
- [Mitchell (2026) Q4: Decision rights that should move closer to execution](https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q4-decision-rights-placement.html)
- [Mitchell (2026) P1: Operating model synthesis for split-authority delivery](https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html)
- [Mitchell (2026) Internal governance controls: effectiveness conditions in regulated enterprises](https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html)

---

## Research Skill Output

### §0 Initialise

Question: When should the system use pre-approval, bounded delegation with guardrails, or post-hoc review and exception escalation?

Scope:
- In scope: comparative evaluation of control regimes under different demand/routing/decision-rights conditions; conditions under which controls should tighten or relax
- Out of scope: Q6 leading-indicator bundle design
- Constraints: Q2, Q3, and Q4 findings are prerequisites; the three control patterns must be evaluated against the demand classes and decision types established in those items

The three control patterns in scope are:
1. Pre-approval: a preventive control requiring authority sign-off before work proceeds. The Committee of Sponsoring Organizations of the Treadway Commission (COSO) classifies this as operating "before the event or activity occurs." [fact; source: https://www.coso.org/guidance-on-ic]
2. Bounded delegation with guardrails: a hybrid control in which authority is pre-delegated to delivery teams within defined parameters, with escalation triggers that fire when parameters are breached. This maps to Williamson's hybrid governance structure (between market and hierarchy). [inference; source: https://www.jstor.org/stable/725118]
3. Post-hoc review and exception escalation: a detective control in which work proceeds and is reviewed after completion, with escalation fired by observable item-level or system-level triggers. COSO classifies this as operating "after the event or activity." [fact; source: https://www.coso.org/guidance-on-ic]

Output format: conditional control-selection matrix with escalation rules; knowledge output.

Prior work:
- Q2 established three demand classes (Class 1: fast path; Class 2: standard path; Class 3: exception path) and three boundary tests (template test, recovery test, blast radius test). [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html]
- Q3 established three-lane physical routing with Work in Progress (WIP) limit on the exception lane, three item-level escalation triggers, and two system-level circuit-breaker triggers. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html]
- Q4 established six execution decision categories that should be delegated, with three governance parameters (cost ceiling, blast radius limit, approved technology catalog) and four binary escalation triggers (catalog deviation, ceiling breach, blast radius overflow, external commitment). [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q4-decision-rights-placement.html]
- P1 identified demand segmentation + bounded delegation + named integrator + indicator bundle + trigger-based regime shifts as the operating model for split-authority delivery. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html]

### §1 Question Decomposition

The main question decomposes into four atomic sub-questions:

**A. What is the correct control pattern assignment for each demand class from Q2?**
- A1: What control pattern is appropriate for Class 1 (fast-path, pre-authorised) work?
- A2: What control pattern is appropriate for Class 2 (standard-path, assessed per-instance) work?
- A3: What control pattern is appropriate for Class 3 (exception-path, full expert review) work?

**B. What are the selection criteria that determine which control pattern applies?**
- B1: What transaction-level properties determine control intensity (following transaction cost economics)?
- B2: How do reversibility, blast radius, and standardisation (the Q2 axes) map to control pattern selection?
- B3: How does decision velocity requirement (the incident response constraint from Q4) modify control pattern selection?

**C. Under what conditions should control regimes tighten or relax?**
- C1: What observable signals trigger tightening (shift toward pre-approval)?
- C2: What observable signals permit relaxing (shift toward bounded delegation or post-hoc review)?
- C3: How does the Site Reliability Engineering (SRE) error budget policy operationalise trigger-based regime shifts?

**D. What is the throughput and risk outcome comparison across the three control patterns?**
- D1: What is the throughput cost (queue latency) of pre-approval vs bounded delegation vs post-hoc review?
- D2: What is the residual risk under each control pattern for each demand class?
- D3: What conditions make the residual risk of post-hoc review acceptable for Class 1 work?

### §2 Investigation

**§2.A: Control pattern assignment for each demand class**

The Q2 demand segmentation item established that the three classification axes (risk level, reversibility, standardisation) are the operative criteria for assigning work to a class. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html] The selection of control pattern follows directly from class assignment, once the control pattern's cost-benefit profile for that class is established.

COSO's internal control framework distinguishes three control types by timing:
- Preventive controls operate before the event: pre-approval is the canonical preventive control.
- Detective controls operate after the event: post-hoc review and exception escalation are detective controls.
- Corrective controls operate after detection: these support exception escalation resolution.
[fact; source: https://www.coso.org/guidance-on-ic]

The COSO selection criterion is: higher-risk and higher-materiality items justify preventive controls because the cost of ex-post detection and remediation exceeds the cost of ex-ante review. Lower-risk, high-volume items use detective controls because the cost of pre-approval exceeds the residual risk. [inference; source: https://www.coso.org/guidance-on-ic]

Transaction Cost Economics (TCE) as developed by Oliver Williamson provides the theoretical underpinning. Williamson (1979) argues that governance structure should be chosen to minimise transaction costs: market-like governance (low control intensity) is efficient when uncertainty is low and transactions are standardised; hierarchical governance (high control intensity) is required when uncertainty is high, asset specificity is high (meaning relationship-specific investment that loses value outside the focal relationship), or consequences of contracting failure are severe. [fact; source: https://www.jstor.org/stable/725118] Hybrid governance (bounded delegation) is appropriate at intermediate levels of uncertainty and asset specificity. [inference; source: https://www.jstor.org/stable/725118]

Applying TCE to the Q2 demand classes:
- Class 1 (reversible, contained, template exists): low uncertainty (the template eliminates most information asymmetry), low asset specificity (the work matches a known pattern), low consequence of failure (blast radius is contained and rollback is tested). TCE predicts market-like governance, which maps to post-hoc review. [inference; source: https://www.jstor.org/stable/725118; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html]
- Class 2 (reversible to moderate, bounded, pattern-based): moderate uncertainty (instance varies from the template but within known bounds), moderate asset specificity (bounded relationship-specific investment), moderate consequence. TCE predicts hybrid governance, which maps to bounded delegation with guardrails. [inference; source: https://www.jstor.org/stable/725118; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html]
- Class 3 (novel or irreversible, system-wide potential blast radius): high uncertainty, high consequence, potentially high asset specificity. TCE predicts hierarchical governance, which maps to pre-approval. [inference; source: https://www.jstor.org/stable/725118; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html]

The IT Service Management (ITSM) framework Information Technology Infrastructure Library (ITIL) 4 Change Enablement reaches the same assignment from a different starting point: standard changes (low-risk, documented, repeatable) are pre-authorised; normal changes require assessed per-instance approval; emergency changes require the Emergency Change Advisory Board (ECAB). [inference; source: https://www.axelos.com/certifications/itil-service-management/what-is-itil] This maps standard = Class 1/post-hoc, normal = Class 2/bounded delegation, emergency = Class 3/pre-approval.

DevOps Research and Assessment (DORA) research confirms that elite delivery organisations achieve high deployment frequency for standard work by pre-authorising low-risk changes, while retaining review for high-risk changes. [inference; source: https://dora.dev/guides/dora-metrics-four-keys/]

**§2.B: Selection criteria for control pattern assignment**

The governance controls effectiveness conditions item in this corpus identified five properties that, when combined, predict whether a governance control minimises coordination cost: (1) proportionality to transaction hazard, (2) clear ownership and authority, (3) authoritative inputs, (4) proportionate trigger conditions, and (5) periodic review cadence. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html]

Five selection criteria for choosing among the three control patterns emerge from combining TCE, COSO, and the prior Q2-Q4 findings:

1. **Reversibility**: If the failure mode has a tested rollback procedure (Q2 recovery test passes), post-hoc review is permissible because detected failure can be corrected before material harm accumulates. If the transaction is irreversible or the rollback is untested, pre-approval is required. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html; https://sre.google/sre-book/embracing-risk/]

2. **Blast radius**: If potential impact is contained within a defined boundary (Q2 blast radius test passes), post-hoc review is permissible. If blast radius is system-wide or cross-boundary, pre-approval is required. At intermediate values, bounded delegation with blast radius as a parameter ceiling is appropriate. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html; https://aws.amazon.com/blogs/architecture/empower-your-teams-with-modern-architecture-governance/]

3. **Standardisation**: If a pre-approved documented pattern exists (Q2 template test passes), the pattern itself constitutes the ex-ante governance; post-hoc review confirms adherence. If the pattern exists but the instance varies, bounded delegation with the pattern as the guardrail is appropriate. If no pattern exists, pre-approval is required. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html; https://www.axelos.com/certifications/itil-service-management/what-is-itil]

4. **Decision velocity requirement**: The Q4 item established that incident response decisions must sit with delivery teams because external approval latency is structurally incompatible with the five-minute response window for services targeting four nines (99.99%) availability. [fact; source: https://sre.google/workbook/incident-response/; https://sre.google/sre-book/being-on-call/] Where response time is time-critical (incident, emergency), bounded delegation or post-hoc review is the only viable pattern; pre-approval is structurally excluded.

5. **Detection velocity**: Post-hoc review is only risk-acceptable if failure is detectable before material harm accumulates. Automated monitoring (error rate, blast radius alerts, SLO burn rate) provides near-real-time detection for Class 1 work; for work where failures are silent or slow-developing, post-hoc review is insufficient and pre-approval is required. [inference; source: https://sre.google/sre-book/embracing-risk/; https://sre.google/workbook/error-budget-policy/]

**§2.C: Trigger-based regime shifts (tightening and relaxing)**

The SRE error budget policy provides the clearest real-world example of a trigger-based control regime shift. Under the Google SRE error budget policy:
- During normal operations (service within Service Level Objective [SLO]): bounded delegation applies; deployments proceed according to release policy. This is the "relax" state.
- When error budget is exhausted (service below SLO target): pre-approval applies; a deployment freeze is enacted on all changes except P0 issues and security fixes. This is the "tighten" state.
[fact; source: https://sre.google/workbook/error-budget-policy/]

The error budget is defined as 1 minus the SLO: a 99.9% SLO service has a 0.1% error budget. [fact; source: https://sre.google/workbook/error-budget-policy/] The trigger is therefore a measurable threshold breach, not a subjective judgment. [fact; source: https://sre.google/workbook/error-budget-policy/]

The Q3 item established two system-level circuit-breaker triggers: exception volume ratio above a calibrated threshold (tighten the fast-path gate), and exception lane WIP limit saturation (ration all-lane intake). [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html] These map directly to SRE error budget policy: the exception volume ratio is analogous to the error budget burn rate; WIP limit saturation is analogous to budget exhaustion.

For relaxing (shifting from pre-approval back toward bounded delegation or post-hoc review), the Q3 circuit-breaker triggers imply:
- Exception volume ratio falls below threshold and stays below it for a calibrated observation window: tightened fast-path gate can be relaxed.
- Error budget recovers above the threshold: deployment freeze can be lifted (SRE model explicitly permits lifting the freeze once SLO compliance is restored). [fact; source: https://sre.google/workbook/error-budget-policy/]
- Post-hoc review over a calibrated period confirms Class 1 work is consistently meeting its boundary conditions with no boundary-test failures: the template catalogue is valid and the post-hoc detective control is working. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html; https://www.axelos.com/certifications/itil-service-management/what-is-itil]

**§2.D: Throughput and risk comparison across control patterns**

Pre-approval's throughput cost is proportional to approval latency times decision frequency. The P1 item established that governance-generated queueing (approval latency, multi-party coordination overhead, fragmented decision rights) is the dominant flow constraint in split-authority delivery systems. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html] Applying pre-approval to all demand converts the approval gate into the constraint and prevents throughput improvement by adding headcount at non-constraint positions, as established by the Theory of Constraints. [inference; source: https://www.tocinstitute.org/five-focusing-steps.html; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html]

Bounded delegation's throughput cost is limited to parameter maintenance and escalation handling overhead. Because the parameters pre-authorise the delegation, decisions within parameters do not generate approval queue latency. The Q4 item found that the governance parameters (cost ceiling, blast radius limit, approved catalog) pre-bound the risk, so the residual governance value of per-decision approval falls to near zero. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q4-decision-rights-placement.html]

Post-hoc review's throughput cost is minimal (review happens after work completes, so it does not block throughput). Its risk cost is the gap between failure occurrence and detection. Automated monitoring closes this gap for reversible, contained work where failure signals are strong (SLO burn rate, error rate, blast radius alert). [inference; source: https://sre.google/sre-book/embracing-risk/; https://sre.google/workbook/error-budget-policy/]

The residual risk under each control pattern:
- Pre-approval applied to Class 1 work: residual risk is near zero but the control is misaligned (the throughput cost exceeds the risk reduction value because the work is reversible and contained by definition). [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html; https://www.jstor.org/stable/725118]
- Bounded delegation applied to Class 2 work: residual risk is limited to the gap between parameter boundary and actual blast radius; the four escalation triggers (catalog deviation, ceiling breach, blast radius overflow, external commitment) close this gap for the scenarios where it matters. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q4-decision-rights-placement.html]
- Post-hoc review applied to Class 1 work: residual risk is the probability of failure times the detection lag times the harm rate. For reversible, contained work with automated monitoring, this product is acceptably small. [inference; source: https://sre.google/sre-book/embracing-risk/; https://sre.google/workbook/error-budget-policy/]
- Pre-approval applied to Class 3 work: this is the appropriate match. Pre-approval's throughput cost is acceptable for low-frequency, high-consequence items where the ex-ante review adds genuine risk-reduction value. [inference; source: https://www.jstor.org/stable/725118; https://www.axelos.com/certifications/itil-service-management/what-is-itil]

The governance failure mechanisms item in this corpus documents that applying coercive controls uniformly to all work generates workaround behaviour (deliberate mis-classification, shadow workflows, informal approval channels). [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html] The Adler and Borys (1996) distinction between enabling and coercive formalisation confirms that controls perceived as coercive generate resistance; controls perceived as enabling (providing authoritative templates, clear escalation paths) support compliance. [inference; source: https://eric.ed.gov/?id=EJ525938]

The conditional control-selection matrix that follows from this analysis:

| Demand class | Reversibility | Blast radius | Standardisation | Decision velocity | Control pattern |
|---|---|---|---|---|---|
| Class 1 | Reversible, tested rollback | Contained | Template exists | Normal or time-critical | Post-hoc review |
| Class 2 | Reversible to moderate | Bounded by parameter | Pattern-based | Normal | Bounded delegation |
| Class 3 | Irreversible or untested rollback | System-wide | Novel | Low-frequency | Pre-approval |
| Any class (tightened state) | Any | Any | Any | Normal | Shift one level toward pre-approval |
| Any class (relaxed state post-sustained-compliance) | Reversible | Contained | Template confirmed valid | Normal | Maintain or shift one level toward post-hoc |

### §3 Reasoning

Removing narrative glue, the causal chain is:

1. The Q2 boundary tests (template, recovery, blast radius) produce a class assignment. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html]
2. Class assignment determines the baseline control pattern (Class 1: post-hoc; Class 2: bounded delegation; Class 3: pre-approval) via TCE discriminating alignment: governance intensity should match transaction hazard. [inference; source: https://www.jstor.org/stable/725118]
3. Decision velocity requirement overrides class assignment for time-critical decisions: pre-approval is structurally excluded when response time is incompatible with approval latency. [fact; source: https://sre.google/workbook/incident-response/]
4. Flow state (exception volume ratio, error budget burn rate) can temporarily upgrade the control pattern one level (from post-hoc to bounded delegation, or from bounded delegation to pre-approval) when threshold breaches indicate systemic risk elevation. [inference; source: https://sre.google/workbook/error-budget-policy/; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html]
5. Sustained compliance over a calibrated observation window permits downgrading the control pattern one level. [inference; source: https://sre.google/workbook/error-budget-policy/; https://www.axelos.com/certifications/itil-service-management/what-is-itil]
6. Detection velocity sets the minimum acceptable post-hoc review window: if failures are silent or slow-developing, post-hoc review is insufficient regardless of class assignment. [inference; source: https://sre.google/sre-book/embracing-risk/]

### §4 Consistency Check

```text
contradiction_scan: no internal contradictions identified
cross_item_consistency: class assignment from Q2 maps cleanly to control patterns
  - Class 1 template/recovery/blast-radius tests pass -> post-hoc is consistent with Q2 conservative-default rule
  - Class 3 novel/irreversible -> pre-approval consistent with Q2 conservative default
scope_guardrail: leading-indicator bundle (Q6) not duplicated here; conditions reference Q3 circuit breakers
  without re-defining their thresholds
sre_analogy_scope: error-budget policy is an analogy, not a claim that all split-authority systems use SLO logic;
  used to illustrate trigger-based regime shift mechanism
confidence_adjustment: all key findings held at medium; no primary cross-firm experimental comparison
  of control patterns in split-authority delivery
tcf_claim_scope: TCE discriminating alignment is applied as a mapping principle, not as empirically validated
  in this specific domain; held at inference with medium confidence
```

### §5 Depth and Breadth Expansion

**Regulatory dimension**: Basel Committee on Banking Supervision (BCBS) 328 requires that control intensity be proportionate to risk profile and that all material responsibilities have named owners with escalation paths. [fact; source: https://www.bis.org/bcbs/publ/d328.pdf] The conditional control-selection matrix is structurally consistent with this requirement: Class 3 work (high consequence) carries pre-approval, which provides the named authority and escalation structure; Class 1 and 2 work operates under bounded delegation with documented parameters and escalation triggers, satisfying the "named responsibility" requirement without per-item pre-approval. [inference; source: https://www.bis.org/bcbs/publ/d328.pdf; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html]

The Human-in-the-Loop (HITL) capacity thresholds item in this corpus found that when review volume exceeds human capacity, nominal pre-approval collapses into rubber-stamping, losing meaningful challenge while retaining all the throughput cost of pre-approval. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-20-hitl-capacity-thresholds-in-banking-compliance.html] Restricting pre-approval to Class 3 work therefore prevents the capacity-exhaustion failure mode: pre-approval applied to Class 1 and 2 volume quickly exceeds meaningful review capacity, producing both high latency and low risk reduction simultaneously. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-20-hitl-capacity-thresholds-in-banking-compliance.html; https://sre.google/sre-book/embracing-risk/]

**Economic dimension**: The SRE "embracing risk" model explicitly frames the control selection decision as a cost-benefit problem: "an incremental improvement in reliability may cost 100x more than the previous increment." [fact; source: https://sre.google/sre-book/embracing-risk/] This confirms that the throughput cost of pre-approval for Class 1 work is not offset by a proportionate risk reduction when the work is reversible and contained.

**Behavioural dimension**: The governance failure mechanisms item documents that the dominant failure mode is deliberate mis-classification of Class 2 or 3 work as Class 1 to avoid governance overhead. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html] The conditional control-selection matrix should therefore be designed to make the Class 1 post-hoc path fast but auditable: legible boundary tests reduce the incentive to claim Class 1 inappropriately, while the WIP limit on the exception lane (from Q3) removes the incentive to inflate exception status for priority service. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html; https://eric.ed.gov/?id=EJ525938]

**Historical dimension**: The ITIL 4 Change Enablement framework represents decades of enterprise governance experience with the same control-pattern selection problem. ITIL 4 endorses automated pre-approval for standard (Class 1 equivalent) changes, per-instance review for normal (Class 2 equivalent) changes, and rapid ECAB convening for emergency (Class 3 equivalent) changes. [inference; source: https://www.axelos.com/certifications/itil-service-management/what-is-itil] This is converging validation from a practitioner governance framework that predates the SRE framing.

### §6 Synthesis

The control-selection question reduces to a demand class-to-control-pattern mapping, governed by five selection criteria (reversibility, blast radius, standardisation, decision velocity, detection velocity) and four conditional modifiers (tighten trigger, relax trigger, velocity override, detection-gap override).

**Executive Summary**

Post-hoc review is the correct control pattern for Class 1 work, bounded delegation is the correct pattern for Class 2 work, and pre-approval is the correct pattern for Class 3 work, with the class assignment determined by the three Q2 boundary tests (template, recovery, blast radius). [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html; https://www.jstor.org/stable/725118; https://www.coso.org/guidance-on-ic] This mapping is supported by TCE discriminating alignment (governance intensity should match transaction hazard), the COSO preventive-detective distinction, ITIL 4 Change Enablement practice, and the SRE error budget policy as a concrete implementation of trigger-based regime shifts. [inference; source: https://www.jstor.org/stable/725118; https://www.coso.org/guidance-on-ic; https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://sre.google/workbook/error-budget-policy/] Applying pre-approval to Class 1 work imposes approval-queue latency without proportionate risk reduction, because the boundary tests that qualify Class 1 work already confirm reversibility, contained blast radius, and pattern adherence. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html; https://sre.google/sre-book/embracing-risk/] Two observable triggers (exception volume ratio above threshold and error budget exhausted) shift the control regime one level toward pre-approval temporarily; two observable conditions (exception volume ratio below threshold for a sustained window and post-hoc review confirming sustained Class 1 compliance) permit shifting one level toward post-hoc review. [inference; source: https://sre.google/workbook/error-budget-policy/; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html]

**Key Findings**

1. Post-hoc review (a detective control operating after the event) is the correct and sufficient control for Class 1 work because the three Q2 boundary tests already provide the ex-ante governance: a passing template test confirms pattern adherence, a passing recovery test confirms reversibility, and a passing blast radius test confirms contained impact, leaving post-hoc review to confirm adherence and update the template catalogue. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html; https://www.coso.org/guidance-on-ic; https://www.axelos.com/certifications/itil-service-management/what-is-itil)

2. Bounded delegation with guardrails (a hybrid governance structure in TCE terms) is the correct control for Class 2 work, in which the three Q4 parameters (cost ceiling, blast radius limit, approved technology catalog) and four escalation triggers (catalog deviation, ceiling breach, blast radius overflow, external commitment) together constitute the control, replacing per-decision pre-approval while preserving governance outcomes for the boundary cases that matter. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q4-decision-rights-placement.html; https://www.jstor.org/stable/725118)

3. Pre-approval is the correct control for Class 3 work (novel, irreversible, or system-wide blast radius), where high uncertainty and high consequence of contracting failure justify the throughput cost of ex-ante review, consistent with TCE hierarchical governance and ITIL 4's ECAB model for emergency and novel-consequence changes. ([inference]; medium confidence; source: https://www.jstor.org/stable/725118; https://www.axelos.com/certifications/itil-service-management/what-is-itil)

4. Decision velocity requirement is an override criterion: time-critical decisions (incident response, emergency mitigation) cannot use pre-approval regardless of class assignment because approval latency is structurally incompatible with the five-minute response window for services targeting four nines (99.99%) availability, and must instead use pre-delegated Incident Command System (ICS) authority with post-hoc review. ([fact]; medium confidence; source: https://sre.google/workbook/incident-response/; https://sre.google/sre-book/being-on-call/)

5. Detection velocity sets the boundary condition for post-hoc review acceptability: post-hoc review is only risk-acceptable when automated monitoring can detect failure before material harm accumulates, as demonstrated by the SRE error budget burn rate as a near-real-time detection mechanism for Class 1 deployment failures. ([inference]; medium confidence; source: https://sre.google/sre-book/embracing-risk/; https://sre.google/workbook/error-budget-policy/)

6. The SRE error budget policy operationalises a trigger-based regime shift from bounded delegation (normal operations, below SLO budget threshold) to pre-approval (deployment freeze when error budget is exhausted), providing a concrete real-world example of automatic control-pattern escalation governed by a measurable threshold rather than a subjective judgment. ([fact]; medium confidence; source: https://sre.google/workbook/error-budget-policy/)

7. Applying pre-approval to Class 1 work generates approval-queue latency without proportionate risk reduction, because the work is reversible and contained by definition; this pattern constitutes a coercive formalisation in Adler and Borys (1996) terms and predictably generates mis-classification and workaround behaviour as documented in the governance failure mechanisms item. ([inference]; medium confidence; source: https://eric.ed.gov/?id=EJ525938; https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html)

8. Two observable conditions trigger temporary tightening of the control regime by one level: exception volume ratio above a calibrated threshold (from the Q3 circuit-breaker model), and error budget exhaustion (from the SRE error budget policy); both conditions indicate that the current class boundary tests are failing to contain risk at their defined levels. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html; https://sre.google/workbook/error-budget-policy/)

9. Two observable conditions permit relaxing the control regime by one level: exception volume ratio below threshold sustained over a calibrated observation window, and post-hoc review over the same window confirming that Class 1 work consistently meets its boundary conditions without in-flight escalation; the SRE model explicitly permits lifting the deployment freeze once SLO compliance is restored. ([inference]; medium confidence; source: https://sre.google/workbook/error-budget-policy/; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html)

10. The Human-in-the-Loop capacity constraint (from the HITL capacity thresholds item in this corpus) provides an independent upper bound on how much work can be routed through pre-approval before meaningful review collapses into rubber-stamping; the conditional control-selection matrix must therefore be designed so that Class 3 volume stays within the genuine review capacity of the authority responsible for pre-approval. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-20-hitl-capacity-thresholds-in-banking-compliance.html; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html)

**Evidence Map**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Post-hoc review is correct and sufficient for Class 1: Q2 boundary tests provide the ex-ante governance | https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html; https://www.coso.org/guidance-on-ic; https://www.axelos.com/certifications/itil-service-management/what-is-itil | medium | Convergence from TCE, COSO, ITIL 4, and Q2 |
| [inference] Bounded delegation is correct for Class 2: Q4 parameters + escalation triggers constitute the control | https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q4-decision-rights-placement.html; https://www.jstor.org/stable/725118 | medium | TCE hybrid governance; Q4 bounded delegation design |
| [inference] Pre-approval is correct for Class 3: high uncertainty, high consequence justify ex-ante review | https://www.jstor.org/stable/725118; https://www.axelos.com/certifications/itil-service-management/what-is-itil | medium | TCE hierarchical governance; ITIL 4 ECAB model |
| [fact] Decision velocity override: incident response pre-approval is structurally incompatible with four-nines response window | https://sre.google/workbook/incident-response/; https://sre.google/sre-book/being-on-call/ | medium | Directly stated in SRE sources; Q4 corroborates |
| [inference] Detection velocity: post-hoc review acceptable only when monitoring can detect failure before material harm | https://sre.google/sre-book/embracing-risk/; https://sre.google/workbook/error-budget-policy/ | medium | SRE error budget burn rate as detection mechanism |
| [fact] SRE error budget policy: trigger-based shift from bounded delegation to pre-approval (deployment freeze) when error budget exhausted | https://sre.google/workbook/error-budget-policy/ | medium | Explicitly documented policy; Google SRE Workbook |
| [inference] Pre-approval on Class 1 is coercive formalisation; generates mis-classification behaviour | https://eric.ed.gov/?id=EJ525938; https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html | medium | Adler and Borys 1996; governance failure mechanisms item |
| [inference] Tighten triggers: exception volume ratio above threshold; error budget exhaustion | https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html; https://sre.google/workbook/error-budget-policy/ | medium | Q3 circuit breakers; SRE error budget policy |
| [inference] Relax conditions: exception volume below threshold sustained; post-hoc review confirming Class 1 compliance | https://sre.google/workbook/error-budget-policy/; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html | medium | SRE freeze-lift condition; ITIL 4 standard change revalidation |
| [inference] HITL capacity constraint sets upper bound on Class 3 volume that can receive meaningful pre-approval | https://davidamitchell.github.io/Research/research/2026-05-20-hitl-capacity-thresholds-in-banking-compliance.html; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html | medium | HITL rubber-stamp failure mode; P1 integrator capacity analysis |

**Assumptions**

1. Automated monitoring provides near-real-time failure detection for Class 1 work. [assumption; source: https://sre.google/sre-book/embracing-risk/; https://dora.dev/guides/dora-metrics-four-keys/; justification: SRE and DORA both treat automated monitoring as a prerequisite for fast-path deployment; without it, detection velocity may be insufficient for post-hoc review to be risk-acceptable]

2. Governance parameters (cost ceiling, blast radius limit, approved catalog) for bounded delegation are maintained on a regular cadence by the central function. [assumption; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q4-decision-rights-placement.html; https://aws.amazon.com/blogs/architecture/empower-your-teams-with-modern-architecture-governance/; justification: stale parameters undermine the bounded delegation model; the Q4 item identified parameter maintenance as the primary operational assumption]

3. The exception volume ratio threshold and error budget threshold are organisation-specific and must be calibrated empirically; the evidence provides the mechanism (trigger-based regime shift) but not universal threshold values. [assumption; source: https://sre.google/workbook/error-budget-policy/; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html; justification: the SRE error budget model explicitly leaves SLO values to be set per service; Q3 similarly leaves circuit-breaker thresholds to empirical calibration]

**Analysis**

The five selection criteria (reversibility, blast radius, standardisation, decision velocity, detection velocity) are not independent. Reversibility and blast radius together determine whether the failure mode can be corrected before material harm accumulates; standardisation determines whether the pattern's failure mode is known in advance. Decision velocity and detection velocity together determine whether either ex-ante or ex-post review can operationally deliver governance value. [inference; source: https://www.jstor.org/stable/725118; https://sre.google/sre-book/embracing-risk/; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html]

Uniform pre-approval is the primary rival to the conditional matrix, and has historically been treated as a compliance default in regulated enterprises. [inference; source: https://www.jstor.org/stable/725118; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html] Multiple independent sources converge against uniform pre-approval: the P1 item identified governance-generated queueing as the dominant flow constraint, the HITL capacity thresholds item showed that pre-approval at high volume degrades to rubber-stamping, and the SRE model demonstrates that even regulated-context governance can use bounded delegation as the default with pre-approval reserved for budget-exhaustion events. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html; https://davidamitchell.github.io/Research/research/2026-05-20-hitl-capacity-thresholds-in-banking-compliance.html; https://sre.google/workbook/error-budget-policy/]

The one scenario where uniform pre-approval is defensible is when the organisation cannot maintain automated monitoring (making detection velocity insufficient for post-hoc review) and cannot maintain the governance parameters that make bounded delegation reliable. In that case, the absence of the enabling conditions for both alternative patterns forces the default back to pre-approval despite its throughput cost. This is the "competence prerequisite" scenario identified in Q4. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q4-decision-rights-placement.html; https://sre.google/sre-book/embracing-risk/]

The BCBS 328 proportionality requirement provides the regulatory floor: control intensity must match risk profile. Uniform pre-approval violates proportionality when applied to Class 1 work; uniform post-hoc review violates proportionality when applied to Class 3 work. The conditional matrix is structurally compliant with BCBS 328 because each class has a named control pattern, named authority (from Q4), and trigger-defined escalation path. [fact; source: https://www.bis.org/bcbs/publ/d328.pdf; inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html]

The behavioural risk is that teams will mis-classify Class 2 or 3 work as Class 1 to access the post-hoc review lane. The Q2 boundary tests (observable, self-evident, auditable) reduce this incentive by making classification legible. The Q3 WIP limit on the exception lane removes the incentive to inflate Class 3 status. The conditional regime-shift mechanism adds a system-level deterrent: sustained mis-classification increases exception volume, triggering the tighten condition that shifts all lanes toward pre-approval, which hurts the mis-classifying teams as much as compliant teams. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html]

**Risks, Gaps, and Uncertainties**

- The conditional control-selection matrix relies on the Q2 demand classification being performed reliably at intake; if classification degrades (stale templates, unmaintained blast radius tooling), the matrix produces incorrect control assignments. This risk is inherited from the Q2 evidence gap identified there.
- Threshold calibration values for tighten and relax triggers are not empirically derived from this item; they are organisation-specific.
- The TCE discriminating alignment argument is applied as an inference principle; no primary study directly validates this specific mapping in a split-authority delivery context.
- The SRE error budget model is drawn from high-capability software engineering organisations; applicability to lower-maturity or less-automated delivery environments requires adjustment.
- BCBS 328 compliance interpretation in this item is an inference from regulatory text, not a confirmed legal opinion; application in highly regulated sectors requires legal review.

**Open Questions**

1. How should the tighten and relax observation windows (the calibration period for sustained compliance) be sized for teams with varying delivery cadence?
2. What monitoring design detects the "silent failure" scenario (where Class 1 failures are slow-developing and not captured by automated monitoring) without recreating pre-approval latency?
3. At what Class 3 volume does the pre-approval mechanism exceed the genuine review capacity of the authority function, triggering the HITL rubber-stamp failure mode?

**Output**

- Type: knowledge
- Description: A conditional control-selection matrix mapping three demand classes to three control patterns (post-hoc review for Class 1, bounded delegation for Class 2, pre-approval for Class 3), governed by five selection criteria and four conditional modifiers, with trigger-based regime-shift mechanism grounded in TCE, COSO, ITIL 4, and SRE evidence. [inference; source: https://www.jstor.org/stable/725118; https://www.coso.org/guidance-on-ic; https://sre.google/workbook/error-budget-policy/]
- Key sources:
  1. [Google SRE Workbook: Error Budget Policy](https://sre.google/workbook/error-budget-policy/)
  2. [Williamson (1979) Transaction-Cost Economics: The Governance of Contractual Relations](https://www.jstor.org/stable/725118)
  3. [Mitchell (2026) Q2: Demand segmentation for fast-path vs controlled-path flow](https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html)

### §7 Recursive Review

```text
review_result: pass
acronym_audit: passed
  - COSO: expanded on first use as Committee of Sponsoring Organizations of the Treadway Commission (COSO)
  - TCE: expanded on first use as Transaction Cost Economics (TCE)
  - SLO: expanded on first use as Service Level Objective (SLO)
  - SRE: expanded on first use as Site Reliability Engineering (SRE)
  - ITIL: expanded on first use in §2.A as Information Technology Infrastructure Library (ITIL) 4 Change Enablement
  - ITSM: expanded on first use as IT Service Management (ITSM)
  - ICS: expanded on first use as Incident Command System (ICS)
  - HITL: expanded on first use as Human-in-the-Loop (HITL)
  - WIP: expanded on first use as Work in Progress (WIP)
  - BCBS: cited via full name Basel Committee on Banking Supervision (BCBS)
  - DORA: expanded on first use in §2.A as DevOps Research and Assessment (DORA)
  - ECAB: expanded on first use as Emergency Change Advisory Board (ECAB)
claim_audit: all claims carry [fact], [inference], or [assumption] labels
parity_check: §6 Synthesis and Findings are aligned
assumption_audit: all [assumption] bullets carry URL-backed source context
scope_guardrail: Q6 leading-indicator bundles not duplicated; Q3 circuit-breaker thresholds referenced not redefined
```

---

## Findings

### Executive Summary

Post-hoc review is the correct and sufficient control for Class 1 (fast-path) work, bounded delegation with guardrails is the correct control for Class 2 (standard-path) work, and pre-approval is the correct control for Class 3 (exception-path) work, with class assignment determined by the three Q2 boundary tests (template, recovery, blast radius). [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html; https://www.jstor.org/stable/725118; https://www.coso.org/guidance-on-ic] This mapping is independently supported by Transaction Cost Economics (TCE) discriminating alignment (governance intensity should match transaction hazard), the Committee of Sponsoring Organizations of the Treadway Commission (COSO) preventive-detective distinction, Information Technology Infrastructure Library version 4 (ITIL 4) Change Enablement practice, and the Site Reliability Engineering (SRE) error budget policy as a concrete implementation of trigger-based regime shifts. [inference; source: https://www.jstor.org/stable/725118; https://www.coso.org/guidance-on-ic; https://www.axelos.com/certifications/itil-service-management/what-is-itil; https://sre.google/workbook/error-budget-policy/] Applying pre-approval to Class 1 work imposes approval-queue latency without proportionate risk reduction, because the boundary tests that qualify Class 1 work already confirm reversibility, contained blast radius, and pattern adherence. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html; https://sre.google/sre-book/embracing-risk/] Two observable triggers (exception volume ratio above threshold and error budget exhausted) shift the control regime one level toward pre-approval temporarily; two observable conditions (exception volume ratio below threshold for a sustained window and post-hoc review confirming sustained Class 1 compliance) permit shifting one level toward post-hoc review. [inference; source: https://sre.google/workbook/error-budget-policy/; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html]

### Key Findings

1. Post-hoc review (a detective control operating after the event) is the correct and sufficient control for Class 1 work because the three Q2 boundary tests already provide the ex-ante governance: a passing template test confirms pattern adherence, a passing recovery test confirms reversibility, and a passing blast radius test confirms contained impact, leaving post-hoc review to confirm adherence and update the template catalogue. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html; https://www.coso.org/guidance-on-ic; https://www.axelos.com/certifications/itil-service-management/what-is-itil)

2. Bounded delegation with guardrails (a hybrid governance structure in TCE terms) is the correct control for Class 2 work, in which the three Q4 parameters (cost ceiling, blast radius limit, approved technology catalog) and four escalation triggers (catalog deviation, ceiling breach, blast radius overflow, external commitment) together constitute the control, replacing per-decision pre-approval while preserving governance outcomes for the boundary cases that matter. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q4-decision-rights-placement.html; https://www.jstor.org/stable/725118)

3. Pre-approval is the correct control for Class 3 work (novel, irreversible, or system-wide blast radius), where high uncertainty and high consequence of contracting failure justify the throughput cost of ex-ante review, consistent with TCE hierarchical governance and ITIL 4's Emergency Change Advisory Board (ECAB) model for emergency and novel-consequence changes. ([inference]; medium confidence; source: https://www.jstor.org/stable/725118; https://www.axelos.com/certifications/itil-service-management/what-is-itil)

4. Decision velocity is an override criterion: time-critical decisions (incident response, emergency mitigation) cannot use pre-approval regardless of class assignment because approval latency is structurally incompatible with the five-minute response window for services targeting four nines (99.99%) availability, and must instead use pre-delegated Incident Command System (ICS) authority with post-hoc review. ([fact]; medium confidence; source: https://sre.google/workbook/incident-response/; https://sre.google/sre-book/being-on-call/)

5. Detection velocity sets the boundary condition for post-hoc review acceptability: post-hoc review is risk-acceptable only when automated monitoring can detect failure before material harm accumulates, as demonstrated by the SRE error budget burn rate as a near-real-time detection mechanism for Class 1 deployment failures. ([inference]; medium confidence; source: https://sre.google/sre-book/embracing-risk/; https://sre.google/workbook/error-budget-policy/)

6. The SRE error budget policy operationalises a trigger-based shift from bounded delegation (normal operations, below Service Level Objective [SLO] budget threshold) to pre-approval (deployment freeze when error budget is exhausted), providing a concrete real-world example of automatic control-pattern escalation governed by a measurable threshold rather than a subjective judgment. ([fact]; medium confidence; source: https://sre.google/workbook/error-budget-policy/)

7. Applying pre-approval to Class 1 work generates approval-queue latency without proportionate risk reduction, because the work is reversible and contained by definition; this pattern constitutes a coercive formalisation in Adler and Borys (1996) terms and predictably generates mis-classification and workaround behaviour as documented in the governance failure mechanisms item in this corpus. ([inference]; medium confidence; source: https://eric.ed.gov/?id=EJ525938; https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html)

8. Two observable conditions trigger temporary tightening of the control regime by one level: exception volume ratio above a calibrated threshold (from the Q3 circuit-breaker model), and error budget exhaustion (from the SRE error budget policy); both conditions indicate that the current class boundary tests are failing to contain risk at their defined levels. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html; https://sre.google/workbook/error-budget-policy/)

9. Two observable conditions permit relaxing the control regime by one level: exception volume ratio below threshold sustained over a calibrated observation window, and post-hoc review over the same window confirming that Class 1 work consistently meets its boundary conditions without in-flight escalation; the SRE model explicitly permits lifting the deployment freeze once SLO compliance is restored. ([inference]; medium confidence; source: https://sre.google/workbook/error-budget-policy/; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html)

10. The Human-in-the-Loop (HITL) capacity constraint provides an independent upper bound on how much work can be routed through pre-approval before meaningful review collapses into rubber-stamping (approval-by-exception without genuine challenge), and the conditional control-selection matrix must therefore be designed so that Class 3 volume stays within the genuine review capacity of the pre-approval authority. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-20-hitl-capacity-thresholds-in-banking-compliance.html; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Post-hoc review correct and sufficient for Class 1: Q2 boundary tests provide ex-ante governance | https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html; https://www.coso.org/guidance-on-ic; https://www.axelos.com/certifications/itil-service-management/what-is-itil | medium | Convergence from TCE, COSO, ITIL 4, and Q2 |
| [inference] Bounded delegation correct for Class 2: Q4 parameters and escalation triggers constitute the control | https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q4-decision-rights-placement.html; https://www.jstor.org/stable/725118 | medium | TCE hybrid governance; Q4 bounded delegation design |
| [inference] Pre-approval correct for Class 3: high uncertainty and consequence justify ex-ante review | https://www.jstor.org/stable/725118; https://www.axelos.com/certifications/itil-service-management/what-is-itil | medium | TCE hierarchical governance; ITIL 4 ECAB model |
| [fact] Decision velocity override: incident response pre-approval incompatible with four-nines response window | https://sre.google/workbook/incident-response/; https://sre.google/sre-book/being-on-call/ | medium | Directly stated in SRE sources; Q4 corroborates |
| [inference] Detection velocity: post-hoc review acceptable only when monitoring detects failure before material harm | https://sre.google/sre-book/embracing-risk/; https://sre.google/workbook/error-budget-policy/ | medium | SRE error budget burn rate as detection mechanism |
| [fact] SRE error budget policy: trigger-based shift from bounded delegation to pre-approval (deployment freeze) on budget exhaustion | https://sre.google/workbook/error-budget-policy/ | medium | Explicitly documented Google SRE Workbook policy |
| [inference] Pre-approval on Class 1 is coercive formalisation; generates mis-classification behaviour | https://eric.ed.gov/?id=EJ525938; https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html | medium | Adler and Borys 1996; governance failure mechanisms item |
| [inference] Tighten triggers: exception volume ratio above threshold; error budget exhaustion | https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html; https://sre.google/workbook/error-budget-policy/ | medium | Q3 circuit breakers; SRE error budget policy |
| [inference] Relax conditions: exception volume below threshold sustained; post-hoc review confirming Class 1 compliance | https://sre.google/workbook/error-budget-policy/; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html | medium | SRE freeze-lift condition; ITIL 4 standard change revalidation |
| [inference] HITL capacity constraint sets upper bound on Class 3 volume for meaningful pre-approval | https://davidamitchell.github.io/Research/research/2026-05-20-hitl-capacity-thresholds-in-banking-compliance.html; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html | medium | HITL rubber-stamp failure mode; P1 integrator capacity analysis |

### Assumptions

1. Automated monitoring provides near-real-time failure detection for Class 1 work. [assumption; source: https://sre.google/sre-book/embracing-risk/; https://dora.dev/guides/dora-metrics-four-keys/] Justification: SRE and DevOps Research and Assessment (DORA) both treat automated monitoring as a prerequisite for fast-path deployment; without it, detection velocity may be insufficient for post-hoc review to be risk-acceptable.

2. Governance parameters (cost ceiling, blast radius limit, approved catalog) for bounded delegation are maintained on a regular cadence by the central function; stale parameters undermine the bounded delegation model and force fallback to pre-approval. [assumption; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q4-decision-rights-placement.html; https://aws.amazon.com/blogs/architecture/empower-your-teams-with-modern-architecture-governance/] Justification: the Q4 item identified parameter maintenance as the primary operational assumption for bounded delegation.

3. Exception volume ratio thresholds and error budget thresholds are organisation-specific and must be calibrated empirically; the evidence provides the mechanism but not universal threshold values. [assumption; source: https://sre.google/workbook/error-budget-policy/; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html] Justification: the SRE error budget model explicitly leaves SLO values to be set per service; Q3 similarly leaves circuit-breaker thresholds to empirical calibration.

### Analysis

The five selection criteria (reversibility, blast radius, standardisation, decision velocity, detection velocity) are not independent: reversibility and blast radius together determine whether the failure mode can be corrected before material harm accumulates, and standardisation determines whether the failure mode is known in advance. Decision velocity and detection velocity together determine whether ex-ante or ex-post review can operationally deliver governance value in the available time. [inference; source: https://www.jstor.org/stable/725118; https://sre.google/sre-book/embracing-risk/; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html]

Uniform pre-approval is the primary rival to the conditional matrix, and has historically been treated as a compliance default in regulated enterprises. [inference; source: https://www.jstor.org/stable/725118; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html] Multiple independent sources converge against uniform pre-approval: the P1 item identified governance-generated queueing as the dominant flow constraint, the HITL capacity thresholds item showed that pre-approval at high volume degrades to rubber-stamping (approval-by-exception without genuine challenge), and the SRE model demonstrates that even regulated-context governance can use bounded delegation as the default with pre-approval reserved for budget-exhaustion events. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-p1-operating-model-synthesis.html; https://davidamitchell.github.io/Research/research/2026-05-20-hitl-capacity-thresholds-in-banking-compliance.html; https://sre.google/workbook/error-budget-policy/]

The one scenario where uniform pre-approval is defensible is when the organisation cannot maintain automated monitoring (making detection velocity insufficient for post-hoc review) and cannot maintain the governance parameters that make bounded delegation reliable; in that case, the absence of the enabling conditions for both alternative patterns forces the default back to pre-approval despite its throughput cost, consistent with the competence-prerequisite scenario identified in Q4. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q4-decision-rights-placement.html; https://sre.google/sre-book/embracing-risk/]

The Basel Committee on Banking Supervision (BCBS) 328 proportionality requirement provides the regulatory floor: control intensity must match risk profile. [fact; source: https://www.bis.org/bcbs/publ/d328.pdf] Uniform pre-approval violates proportionality when applied to Class 1 work; uniform post-hoc review violates proportionality when applied to Class 3 work. The conditional matrix is structurally consistent with BCBS 328 because each demand class carries a named control pattern, a named authority (from Q4), and trigger-defined escalation paths. [inference; source: https://www.bis.org/bcbs/publ/d328.pdf; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html]

The behavioural risk is that teams will mis-classify Class 2 or 3 work as Class 1 to access the post-hoc review lane. The Q2 boundary tests (observable, self-evident, auditable) reduce this incentive by making classification legible. The Q3 Work in Progress (WIP) limit on the exception lane removes the incentive to inflate Class 3 status for priority service. The conditional regime-shift mechanism adds a system-level deterrent: sustained mis-classification raises exception volume, triggering the tighten condition that shifts all lanes toward pre-approval, which penalises compliant teams alongside mis-classifying teams and therefore creates collective pressure to maintain accurate classification. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q3-routing-exception-isolation.html]

### Risks, Gaps, and Uncertainties

- The conditional control-selection matrix relies on reliable demand classification at intake; if classification degrades (stale templates, unmaintained blast radius tooling), the matrix produces incorrect control assignments. This risk is inherited from the Q2 evidence gap.
- Tighten and relax observation window sizing is not empirically derived from this item; the observation window length is organisation-specific.
- The TCE discriminating alignment argument is applied as an inference principle; no primary study directly validates this specific mapping in a split-authority delivery context.
- The SRE error budget model is drawn from high-capability software engineering organisations; applicability to lower-maturity or less-automated delivery environments requires adjustment.
- BCBS 328 compliance interpretation in this item is an inference from regulatory text, not a confirmed legal interpretation; application in highly regulated sectors requires legal review.

### Open Questions

1. How should the tighten and relax observation windows be sized for teams with varying delivery cadence?
2. What monitoring design detects "silent failure" scenarios (where Class 1 failures are slow-developing and not captured by automated monitoring) without recreating pre-approval latency?
3. At what Class 3 volume does the pre-approval mechanism exceed the genuine review capacity of the authority function, triggering the HITL rubber-stamp failure mode?

### Output

- Type: knowledge
- Description: A conditional control-selection matrix mapping three demand classes to three control patterns (post-hoc review for Class 1, bounded delegation for Class 2, pre-approval for Class 3), governed by five selection criteria and four conditional modifiers, with trigger-based regime-shift mechanism grounded in TCE, COSO, ITIL 4, and SRE evidence. [inference; source: https://www.jstor.org/stable/725118; https://www.coso.org/guidance-on-ic; https://sre.google/workbook/error-budget-policy/]
- Key sources:
  1. [Google SRE Workbook: Error Budget Policy (Thurgood, 2018)](https://sre.google/workbook/error-budget-policy/)
  2. [Williamson (1979) Transaction-Cost Economics: The Governance of Contractual Relations](https://www.jstor.org/stable/725118)
  3. [Mitchell (2026) Q2: Demand segmentation for fast-path vs controlled-path flow](https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q2-demand-segmentation.html)
