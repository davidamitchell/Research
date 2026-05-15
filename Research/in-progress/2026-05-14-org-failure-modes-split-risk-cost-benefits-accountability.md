---
review_count: 1
title: "Organisational failure modes: risk, operational cost, and benefits accountability in separate business units"
added: 2026-05-14T18:48:56+00:00
status: reviewing
priority: high  # low | medium | high
blocks: []
tags: [organisation, organisational-design, governance, risk-management, financial-governance]
started: 2026-05-15T03:28:43+00:00
completed: ~
output: [knowledge]
cites: [2026-05-14-org-failure-modes-accountability-gaps, 2026-05-14-org-failure-modes-project-demand-product-it]
related: [2026-05-14-org-failure-modes-cohort-demand-domain-it, 2026-04-22-enterprise-ai-platform-operating-models]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Organisational failure modes: risk, operational cost, and benefits accountability in separate business units

## Research Question

What failure modes have been empirically observed in organisations where accountability for risk, operational cost, and benefits realisation are held in separate business units (BUs) rather than co-located in a single accountable party?

## Scope

**In scope:**
- Empirically documented failure modes arising when the business unit (BU) that owns risk (e.g., Risk, Compliance, Audit) is structurally separate from the BU that owns operational cost (e.g., IT Operations, Shared Services) and both are separate from the BU that claims benefits (e.g., Business Line, Product Owner)
- Observable symptoms: sub-optimisation, cost-shifting, risk acceptance without cost visibility, benefit claims without corresponding risk or cost ownership, governance deadlock, inability to make timely investment decisions
- Financial governance and organisational economics literature on split incentives and principal-agent problems
- Both private-sector and public-sector evidence

**Out of scope:**
- Failure modes in organisations where risk, cost, and benefits are deliberately co-located (these are the comparator, not the subject)
- Tax, regulatory, or legal structural requirements that mandate certain separations (unless they are directly linked to observed failure modes)
- Prescriptive org design solutions without empirical grounding

**Constraints:**
- Prefer empirical sources (case studies, audit findings, governance reviews, academic research) over consulting opinion
- Every source must include a verifiable URL
- Acronyms expanded on first use throughout

## Context

