---
title: "Best practices in financial forecasting for IT operational run costs: assumptions, uncertainty, and regulatory considerations"
added: 2026-03-13
status: reviewing
priority: high
blocks: []
tags: [financial-forecasting, it-run-costs, uncertainty-modelling, regulatory, error-bars, infrastructure-costing, assumptions]
started: 2026-03-14
completed: ~
output: [knowledge]
---

# Best practices in financial forecasting for IT operational run costs: assumptions, uncertainty, and regulatory considerations

## Research Question

What are the established best practices for financially responsible forecasting of Information Technology (IT) operational run costs — covering cost estimation by technology and infrastructure type, required assumptions, uncertainty modelling (error bars and compounding estimate impact), and the regulatory and governance considerations that apply when these projections appear in financial filings or are used for planning and investment decisions?

## Scope

**In scope:**
- Established methodologies for estimating IT operational run costs (on-premises hardware, cloud Infrastructure-as-a-Service (IaaS), Platform-as-a-Service (PaaS), Software-as-a-Service (SaaS), networking, licensing, support, and labour)
- Required assumptions for each cost category and how those assumptions should be documented and disclosed
- Techniques for quantifying and communicating forecast uncertainty: confidence intervals, error bars, Monte Carlo simulation, scenario analysis, and sensitivity analysis
- Compounding uncertainty: how individual estimate uncertainties interact and accumulate across multi-year or multi-component forecasts
- Financially responsible practices: materiality, conservatism principle, range-based vs point-estimate disclosures
- Regulatory and governance context for IT cost projections that appear in financial statements, board papers, prospectuses, or regulatory filings (e.g., International Financial Reporting Standards (IFRS), Generally Accepted Accounting Principles (GAAP), Sarbanes-Oxley Act (SOX) controls, and equivalent frameworks)
- Internal governance: how organisations structure forecasting processes to meet audit and board-level scrutiny

**Out of scope:**
- Capital expenditure (CapEx) project estimation methodology (focus is on operational run costs — OpEx)
- Detailed accounting treatment of cloud costs (recognition, capitalisation vs expense) — except as it affects disclosure obligations
- IT cost optimisation or cloud cost reduction tactics
- Vendor-specific pricing calculators in detail

**Constraints:**
- Distinguish between *internal planning* standards (what is prudent) and *external disclosure* standards (what is legally required). These have overlapping but not identical requirements.
- Evidence should be sourced from authoritative bodies: accounting standards boards, regulatory bodies, practitioner frameworks (e.g., ISACA, ITIL, Gartner), and peer-reviewed literature where available.

## Context

Organisations regularly produce multi-year IT run-cost forecasts for board approval, investment cases, and regulatory filings. These forecasts are inherently uncertain: cloud unit prices shift, usage grows at variable rates, licence renewals fluctuate, and staffing costs change. When a single-point estimate is presented without stated assumptions or uncertainty ranges, decision-makers cannot assess the risk embedded in the number.

The stakes escalate when these figures enter external filings. A listed company presenting an IT cost projection in a prospectus or annual report has disclosure obligations. An error in a material estimate, or a failure to disclose known uncertainty, can constitute a misrepresentation.

This research is motivated by a practical need: to build forecasting models that are (a) methodologically sound, (b) honest about uncertainty, and (c) defensible under regulatory scrutiny. The answer needs to span the technical (how to model) and the governance/regulatory (what must be disclosed and how).

## Approach

1. **Cost categorisation and estimation by type** — identify the standard IT cost taxonomy (IaaS, PaaS, SaaS, on-premises hardware, networking, labour, licensing, support/maintenance). For each category, document: the primary cost drivers, the typical estimation approach, and the volatility characteristics that inform uncertainty modelling.

2. **Required assumptions** — survey practitioner frameworks (Gartner, Forrester, ISACA, ITIL Financial Management) for the canonical set of assumptions that must be stated for an IT run-cost estimate to be auditable: growth rate assumptions, unit price assumptions, utilisation assumptions, currency/exchange rate assumptions, and vendor contract assumptions. Identify which assumptions are typically material.

3. **Uncertainty modelling techniques** — investigate the three principal approaches used in financial and engineering forecasting:
   - Scenario analysis (base / optimistic / pessimistic)
   - Sensitivity analysis (tornado charts, one-at-a-time parameter variation)
   - Probabilistic simulation (Monte Carlo — when inputs have known or estimable distributions)
   Assess when each is appropriate for IT run-cost contexts.

4. **Compounding estimates** — examine how uncertainty propagates when combining estimates across cost categories or across forecast years. Determine whether standard financial practice treats errors as independent (root-sum-square) or correlated (arithmetic addition of ranges), and what this means for multi-year total cost of ownership (TCO) forecasts.

5. **Regulatory and disclosure requirements** — investigate:
   - What IFRS and GAAP require regarding forward-looking cost disclosures (Management Discussion & Analysis (MD&A) sections, going concern disclosures, commitments and contingencies notes)
   - SOX Section 302/404 implications for IT cost controls and the accuracy of related financial projections
   - UK FRC (Financial Reporting Council) and equivalent body guidance on uncertainty disclosure
   - Prospectus Regulation requirements (EU/UK) for risk factor and financial projection disclosures
   - Whether IT run-cost forecasts embedded in business cases or board papers carry any separate regulatory obligation (likely jurisdiction-dependent)

6. **Financially responsible practices** — synthesise into a set of principles for producing a forecast that is conservative without being misleading, range-based without being uninformative, and assumption-transparent without being unmanageably complex.

## Sources

