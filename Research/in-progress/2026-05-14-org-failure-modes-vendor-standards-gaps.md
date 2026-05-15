---
title: "Organisational failure modes: vendor non-compliance with or absence of implementation standards"
added: 2026-05-14T18:48:56+00:00
status: reviewing
priority: high  # low | medium | high
blocks: []
tags: [organisation, organisational-design, governance, vendor-management, technical-debt]
started: 2026-05-15T03:53:08+00:00
completed: ~
output: [knowledge]
cites: [2026-05-14-org-failure-modes-accountability-gaps, 2026-05-14-org-failure-modes-split-risk-cost-benefits-accountability]
related: [2026-05-14-org-failure-modes-cohort-demand-domain-it, 2026-05-14-org-failure-modes-project-demand-product-it]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Organisational failure modes: vendor non-compliance with or absence of implementation standards

## Research Question

What failure modes have been empirically observed in organisations where vendors do not comply with established implementation standards, or where implementation standards are absent or insufficiently defined?

## Scope

**In scope:**
- Empirically documented failure modes arising when third-party vendors deliver solutions that deviate from organisational implementation standards (e.g., integration patterns, security baselines, data contracts, coding standards)
- Failure modes arising when no implementation standards exist and vendors therefore operate with unconstrained discretion
- Both scenarios: (a) standards exist but are not enforced; (b) standards are never written
- Observable symptoms: integration failures, security incidents, runaway technical debt, shadow systems, increased support cost, vendor lock-in, difficult decommissioning
- Evidence from enterprise IT governance, outsourcing, and multi-vendor environments

**Out of scope:**
- Failure modes solely caused by poor vendor capability unrelated to standards compliance
- Regulatory compliance standards (e.g., PCI DSS, GDPR) unless the failure mode maps to an IT implementation standard gap
- Prescriptive standards-writing templates without empirical failure-mode grounding

**Constraints:**
- Prefer empirical sources (case studies, audit findings, industry surveys) over vendor promotional material
- Every source must include a verifiable URL
- Acronyms expanded on first use throughout

## Context

