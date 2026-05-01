---
title: "Deterministic weighted scoring models for customer risk rating under MLR 2017: effectiveness, regulatory fit, and hybrid alternatives"
added: 2026-04-30T19:11:29+00:00
status: reviewing
priority: high  # low | medium | high
blocks: []
tags: [governance, regulation, financial-services, audit, risk-management, compliance, machine-learning, explainability]
started: 2026-05-01T02:01:23+00:00
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
cites: [2026-04-24-ai-agent-regulation-global-financial-services]
related: [2026-04-22-ai-governance-assurance-change-control-verification, 2026-02-28-rbnz-ai-supervisory-expectations]
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
- Definition and mechanics of deterministic four-factor customer risk rating (CRR) models: factor weights, sub-factor scoring scales, weighted-sum calculation, and band mapping
- MLR 2017 regulatory requirements: Regulation 18 and Regulation 28; the risk-based approach and proportionality principle; Financial Conduct Authority (FCA) supervisory signals
- Effectiveness evaluation metrics: relationship to suspicious activity report (SAR) filings, investigation outcomes, false positives, false negatives, auditability, and regulatory defensibility
- Comparison with hybrid models and fully supervised machine learning (ML) approaches for customer risk prediction
- Practical implementation considerations: calibration, governance, periodic recalibration, small versus large firm differences, and de-risking effects
- United Kingdom (UK)-specific supervisory landscape

**Out of scope:**
- Transaction monitoring models as a standalone control class
- Non-UK jurisdictions except where comparator guidance sharpens the analysis
- Cryptocurrency-specific anti-money laundering (AML) controls, except where used to illustrate model design
- Full derivations of ML algorithms

**Constraints:**
- Focus on published guidance, open academic literature, and practitioner sources from 2017 onwards where possible
- English-language sources only

## Context

