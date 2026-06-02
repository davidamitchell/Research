---
review_count: 2
title: "SRE: establishing SLOs as contractual capability boundaries"
added: 2026-05-31T09:42:57+00:00
status: completed
priority: high
blocks: []
themes: [software-engineering, governance-policy, mlops-deployment, organisational-design]
started: 2026-06-01T15:46:51+00:00
completed: 2026-06-02T11:27:02+00:00
output: [knowledge]
cites: [2026-05-31-capability-claim-telemetry-conflict-arbitration]
related: [2026-05-31-capability-claim-telemetry-conflict-arbitration]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# SRE: establishing SLOs as contractual capability boundaries

## Research Question

How do Site Reliability Engineering (SRE) practices establish what a system can safely do, expressed as a contractual boundary rather than an observed average: specifically, how are Service Level Objectives (SLOs) set, and what evidence justifies the chosen threshold?

## Scope

**In scope:**
- SRE methodology for setting SLOs: the process, the evidence types used, and the decision logic for threshold selection.
- The distinction between SLOs as contractual commitments vs. observed operational averages.
- What evidence (telemetry, user research, business negotiation) is considered authoritative for SLO threshold selection.
- Error budget derivation and its relationship to capability boundaries.

**Out of scope:**
- Service Level Agreement (SLA) legal enforceability analysis.
- Full SRE operational practices beyond SLO/error-budget setting.
- Specific vendor SRE tooling comparison.

**Constraints:** (time, source types, access)
- Primary sources: Google SRE books, industry SRE literature, and practitioner retrospectives.
- Focus on evidence-based threshold justification, not aspirational SLO setting.

## Context

Systems that act on behalf of teams must know the capability boundaries those teams can reliably commit to, not their best-case performance. SRE's SLO model is the most widely documented method for expressing this as a verifiable contractual boundary. Understanding how thresholds are justified is prerequisite to assessing whether a stated allowance is evidence-backed or asserted. This is Gap 2 Q5 from issue #618.

## Approach

1. Document the SRE SLO-setting process from primary sources (Google SRE book, SRE workbook): inputs, steps, and output artefacts.
2. Identify what evidence types are specified as required vs. optional for threshold selection.
3. Analyse the error-budget model: how it converts an SLO threshold into a quantified capability boundary.
4. Survey practitioner literature for cases where SLO thresholds were set without adequate evidence and the resulting failure modes.
5. Assess whether the SRE model provides explicit rules for distinguishing a contractual boundary from an observed average.

## Sources

- [ ] [Beyer et al. (2016) Site Reliability Engineering: How Google Runs Production Systems](https://sre.google/sre-book/table-of-contents/): primary Google SRE reference: SLO definition, error budgets, and threshold selection
- [ ] [Beyer et al. (2018) The Site Reliability Workbook: Practical Ways to Implement SRE](https://sre.google/workbook/table-of-contents/): practical SLO setting guidance and worked examples
- [ ] [Hidalgo (2020) Implementing Service Level Objectives](https://www.oreilly.com/library/view/implementing-service-level/9781492076803/): practitioner guide to evidence-based SLO threshold selection
- [ ] [DORA State of DevOps Reports](https://dora.dev/research/): empirical data on SLO adoption and associated reliability outcomes

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. §§0-5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

Question: How do Site Reliability Engineering (SRE) practices establish what a system can safely do, expressed as a contractual boundary rather than an observed average, specifically how are Service Level Objectives (SLOs) set, and what evidence justifies the chosen threshold?

Scope: SRE methodology for setting SLOs: the process, the evidence types used, and the decision logic for threshold selection; the distinction between SLOs as contractual commitments vs. observed operational averages; evidence considered authoritative for SLO threshold selection; error budget derivation and its relationship to capability boundaries.

Out of scope: Service Level Agreement (SLA) legal enforceability analysis; full SRE operational practices beyond SLO/error-budget setting; specific vendor SRE tooling comparison.

Constraints: Primary sources are Google SRE books and industry SRE literature. Focus on evidence-based threshold justification, not aspirational SLO setting. [assumption; justification: Google SRE books are the canonical primary source for SRE SLO methodology, widely cited as founding documents of the discipline; source: https://sre.google/sre-book/table-of-contents/]

Output format: knowledge item with structured Findings.

### §1 Question Decomposition

**A. What is the SRE SLO-setting process?**
- A1. What inputs does the SRE SLO-setting process require?
- A2. What steps does the process follow from input to output artefact?
- A3. What output artefacts does the process produce?

**B. What evidence types are required vs. optional for threshold selection?**
- B1. What evidence types does the Google SRE book specify as inputs to SLO threshold selection?
- B2. Which evidence types are specified as required?
- B3. Which evidence types are described as optional or supplementary?

**C. How does the error budget model convert an SLO threshold into a quantified capability boundary?**
- C1. How is the error budget calculated from an SLO threshold?
- C2. How does error budget exhaustion enforce the capability boundary?
- C3. What is the prescribed organisational response when the error budget is consumed?

**D. What happens when SLO thresholds are set without adequate evidence?**
- D1. What failure modes are documented for aspirational vs. evidence-based SLOs?
- D2. What practitioner cases illustrate these failure modes?

**E. Does the SRE model distinguish contractual boundary from observed average?**
- E1. How does the SRE model define the distinction between SLO as contractual commitment and observed operational average?
- E2. What mechanisms enforce that distinction?

### §2 Investigation

**A1-A3: SRE SLO-setting process**

The Google SRE book defines Service Level Indicators (SLIs) as "a carefully defined quantitative measure of some aspect of the level of service that is provided," and SLOs as "a target value or range of values for a service level that is measured by an SLI." [fact; source: https://sre.google/sre-book/service-level-objectives/]

The SRE Workbook specifies a four-step SLO-adoption state: (1) SLOs approved by all stakeholders as fit for purpose; (2) the people responsible for meeting the SLO have agreed it is achievable under normal circumstances; (3) the organisation has committed to using the error budget for prioritisation; (4) a process for refining the SLO is in place. [fact; source: https://sre.google/workbook/implementing-slos/]

The SRE Workbook recommends a starting process: identify the user population and common user interactions, choose a small number (five or fewer) of SLI types that represent the most critical functionality, select initial thresholds from historical performance rounded to manageable numbers, then iteratively tighten as confidence grows. [fact; source: https://sre.google/workbook/implementing-slos/]

The process requires stakeholder agreement across three roles: product managers confirming the threshold is sufficient for users; product developers agreeing to reliability-focus actions when error budget is exhausted; and the team responsible for production confirming the target is achievable without unsustainable toil. [fact; source: https://sre.google/workbook/implementing-slos/]

**B1-B3: Evidence types for threshold selection**

The SRE book states: "Start by thinking about (or finding out!) what your users care about, not what you can measure." [fact; source: https://sre.google/sre-book/service-level-objectives/] This positions user-experience evidence as the primary input, with measurable proxies as implementation compromises. [inference; source: https://sre.google/sre-book/service-level-objectives/]

Three evidence types are described: (i) historical telemetry from production systems (the most accessible first-pass input); (ii) user experience data, which is described as the ideal starting point but difficult to measure; (iii) business negotiation, as product managers and product developers must agree the threshold is appropriate for users and achievable in production. [fact; source: https://sre.google/workbook/implementing-slos/]

The SRE Workbook explicitly warns against basing SLOs solely on current performance: "we advise against picking an SLO based upon current performance, because this can commit you to unnecessarily strict SLOs." [fact; source: https://sre.google/workbook/implementing-slos/] However, it simultaneously acknowledges that current performance is often the practical starting point when no other information is available. [fact; source: https://sre.google/workbook/implementing-slos/]

No evidence type is specified as strictly required in a mandatory technical sense; the three-party stakeholder agreement process is the procedural requirement. [inference; source: https://sre.google/workbook/implementing-slos/]

The Evernote case study describes setting an initial SLO at 99.95% "based upon discussions with our internal customer support and product teams and, more importantly, user feedback," using uptime as the simplest available proxy, illustrating that at least one practitioner implementation began with negotiation supplemented by available telemetry rather than rigorous user-impact studies. [inference; source: https://sre.google/workbook/slo-engineering-case-studies/]

**C1-C3: Error budget as quantified capability boundary**

The error budget is defined as 100% minus the SLO target. For a 99.9% SLO with 1,000,000 requests over four weeks, the error budget is 1,000 errors. [fact; source: https://sre.google/workbook/error-budget-policy/]

The error budget policy document specifies: if the service has exceeded its error budget for the preceding four-week window, all changes and releases other than highest-priority issues or security fixes are halted until the service returns within its SLO. [fact; source: https://sre.google/workbook/error-budget-policy/]

Changes are described as "roughly 70% of our outages" and the error budget forms a control mechanism for diverting attention to stability. [fact; source: https://sre.google/workbook/error-budget-policy/]

The escalation path is documented: in the event of disagreement about error budget calculation or required actions, the issue is escalated to the Chief Technology Officer (CTO) to make a decision. [fact; source: https://sre.google/workbook/error-budget-policy/]

A single incident consuming more than 20% of error budget over four weeks requires a post-mortem with at least one highest-priority action item; a single class of outage consuming more than 20% of error budget over a quarter requires it to be addressed in the following quarter's planning document. [fact; source: https://sre.google/workbook/error-budget-policy/]

**D1-D2: Failure modes of inadequate threshold evidence**

The SRE Workbook identifies "an SLO without teeth" as a specific failure mode: a system with an SLO below 100% but "without a common understanding about its importance or how to leverage it to make continuous improvement choices." [fact; source: https://sre.google/workbook/implementing-slos/] Without the four preconditions (stakeholder approval, production agreement, error-budget commitment, refinement process), "SLO compliance will simply be another KPI (key performance indicator) or reporting metric, rather than a decision-making tool." [fact; source: https://sre.google/workbook/implementing-slos/]

The SRE book documents the Chubby global planned outage as a case where absence of an explicit SLO led to over-reliance: users developed beliefs about service availability that were incorrect because no SLO had been published to calibrate expectations. [fact; source: https://sre.google/sre-book/service-level-objectives/]

The SRE book notes that aspirational SLOs "can result in wasted work if a team uses heroic efforts to meet an overly aggressive SLO, or a bad product if the SLO is too lax." [fact; source: https://sre.google/sre-book/service-level-objectives/]

The risk tolerance chapter in the SRE book documents Google's practice of aligning YouTube's SLO with its business lifecycle stage, setting a lower availability target during rapid growth because "rapid feature development was correspondingly more important." Purely aspirational SLOs misaligned with business context impose unnecessary constraints, as this case illustrates. [inference; source: https://sre.google/sre-book/embracing-risk/]

**E1-E2: SLO as contractual boundary vs. observed average**

The SRE book explicitly frames SLOs as a target that functions as both a minimum and a maximum: "we view the availability target as both a minimum and a maximum." [fact; source: https://sre.google/sre-book/embracing-risk/] Operating significantly above the SLO "would waste opportunities to add features to the system, clean up technical debt, or reduce its operational costs." This means the SLO is not an aspirational upper bound but a specific agreed capability range. [inference; source: https://sre.google/sre-book/embracing-risk/]

The SRE book recommends using a tighter internal SLO than the externally published SLO, creating a buffer between the operational contractual boundary and the user-facing published commitment. [fact; source: https://sre.google/sre-book/service-level-objectives/]

The distinction between SLO and observed operational average is operationalised by the error budget: the SLO is the target; the SLI measurement provides the observed value; the error budget tracks the difference. The error budget policy converts this difference into mandated organisational responses, preventing the SLO from being a passive reporting number. [inference; source: https://sre.google/workbook/implementing-slos/; https://sre.google/workbook/error-budget-policy/]

The SRE workbook explicitly states that the SLO target represents the threshold below which "users are likely to start complaining or to stop using the service," grounding the contractual nature in user-impact evidence rather than in technical capability alone. [fact; source: https://sre.google/workbook/implementing-slos/]

### §3 Reasoning

The SRE model establishes SLOs as contractual capability boundaries through a three-mechanism structure:

1. The SLO threshold is set by a defined evidence-gathering and negotiation process, not by unilateral technical assertion. User-impact evidence is specified as the ideal primary input; telemetry and stakeholder negotiation provide the practical working inputs. [inference; source: https://sre.google/workbook/implementing-slos/; https://sre.google/sre-book/service-level-objectives/]

2. The error budget converts the SLO threshold into a quantified resource that is consumed by service failures. When exhausted, the error budget triggers prescribed organisational responses, making the threshold enforceable rather than aspirational. [inference; source: https://sre.google/workbook/error-budget-policy/]

3. The three-stakeholder agreement requirement (product manager, development team, SRE team) prevents the SLO from being set by a single party and ensures it reflects an achievable, user-relevant commitment. [inference; source: https://sre.google/workbook/implementing-slos/]

The failure mode of "SLO without teeth" is distinct from the failure of setting an evidence-free threshold: both produce a threshold that does not govern behaviour, but by different mechanisms. An evidence-free threshold can still have enforcement teeth if the error budget policy is enforced; conversely, an evidence-backed threshold becomes inert if the error budget policy is not adopted. [inference; source: https://sre.google/workbook/implementing-slos/; https://sre.google/workbook/error-budget-policy/]

Narrative glue removed: the SRE model does not claim that SLOs are inherently contractual; they become contractual through the adoption of the error budget policy and stakeholder agreement. The threshold alone is not the mechanism; it is the threshold combined with the enforced error budget policy. [inference; source: https://sre.google/workbook/implementing-slos/]

### §4 Consistency Check

```text
contradiction_scan: no internal contradictions found
note_1: SRE book advises against basing SLO solely on current performance (workbook) but acknowledges it as practical starting point; both claims are present in the same source; this is not a contradiction but a tension the source explicitly acknowledges
note_2: SLO as both minimum and maximum (embracing-risk) is consistent with the error budget concept; the SLO is a target range, not an aspirational upper bound
note_3: distinction between evidence-free threshold and SLO-without-teeth is confirmed by separate failure mode descriptions in the workbook
confidence_adjustment: medium maintained throughout; no primary controlled studies on SLO setting outcomes are cited in Google SRE sources; Evernote case study provides practitioner corroboration but is a single vendor account
scope_guardrail: maintained; SLA legal enforceability, vendor tooling comparison excluded
```

### §5 Depth and Breadth Expansion

**Technical lens:** The SRE model treats SLI measurement implementation as a reliability concern in its own right. A single SLI specification can have multiple implementations with different accuracy and coverage trade-offs. The choice of SLI implementation affects how faithfully the SLO boundary represents the user experience, meaning the threshold can be evidence-backed but the measurement proxy can still under-represent actual user impact. [inference; source: https://sre.google/workbook/implementing-slos/]

**Regulatory/governance lens:** The Google SRE embracing-risk chapter describes a cost/benefit framework for setting the availability target: for a service with $1M revenue, improving from 99.9% to 99.99% availability adds at most $900 in value; if the cost exceeds $900, the higher target is economically unjustified. [fact; source: https://sre.google/sre-book/embracing-risk/] This introduces an economic constraint on the contractual boundary: the SLO threshold should not exceed what the business can justify investing to defend. [inference; source: https://sre.google/sre-book/embracing-risk/]

**Behavioural lens:** The SRE book documents a planning fallacy analogue: without an explicit SLO, users develop their own beliefs about service availability, which "may be unrelated to the beliefs held by the people designing and operating the service." [fact; source: https://sre.google/sre-book/service-level-objectives/] This mirrors the capability overestimation dynamic documented in the companion item on telemetry arbitration. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-31-capability-claim-telemetry-conflict-arbitration.html]

**Historical lens:** The SRE book documents Google's deliberate decision to plan outages for the Chubby distributed lock service because without an explicit downtime target, service teams built critical dependencies on Chubby with the implicit assumption of near-100% availability, creating a fragility the team had not committed to supporting. This is an empirical case study demonstrating that the absence of a contractual boundary enables capability overestimation. [inference; source: https://sre.google/sre-book/service-level-objectives/]

**Comparison with related item:** The companion completed item on capability claim vs. telemetry arbitration (2026-05-31-capability-claim-telemetry-conflict-arbitration) establishes that telemetry override is the most structurally direct mechanism for correcting capability overestimation. The SRE error budget policy is the specific operationalisation of that override: the SLO threshold is set through the evidence and negotiation process, and the error budget policy enforces it through telemetry measurement and prescribed organisational responses. [inference; source: https://sre.google/workbook/error-budget-policy/; https://davidamitchell.github.io/Research/research/2026-05-31-capability-claim-telemetry-conflict-arbitration.html]

### §6 Synthesis

**Executive summary:**

SRE establishes Service Level Objectives (SLOs) as contractual capability boundaries through a combined evidence-gathering, stakeholder-negotiation, and error-budget-enforcement process. [inference; source: https://sre.google/workbook/implementing-slos/; https://sre.google/workbook/error-budget-policy/] User-impact evidence is specified as the primary input for threshold selection, with historical telemetry and stakeholder negotiation as the practical working inputs. [fact; source: https://sre.google/sre-book/service-level-objectives/; https://sre.google/workbook/implementing-slos/] The SLO threshold becomes contractual through the adoption of an error budget policy with prescribed organisational consequences, not through the threshold number alone. [inference; source: https://sre.google/workbook/implementing-slos/; https://sre.google/workbook/error-budget-policy/] SLOs set without adequate evidence or without an enforced error budget policy degrade to reporting metrics rather than decision-making tools, producing the documented failure mode of "SLO without teeth." [fact; source: https://sre.google/workbook/implementing-slos/]

**Key findings:**

1. SRE defines SLOs as the threshold below which users are likely to start complaining or stop using the service, grounding the contractual boundary in user-impact evidence rather than in technical capability assertion alone. ([fact]; medium confidence; source: https://sre.google/workbook/implementing-slos/)

2. The SRE SLO-setting process requires three-party stakeholder agreement across product manager, development team, and SRE team as a procedural safeguard preventing any single party from setting a threshold unilaterally. ([fact]; medium confidence; source: https://sre.google/workbook/implementing-slos/)

3. The error budget converts the SLO threshold into a quantified resource consumed by failures, making the threshold enforceable: when the error budget is exhausted, all releases are halted until the service returns within its SLO. ([fact]; medium confidence; source: https://sre.google/workbook/error-budget-policy/)

4. The SRE Workbook advises against basing SLOs solely on current observed performance because doing so can commit a service to unnecessarily strict targets; user-impact evidence is specified as the ideal primary input, with telemetry as the practical first-pass proxy. ([fact]; medium confidence; source: https://sre.google/workbook/implementing-slos/)

5. Google SRE frames the SLO target as both a minimum and a maximum: exceeding it significantly wastes engineering resources, establishing the SLO as a specific agreed capability range rather than an aspirational upper bound. ([inference]; medium confidence; source: https://sre.google/sre-book/embracing-risk/)

6. The SRE model distinguishes contractual boundary from observed average through the error budget measurement loop: the SLO is the target, the SLI measurement is the observed value, and the error budget tracks the difference with mandated organisational responses. ([inference]; medium confidence; source: https://sre.google/workbook/implementing-slos/; https://sre.google/workbook/error-budget-policy/)

7. SLOs adopted without an enforced error budget policy become passive reporting metrics rather than decision-making tools, the documented "SLO without teeth" failure mode that the SRE Workbook explicitly identifies. ([fact]; medium confidence; source: https://sre.google/workbook/implementing-slos/)

8. Evernote set its initial SLO at 99.95% through negotiation with customer support and product teams supplemented by available uptime telemetry, then iterated as evidence accumulated, illustrating that at least one practitioner implementation began with negotiation rather than rigorous user-impact studies. ([inference]; medium confidence; source: https://sre.google/workbook/slo-engineering-case-studies/)

9. The SRE book documents the Chubby planned-outage case as empirical evidence that absence of an explicit SLO threshold allows users to develop incorrect availability expectations, generating fragile dependencies on reliability levels the service had not committed to providing. ([fact]; medium confidence; source: https://sre.google/sre-book/service-level-objectives/)

10. Google SRE introduces an economic constraint on SLO threshold selection: the marginal cost of each additional nine of availability must be compared against the marginal revenue or user-value gain, providing a quantitative upper bound on justifiable threshold stringency. ([inference]; medium confidence; source: https://sre.google/sre-book/embracing-risk/)

11. The SRE error budget policy specifies an escalation path to the CTO for disputes about error budget calculation or required actions, demonstrating that the contractual force of the SLO boundary is backed by an organisational authority structure. ([fact]; medium confidence; source: https://sre.google/workbook/error-budget-policy/)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] SLO is threshold below which users are likely to complain or stop using the service | [Google SRE Workbook: Implementing SLOs](https://sre.google/workbook/implementing-slos/) | medium | Primary SRE source; user-happiness framing |
| [fact] Three-party stakeholder agreement required: product manager, development team, SRE team | [Google SRE Workbook: Implementing SLOs](https://sre.google/workbook/implementing-slos/) | medium | Procedural safeguard against unilateral threshold setting |
| [fact] Error budget = 100% minus SLO; exhaustion halts all releases | [Google SRE Workbook: Error Budget Policy](https://sre.google/workbook/error-budget-policy/) | medium | Specific policy document with enforcement mechanism |
| [fact] SRE advises against basing SLO solely on current performance | [Google SRE Workbook: Implementing SLOs](https://sre.google/workbook/implementing-slos/) | medium | Direct quotation; user evidence specified as primary input |
| [inference] SLO target functions as both minimum and maximum; consistently exceeding it wastes capacity | [Google SRE Book: Embracing Risk](https://sre.google/sre-book/embracing-risk/) | medium | Min/max framing is explicit; capability-range conclusion is derived |
| [inference] Error budget loop distinguishes contractual boundary from observed average | [Implementing SLOs](https://sre.google/workbook/implementing-slos/); [Error Budget Policy](https://sre.google/workbook/error-budget-policy/) | medium | Derived from error budget mechanics; not directly stated as a distinction |
| [fact] SLO without teeth: SLO without enforced error budget policy is a passive reporting metric | [Google SRE Workbook: Implementing SLOs](https://sre.google/workbook/implementing-slos/) | medium | Direct statement of failure mode |
| [fact] Evernote SLO set at 99.95% based on user feedback and internal discussions | [SRE Workbook: SLO Engineering Case Studies](https://sre.google/workbook/slo-engineering-case-studies/) | medium | Single vendor case study; practitioner corroboration |
| [fact] Chubby planned-outage case: absence of explicit SLO creates incorrect user expectations | [Google SRE Book: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/) | medium | Google-documented empirical case |
| [inference] Economic framework: marginal cost of additional nine vs. marginal value gain provides a ceiling on justifiable stringency | [Google SRE Book: Embracing Risk](https://sre.google/sre-book/embracing-risk/) | medium | Qualitative framework with one quantified example; ceiling conclusion is derived |
| [fact] Escalation to CTO for disputes about error budget calculation or required actions | [Google SRE Workbook: Error Budget Policy](https://sre.google/workbook/error-budget-policy/) | medium | Specific policy document |

**Assumptions:**

- [assumption] Google SRE documentation is representative of established SRE practice across the industry, not only within Google. Justification: the SRE book and SRE Workbook are the canonical primary references cited by organisations adopting SRE practices; the Evernote and Home Depot case studies in the SRE Workbook provide cross-organisation corroboration. [source: https://sre.google/workbook/slo-engineering-case-studies/]

- [assumption] The Alex Hidalgo (2020) book "Implementing Service Level Objectives" provides consistent guidance with Google SRE sources on evidence-based threshold selection. Justification: Hidalgo was a co-author on the SRE Workbook; the O'Reilly book is described as extending the same methodology with statistical analysis tools. [source: https://www.oreilly.com/library/view/implementing-service-level/9781492076803/]

**Analysis:**

The SRE model provides a specific answer to how a threshold becomes a contractual boundary: through the combination of evidence-based threshold selection and an enforced error budget policy; neither component alone is sufficient. [inference; source: https://sre.google/workbook/implementing-slos/; https://sre.google/workbook/error-budget-policy/] A well-evidenced threshold without an enforced error budget policy produces an "SLO without teeth," and an enforced error budget policy with an inadequately evidenced threshold produces enforcement of an arbitrary number, which can result in either heroic efforts to meet an overly aggressive target or a bad product if the target is too lax. [inference; source: https://sre.google/workbook/implementing-slos/; https://sre.google/sre-book/service-level-objectives/]

The distinction between the SLO as a contractual boundary and the SLI as the observed measurement is operationalised through the error budget: the SLO sets the target, SLI measurement produces the observed value, and the error budget is the accumulated difference over the measurement window, triggering policy responses when exceeded. [inference; source: https://sre.google/workbook/implementing-slos/; https://sre.google/workbook/error-budget-policy/] An observed average is computed from past measurements and does not carry enforcement consequences; an SLO threshold carries them through the error budget policy, making the distinction structural rather than merely semantic: the same reliability number can be a passive average or an enforced boundary depending on whether the error budget policy exists and is acted upon. [inference; source: https://sre.google/workbook/implementing-slos/; https://sre.google/workbook/error-budget-policy/]

The three-party stakeholder agreement requirement is the SRE model's mechanism for ensuring that user-impact evidence reaches the threshold-setting process: the product manager's agreement criterion is explicitly that "this threshold is good enough for users." [fact; source: https://sre.google/workbook/implementing-slos/] Without this criterion, a threshold could be set based on what is technically achievable or administratively convenient rather than on what users require. [inference; source: https://sre.google/workbook/implementing-slos/]

The tension between the advice to avoid basing SLOs solely on current performance and the practical starting point of current telemetry is resolved by the SRE model through an iterative refinement process: start with an achievable threshold, observe whether it correlates with user satisfaction, and tighten iteratively. [inference; source: https://sre.google/workbook/implementing-slos/] Organisational commitment to acting on the error budget policy at each iteration is a necessary precondition for this refinement process to produce an accurate, user-grounded threshold over time. [inference; source: https://sre.google/workbook/implementing-slos/; https://sre.google/workbook/error-budget-policy/]

The economic constraint framework for threshold selection (marginal cost vs. marginal revenue per additional nine) provides a quantitative ceiling on SLO stringency: a threshold set above what the business can economically justify defending is structurally aspirational rather than contractual, because the organisation lacks the incentive structure to enforce it consistently. [inference; source: https://sre.google/sre-book/embracing-risk/]

Plausible rival approaches not rejected by the SRE model: (a) setting thresholds purely from business negotiation without user-impact evidence, which the SRE model permits as a starting approach but flags as subject to revision through iteration; (b) setting thresholds from historical performance, which the SRE model explicitly advises against in the long run while accepting as a pragmatic first step. Both rivals are accommodated within the iterative refinement framework rather than excluded. [inference; source: https://sre.google/workbook/implementing-slos/]

**Risks, gaps, uncertainties:**

- No controlled before-after studies comparing SLO threshold-setting methods (evidence-based vs. negotiated vs. telemetry-only) and their subsequent outcomes in terms of reliability, user satisfaction, or engineering efficiency are cited in the Google SRE sources. Effectiveness claims rest on documented practice and case studies rather than controlled measurement.

- The SRE model assumes organisations are willing and able to enforce the error budget policy. The Workbook acknowledges that SLOs remain passive reporting metrics without this enforcement, but provides no empirical data on the prevalence of this failure mode in practice.

- The Evernote case study (99.95% uptime target set from user feedback and product-team discussions) is a single vendor account from a non-safety-critical consumer application; it may not represent SLO-setting practice in regulated, safety-critical, or infrastructure-service contexts.

- The economic framework for availability target selection (marginal cost vs. marginal revenue) is presented qualitatively with one illustrative example; no empirical validation of the cost function shape across service types is provided.

**Open questions:**

- What is the empirical distribution of SLO-setting methods across industry, and do evidence-based methods produce measurably better outcomes than negotiated or telemetry-only approaches?

- In practice, how often do organisations adopt the SLO threshold without implementing an enforced error budget policy, and what measurable reliability outcomes result from the "SLO without teeth" state?

- How should SLO thresholds be set for services with no prior production history, where neither telemetry nor historical user-impact data is available?

### §7 Recursive Review

```text
review_result: pass
acronym_audit: SRE expanded at first use in Research Question; SLO expanded at first use in Research Question; SLI expanded in §2 Investigation; SLA expanded in Scope; KPI expanded in §2 Investigation; CTO expanded in §2 Investigation; HTTP used in evidence map citation context only; CRE (Customer Reliability Engineering) appears only in §2 context of Evernote case study from cited source text; no unexpanded domain-specific abbreviations identified
parity_check: §6 Synthesis and §2 Investigation are consistent; no claims in §6 not grounded in §2
claim_audit: all factual and inferential claims carry [fact], [inference], or [assumption] labels; all [fact] claims bind to accessible URLs
assumption_audit: two assumptions identified and justified with URL-backed sources
contradiction_check: no internal contradictions; tension between "avoid current performance as basis" and "current performance is practical starting point" acknowledged explicitly in both §3 Reasoning and §2 Investigation
scope_guardrail: SLA legal enforceability, vendor tooling comparison excluded throughout
open_questions_check: three open questions identified for potential backlog
```

---

## Findings

### Executive Summary

SRE establishes SLOs as contractual capability boundaries through a combined evidence-gathering, three-party stakeholder-negotiation, and error-budget-enforcement process, not through the threshold number alone. [inference; source: https://sre.google/workbook/implementing-slos/; https://sre.google/workbook/error-budget-policy/] User-impact evidence is the specified primary input for threshold selection, with historical telemetry as the practical first-pass proxy when user-impact data is unavailable. [fact; source: https://sre.google/sre-book/service-level-objectives/; https://sre.google/workbook/implementing-slos/] The error budget converts the SLO threshold into a measurable resource consumed by failures, and exhaustion of that resource triggers prescribed organisational responses that give the threshold its contractual force. [inference; source: https://sre.google/workbook/error-budget-policy/] SLOs adopted without an enforced error budget policy become passive reporting metrics, the "SLO without teeth" failure mode the SRE Workbook explicitly identifies as a documented adoption risk. [fact; source: https://sre.google/workbook/implementing-slos/]

### Key Findings

1. SRE defines the SLO threshold as the reliability level below which users are likely to start complaining or stop using the service, grounding the contractual boundary in user-impact evidence rather than in technical capability assertion alone. ([fact]; medium confidence; source: https://sre.google/workbook/implementing-slos/)

2. The SRE SLO-setting process requires three-party stakeholder agreement across product manager, development team, and SRE team as a procedural safeguard ensuring the threshold reflects both user needs and production achievability before it becomes operative. ([fact]; medium confidence; source: https://sre.google/workbook/implementing-slos/)

3. The error budget (100% minus the SLO target) converts the threshold into a quantified resource: when it is exhausted over a four-week window, all releases other than highest-priority or security fixes are halted until the service returns within its SLO. ([fact]; medium confidence; source: https://sre.google/workbook/error-budget-policy/)

4. The Google SRE Workbook explicitly advises against basing SLO thresholds solely on current observed performance because this can commit a service to unnecessarily strict targets; user-impact evidence is the specified primary input, with telemetry as the practical first-pass proxy. ([fact]; medium confidence; source: https://sre.google/workbook/implementing-slos/)

5. Google SRE frames the SLO target as both a minimum and a maximum: consistently exceeding the SLO wastes engineering capacity, establishing the threshold as a specific agreed capability range rather than an aspirational upper bound. ([inference]; medium confidence; source: https://sre.google/sre-book/embracing-risk/)

6. The SRE model distinguishes the contractual SLO boundary from the observed operational average through the error budget measurement loop: the SLO is the target, the Service Level Indicator (SLI) measurement is the observed value, and the error budget tracks the accumulated difference with mandated organisational responses. ([inference]; medium confidence; source: https://sre.google/workbook/implementing-slos/; https://sre.google/workbook/error-budget-policy/)

7. SLOs adopted without an enforced error budget policy become passive reporting metrics (the "SLO without teeth" failure mode) because compliance becomes another key performance indicator rather than a decision-making tool with prescribed consequences. ([fact]; medium confidence; source: https://sre.google/workbook/implementing-slos/)

8. Evernote set its initial SLO at 99.95% through negotiation with customer support and product teams supplemented by available uptime telemetry, then iterated as evidence accumulated, illustrating that at least one practitioner implementation began with negotiation rather than rigorous user-impact studies. ([inference]; medium confidence; source: https://sre.google/workbook/slo-engineering-case-studies/)

9. The SRE book documents the Chubby planned-outage case as empirical evidence that the absence of an explicit SLO threshold allows users to develop availability expectations that exceed what the service has committed to, creating fragile dependencies on unguaranteed reliability levels. ([fact]; medium confidence; source: https://sre.google/sre-book/service-level-objectives/)

10. Google SRE applies an economic constraint to SLO threshold selection: the marginal cost of each additional nine of availability must be justified against marginal revenue or user-value gain, providing a quantitative ceiling on justifiable threshold stringency. ([inference]; medium confidence; source: https://sre.google/sre-book/embracing-risk/)

11. The error budget policy specifies escalation to the CTO for disputes about error budget calculation or required actions, demonstrating that the contractual force of the SLO boundary is backed by an explicit organisational authority structure rather than by engineering convention alone. ([fact]; medium confidence; source: https://sre.google/workbook/error-budget-policy/)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] SLO is the threshold below which users are likely to complain or stop using the service | [Google SRE Workbook: Implementing SLOs](https://sre.google/workbook/implementing-slos/) | medium | User-happiness framing; primary SRE source |
| [fact] Three-party stakeholder agreement required: product manager, development team, SRE team | [Google SRE Workbook: Implementing SLOs](https://sre.google/workbook/implementing-slos/) | medium | Procedural safeguard; required before error budget policy can be adopted |
| [fact] Error budget = 100% minus SLO; exhaustion halts all releases except highest-priority or security fixes | [Google SRE Workbook: Error Budget Policy](https://sre.google/workbook/error-budget-policy/) | medium | Specific policy document with enforcement mechanism and CTO escalation |
| [fact] SRE advises against basing SLO solely on current performance; user evidence is primary input | [Google SRE Workbook: Implementing SLOs](https://sre.google/workbook/implementing-slos/) | medium | Direct quotation; acknowledged as tension with telemetry-first practice |
| [inference] SLO target functions as both minimum and maximum; consistently exceeding it wastes engineering capacity | [Google SRE Book: Embracing Risk](https://sre.google/sre-book/embracing-risk/) | medium | Min/max framing is explicit in source; capability-range conclusion is derived |
| [inference] Error budget loop distinguishes contractual boundary from observed average | [Implementing SLOs](https://sre.google/workbook/implementing-slos/); [Error Budget Policy](https://sre.google/workbook/error-budget-policy/) | medium | Derived from mechanics; not stated as an explicit distinction in a single source sentence |
| [fact] SLO without enforced error budget policy is a passive reporting metric (SLO without teeth) | [Google SRE Workbook: Implementing SLOs](https://sre.google/workbook/implementing-slos/) | medium | Direct statement in workbook |
| [fact] Evernote 99.95% SLO set from user feedback and internal stakeholder discussions | [SRE Workbook: SLO Engineering Case Studies](https://sre.google/workbook/slo-engineering-case-studies/) | medium | Single vendor case study |
| [fact] Chubby planned outage: absence of explicit SLO creates incorrect user availability expectations | [Google SRE Book: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/) | medium | Google-documented empirical case |
| [inference] Economic framework: marginal cost of additional nine vs. marginal revenue gain provides a quantitative ceiling on justifiable stringency | [Google SRE Book: Embracing Risk](https://sre.google/sre-book/embracing-risk/) | medium | Qualitative framework with one illustrative quantified example; ceiling is derived |
| [fact] CTO escalation path for error budget calculation disputes | [Google SRE Workbook: Error Budget Policy](https://sre.google/workbook/error-budget-policy/) | medium | Specific policy document |

### Assumptions

- **Assumption:** Google SRE documentation is representative of established SRE practice across the industry, not only within Google. **Justification:** The SRE book and SRE Workbook are the canonical primary references cited by organisations adopting SRE practices; the Evernote and Home Depot case studies in the SRE Workbook provide cross-organisation corroboration from organisations of different sizes and sectors. [source: https://sre.google/workbook/slo-engineering-case-studies/]

- **Assumption:** The Hidalgo (2020) "Implementing Service Level Objectives" book provides guidance consistent with Google SRE sources on evidence-based threshold selection. **Justification:** Hidalgo was a co-author on the SRE Workbook chapter on implementing SLOs; the O'Reilly book is described as extending the same methodology with statistical analysis tools. [source: https://www.oreilly.com/library/view/implementing-service-level/9781492076803/]

### Analysis

The SRE model provides a specific answer to how a threshold becomes a contractual boundary: through the combination of evidence-based threshold selection and an enforced error budget policy; neither component alone is sufficient. [inference; source: https://sre.google/workbook/implementing-slos/; https://sre.google/workbook/error-budget-policy/] A well-evidenced threshold without an enforced error budget policy produces an "SLO without teeth," and an enforced error budget policy with an inadequately evidenced threshold produces enforcement of an arbitrary number, which can result in heroic efforts to meet an overly aggressive target or a degraded product if the target is too lax. [inference; source: https://sre.google/workbook/implementing-slos/; https://sre.google/sre-book/service-level-objectives/]

The error budget loop is the structural mechanism that distinguishes a contractual boundary from an observed average. [inference; source: https://sre.google/workbook/implementing-slos/; https://sre.google/workbook/error-budget-policy/] An observed average is computed from past measurements and carries no enforcement consequences; an SLO threshold carries them through the error budget policy, making the distinction structural rather than merely semantic: the same reliability number can be a passive average or an enforced boundary depending on whether the error budget policy exists and is acted upon. [inference; source: https://sre.google/workbook/implementing-slos/; https://sre.google/workbook/error-budget-policy/]

The three-party stakeholder agreement requirement ensures that user-impact evidence reaches the threshold-setting process. [inference; source: https://sre.google/workbook/implementing-slos/] The product manager's agreement criterion is explicitly that the threshold must be "good enough for users." [fact; source: https://sre.google/workbook/implementing-slos/] Without this criterion, a threshold could be set based on technical achievability or administrative convenience rather than on user requirements. [inference; source: https://sre.google/workbook/implementing-slos/]

The tension between the advice to avoid basing SLOs on current performance and the practical starting point of current telemetry is resolved through an iterative refinement process: start with an achievable threshold, observe whether it correlates with user satisfaction, and tighten iteratively. [inference; source: https://sre.google/workbook/implementing-slos/] Organisational commitment to acting on the error budget policy at each iteration is a necessary precondition for this refinement process to produce an accurate, user-grounded threshold over time. [inference; source: https://sre.google/workbook/implementing-slos/; https://sre.google/workbook/error-budget-policy/]

The economic constraint framework for threshold selection provides a quantitative ceiling on SLO stringency: a threshold set above what the business can economically justify defending is structurally aspirational rather than contractual, because the organisation lacks the incentive to enforce it consistently. [inference; source: https://sre.google/sre-book/embracing-risk/]

### Risks, Gaps, and Uncertainties

- No controlled before-after studies comparing SLO threshold-setting methods (evidence-based vs. negotiated vs. telemetry-only) and their subsequent reliability, user satisfaction, or engineering efficiency outcomes are cited in the Google SRE sources. Effectiveness claims rest on documented practice and case studies rather than controlled measurement.

- The SRE model assumes organisations are willing and able to enforce the error budget policy. [assumption; justification: The SRE Workbook presents the error budget policy as the intended mechanism but does not report empirical data on adoption rates; source: https://sre.google/workbook/implementing-slos/] The Workbook acknowledges that SLOs remain passive reporting metrics without this enforcement but provides no empirical data on the prevalence of the "SLO without teeth" failure mode in practice. [inference; source: https://sre.google/workbook/implementing-slos/]

- The Evernote case study is a single vendor account from a consumer application; it may not represent SLO-setting practice in regulated, safety-critical, or infrastructure-service contexts.

- The economic framework for availability target selection is presented with one illustrative example and no empirical validation of the cost function shape across service types.

### Open Questions

- What is the empirical distribution of SLO-setting methods across industry, and do evidence-based methods produce measurably better outcomes than negotiated or telemetry-only approaches? (Potential backlog item.)

- In practice, how often do organisations adopt the SLO threshold without implementing an enforced error budget policy, and what measurable reliability outcomes result from the "SLO without teeth" state?

- How should SLO thresholds be set for services with no prior production history, where neither telemetry nor historical user-impact data is available?

---

## Output

- Type: knowledge
- Description: SRE establishes SLO thresholds as contractual capability boundaries through evidence-based threshold selection combined with an enforced error budget policy; neither component alone is sufficient. [inference; source: https://sre.google/workbook/implementing-slos/; https://sre.google/workbook/error-budget-policy/]
- Links:
  - https://sre.google/sre-book/service-level-objectives/
  - https://sre.google/workbook/implementing-slos/
  - https://sre.google/workbook/error-budget-policy/