- Vendors become a governance risk surface when implementation standards are missing, vague, or unenforced, because each supplier can optimize for its local contract while the buyer absorbs the resulting integration, security, and exit costs. [inference; source: https://www.nao.org.uk/reports/government-shared-services/; https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-134.html; https://qa.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Auditors-Office/Audit-Services/Audit-Reports/Information-Technology-Vendor-Management]

## Approach

1. Define what "implementation standards" means in an IT delivery context (e.g., API (Application Programming Interface) design standards, security baselines, data model conventions, infrastructure-as-code patterns) and distinguish the "no standards" from the "standards exist but unenforced" scenario.
2. Search for empirical evidence of failure modes, including post-mortems, audit reports, and industry surveys, attributable to vendor non-compliance or absent standards.
3. Identify the most commonly reported failure modes and categorise them by type (integration, security, operational, cost, delivery).
4. Examine whether failure severity varies by vendor engagement model (staff augmentation, managed service, SaaS (Software as a Service), bespoke build).
5. Review empirically supported governance mechanisms (e.g., standards registers, compliance gates, contract clauses, architectural review boards) and evidence for their effectiveness.

## Sources

- [ ] [Gartner IT Vendor Risk Management](https://www.gartner.com/en/information-technology/topics/vendor-risk-management) - seeded source checked; direct access returned 403 in this session.
- [x] [National Institute of Standards and Technology (NIST) (2022) Cybersecurity Supply Chain Risk Management Practices for Systems and Organizations](https://csrc.nist.gov/publications/detail/sp/800-161/rev-1/final) - consulted for standards-body framing of supplier risk management, then supplemented with more empirical NIST case-study material.
- [ ] [Bass, Clements and Kazman (2021) Software Architecture in Practice](https://www.pearson.com/en-us/subject-catalog/p/software-architecture-in-practice/P200000000537) - seeded source checked; the public Pearson page exposed no extractable empirical evidence in this session.
- [x] [National Institute of Standards and Technology (NIST) (2020) Case Studies in Cyber Supply Chain Risk Management: Summary of Findings and Recommendations](https://www.nist.gov/publications/case-studies-cyber-supply-chain-risk-management-summary-findings-and-recommendations) - consulted for the empirical case-study base of 16 subject matter expert interviews across six companies and for the recommendations on supplier terms, criticality, and lifecycle governance.
- [x] [National Institute of Standards and Technology (NIST) (2021) NIST Shares Key Practices in Cyber Supply Chain Risk Management Based on Industry Research](https://www.nist.gov/news-events/news/2021/02/nist-shares-key-practices-cyber-supply-chain-risk-management-based) - consulted for the industry-derived practices of formal supplier governance, continuous monitoring, and full-lifecycle planning.
- [x] [Office of the Comptroller of the Currency (2020) OCC Assesses $60 Million Civil Money Penalty Against Morgan Stanley](https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-134.html) - consulted for the official enforcement findings on failed vendor oversight during decommissioning.
- [x] [City and County of Denver Auditor (2022) Information Technology Vendor Management](https://qa.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Auditors-Office/Audit-Services/Audit-Reports/Information-Technology-Vendor-Management) - consulted for audit-backed recommendations on structure, security review, performance monitoring, and vendor-separation procedures.
- [x] [National Audit Office (2022) Government shared services](https://www.nao.org.uk/reports/government-shared-services/) - consulted for evidence on standardisation goals, missing business-case discipline, weak process and data convergence, and repeated failure to realise intended benefits.
- [x] [UK Government Data Standards Authority (2024) Data Standards Authority: operational model and processes](https://www.gov.uk/government/publications/data-standards-authority-operational-model-and-processes/data-standards-authority-operational-model-and-processes) - consulted for the governance mechanisms used to set common standards, monitor compliance, and assign accountable ownership.
- [x] [Ramasubbu and Kemerer (2021) Controlling Technical Debt Remediation in Outsourced Enterprise Systems Maintenance: An Empirical Analysis](https://www.jmis-web.org/articles/1510) - consulted for the empirical link between standards violations, technical debt, outsourcing, and migration control.
- [x] [Ilori, Nwosu, and Naiho (2024) Third-party vendor risks in IT security: A comprehensive audit review and mitigation strategies](https://wjarr.com/content/third-party-vendor-risks-it-security-comprehensive-audit-review-and-mitigation-strategies) - consulted as a secondary synthesis of recurrent vendor-security failure modes and mitigation patterns.
- [x] [Research item (2026) Organisational failure modes: overlapping and absent accountability at strategic and information technology (IT) layers](https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-accountability-gaps.html) - consulted as adjacent repository evidence on missing governance owners.
- [x] [Research item (2026) Organisational failure modes: risk, operational cost, and benefits accountability in separate business units](https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-split-risk-cost-benefits-accountability.html) - consulted as adjacent repository evidence on cost externalisation and weak integrator functions.

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0-5 are the investigation; Section 6 seeds the Findings section below.)*

### §0 Initialise

Question: identify empirically observed failure modes when vendors do not comply with implementation standards, or when implementation standards are absent or too weakly defined to constrain vendor delivery.

Scope: in scope are enterprise and public-sector cases involving implementation standards for architecture, security, data, lifecycle control, and delivery governance; out of scope are generic vendor underperformance that cannot be tied to a standards gap.

Constraints: prefer audit reports, regulator actions, standards-body case studies, and empirical studies; keep all citations URL-backed; separate direct observation from structural inference; use prior completed repository items only as adjacent support, not as the sole basis for a core claim.

Output: knowledge, specifically a structured synthesis with executive summary, key findings, evidence map, assumptions, analysis, risks, gaps, uncertainties, and open questions.

Mode: full.

- [assumption; source: https://www.gartner.com/en/information-technology/topics/vendor-risk-management; https://www.pearson.com/en-us/subject-catalog/p/software-architecture-in-practice/P200000000537] Access note: the seeded Gartner page returned 403 in this session and the public Pearson page exposed no extractable empirical evidence, so the item substitutes accessible audit, regulator, and standards-body sources.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-accountability-gaps.html; https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-split-risk-cost-benefits-accountability.html] Prior completed repository work already shows that missing owners and split incentives amplify governance failure, so this item treats vendor standards as a vendor-facing control surface where that broader accountability problem becomes observable.

### §1 Question Decomposition

- **Root question:** what failure modes appear when vendor work is not bounded by clear, enforced implementation standards?
  - **A. Definitions**
    - A1. What counts as an implementation standard in this context?
    - A2. How does "no standard" differ from "standard exists but is unenforced"?
  - **B. Direct failure modes**
    - B1. What integration or interoperability failures recur?
    - B2. What security and control failures recur?
    - B3. What cost, benefit, and support failures recur?
    - B4. What technical-debt and maintainability failures recur?
    - B5. What exit, decommissioning, or transition failures recur?
  - **C. Context variation**
    - C1. How do symptoms differ across shared-service, outsourced maintenance, and managed-service arrangements?
    - C2. Which failure modes appear to require absent standards, and which require weak enforcement of existing standards?
  - **D. Remedies**
    - D1. Which governance mechanisms have the strongest empirical support?
    - D2. Which remedies remain inferential but consistent with the evidence base?

### §2 Investigation

#### 2.1 Source checks and definitional baseline

- [assumption; source: https://www.gartner.com/en/information-technology/topics/vendor-risk-management] Access note: the seeded Gartner source remained inaccessible in this session, so it is not used as evidence.
- [assumption; source: https://www.pearson.com/en-us/subject-catalog/p/software-architecture-in-practice/P200000000537] Access note: the seeded Pearson book page was reachable but did not expose extractable empirical content, so it is not used as evidence.
- [fact; source: https://www.nao.org.uk/reports/government-shared-services/] The National Audit Office states that the aim of shared services is to standardise processes and services, often by moving to a common information technology system or operating platform, so that delivery becomes consistent and repeatable at scale.
- [fact; source: https://www.nist.gov/news-events/news/2021/02/nist-shares-key-practices-cyber-supply-chain-risk-management-based] NIST's industry-derived key practices include establishing a formal Cyber Supply Chain Risk Management (C-SCRM) program, knowing and managing critical suppliers, assessing and monitoring throughout the supplier relationship, and planning for the full life cycle.
- [fact; source: https://qa.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Auditors-Office/Audit-Services/Audit-Reports/Information-Technology-Vendor-Management] Denver's 2022 audit recommendations require an approved vendor-management structure, contract-compliance monitoring, annual or better security review, a single system of record, and vendor-separation procedures.
- [inference; source: https://www.nao.org.uk/reports/government-shared-services/; https://www.nist.gov/news-events/news/2021/02/nist-shares-key-practices-cyber-supply-chain-risk-management-based; https://qa.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Auditors-Office/Audit-Services/Audit-Reports/Information-Technology-Vendor-Management] For this item, implementation standards are the explicit architecture, data, security, monitoring, and exit rules that let the buyer constrain vendor discretion over how a solution is built, integrated, operated, and retired.

#### 2.2 Failure modes when standards are absent or under-specified

- [fact; source: https://www.nao.org.uk/reports/government-shared-services/] The National Audit Office concluded that the government's previous shared-services strategies failed to deliver their intended cost savings and other benefits.
- [fact; source: https://www.nao.org.uk/reports/government-shared-services/] The same report says it is difficult to judge progress on enabling conditions such as process and data convergence.
- [fact; source: https://www.nao.org.uk/reports/government-shared-services/] The National Audit Office found that the Cabinet Office launched the current strategy with a case for change rather than a detailed business case, and that the central benefits database contained narrative descriptions rather than measured savings figures.
- [inference; source: https://www.nao.org.uk/reports/government-shared-services/; https://www.gov.uk/government/publications/data-standards-authority-operational-model-and-processes/data-standards-authority-operational-model-and-processes] Absent or weakly defined standards let vendors and departments optimize locally, which leaves interoperability, process convergence, and measurable benefits unproven even when the overall program is nominally about standardisation.

#### 2.3 Failure modes when standards exist but enforcement is weak

- [fact; source: https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-134.html] The Office of the Comptroller of the Currency found that Morgan Stanley failed to exercise proper oversight of the 2016 decommissioning of two Wealth Management data centers, failed to assess hardware-decommissioning risk, failed to assess subcontracting risk adequately, and failed to maintain appropriate inventory of customer data stored on the decommissioned devices.
- [fact; source: https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-134.html] The same regulator action says Morgan Stanley also failed to exercise adequate due diligence in selecting the vendor and failed to monitor the vendor's performance, and that similar vendor-management control deficiencies recurred in 2019.
- [fact; source: https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-134.html] The Office of the Comptroller of the Currency states that these deficiencies resulted in noncompliance with the Interagency Guidelines Establishing Information Security Standards.
- [inference; source: https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-134.html; https://qa.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Auditors-Office/Audit-Services/Audit-Reports/Information-Technology-Vendor-Management] Existing standards do not protect the buyer when there is no reliable enforcement path, because vendor due diligence, performance monitoring, and exit controls can all fail while the contract still nominally exists.

#### 2.4 Technical-debt and maintainability failure

- [fact; source: https://www.jmis-web.org/articles/1510] Ramasubbu and Kemerer define technical debt as maintenance obligations that stem from violations of established standards during the development and subsequent maintenance of enterprise systems.
- [fact; source: https://www.jmis-web.org/articles/1510] Their empirical analysis used data from 1,824 real-world outsourced enterprise-systems maintenance projects.
- [fact; source: https://www.jmis-web.org/articles/1510] The study found that control balancing improves technical-debt remediation primarily when processes for migrating debt-laden systems to new technological platforms have been identified.
- [inference; source: https://www.jmis-web.org/articles/1510; https://www.nao.org.uk/reports/government-shared-services/] In outsourced delivery, a standards deviation becomes a persistent maintainability problem rather than a one-off defect, and remediation becomes harder once the buyer must unwind vendor-specific platform choices or migrate away from them.

#### 2.5 Supplier-monitoring and lifecycle-control failure

- [fact; source: https://www.nist.gov/publications/case-studies-cyber-supply-chain-risk-management-summary-findings-and-recommendations] NIST's 2020 case-study summary is based on interviews with 16 subject matter experts across six companies in different industries.
- [fact; source: https://www.nist.gov/publications/case-studies-cyber-supply-chain-risk-management-summary-findings-and-recommendations] The same publication says proposed follow-up research includes requirements to add to supplier terms and conditions, methods of applying supplier criticality, and additional guidance for less mature organizations.
- [fact; source: https://www.nist.gov/news-events/news/2021/02/nist-shares-key-practices-cyber-supply-chain-risk-management-based] NIST's 2021 summary of industry research says organizations need supplier management that continues throughout the supplier relationship and across the full life cycle.
- [fact; source: https://wjarr.com/content/third-party-vendor-risks-it-security-comprehensive-audit-review-and-mitigation-strategies] Ilori, Nwosu, and Naiho identify recurring vendor-risk areas including data breaches, inadequate security controls, and compliance issues, and recommend regular security assessments, clear contractual agreements, and continuous monitoring.
- [inference; source: https://www.nist.gov/publications/case-studies-cyber-supply-chain-risk-management-summary-findings-and-recommendations; https://www.nist.gov/news-events/news/2021/02/nist-shares-key-practices-cyber-supply-chain-risk-management-based; https://wjarr.com/content/third-party-vendor-risks-it-security-comprehensive-audit-review-and-mitigation-strategies] Multi-vendor environments fail predictably when supplier checks are treated as an onboarding activity instead of a lifecycle discipline with monitoring, incident coordination, and explicit contractual obligations.

#### 2.6 Variation by engagement model and best-supported remedies

- [inference; source: https://www.nao.org.uk/reports/government-shared-services/; https://www.jmis-web.org/articles/1510; https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-134.html] Shared-service and Enterprise Resource Planning (ERP) programs show standards gaps as convergence, interoperability, and benefits-realisation failures; outsourced maintenance shows them as technical debt and migration friction; managed-service and decommissioning cases show them as security, data-handling, and exit-control failures.
- [fact; source: https://www.gov.uk/government/publications/data-standards-authority-operational-model-and-processes/data-standards-authority-operational-model-and-processes] The Data Standards Authority says cross-government governance should set common data standards, carry out due diligence, improve monitoring of and compliance with common standards, and ensure proposals have a clear owner outside the authority.
- [fact; source: https://qa.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Auditors-Office/Audit-Services/Audit-Reports/Information-Technology-Vendor-Management] Denver's audit recommendations call for a designated authority, approved policies and procedures, ongoing security review, service-level monitoring, restitution processes, vendor-separation procedures, and a single system of record.
- [inference; source: https://www.gov.uk/government/publications/data-standards-authority-operational-model-and-processes/data-standards-authority-operational-model-and-processes; https://qa.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Auditors-Office/Audit-Services/Audit-Reports/Information-Technology-Vendor-Management; https://www.nist.gov/news-events/news/2021/02/nist-shares-key-practices-cyber-supply-chain-risk-management-based] The best-supported remedy pattern is not one more standards document by itself, but a combination of accountable ownership, contractually specific requirements, continuous monitoring, lifecycle and exit control, and one authoritative record of vendor obligations and evidence.

### §3 Reasoning

- [fact; source: https://www.nao.org.uk/reports/government-shared-services/; https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-134.html; https://www.jmis-web.org/articles/1510] The strongest direct evidence comes from official audit and regulator findings plus one large empirical outsourcing study, rather than from vendor advisories or opinion pieces.
- [inference; source: https://www.nao.org.uk/reports/government-shared-services/; https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-134.html; https://www.jmis-web.org/articles/1510; https://www.nist.gov/news-events/news/2021/02/nist-shares-key-practices-cyber-supply-chain-risk-management-based] The evidence points to a common mechanism: when vendors can choose or deviate from implementation details without a strong governing standard and enforcement path, the buyer loses the ability to coordinate integration, verify control operation, or exit cheaply.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-accountability-gaps.html; https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-split-risk-cost-benefits-accountability.html; https://qa.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Auditors-Office/Audit-Services/Audit-Reports/Information-Technology-Vendor-Management] This is consistent with prior repository findings that governance fails when no single actor owns the trade-off between risk, cost, and benefits, because vendor standards are only effective when someone owns the decision to enforce them.

### §4 Consistency Check

- [fact; source: https://www.nao.org.uk/reports/government-shared-services/; https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-134.html; https://www.jmis-web.org/articles/1510] The evidence supports three high-signal failure families without contradiction: integration and convergence failure, control and security failure, and technical-debt and exit failure.
- [inference; source: https://www.nao.org.uk/reports/government-shared-services/; https://www.jmis-web.org/articles/1510; https://wjarr.com/content/third-party-vendor-risks-it-security-comprehensive-audit-review-and-mitigation-strategies] Direct evidence is thinner on shadow systems and pure vendor lock-in than on cost, convergence, security, and decommissioning, so those two themes are treated as lower-confidence implications rather than headline findings.
- [inference; source: https://www.nist.gov/publications/case-studies-cyber-supply-chain-risk-management-summary-findings-and-recommendations; https://www.nist.gov/news-events/news/2021/02/nist-shares-key-practices-cyber-supply-chain-risk-management-based] The NIST material is more useful for lifecycle governance and remedy design than for single-incident quantification, so it is used to support governance-mechanism findings rather than to quantify loss severity.

### §5 Depth and Breadth Expansion

- [inference; source: https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-134.html; https://wjarr.com/content/third-party-vendor-risks-it-security-comprehensive-audit-review-and-mitigation-strategies] Through a technical and security lens, weak vendor standards expose the organization at system retirement as much as at system delivery, because decommissioning and subcontracting are implementation phases with their own control obligations.
- [inference; source: https://www.nao.org.uk/reports/government-shared-services/; https://www.jmis-web.org/articles/1510] Through an economic lens, absent standards push cost out of the initial contract and into later integration, migration, and support work, which is why benefits often stay qualitative while remediation costs become concrete.
- [inference; source: https://www.gov.uk/government/publications/data-standards-authority-operational-model-and-processes/data-standards-authority-operational-model-and-processes; https://www.nist.gov/news-events/news/2021/02/nist-shares-key-practices-cyber-supply-chain-risk-management-based] Through a governance lens, standards only change behavior when they are attached to due diligence, compliance monitoring, and an identified owner with authority to reject exceptions or force remediation.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-accountability-gaps.html; https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-split-risk-cost-benefits-accountability.html] Through an organisational-design lens, vendor standards gaps are one manifestation of a broader coordination problem in which integration risk, operating cost, and claimed benefits sit in different hands.

### §6 Synthesis

**Executive summary:**

- Organisations that let vendors deviate from implementation standards, or fail to specify those standards clearly, repeatedly incur integration fragmentation, control failures, and expensive exit problems rather than isolated delivery defects. [inference; source: https://www.nao.org.uk/reports/government-shared-services/; https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-134.html; https://www.jmis-web.org/articles/1510]
- The direct evidence is strongest for three observable failure families: weak convergence and unmeasured benefits in shared-service programs, data-security and exit-control failure in vendor-managed decommissioning, and persistent technical debt in outsourced enterprise systems. [fact; source: https://www.nao.org.uk/reports/government-shared-services/; https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-134.html; https://www.jmis-web.org/articles/1510]
- The pattern extends prior repository work on accountability gaps and split incentives, because vendor standards fail when no single owner has the authority and evidence base to enforce them across the supplier lifecycle. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-accountability-gaps.html; https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-split-risk-cost-benefits-accountability.html; https://qa.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Auditors-Office/Audit-Services/Audit-Reports/Information-Technology-Vendor-Management]
- The most credible mitigation pattern is accountable ownership plus contractually specific standards, continuous monitoring, and full-lifecycle exit control, not a standards document alone. [inference; source: https://www.nist.gov/news-events/news/2021/02/nist-shares-key-practices-cyber-supply-chain-risk-management-based; https://www.gov.uk/government/publications/data-standards-authority-operational-model-and-processes/data-standards-authority-operational-model-and-processes; https://qa.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Auditors-Office/Audit-Services/Audit-Reports/Information-Technology-Vendor-Management]

**Key findings:**

1. **Multi-vendor and shared-service programs without sufficiently specific common standards repeatedly fail to achieve process convergence, measured benefits, or reliable value-for-money outcomes.** ([inference]; medium confidence; source: https://www.nao.org.uk/reports/government-shared-services/; https://www.gov.uk/government/publications/data-standards-authority-operational-model-and-processes/data-standards-authority-operational-model-and-processes)
2. **Vendor-management standards that are not operationalised into approved structure, security review, service-level monitoring, and separation procedures leave buyers unable to show continuous compliance or controlled exit activity.** ([inference]; medium confidence; source: https://qa.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Auditors-Office/Audit-Services/Audit-Reports/Information-Technology-Vendor-Management; https://wjarr.com/content/third-party-vendor-risks-it-security-comprehensive-audit-review-and-mitigation-strategies)
3. **Weak enforcement of existing standards can escalate into explicit information-security noncompliance, as shown by Morgan Stanley's failed oversight of vendor-led decommissioning, deficient due diligence, and poor data inventory controls.** ([fact]; medium confidence; source: https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-134.html)
4. **In outsourced enterprise-systems maintenance, violations of established standards create technical debt that is empirically harder to remediate, especially when migration processes away from debt-laden platforms have not been defined.** ([fact]; medium confidence; source: https://www.jmis-web.org/articles/1510)
5. **Supplier governance that stops at onboarding leaves organisations exposed during operation, incident response, and retirement, because the strongest NIST-derived practice set requires monitoring throughout the supplier relationship and planning for the full life cycle.** ([inference]; medium confidence; source: https://www.nist.gov/news-events/news/2021/02/nist-shares-key-practices-cyber-supply-chain-risk-management-based; https://www.nist.gov/publications/case-studies-cyber-supply-chain-risk-management-summary-findings-and-recommendations)
6. **The dominant symptom varies by engagement model: shared-service and Enterprise Resource Planning (ERP) programs skew toward integration and benefits failures, outsourced builds skew toward technical debt, and managed-service or decommissioning arrangements skew toward security and exit-control failures.** ([inference]; medium confidence; source: https://www.nao.org.uk/reports/government-shared-services/; https://www.jmis-web.org/articles/1510; https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-134.html)
7. **The remedy pattern supported across audits, standards bodies, and adjacent repository items is a governance stack of one accountable owner, explicit contractual requirements, continuous compliance evidence, and controlled vendor exit, rather than discretionary exception handling.** ([inference]; medium confidence; source: https://qa.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Auditors-Office/Audit-Services/Audit-Reports/Information-Technology-Vendor-Management; https://www.nist.gov/news-events/news/2021/02/nist-shares-key-practices-cyber-supply-chain-risk-management-based; https://www.gov.uk/government/publications/data-standards-authority-operational-model-and-processes/data-standards-authority-operational-model-and-processes; https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-accountability-gaps.html; https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-split-risk-cost-benefits-accountability.html)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Shared-service programs without strong common standards fail on convergence and measurable value. | https://www.nao.org.uk/reports/government-shared-services/ ; https://www.gov.uk/government/publications/data-standards-authority-operational-model-and-processes/data-standards-authority-operational-model-and-processes | medium | Shared-service pattern |
| [inference] Missing operational vendor-management controls make continuous compliance and controlled exit unverifiable. | https://qa.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Auditors-Office/Audit-Services/Audit-Reports/Information-Technology-Vendor-Management ; https://wjarr.com/content/third-party-vendor-risks-it-security-comprehensive-audit-review-and-mitigation-strategies | medium | Audit plus review article |
| [fact] Weak enforcement during decommissioning produced regulator-confirmed information-security noncompliance at Morgan Stanley. | https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-134.html | medium | Primary regulator action |
| [fact] Standards violations in outsourced maintenance create technical debt that is harder to remediate without migration processes. | https://www.jmis-web.org/articles/1510 | medium | Large empirical study |
| [inference] Supplier governance must extend through the full supplier lifecycle, not just onboarding. | https://www.nist.gov/news-events/news/2021/02/nist-shares-key-practices-cyber-supply-chain-risk-management-based ; https://www.nist.gov/publications/case-studies-cyber-supply-chain-risk-management-summary-findings-and-recommendations | medium | NIST industry research |
| [inference] Different engagement models surface different dominant failure symptoms. | https://www.nao.org.uk/reports/government-shared-services/ ; https://www.jmis-web.org/articles/1510 ; https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-134.html | medium | Cross-source synthesis |
| [inference] Effective remediation requires an accountable owner plus contractual, monitoring, and exit controls. | https://qa.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Auditors-Office/Audit-Services/Audit-Reports/Information-Technology-Vendor-Management ; https://www.nist.gov/news-events/news/2021/02/nist-shares-key-practices-cyber-supply-chain-risk-management-based ; https://www.gov.uk/government/publications/data-standards-authority-operational-model-and-processes/data-standards-authority-operational-model-and-processes ; https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-accountability-gaps.html ; https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-split-risk-cost-benefits-accountability.html | medium | Cross-item synthesis |

**Assumptions:**

- [assumption; source: https://www.gartner.com/en/information-technology/topics/vendor-risk-management; https://www.pearson.com/en-us/subject-catalog/p/software-architecture-in-practice/P200000000537] The inaccessible or non-extractable seeded sources would likely have been directionally consistent with the accessible evidence base, so replacing them does not appear to bias the overall conclusion materially.
- [assumption; source: https://www.nao.org.uk/reports/government-shared-services/; https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-134.html; https://www.jmis-web.org/articles/1510] Cross-sector public-sector and financial-services cases are sufficiently comparable to support a general vendor-governance pattern, even though the exact systems and contracts differ.

**Analysis:**

- The evidence weights official regulator and audit findings more heavily than general vendor-risk commentary because those sources tie concrete outcomes to identifiable control failures. [inference; source: https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-134.html; https://www.nao.org.uk/reports/government-shared-services/; https://qa.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Auditors-Office/Audit-Services/Audit-Reports/Information-Technology-Vendor-Management]
- Absent standards and unenforced standards are analytically distinct but operationally adjacent: the first widens vendor discretion at design time, while the second allows known control expectations to decay during delivery and exit. [inference; source: https://www.nao.org.uk/reports/government-shared-services/; https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-134.html]
- A plausible rival explanation is that these failures reflect generic project weakness rather than standards gaps, but the recurring source pattern is the absence of common rules, evidence, owners, and lifecycle controls rather than isolated delivery mistakes. [inference; source: https://www.jmis-web.org/articles/1510; https://www.nist.gov/news-events/news/2021/02/nist-shares-key-practices-cyber-supply-chain-risk-management-based; https://qa.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Auditors-Office/Audit-Services/Audit-Reports/Information-Technology-Vendor-Management]
- This item also sharpens earlier repository findings on accountability gaps and split incentives by showing that vendor standards are where those abstract governance defects become observable in contract, monitoring, and exit behavior. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-accountability-gaps.html; https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-split-risk-cost-benefits-accountability.html; https://qa.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Auditors-Office/Audit-Services/Audit-Reports/Information-Technology-Vendor-Management]

**Risks, gaps, uncertainties:**

- Direct empirical comparison between "no standards" and "standards exist but are unenforced" is limited, so that distinction is partly reconstructed from how the cases describe missing versus failed controls. [inference; source: https://www.nao.org.uk/reports/government-shared-services/; https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-134.html]
- The evidence is stronger on convergence, security, and technical debt than on shadow systems or hard vendor lock-in, so those latter themes should not be treated as equally well established from this item alone. [inference; source: https://www.nao.org.uk/reports/government-shared-services/; https://www.jmis-web.org/articles/1510]
- The most accessible public cases are from government and financial-services contexts, so transfer to small private firms should be treated cautiously. [assumption; source: https://www.nist.gov/publications/case-studies-cyber-supply-chain-risk-management-summary-findings-and-recommendations; https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-134.html]

**Open questions:**

- Which contractual clauses most reliably reduce vendor non-compliance without materially slowing procurement?
- How often do buyer-side exception processes, rather than vendor resistance, create the actual breakdown in standards enforcement?
- What quantitative evidence exists on the cost delta between standards-based integration and heavily customized vendor delivery over a full system lifecycle?

### §7 Recursive Review

Review result: pass

Acronym audit: information technology (IT), Cyber Supply Chain Risk Management (C-SCRM), and Enterprise Resource Planning (ERP) are expanded on first use; no unexpanded Command Line Interface (CLI), Software Development Kit (SDK), Model Context Protocol (MCP), Retrieval-Augmented Generation (RAG), Large Language Model (LLM), or similar abbreviations remain in the drafted research prose.

Claim audit: all visible claims in `## Research Skill Output` are labelled as [fact], [inference], or [assumption], and all factual or inferential claims in `## Findings` below carry suffix-style source binding.

Cross-item audit: adjacent completed items on accountability gaps and split risk-cost-benefit accountability are integrated where the synthesis depends on governance ownership and incentive alignment.

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

Organisations that let vendors deviate from implementation standards, or fail to specify those standards clearly, repeatedly incur integration fragmentation, control failures, and expensive exit problems rather than isolated delivery defects. [inference; source: https://www.nao.org.uk/reports/government-shared-services/; https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-134.html; https://www.jmis-web.org/articles/1510]

The direct evidence is strongest for three observable failure families: weak convergence and unmeasured benefits in shared-service programs, data-security and exit-control failure in vendor-managed decommissioning, and persistent technical debt in outsourced enterprise systems. [fact; source: https://www.nao.org.uk/reports/government-shared-services/; https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-134.html; https://www.jmis-web.org/articles/1510]

This pattern extends prior repository findings on accountability gaps and split incentives, because vendor standards fail when no single owner has the authority and evidence base to enforce them across the supplier lifecycle. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-accountability-gaps.html; https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-split-risk-cost-benefits-accountability.html; https://qa.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Auditors-Office/Audit-Services/Audit-Reports/Information-Technology-Vendor-Management]

The most credible mitigation pattern is accountable ownership plus contractually specific standards, continuous monitoring, and full-lifecycle exit control, not a standards document alone. [inference; source: https://www.nist.gov/news-events/news/2021/02/nist-shares-key-practices-cyber-supply-chain-risk-management-based; https://www.gov.uk/government/publications/data-standards-authority-operational-model-and-processes/data-standards-authority-operational-model-and-processes; https://qa.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Auditors-Office/Audit-Services/Audit-Reports/Information-Technology-Vendor-Management]

### Key Findings

1. **Multi-vendor and shared-service programs without sufficiently specific common standards repeatedly fail to achieve process convergence, measured benefits, or reliable value-for-money outcomes.** ([inference]; medium confidence; source: https://www.nao.org.uk/reports/government-shared-services/; https://www.gov.uk/government/publications/data-standards-authority-operational-model-and-processes/data-standards-authority-operational-model-and-processes)
2. **Vendor-management standards that are not operationalised into approved structure, security review, service-level monitoring, and separation procedures leave buyers unable to show continuous compliance or controlled exit activity.** ([inference]; medium confidence; source: https://qa.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Auditors-Office/Audit-Services/Audit-Reports/Information-Technology-Vendor-Management; https://wjarr.com/content/third-party-vendor-risks-it-security-comprehensive-audit-review-and-mitigation-strategies)
3. **Weak enforcement of existing standards can escalate into explicit information-security noncompliance, as shown by Morgan Stanley's failed oversight of vendor-led decommissioning, deficient due diligence, and poor data inventory controls.** ([fact]; medium confidence; source: https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-134.html)
4. **In outsourced enterprise-systems maintenance, violations of established standards create technical debt that is empirically harder to remediate, especially when migration processes away from debt-laden platforms have not been defined.** ([fact]; medium confidence; source: https://www.jmis-web.org/articles/1510)
5. **Supplier governance that stops at onboarding leaves organisations exposed during operation, incident response, and retirement, because the strongest NIST-derived practice set requires monitoring throughout the supplier relationship and planning for the full life cycle.** ([inference]; medium confidence; source: https://www.nist.gov/news-events/news/2021/02/nist-shares-key-practices-cyber-supply-chain-risk-management-based; https://www.nist.gov/publications/case-studies-cyber-supply-chain-risk-management-summary-findings-and-recommendations)
6. **The dominant symptom varies by engagement model: shared-service and Enterprise Resource Planning (ERP) programs skew toward integration and benefits failures, outsourced builds skew toward technical debt, and managed-service or decommissioning arrangements skew toward security and exit-control failures.** ([inference]; medium confidence; source: https://www.nao.org.uk/reports/government-shared-services/; https://www.jmis-web.org/articles/1510; https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-134.html)
7. **The remedy pattern supported across audits, standards bodies, and adjacent repository items is a governance stack of one accountable owner, explicit contractual requirements, continuous compliance evidence, and controlled vendor exit, rather than discretionary exception handling.** ([inference]; medium confidence; source: https://qa.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Auditors-Office/Audit-Services/Audit-Reports/Information-Technology-Vendor-Management; https://www.nist.gov/news-events/news/2021/02/nist-shares-key-practices-cyber-supply-chain-risk-management-based; https://www.gov.uk/government/publications/data-standards-authority-operational-model-and-processes/data-standards-authority-operational-model-and-processes; https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-accountability-gaps.html; https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-split-risk-cost-benefits-accountability.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Shared-service programs without strong common standards fail on convergence and measurable value. | https://www.nao.org.uk/reports/government-shared-services/ ; https://www.gov.uk/government/publications/data-standards-authority-operational-model-and-processes/data-standards-authority-operational-model-and-processes | medium | Shared-service pattern |
| [inference] Missing operational vendor-management controls make continuous compliance and controlled exit unverifiable. | https://qa.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Auditors-Office/Audit-Services/Audit-Reports/Information-Technology-Vendor-Management ; https://wjarr.com/content/third-party-vendor-risks-it-security-comprehensive-audit-review-and-mitigation-strategies | medium | Audit plus review article |
| [fact] Weak enforcement during decommissioning produced regulator-confirmed information-security noncompliance at Morgan Stanley. | https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-134.html | medium | Primary regulator action |
| [fact] Standards violations in outsourced maintenance create technical debt that is harder to remediate without migration processes. | https://www.jmis-web.org/articles/1510 | medium | Large empirical study |
| [inference] Supplier governance must extend through the full supplier lifecycle, not just onboarding. | https://www.nist.gov/news-events/news/2021/02/nist-shares-key-practices-cyber-supply-chain-risk-management-based ; https://www.nist.gov/publications/case-studies-cyber-supply-chain-risk-management-summary-findings-and-recommendations | medium | NIST industry research |
| [inference] Different engagement models surface different dominant failure symptoms. | https://www.nao.org.uk/reports/government-shared-services/ ; https://www.jmis-web.org/articles/1510 ; https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-134.html | medium | Cross-source synthesis |
| [inference] Effective remediation requires an accountable owner plus contractual, monitoring, and exit controls. | https://qa.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Auditors-Office/Audit-Services/Audit-Reports/Information-Technology-Vendor-Management ; https://www.nist.gov/news-events/news/2021/02/nist-shares-key-practices-cyber-supply-chain-risk-management-based ; https://www.gov.uk/government/publications/data-standards-authority-operational-model-and-processes/data-standards-authority-operational-model-and-processes ; https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-accountability-gaps.html ; https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-split-risk-cost-benefits-accountability.html | medium | Cross-item synthesis |

### Assumptions

- [assumption; source: https://www.gartner.com/en/information-technology/topics/vendor-risk-management; https://www.pearson.com/en-us/subject-catalog/p/software-architecture-in-practice/P200000000537] The inaccessible or non-extractable seeded sources would likely have been directionally consistent with the accessible evidence base, so replacing them does not appear to bias the overall conclusion materially.
- [assumption; source: https://www.nao.org.uk/reports/government-shared-services/; https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-134.html; https://www.jmis-web.org/articles/1510] Cross-sector public-sector and financial-services cases are sufficiently comparable to support a general vendor-governance pattern, even though the exact systems and contracts differ.

### Analysis

- The evidence weights official regulator and audit findings more heavily than general vendor-risk commentary because those sources tie concrete outcomes to identifiable control failures. [inference; source: https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-134.html; https://www.nao.org.uk/reports/government-shared-services/; https://qa.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Auditors-Office/Audit-Services/Audit-Reports/Information-Technology-Vendor-Management]
- Absent standards and unenforced standards are analytically distinct but operationally adjacent: the first widens vendor discretion at design time, while the second allows known control expectations to decay during delivery and exit. [inference; source: https://www.nao.org.uk/reports/government-shared-services/; https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-134.html]
- A plausible rival explanation is that these failures reflect generic project weakness rather than standards gaps, but the recurring source pattern is the absence of common rules, evidence, owners, and lifecycle controls rather than isolated delivery mistakes. [inference; source: https://www.jmis-web.org/articles/1510; https://www.nist.gov/news-events/news/2021/02/nist-shares-key-practices-cyber-supply-chain-risk-management-based; https://qa.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Auditors-Office/Audit-Services/Audit-Reports/Information-Technology-Vendor-Management]
- This item also sharpens earlier repository findings on accountability gaps and split incentives by showing that vendor standards are where those abstract governance defects become observable in contract, monitoring, and exit behavior. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-accountability-gaps.html; https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-split-risk-cost-benefits-accountability.html; https://qa.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Auditors-Office/Audit-Services/Audit-Reports/Information-Technology-Vendor-Management]

### Risks, Gaps, and Uncertainties

- Direct empirical comparison between "no standards" and "standards exist but are unenforced" is limited, so that distinction is partly reconstructed from how the cases describe missing versus failed controls. [inference; source: https://www.nao.org.uk/reports/government-shared-services/; https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-134.html]
- The evidence is stronger on convergence, security, and technical debt than on shadow systems or hard vendor lock-in, so those latter themes should not be treated as equally well established from this item alone. [inference; source: https://www.nao.org.uk/reports/government-shared-services/; https://www.jmis-web.org/articles/1510]
- The most accessible public cases are from government and financial-services contexts, so transfer to small private firms should be treated cautiously. [assumption; source: https://www.nist.gov/publications/case-studies-cyber-supply-chain-risk-management-summary-findings-and-recommendations; https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-134.html]

### Open Questions

- Which contractual clauses most reliably reduce vendor non-compliance without materially slowing procurement?
- How often do buyer-side exception processes, rather than vendor resistance, create the actual breakdown in standards enforcement?
- What quantitative evidence exists on the cost delta between standards-based integration and heavily customized vendor delivery over a full system lifecycle?

---

## Output

*(Filled in on completion with what this research produced.)*

- Type: knowledge
- Description: This item synthesises audit, regulator, standards-body, and empirical-study evidence on how absent or unenforced vendor implementation standards create integration, security, technical-debt, and exit failures. [inference; source: https://www.nao.org.uk/reports/government-shared-services/; https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-134.html; https://www.jmis-web.org/articles/1510]
- Links:
  - https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-134.html
  - https://www.nao.org.uk/reports/government-shared-services/
  - https://www.jmis-web.org/articles/1510