UK-regulated firms subject to MLR 2017 must adopt a risk-based approach to customer due diligence (CDD), calibrated to their assessed money laundering and terrorist financing risk exposure. [fact; source: https://www.legislation.gov.uk/uksi/2017/692/regulation/18; https://www.legislation.gov.uk/uksi/2017/692/regulation/28]

Deterministic weighted scoring models are a common operational way to turn those obligations into customer risk ratings, because they let firms document factors, thresholds, overrides, and review triggers in a form that staff and supervisors can follow. [inference; source: https://www.ey.com/en_ch/disrupting-financial-crime/how-do-you-successfully-operationalize-your-client-risk-rating-model; https://www.fca.org.uk/publications/thematic-reviews/tr19-4-understanding-money-laundering-risks-capital-markets]

However, static weights can drift away from real risk, miss interactions between factors, and fail to learn from outcomes without manual recalibration, which is why the question of hybrid or machine learning (ML)-enhanced alternatives matters in practice. [inference; source: https://financialcrimeacademy.org/customer-risk-rating-models/; https://www.bis.org/bcbs/publ/d353.pdf]

This item connects directly to the completed research on finance-sector artificial intelligence regulation and explainability expectations and indirectly to the completed research on governance assurance and review loops. [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-24-ai-agent-regulation-global-financial-services.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-ai-governance-assurance-change-control-verification.md]

## Approach

1. **Define the model class** - Describe deterministic CRR mechanics in detail and identify published examples.
2. **Map regulatory requirements** - Read Regulation 18, Regulation 28, GOV.UK guidance, and FCA material to establish what the law and supervisors require versus what is merely convention.
3. **Evaluate model effectiveness** - Search for empirical studies or regulator evidence linking deterministic scores to SAR or investigation outcomes.
4. **Catalogue limitations** - Identify documented weaknesses such as stale weights, ignored interactions, gaming, and de-risking effects.
5. **Survey alternatives** - Review hybrid architectures and fully ML-driven approaches, especially their explainability and governance implications.
6. **Analyse trade-offs** - Compare deterministic, hybrid, and ML approaches on defensibility, accuracy, operating cost, governance burden, and inclusion effects.
7. **Note the tooling landscape** - Capture only enough practitioner evidence to ground how firms operationalize CRR models in practice.

## Sources

- [x] [UK Legislation (2017) Money Laundering Regulations 2017, Regulation 18](https://www.legislation.gov.uk/uksi/2017/692/regulation/18) - primary statutory text for the business-wide risk assessment requirement.
- [x] [UK Legislation (2017) Money Laundering Regulations 2017, Regulation 28](https://www.legislation.gov.uk/uksi/2017/692/regulation/28) - primary statutory text for customer due diligence and ongoing monitoring.
- [ ] [Joint Money Laundering Steering Group (2025) Current Guidance](https://www.jmlsg.org.uk/guidance/current-guidance/) - official industry guidance starting point for current UK convention statements.
- [x] [HM Government (2025) Money laundering regulations: risk assessments](https://www.gov.uk/guidance/money-laundering-regulations-risk-assessments) - official UK guidance on applying a risk-based approach and choosing methodology.
- [x] [HM Government (2025) Money laundering regulations: your responsibilities](https://www.gov.uk/guidance/money-laundering-regulations-your-responsibilities) - official UK operational guidance on customer due diligence, enhanced due diligence, and controls.
- [x] [Financial Conduct Authority (2019, updated 2025) TR19/4 Understanding the money laundering risks in the capital markets](https://www.fca.org.uk/publications/thematic-reviews/tr19-4-understanding-money-laundering-risks-capital-markets) - official FCA thematic-review page highlighting customer risk assessment and due diligence expectations.
- [x] [Financial Conduct Authority (2025) FCG 3 Money laundering and terrorist financing](https://handbook.fca.org.uk/handbook/FCG/3) - official FCA handbook section used for customer due diligence and risk-based-approach expectations.
- [ ] [FATF (2014) Risk-Based Approach Guidance for the Banking Sector](https://www.fatf-gafi.org/media/fatf/documents/reports/Risk-Based-Approach-Banking-Sector.pdf) - official international comparator for risk-factor taxonomies and proportionality.
- [x] [Basel Committee on Banking Supervision (2016) Sound management of risks related to money laundering and financing of terrorism](https://www.bis.org/bcbs/publ/d353.pdf) - official banking guidance on customer risk profiles and ongoing monitoring.
- [x] [National Crime Agency (2024) SARs Annual Report 2024](https://www.nationalcrimeagency.gov.uk/who-we-are/publications/747-sars-annual-report-2024/file) - official regime-level outcomes data for SAR and Defence Against Money Laundering activity.
- [x] [EY (2023) How do you successfully operationalize your client risk rating model?](https://www.ey.com/en_ch/disrupting-financial-crime/how-do-you-successfully-operationalize-your-client-risk-rating-model) - practitioner description of point-based CRR mechanics, weights, and triggers.
- [x] [Financial Crime Academy (2022) Customer Risk Rating Models in Customer Due Diligence and Know Your Customer](https://financialcrimeacademy.org/customer-risk-rating-models/) - practitioner source on static customer risk models and their operational weaknesses.
- [x] [Canhoto (2021) Leveraging machine learning in the global fight against money laundering and terrorism financing: An affordances perspective](https://bura.brunel.ac.uk/bitstream/2438/25258/1/FullText.pdf) - open-access academic paper on where supervised, unsupervised, and reinforced ML fit in AML.
- [x] [Savage et al. (2016) Detection of Money Laundering Groups: Supervised Learning on Small Networks](https://arxiv.org/abs/1608.00708) - open-access example of supervised learning succeeding in group-behavior detection rather than simple onboarding scoring.
- [x] [Jensen et al. (2023) Fighting Money Laundering with Statistics and Machine Learning](https://arxiv.org/abs/2201.04207) - open-access review of client risk profiling, suspicious-behavior flagging, interpretability, and data scarcity.
- [x] [Mitchell (2026) Global artificial intelligence agent regulation in financial services](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-24-ai-agent-regulation-global-financial-services.md) - prior repository item showing that explainability, auditability, and human oversight recur across finance-sector AI regulation.

---

## Research Skill Output

*(Full output from running the research skill - retained verbatim in the completed item. Sections 0 to 5 are the investigation; Section 6 seeds the Findings section below.)*

### §0 Initialise

- [fact; source: https://www.legislation.gov.uk/uksi/2017/692/regulation/18; https://www.legislation.gov.uk/uksi/2017/692/regulation/28] **Research question restated:** whether deterministic weighted customer risk rating (CRR) models are an effective and proportionate way to implement the Money Laundering Regulations 2017 (MLR 2017) risk-based approach to customer due diligence (CDD), and where hybrid or machine learning (ML)-enhanced alternatives materially improve on them.
- [fact; source: https://www.gov.uk/guidance/money-laundering-regulations-risk-assessments; https://www.gov.uk/guidance/money-laundering-regulations-your-responsibilities; https://www.fca.org.uk/publications/thematic-reviews/tr19-4-understanding-money-laundering-risks-capital-markets] **Scope confirmed:** this item focuses on United Kingdom (UK) legal requirements, Financial Conduct Authority (FCA) supervisory expectations, public evidence on effectiveness, and the trade-off between deterministic, hybrid, and ML-driven approaches for onboarding and lifecycle anti-money laundering (AML) customer risk assessment.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-24-ai-agent-regulation-global-financial-services.md] **Prior work cross-reference:** the most relevant completed repository item already established that explainability, auditability, and human oversight recur across finance-sector AI governance, so this item tests how far deterministic CRR models currently satisfy those expectations better than more opaque ML alternatives.
- [fact; source: https://www.bis.org/bcbs/publ/d353.pdf; https://arxiv.org/abs/2201.04207] **Output format:** the output is a knowledge item that separates legal fit from predictive effectiveness, then compares deterministic, hybrid, and ML approaches against both dimensions.

### §1 Question Decomposition

- **Root question:** How well do deterministic weighted CRR models satisfy MLR 2017 and how do they compare with hybrid or ML-enhanced alternatives?
- **A. Legal and supervisory baseline**
  - A1. What does Regulation 18 require a firm to assess and document?
  - A2. What does Regulation 28 require for customer due diligence, ongoing monitoring, and evidencing appropriateness?
  - A3. Do current UK guidance sources prescribe a fixed four-factor weighted formula, or do they only prescribe factor classes and proportionality?
- **B. Deterministic model mechanics**
  - B1. How do published CRR models turn risk factors into low, medium, and high customer bands?
  - B2. Which variables, weights, and override triggers are common in practice?
- **C. Effectiveness**
  - C1. Is there public evidence linking deterministic CRR bands to suspicious activity report (SAR) or investigation outcomes?
  - C2. What public evidence exists on false positives, false negatives, stale data, and calibration problems?
- **D. Alternatives**
  - D1. Where does supervised ML outperform static scoring in AML contexts?
  - D2. What limits supervised ML in customer risk scoring?
  - D3. What does a credible hybrid model keep from deterministic scoring and what does it add?
- **E. Trade-offs**
  - E1. Which approach best fits regulatory defensibility?
  - E2. Which approach best fits predictive performance?
  - E3. Which approach creates the lowest governance and inclusion risk?

### §2 Investigation

#### A. UK legal and supervisory baseline

- [fact; source: https://www.legislation.gov.uk/uksi/2017/692/regulation/18] Regulation 18 requires a relevant person to identify and assess money laundering and terrorist financing risks by taking account of factors relating to customers, countries or geographic areas, products or services, transactions, and delivery channels, and to size that assessment to the size and nature of the business.
- [fact; source: https://www.legislation.gov.uk/uksi/2017/692/regulation/28] Regulation 28 requires customer due diligence and ongoing monitoring measures to reflect both the firm's Regulation 18 business-wide risk assessment and the level of risk in the particular case, and it expressly says the extent of measures may differ from case to case.
- [fact; source: https://www.gov.uk/guidance/money-laundering-regulations-risk-assessments] GOV.UK guidance states that firms can choose their own methodology for risk assessment, ranging from simple to sophisticated, provided they identify relevant risks, design controls, monitor those controls, and record what they did and why they did it.
- [fact; source: https://www.gov.uk/guidance/money-laundering-regulations-your-responsibilities] GOV.UK guidance also states that firms must identify customers and beneficial owners, understand the purpose and intended nature of relationships, keep customer information up to date, and apply enhanced due diligence in higher-risk situations such as politically exposed person relationships, non-face-to-face onboarding, or high-risk third-country exposure.
- [fact; source: https://www.fca.org.uk/publications/thematic-reviews/tr19-4-understanding-money-laundering-risks-capital-markets] The FCA's TR19/4 thematic-review page says effective customer risk assessment and customer due diligence are key to reducing opportunities for money laundering, and it also highlights weak first-line ownership and uneven maturity across firms.
- [fact; source: https://www.legislation.gov.uk/uksi/2017/692/regulation/18; https://www.gov.uk/guidance/money-laundering-regulations-risk-assessments; https://www.fca.org.uk/publications/thematic-reviews/tr19-4-understanding-money-laundering-risks-capital-markets] No accessible primary UK source reviewed in this session prescribed fixed numeric weights for customer, geography, product or service, and delivery-channel factors.

#### B. Deterministic model mechanics in practice

- [fact; source: https://www.ey.com/en_ch/disrupting-financial-crime/how-do-you-successfully-operationalize-your-client-risk-rating-model] EY describes client risk rating models as classifying customers into categories such as low, medium, and high risk using factors such as source of wealth, source of funds, domicile, transaction behavior, complex ownership structures, industry, negative news, wealth volume, and politically exposed person status.
- [fact; source: https://www.ey.com/en_ch/disrupting-financial-crime/how-do-you-successfully-operationalize-your-client-risk-rating-model] EY also describes a common "risk point" model in which each factor receives points, factors can receive additional weighting, automatic high-risk triggers can override the score, and the total is compared with classification thresholds.
- [fact; source: https://financialcrimeacademy.org/customer-risk-rating-models/] Financial Crime Academy describes mainstream customer risk models as relying heavily on onboarding information such as employment, salary, and products used, then calculating a weighted risk score from those inputs.
- [fact; source: https://financialcrimeacademy.org/customer-risk-rating-models/] Financial Crime Academy says those onboarding inputs are seldom updated, which means many customer risk models take a static view of the customer profile unless a major trigger event forces review.
- [inference; source: https://www.legislation.gov.uk/uksi/2017/692/regulation/18; https://www.ey.com/en_ch/disrupting-financial-crime/how-do-you-successfully-operationalize-your-client-risk-rating-model] Deterministic four-factor CRR models are therefore best understood as an institution-designed operationalization of Regulation 18 factor classes, not as a regulator-mandated formula.
- [fact; source: https://www.legislation.gov.uk/uksi/2017/692/regulation/18; https://www.gov.uk/guidance/money-laundering-regulations-risk-assessments] Failed primary-source search note: searches for an official UK source prescribing fixed percentage weights such as 35/30/25/10 returned only general factor-based guidance, not an authoritative UK rule requiring any particular weighting split.

#### C. Public evidence on effectiveness and limitations

- [fact; source: https://www.nationalcrimeagency.gov.uk/who-we-are/publications/747-sars-annual-report-2024/file] The UK Financial Intelligence Unit (UKFIU) SARs Annual Report 2024 records 872,048 SARs submitted in 2023-2024 and reports that sectors and their supervisors must judge whether report volumes are proportionate to risk, but it does not publish any linkage between customer onboarding risk bands and later SAR outcomes.
- [fact; source: https://www.nationalcrimeagency.gov.uk/who-we-are/publications/747-sars-annual-report-2024/file] The same report records 74,431 Defence Against Money Laundering (DAML) requests in 2023-2024 versus 57,081 in 2022-2023, which again provides regime-level outcome data rather than customer-risk-rating validation data.
- [fact; source: https://financialcrimeacademy.org/customer-risk-rating-models/] Financial Crime Academy says deterministic customer risk scores are often inaccurate, miss some high-risk customers, and misclassify many low-risk customers as high-risk, which increases review cost and dilutes anti-money laundering (AML) team efficiency.
- [fact; source: https://www.ey.com/en_ch/disrupting-financial-crime/how-do-you-successfully-operationalize-your-client-risk-rating-model] EY states that firms often struggle with inaccurate ratings and increased operational effort when they operationalize CRR models, and it emphasizes testing and calibration rather than blind reliance on initial weights.
- [fact; source: https://www.bis.org/bcbs/publ/d353.pdf] Basel guidance says banks should develop customer risk profiles that reflect the purpose and nature of the relationship, expected activity, transaction type, and where necessary sources of funds, then update those risk assessments as significant information about customer activity or behavior emerges.
- [fact; source: https://www.bis.org/bcbs/publ/d353.pdf] Basel also says ongoing monitoring is essential because a bank can only manage risk if it understands customers' normal activity well enough to identify unusual transactions outside that pattern.
- [inference; source: https://www.bis.org/bcbs/publ/d353.pdf; https://financialcrimeacademy.org/customer-risk-rating-models/] A one-time deterministic onboarding score is therefore insufficient on its own, because authoritative banking guidance expects risk profiles to evolve as behavior and transaction patterns become visible.
- [fact; source: https://arxiv.org/abs/2201.04207] Jensen et al. review the AML literature and conclude that client risk profiling is largely diagnostic while suspicious-behavior flagging still relies heavily on hand-crafted indices and non-disclosed features, and they identify the lack of public datasets as a major barrier to stronger evidence and benchmarking.
- [fact; source: https://bura.brunel.ac.uk/bitstream/2438/25258/1/FullText.pdf] Canhoto finds that the unavailability of high-quality, large training datasets on money laundering methods leaves limited scope for supervised ML, while unsupervised and reinforced methods are more feasible for modeling unusual behavior rather than confirmed laundering.
- [fact; source: https://arxiv.org/abs/1608.00708] Savage et al. show that supervised learning can detect suspicious activity with low false positives in group-behavior analysis, but their successful setting is networked transaction behavior rather than a simple deterministic onboarding score.
- [fact; source: https://arxiv.org/abs/2201.04207; https://bura.brunel.ac.uk/bitstream/2438/25258/1/FullText.pdf] Failed primary-source search note: searches for public UK evidence linking deterministic customer-risk bands directly to SAR filings, DAML outcomes, or investigation results did not surface an official dataset or peer-reviewed study with that exact linkage.

#### D. Hybrid and ML-enhanced alternatives

- [fact; source: https://financialcrimeacademy.org/customer-risk-rating-models/] Financial Crime Academy says leading institutions are simplifying model architecture, improving data quality, introducing statistical analysis alongside expert judgment, continuously updating customer profiles, and adding ML or network-science tools.
- [fact; source: https://www.ey.com/en_ch/disrupting-financial-crime/how-do-you-successfully-operationalize-your-client-risk-rating-model] EY says firms often combine weighted scoring with automatic high-risk triggers, transaction behavior, and calibration work, which means real-world CRR practice already mixes deterministic and non-deterministic elements.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-24-ai-agent-regulation-global-financial-services.md] The completed repository item on finance-sector AI regulation found that explainability, auditability, robustness, and human oversight recur across multiple financial-services regulatory frameworks.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-24-ai-agent-regulation-global-financial-services.md; https://bura.brunel.ac.uk/bitstream/2438/25258/1/FullText.pdf; https://arxiv.org/abs/2201.04207] Those recurring governance expectations make full black-box replacement of deterministic CRR harder to defend than a hybrid approach that preserves an interpretable base score and overlays behavior, statistics, or network signals.
- [inference; source: https://arxiv.org/abs/1608.00708; https://bura.brunel.ac.uk/bitstream/2438/25258/1/FullText.pdf] The public evidence reviewed here suggests ML is strongest when it learns from richer behavioral or network data than a static onboarding questionnaire can provide, which makes hybrid architectures more plausible than pure supervised replacement for customer onboarding risk scoring.

### §3 Reasoning

- [fact; source: https://www.legislation.gov.uk/uksi/2017/692/regulation/18; https://www.legislation.gov.uk/uksi/2017/692/regulation/28] The statutory test is whether a firm's method is proportionate, documented, and capable of supporting appropriate due-diligence measures, not whether it uses a particular scoring formula.
- [inference; source: https://www.gov.uk/guidance/money-laundering-regulations-risk-assessments; https://www.ey.com/en_ch/disrupting-financial-crime/how-do-you-successfully-operationalize-your-client-risk-rating-model] Deterministic weighted CRR is therefore legally acceptable as a method class, because it converts the regulation's factor categories into a documented decision process that can be explained and reviewed.
- [inference; source: https://www.nationalcrimeagency.gov.uk/who-we-are/publications/747-sars-annual-report-2024/file; https://arxiv.org/abs/2201.04207] Effectiveness is a different question from legal acceptability, and the public evidence on effectiveness is weak because accessible sources do not connect onboarding scores to later suspicious outcomes.
- [inference; source: https://www.bis.org/bcbs/publ/d353.pdf; https://financialcrimeacademy.org/customer-risk-rating-models/] Static deterministic models underperform once customer behavior changes or risk-factor interactions matter, because authoritative banking guidance expects profiles to update and practitioner evidence says stale profiles drive misclassification and cost.
- [inference; source: https://bura.brunel.ac.uk/bitstream/2438/25258/1/FullText.pdf; https://arxiv.org/abs/1608.00708; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-24-ai-agent-regulation-global-financial-services.md] Hybrid models are the most defensible next step because they can preserve an explainable baseline while using richer data where ML is actually effective.

### §4 Consistency Check

- [fact; source: https://www.legislation.gov.uk/uksi/2017/692/regulation/18; https://www.gov.uk/guidance/money-laundering-regulations-risk-assessments] There is no contradiction between the legal text and the conclusion that methodology is flexible, because both the statute and GOV.UK guidance emphasize relevant factor classes and proportionality rather than a mandated scoring recipe.
- [fact; source: https://www.bis.org/bcbs/publ/d353.pdf; https://financialcrimeacademy.org/customer-risk-rating-models/] There is no contradiction between deterministic CRR being useful and it being limited, because the sources consistently distinguish initial profiling from the later need for ongoing monitoring and profile updates.
- [inference; source: https://arxiv.org/abs/2201.04207; https://bura.brunel.ac.uk/bitstream/2438/25258/1/FullText.pdf] The main unresolved gap is not conceptual but evidential, because the literature reviewed here provides strong reasons to question static scoring yet limited public proof about exact incremental gains from one model architecture over another in UK onboarding use cases.

### §5 Depth and Breadth Expansion

- [inference; source: https://www.bis.org/bcbs/publ/d353.pdf; https://www.fca.org.uk/publications/thematic-reviews/tr19-4-understanding-money-laundering-risks-capital-markets] **Technical lens:** the strongest technical argument against a purely deterministic model is not that it is simple, but that simplicity becomes brittle when the control objective requires learning what "normal" activity looks like over time.
- [inference; source: https://www.legislation.gov.uk/uksi/2017/692/regulation/28; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-24-ai-agent-regulation-global-financial-services.md] **Regulatory lens:** the deeper supervisory concern is evidencing why the chosen method remains appropriate, so governance, recalibration, and explainability matter as much as raw scoring logic.
- [inference; source: https://financialcrimeacademy.org/customer-risk-rating-models; https://www.ey.com/en_ch/disrupting-financial-crime/how-do-you-successfully-operationalize-your-client-risk-rating-model] **Economic lens:** stale deterministic scoring creates operational drag through false positives and repeated review work, which is why firms try to simplify factor sets, repair data quality, and add more predictive signals.
- [inference; source: https://www.gov.uk/guidance/money-laundering-regulations-your-responsibilities; https://financialcrimeacademy.org/customer-risk-rating-models] **Behavioral and inclusion lens:** if firms respond to uncertainty by over-weighting coarse proxies such as geography or customer category, deterministic models can support defensive over-classification and contribute to de-risking rather than proportionate treatment.

### §6 Synthesis

*(This section seeds the Findings below.)*

**Executive summary:**

- [inference; source: https://www.legislation.gov.uk/uksi/2017/692/regulation/18; https://www.legislation.gov.uk/uksi/2017/692/regulation/28; https://www.gov.uk/guidance/money-laundering-regulations-risk-assessments] Deterministic weighted customer risk rating models are legally compatible with MLR 2017 because they can operationalize the required factor-based, proportionate assessment, but the law does not require fixed weights or a single four-factor formula.
- [inference; source: https://www.fca.org.uk/publications/thematic-reviews/tr19-4-understanding-money-laundering-risks-capital-markets; https://www.bis.org/bcbs/publ/d353.pdf] Their strongest advantage is regulatory defensibility, because they are easier to explain, document, and test than opaque models.
- [inference; source: https://www.nationalcrimeagency.gov.uk/who-we-are/publications/747-sars-annual-report-2024/file; https://arxiv.org/abs/2201.04207] Their weakest point is outcome validation, because public UK sources do not show that deterministic onboarding bands reliably predict suspicious activity outcomes.
- [inference; source: https://bura.brunel.ac.uk/bitstream/2438/25258/1/FullText.pdf; https://arxiv.org/abs/1608.00708; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-24-ai-agent-regulation-global-financial-services.md] Hybrid models are the best-supported next step because they preserve interpretable controls while adding behavioral or network signals in the areas where ML appears to add real value.

**Key findings:**

1. [inference] Deterministic weighted CRR models fit the legal shape of MLR 2017 because Regulation 18 and Regulation 28 require firms to assess customer, geography, product or service, transaction, and delivery-channel risks proportionately, but they do not prescribe a mandatory numeric weighting formula. (high confidence; source: https://www.legislation.gov.uk/uksi/2017/692/regulation/18; https://www.legislation.gov.uk/uksi/2017/692/regulation/28; https://www.gov.uk/guidance/money-laundering-regulations-risk-assessments)
2. [inference] The main regulatory strength of deterministic CRR is auditability, because firms can show which factors, points, overrides, and thresholds produced a rating and then connect that rating to standard, enhanced, or simplified due-diligence decisions. (high confidence; source: https://www.ey.com/en_ch/disrupting-financial-crime/how-do-you-successfully-operationalize-your-client-risk-rating-model; https://www.fca.org.uk/publications/thematic-reviews/tr19-4-understanding-money-laundering-risks-capital-markets; https://www.legislation.gov.uk/uksi/2017/692/regulation/28)
3. [fact] Published practitioner descriptions show that real CRR models are usually point-based or weighted systems with factor-specific weights and automatic high-risk triggers rather than purely discretionary narratives, but the exact mechanics vary materially by institution. (medium confidence; source: https://www.ey.com/en_ch/disrupting-financial-crime/how-do-you-successfully-operationalize-your-client-risk-rating-model; https://financialcrimeacademy.org/customer-risk-rating-models/)
4. [inference] Static deterministic CRR models are vulnerable to stale data, cross-business inconsistency, and missed interactions between factors, which means they tend to drift away from actual risk unless firms recalibrate them and update profiles continuously. (medium confidence; source: https://financialcrimeacademy.org/customer-risk-rating-models/; https://www.bis.org/bcbs/publ/d353.pdf)
5. [inference] Publicly accessible UK evidence supports deterministic CRR as a process control, but it does not validate deterministic customer-risk bands against SAR or investigation outcomes, so claims of predictive effectiveness remain materially under-evidenced. (medium confidence; source: https://www.nationalcrimeagency.gov.uk/who-we-are/publications/747-sars-annual-report-2024/file; https://arxiv.org/abs/2201.04207)
6. [fact] Open-access AML research indicates that supervised ML is constrained by the scarcity of high-quality labeled laundering datasets, while unsupervised, reinforced, and network-oriented methods are more feasible for detecting unusual behavior than for replacing onboarding scores outright. (medium confidence; source: https://bura.brunel.ac.uk/bitstream/2438/25258/1/FullText.pdf; https://arxiv.org/abs/2201.04207; https://arxiv.org/abs/1608.00708)
7. [inference] Basel guidance pushes firms beyond one-time deterministic scoring because it expects customer risk profiles to incorporate intended relationship purpose, expected activity, behavior over time, and ongoing monitoring, all of which reward dynamic rather than static models. (high confidence; source: https://www.bis.org/bcbs/publ/d353.pdf; https://www.gov.uk/guidance/money-laundering-regulations-your-responsibilities)
8. [inference] Hybrid models that keep an interpretable deterministic backbone and add behavioral, statistical, or network overlays are the most regulator-friendly improvement path because they address static-model weaknesses without abandoning explainability, auditability, or human oversight. (medium confidence; source: https://www.ey.com/en_ch/disrupting-financial-crime/how-do-you-successfully-operationalize-your-client-risk-rating-model; https://bura.brunel.ac.uk/bitstream/2438/25258/1/FullText.pdf; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-24-ai-agent-regulation-global-financial-services.md)

**Evidence map:**

- Claim 1: [inference] Deterministic weighted CRR fits the legal factor taxonomy, but fixed numeric weights are not mandated. | Source: https://www.legislation.gov.uk/uksi/2017/692/regulation/18 ; https://www.legislation.gov.uk/uksi/2017/692/regulation/28 ; https://www.gov.uk/guidance/money-laundering-regulations-risk-assessments | Confidence: high | Notes: legal-fit finding
- Claim 2: [inference] Deterministic CRR's strongest advantage is auditability and traceable due-diligence routing. | Source: https://www.ey.com/en_ch/disrupting-financial-crime/how-do-you-successfully-operationalize-your-client-risk-rating-model ; https://www.fca.org.uk/publications/thematic-reviews/tr19-4-understanding-money-laundering-risks-capital-markets ; https://www.legislation.gov.uk/uksi/2017/692/regulation/28 | Confidence: high | Notes: defensibility finding
- Claim 3: [fact] Real-world CRR models are typically weighted or point-based with overrides, not purely narrative. | Source: https://www.ey.com/en_ch/disrupting-financial-crime/how-do-you-successfully-operationalize-your-client-risk-rating-model ; https://financialcrimeacademy.org/customer-risk-rating-models/ | Confidence: medium | Notes: practitioner evidence
- Claim 4: [inference] Static deterministic models drift without recalibration and profile updates. | Source: https://financialcrimeacademy.org/customer-risk-rating-models/ ; https://www.bis.org/bcbs/publ/d353.pdf | Confidence: medium | Notes: operational limitation
- Claim 5: [inference] Public UK evidence does not validate deterministic CRR against suspicious outcomes. | Source: https://www.nationalcrimeagency.gov.uk/who-we-are/publications/747-sars-annual-report-2024/file ; https://arxiv.org/abs/2201.04207 | Confidence: medium | Notes: evidence gap
- Claim 6: [fact] Open literature limits supervised ML for AML because labeled data are weak and scarce. | Source: https://bura.brunel.ac.uk/bitstream/2438/25258/1/FullText.pdf ; https://arxiv.org/abs/2201.04207 ; https://arxiv.org/abs/1608.00708 | Confidence: medium | Notes: data-availability constraint
- Claim 7: [inference] Basel expectations make static one-time scoring insufficient on their own. | Source: https://www.bis.org/bcbs/publ/d353.pdf ; https://www.gov.uk/guidance/money-laundering-regulations-your-responsibilities | Confidence: high | Notes: dynamic-profile expectation
- Claim 8: [inference] Hybrid models are the best-supported improvement path under current governance expectations. | Source: https://www.ey.com/en_ch/disrupting-financial-crime/how-do-you-successfully-operationalize-your-client-risk-rating-model ; https://bura.brunel.ac.uk/bitstream/2438/25258/1/FullText.pdf ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-24-ai-agent-regulation-global-financial-services.md | Confidence: medium | Notes: synthesis finding

**Assumptions:**

- [assumption] The inaccessible current JMLSG text is directionally consistent with the accessible UK legal and supervisory sources reviewed here on factor-based, proportionate risk assessment. Justification: the current official JMLSG entry point remained the authoritative starting point, but the core legal obligations were directly available from Regulation 18, Regulation 28, GOV.UK guidance, and FCA material.
- [assumption] Public absence of UK score-to-SAR validation evidence means an evidence gap, not proof that firms never perform private validation internally. Justification: banks may hold internal validation studies that are not published.

**Analysis:**

- [fact; source: https://www.legislation.gov.uk/uksi/2017/692/regulation/18; https://www.legislation.gov.uk/uksi/2017/692/regulation/28; https://www.gov.uk/guidance/money-laundering-regulations-risk-assessments] Legal fit was weighted most heavily toward primary UK statutory and government guidance, which consistently require relevant factor classes, proportionality, and demonstrable appropriateness.
- [inference; source: https://www.legislation.gov.uk/uksi/2017/692/regulation/18; https://www.ey.com/en_ch/disrupting-financial-crime/how-do-you-successfully-operationalize-your-client-risk-rating-model] Because those sources do not prescribe exact percentages, practitioner descriptions of weighted CRR mechanics were treated as evidence of common implementation practice rather than evidence of mandatory UK law.
- [inference; source: https://www.nationalcrimeagency.gov.uk/who-we-are/publications/747-sars-annual-report-2024/file; https://arxiv.org/abs/2201.04207; https://bura.brunel.ac.uk/bitstream/2438/25258/1/FullText.pdf] Effectiveness was weighted separately from legal fit, and on that dimension the accessible evidence was notably weaker because regime-level SAR data and open literature highlight data scarcity and process issues more than direct validation of deterministic onboarding scores.
- [inference; source: https://www.bis.org/bcbs/publ/d353.pdf; https://arxiv.org/abs/1608.00708; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-24-ai-agent-regulation-global-financial-services.md] The resulting trade-off is clear: deterministic models remain easier to defend and govern, but hybrid models are better positioned to improve accuracy where richer behavioral data exist without losing the explainability that supervisors still expect.

**Risks, gaps, uncertainties:**

- [inference; source: https://www.nationalcrimeagency.gov.uk/who-we-are/publications/747-sars-annual-report-2024/file] Public UK outcome data are aggregated at regime level, so this item cannot verify whether high-risk CRR bands actually correlate with more valuable SAR or DAML outcomes.
- [inference; source: https://financialcrimeacademy.org/customer-risk-rating-models/; https://www.ey.com/en_ch/disrupting-financial-crime/how-do-you-successfully-operationalize-your-client-risk-rating-model] The detailed practitioner claims about false-positive reduction and better calibration are directionally useful but are not independently replicated here with an open UK bank dataset.
- [inference; source: https://bura.brunel.ac.uk/bitstream/2438/25258/1/FullText.pdf; https://arxiv.org/abs/2201.04207] Most open ML literature reviewed here addresses transaction or network behavior more directly than onboarding CRR, so claims about full ML replacement for onboarding remain lower-confidence than claims about behavior overlays.

**Open questions:**

- What internal validation metrics do UK firms actually use to test whether customer-risk bands predict later suspicious activity?
- Which hybrid governance pattern best preserves explainability when a behavioral overlay disagrees with a deterministic base score?
- Will future FCA, HMRC, or JMLSG guidance become more explicit about acceptable use of ML within customer risk-rating models?

### §7 Recursive Review

- [fact; source: https://www.legislation.gov.uk/uksi/2017/692/regulation/18; https://www.legislation.gov.uk/uksi/2017/692/regulation/28; https://www.bis.org/bcbs/publ/d353.pdf] All legal-fit conclusions in this item remain anchored to primary or official sources rather than to practitioner examples alone.
- [fact; source: https://www.nationalcrimeagency.gov.uk/who-we-are/publications/747-sars-annual-report-2024/file; https://arxiv.org/abs/2201.04207; https://bura.brunel.ac.uk/bitstream/2438/25258/1/FullText.pdf] All weaker claims were kept at medium confidence because outcome-validation evidence is thin and direct public data for customer-risk-band performance were not found.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-24-ai-agent-regulation-global-financial-services.md] Repository cross-reference was applied where governance findings touched explainability and auditability expectations already established in prior completed work.
- [inference; source: https://www.legislation.gov.uk/uksi/2017/692/regulation/18; https://www.bis.org/bcbs/publ/d353.pdf; https://arxiv.org/abs/2201.04207] The overall confidence remains medium because the normative baseline is strong, but the public empirical case for deterministic onboarding scores versus hybrids remains incomplete.

---

## Findings

### Executive Summary

Deterministic weighted customer risk rating (CRR) models are a legally defensible but only partially validated way to implement the Money Laundering Regulations 2017 (MLR 2017) risk-based approach, because the regulations require proportionate factor-based assessment but do not require fixed weights or prove that static scores predict suspicious outcomes. [inference; source: https://www.legislation.gov.uk/uksi/2017/692/regulation/18; https://www.legislation.gov.uk/uksi/2017/692/regulation/28; https://www.gov.uk/guidance/money-laundering-regulations-risk-assessments; https://www.nationalcrimeagency.gov.uk/who-we-are/publications/747-sars-annual-report-2024/file]

Their main advantage is auditability: firms can explain which customer, geography, product or service, and delivery-channel inputs drove a risk rating and then show why that rating led to standard or enhanced customer due diligence (CDD). [inference; source: https://www.ey.com/en_ch/disrupting-financial-crime/how-do-you-successfully-operationalize-your-client-risk-rating-model; https://www.fca.org.uk/publications/thematic-reviews/tr19-4-understanding-money-laundering-risks-capital-markets; https://www.legislation.gov.uk/uksi/2017/692/regulation/28]

Their main weakness is that public evidence reviewed here does not connect onboarding risk bands to suspicious activity report (SAR) or investigation outcomes, while both practitioner and banking-governance sources point to stale data, inconsistent factors, and missing behavioral context as recurring failure modes. [inference; source: https://www.nationalcrimeagency.gov.uk/who-we-are/publications/747-sars-annual-report-2024/file; https://financialcrimeacademy.org/customer-risk-rating-models/; https://www.bis.org/bcbs/publ/d353.pdf]

Hybrid models that keep an interpretable deterministic backbone and add behavioral, statistical, or network overlays are the best-supported improvement path, because open literature shows machine learning (ML) is more credible on richer behavioral data than on sparse labeled onboarding data, while prior finance-sector governance research still points toward explainability and human oversight as non-negotiable controls. [inference; source: https://bura.brunel.ac.uk/bitstream/2438/25258/1/FullText.pdf; https://arxiv.org/abs/1608.00708; https://arxiv.org/abs/2201.04207; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-24-ai-agent-regulation-global-financial-services.md]

### Key Findings

1. **Deterministic weighted CRR models fit the legal shape of MLR 2017 because Regulation 18 and Regulation 28 require firms to assess customer, geography, product or service, transaction, and delivery-channel risks proportionately, but they do not prescribe a mandatory numeric weighting formula.** ([inference]; high confidence; source: https://www.legislation.gov.uk/uksi/2017/692/regulation/18; https://www.legislation.gov.uk/uksi/2017/692/regulation/28; https://www.gov.uk/guidance/money-laundering-regulations-risk-assessments)
2. **The main regulatory strength of deterministic CRR is auditability, because firms can show which factors, points, overrides, and thresholds produced a rating and then connect that rating to standard, enhanced, or simplified due-diligence decisions.** ([inference]; high confidence; source: https://www.ey.com/en_ch/disrupting-financial-crime/how-do-you-successfully-operationalize-your-client-risk-rating-model; https://www.fca.org.uk/publications/thematic-reviews/tr19-4-understanding-money-laundering-risks-capital-markets; https://www.legislation.gov.uk/uksi/2017/692/regulation/28)
3. **Published practitioner descriptions show that real CRR models are usually point-based or weighted systems with factor-specific weights and automatic high-risk triggers rather than purely discretionary narratives, but the exact mechanics vary materially by institution.** ([fact]; medium confidence; source: https://www.ey.com/en_ch/disrupting-financial-crime/how-do-you-successfully-operationalize-your-client-risk-rating-model; https://financialcrimeacademy.org/customer-risk-rating-models/)
4. **Static deterministic CRR models are vulnerable to stale data, cross-business inconsistency, and missed interactions between factors, which means they tend to drift away from actual risk unless firms recalibrate them and update profiles continuously.** ([inference]; medium confidence; source: https://financialcrimeacademy.org/customer-risk-rating-models/; https://www.bis.org/bcbs/publ/d353.pdf)
5. **Publicly accessible UK evidence supports deterministic CRR as a process control, but it does not validate deterministic customer-risk bands against SAR or investigation outcomes, so claims of predictive effectiveness remain materially under-evidenced.** ([inference]; medium confidence; source: https://www.nationalcrimeagency.gov.uk/who-we-are/publications/747-sars-annual-report-2024/file; https://arxiv.org/abs/2201.04207)
6. **Open-access AML research indicates that supervised ML is constrained by the scarcity of high-quality labeled laundering datasets, while unsupervised, reinforced, and network-oriented methods are more feasible for detecting unusual behavior than for replacing onboarding scores outright.** ([fact]; medium confidence; source: https://bura.brunel.ac.uk/bitstream/2438/25258/1/FullText.pdf; https://arxiv.org/abs/2201.04207; https://arxiv.org/abs/1608.00708)
7. **Basel guidance pushes firms beyond one-time deterministic scoring because it expects customer risk profiles to incorporate intended relationship purpose, expected activity, behavior over time, and ongoing monitoring, all of which reward dynamic rather than static models.** ([inference]; high confidence; source: https://www.bis.org/bcbs/publ/d353.pdf; https://www.gov.uk/guidance/money-laundering-regulations-your-responsibilities)
8. **Hybrid models that keep an interpretable deterministic backbone and add behavioral, statistical, or network overlays are the most regulator-friendly improvement path because they address static-model weaknesses without abandoning explainability, auditability, or human oversight.** ([inference]; medium confidence; source: https://www.ey.com/en_ch/disrupting-financial-crime/how-do-you-successfully-operationalize-your-client-risk-rating-model; https://bura.brunel.ac.uk/bitstream/2438/25258/1/FullText.pdf; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-24-ai-agent-regulation-global-financial-services.md)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Deterministic weighted CRR fits the legal factor taxonomy, but fixed numeric weights are not mandated. | https://www.legislation.gov.uk/uksi/2017/692/regulation/18 ; https://www.legislation.gov.uk/uksi/2017/692/regulation/28 ; https://www.gov.uk/guidance/money-laundering-regulations-risk-assessments | high | legal-fit finding |
| [inference] Deterministic CRR's strongest advantage is auditability and traceable due-diligence routing. | https://www.ey.com/en_ch/disrupting-financial-crime/how-do-you-successfully-operationalize-your-client-risk-rating-model ; https://www.fca.org.uk/publications/thematic-reviews/tr19-4-understanding-money-laundering-risks-capital-markets ; https://www.legislation.gov.uk/uksi/2017/692/regulation/28 | high | defensibility finding |
| [fact] Real-world CRR models are typically weighted or point-based with overrides, not purely narrative. | https://www.ey.com/en_ch/disrupting-financial-crime/how-do-you-successfully-operationalize-your-client-risk-rating-model ; https://financialcrimeacademy.org/customer-risk-rating-models/ | medium | practitioner evidence |
| [inference] Static deterministic models drift without recalibration and profile updates. | https://financialcrimeacademy.org/customer-risk-rating-models/ ; https://www.bis.org/bcbs/publ/d353.pdf | medium | operational limitation |
| [inference] Public UK evidence does not validate deterministic CRR against suspicious outcomes. | https://www.nationalcrimeagency.gov.uk/who-we-are/publications/747-sars-annual-report-2024/file ; https://arxiv.org/abs/2201.04207 | medium | evidence gap |
| [fact] Open literature limits supervised ML for AML because labeled data are weak and scarce. | https://bura.brunel.ac.uk/bitstream/2438/25258/1/FullText.pdf ; https://arxiv.org/abs/2201.04207 ; https://arxiv.org/abs/1608.00708 | medium | data-availability constraint |
| [inference] Basel expectations make static one-time scoring insufficient on their own. | https://www.bis.org/bcbs/publ/d353.pdf ; https://www.gov.uk/guidance/money-laundering-regulations-your-responsibilities | high | dynamic-profile expectation |
| [inference] Hybrid models are the best-supported improvement path under current governance expectations. | https://www.ey.com/en_ch/disrupting-financial-crime/how-do-you-successfully-operationalize-your-client-risk-rating-model ; https://bura.brunel.ac.uk/bitstream/2438/25258/1/FullText.pdf ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-24-ai-agent-regulation-global-financial-services.md | medium | synthesis finding |

### Assumptions

- Deterministic CRR design conventions described by EY and Financial Crime Academy are broadly representative of mainstream bank practice rather than outlier implementations. [assumption; source: https://www.ey.com/en_ch/disrupting-financial-crime/how-do-you-successfully-operationalize-your-client-risk-rating-model; https://financialcrimeacademy.org/customer-risk-rating-models/]
- Public absence of UK score-to-SAR validation evidence reflects an evidence gap in open sources, not proof that private firms never validate their models internally. [assumption; source: https://www.nationalcrimeagency.gov.uk/who-we-are/publications/747-sars-annual-report-2024/file; https://arxiv.org/abs/2201.04207]

### Analysis

The legal and supervisory question was answered primarily from UK statutory text and official guidance, because those sources directly define what counts as an acceptable risk-based approach under MLR 2017. [fact; source: https://www.legislation.gov.uk/uksi/2017/692/regulation/18; https://www.legislation.gov.uk/uksi/2017/692/regulation/28; https://www.gov.uk/guidance/money-laundering-regulations-risk-assessments]

Those sources consistently support factor-based, proportionate, documented decision-making, but they do not require a fixed weight split, which means practitioner evidence on weighted or point-based CRR mechanics was used only to describe common implementation patterns rather than to infer legal obligation. [inference; source: https://www.legislation.gov.uk/uksi/2017/692/regulation/18; https://www.ey.com/en_ch/disrupting-financial-crime/how-do-you-successfully-operationalize-your-client-risk-rating-model]

Effectiveness had to be judged on weaker public evidence, because the UKFIU publishes aggregate SAR and DAML outcomes rather than customer-risk-band validation, while open AML literature emphasizes sparse labeled datasets, interpretability, and data-quality limits more than direct benchmarking of deterministic onboarding scores. [inference; source: https://www.nationalcrimeagency.gov.uk/who-we-are/publications/747-sars-annual-report-2024/file; https://arxiv.org/abs/2201.04207; https://bura.brunel.ac.uk/bitstream/2438/25258/1/FullText.pdf]

That evidence pattern supports a split conclusion: deterministic models remain strong on explainability and supervisory defensibility, but hybrid models offer a better balance once firms want more adaptive risk detection without giving up auditable logic or human accountability. [inference; source: https://www.bis.org/bcbs/publ/d353.pdf; https://arxiv.org/abs/1608.00708; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-24-ai-agent-regulation-global-financial-services.md]

### Risks, Gaps, and Uncertainties

- Public UK data reviewed here do not show whether high-risk CRR bands actually produce more valuable SAR or DAML outcomes than lower-risk bands. [inference; source: https://www.nationalcrimeagency.gov.uk/who-we-are/publications/747-sars-annual-report-2024/file]
- The open-access literature reviewed here is stronger on transaction or network analytics than on pure onboarding CRR, so claims about full ML replacement remain less certain than claims about behavior overlays. [inference; source: https://arxiv.org/abs/1608.00708; https://arxiv.org/abs/2201.04207; https://bura.brunel.ac.uk/bitstream/2438/25258/1/FullText.pdf]
- Publicly accessible primary UK sources reviewed here do not prescribe exact factor weights, so conclusions about detailed weighting conventions rely more on accessible law, regulator material, and practitioner descriptions than on directly quoted JMLSG Chapter 4 wording. [inference; source: https://www.legislation.gov.uk/uksi/2017/692/regulation/18; https://www.gov.uk/guidance/money-laundering-regulations-risk-assessments; https://www.ey.com/en_ch/disrupting-financial-crime/how-do-you-successfully-operationalize-your-client-risk-rating-model]

### Open Questions

- What internal validation metrics do UK firms actually use to test whether customer-risk bands predict later suspicious activity?
- Which hybrid governance pattern best preserves explainability when a behavioral overlay disagrees with a deterministic base score?
- Will future FCA, HM Revenue & Customs, or JMLSG guidance become more explicit about acceptable use of ML inside customer risk-rating models?

---

## Output

- Type: knowledge
- Description: Research note concluding that deterministic weighted CRR remains legally defensible under MLR 2017 but is only weakly validated in public outcome data, with hybrid models offering the strongest improvement path.
- Links:
  - https://www.legislation.gov.uk/uksi/2017/692/regulation/18
  - https://www.legislation.gov.uk/uksi/2017/692/regulation/28
  - https://www.bis.org/bcbs/publ/d353.pdf
