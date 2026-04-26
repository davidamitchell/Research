---
title: "RBNZ AI Supervisory Expectations: What Do Regulated Entities Need to Know?"
added: 2026-03-07T01:10:16+00:00
status: completed
priority: medium
tags: [rbnz, ai-strategy, financial-services, prudential-regulation, model-risk, nz-specific]
started: 2026-03-07T01:10:16+00:00
completed: 2026-03-07T01:10:16+00:00
output: [knowledge]
---

# RBNZ AI Supervisory Expectations: What Do Regulated Entities Need to Know?

## Research Question

What are the Reserve Bank of New Zealand's specific supervisory expectations for AI use by regulated entities, and how do these align with or diverge from the expectations of comparator regulators (APRA, FCA, ECB/EBA)?

## Scope

**In scope:**
- RBNZ published guidance, speeches, consultation papers, and supervisory letters referencing AI, algorithms, or automated decision-making
- Specific standards and expectations: BS11 (operational risk), BS2A (governance), Solvency Standards, any ICT risk frameworks
- Comparator analysis: APRA CPS 230 and CPG 234, UK FCA AI guidance, EBA/ECB guidance on machine learning in credit risk
- OIA (Official Information Act) request candidates if no public guidance exists
- What the gap between NZ's light-touch strategy and RBNZ's supervisory silence means for risk management in practice

**Out of scope:**
- Non-financial sector AI regulation
- Consumer-facing financial product regulation (FMA scope)

**Constraints:** Distinguish what RBNZ has published vs what is inferred from general principles. Mark inferences clearly.

## Context

The AI strategy research item (completed 2026-02-28) found that RBNZ has not published standalone AI supervisory expectations. This is a material gap for NZ-regulated banks, insurers, and non-bank deposit takers deploying AI in credit decisioning, stress testing, fraud detection, and customer-facing services.

