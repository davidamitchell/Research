---
title: "Best practices in financial forecasting for IT operational run costs: assumptions, uncertainty, and regulatory considerations"
added: 2026-03-13
status: backlog
priority: high
blocks: []
tags: [financial-forecasting, it-run-costs, uncertainty-modelling, regulatory, error-bars, infrastructure-costing, assumptions]
started: ~
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
