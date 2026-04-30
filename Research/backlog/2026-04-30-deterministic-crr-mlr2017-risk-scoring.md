---
title: "Deterministic weighted scoring models for customer risk rating under MLR 2017: effectiveness, regulatory fit, and hybrid alternatives"
added: 2026-04-30T19:11:29+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: []
tags: [governance, regulation, financial-services, audit, risk-management, compliance, machine-learning]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
cites: []
related: [2026-04-30-explainable-ai-xai-regulation-governance, 2026-04-24-ai-agent-regulation-global-financial-services]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Deterministic weighted scoring models for customer risk rating under MLR 2017: effectiveness, regulatory fit, and hybrid alternatives

## Research Question

To what extent do deterministic weighted scoring models (based on the four main risk factors: customer, geographic, product/service, and delivery channel) effectively support a proportionate risk-based approach to customer due diligence (CDD) under the Money Laundering Regulations 2017 (MLR 2017), and what are their limitations compared to hybrid or machine learning-enhanced alternatives?

## Scope

**In scope:**
- Definition and mechanics of deterministic four-factor customer risk rating (CRR) models: factor weights (Geographic ~30%, Customer ~35%, Product/Service ~25%, Channel/Delivery ~10%), sub-factor scoring scales, weighted-sum calculation, and band mapping (Low/Medium/High/Critical)
- MLR 2017 regulatory requirements: Regulation 18 (firm-wide risk assessment) and Regulation 28 (customer due diligence); the risk-based approach (RBA) and proportionality principle; JMLSG (Joint Money Laundering Steering Group) Part I guidance on risk factor weighting
- Effectiveness evaluation metrics: alignment of assigned risk bands with actual suspicious activity report (SAR) filings and investigation outcomes; false positive and false negative rates; auditability and regulatory defensibility
- Comparison with hybrid models (deterministic rules combined with statistical or machine learning overlays) and fully supervised machine learning (ML) approaches (e.g., XGBoost, random forests) for customer risk prediction
- Practical implementation considerations: calibration of weights and thresholds, governance and periodic recalibration, small vs. large firm differences, impact on de-risking and financial inclusion
- UK-specific supervisory landscape: Financial Conduct Authority (FCA) and HMRC supervisory expectations; evidence from thematic reviews

**Out of scope:**
- Transaction monitoring models (distinct from customer risk rating)
- Non-UK jurisdictions (Fifth Anti-Money Laundering Directive [5AMLD]/Sixth Anti-Money Laundering Directive [6AMLD] context referenced only for comparison)
- Cryptocurrency-specific AML (Anti-Money Laundering) controls, except where used to illustrate model design
- Full derivations of ML algorithms

**Constraints:**
- Focus on published guidance (MLR 2017 text, JMLSG, FCA), academic literature, and practitioner sources from 2017 onwards
- English-language sources only

## Context

UK-regulated firms subject to MLR 2017 must adopt a risk-based approach to CDD, calibrated to their assessed money laundering (ML) and terrorist financing (TF) risk exposure. The dominant tool is a deterministic weighted scoring model that maps customer attributes to a numeric risk score and then to a CDD level (standard, enhanced, or simplified). These models are attractive because of their transparency, auditability, and ease of explanation to regulators and staff — properties that purely data-driven ML models struggle to provide.

However, deterministic models have well-known weaknesses: static weights may not reflect current typologies, interactions between risk factors are ignored, and the model cannot learn from outcome data without manual recalibration. As ML tooling matures and regulators begin to accept "explainable AI" (XAI) frameworks, firms are asking whether hybrid or ML-enhanced models can improve risk stratification accuracy without sacrificing regulatory defensibility. This question is practically significant for compliance teams designing or validating CRR models and for supervisors assessing model adequacy under Regulation 18.

This item connects to the completed research on XAI and regulatory requirements (`2026-04-30-explainable-ai-xai-regulation-governance`) and to AI governance in financial services (`2026-04-24-ai-agent-regulation-global-financial-services`).

## Approach

1. **Define the model class** — Describe deterministic four-factor CRR model mechanics in detail: factor selection, typical weight ranges, sub-factor taxonomies (PEP status, high-risk jurisdiction lists, channel types), scoring scales, band thresholds. Identify open-source or published examples from compliance tooling or academic papers.

2. **Map regulatory requirements** — Review MLR 2017 Regulations 18 and 28 text directly; review JMLSG Part I guidance sections on risk factors and weighting; review FCA thematic reviews and supervisory notices that reference CRR model adequacy. Establish what the regulations actually require vs. what is convention.