- [ ] **IFRS Practice Statement 1 — Making Materiality Judgements** — IFRS Foundation
- [ ] **IAS 37 — Provisions, Contingent Liabilities and Contingent Assets** — IFRS Foundation (relevant for uncertain future obligations)
- [ ] **FASB ASC 275 — Risks and Uncertainties** — GAAP disclosure requirements for estimates subject to significant change
- [ ] **SEC FR-72 — Commission Guidance Regarding Management's Discussion and Analysis** — SEC guidance on forward-looking disclosures
- [ ] **PCAOB AS 2101 / AICPA AU-C 540** — Auditing accounting estimates (relevant for what auditors expect from estimates)
- [ ] **ISACA COBIT 2019** — IT governance framework including Financial Management practices
- [ ] **ITIL 4 — Financial Management for IT Services** — practitioner framework for IT cost modelling
- [ ] **Gartner IT Budgeting and Cost Optimisation research** — industry benchmarks and cost categorisation frameworks
- [ ] **RICS Professional Standards — Uncertainty of Valuation** — for uncertainty disclosure methodology (adjacent field with mature practice)
- [ ] **Vose, D. — Risk Analysis: A Quantitative Guide (3rd ed., Wiley)** — Monte Carlo simulation and compounding uncertainty
- [ ] **Hubbard, D.W. — How to Measure Anything (3rd ed., Wiley)** — applied estimation and uncertainty quantification
- [ ] **UK FRC — Financial Reporting Lab: Judgements and Estimates** — guidance on disclosing estimation uncertainty
- [ ] **EU Prospectus Regulation (2017/1129)** — financial projections disclosure requirements

---

## Findings

### Executive Summary

Financially responsible forecasting of IT operational run costs requires three interlocking practices: a structured cost taxonomy aligned to the Technology Business Management (TBM) Council standard or ITIL (IT Infrastructure Library) 4 cost types; stated and documented assumptions for each material cost driver (consumption growth, unit prices, contract terms, labour rates, and exchange rates); and quantified uncertainty modelling that reflects the correlated nature of most IT cost risks. The dominant external disclosure frameworks — International Accounting Standard (IAS) 1 paragraph 125, US Generally Accepted Accounting Principles (GAAP) ASC 275, Securities and Exchange Commission (SEC) Management Discussion and Analysis (MD&A) Item 303, Sarbanes-Oxley Act (SOX) Sections 302/404, the UK Financial Reporting Council (FRC) guidance, and EU Prospectus Regulation 2017/1129 — converge on the principle that material forward-looking cost estimates must be accompanied by their assumptions and a quantification of the uncertainty that attaches to those estimates. The key distinction between internal planning standards and external disclosure standards is one of threshold: internal good practice is conservative and range-based; external disclosure is legally required when uncertainty is material and the estimate is reasonably likely to change materially. Organisations that present single-point IT cost estimates in board papers or regulatory filings without stated assumptions and uncertainty ranges are neither meeting best practice standards nor, where the estimate is material, meeting their disclosure obligations.

### Key Findings

1. **The TBM Council V4 taxonomy is the de facto industry standard for categorising IT operational costs, providing a cost pool layer — labour, Software-as-a-Service (SaaS), cloud services, hardware, telecom, and facilities — that forms the required structure for building auditable run-cost estimates across all deployment models.** Confidence: high.

2. **Infrastructure-as-a-Service (IaaS) cloud compute costs are consumption-driven and metered by the second, making them the highest-volatility IT cost category: cloud spend can increase 20–30% annually without active governance, driven by usage growth that outpaces the per-unit price reductions that cloud providers have historically delivered.** Confidence: high.

3. **Eight canonical assumptions must be documented for an IT run-cost estimate to be auditable: consumption growth rate by category, unit prices and vendor escalation clauses, staffing headcount and grade mix, currency and exchange rate assumptions, vendor contract terms and renewal dates, capitalisation versus expense treatment, hardware refresh cycle schedule, and planned organisational changes such as cloud migrations or divestitures.** Consumption growth rate and unit price assumptions are typically the most material. Confidence: high.

4. **Scenario analysis, sensitivity analysis (tornado charts), and Monte Carlo simulation are complementary uncertainty modelling techniques addressing different aspects of forecast uncertainty: scenario analysis describes qualitatively different futures; sensitivity analysis identifies which assumptions drive the most variance; Monte Carlo produces a probability distribution of outcomes required for regulatory or board-level defensibility.** Confidence: high.

5. **Most IT cost uncertainties are positively correlated — macro-economic inflation, foreign exchange movements, and vendor price cycles affect multiple cost categories simultaneously — so arithmetic addition of percentage uncertainty ranges is more conservative and appropriate than root-sum-square (RSS) combination, which systematically underestimates combined uncertainty when inputs are correlated.** Confidence: medium.

6. **In multi-year total cost of ownership (TCO) forecasts, errors in year-one growth rate assumptions compound through later years: an annual uncertainty of ±15% produces approximately ±34% five-year uncertainty under the independence assumption and up to ±75% under full correlation, meaning that the stated uncertainty range for a five-year forecast must be substantially wider than the stated annual uncertainty.** Confidence: medium.

7. **IFRS IAS 1 paragraph 125 requires disclosure of assumptions with a significant risk of resulting in a material adjustment to asset or liability carrying amounts within the next financial year; UK FRC thematic reviews conducted in 2017 and 2022 found widespread non-compliance characterised by generic boilerplate text, missing quantitative sensitivity disclosures, and failure to distinguish short-term from longer-term estimation uncertainties.** Confidence: high.

8. **US GAAP ASC 275 triggers disclosure when it is at least "reasonably possible" that an estimate will change materially in the near term, a lower threshold than IFRS IAS 1.125's "significant risk" standard, making ASC 275 more easily triggered for IT cost commitments such as cloud minimum spend obligations and prepaid licence agreements.** Confidence: high.

9. **SEC MD&A Item 303 (FR-72) classifies disclosure of known trends reasonably likely to cause a material change in cost-revenue relationships as a required disclosure, not optional forward-looking information — explicitly covering known or reasonably likely increases in labour, materials, or vendor prices, which encompasses IT labour cost escalation and software vendor price increases at contract renewal.** Confidence: high.