- A common enterprise and government pattern is to place risk oversight, operating-cost accountability, and benefits ownership in different functions, which turns one investment decision into several differently incentivised decisions. [inference; source: https://cisr.mit.edu/content/classic-topics-decision-rights; https://cisr.mit.edu/content/simplifying-decision-rights-growth; https://www.canada.ca/en/treasury-board-secretariat/corporate/reports/lessons-learned-transformation-pay-administration-initiative.html]

## Approach

1. Define the three accountability dimensions (risk, operational cost, benefits realisation) precisely and characterise what "separation" means in structural and governance terms.
2. Review principal-agent theory and organisational economics literature for foundational models of split-incentive failure.
3. Search for empirical evidence, case studies, audit reports, and governance research, of failure modes directly attributable to this separation.
4. Categorise the failure modes by type (decision quality, investment timing, cost management, risk tolerance, outcome realisation).
5. Examine whether failure severity varies by sector (financial services, government, healthcare, technology) or organisation size.
6. Review evidence on governance mechanisms (e.g., portfolio accountability boards, Profit and Loss (P&L) co-ownership, value stream funding) that have empirically reduced failure rates from this separation.

## Sources

- [ ] [Jensen and Meckling (1976) Theory of the Firm: Managerial Behavior, Agency Costs and Ownership Structure](https://www.sciencedirect.com/science/article/pii/0304405X7690026X) - seeded source checked; direct access remained blocked and no usable primary text was retrieved in this session.
- [ ] [Weill and Ross (2004) IT Governance: How Top Performers Manage IT Decision Rights for Superior Results](https://www.hbs.edu/faculty/Pages/item.aspx?num=20375) - seeded source checked; direct access remained blocked in this session.
- [ ] [Kaplan and Norton (1996) The Balanced Scorecard: Translating Strategy into Action](https://www.hbs.edu/faculty/Pages/item.aspx?num=9691) - seeded source checked; direct access remained blocked in this session.
- [x] [MIT Center for Information Systems Research (MIT CISR) (n.d.) Classic Topics: Decision Rights](https://cisr.mit.edu/content/classic-topics-decision-rights) - consulted for the governance definition tying decision rights to accountability and value from technology.
- [x] [MIT Center for Information Systems Research (MIT CISR) (2023) Simplifying decision rights for growth](https://cisr.mit.edu/content/simplifying-decision-rights-growth) - consulted for the specific decision categories that matter in digital transformation: what versus how, investment prioritisation, and exception handling.
- [x] [National Audit Office (2022) Government shared services](https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf) - consulted via Portable Document Format (PDF) extraction for evidence on fragmented governance, unclear benefits, weak risk ownership, and departmental buy-in problems.
- [x] [National Audit Office (2026) Update on government shared services](https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf) - consulted via PDF extraction for evidence on missing central ownership, unfunded local burdens, uneven functional readiness, and interdependency failures.
- [x] [National Audit Office (2011) The National Programme for information technology (IT) in the National Health Service: an update on the delivery of detailed care records systems](https://www.nao.org.uk/wp-content/uploads/2011/05/1012888.pdf) - consulted via PDF extraction for evidence on scope reduction without matched cost reduction, unknown benefit ownership, and uncertain financial liability at handover.
- [x] [Treasury Board of Canada Secretariat (2017) Lessons Learned from the Transformation of Pay Administration Initiative](https://www.canada.ca/en/treasury-board-secretariat/corporate/reports/lessons-learned-transformation-pay-administration-initiative.html) - consulted for the lessons that governance and oversight are foundational, that one office must hold accountability and authority, and that outcomes management must persist through the life of the initiative.
- [x] [Auditor General of Canada (2026) Modernizing the Pay System](https://www.canada.ca/content/dam/oag-bvg/audit-reports/documents/ag-202603-modernizing-pay-system.pdf) - consulted via PDF extraction for evidence on separated business ownership versus project ownership, shared accountability across departments, incomplete cost estimates, undefined savings measurement, and persistent backlog risk.
- [x] [Research item (2026) Organisational failure modes: overlapping and absent accountability at strategic and information technology (IT) layers](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-14-org-failure-modes-accountability-gaps.md) - consulted as adjacent repository evidence on missing decision-right owners and execution ambiguity.
- [x] [Research item (2026) Organisational failure modes: project-based demand with product-based information technology (IT) teams](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-14-org-failure-modes-project-demand-product-it.md) - consulted as adjacent repository evidence on matrix behaviour inside split governance structures.

---

## Research Skill Output

*(Full output from running the research skill - retained verbatim in the completed item. Sections 0-5 are the investigation; Section 6 seeds the Findings section below.)*

### §0 Initialise

Question: identify empirically observed failure modes when risk oversight, operational-cost accountability, and benefits-realisation accountability sit in separate business units instead of one accountable owner.

Scope: in scope are observable failure modes, sector variation, and evidence-backed mitigations from audit reports, governance research, and transformation reviews; out of scope are unsupported redesign blueprints and pure theory without empirical support.

Constraints: prefer accessible public sources with URLs, record failed primary-source checks explicitly, keep prior completed repository items as supporting synthesis rather than the sole basis for core claims, and use canonical tags only.

Output: knowledge, specifically a structured synthesis with executive summary, key findings, evidence map, assumptions, analysis, risks, gaps, uncertainties, and open questions.

Mode: full.

- [inference; source: https://cisr.mit.edu/content/classic-topics-decision-rights; https://cisr.mit.edu/content/simplifying-decision-rights-growth; https://www.canada.ca/en/treasury-board-secretariat/corporate/reports/lessons-learned-transformation-pay-administration-initiative.html] For this item, split accountability means one unit sets or audits risk tolerances, another absorbs or manages operating expenditure, and a third claims strategic or service benefits, so the same decision is experienced through different incentive systems.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-14-org-failure-modes-accountability-gaps.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-14-org-failure-modes-project-demand-product-it.md] Prior completed repository work already shows that missing owners and matrix-style demand allocation degrade delivery, so this item treats split risk-cost-benefit ownership as a more specific version of that wider accountability problem.

### §1 Question Decomposition

- **Root question:** what failure modes appear when risk, operating cost, and benefits ownership are structurally separated?
  - **A. Definitions**
    - A1. What counts as risk ownership in governance terms?
    - A2. What counts as operational-cost ownership?
    - A3. What counts as benefits-realisation ownership?
    - A4. What organisational condition marks these accountabilities as separated rather than co-located?
  - **B. Core failure mechanisms**
    - B1. What happens to decision rights when no single unit owns all three consequences?
    - B2. What happens to business cases and benefit tracking when benefits sit away from cost and risk owners?
    - B3. What happens to budgets when central sponsors and local operators bear different cost exposure?
    - B4. What happens to risk management when risk owners do not control budget or delivery levers?
  - **C. Observable failure modes**
    - C1. What deadlock or delay patterns recur?
    - C2. What cost-shifting or unfunded-burden patterns recur?
    - C3. What benefit-erosion or measurement failures recur?
    - C4. What liability, handover, or backlog failures recur?
  - **D. Variation**
    - D1. Do patterns differ by sector or function?
    - D2. Do patterns differ by maturity of shared standards or governance?
  - **E. Mitigations**
    - E1. Which remedies have direct empirical support?
    - E2. Which remedies remain inferential design guidance?

### §2 Investigation

#### 2.1 Source checks and definitional baseline

- Search note: seeded query `Jensen Meckling 1976 PDF agency costs ownership structure` returned ScienceDirect, SSRN, and OA.mg landing pages, but no accessible primary text was retrieved in this session.
- Search note: seeded query `Weill Ross 2004 IT Governance HBS` returned the Harvard Business School item page, but the page remained inaccessible in this session.
- Search note: seeded query `Kaplan Norton 1996 Balanced Scorecard HBS` returned the Harvard Business School item page, but the page remained inaccessible in this session.
- Search note: seeded URL `https://www.nao.org.uk/reports/managing-the-costs-of-it/` returned 404, so the investigation used accessible National Audit Office reports on shared services and programme governance instead.
- [fact; source: https://cisr.mit.edu/content/classic-topics-decision-rights] The MIT Center for Information Systems Research (MIT CISR) defines governance as a company’s allocation of decision rights and accountabilities, and states that clear specification of both is key to making progress on digital transformation.
- [fact; source: https://cisr.mit.edu/content/simplifying-decision-rights-growth] MIT CISR identifies a small set of transformation decisions that most matter: who decides what is done versus how, how investment is prioritised, and who handles exceptions.
- [fact; source: https://www.canada.ca/en/treasury-board-secretariat/corporate/reports/lessons-learned-transformation-pay-administration-initiative.html] The Canadian pay-transformation lessons identify governance and oversight as foundational and recommend assigning accountability and authority for a multi-department transformation to a single minister and deputy head, supported by an overall accountability framework.
- [inference; source: https://cisr.mit.edu/content/classic-topics-decision-rights; https://cisr.mit.edu/content/simplifying-decision-rights-growth; https://www.canada.ca/en/treasury-board-secretariat/corporate/reports/lessons-learned-transformation-pay-administration-initiative.html] Risk, operating cost, and benefits become dangerously separated when the unit that can veto or escalate risk, the unit that pays or absorbs recurring operating cost, and the unit that claims value are not the same decision owner or are not governed by one authoritative integration mechanism.

#### 2.2 Missing integrator and governance deadlock

- [fact; source: https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf] The National Audit Office reported in 2026 that there was no clear owner for government shared services with the levers to deliver the strategy.
- [fact; source: https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf] The same report concluded that there was no single owner in the centre of government with a clear mandate to secure departmental onboarding, leaving buy-in uncertain and timelines at risk.
- [fact; source: https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf] The 2022 National Audit Office report found fragmented and cumbersome governance arrangements that duplicated effort and produced disjointed decision-making across centre, cluster, and departmental layers.
- [fact; source: https://www.nao.org.uk/wp-content/uploads/2011/05/1012888.pdf] The 2011 National Audit Office report on the National Programme for information technology in the National Health Service recorded that, after governance changes, it was not yet known who would manage existing contracts, who would measure and report benefits, or how structural-change costs would be managed.
- [inference; source: https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf; https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf; https://www.nao.org.uk/wp-content/uploads/2011/05/1012888.pdf] When risk, cost, and benefits sit in separate units, the organisation repeatedly produces a missing-integrator failure mode: multiple forums can discuss trade-offs, but no single actor can close them decisively.

#### 2.3 Benefits opacity and weak investment cases

- [fact; source: https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf] The 2022 National Audit Office report states that the Cabinet Office used a case for change instead of a detailed business case, leaving costs, benefits, risks, alternative options, and safeguards under-specified.
- [fact; source: https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf] The same report says the central benefits database contained no figures or measured savings, only narrative descriptions of anticipated benefits.
- [fact; source: https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf] Departments told the National Audit Office that the Cabinet Office did not calculate expected programme benefits because it did not understand what benefits could be generated.
- [fact; source: https://www.nao.org.uk/wp-content/uploads/2011/05/1012888.pdf] The National Programme for information technology in the National Health Service reduced scope substantially, but the Department did not state what impact those reductions would have on expected benefits.
- [fact; source: https://www.canada.ca/content/dam/oag-bvg/audit-reports/documents/ag-202603-modernizing-pay-system.pdf] The Auditor General of Canada reported that the preliminary estimate for the new Dayforce pay system excluded important departmental transition costs and that Public Services and Procurement Canada was still determining how cost savings would be measured.
- [inference; source: https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf; https://www.nao.org.uk/wp-content/uploads/2011/05/1012888.pdf; https://www.canada.ca/content/dam/oag-bvg/audit-reports/documents/ag-202603-modernizing-pay-system.pdf] Separating benefits ownership from cost and risk ownership makes the business case fragile, because the unit claiming value can keep benefits qualitative while other units bear concrete delivery, transition, and compliance burdens.

#### 2.4 Cost shifting, unfunded burdens, and liability transfer

- [fact; source: https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf] In 2026, clusters told the National Audit Office that funding gaps still existed and might need to be covered from departmental budgets.
- [fact; source: https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf] The same report says current business case plans do not include all arm's-length bodies (ALBs), so departments and clusters must still plan for additional onboarding costs and resources.
- [fact; source: https://www.nao.org.uk/wp-content/uploads/2011/05/1012888.pdf] The National Programme for information technology in the National Health Service reported that local costs could increase because systems outside the programme would need to be made compatible with programme systems.
- [fact; source: https://www.nao.org.uk/wp-content/uploads/2011/05/1012888.pdf] The same report records considerable uncertainty about the financial liability of National Health Service organisations using programme systems and the cost and mechanism for transferring services to new suppliers.
- [fact; source: https://www.canada.ca/content/dam/oag-bvg/audit-reports/documents/ag-202603-modernizing-pay-system.pdf] The Auditor General of Canada found that the Dayforce cost estimate excluded important transition costs for departments and agencies, even though those units would need to onboard in waves.
- [inference; source: https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf; https://www.nao.org.uk/wp-content/uploads/2011/05/1012888.pdf; https://www.canada.ca/content/dam/oag-bvg/audit-reports/documents/ag-202603-modernizing-pay-system.pdf] A recurring split-accountability failure mode is cost externalisation: central sponsors keep the strategic case alive while operational units inherit unbudgeted onboarding, compatibility, or support costs.

#### 2.5 Risk ownership without delivery leverage

- [fact; source: https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf] The 2022 National Audit Office report found practical weaknesses in the central risk register, including risks with no owner, risks with no control activity or response, and risks that had not been properly assessed.
- [fact; source: https://www.canada.ca/content/dam/oag-bvg/audit-reports/documents/ag-202603-modernizing-pay-system.pdf] The Auditor General of Canada reports that departments, agencies, Public Services and Procurement Canada, and the Treasury Board of Canada Secretariat have shared accountability for paying employees accurately and on time.
- [fact; source: https://www.canada.ca/content/dam/oag-bvg/audit-reports/documents/ag-202603-modernizing-pay-system.pdf] The same audit distinguishes the Treasury Board of Canada Secretariat as business owner, responsible for business requirements and oversight, from Public Services and Procurement Canada as project sponsor and project owner, responsible for delivery and backlog management.
- [fact; source: https://www.canada.ca/content/dam/oag-bvg/audit-reports/documents/ag-202603-modernizing-pay-system.pdf] The audit also reports that backlog elimination remained limited and that unresolved simplification forced continuing customisation costs and manual workarounds.
- [inference; source: https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf; https://www.canada.ca/content/dam/oag-bvg/audit-reports/documents/ag-202603-modernizing-pay-system.pdf] Risk ownership separated from budget and operational control degrades into advisory oversight, because identified risks cannot be retired cleanly when the actor holding the risk view does not control the delivery and spending levers that would remove them.

#### 2.6 Sector and function variation

- [fact; source: https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf] The National Audit Office found that the Finance Function was the most advanced in standardisation and benefits tracking and was widely seen as the easiest function to prepare for transition.
- [fact; source: https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf] The same report found that the Human Resources (HR) Function lagged in all clusters except the already operational Overseas and Defence civilian capability, and that HR data and processes often were not compatible with functional standards.
- [fact; source: https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf] The report also notes that one co-sponsored Commercial Function decided not to implement the common standard, while HR participated in design but did not work toward implementation.
- [inference; source: https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf] Split accountability hurts more severely in multi-function programmes where one function can delay convergence without directly bearing the full system-wide opportunity cost of that delay.

#### 2.7 Mitigations and evidence quality

- [fact; source: https://www.canada.ca/en/treasury-board-secretariat/corporate/reports/lessons-learned-transformation-pay-administration-initiative.html] The Canadian pay-transformation lessons recommend assigning accountability and authority to a single office, establishing broad and inclusive governance, implementing explicit outcomes management, and funding affected stakeholders so they can support the initiative.
- [fact; source: https://cisr.mit.edu/content/classic-topics-decision-rights; https://cisr.mit.edu/content/simplifying-decision-rights-growth] MIT CISR presents clear decision rights, accountability frameworks, investment prioritisation clarity, and explicit exception handling as necessary governance conditions for realising value from digital investments.
- [fact; source: https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf] The 2026 National Audit Office report recommends clarifying governance responsibilities, agreeing onboarding plans with each cluster, and strengthening the Service and Technical Design Authority to deal with cross-cluster design and interdependency issues.
- [inference; source: https://www.canada.ca/en/treasury-board-secretariat/corporate/reports/lessons-learned-transformation-pay-administration-initiative.html; https://cisr.mit.edu/content/classic-topics-decision-rights; https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf] The strongest evidence-backed mitigation is not merely more oversight forums, but one accountable owner with authority over trade-offs among risk, operating cost, and benefits, supported by a documented cross-party accountability framework and shared cost-benefit data.

### §3 Reasoning

- [fact; source: https://cisr.mit.edu/content/classic-topics-decision-rights; https://cisr.mit.edu/content/simplifying-decision-rights-growth] The definitional evidence shows that governance quality depends on how decision rights, investment choices, and exception handling are allocated.
- [fact; source: https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf; https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf; https://www.nao.org.uk/wp-content/uploads/2011/05/1012888.pdf; https://www.canada.ca/content/dam/oag-bvg/audit-reports/documents/ag-202603-modernizing-pay-system.pdf] The empirical cases repeatedly show missing owners, unclear benefits, uncertain liabilities, duplicated governance, backlog persistence, and unfunded local costs.
- [inference; source: https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf; https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf; https://www.nao.org.uk/wp-content/uploads/2011/05/1012888.pdf; https://www.canada.ca/content/dam/oag-bvg/audit-reports/documents/ag-202603-modernizing-pay-system.pdf] The most defensible causal interpretation is that separating risk, cost, and benefit ownership creates an integration problem, because the recurring failures concern trade-offs across those dimensions rather than isolated technical defects.
- [assumption; source: https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf; https://www.canada.ca/en/treasury-board-secretariat/corporate/reports/lessons-learned-transformation-pay-administration-initiative.html] Large public-sector shared-service and payroll transformations are treated here as valid proxies for the organisational mechanism in private firms, because the incentive split between sponsor, operator, and beneficiary is structurally similar even when sector context differs.

### §4 Consistency Check

- [fact; source: https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf; https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf] The 2022 and 2026 National Audit Office reports are consistent on the key points that governance fragmentation, unclear benefits, and weak ownership remained central problems despite a refreshed delivery model.
- [fact; source: https://www.nao.org.uk/wp-content/uploads/2011/05/1012888.pdf; https://www.canada.ca/content/dam/oag-bvg/audit-reports/documents/ag-202603-modernizing-pay-system.pdf] The National Health Service and Canadian pay cases differ in programme design, but both report uncertainty over who owns benefits, who bears downstream costs, and how to retire operational risk.
- [inference; source: https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf; https://www.nao.org.uk/wp-content/uploads/2011/05/1012888.pdf; https://www.canada.ca/content/dam/oag-bvg/audit-reports/documents/ag-202603-modernizing-pay-system.pdf] No material contradiction appears in the evidence base; the main limitation is not disagreement about the mechanism but weaker direct private-sector audit evidence than public-sector evidence.

### §5 Depth and Breadth Expansion

- [inference; source: https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf; https://www.nao.org.uk/wp-content/uploads/2011/05/1012888.pdf] Technical lens: split accountability often manifests as interoperability work, local customisation, and handover uncertainty because technical architecture has to compensate for unresolved organisational seams.
- [inference; source: https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf; https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf; https://www.canada.ca/content/dam/oag-bvg/audit-reports/documents/ag-202603-modernizing-pay-system.pdf] Economic lens: central benefits narratives and local unfunded burdens create classic externalities, where the unit making the investment case does not fully bear the operating or transition cost.
- [inference; source: https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf; https://www.canada.ca/en/treasury-board-secretariat/corporate/reports/lessons-learned-transformation-pay-administration-initiative.html] Behavioural lens: when departments are asked to absorb onboarding work or local process change without a clear owner for the whole system, they delay commitment, protect local budgets, or only implement the minimum they must.
- [inference; source: https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf; https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf] Historical lens: repeated National Audit Office findings across 2022 and 2026 show that adding more forums without integrating accountability does not remove the failure class.

### §6 Synthesis

**Executive summary:**
- [inference; source: https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf; https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf; https://www.nao.org.uk/wp-content/uploads/2011/05/1012888.pdf] Organisations that separate risk oversight, operating-cost accountability, and benefits ownership across different business units reliably create a missing-integrator problem in which no single actor can make or enforce timely trade-offs across all three consequences.
- [inference; source: https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf; https://www.canada.ca/content/dam/oag-bvg/audit-reports/documents/ag-202603-modernizing-pay-system.pdf] The most recurrent observed symptoms are fragmented governance, weak or narrative-only benefit tracking, incomplete cost estimates, unfunded local burdens, and risk registers or backlogs that persist without decisive remediation.
- [inference; source: https://www.nao.org.uk/wp-content/uploads/2011/05/1012888.pdf; https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf] These failures become especially damaging during handover or multi-party operating models, where liabilities, interoperability costs, and benefit ownership are left unresolved at the point where responsibility shifts.
- [inference; source: https://www.canada.ca/en/treasury-board-secretariat/corporate/reports/lessons-learned-transformation-pay-administration-initiative.html; https://cisr.mit.edu/content/classic-topics-decision-rights; https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf] The strongest supported mitigation is one accountable owner with authority over risk, cost, and benefits trade-offs, backed by an explicit accountability framework and common cost-benefit data rather than by extra committees alone.

**Key findings:**
- [inference; medium confidence; source: https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf; https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf; https://www.nao.org.uk/wp-content/uploads/2011/05/1012888.pdf] Splitting risk, operating cost, and benefits across different units repeatedly removes the one actor who can close trade-offs, so programmes accumulate duplicated forums, delayed commitments, and reversible decisions rather than decisive governance.
- [inference; high confidence; source: https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf; https://www.nao.org.uk/wp-content/uploads/2011/05/1012888.pdf; https://www.canada.ca/content/dam/oag-bvg/audit-reports/documents/ag-202603-modernizing-pay-system.pdf] Benefit ownership separated from cost and delivery ownership produces weak business cases, because central sponsors leave benefits narrative or unmeasured while local operators face specific budget, transition, and service burdens.
- [inference; high confidence; source: https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf; https://www.nao.org.uk/wp-content/uploads/2011/05/1012888.pdf; https://www.canada.ca/content/dam/oag-bvg/audit-reports/documents/ag-202603-modernizing-pay-system.pdf] Split accountability makes cost shifting and liability transfer normal operating behaviour, with central programmes omitting local transition costs and local units inheriting onboarding, compatibility, or support obligations later.
- [inference; medium confidence; source: https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf; https://www.canada.ca/content/dam/oag-bvg/audit-reports/documents/ag-202603-modernizing-pay-system.pdf] Risk management weakens when the actor naming the risk does not control delivery and spend, which shows up as ownerless risk register items, persistent backlogs, continuing customisations, and slow corrective action.
- [inference; medium confidence; source: https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf] Severity rises in multi-function or multi-organisation settings where one function can opt out or lag on standards, because the full-system benefit depends on the slowest function even when other functions are ready.
- [inference; high confidence; source: https://www.nao.org.uk/wp-content/uploads/2011/05/1012888.pdf; https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf] Handover points are a distinctive failure surface under split accountability, because unresolved questions about benefits reporting, liability, technical standards, and service-transfer cost emerge exactly when operational responsibility changes hands.
- [inference; high confidence; source: https://www.canada.ca/en/treasury-board-secretariat/corporate/reports/lessons-learned-transformation-pay-administration-initiative.html; https://cisr.mit.edu/content/classic-topics-decision-rights; https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf] Evidence-backed mitigations converge on integrated decision rights, one accountable office, explicit outcomes management, and funded support for participating units, rather than on adding more oversight layers to the same fragmented structure.

**Evidence map:**
| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Splitting risk, operating cost, and benefits across different units removes the actor who can close trade-offs, creating duplicated forums and delayed commitments. | https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf; https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf; https://www.nao.org.uk/wp-content/uploads/2011/05/1012888.pdf | medium | Recurrent governance pattern across three public-sector cases. |
| [inference] Separating benefits ownership from cost and delivery ownership produces weak business cases and unmeasured benefits. | https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf; https://www.nao.org.uk/wp-content/uploads/2011/05/1012888.pdf; https://www.canada.ca/content/dam/oag-bvg/audit-reports/documents/ag-202603-modernizing-pay-system.pdf | high | All three sources report unclear, missing, or still-undecided benefit measurement. |
| [inference] Split accountability normalises cost shifting and late liability transfer to local operators. | https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf; https://www.nao.org.uk/wp-content/uploads/2011/05/1012888.pdf; https://www.canada.ca/content/dam/oag-bvg/audit-reports/documents/ag-202603-modernizing-pay-system.pdf | high | Local onboarding or transfer costs repeatedly excluded or deferred. |
| [inference] Risk management weakens when risk owners do not control delivery and spend. | https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf; https://www.canada.ca/content/dam/oag-bvg/audit-reports/documents/ag-202603-modernizing-pay-system.pdf | medium | Direct evidence on ownerless risks plus shared-accountability backlog persistence. |
| [inference] Severity rises when shared standards depend on multiple functions or organisations moving together. | https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf | medium | Strong within-source evidence, weaker cross-source replication. |
| [inference] Handover points expose unresolved benefit, liability, and service-transfer questions under split accountability. | https://www.nao.org.uk/wp-content/uploads/2011/05/1012888.pdf; https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf | high | Directly observed in National Health Service and shared-services cases. |
| [inference] The strongest supported mitigation is one accountable office with integrated decision rights, outcomes management, and support for participating units. | https://www.canada.ca/en/treasury-board-secretariat/corporate/reports/lessons-learned-transformation-pay-administration-initiative.html; https://cisr.mit.edu/content/classic-topics-decision-rights; https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf | high | Mitigation appears in governance research plus two audit-derived reform strands. |

**Assumptions:**
- [assumption; source: https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf; https://www.canada.ca/en/treasury-board-secretariat/corporate/reports/lessons-learned-transformation-pay-administration-initiative.html] Public-sector transformation cases are treated as valid mechanism evidence for private-sector organisations because the core split-incentive structure between sponsor, operator, and beneficiary is the same even when legal settings differ.
- [assumption; source: https://cisr.mit.edu/content/classic-topics-decision-rights; https://cisr.mit.edu/content/simplifying-decision-rights-growth] Operational-cost accountability is interpreted broadly enough to include local transition workload, customisation burden, and support liability, not just the headline central programme budget.

**Analysis:**
- [inference; source: https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf; https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf; https://www.canada.ca/content/dam/oag-bvg/audit-reports/documents/ag-202603-modernizing-pay-system.pdf] The evidence does not suggest that separated ownership is harmful merely because more parties are involved; it is harmful when no party has both the authority and incentive to optimise across risk, cost, and benefits together.
- [inference; source: https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf; https://www.nao.org.uk/wp-content/uploads/2011/05/1012888.pdf] The most decision-useful pattern is not isolated cost overrun or isolated delay, but the repeated combination of scope erosion, uncertain benefits, and unresolved liabilities after governance has already been fragmented.
- [inference; source: https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf; https://www.canada.ca/en/treasury-board-secretariat/corporate/reports/lessons-learned-transformation-pay-administration-initiative.html] A plausible rival explanation is simply that these programmes were large and technically difficult, but the evidence still points to governance structure as a central driver because the recommended fixes target ownership, authority, and outcomes management rather than only technical execution.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-14-org-failure-modes-accountability-gaps.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-14-org-failure-modes-project-demand-product-it.md] Adjacent completed repository items reinforce that these findings belong to the broader class of accountability-gap and matrix-behaviour failures, but this item adds the specific mechanism of cost-benefit-risk separation.

**Risks, gaps, uncertainties:**
- [fact; source: https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf; https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf] The empirical base is strongest in public-sector digital-transformation and shared-service programmes, so the item has better evidence for the mechanism than for exact cross-sector prevalence.
- [fact; source: https://cisr.mit.edu/content/classic-topics-decision-rights; https://cisr.mit.edu/content/simplifying-decision-rights-growth] The accessible governance research is rich on decision-right principles but thinner on openly published, named private-sector failure case studies that separate risk, cost, and benefits in exactly the way asked here.
- [fact; source: https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf; https://www.canada.ca/content/dam/oag-bvg/audit-reports/documents/ag-202603-modernizing-pay-system.pdf] Some recent cases remain in flight, so final realised costs and benefits are still moving targets.
- [fact; source: https://cisr.mit.edu/content/classic-topics-decision-rights; https://cisr.mit.edu/content/simplifying-decision-rights-growth] The conceptual strand relies on accessible MIT CISR governance material and audit reports because openly accessible primary texts for the seeded Jensen and Meckling, Weill and Ross, and Kaplan and Norton sources were not part of this evidence base.

**Open questions:**
- [inference; source: https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf; https://www.canada.ca/en/treasury-board-secretariat/corporate/reports/lessons-learned-transformation-pay-administration-initiative.html] Which quantitative governance indicators best predict that split accountability is becoming harmful before cost and benefit failures are visible?
- [inference; source: https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf; https://cisr.mit.edu/content/classic-topics-decision-rights] Under what conditions can a formal accountability framework substitute for full co-location of risk, cost, and benefits ownership without recreating the same integration problem?
### §7 Recursive Review

- status: pass
- acronym-first-use: checked
- claim-labels: checked
- findings-parity: checked
- cross-item-links: checked

---

## Findings

### Executive Summary

Organisations that separate risk oversight, operating-cost accountability, and benefits ownership across different business units consistently create a missing-integrator problem in which no single actor can make timely trade-offs across all three consequences. [inference; source: https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf; https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf; https://www.nao.org.uk/wp-content/uploads/2011/05/1012888.pdf]

The most recurrent observed symptoms are fragmented governance, weak or narrative-only benefit tracking, incomplete cost estimates, unfunded local burdens, and risk items or backlogs that persist without decisive remediation. [inference; source: https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf; https://www.canada.ca/content/dam/oag-bvg/audit-reports/documents/ag-202603-modernizing-pay-system.pdf]

These failures become especially damaging during handover or multi-party operating models, where liabilities, interoperability costs, and benefit ownership are still unresolved when responsibility shifts from central programme teams to operating units. [inference; source: https://www.nao.org.uk/wp-content/uploads/2011/05/1012888.pdf; https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf]

The strongest supported mitigation is one accountable owner with authority over risk, cost, and benefits trade-offs, backed by an explicit accountability framework and common cost-benefit data rather than by additional committees alone. [inference; source: https://www.canada.ca/en/treasury-board-secretariat/corporate/reports/lessons-learned-transformation-pay-administration-initiative.html; https://cisr.mit.edu/content/classic-topics-decision-rights; https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf]

### Key Findings

1. **When risk, operating cost, and benefits are owned by different units, programmes repeatedly lose the one actor who can close trade-offs, so governance expands into duplicated boards, delayed commitments, and reversible decisions rather than decisive action.** ([inference]; medium confidence; source: https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf; https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf; https://www.nao.org.uk/wp-content/uploads/2011/05/1012888.pdf)
2. **Benefit ownership separated from cost and delivery ownership produces weak investment cases, because central sponsors keep benefits qualitative or unmeasured while local operators face specific budget, transition, and service burdens that are easier to see and harder to ignore.** ([inference]; high confidence; source: https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf; https://www.nao.org.uk/wp-content/uploads/2011/05/1012888.pdf; https://www.canada.ca/content/dam/oag-bvg/audit-reports/documents/ag-202603-modernizing-pay-system.pdf)
3. **Split accountability makes cost shifting and liability transfer normal operating behaviour, with central programmes omitting local transition costs and local units later inheriting onboarding, compatibility, support, or transfer obligations they did not fully price into the original decision.** ([inference]; high confidence; source: https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf; https://www.nao.org.uk/wp-content/uploads/2011/05/1012888.pdf; https://www.canada.ca/content/dam/oag-bvg/audit-reports/documents/ag-202603-modernizing-pay-system.pdf)
4. **Risk management weakens when the actor naming the risk does not control delivery and spend, which shows up empirically as ownerless risk-register items, persistent backlogs, continuing customisations, and slow corrective action even after the problem is well understood.** ([inference]; medium confidence; source: https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf; https://www.canada.ca/content/dam/oag-bvg/audit-reports/documents/ag-202603-modernizing-pay-system.pdf)
5. **Severity rises in multi-function or multi-organisation settings where one function can lag or opt out of standards, because the full-system benefit depends on the slowest function even when finance, technology, or another domain is already prepared to move.** ([inference]; medium confidence; source: https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf)
6. **Handover points are a distinctive failure surface under split accountability, because unresolved questions about benefits reporting, financial liability, technical standards, and service-transfer cost emerge exactly when operational responsibility changes hands.** ([inference]; high confidence; source: https://www.nao.org.uk/wp-content/uploads/2011/05/1012888.pdf; https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf)
7. **The best-supported mitigations converge on integrated decision rights, one accountable office, explicit outcomes management, and funded support for participating units, rather than on adding more oversight layers to the same fragmented structure.** ([inference]; high confidence; source: https://www.canada.ca/en/treasury-board-secretariat/corporate/reports/lessons-learned-transformation-pay-administration-initiative.html; https://cisr.mit.edu/content/classic-topics-decision-rights; https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Splitting risk, operating cost, and benefits across different units removes the actor who can close trade-offs, creating duplicated forums and delayed commitments. | https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf; https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf; https://www.nao.org.uk/wp-content/uploads/2011/05/1012888.pdf | medium | Recurrent governance pattern across three public-sector cases. |
| [inference] Separating benefits ownership from cost and delivery ownership produces weak business cases and unmeasured benefits. | https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf; https://www.nao.org.uk/wp-content/uploads/2011/05/1012888.pdf; https://www.canada.ca/content/dam/oag-bvg/audit-reports/documents/ag-202603-modernizing-pay-system.pdf | high | All three sources report unclear, missing, or still-undecided benefit measurement. |
| [inference] Split accountability normalises cost shifting and late liability transfer to local operators. | https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf; https://www.nao.org.uk/wp-content/uploads/2011/05/1012888.pdf; https://www.canada.ca/content/dam/oag-bvg/audit-reports/documents/ag-202603-modernizing-pay-system.pdf | high | Local onboarding or transfer costs repeatedly excluded or deferred. |
| [inference] Risk management weakens when risk owners do not control delivery and spend. | https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf; https://www.canada.ca/content/dam/oag-bvg/audit-reports/documents/ag-202603-modernizing-pay-system.pdf | medium | Direct evidence on ownerless risks plus shared-accountability backlog persistence. |
| [inference] Severity rises when shared standards depend on multiple functions or organisations moving together. | https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf | medium | Strong within-source evidence, weaker cross-source replication. |
| [inference] Handover points expose unresolved benefit, liability, and service-transfer questions under split accountability. | https://www.nao.org.uk/wp-content/uploads/2011/05/1012888.pdf; https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf | high | Directly observed in National Health Service and shared-services cases. |
| [inference] The strongest supported mitigation is one accountable office with integrated decision rights, outcomes management, and support for participating units. | https://www.canada.ca/en/treasury-board-secretariat/corporate/reports/lessons-learned-transformation-pay-administration-initiative.html; https://cisr.mit.edu/content/classic-topics-decision-rights; https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf | high | Mitigation appears in governance research plus two audit-derived reform strands. |

### Assumptions

- Public-sector transformation cases are treated as valid mechanism evidence for private-sector organisations because the split between sponsor, operator, and beneficiary incentives is structurally similar. [assumption; source: https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf; https://www.canada.ca/en/treasury-board-secretariat/corporate/reports/lessons-learned-transformation-pay-administration-initiative.html]
- Operational-cost accountability is interpreted broadly enough to include local transition workload, customisation burden, and support liability, not just the headline central budget. [assumption; source: https://cisr.mit.edu/content/classic-topics-decision-rights; https://cisr.mit.edu/content/simplifying-decision-rights-growth]

### Analysis

The evidence does not suggest that separated ownership is harmful merely because more parties are involved; it is harmful when no party has both the authority and incentive to optimise across risk, cost, and benefits together. [inference; source: https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf; https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf; https://www.canada.ca/content/dam/oag-bvg/audit-reports/documents/ag-202603-modernizing-pay-system.pdf]

The most decision-useful pattern is not isolated cost overrun or isolated delay, but the repeated combination of scope erosion, uncertain benefits, and unresolved liabilities after governance has already been fragmented. [inference; source: https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf; https://www.nao.org.uk/wp-content/uploads/2011/05/1012888.pdf]

A plausible rival explanation is simply that these programmes were large and technically difficult, but the evidence still points to governance structure as a central driver because the recommended fixes target ownership, authority, and outcomes management rather than only technical execution. [inference; source: https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf; https://www.canada.ca/en/treasury-board-secretariat/corporate/reports/lessons-learned-transformation-pay-administration-initiative.html]

Adjacent completed repository items on accountability gaps and project-demand mismatch reinforce that this item belongs to a broader class of matrix-style governance failures, but the new contribution here is the specific mechanism by which separated risk, cost, and benefits ownership produce those failures. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-14-org-failure-modes-accountability-gaps.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-14-org-failure-modes-project-demand-product-it.md]

### Risks, Gaps, and Uncertainties

- The empirical base is strongest in public-sector digital-transformation and shared-service programmes, so the item has better evidence for the mechanism than for exact cross-sector prevalence. [fact; source: https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf; https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf]
- The accessible governance research is rich on decision-right principles but thinner on openly published, named private-sector failure case studies that separate risk, cost, and benefits in exactly the way asked here. [fact; source: https://cisr.mit.edu/content/classic-topics-decision-rights; https://cisr.mit.edu/content/simplifying-decision-rights-growth]
- Some recent cases remain in flight, so final realised costs and benefits are still moving targets. [fact; source: https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf; https://www.canada.ca/content/dam/oag-bvg/audit-reports/documents/ag-202603-modernizing-pay-system.pdf]
- The conceptual strand relies on accessible MIT Center for Information Systems Research (MIT CISR) governance material and audit reports because openly accessible primary texts for the seeded Jensen and Meckling, Weill and Ross, and Kaplan and Norton sources were not part of this evidence base. [fact; source: https://cisr.mit.edu/content/classic-topics-decision-rights; https://cisr.mit.edu/content/simplifying-decision-rights-growth]

### Open Questions

- Which quantitative governance indicators best predict that split accountability is becoming harmful before cost and benefit failures are visible? [inference; source: https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf; https://www.canada.ca/en/treasury-board-secretariat/corporate/reports/lessons-learned-transformation-pay-administration-initiative.html]
- Under what conditions can a formal accountability framework substitute for full co-location of risk, cost, and benefits ownership without recreating the same integration problem? [inference; source: https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf; https://cisr.mit.edu/content/classic-topics-decision-rights]

---

## Output

- Type: knowledge
- Description: Structured synthesis of empirically observed failure modes that arise when risk, operating cost, and benefits accountability are split across business units, together with the most strongly supported governance mitigations. [inference; source: https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf; https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf; https://www.canada.ca/en/treasury-board-secretariat/corporate/reports/lessons-learned-transformation-pay-administration-initiative.html]
- Links:
  - https://www.nao.org.uk/wp-content/uploads/2026/03/update-on-government-shared-services.pdf
  - https://www.nao.org.uk/wp-content/uploads/2022/11/government-shared-services.pdf
  - https://www.canada.ca/en/treasury-board-secretariat/corporate/reports/lessons-learned-transformation-pay-administration-initiative.html