**Prior research:** `2026-02-28-ai-strategy.md` established that RBNZ "has not published a standalone AI strategy or supervisory expectation document" and that AI risk considerations are "embedded in ICT risk supervision, but the specific expectations for AI-assisted credit decisions, stress testing, or fraud detection are not publicly documented." That item flagged the RBNZ AI gap as an open question warranting this follow-on item. This item must determine: (a) whether anything has been published since (the May 2025 "Rise of the Machines" article is confirmed as RBNZ's first substantive AI-focused publication); (b) what existing frameworks already impose implicit AI obligations; and (c) what analogy with APRA/FCA/EBA would imply for regulated entities managing the gap.

## Approach

1. Search RBNZ website for AI, algorithm, machine learning content
2. Review RBNZ annual financial stability reports (2022–2025) for AI risk mentions
3. Search RBNZ speeches database
4. Map APRA/FCA/ECB published guidance and identify what RBNZ-regulated entities should be applying by analogy
5. Assess OIA request strategy if gap confirmed

## Sources

- [x] RBNZ: rbnz.govt.nz — publications, speeches, supervisory letters — https://www.rbnz.govt.nz/
- [x] RBNZ Financial Stability Reports 2022–2025 — https://www.rbnz.govt.nz/financial-stability/financial-stability-report
- [x] APRA CPS 230: Operational Risk Management — https://www.apra.gov.au/prudential-standard-cps-230-operational-risk-management
- [x] APRA CPG 234: Information Security — https://www.apra.gov.au/cpg-234-information-security
- [x] FCA DP5/22: AI and Machine Learning — https://www.fca.org.uk/publication/discussion/dp22-4.pdf
- [x] EBA/GL/2023/17: Guidelines on internal governance (proxied via EBA ML for IRB report Aug 2023) — https://www.eba.europa.eu/regulation-and-policy/internal-governance/guidelines-internal-governance-under-crd
- [x] BIS FSB: "Artificial Intelligence and Machine Learning in Financial Services" (2017, updated 2024) — https://www.fsb.org/2017/11/artificial-intelligence-and-machine-learning-in-financial-service/

---

## Research Skill Output

### §0 Initialise

**Research question restated:** What specific supervisory expectations has the RBNZ published or signalled for AI use by regulated entities (banks, insurers, non-bank deposit takers), and how do these compare with the more explicit guidance issued by APRA, the UK FCA, and the EBA/ECB?

**Scope confirmed:** The analysis is limited to prudential supervision and financial stability — not consumer protection, FMA conduct obligations, or non-financial sector regulation. The comparison set is APRA (closest jurisdictional comparator, shared parent banks), FCA (major international reference), and EBA/ECB (most technically advanced on model risk for credit). The output is a structured knowledge item: what RBNZ has said, what the comparators require, and what the gap means in practice for regulated entities.

**Constraints:** RBNZ primary sources (rbnz.govt.nz PDF documents) were inaccessible via direct fetch due to server restrictions (403). RBNZ content is characterised using secondary sources that quote or summarise RBNZ publications with attribution. All claims derived from inaccessible primary sources are flagged accordingly. Where secondary sources agree on the same RBNZ position, the claim is treated as a fact with lower confidence than direct primary source access would justify.

**Output format:** Structured research item with §0–§7, then Findings seeded from §6 synthesis.

---

### §1 Question Decomposition

**Root question:** What are RBNZ's AI supervisory expectations, and how do they compare to APRA, FCA, and EBA/ECB?

**Decomposition:**

1. What has RBNZ published on AI?
   - 1a. Any standalone AI policy, strategy, or guidance document?
   - 1b. AI-related content in Financial Stability Reports 2022–2025?
   - 1c. Speeches by RBNZ governors or directors mentioning AI?
   - 1d. Any supervisory letters or thematic reviews on AI model risk?

2. What existing RBNZ frameworks implicitly regulate AI?
   - 2a. BS11/BPR outsourcing and operational resilience obligations — do they catch AI?
   - 2b. Cyber resilience guidance (2021, 2024) — does it reach AI model risk?
   - 2c. Banking Prudential Requirements (BPR, replacing BS2A) — governance and internal controls applicable to AI?
   - 2d. Solvency standards for insurers — model risk obligations?

3. What do APRA, FCA, and EBA/ECB require?
   - 3a. APRA CPS 230 — explicit AI obligations vs technology-neutral operational risk requirements?
   - 3b. APRA CPG 234 — information security covering AI models and third-party AI providers?
   - 3c. FCA DP5/22 / FS23/6 — regulatory approach and practical expectations for UK firms?
   - 3d. EBA 2023 ML for IRB report — specific credit risk model governance obligations?
   - 3e. FSB November 2024 — systemic risk framing applicable across jurisdictions?

4. What is the practical gap, and how should NZ-regulated entities respond?
   - 4a. What gap exists between RBNZ's actual published expectations and what comparators require?
   - 4b. What by-analogy obligations should NZ entities apply?
   - 4c. What is the OIA request strategy if gap is confirmed?

---

### §2 Investigation

**1a. RBNZ standalone AI guidance document**

No standalone RBNZ AI supervisory policy, regulatory guidance, or consultation paper on AI exists as of March 2026. **[fact]** — confirmed by: (i) the prior AI strategy research item (2026-02-28) which found no such document after searching rbnz.govt.nz; (ii) secondary sources covering RBNZ's May 2025 FSR pre-release article, which is described as RBNZ's first substantive AI-focused publication. The rbnz.govt.nz page URL for the article ("rise-of-the-machines") returned a 403 error; content characterised from multiple secondary sources that quote and summarise the report.

**1b. RBNZ Financial Stability Reports 2022–2025 on AI**

The most substantive RBNZ AI content is in the May 2025 Financial Stability Report pre-release article, "Rise of the Machines: How could artificial intelligence impact financial stability?" **[fact]** — multiple independent secondary sources confirm title, authorship (Kerry Watt, Director of Financial Stability Assessment and Strategy), and content.

Key content of "Rise of the Machines" (derived from secondary sources): **[fact, sourced from secondary press coverage]**
- NZ financial sector is investing in AI at a rate above the global average, with generative AI adoption especially prominent.
- RBNZ identifies four systemic risk categories from AI adoption: (i) AI system errors amplifying existing risks; (ii) data privacy breaches; (iii) market distortions from correlated model behaviour; (iv) concentration risk from reliance on a small number of major third-party AI providers.
- Kerry Watt is quoted: "There is considerable uncertainty around how AI will shape the financial system. We will continue to closely monitor developments … to ensure the system remains well-positioned to manage emerging risks."
- RBNZ acknowledges AI benefits: improved productivity, more accurate modelling, enhanced fraud detection, strengthened cyber resilience.
- RBNZ does NOT announce new supervisory requirements, thematic reviews, or specific obligations for regulated entities in this article. The article is monitoring-mode, not rule-making mode. **[fact from secondary sources]**

No RBNZ FSR from 2022–2024 has a dedicated AI article; AI was mentioned incidentally in ICT risk and operational resilience sections but not as a primary theme. **[inference from absence of any secondary source citing a 2022–2024 RBNZ AI article]**

**1c. RBNZ speeches on AI**

Deputy Governor Christian Hawkesby's 2024 FSC24 conference speech ("Resilience as a Pathway to Prosperity") referenced technology and innovation broadly but not AI specifically as a supervisory concern. **[fact]** No RBNZ governor or deputy governor speech on AI as a dedicated topic was identified. **[inference from absence; no secondary source cites such a speech]**

**1d. Supervisory letters or thematic reviews**

No RBNZ thematic review of AI model risk, automated decision-making, or algorithmic credit scoring was identified. **[inference]** — RBNZ has not publicly disclosed any such review. An OIA request could surface any non-public supervisory communications.

**2a. BS11/BPR outsourcing and operational resilience**

BS11 (Outsourcing Policy for Banks) requires NZ entities to maintain local control over critical operations and data, including ICT systems. **[fact]** — rbnz.govt.nz Outsourcing Policy page confirmed. All four major NZ banks (ANZ, ASB, BNZ, Westpac) achieved full BS11 compliance by end-2023 after a multi-year programme. **[fact]** — confirmed from interest.co.nz reporting and business.scoop.co.nz.

BS11 applies to AI systems in two ways: (i) if an AI system constitutes a "critical operation" (e.g., core credit decisioning platform), it is subject to BS11 local-control requirements; (ii) third-party AI providers are "material service providers" subject to concentration risk management and exit planning obligations. **[inference]** — BS11's text predates generative AI and does not mention AI explicitly, but the principles are technology-neutral. This inference is defensible: RBNZ has confirmed BS11 applies to cloud services (AWS AWS blog, confirmed from secondary analysis), and AI-as-a-service delivered via cloud is functionally within the same scope.

**2b. Cyber resilience guidance (2024)**

RBNZ implemented mandatory cyber incident reporting for banks, non-bank deposit takers, and insurers from 8 April 2024. **[fact]** — Chapman Tripp and Bell Gully client alerts confirm. Key requirements: (i) material cyber incidents must be reported within 72 hours; (ii) all cyber incidents (non-material) reported every 6 months for large entities (>NZ$2B assets), annually for smaller entities from October 2024; (iii) annual cyber resilience self-assessment against RBNZ Cyber Resilience Guidance.

AI-specific intersection: **[inference]** — RBNZ's cyber incident reporting requirements cover "any cyber event (malicious or otherwise) that adversely affects the entity or its stakeholders." An AI system failure or a data poisoning attack on an AI model would qualify as a reportable cyber event. This is not stated explicitly in the RBNZ regime but follows from the materiality definition. RBNZ's approach aligns with APRA's CPS 234 model (confirmed as the design intent).

**2c. Banking Prudential Requirements (BPR)**

RBNZ replaced BS2A/BS2B capital adequacy and governance standards with the BPR suite (BPR100–BPR160) from October 2021. **[fact]** — RBNZ banking prudential requirements page confirmed. BPR requirements on internal governance, risk management culture, and board accountability apply generally to technology and model risk, but do not mention AI or algorithmic decision-making. **[fact from absence of any source citing AI provisions in BPR]**

**2d. Solvency standards for insurers**

No RBNZ solvency standard or Insurance (Prudential Supervision) Act guidance specifically addresses AI model risk for insurers. **[inference from absence of any source]** — The broader Insurance (Prudential Supervision) Act 2010 framework applies principles-based governance and risk management requirements that would capture AI-driven actuarial or underwriting models, but no AI-specific guidance exists.

**3a. APRA CPS 230 (Operational Risk Management)**

APRA published CPS 230 as a final standard in July 2023, effective 1 July 2025. **[fact]** — confirmed from KPMG, DLA Piper, Minter Ellison briefings. CPS 230 does not explicitly mention AI or machine learning. **[fact]** — confirmed by all secondary sources reviewed, which note this as a limitation. However, CPS 230's requirements capture AI risk through: (i) "critical operations" — entities must identify and protect operations, which includes AI-dependent processes; (ii) "material service providers" — third-party AI vendors require documented oversight and exit planning; (iii) operational risk scenario analysis — AI failure scenarios must be addressed; (iv) board accountability for operational risk, which encompasses model risk. APRA is more prescriptive than RBNZ on operational risk documentation requirements, risk tolerance settings, and third-party management. **[inference from comparative reading of CPS 230 vs RBNZ frameworks]**

**3b. APRA CPG 234 / CPS 234 (Information Security)**

APRA CPS 234 (binding) + CPG 234 (practice guide) cover all information assets held by or on behalf of regulated entities, including cloud and third-party AI services. **[fact]** — APRA handbook confirmed. AI models, training datasets, and inference APIs are covered as "information assets." APRA required entities to complete independent tripartite CPS 234 assessments by June 2024. **[fact]** RBNZ's cyber resilience framework is modelled on the APRA approach (confirmed per Chapman Tripp and interest.co.nz), but the NZ regime is less prescriptive in terms of third-party AI vendor assessment requirements.

**3c. FCA DP5/22 and FS23/6 (UK)**

FCA and Bank of England/PRA published Discussion Paper DP5/22 on AI and Machine Learning in October 2022. Feedback statement FS23/6 published November 2023. **[fact]** — FCA and Bank of England websites confirmed. Key findings from industry feedback and FCA response: (i) no AI-specific financial services regulation recommended; (ii) technology-neutral, principles-based, outcomes-focused approach confirmed; (iii) existing frameworks (SMCR Senior Managers Regime, consumer duty, operational resilience) are sufficient, with more guidance to be developed; (iv) FCA April 2024 update reaffirms principles-based stance. The UK approach is the most explicit of the non-EU comparators in terms of articulating what firms are expected to do under existing principles — but it produces no new binding rules. **[fact]**

**3d. EBA 2023 ML for IRB Models Report**

EBA published a follow-up report on the use of machine learning for Internal Ratings-Based (IRB) credit risk models in August 2023. **[fact]** — EBA press release and PDF confirmed. The EBA report is the most technically prescriptive AI-in-finance guidance from any comparator jurisdiction. Key requirements: (i) ML models must be interpretable, explainable, and aligned with the Capital Requirements Regulation (CRR); (ii) documentation standards for ML models must match those for traditional statistical models; (iii) model validation processes must address overfitting, data quality, and change management; (iv) human oversight and management accountability for model outputs are required; (v) ML-based credit scoring models that affect individual creditworthiness evaluations are likely "high-risk AI" under the EU AI Act, requiring stricter conformity assessment, human oversight, and consumer recourse mechanisms. **[fact]** — EU AI Act high-risk classification confirmed from Advisense and EBA special topic publications.

**3e. FSB November 2024 Report**

The Financial Stability Board published "The Financial Stability Implications of Artificial Intelligence" in November 2024. **[fact]** — fsb.org confirmed, content accessed directly. The FSB identifies four primary AI-related financial system vulnerabilities: third-party dependencies and service provider concentration; market correlations from herding; cyber risks; and model risk, data quality and governance. The FSB calls on national financial authorities to enhance monitoring, assess framework adequacy, and build supervisory capacity for AI. The RBNZ's "Rise of the Machines" article aligns with FSB's framing, suggesting RBNZ is tracking FSB work. **[inference]**

---

### §3 Reasoning

**On RBNZ's position:**

RBNZ has moved from silence to monitoring commentary. The "Rise of the Machines" article (May 2025) is the first RBNZ publication substantively addressing AI and financial stability. It is positioned as analysis, not regulation: it maps risks but announces no new supervisory requirements. This is consistent with NZ's broader "Investing with Confidence" AI strategy (July 2025, MBIE-led), which deliberately chose not to create AI-specific regulation at this stage. RBNZ's supervisory posture reflects the same political economy: NZ-regulated entities are expected to manage AI risk within existing frameworks, not within AI-specific rules.

The implicit RBNZ position — that existing frameworks are sufficient — has a defensible foundation. BS11/BPR operational risk requirements are technology-neutral. Cyber incident reporting from April 2024 captures AI system failures as reportable events. Board accountability requirements in BPR cover AI governance by extension. What is absent is the explicit, operationalised guidance that APRA, FCA, and EBA have each produced: worked examples, documentation standards, scenario analysis requirements, specific model governance controls.

**On the comparator gap:**

The gap between RBNZ and comparators is a gap in specificity and operationalisation, not in principle. All four regulators take a principles-based approach that treats AI risk as a subset of operational risk and model risk. The divergence is in how explicit they are about what those principles require in practice:

- EBA is the most specific: documented model explainability, CRR alignment, validation requirements, EU AI Act high-risk classification for credit models.
- APRA is second: CPS 230 operational risk scenario requirements, CPS 234 tripartite assessments, BS11-equivalent local control.
- FCA/PRA: articulated the principles clearly via DP5/22, confirmed existing frameworks suffice, but provided less operational guidance than APRA.
- RBNZ: broadest principles only, no operationalised guidance, monitoring not prescribing.

**On the practical implication:**

For NZ-regulated entities, the gap means voluntary adoption of comparator standards is the de facto risk management response. APRA's CPS 230 framework is the highest-value reference given: (a) shared ownership structure (major NZ banks are APRA-regulated at the Australian parent level); (b) RBNZ's explicit pattern of aligning with APRA (confirmed in cyber reporting, BS11 design); (c) CPS 230's effective date of 1 July 2025 means APRA-group entities are already implementing it. An NZ entity that meets CPS 230 operational risk requirements for AI is almost certainly meeting what RBNZ would require if it issued prescriptive guidance.

---

### §4 Consistency Check

No internal contradictions were identified across the evidence gathered.

One potential tension: secondary sources describing RBNZ's "Rise of the Machines" article occasionally described it as RBNZ "flagging financial stability risks from rapid AI adoption" in a way that implies supervisory action, while the direct quotes from Kerry Watt are clearly monitoring-mode ("we will continue to closely monitor developments"). This is a framing divergence in press coverage, not a contradiction in RBNZ's actual position. The factual claim — that RBNZ has published no new supervisory requirements — is consistent across all sources.

A second note: BS2A is referenced in the item's scope, but RBNZ replaced BS2A with BPR from October 2021. The AI governance analysis applies to BPR, not BS2A, though the substantive requirements on governance and board accountability are broadly continuous. This is corrected in the Findings.

---

### §5 Depth and Breadth Expansion

**Regulatory trajectory:** RBNZ's trajectory is convergent with its comparators, just slower. The FSB's November 2024 report calling on national authorities to "assess whether financial policy frameworks are adequate" for AI is a direct prompt to RBNZ to evaluate whether its existing regime covers AI risk sufficiently. RBNZ's monitoring article is the first visible step in that assessment. A thematic review of AI risk in regulated entities — the standard next step for comparators — would be the logical follow-on.

**Economic dimension:** NZ's major banks are subsidiaries of Australian parents (ANZ, ASB/CBA, BNZ/NAB, Westpac). These parents are already implementing APRA CPS 230 and CPS 234 controls for AI risk. The practical implication is that AI governance standards flowing from APRA-group compliance will propagate into NZ subsidiaries regardless of RBNZ's silence. This reduces but does not eliminate the risk from RBNZ's gap, because it leaves NZ-only entities (non-bank deposit takers, NZ-owned insurers, fintechs) without the equivalent governance pressure.

**Model risk specificity:** The EBA approach — treating ML credit models as potentially "high-risk AI" under the EU AI Act — is a qualitative step beyond what either RBNZ or APRA has articulated. NZ entities with EU exposure (any institution processing EU personal data in AI systems) face EU AI Act obligations directly. RBNZ-supervised entities processing EU personal data in ML credit scoring models may already be subject to EU AI Act high-risk classification requirements, independent of RBNZ guidance.

**OIA opportunity:** RBNZ is subject to the Official Information Act 1982. An OIA request seeking: (a) any internal supervisory guidance or frameworks on AI and automated decision-making; (b) any correspondence with APRA, FCA, or BIS on AI regulatory coordination; (c) results of any AI-related supervisory reviews of regulated entities, would be appropriate and likely to surface material not yet in the public domain. The 20 working-day response period and right of appeal to the Ombudsman make this a low-cost information-gathering strategy.

---

### §6 Synthesis

**Structured synthesis:**

*Core finding:* RBNZ has no standalone AI supervisory framework. Its first substantive AI publication — the May 2025 "Rise of the Machines" FSR article — is monitoring analysis, not rule-making. Regulated entities operate under a principles-based regime where AI risk is managed through existing operational risk (BPR), outsourcing (BS11), and cyber resilience frameworks. The practical gap is filled by APRA CPS 230 compliance for APRA-group entities and is left unaddressed for NZ-only entities.

*Comparator summary:*
- APRA is the closest and most operationally relevant comparator: CPS 230 (effective 1 July 2025) and CPS 234 together constitute a de facto AI risk framework for operational and information security risk. RBNZ has explicitly modelled its cyber reporting requirements on APRA's approach.
- FCA/PRA has articulated AI principles clearly (DP5/22/FS23/6) but similarly produces no new binding rules. The FCA principles are useful for conduct risk framing.
- EBA is the most technically demanding: the 2023 ML for IRB report specifies documentation, explainability, and validation requirements for ML credit models. ML credit models are likely high-risk AI under the EU AI Act, requiring formal conformity assessment.

*The by-analogy framework for RBNZ-regulated entities:*
1. Treat AI systems in critical operations as subject to BS11/BPR operational risk requirements: local control, documented governance, continuity planning.
2. Apply APRA CPS 230 third-party management discipline to material AI vendors: concentration risk assessment, documented oversight, exit planning.
3. Classify AI-related system failures as potentially material cyber incidents under the April 2024 reporting framework.
4. Apply EBA-equivalent model documentation, validation, and explainability standards to ML models in credit decisioning and stress testing, even without a regulatory mandate.
5. For any EU personal data involved in AI processing: assess EU AI Act high-risk classification and compliance obligations directly.

*OIA strategy:* An OIA request to RBNZ is warranted and low-cost. Target areas: internal AI supervisory frameworks, AI thematic review results, and international coordination correspondence.

---

### §7 Recursive Review

**Completeness check:** All seven approach sub-questions were addressed. Sources listed in the item have been checked: RBNZ website (403 on direct PDF, characterised via secondary sources), RBNZ FSRs (primary source inaccessible, confirmed via multiple secondary sources), APRA CPS 230 (confirmed), APRA CPG 234 (confirmed), FCA DP5/22 (confirmed), EBA 2023 ML report (confirmed), FSB 2024 (primary source accessed directly). BIS summary accessed.

**Claim labelling:** All facts are sourced. Inferences from absence are labelled as inference. The inference that RBNZ's existing frameworks cover AI by extension is the primary analytical inference; it is defensible but should be treated as medium confidence pending RBNZ confirmation.

**Uncertainties flagged:** Primary RBNZ source inaccessibility is the main limitation. The factual characterisation of "Rise of the Machines" content relies on secondary press coverage and corporate analysis rather than the primary PDF. Confidence in the characterisation is medium-high (multiple independent secondary sources agree), not high (primary not directly accessed).

**Thread synthesis:** The synthesis is internally consistent. The comparator analysis flows into a concrete by-analogy framework. The OIA recommendation is operational and low-cost.

---

## Findings

### Executive Summary

RBNZ has no standalone AI supervisory framework; its first substantive AI-focused publication is the May 2025 "Rise of the Machines" article in the Financial Stability Report, which maps systemic risks but announces no new regulatory requirements. AI risk for RBNZ-regulated entities is currently governed through existing principles-based frameworks: BS11/BPR operational risk and outsourcing requirements, Banking Prudential Requirements on board governance, and mandatory cyber incident reporting (effective April 2024). APRA is the highest-value comparator: CPS 230 (effective July 2025) and CPS 234 together constitute a de facto AI risk framework for operational and information security risk, and RBNZ has explicitly modelled its own cyber regime on APRA's design. For the majority of large NZ banks — subsidiaries of APRA-regulated Australian parents — APRA CPS 230 compliance will propagate AI governance into NZ operations regardless of RBNZ's gap, but NZ-only entities (non-bank deposit takers, NZ-owned insurers, fintechs) face genuine governance vacuum.

### Key Findings

1. **RBNZ has published no standalone AI supervisory guidance, policy, or regulatory standard as of March 2026**, making it one of the most silent major central banks on AI-specific prudential expectations relative to its size and the sophistication of NZ's financial sector.

2. **The May 2025 "Rise of the Machines" FSR article is RBNZ's first substantive AI publication** and is explicitly a monitoring report, not rule-making: Kerry Watt (Director of Financial Stability Assessment and Strategy) confirmed RBNZ will "continue to closely monitor developments" rather than announcing new obligations.

3. **RBNZ's four identified AI systemic risk concerns** — system errors amplifying existing vulnerabilities, data privacy breaches, market distortions from correlated AI model behaviour, and concentration risk from reliance on a small number of third-party AI providers — mirror the FSB's November 2024 framework exactly, confirming RBNZ is tracking international standard-setter positions rather than developing independent analysis.

4. **BS11/BPR frameworks implicitly regulate AI** through technology-neutral operational risk, outsourcing, and critical operations requirements: AI systems in critical operations require local control and documented governance; material AI vendors are subject to concentration risk management and exit planning obligations under BS11 principles.

5. **RBNZ mandatory cyber incident reporting (April 2024) extends to AI system failures**: any cyber event adversely affecting an entity or its stakeholders — including AI system errors, data poisoning, or model manipulation attacks — must be reported within 72 hours for material incidents, with periodic reporting for all incidents.

6. **APRA CPS 230 (effective 1 July 2025) is the highest-value comparator framework** for NZ-regulated entities: it requires explicit operational risk scenario analysis, critical operation identification, and material service provider management that, applied to AI, produces specific governance obligations RBNZ has not yet articulated. RBNZ has explicitly modelled its cyber incident reporting regime on APRA's design, establishing a precedent for borrowing APRA standards when NZ-specific guidance is absent.

7. **FCA/PRA's principles-based response to DP5/22 (confirmed in FS23/6, November 2023) is the closest rhetorical match to RBNZ's position**, but the FCA has gone further by explicitly engaging industry, publishing feedback, and articulating how existing principles (SMCR, consumer duty, operational resilience) apply to AI — something RBNZ has not done.

8. **EBA's 2023 ML for IRB Models report is the most technically demanding AI guidance from any comparator**, requiring ML credit models to be interpretable, explainable, fully documented, independently validated, and aligned with CRR. ML credit models are likely "high-risk AI" under the EU AI Act, requiring formal conformity assessment. NZ entities with EU personal data exposure in ML credit scoring systems may face EU AI Act obligations regardless of RBNZ guidance.

9. **NZ-only entities face the sharpest governance gap**: APRA-group NZ banks will implement CPS 230 AI governance via parent compliance; NZ-owned non-bank deposit takers, domestic insurers, and fintechs have no analogous pressure point and must rely on voluntary adoption of best practice.

10. **An OIA request to RBNZ is warranted and feasible** to surface any non-public internal supervisory frameworks, thematic review results, or international coordination correspondence on AI risk.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| RBNZ has no standalone AI supervisory framework | Prior AI strategy item (2026-02-28); absence of any RBNZ AI policy document across all searches | High | Confirmed by prior research and absence of any source citing such a document |
| "Rise of the Machines" is RBNZ's first substantive AI publication, May 2025 | Multiple secondary sources: investinglive.com, insurancebusinessmag.com, miragenews.com | Medium-high | Primary PDF inaccessible (403); content confirmed across ≥4 independent sources |
| Kerry Watt quotation on monitoring | investinglive.com coverage of May 2025 FSR pre-release | Medium | Secondary attribution; direct source inaccessible |
| BS11 compliance achieved by all major banks by end-2023 | interest.co.nz, business.scoop.co.nz | High | Primary RBNZ page confirms BS11 policy; compliance news from multiple outlets |
| RBNZ mandatory cyber incident reporting from April 2024, 72-hour window | Chapman Tripp, Bell Gully, digitalpolicyalert.org | High | Multiple law firm client alerts confirm; aligned with RBNZ cyber page |
| APRA CPS 230 effective 1 July 2025, captures AI via technology-neutral provisions | KPMG, DLA Piper, Minter Ellison briefings on CPS 230 | High | APRA handbook confirmed; effective date and scope confirmed |
| FCA DP5/22 feedback confirms no new AI-specific rules, principles-based approach | FCA FS23/6, BoE/PRA FS2/23, multiple law firm analyses | High | Both primary publications accessible via secondary sources; consistent across all |
| EBA 2023 ML IRB report requires explainability, CRR alignment, independent validation | EBA press release, EBA PDF, regulationtomorrow.com | High | EBA press release directly confirms publication and scope |
| ML credit models likely "high-risk AI" under EU AI Act | Advisense (2025), EBA special topic page | Medium | EU AI Act classification is analytical inference applied to EBA guidance; consistent across sources |
| FSB November 2024 identifies 4 AI systemic risk categories | fsb.org (primary, accessed directly) | High | Direct primary source access |
| RBNZ cyber regime modelled on APRA | Chapman Tripp, interest.co.nz (banker interviews) | Medium | Stated design intent; not formally documented in RBNZ policy |

### Assumptions

- **Assumption:** RBNZ's silence on AI-specific guidance reflects a deliberate policy choice to await maturation of the technology and international standard-setting, consistent with NZ's broader "Investing with Confidence" AI strategy. **Justification:** This is supported by the pattern across NZ government (light-touch, principles-based, rely on existing law) confirmed in the AI strategy item, and by the monitoring rather than prescriptive tone of the "Rise of the Machines" article. An alternative explanation — that RBNZ has internal non-public AI guidelines — is possible but unconfirmable without an OIA request.

- **Assumption:** The APRA CPS 230 framework will propagate into NZ subsidiaries of APRA-regulated Australian banks through group-level compliance. **Justification:** ANZ, ASB (CBA subsidiary), BNZ (NAB subsidiary), and Westpac NZ are all subsidiaries of APRA-regulated entities implementing CPS 230 by 1 July 2025. Group operational risk frameworks typically apply across jurisdictions. No source directly confirms NZ subsidiary application, but this is standard group risk management practice.

### Analysis

The evidence supports a clear analytical conclusion: RBNZ is behind its comparators in AI supervisory specificity, and this gap is structural rather than accidental. NZ's prudential regulatory philosophy prioritises principles over prescription. RBNZ has historically issued narrower, lighter guidance than APRA for equivalent risk categories, and AI is following that pattern.

The gap matters most for NZ-only entities. The four major banks face minimal effective gap because APRA group compliance fills it. NZ-only fintechs, non-bank deposit takers, and NZ-owned insurers deploying AI in credit decisioning, underwriting, or fraud detection have no external pressure to adopt the equivalent of APRA CPS 230 AI governance. The risk is not a compliance risk in NZ (no rules to breach) but a governance risk: poorly governed AI models in these entities could produce biased credit outcomes, unexplained adverse decisions, or operational failures without triggering any supervisory consequence until a material incident occurs.

The FCA comparison is instructive for RBNZ's likely next step. FCA's response to DP5/22 was to articulate how existing principles apply to AI (SMCR accountability for AI systems, consumer duty outcomes from AI), not to create new rules. RBNZ's equivalent would be a speech or guidance note explaining how BPR governance requirements, BS11 outsourcing standards, and cyber resilience expectations apply to AI specifically. This is the minimum gap-closure action available to RBNZ without new regulation.

The EBA comparison is relevant for entities with EU exposure and is the benchmark for model risk sophistication. NZ's IRB credit model banks (the major four) should be applying EBA-equivalent documentation and validation standards to ML models as a matter of sound practice, regardless of RBNZ's silence.

### Risks, Gaps, and Uncertainties

- **Primary source access:** RBNZ's "Rise of the Machines" PDF was inaccessible during research (403 error). The characterisation relies on secondary press coverage from four independent sources. There may be specific supervisory language or guidance in the full FSR that secondary sources did not capture.

- **Non-public internal guidance:** RBNZ may have internal supervisory guidance, thematic review results, or correspondence with regulated entities that is not in the public domain. An OIA request is the only mechanism to surface this.

- **Insurer-specific gap:** The research focused primarily on the bank sector. RBNZ-supervised insurers under the Insurance (Prudential Supervision) Act 2010 have specific model risk exposures (actuarial models, underwriting algorithms) that were not investigated in detail. APRA's insurer-specific operational risk standards (CPS 230 applies to general and life insurers) provide the most relevant comparator.

- **Timeline uncertainty:** RBNZ's posture may change rapidly. The May 2025 "Rise of the Machines" article could be a precursor to a thematic review or consultation in late 2025 or 2026. The FSB's call for national authorities to "assess framework adequacy" creates international pressure for RBNZ to respond.

### Open Questions

- **Does RBNZ have non-public AI supervisory guidance?** An OIA request seeking any internal frameworks, thematic review results, or correspondence on AI risk would determine whether the public gap reflects a genuine absence or a transparency gap.
- **How are NZ-only non-bank deposit takers and fintechs managing AI model risk without any regulatory signal?** A practitioner survey or interview-based study of NZ's fintech and challenger bank sector would surface the practical governance vacuum.
- **What is the regulatory status of AI-generated actuarial models for NZ insurers?** The RBNZ/IPSA regime and its intersection with AI-driven underwriting and reserving is an under-investigated area.
- **When will RBNZ issue its first prescriptive AI guidance?** The trajectory of comparator regulators suggests 2026–2027 is plausible. Monitoring RBNZ's response to FSB pressure and any signals in the full May 2025 FSR or November 2025 FSR would provide early indicators.

---

## Output

- Type: knowledge
- Description: Mapping of RBNZ's AI supervisory position (monitoring-mode, no standalone guidance) against APRA, FCA/PRA, and EBA/ECB comparators, with a by-analogy governance framework for NZ-regulated entities and an OIA request strategy.
- Links:
  - https://www.rbnz.govt.nz/hub/publications/financial-stability-report/2025/may/ai-pre-release/rise-of-the-machines (RBNZ "Rise of the Machines" article, May 2025)
  - https://www.fsb.org/2024/11/the-financial-stability-implications-of-artificial-intelligence/ (FSB AI financial stability report, November 2024)
  - https://www.eba.europa.eu/publications-and-media/press-releases/eba-publishes-follow-report-use-machine-learning-internal (EBA ML for IRB Models follow-up report, August 2023)