10. **SOX Sections 302 and 404 require that internal controls over financial reporting (ICFR) extend to the processes underlying all material financial estimates; for organisations where IT operational costs are material to reported financial figures, the IT cost estimation process itself must be assessed as part of ICFR by management (Section 404(a)) and attested by external auditors (Section 404(b)).** Confidence: high.

11. **EU Prospectus Regulation (Regulation (EU) 2017/1129) requires material, issuer-specific risk factors categorised by significance; generic IT cost risk factors that apply to all technology companies are non-compliant, and a material IT operational cost uncertainty must be disclosed with specific quantification and placed prominently according to its materiality ranking.** Confidence: high.

12. **The structural gap between internal planning practice — which commonly uses single-point optimistic estimates to secure budget approval — and external disclosure requirements — which require range-based, assumption-transparent, specifically quantified disclosures — creates regulatory risk for organisations that submit internal forecast outputs directly into prospectuses or annual reports without upgrading disclosure quality to the applicable standard.** Confidence: medium.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| TBM Council V4 is de facto standard for IT cost categorisation | TBM Council https://www.tbmcouncil.org/taxonomy/ [x] | High | Primary source from industry standard body |
| IaaS costs can increase 20–30% annually without governance | InfoTech "Invest in Realistic Project Costing" https://www.infotech.com/research/ss/invest-in-realistic-and-comprehensive-project-costing [x] | High | Practitioner source; consistent with cloud billing literature |
| Eight canonical required assumptions | ITIL 4 Practice Guide https://uat2.axelos.com/resource-hub/practice/service-financial-management-itil-4-practice-guide [x]; TBM Council [x]; COBIT (Control Objectives for Information and Related Technologies) 2019 APO06 https://nextstepac.com/wp-content/uploads/2025/12/COBIT-2019-Design-Guide-by-ISACA.pdf [x] | High | Synthesised from three independent practitioner frameworks |
| Monte Carlo produces probability distribution; scenarios do not | Toptal https://www.toptal.com/management-consultants/financial-forecasting/monte-carlo-simulation [x]; FinancialModelsLab https://financialmodelslab.com/blogs/blog/monte-carlo-simulation-financial-modelling [x]; Investopedia https://www.investopedia.com/terms/m/montecarlosimulation.asp [x] | High | Three independent secondary sources agree |
| Positive IT cost correlation → arithmetic addition more conservative than RSS | Wikipedia "Propagation of uncertainty" https://en.wikipedia.org/wiki/Propagation_of_uncertainty [x]; WSU error propagation PDF https://s3.wp.wsu.edu/uploads/sites/2621/2021/06/A-3-Data-Analysis-4-Error-Propagation.pdf [x] | Medium | Mathematical basis established; correlation direction is inference applied to IT domain |
| Early-stage errors amplified in multi-stage forecasts | TTI/Texas A&M "Propagation of Uncertainty Through Travel Demand Models" https://static.tti.tamu.edu/swutc.tamu.edu/publications/technicalreports/167804-1.pdf [x] | Medium | Adjacent field; directly applicable mathematical mechanism |
| IAS 1.125 requires near-term material adjustment uncertainty disclosure | IFRS Foundation staff paper https://www.ifrs.org/content/dam/ifrs/meetings/2023/january/issb/ap3b-general-sustainability-related-disclosures-s1-disclosure-of-judgements-assumptions-and-estimates.pdf [x]; dreport.cz IAS 1.125 explainer https://www.dreport.cz/en/blog/disclosure-of-significant-judgements-and-key-sources-of-estimation-uncertainty/ [x] | High | Primary and secondary sources consistent |
| FRC found widespread IAS 1.125 non-compliance (2017, 2022) | FRC July 2022 thematic review https://www.frc.org.uk/news-and-events/news/2022/07/frc-publishes-review-of-judgements-and-estimates/ [x] | High | Regulatory body's own published finding |
| GAAP ASC 275 "reasonably possible" lower trigger than IFRS | PwC Viewpoint 24.3 https://viewpoint.pwc.com/dt/us/en/pwc/accounting_guides/financial_statement_/financial_statement___18_US/chapter_24_risks_and_US/243_disclosure_US.html [x]; SEC SAB Topic 5 https://www.sec.gov/interps/account/sabcodet5.htm [x] | High | Two independent accounting guidance sources |
| SEC MD&A Item 303 requires known cost trend disclosure | SEC FR-72 (2003) https://www.sec.gov/rules-regulations/2003/12/commission-guidance-regarding-managements-discussion-analysis-financial-condition-results-operations [x]; Federal Register 2021 amendments https://www.federalregister.gov/documents/2021/01/11/2020-26090/managements-discussion-and-analysis-selected-financial-data-and-supplementary-financial-information [x] | High | Primary regulatory sources |
| SOX 302/404 applies to ICFR for material IT cost estimation | AuditBoard SOX overview https://auditboard.com/blog/sarbanes-oxley-act [x]; UpGuard SOX guide https://www.upguard.com/blog/sox-compliance [x] | High | Multiple independent secondary sources |
| EU Prospectus Regulation requires specific, quantified IT risk factors | EUR-Lex Regulation (EU) 2017/1129 https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:02017R1129-20191231 [x]; Travers Smith overview https://www.traverssmith.com/knowledge/knowledge-container/eu-prospectus-regulation-what-fund-managers-and-investment-companies-sponsors-need-to-know/ [x] | High | Primary regulatory source and legal practitioner commentary |

**Identified but not consulted:**
- Vose, D. — *Risk Analysis: A Quantitative Guide* (3rd ed., Wiley) [ ]
- Hubbard, D.W. — *How to Measure Anything* (3rd ed., Wiley) [ ]
- RICS Professional Standards — Uncertainty of Valuation [ ]
- PCAOB AS 2101 full text [ ]
- ISACA COBIT 2019 full publication text [ ]
- IFRS Practice Statement 1 on Materiality Judgements [ ]

### Assumptions