3. **Evaluate model effectiveness** — Search for empirical studies or practitioner evidence correlating deterministic CRR scores with SAR outcomes, investigation results, or regulatory findings. Assess whether the literature provides outcome-based validation evidence, or only process-based arguments (transparency, auditability).

4. **Catalogue limitations** — Systematically identify documented weaknesses: inability to handle factor interactions, static calibration, risk of "checkbox" compliance, gaming potential, impact on de-risking.

5. **Survey alternatives** — Review hybrid model architectures (rules + ML overlay, rules + behavioural layer) and fully ML-driven CRR approaches. Assess the explainability challenge under current FCA/supervisory expectations and emerging XAI approaches.

6. **Analyse trade-offs** — Synthesise the evidence into a structured comparison: deterministic vs. hybrid vs. ML on the dimensions of regulatory defensibility, accuracy, operational cost, governance overhead, and de-risking risk.

7. **Survey the vendor and technology landscape** — Identify firms building CRR tooling (deterministic, hybrid, and ML-based) and note any open-source frameworks.

## Sources

- [ ] [Money Laundering, Terrorist Financing and Transfer of Funds (Information on the Payer) Regulations 2017 — UK Statute](https://www.legislation.gov.uk/uksi/2017/692/contents) — primary regulatory text; Regulations 18 and 28 directly relevant
- [ ] [JMLSG Guidance Part I — Prevention of money laundering/combating terrorist financing (2022 revised)](https://www.jmlsg.org.uk/guidance/current-guidance/) — industry guidance on risk-based approach and risk factor weighting; primary reference for model design conventions
- [ ] [FCA — Financial Crime Guide: A firm's guide to countering financial crime risks](https://www.handbook.fca.org.uk/handbook/FCG/) — FCA expectations for risk-based approach and customer risk rating
- [ ] [FATF (Financial Action Task Force) — Guidance for a Risk-Based Approach: The Banking Sector (2014)](https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Risk-based-approach-banking-sector.html) — FATF framework underpinning MLR 2017 risk-based approach; risk factor taxonomy
- [ ] [Basel Committee on Banking Supervision — Sound management of risks related to money laundering and financing of terrorism (2020)](https://www.bis.org/bcbs/publ/d505.htm) — Basel guidance on AML/CFT risk assessment frameworks for banks; customer risk rating expectations
- [ ] [Levi & Reuter (2006) — Money Laundering](https://doi.org/10.1086/655355) — foundational criminology review of ML/TF risk and its measurement; contextualises what risk-based models are trying to predict
- [ ] [Ferwerda et al. (2013) — Detecting Money Laundering: A Risk-Based Approach](https://doi.org/10.1111/j.1467-6419.2012.00741.x) — academic study of risk-based AML approaches; evidence on scoring model design
- [ ] [de Koker (2009) — The Money Laundering Risk Posed by Low-Risk Financial Products in South Africa: Findings and Guidelines](https://doi.org/10.1080/10511970.2009.9521756) — evidence on risk scoring calibration and de-risking effects
- [ ] [Canhoto (2021) — Leveraging machine learning in the global fight against money laundering and terrorist financing: An affordances perspective](https://doi.org/10.1016/j.jbusres.2020.10.035) — review of ML applications in AML; contrasts with rule-based approaches
- [ ] [Savage et al. (2016) — Detection of Money Laundering Groups: Supervised Learning on Small Networks](https://arxiv.org/abs/1608.00708) — supervised ML approach to AML detection; benchmark for comparing with deterministic methods
- [ ] [FCA — TR19/4: Banks' management of high money-laundering risk situations (2011, updated guidance)](https://www.fca.org.uk/publications/thematic-reviews/tr11-12-banks-management-money-laundering-risk) — FCA thematic review; evidence on how firms implement customer risk rating in practice
- [ ] [Home Office / UKFIU — Suspicious Activity Reports (SARs) Annual Report](https://www.nationalcrimeagency.gov.uk/what-we-do/national-economic-crime-centre/financial-intelligence-unit) — UK SAR statistics; baseline data for assessing model outcome correlation

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

-

### §1 Question Decomposition

-

### §2 Investigation

-

### §3 Reasoning

-

### §4 Consistency Check

-

### §5 Depth and Breadth Expansion

-

### §6 Synthesis

*(This section seeds the Findings below.)*

**Executive summary:**

**Key findings:**

**Evidence map:**

**Assumptions:**

**Analysis:**

**Risks, gaps, uncertainties:**

**Open questions:**

### §7 Recursive Review

-

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

### Key Findings

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|

### Assumptions

### Analysis

### Risks, Gaps, and Uncertainties

### Open Questions

---

## Output

*(Fill in when completing — what was produced as a result of this research?)*

- Type: # skill | tool | agent | knowledge | backlog-item
- Description:
- Links:
