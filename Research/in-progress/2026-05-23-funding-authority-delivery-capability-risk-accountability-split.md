---
review_count: 2
title: "Funding authority and delivery-risk accountability split"
added: 2026-05-23T10:24:15+00:00
status: reviewing
priority: high
blocks: []
themes: [organisational-design, governance-policy, cost-performance, enterprise-adoption, software-engineering]
started: 2026-05-23T19:39:12+00:00
completed: ~
output: [knowledge]
cites:
  - 2026-05-14-org-failure-modes-split-risk-cost-benefits-accountability
  - 2026-05-16-governance-structures-build-mode-without-full-accountability-colocation
  - 2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance
  - 2026-05-23-governance-controls-effectiveness-conditions
related:
  - 2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention
  - 2026-05-19-how-do-formal-governance-structures-distort-cross-department-knowledge-flows
  - 2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Funding authority and delivery-risk accountability split

## Research Question

What governance and commercial structures best preserve delivery velocity, delivered quality, delivered risk control, delivery cost, and total cost of ownership when funding authority sits with a party that lacks delivery capability while delivery and operational risk accountability sit with a separate party that has delivery capability but no funding authority?

## Scope

**In scope:**
- Delivery models where budget approval rights and delivery capability are split across two parties
- Effects on delivery velocity, delivery quality, delivered risk, delivery cost, and total cost of ownership
- Governance mechanisms that can realign incentives, for example decision rights, joint accountability, funding gates, and service-level contracts

**Out of scope:**
- Single-party delivery models where funding authority and delivery accountability are co-located
- Sector-specific procurement law detail by jurisdiction
- Detailed financial modelling for one specific organisation

**Constraints:** (time, source types, access)
- Use publicly accessible sources available on the open web
- Prioritise empirical studies, operations research, and major practitioner datasets over opinion-only material
- Focus on evidence published in the last 10 years, while including foundational agency-theory references where needed

## Context

When funding authority, prioritisation rights, and exception handling sit away from the team that sees delivery and operational risk directly, the core trade-offs about scope, timing, reliability, and cost are more likely to be settled through inter-party negotiation than by the accountable delivery team. [inference; source: https://cisr.mit.edu/content/classic-topics-decision-rights; https://cisr.mit.edu/content/simplifying-decision-rights-growth; https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-split-risk-cost-benefits-accountability.html]

Recent government reviews also show that funding and control models often remain poorly matched to modern digital delivery because they privilege predictable business cases, capital approvals, and central process assurance over continuous improvement, resilience, and flexible execution. [fact; source: https://www.gov.uk/government/publications/state-of-digital-government-review/state-of-digital-government-review; https://www.nao.org.uk/reports/digital-transformation-in-government-addressing-the-barriers/; https://www.nao.org.uk/insights/six-reasons-why-digital-transformation-is-still-a-problem-for-government/]

Modern development and operations (DevOps), Site Reliability Engineering (SRE), and Financial Operations (FinOps) guidance all point toward the same structural requirement: the team expected to deliver and run the service needs routine authority over day-to-day technical, service, and cost trade-offs inside clearly defined guardrails. [inference; source: https://docs.cloud.google.com/architecture/devops; https://sre.google/sre-book/embracing-risk/; https://www.finops.org/framework/principles/]

## Approach

1. Define the failure modes created by this split, including incentive misalignment, handoff delay, and accountability diffusion, and map each mode to measurable outcomes.
2. Review evidence on delivery velocity impact under split authority versus co-located authority models.
3. Review evidence on quality outcomes, including defect rates, rework, reliability, and maintainability, under split authority structures.
4. Review evidence on risk outcomes, including risk transfer, latent operational risk, and maintenance burden.
5. Review evidence on direct delivery cost and downstream total cost of ownership under split versus aligned authority models.
6. Identify governance and contracting patterns that mitigate the split, and specify conditions where they succeed or fail.

## Sources

- [ ] [Jensen and Meckling (1976) Theory of the Firm: Managerial Behavior, Agency Costs and Ownership Structure](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=94043) - seeded source checked; the Social Science Research Network (SSRN) page returned 403 in this session, so downstream claims use accessible governance and audit sources instead of this blocked landing page.
- [ ] [Forsgren, Humble, and Kim (2018) Accelerate: The Science of Lean Software and DevOps](https://itrevolution.com/product/accelerate/) - seeded source checked; the product page is accessible, but downstream claims rely on the public Google Cloud DevOps and DevOps Research and Assessment (DORA) pages that expose the relevant findings directly.
- [x] [Google Site Reliability Engineering Book](https://sre.google/sre-book/table-of-contents/) - consulted as the canonical book entry for operational ownership and risk trade-offs.
- [x] [Google Site Reliability Engineering Book: Embracing Risk](https://sre.google/sre-book/embracing-risk/) - consulted for the direct risk, speed, and cost trade-off framing.
- [x] [Google Site Reliability Engineering Book: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/) - consulted for the metric and accountability framing for service outcomes.
- [x] [Google Cloud Architecture Center DevOps capabilities](https://docs.cloud.google.com/architecture/devops) - consulted for the explicit guidance to replace heavyweight change approval with peer review.
- [x] [Google Cloud (2024) Announcing the 2024 DORA report](https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report) - consulted for the current DORA framing on software delivery performance and developer workflow.
- [x] [MIT Center for Information Systems Research (MIT CISR) Classic Topics: Decision Rights](https://cisr.mit.edu/content/classic-topics-decision-rights) - consulted for the definition of governance as the allocation of decision rights and accountabilities.
- [x] [MIT Center for Information Systems Research (MIT CISR) (2023) Simplifying decision rights for growth](https://cisr.mit.edu/content/simplifying-decision-rights-growth) - consulted for the key decision-right categories, especially investment prioritisation and exception handling.
- [x] [FinOps Foundation Framework Overview](https://www.finops.org/framework/) - consulted for the FinOps operating-model baseline.
- [x] [FinOps Foundation Principles](https://www.finops.org/framework/principles/) - consulted for decentralized cost accountability and central enablement.
- [x] [FinOps Foundation Personas](https://www.finops.org/framework/personas/) - consulted for the required cross-functional collaboration between engineering, finance, and service-management roles.
- [x] [National Audit Office (2023) Digital transformation in government: addressing the barriers](https://www.nao.org.uk/reports/digital-transformation-in-government-addressing-the-barriers/) - consulted for systemic delivery barriers, capability constraints, and central-versus-department governance issues.
- [x] [National Audit Office (2021) Six reasons why digital transformation is still a problem for government](https://www.nao.org.uk/insights/six-reasons-why-digital-transformation-is-still-a-problem-for-government/) - consulted for flexible contracting, governance, coordination, and funding lessons.
- [x] [Government of the United Kingdom (2025) State of digital government review](https://www.gov.uk/government/publications/state-of-digital-government-review/state-of-digital-government-review) - consulted for evidence on funding-model mismatch, fragmented delivery, legacy burden, and role-mix imbalance.
- [x] [Technology Modernization Fund Homepage](https://tmf.cio.gov/) - consulted for milestone-based funding release and return-on-investment gating.
- [x] [Technology Modernization Fund Board](https://tmf.cio.gov/board/) - consulted for the board's investment-evaluation and performance-monitoring role.
- [x] [United States Shared Services Management Governance ecosystem](https://ussm.gsa.gov/governance/) - consulted for the explicit escalation, coordination, and accountable-point-of-contact model.
- [x] [Mitchell (2026) Organisational failure modes: risk, operational cost, and benefits accountability in separate business units](https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-split-risk-cost-benefits-accountability.html) - consulted as the closest prior repository item on the missing-integrator failure mode.
- [x] [Mitchell (2026) Governance structures that support investment in delivery capability without one owner for risk, cost, and benefits](https://davidamitchell.github.io/Research/research/2026-05-16-governance-structures-build-mode-without-full-accountability-colocation.html) - consulted for the earlier synthesis on minimum authority bundles.
- [x] [Mitchell (2026) Governance designs where explicit integrator rights substitute for co-location of risk, cost, and benefits](https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html) - consulted for the conditions under which explicit integrator rights work.
- [x] [Mitchell (2026) Conditions under which internal governance controls minimise coordination costs in regulated enterprises](https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html) - consulted for the proportionality and ownership qualifier.

---

## Research Skill Output

### §0 Initialise

Question: what governance and commercial structures best preserve delivery velocity, quality, risk control, cost, and total cost of ownership when the money sits with a party that lacks delivery capability and the delivery risk sits with a different party that lacks funding authority?

Scope: compare split-authority delivery models with stronger integrator designs, with emphasis on decision rights, funding mechanics, contracting patterns, and operational-accountability structures; detailed jurisdiction-specific procurement law and single-firm redesign are out of scope.

Constraints: public web sources only, full-mode research, explicit [fact] or [inference] labels, URL-backed citations throughout, and repeated cross-reference to adjacent completed items that touch the same governance surface.

Output: knowledge, specifically a structured synthesis with executive summary, key findings, evidence map, assumptions, analysis, risks and gaps, open questions, and output details.

Mode: full.

- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-split-risk-cost-benefits-accountability.html; https://davidamitchell.github.io/Research/research/2026-05-16-governance-structures-build-mode-without-full-accountability-colocation.html; https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html] Prior-work scan found four directly relevant completed items on the missing-integrator problem, authority bundles for non-co-located accountability, explicit integrator rights, and the conditions that keep controls proportionate.
- [inference; source: https://cisr.mit.edu/content/classic-topics-decision-rights; https://cisr.mit.edu/content/simplifying-decision-rights-growth; https://www.gov.uk/government/publications/state-of-digital-government-review/state-of-digital-government-review] In this item, the decisive split is not only financial, but also decisional: the same parties who are separated by budget authority are often also separated by prioritisation authority, exception handling, and ongoing operating-fund discretion.
- [assumption; source: https://www.finops.org/framework/principles/; https://sre.google/sre-book/embracing-risk/; https://ussm.gsa.gov/governance/] The term "party" is treated functionally rather than legally here, so it can mean a business unit, shared-service function, programme office, or supplier-side commercial actor whenever the same decision-right split is present.

### §1 Question Decomposition

```text
Q. Which structures preserve delivery outcomes when funding authority and delivery accountability are split?
├── A. Mechanism definition
│   ├── A1. Which decision rights are separated in the target operating model?
│   ├── A2. Which outcomes expose the split: speed, quality, risk, cost, or total cost of ownership?
│   └── A3. Which earlier completed items already explain the missing-integrator mechanism?
├── B. Delivery-velocity effects
│   ├── B1. What happens when approvals or reprioritisation sit outside the delivery team?
│   ├── B2. What evidence compares heavyweight approval with peer review or delegated authority?
│   └── B3. What governance still remains necessary around exceptions?
├── C. Quality and risk effects
│   ├── C1. What happens to reliability and technical-debt choices when the team lacks budget discretion?
│   ├── C2. How are service-level trade-offs supposed to be closed?
│   └── C3. What risk-control failures recur when funding is mismatched to operations?
├── D. Cost and total-cost effects
│   ├── D1. What happens when funding models favour project capital over ongoing service operation?
│   ├── D2. What does FinOps say about where cost accountability should sit?
│   └── D3. Which funding mechanisms create better alignment?
├── E. Mitigation patterns
│   ├── E1. Which decision-right bundles close the trade-offs?
│   ├── E2. Which commercial or milestone-funding patterns help?
│   └── E3. Under what conditions can explicit integrator rights substitute for full co-location?
└── F. Boundary conditions
    ├── F1. When is a split-authority model tolerable?
    └── F2. When is structural reallocation of authority the safer answer?
```

### §2 Investigation

#### 2.1 Source checks and prior-work sweep

```text
failed_primary_search:
  - query: Jensen Meckling 1976 agency costs pdf
    inspected: Social Science Research Network (SSRN) abstract page, index pages
    accessible_primary_text: none_retrieved_in_session
  - query: Accelerate change approval DORA public
    inspected: book product page, Google Cloud Architecture Center page, current DORA pages
    accessible_primary_text: public Google Cloud pages only
source_correction:
  - original_2021_nao_report_page: https://www.nao.org.uk/reports/the-challenges-in-implementing-digital-change/
    session_outcome: 404
    replacement_evidence_family: official National Audit Office insight page and 2023 barrier report
prior_work_repeat_scan:
  directly_cited:
    - 2026-05-14-org-failure-modes-split-risk-cost-benefits-accountability
    - 2026-05-16-governance-structures-build-mode-without-full-accountability-colocation
    - 2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance
    - 2026-05-23-governance-controls-effectiveness-conditions
  thematically_related:
    - 2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention
    - 2026-05-19-how-do-formal-governance-structures-distort-cross-department-knowledge-flows
    - 2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates
```
- [fact; source: https://cisr.mit.edu/content/classic-topics-decision-rights] MIT CISR defines governance as a company's allocation of decision rights and accountabilities, and says clear specification of both is key to progress on digital transformation.
- [fact; source: https://cisr.mit.edu/content/simplifying-decision-rights-growth] MIT CISR identifies the few decisions that matter most in digital transformation as who decides what versus how, how much is invested and how spending is prioritised, and who handles exceptions.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-split-risk-cost-benefits-accountability.html] The closest prior completed item found a recurring missing-integrator failure mode when risk, cost, and benefits sit in separate units.
- [inference; source: https://cisr.mit.edu/content/classic-topics-decision-rights; https://cisr.mit.edu/content/simplifying-decision-rights-growth; https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-split-risk-cost-benefits-accountability.html] The present question is therefore best treated as a narrower operating-model variant of the missing-integrator problem, with budget approval rights as the most visible missing decision right.

#### 2.2 Delivery velocity under split authority

- [fact; source: https://docs.cloud.google.com/architecture/devops] Google Cloud's DevOps guidance says teams should replace heavyweight change-approval processes with peer review to get the benefits of a more reliable, compliant release process without sacrificing speed.
- [fact; source: https://www.nao.org.uk/insights/six-reasons-why-digital-transformation-is-still-a-problem-for-government/] The National Audit Office says that, when agile methods are used, strong governance, effective coordination of activities, and robust progress reporting still need to be in place.
- [fact; source: https://www.gov.uk/government/publications/state-of-digital-government-review/state-of-digital-government-review] The 2025 state of digital government review says existing governance and controls processes are not well suited to digital programmes because they prioritise predictable returns and do not allow for the flexible nature of digital delivery.
- [fact; source: https://www.nao.org.uk/reports/digital-transformation-in-government-addressing-the-barriers/] The 2023 National Audit Office report says stronger levers for delivery were created through permanent-secretary-level sponsors and boards, but also warns that small central budgets and headcount constrain the intended reforms.
- [inference; source: https://docs.cloud.google.com/architecture/devops; https://cisr.mit.edu/content/simplifying-decision-rights-growth; https://www.gov.uk/government/publications/state-of-digital-government-review/state-of-digital-government-review; https://www.nao.org.uk/reports/digital-transformation-in-government-addressing-the-barriers/] Delivery velocity degrades when funding authority sits outside the delivery-capable party because prioritisation, spend approval, and exception handling become external queueing events rather than routine delivery decisions.

#### 2.3 Delivered quality and risk control

- [fact; source: https://sre.google/sre-book/embracing-risk/] Google's Site Reliability Engineering (SRE) guidance says extreme reliability has rising cost and slows feature delivery, and that the goal is to align the risk taken by a service with the risk the business is willing to bear.
- [fact; source: https://sre.google/sre-book/embracing-risk/] The same chapter says SREs must work with product owners to turn business goals into explicit objectives to which engineers can build.
- [fact; source: https://sre.google/sre-book/service-level-objectives/] The Service Level Objectives chapter says service-level indicators, objectives, and agreements exist to define what matters, what values are expected, and how the organisation will react if those values are missed.
- [fact; source: https://www.gov.uk/government/publications/state-of-digital-government-review/state-of-digital-government-review] The 2025 review says many public systems lack adequate incident-management plans, service reliability is too low, and budgets frequently prioritise new programmes over continuous improvement and legacy remediation.
- [inference; source: https://sre.google/sre-book/embracing-risk/; https://sre.google/sre-book/service-level-objectives/; https://www.gov.uk/government/publications/state-of-digital-government-review/state-of-digital-government-review] Delivered quality and risk control worsen when the party accountable for operation cannot directly fund reliability work, technical-debt reduction, or service-level trade-offs, because the accountable party can describe the risk but cannot close the trade-off.

#### 2.4 Direct cost and total cost of ownership

- [fact; source: https://www.finops.org/framework/principles/] FinOps says accountability for usage and cost should be pushed to the edge, with engineers taking ownership of costs from architecture design to ongoing operations.
- [fact; source: https://www.finops.org/framework/principles/] FinOps also says individual feature and product teams should be empowered to manage their own mix of technology usage against budgets they help control, while a central FinOps function enables shared accountability.
- [fact; source: https://www.finops.org/framework/personas/] FinOps personas guidance says engineering, finance, product, Information Technology Financial Management (ITFM), and Information Technology Service Management (ITSM) roles must collaborate rather than treat cloud cost as a finance-only concern.
- [fact; source: https://www.gov.uk/government/publications/state-of-digital-government-review/state-of-digital-government-review] The 2025 review says modern digital delivery is now revenue-intensive and based on continuous improvement and subscription services, but central-government digital funding still undersupplies resource funding relative to peer benchmarks and only one in five survey respondents felt the current funding model enabled effective investment in and running of digital services.
- [fact; source: https://tmf.cio.gov/; https://tmf.cio.gov/board/] The United States Technology Modernization Fund uses flexible and incremental funding, releases transfers only as project milestones are completed, and uses a board of senior technology executives to evaluate investments and monitor project performance.
- [inference; source: https://www.finops.org/framework/principles/; https://www.finops.org/framework/personas/; https://www.gov.uk/government/publications/state-of-digital-government-review/state-of-digital-government-review; https://tmf.cio.gov/; https://tmf.cio.gov/board/] Split-authority models usually increase total cost of ownership because they separate the budget-holder from the engineers who can optimize spend in design and operations, while one-off or capital-leaning approvals underfund the recurring work that keeps services healthy over time.

#### 2.5 Governance and commercial patterns that mitigate the split

- [fact; source: https://ussm.gsa.gov/governance/] The United States shared-services governance model uses a Shared Services Governance Board as an escalation point and assigns a Senior Accountable Point of Contact to coordinate across agency mission-support functions.
- [fact; source: https://www.nao.org.uk/insights/six-reasons-why-digital-transformation-is-still-a-problem-for-government/] The National Audit Office recommends early engagement with commercial partners, flexible contracting that recognises changing scope and requirements, and a partnership model with suppliers.
- [fact; source: https://cisr.mit.edu/content/simplifying-decision-rights-growth] MIT CISR treats exception handling as one of the few decisions that must be explicitly assigned in digital transformation.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html] The prior integrator-rights item found that explicit integrator rights can substitute for structural co-location when the escalation body can force resolution, performance is measurable, and local teams keep enough execution authority to make day-to-day trade-offs quickly.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html] The prior governance-controls item found that effective controls stay proportionate when they have clear ownership, explicit authority, and review tied to real change rather than generic process accumulation.
- [inference; source: https://ussm.gsa.gov/governance/; https://www.nao.org.uk/insights/six-reasons-why-digital-transformation-is-still-a-problem-for-government/; https://cisr.mit.edu/content/simplifying-decision-rights-growth; https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html] The strongest mitigation pattern is a two-level structure: delegated day-to-day delivery and operating authority inside a ring-fenced budget envelope for the delivery-capable team, combined with a small integrator layer that owns portfolio allocation, exception adjudication, and milestone release rather than universal pre-approval.

#### 2.6 Failure boundary

- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html] The adjacent governance-failure item shows that control systems become bureaucratic overhead when control intensity no longer matches the actual risk profile and reversibility of the work, and when proxy compliance displaces the underlying objective.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-19-how-do-formal-governance-structures-distort-cross-department-knowledge-flows.html] The adjacent knowledge-flow item finds that centralized governance distorts cross-boundary work when it substitutes vertical routing for the local context and lateral relationships needed to resolve ambiguity.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html; https://davidamitchell.github.io/Research/research/2026-05-19-how-do-formal-governance-structures-distort-cross-department-knowledge-flows.html; https://www.gov.uk/government/publications/state-of-digital-government-review/state-of-digital-government-review] A split funding-authority model becomes unsafe or uneconomic when approvals accumulate faster than learning, when local delivery teams cannot change spend or scope inside guardrails, or when continuous-improvement work has to compete repeatedly with new-project business cases.

### §3 Reasoning

- [fact; source: https://cisr.mit.edu/content/classic-topics-decision-rights; https://cisr.mit.edu/content/simplifying-decision-rights-growth; https://docs.cloud.google.com/architecture/devops; https://www.finops.org/framework/principles/] Direct external evidence supports four linked propositions: governance is a question of decision-right allocation, a few digital decisions matter disproportionately, heavy external change approval is counterproductive, and cost accountability should sit with the teams making technical choices.
- [fact; source: https://sre.google/sre-book/embracing-risk/; https://www.gov.uk/government/publications/state-of-digital-government-review/state-of-digital-government-review; https://www.nao.org.uk/insights/six-reasons-why-digital-transformation-is-still-a-problem-for-government/] Direct external evidence also supports that risk, resilience, and continuous-improvement work require ongoing trade-offs and ongoing funding rather than one-off programme approvals.
- [inference; source: https://docs.cloud.google.com/architecture/devops; https://sre.google/sre-book/embracing-risk/; https://www.finops.org/framework/principles/; https://tmf.cio.gov/; https://ussm.gsa.gov/governance/] No single public source directly compares all five requested outcome variables under the exact same split-authority pattern, so the conclusion is a mechanism-based synthesis across software-delivery research, operations guidance, funding reviews, and governance operating models.
- [assumption; source: https://www.gov.uk/government/publications/state-of-digital-government-review/state-of-digital-government-review; https://www.nao.org.uk/reports/digital-transformation-in-government-addressing-the-barriers/] Public-sector digital-delivery evidence is used as structurally relevant here because the same split between budget holders, central controls, and delivery-accountable teams is explicitly described in the reviewed government sources.

### §4 Consistency Check

```text
contradiction_scan: resolved
source_scope_check: maintained
comparative_claims: kept inferential unless the source made the comparison directly
repository_cross_reference_sweep: repeated and incorporated
confidence_adjustment: overall item kept at medium because the synthesis depends on converging authoritative sources rather than one direct comparative study
```

### §5 Depth and Breadth Expansion

- [inference; source: https://docs.cloud.google.com/architecture/devops; https://sre.google/sre-book/embracing-risk/] Technical lens: the split is most damaging where delivery needs fast local trade-offs, because central approval can validate conformity but cannot replace the local engineering judgment needed to balance release speed, reliability, and debt reduction.
- [inference; source: https://www.finops.org/framework/principles/; https://www.gov.uk/government/publications/state-of-digital-government-review/state-of-digital-government-review] Economic lens: the decisive cost issue is not only whether work is funded, but whether the accountable delivery team controls enough operating budget to act on cost signals before waste becomes embedded.
- [inference; source: https://www.nao.org.uk/insights/six-reasons-why-digital-transformation-is-still-a-problem-for-government/; https://tmf.cio.gov/] Commercial lens: contracts and funding gates help only when they are flexible enough to accommodate learning and when milestone release is tied to observable progress rather than static front-loaded specification.
- [inference; source: https://ussm.gsa.gov/governance/; https://cisr.mit.edu/content/simplifying-decision-rights-growth] Organisational lens: explicit integrator rights are a practical substitute for full structural co-location only when a named escalation body can decide exceptions and a named accountable contact can coordinate across functions continuously.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html; https://davidamitchell.github.io/Research/research/2026-05-19-how-do-formal-governance-structures-distort-cross-department-knowledge-flows.html] Behavioural lens: if shared metrics and local discretion are missing, the split drifts toward proxy optimisation, queue-clearing, and blame transfer, because each party optimises the metric it owns rather than the service outcome the enterprise wants.

### §6 Synthesis

**Executive summary**

- [inference; source: https://cisr.mit.edu/content/classic-topics-decision-rights; https://cisr.mit.edu/content/simplifying-decision-rights-growth; https://docs.cloud.google.com/architecture/devops; https://www.finops.org/framework/principles/; https://sre.google/sre-book/embracing-risk/] The strongest supported answer is a product or service-aligned delivery team that holds routine delivery and operating authority inside a ring-fenced budget envelope, while a small central integrator retains portfolio-allocation, exception, and milestone-release rights instead of approving every change.
- [inference; source: https://www.gov.uk/government/publications/state-of-digital-government-review/state-of-digital-government-review; https://www.nao.org.uk/insights/six-reasons-why-digital-transformation-is-still-a-problem-for-government/; https://tmf.cio.gov/; https://ussm.gsa.gov/governance/] Split-authority models fail when funding approval remains project-like, capital-biased, or committee-heavy, because the delivery-capable party then inherits reliability, legacy, and maintenance obligations without the budget discretion needed to manage them.
- [inference; source: https://docs.cloud.google.com/architecture/devops; https://sre.google/sre-book/service-level-objectives/; https://www.finops.org/framework/personas/] The evidence points toward relocating central governance to guardrails, portfolio pacing, and escalation rather than abolishing it, because the reviewed sources still assign a central role to metrics, exception handling, and investment oversight.

**Key findings**

1. [inference; source: https://docs.cloud.google.com/architecture/devops; https://cisr.mit.edu/content/simplifying-decision-rights-growth; https://www.gov.uk/government/publications/state-of-digital-government-review/state-of-digital-government-review] Split funding authority usually slows delivery because prioritisation, spend approval, and exception handling move into external forums, even though public DevOps guidance says heavy external approval should be replaced by peer review and lightweight guardrails.
2. [inference; source: https://sre.google/sre-book/embracing-risk/; https://sre.google/sre-book/service-level-objectives/; https://www.gov.uk/government/publications/state-of-digital-government-review/state-of-digital-government-review] Delivered quality and risk control degrade when the accountable operator cannot directly fund reliability work, because service-level trade-offs, incident readiness, and technical-debt choices then depend on a budget holder who does not see the operational consequences first-hand.
3. [inference; source: https://www.finops.org/framework/principles/; https://www.finops.org/framework/personas/; https://www.gov.uk/government/publications/state-of-digital-government-review/state-of-digital-government-review] Total cost of ownership rises under split models when cost accountability is detached from engineering decisions, because teams that create spend do not control enough of the budget to optimize architecture and operating choices continuously.
4. [inference; source: https://tmf.cio.gov/; https://tmf.cio.gov/board/; https://www.nao.org.uk/insights/six-reasons-why-digital-transformation-is-still-a-problem-for-government/] Milestone-based and outcome-aware funding releases are one credible way to keep central investment control while allowing delivery-capable teams to learn, adapt scope, and draw money incrementally as measurable progress is demonstrated.
5. [inference; source: https://ussm.gsa.gov/governance/; https://cisr.mit.edu/content/simplifying-decision-rights-growth; https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html] The most reliable substitute for full structural co-location is a named integrator with explicit authority over portfolio allocation, exceptions, and escalation, plus a named accountable contact inside each participating unit.
6. [inference; source: https://www.nao.org.uk/insights/six-reasons-why-digital-transformation-is-still-a-problem-for-government/; https://www.gov.uk/government/publications/state-of-digital-government-review/state-of-digital-government-review] Commercial structures should budget for both build and run costs and should allow changing scope, because rigid capital-heavy or specification-heavy models systematically underfund the ongoing work that keeps services safe and useful.
7. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html; https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html; https://davidamitchell.github.io/Research/research/2026-05-19-how-do-formal-governance-structures-distort-cross-department-knowledge-flows.html] Split-authority governance becomes counterproductive when control intensity exceeds the actual risk profile and reversibility of the work, because the result is queueing, proxy compliance, and escalation traffic rather than faster learning or better risk reduction.
8. [inference; source: https://www.finops.org/framework/principles/; https://docs.cloud.google.com/architecture/devops; https://sre.google/sre-book/service-level-objectives/] A well-supported operating pattern combines delegated delivery authority, central guardrails, shared outcome metrics, and approval-by-exception, which keeps central review focused on exceptions instead of routine local technical and operational choices.

**Evidence map**

| claim | source | confidence | notes |
|---|---|---|---|
| [inference] Delivery slows when prioritisation, spend approval, and exceptions sit outside the delivery team. | https://docs.cloud.google.com/architecture/devops; https://cisr.mit.edu/content/simplifying-decision-rights-growth; https://www.gov.uk/government/publications/state-of-digital-government-review/state-of-digital-government-review | medium | approval queue, external decision rights |
| [inference] Quality and risk control weaken when operators cannot fund reliability trade-offs directly. | https://sre.google/sre-book/embracing-risk/; https://sre.google/sre-book/service-level-objectives/; https://www.gov.uk/government/publications/state-of-digital-government-review/state-of-digital-government-review | medium | reliability, service levels, incident readiness |
| [inference] Total cost of ownership rises when engineering decisions and cost accountability are separated. | https://www.finops.org/framework/principles/; https://www.finops.org/framework/personas/; https://www.gov.uk/government/publications/state-of-digital-government-review/state-of-digital-government-review | medium | edge accountability, operating-fund gap |
| [inference] Milestone-based funding releases are one credible way to keep central investment control while allowing incremental delivery. | https://tmf.cio.gov/; https://tmf.cio.gov/board/; https://www.nao.org.uk/insights/six-reasons-why-digital-transformation-is-still-a-problem-for-government/ | medium | incremental release, monitored progress |
| [inference] Named integrator rights are the strongest substitute for full co-location. | https://ussm.gsa.gov/governance/; https://cisr.mit.edu/content/simplifying-decision-rights-growth; https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html | medium | escalation, exception handling, accountable contact |
| [inference] Flexible contracts and combined build-run funding help reduce downstream burden. | https://www.nao.org.uk/insights/six-reasons-why-digital-transformation-is-still-a-problem-for-government/; https://www.gov.uk/government/publications/state-of-digital-government-review/state-of-digital-government-review | medium | flexible scope, resource funding |
| [inference] Over-governed split models drift into proxy compliance and coordination overhead. | https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html; https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html; https://davidamitchell.github.io/Research/research/2026-05-19-how-do-formal-governance-structures-distort-cross-department-knowledge-flows.html | medium | control intensity, bureaucracy, distortion |
| [inference] Delegated delivery authority plus central guardrails keeps central review focused on exceptions. | https://www.finops.org/framework/principles/; https://docs.cloud.google.com/architecture/devops; https://sre.google/sre-book/service-level-objectives/ | medium | approval-by-exception, shared metrics |

**Assumptions**

- [assumption; source: https://www.finops.org/framework/principles/; https://sre.google/sre-book/embracing-risk/] The same team that is best placed to control direct delivery choices is also usually best placed to control a meaningful portion of ongoing operating cost, because architecture and reliability decisions are major cost drivers.
- [assumption; source: https://www.gov.uk/government/publications/state-of-digital-government-review/state-of-digital-government-review; https://www.nao.org.uk/reports/digital-transformation-in-government-addressing-the-barriers/] Public-sector digital-governance evidence is sufficiently analogous to enterprise delivery governance for this item's mechanism-level conclusions, because both settings document the same capital-versus-resource and centre-versus-delivery tensions.
- [assumption; source: https://ussm.gsa.gov/governance/; https://tmf.cio.gov/] A ring-fenced delivery budget envelope can be operationalised inside a split-authority enterprise even if the legal appropriation or top-level approval remains central, because the reviewed governance models show delegation inside centrally controlled funding structures.

**Analysis**

- [inference; source: https://cisr.mit.edu/content/classic-topics-decision-rights; https://cisr.mit.edu/content/simplifying-decision-rights-growth; https://docs.cloud.google.com/architecture/devops] The evidence weighs most heavily toward authority placement rather than generic "collaboration" because the most concrete external sources all name specific decision categories, and the clearest delivery-performance guidance is to remove heavy external approval from routine change decisions.
- [inference; source: https://sre.google/sre-book/embracing-risk/; https://www.finops.org/framework/principles/; https://www.gov.uk/government/publications/state-of-digital-government-review/state-of-digital-government-review] Speed, quality, risk, and cost are not separate outcome families here, because the reviewed sources repeatedly show that the same governance placement determines whether those trade-offs can be closed in real time or only debated after harm appears.
- [inference; source: https://tmf.cio.gov/; https://tmf.cio.gov/board/; https://ussm.gsa.gov/governance/; https://www.nao.org.uk/insights/six-reasons-why-digital-transformation-is-still-a-problem-for-government/] The most credible commercial compromise is not unrestricted local autonomy, but staged delegation: central actors keep investment pacing, escalation, and guardrails, while delivery-capable teams receive enough budgetary and operational discretion to act without reopening the whole business case for routine decisions.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html] The repository cross-reference sharpens the boundary condition: explicit integrator rights can work, but only when they are backed by real authority, measurable service outcomes, and proportionate review rather than by another layer of committee process.
- [inference; source: https://www.gov.uk/government/publications/state-of-digital-government-review/state-of-digital-government-review; https://www.nao.org.uk/reports/digital-transformation-in-government-addressing-the-barriers/] Capability shortages, legacy burden, and sector-specific funding constraints also materially affect delivery outcomes, and the funding-authority split matters most when it amplifies those baseline constraints by making local trade-offs slower or harder to fund.

**Risks, gaps, uncertainties**

- [inference; source: https://cisr.mit.edu/content/classic-topics-decision-rights; https://docs.cloud.google.com/architecture/devops; https://www.finops.org/framework/principles/] The public evidence base is strong on mechanism families, but thinner on direct head-to-head comparative studies that isolate this exact split from all other organisational differences.
- [inference; source: https://www.nao.org.uk/insights/six-reasons-why-digital-transformation-is-still-a-problem-for-government/; https://www.gov.uk/government/publications/state-of-digital-government-review/state-of-digital-government-review] Government evidence is highly relevant to split authority, but some sector-specific frictions may overstate the severity of the problem for private firms with simpler capital-allocation paths.

**Open questions**

- How far can delegated budget envelopes be pushed in heavily regulated sectors before legal or prudential constraints require a different authority pattern?
- Which service-level metric bundle best predicts when approval-by-exception should tighten back into pre-execution review?
- What contractual clauses most effectively tie supplier incentives to long-run service reliability instead of short-run delivery milestones?

### §7 Recursive Review

```text
review_result: pass
acronym_audit: passed
domain_term_audit: passed
claim_label_audit: passed
findings_parity_check: passed
source_url_check: passed
repository_cross_reference_repeat: completed
```

---

## Findings

### Executive Summary

The strongest supported structure is a product or service-aligned delivery team that holds routine delivery and operating authority inside a ring-fenced budget envelope, while a small central integrator retains portfolio-allocation, exception, and milestone-release rights instead of approving every change. [inference; source: https://cisr.mit.edu/content/classic-topics-decision-rights; https://cisr.mit.edu/content/simplifying-decision-rights-growth; https://docs.cloud.google.com/architecture/devops; https://www.finops.org/framework/principles/]

When funding authority remains external and committee-heavy, delivery speed, reliability, and total cost of ownership usually worsen because the team carrying operational risk cannot close trade-offs about scope, reliability, technical debt, and spend in real time. [inference; source: https://sre.google/sre-book/embracing-risk/; https://sre.google/sre-book/service-level-objectives/; https://www.gov.uk/government/publications/state-of-digital-government-review/state-of-digital-government-review]

The evidence points away from abolishing central governance and toward relocating it, so that central actors own guardrails, portfolio pacing, and escalation while delivery-capable teams own routine engineering, service, and cost decisions inside those guardrails. [inference; source: https://www.nao.org.uk/insights/six-reasons-why-digital-transformation-is-still-a-problem-for-government/; https://tmf.cio.gov/; https://ussm.gsa.gov/governance/; https://docs.cloud.google.com/architecture/devops; https://www.finops.org/framework/personas/; https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html]

### Key Findings

1. **When funding authority, prioritisation, and exception handling are separated from the team that carries delivery and operational risk, delivery usually slows because decisions queue in external forums that modern DevOps guidance and recent government reviews both describe as poorly suited to flexible digital work.** ([inference]; medium confidence; source: https://docs.cloud.google.com/architecture/devops; https://cisr.mit.edu/content/simplifying-decision-rights-growth; https://www.gov.uk/government/publications/state-of-digital-government-review/state-of-digital-government-review)
2. **Delivered quality and operational risk control weaken when the accountable operator cannot directly fund reliability work, because service-level trade-offs, incident readiness, and technical-debt reduction then depend on a budget holder who does not experience the operational consequences first-hand.** ([inference]; medium confidence; source: https://sre.google/sre-book/embracing-risk/; https://sre.google/sre-book/service-level-objectives/; https://www.gov.uk/government/publications/state-of-digital-government-review/state-of-digital-government-review)
3. **Total cost of ownership increases under split-authority models when cost accountability is detached from engineering decisions, because the teams that determine architecture and usage patterns do not control enough of the operating budget to optimize spend continuously.** ([inference]; medium confidence; source: https://www.finops.org/framework/principles/; https://www.finops.org/framework/personas/; https://www.gov.uk/government/publications/state-of-digital-government-review/state-of-digital-government-review)
4. **Milestone-based and outcome-aware funding releases are one credible way to keep central investment control while allowing delivery-capable teams to learn, adapt scope, and draw money incrementally as measurable progress is demonstrated.** ([inference]; medium confidence; source: https://tmf.cio.gov/; https://tmf.cio.gov/board/; https://www.nao.org.uk/insights/six-reasons-why-digital-transformation-is-still-a-problem-for-government/)
5. **The strongest supported substitute for full structural co-location is a named integrator with explicit authority over portfolio allocation, exception handling, and escalation, combined with a named accountable contact inside each participating unit that can turn central decisions into local action quickly.** ([inference]; medium confidence; source: https://ussm.gsa.gov/governance/; https://cisr.mit.edu/content/simplifying-decision-rights-growth; https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html)
6. **Commercial arrangements should budget for both build and run costs and permit changing scope, because rigid capital-heavy or specification-heavy models systematically underfund the ongoing maintenance, resilience, and integration work that determines long-run service performance.** ([inference]; medium confidence; source: https://www.nao.org.uk/insights/six-reasons-why-digital-transformation-is-still-a-problem-for-government/; https://www.gov.uk/government/publications/state-of-digital-government-review/state-of-digital-government-review)
7. **Split-authority governance becomes counterproductive when control intensity exceeds the actual risk profile and reversibility of the work, because the result is queueing, proxy compliance, and escalation traffic rather than materially better risk reduction or faster learning.** ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html; https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html; https://davidamitchell.github.io/Research/research/2026-05-19-how-do-formal-governance-structures-distort-cross-department-knowledge-flows.html)
8. **A well-supported operating pattern combines delegated delivery authority, central guardrails, shared outcome metrics, and approval-by-exception, which keeps central review focused on exceptions instead of routine local technical and operational choices.** ([inference]; medium confidence; source: https://www.finops.org/framework/principles/; https://docs.cloud.google.com/architecture/devops; https://sre.google/sre-book/service-level-objectives/)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Delivery slows when prioritisation, spend approval, and exceptions sit outside the delivery team. | https://docs.cloud.google.com/architecture/devops; https://cisr.mit.edu/content/simplifying-decision-rights-growth; https://www.gov.uk/government/publications/state-of-digital-government-review/state-of-digital-government-review | medium | external queue, slow reprioritisation |
| [inference] Quality and risk control weaken when operators cannot fund reliability trade-offs directly. | https://sre.google/sre-book/embracing-risk/; https://sre.google/sre-book/service-level-objectives/; https://www.gov.uk/government/publications/state-of-digital-government-review/state-of-digital-government-review | medium | reliability, service levels, incident readiness |
| [inference] Total cost of ownership rises when engineering decisions and cost accountability are separated. | https://www.finops.org/framework/principles/; https://www.finops.org/framework/personas/; https://www.gov.uk/government/publications/state-of-digital-government-review/state-of-digital-government-review | medium | edge accountability, resource-funding gap |
| [inference] Milestone-based funding releases are one credible way to keep central investment control while allowing incremental delivery. | https://tmf.cio.gov/; https://tmf.cio.gov/board/; https://www.nao.org.uk/insights/six-reasons-why-digital-transformation-is-still-a-problem-for-government/ | medium | incremental release, monitored progress |
| [inference] Named integrator rights are the strongest substitute for full co-location. | https://ussm.gsa.gov/governance/; https://cisr.mit.edu/content/simplifying-decision-rights-growth; https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html | medium | escalation, accountable contact |
| [inference] Flexible contracts and combined build-run funding reduce downstream burden better than rigid project contracts. | https://www.nao.org.uk/insights/six-reasons-why-digital-transformation-is-still-a-problem-for-government/; https://www.gov.uk/government/publications/state-of-digital-government-review/state-of-digital-government-review | medium | flexible scope, operating funds |
| [inference] Over-governed split models drift into proxy compliance and coordination overhead. | https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html; https://davidamitchell.github.io/Research/research/2026-05-23-governance-failure-mechanisms-bureaucracy-circumvention.html; https://davidamitchell.github.io/Research/research/2026-05-19-how-do-formal-governance-structures-distort-cross-department-knowledge-flows.html | medium | control overload, distortion |
| [inference] Delegated delivery authority plus central guardrails is better supported than routine central re-approval. | https://www.finops.org/framework/principles/; https://docs.cloud.google.com/architecture/devops; https://sre.google/sre-book/service-level-objectives/ | medium | approval-by-exception, shared metrics |

### Assumptions

- **Assumption:** The delivery-capable party is also the party best placed to optimize a meaningful share of operating cost. **Justification:** Architecture, service-level, and reliability choices drive a large share of ongoing spend. [assumption; source: https://www.finops.org/framework/principles/; https://sre.google/sre-book/embracing-risk/]
- **Assumption:** Public-sector digital-governance evidence is structurally informative for enterprise delivery-governance design. **Justification:** The reviewed government sources explicitly document the same separation between budget holders, central controls, and accountable delivery teams that the present item studies. [assumption; source: https://www.gov.uk/government/publications/state-of-digital-government-review/state-of-digital-government-review; https://www.nao.org.uk/reports/digital-transformation-in-government-addressing-the-barriers/]
- **Assumption:** Ring-fenced delivery envelopes can exist inside centrally controlled funding structures. **Justification:** The reviewed funding and governance models show central investment control coexisting with delegated execution and milestone-based release. [assumption; source: https://tmf.cio.gov/; https://ussm.gsa.gov/governance/]

### Analysis

The evidence is strongest on decision-right placement rather than on abstract calls for collaboration, because the most concrete sources all specify who should decide routine change, cost, investment, and exception questions. [inference; source: https://cisr.mit.edu/content/classic-topics-decision-rights; https://cisr.mit.edu/content/simplifying-decision-rights-growth; https://docs.cloud.google.com/architecture/devops]

Speed, quality, risk, cost, and total cost of ownership are linked in this problem rather than separable, because the same misplaced authority determines whether those trade-offs are closed locally by the accountable team or escalated outward into queueing and delay. [inference; source: https://sre.google/sre-book/embracing-risk/; https://www.finops.org/framework/principles/; https://www.gov.uk/government/publications/state-of-digital-government-review/state-of-digital-government-review]

The most credible commercial compromise is staged delegation rather than full centralization or full decentralization, because central funders still need portfolio pacing and visible control while delivery-capable teams need enough budgetary and operational discretion to learn without re-opening the whole business case every time. [inference; source: https://tmf.cio.gov/; https://tmf.cio.gov/board/; https://ussm.gsa.gov/governance; https://www.nao.org.uk/insights/six-reasons-why-digital-transformation-is-still-a-problem-for-government/]

The adjacent repository items sharpen the boundary condition rather than changing the answer: explicit integrator rights can work, but only when they are backed by real authority, measurable service outcomes, and proportionate review instead of another committee layer. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-17-integrator-rights-vs-risk-cost-benefit-colocation-governance.html; https://davidamitchell.github.io/Research/research/2026-05-23-governance-controls-effectiveness-conditions.html]

### Risks, Gaps, and Uncertainties

- The public evidence base is stronger on mechanisms and operating-model patterns than on direct comparative studies that isolate this exact funding-versus-delivery split from all other organisational variables. [inference; source: https://cisr.mit.edu/content/classic-topics-decision-rights; https://docs.cloud.google.com/architecture/devops; https://www.finops.org/framework/principles/]
- Two seeded foundational sources, Jensen and Meckling's original article and the full Accelerate book text, were not directly accessible in this session, so their influence appears only through accessible official or repository-adjacent sources. [fact; source: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=94043; https://itrevolution.com/product/accelerate/]
- Government evidence is highly relevant to split authority, but some public-finance and legacy constraints may overstate how severe the same problem is in firms with simpler capital-allocation paths. [inference; source: https://www.nao.org.uk/insights/six-reasons-why-digital-transformation-is-still-a-problem-for-government/; https://www.gov.uk/government/publications/state-of-digital-government-review/state-of-digital-government-review]

### Open Questions

- How far can delegated budget envelopes be pushed in heavily regulated sectors before legal or prudential constraints require a different authority pattern?
- Which service-level metric bundle best predicts when approval-by-exception should tighten back into pre-execution review?
- What contractual clauses most effectively tie supplier incentives to long-run service reliability instead of short-run milestone completion?

---

## Output

- Type: knowledge
- Description: Evidence-backed synthesis of governance and commercial structures that preserve delivery outcomes when funding authority and delivery accountability are split, with a practical recommendation for delegated authority inside central guardrails. [inference; source: https://cisr.mit.edu/content/classic-topics-decision-rights; https://www.finops.org/framework/principles/; https://docs.cloud.google.com/architecture/devops]
- Links:
  - https://cisr.mit.edu/content/classic-topics-decision-rights
  - https://www.finops.org/framework/principles/
  - https://sre.google/sre-book/embracing-risk/