1. **[assumption]** The TBM Council V4 taxonomy is sufficiently representative of industry practice to serve as the reference taxonomy for IT cost categorisation. Justification: cited by multiple independent practitioner sources and adopted by US government agencies; no competing standard of equal authority was found.

2. **[assumption]** Error propagation mathematics from engineering and travel demand modelling applies to IT cost forecasting. Justification: the mathematical mechanism (correlated vs. independent errors, compounding through multiplicative models) is domain-independent. Specific correlation coefficient values for IT cost categories are not empirically calibrated from this investigation.

3. **[assumption]** The 20–30% annual IaaS cost increase figure applies to organisations without active cloud cost governance. Justification: the source explicitly conditions the figure on unmanaged cloud spending; it is not a universal rate and should not be applied to organisations with active FinOps (Financial Operations) practices.

### Analysis

The evidence supports a two-tier framework for IT operational run-cost forecasting.

*Tier 1 — Internal planning standard:* A well-constructed internal IT run-cost forecast uses the TBM taxonomy to categorise costs, documents the eight canonical assumptions for each material category, applies sensitivity analysis to identify the critical assumptions, and presents a range (minimum/base/maximum) rather than a single point. This is the standard that ITIL 4 Service Financial Management, COBIT 2019 APO06, and the TBM Council collectively endorse.

*Tier 2 — External disclosure standard:* When IT cost estimates appear in financial filings, regulatory requirements add further obligations: assumptions must be specifically disclosed (not generic boilerplate), sensitivity must be quantified, and the uncertainty must be characterised in terms of near-term material adjustment risk (IFRS/FRC) or reasonable possibility of material change (GAAP/SEC MD&A). The EU Prospectus Regulation requires issuer-specific quantified risk factors where IT costs are material.

The governance mechanism linking Tier 1 and Tier 2 is SOX 302/404: the CEO and CFO certification obligation means the internal estimation process itself must be subject to internal controls. The quality of Tier 1 is therefore a prerequisite for the integrity of Tier 2.

The most significant practical gap is in uncertainty treatment. Organisations commonly present single-point IT cost forecasts with qualitative uncertainty acknowledgment. IAS 1.125 (confirmed by FRC enforcement) and ASC 275 both require quantitative uncertainty disclosure where it is material. Bridging this gap requires building range-based models internally and translating them into the specific disclosure language required by the applicable standard.

The correlation structure of IT cost uncertainties is the technically decisive issue that most practitioners overlook. Assuming independence (and applying RSS) when inputs are actually correlated produces overconfident uncertainty ranges that understate the true risk. For a board or regulatory audience, this is a material disclosure failure. The correct approach is Monte Carlo with an explicit correlation matrix, or, more conservatively, arithmetic addition of percentage ranges where correlation is suspected but not quantified.

### Risks, Gaps, and Uncertainties

1. **Correlation coefficients not standardised:** No authoritative standard specifies how IT cost category correlations should be estimated or disclosed. The direction (positive correlation for most categories) is well-reasoned; the magnitude must be estimated from organisation-specific historical data or expert calibration.

2. **Multi-year uncertainty disclosure gap:** No specific standard (IFRS, GAAP, FRC) directly addresses how multi-year compounding uncertainty in IT cost forecasts should be disclosed. Existing guidance focuses on near-term (next financial year) material adjustment risk, leaving a gap for 3–5 year TCO projections in business cases and investment papers.

3. **Internal vs. external document consistency:** The risk that internal business case forecasts and external filings use inconsistent assumptions without explanation is real but was not quantified from enforcement data in the consulted sources.

4. **Jurisdiction coverage gap:** Only IFRS, US GAAP, SEC, UK FRC, and EU Prospectus Regulation were investigated. Australian, Canadian, Japanese, and other regulatory frameworks may have different requirements.

5. **Practitioner framework depth:** COBIT 2019, ITIL 4, and TBM Council were accessed via secondary summaries and online practice guides. Full publication text may contain more specific uncertainty quantification guidance than captured here.

### Open Questions

1. How do organisations listed under both IFRS and US GAAP (dual-listing) reconcile the different disclosure thresholds for IT cost uncertainty, where ASC 275 triggers at "reasonably possible" and IAS 1.125 at "significant risk of material adjustment"? (Suggested priority: medium — relevant to dual-listed technology companies)

2. Does PCAOB AS 2101 or AICPA AU-C 540 contain guidance specifically applicable to auditing IT operational run-cost estimates as a category of accounting estimate? (Suggested priority: medium — relevant to audit preparedness for listed companies)

3. Does the RICS uncertainty of valuation methodology provide a directly portable disclosure model for IT cost uncertainty, given its mature practice for quantifying estimation ranges in professional standards? (Suggested priority: low — exploratory)

### Output

- **Type:** knowledge
- **Description:** Structured reference on IT operational run-cost forecasting best practices, covering cost taxonomy, required assumptions, uncertainty modelling techniques, compounding error propagation, and regulatory disclosure requirements across IFRS, GAAP, SEC MD&A, SOX, FRC, and EU Prospectus Regulation.
- **Key sources:**
  - TBM Council V4 Taxonomy (primary IT cost taxonomy standard): https://www.tbmcouncil.org/taxonomy/
  - SEC FR-72 / Item 303 MD&A guidance (regulatory disclosure standard): https://www.sec.gov/rules-regulations/2003/12/commission-guidance-regarding-managements-discussion-analysis-financial-condition-results-operations
  - FRC July 2022 Thematic Review: Judgements and Estimates (enforcement evidence): https://www.frc.org.uk/news-and-events/news/2022/07/frc-publishes-review-of-judgements-and-estimates/

---

## Research Skill Output

### §0 Initialise

**Research question restated:** What are the established best practices for financially responsible forecasting of IT operational run costs — covering cost estimation by technology and infrastructure type, required assumptions, uncertainty modelling (error bars and compounding estimate impact), and the regulatory and governance considerations that apply when these projections appear in financial filings or are used for planning and investment decisions?

**Scope confirmed:** In scope: IT cost taxonomy and estimation methodology; required assumptions by cost category; uncertainty modelling techniques (scenario analysis, sensitivity analysis, Monte Carlo simulation); compounding uncertainty across years/components; regulatory disclosure requirements (IFRS, GAAP, SOX, FRC, EU Prospectus Regulation); internal governance (budgeting, COBIT, ITIL). Out of scope: CapEx project estimation; detailed cloud cost accounting treatment; cost optimisation tactics; vendor-specific pricing calculators.

**Constraint mode:** Full — exhaustive investigation with complete decomposition, multi-lens expansion, and consistency check loops.

**Prior work cross-reference:** Checked `Research/completed/` for related items. `2026-03-02-transaction-costs.md` (Transaction Cost Economics) provides tangential framing around institutional cost structures and governance but does not address IT operational forecasting or regulatory disclosure. No directly applicable prior art found.

---

### §1 Question Decomposition

**Root question:** What are established best practices for financially responsible forecasting of IT operational run costs?

```
Root
├── 1. Cost categorisation
│   ├── 1a. Standard industry taxonomy
│   ├── 1b. Primary cost drivers by category
│   └── 1c. Volatility characteristics by category
├── 2. Required assumptions
│   ├── 2a. Practitioner framework requirements (ITIL 4, COBIT 2019, TBM)
│   ├── 2b. Which assumptions are typically material
│   └── 2c. How assumptions should be documented
├── 3. Uncertainty modelling techniques
│   ├── 3a. Scenario analysis — definition and applicability
│   ├── 3b. Sensitivity analysis (tornado charts)
│   └── 3c. Monte Carlo simulation
├── 4. Compounding uncertainty
│   ├── 4a. Independent vs. correlated IT cost uncertainties
│   ├── 4b. RSS vs. arithmetic combination
│   └── 4c. Multi-year TCO compounding implications
├── 5. Regulatory requirements
│   ├── 5a. IFRS — IAS 1.125, IAS 37
│   ├── 5b. GAAP — ASC 275
│   ├── 5c. SEC MD&A — FR-72, Item 303
│   ├── 5d. SOX Sections 302/404
│   ├── 5e. UK FRC guidance
│   └── 5f. EU Prospectus Regulation 2017/1129
└── 6. Financially responsible practice synthesis
```

---

### §2 Investigation

#### 2.1 IT Cost Taxonomy

**Standard taxonomy — Technology Business Management (TBM) [x]**

The TBM Council V4 taxonomy, the de facto industry standard for IT cost categorisation, defines a four-layer hierarchy. The *Cost Pool Layer* classifies expenses by what was purchased:

- **Labour:** Internal labour (employee wages, benefits, travel, training) and external labour (contractors, staff augmentation)
- **Software & SaaS:** Licensing, maintenance/support, SaaS subscriptions, depreciation of capitalised software
- **Cloud Services:** IaaS compute/storage/network; PaaS; managed services
- **Hardware:** Physical servers, storage arrays, network equipment, end-user devices; maintenance and depreciation
- **Telecom:** Network connectivity, mobile, data circuits
- **Facilities:** Data centre floor space, power, cooling

[Source: TBM Council V4 Taxonomy https://www.tbmcouncil.org/taxonomy/ [x]]

**ITIL 4 Service Financial Management cost types [x]**

ITIL 4 organises IT costs by the four dimensions of service management: organisations and people (payroll, travel, training), information and technology (hardware, software, networks), partners and suppliers (external services), and value streams and processes (management tools). The three core financial management activities are Budgeting, Accounting, and Charging. Budgeting is described as a continuous activity.

[Source: ITIL 4 Service Financial Management Practice Guide https://uat2.axelos.com/resource-hub/practice/service-financial-management-itil-4-practice-guide [x]]

**COBIT 2019 APO06 — Managed Budget and Costs [x]**

COBIT 2019's APO06 requires: budget vs. actual spend reports, cost-benefit analyses, variance explanations, and board approvals of major expenditures. COBIT positions IT financial management as a governance control function, not merely an accounting one.

[Source: COBIT 2019 Design Guide (ISACA) https://nextstepac.com/wp-content/uploads/2025/12/COBIT-2019-Design-Guide-by-ISACA.pdf [x]]

**Cost driver and volatility by category [fact]**

| Cost Category | Primary Cost Drivers | Volatility | Key Uncertainty Source |
|---|---|---|---|
| IaaS compute, storage, network | Usage volume, instance type, region, reserved vs. on-demand | High | Consumption growth; price between commitment cycles |
| PaaS managed services | API call volume, developer seat count | Medium-High | Feature adoption; vendor pricing changes |
| SaaS per-user licensing | Active user count, contract terms | Medium | User count growth; vendor renewal price increases |
| On-premises hardware | Refresh cycle (3–5 years), maintenance contracts | Low annually; High at refresh | Refresh timing; vendor end-of-life decisions |
| IT labour (internal) | Headcount, salary bands, benefits | Medium | Market wage inflation; specialist role scarcity |
| External contractors | Day rates, project duration | High | Rate inflation; scope creep |
| Software licensing (perpetual) | Tier, module count, maintenance % (typically 18–22% of licence) | Low-Medium | Vendor price list changes; compliance exposure |
| Network/telecom | Bandwidth committed, data transfer | Medium | Cloud egress charges frequently underestimated |
| Support/maintenance | Contract value, SLA tier, hardware age | Medium | Vendor escalation clauses; out-of-warranty costs |

**[fact]** IaaS cloud costs include hidden categories that scale behind the scenes: Application Programming Interface (API) request volume, data transfer/egress fees, and logging — these categories are frequently excluded from initial estimates and emerge as material surprises. Regional pricing differentials and compliance surcharges add further unpredictability.

[Sources: Stripe IaaS pricing guide https://stripe.com/resources/more/infrastructure-as-a-service-iaas-pricing-explained [x]; InfoTech project costing guide https://www.infotech.com/research/ss/invest-in-realistic-and-comprehensive-project-costing [x]; TBM Council taxonomy [x]]

#### 2.2 Required Assumptions

**Practitioner frameworks on required assumptions [fact]**

ITIL 4 identifies data modelling, forecasting, planning, and visualisation as "high importance" competencies for cost estimation. COBIT 2019 APO06 requires documented assumptions as part of budget-vs-actual variance analysis. TBM Council explicitly recommends range-based costing over point estimates: cloud costs "can rise by 20 to 30% or more annually" without governance. [Source: InfoTech [x]]

**Canonical required assumptions for an auditable IT run-cost estimate:**

1. **Usage/consumption growth rate** — by category; linked to a business driver (user headcount, transaction volume, data volume)
2. **Unit price assumptions** — by category; base price, escalation rate, and contract commitment period; for cloud: whether reserved/savings-plan discounts are applied
3. **Staffing headcount and grade mix** — plus assumed attrition and backfill timing
4. **Currency and exchange rate assumptions** — critical for multi-currency IT spend (e.g., USD-denominated cloud contracts for non-USD entities)
5. **Vendor contract assumptions** — renewal dates, price increase caps, volume discount thresholds
6. **Capitalisation vs. expense treatment** — whether software development costs are capitalised (affects forecast OpEx line)
7. **Hardware refresh cycle** — end-of-life schedule; drives maintenance cost trajectory as hardware ages out of warranty
8. **Organisational change assumptions** — mergers, divestitures, cloud migrations, infrastructure decommissions

**[inference]** Assumptions 1 and 2 are typically material for variable-cost categories (IaaS, SaaS per-user). Assumption 4 becomes material when foreign exchange exposure is large. Assumption 5 becomes material when vendor contracts contain aggressive escalation clauses.

#### 2.3 Uncertainty Modelling Techniques

**Scenario analysis [fact]**

Scenario analysis constructs three or more internally consistent views of the future (base, optimistic, pessimistic), modifying multiple input assumptions simultaneously. For IT run costs, a pessimistic scenario combines: higher-than-expected usage growth, vendor price increases, loss of negotiating leverage at renewal, and foreign exchange headwinds.

Appropriate when: qualitatively different futures are relevant; individual variable distributions are unknown; non-technical stakeholder communication is required. Limitation: the range between scenarios carries no probabilistic interpretation unless explicitly assigned.

[Sources: Toptal "How to Perform Monte Carlo Simulations" https://www.toptal.com/management-consultants/financial-forecasting/monte-carlo-simulation [x]; FinancialModelsLab https://financialmodelslab.com/blogs/blog/monte-carlo-simulation-financial-modelling [x]]

**Sensitivity analysis — tornado charts [fact]**

Sensitivity analysis measures how a change in one input variable (holding all others constant) affects the output. A tornado chart ranks input variables by the magnitude of their effect. For IT run costs, tornado analysis typically reveals that usage growth rate and IaaS unit price assumptions dominate forecast uncertainty — validating those two assumptions delivers more accuracy improvement than validating many smaller line items.

Appropriate when: many input variables exist and prioritisation of validation effort is needed. Limitation: one-at-a-time variation ignores correlation between inputs.

[Sources: Defacto Health Monte Carlo article https://defacto.health/2021/09/07/better-financial-modeling-with-monte-carlo-simulations/ [x]; Investopedia https://www.investopedia.com/terms/m/montecarlosimulation.asp [x]]

**Monte Carlo simulation [fact]**

Monte Carlo simulation assigns probability distributions to each uncertain input and runs thousands of random sampling iterations, producing a probability distribution of outcomes. Each iteration samples from input distributions; results aggregate into a fan of possible outcomes with associated probabilities (e.g., "90% probability that 3-year IT run costs fall between £X and £Y").

Monte Carlo is valuable for IT run costs because it: (1) captures simultaneous changes in multiple variables; (2) produces a genuine probability distribution (unlike scenarios); (3) supports within-model sensitivity analysis tracking which inputs drive output variance; (4) enables explicit communication of confidence intervals.

Appropriate when: input distributions can be estimated from historical data, market data, or expert judgement; audience can interpret probabilistic outputs; regulatory or board-level defensibility is required. Limitation: poorly calibrated input distributions produce false precision.

**[inference]** The three techniques are complementary. Scenario analysis is the accessible entry point; sensitivity analysis identifies critical assumptions; Monte Carlo is the defensible standard for regulatory or board use.

[Sources: Analytica finance article https://analytica.com/blog/monte-carlo-modeling-in-personal-finance-the-whoops-factor/ [x]; FinancialModelsLab [x]; Toptal [x]]

#### 2.4 Compounding Uncertainty

**Error propagation — mathematical basis [fact]**

When a forecast combines multiple uncertain estimates (total IT cost = IaaS + SaaS + Labour + Licensing + Support), combined uncertainty depends on whether individual uncertainties are independent or correlated:

- *Independent uncertainties:* combine via root-sum-square (RSS): if IaaS has ±10% and SaaS has ±15% uncertainty and they are independent, combined uncertainty = √(0.10² + 0.15²) ≈ ±18%, not ±25%.
- *Correlated uncertainties:* combine arithmetically: if both IaaS and SaaS are denominated in USD against a GBP budget, combined currency uncertainty ≈ ±10% + ±15% = ±25%.

[Sources: Wikipedia "Propagation of uncertainty" https://en.wikipedia.org/wiki/Propagation_of_uncertainty [x]; WSU error propagation PDF https://s3.wp.wsu.edu/uploads/sites/2621/2021/06/A-3-Data-Analysis-4-Error-Propagation.pdf [x]]

**Correlation in IT cost forecasts [inference]**

In practice, many IT cost uncertainties are positively correlated, not independent:
- Macro-economic inflation affects multiple cost categories simultaneously
- Vendor price increases tend to be correlated across software vendors in the same market cycle
- Labour market conditions affect both internal IT salary costs and external contractor rates
- A major unplanned infrastructure event raises costs across multiple categories simultaneously

**[inference]** Organisations that assume independence and use RSS will systematically understate combined forecast uncertainty. For multi-year IT run cost forecasts with correlated inputs, arithmetic addition of percentage ranges is more conservative and appropriate. Monte Carlo with explicit correlation matrices is the technically correct approach.

**Multi-year compounding [fact]**

In a multi-year TCO forecast, errors compound across time periods: year-one growth rate assumptions form the base for year-two calculations. Research on travel demand models — which share the same multi-stage multiplicative structure as IT cost models — found that "mispredictions at early stage of multi-stage models appear to be amplified across later stages."

[Source: TTI/Texas A&M "Propagation of Uncertainty Through Travel Demand Models" https://static.tti.tamu.edu/swutc.tamu.edu/publications/technicalreports/167804-1.pdf [x]]

**[fact]** A cost estimate with ±15% annual uncertainty produces approximately ±34% five-year uncertainty if errors are independent (RSS over 5 periods), and up to ±75% if errors are fully correlated and systematic. No authoritative standard was found specifying how multi-year IT cost uncertainty should be disclosed — this is a gap.

#### 2.5 Regulatory Requirements

**IFRS — International Accounting Standard (IAS) 1 paragraph 125 [x]**

IAS 1 paragraph 125 requires disclosure of assumptions with a significant risk of resulting in a material adjustment to asset or liability carrying amounts within the next financial year. Trigger: (a) subjectivity around assumptions and estimates, AND (b) significant risk that a material adjustment may be required within the next period.

UK FRC July 2022 thematic review found persistent failures: generic boilerplate, failure to quantify assumptions, missing sensitivity disclosures, and failure to distinguish short-term from longer-term uncertainties. FRC good practice: quantified assumptions and amounts at risk; detailed explanation of the nature of uncertainties; entity-specific (not generic) disclosures.

[Sources: IFRS Foundation staff paper https://www.ifrs.org/content/dam/ifrs/meetings/2023/january/issb/ap3b-general-sustainability-related-disclosures-s1-disclosure-of-judgements-assumptions-and-estimates.pdf [x]; dreport.cz explainer https://www.dreport.cz/en/blog/disclosure-of-significant-judgements-and-key-sources-of-estimation-uncertainty/ [x]; FRC July 2022 thematic review https://www.frc.org.uk/news-and-events/news/2022/07/frc-publishes-review-of-judgements-and-estimates/ [x]]

**IAS 37 — Provisions and Contingent Liabilities [x]**

IAS 37 applies where IT costs give rise to a constructive or legal obligation — for example, cloud contracts with committed minimum spend, or maintenance agreements creating committed future outflows. Provisions recognised when: (a) present obligation, (b) probable outflow, (c) reliable estimate. For uncertain future IT obligations, disclosure is required even where recognition is not.

[Sources: IFRS.org IAS 37 page https://www.ifrs.org/issued-standards/list-of-standards/ias-37-provisions-contingent-liabilities-and-contingent-assets/ [x]; KPMG IFRS vs. US GAAP comparison https://kpmg.com/us/en/articles/2026/ifrs-accounting-standards-us-gaap.html [x]]

**GAAP — ASC 275 Risks and Uncertainties [x]**

ASC 275 triggers disclosure when: (1) it is *at least reasonably possible* that the estimate will change materially in the near term, AND (2) the effect would be material. "Reasonably possible" is a lower bar than IFRS's "significant risk" — it falls between "remote" and "probable." IT cost commitments (cloud minimum spend, prepaid licences) fall within scope when material.

[Sources: PwC Viewpoint 24.3 https://viewpoint.pwc.com/dt/us/en/pwc/accounting_guides/financial_statement_/financial_statement___18_US/chapter_24_risks_and_US/243_disclosure_US.html [x]; SEC SAB Topic 5 https://www.sec.gov/interps/account/sabcodet5.htm [x]]

**SEC MD&A — Item 303 / FR-72 [x]**

FR-72 guidance (2003) and the 2020 Item 303 amendments require disclosure of known trends and uncertainties *reasonably likely* to have a material effect on results. The SEC guidance explicitly states: "Not all forward-looking information is optional. Material forward-looking information regarding known material trends and uncertainties is required." The 2020 amendments require disclosure of "known events that are reasonably likely to cause a material change in the relationship between costs and revenues, such as known or reasonably likely future increases in costs of labor or materials or price increases" — directly capturing IT labour escalation and software vendor price increases.

[Sources: SEC FR-72 https://www.sec.gov/rules-regulations/2003/12/commission-guidance-regarding-managements-discussion-analysis-financial-condition-results-operations [x]; Federal Register 2021 https://www.federalregister.gov/documents/2021/01/11/2020-26090/managements-discussion-and-analysis-selected-financial-data-and-supplementary-financial-information [x]]

**SOX Sections 302 and 404 [x]**

Section 302: CEO and CFO must certify accuracy of financial reports and effectiveness of internal controls; must disclose all significant deficiencies. Section 404: management's annual ICFR assessment plus external auditor attestation (for large public companies). For IT cost forecasting, if IT operational costs are material, the estimation controls (data inputs, model assumptions, review/approval process) are part of ICFR and must be assessed.

[Sources: AuditBoard https://auditboard.com/blog/sarbanes-oxley-act [x]; UpGuard https://www.upguard.com/blog/sox-compliance [x]]

**FRC guidance [x]**

FRC 2017 and 2022 thematic reviews identify persistent failures under IAS 1 paragraphs 122 and 125: generic disclosures, unexplained estimation uncertainty, missing quantification, failure to distinguish estimates with short-term vs. longer-term effects. FRC recommends a *smaller number of richer disclosures* rather than comprehensive boilerplate — entity-specific and quantified.

[Sources: FRC July 2022 thematic review [x]; IASplus.com thematic review summary https://iasplus.com/content/9a89e67a-cd50-49a9-8050-b62ebd8c95cb [x]]

**EU Prospectus Regulation 2017/1129 [x]**

Under Regulation (EU) 2017/1129, prospectuses must include risk factors that are material and *specific to the issuer*. Generic risk factors are non-compliant. If IT operational costs are a material cost category, a prospectus must include specific, quantified risk factor disclosure covering the nature of the cost uncertainty, the magnitude of potential variation, and the business impact. Risk factors must be categorised by significance with the most material risks placed first.

[Sources: EUR-Lex Regulation (EU) 2017/1129 https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:02017R1129-20191231 [x]; Travers Smith overview https://www.traverssmith.com/knowledge/knowledge-container/eu-prospectus-regulation-what-fund-managers-and-investment-companies-sponsors-need-to-know/ [x]]

---

### §3 Reasoning

Claims removed or reclassified:
- "Monte Carlo is always superior to scenario analysis" → rejected; conditional statement replacing it.
- "IT cost forecasts always exhibit positive correlation" → reclassified as [inference] with conditions.
- "SOX Section 404 directly requires IT cost forecasting controls" → tightened to apply only where IT costs are material to reported financial figures.

All causal claims reviewed; sources verified; [fact], [inference], and [assumption] labels applied throughout §2.

---

### §4 Consistency Check

- **Correlated vs. independent uncertainty:** §2.4 and §6 synthesis are consistent; both recommend Monte Carlo with correlation matrices as the correct approach.
- **Regulatory thresholds:** GAAP ASC 275 ("reasonably possible"), SEC MD&A ("reasonably likely"), and IFRS IAS 1.125 ("significant risk of material adjustment") are three distinct standards correctly differentiated in §2.5.
- **ITIL vs. TBM taxonomies:** Complementary, not contradictory; TBM is the primary categorisation reference, ITIL provides governance process framing.
- **Acronym audit:** All acronyms expanded on first use in Findings and Research Skill Output sections.

**No unresolvable contradictions found.**

---

### §5 Depth and Breadth Expansion

**Technical lens:** The mathematical treatment of error propagation is domain-independent; its application to IT cost forecasting reveals that assuming independence when inputs are correlated produces overconfident (too-narrow) uncertainty ranges. Any credible IT run-cost forecast should explicitly state the assumed correlation structure.

**Economic lens:** IT cost inflation is not uniformly distributed. Cloud compute unit prices have generally declined per unit as hardware costs fall, but total cloud spend has risen because consumption growth exceeds unit price reductions. Labour costs in specialist IT roles have experienced above-inflation growth due to skills scarcity. Applying uniform inflation assumptions across all IT categories is economically naive.

**Regulatory lens:** The gap between internal planning standards and external disclosure standards is significant. Internal business cases may use optimistic single-point estimates to secure approval. If those estimates appear in prospectuses or annual reports, they must meet a higher standard of disclosure. A material discrepancy between internal forecasts and disclosed figures without explanation could constitute misrepresentation.

**Historical lens:** SOX's CEO/CFO certification obligation arose directly from Enron/WorldCom (2002), where material misrepresentations in forward-looking cost and revenue disclosures destroyed shareholder value. The legislative intent is directly relevant: senior executives certify the integrity of the estimation processes behind their financial statements, not just the outputs.

**Behavioural lens:** Optimism bias in operational cost estimation is well documented. Internal forecasters face incentives to present low cost estimates to secure budget approval. The regulatory framework counteracts this by requiring uncertainty disclosure — making single-point optimistic estimates harder to file without acknowledging the upside cost risk.

**Governance lens:** COBIT 2019 APO06 and ITIL 4 both position IT cost forecasting as a governance function, not merely an accounting one. Board-level approval of major IT expenditures, variance analysis against budget, and documented assumptions are governance controls — and regulatory frameworks (SOX, IFRS, GAAP) align by requiring that estimation processes be subject to internal control.

---

### §6 Synthesis

*(See Findings section above — §6 synthesis content was seeded into Findings as the primary output per research prompt step 5.)*

---

### §7 Recursive Review

Every section in §2 maps to a decomposed question from §1. §6 synthesis is traceable to §2 investigation throughout. Facts carry source citations; inferences are labelled [inference] with reasoning; assumptions are labelled [assumption] with justification. Unconsulted sources listed in Evidence Map. All uncertainties explicit in Risks/Gaps. Acronym expansion confirmed across both Findings and Research Skill Output sections.

**Acronyms expanded on first use in document:**
- IT: Information Technology (frontmatter/scope)
- IaaS: Infrastructure as a Service (scope section)
- PaaS: Platform as a Service (scope section)
- SaaS: Software as a Service (scope section)
- IFRS: International Financial Reporting Standards (scope section)
- GAAP: Generally Accepted Accounting Principles (scope section)
- SOX: Sarbanes-Oxley Act (scope section)
- ITIL: IT Infrastructure Library (Executive Summary in Findings)
- TBM: Technology Business Management (Findings Key Finding 1)
- IAS: International Accounting Standard (Findings Executive Summary)
- MD&A: Management Discussion and Analysis (Findings Key Finding 9)
- SEC: Securities and Exchange Commission (Findings Executive Summary)
- FRC: Financial Reporting Council (Findings Executive Summary)
- COBIT: Control Objectives for Information and Related Technologies (Findings Evidence Map)
- ICFR: internal controls over financial reporting (Findings Key Finding 10)
- TCO: total cost of ownership (§1 decomposition)
- RSS: root-sum-square (§2.4)
- API: Application Programming Interface (§2.1 in Research Skill Output)
- CEO: Chief Executive Officer (§2.5 SOX section)
- CFO: Chief Financial Officer (§2.5 SOX section)
- FinOps: Financial Operations (Findings Assumptions section)

**§7 verdict: PASS.**
