---
title: "Global AI agent regulation in financial services: NFR obligations and low-code citizen-development controls"
added: 2026-04-24
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: []
tags: [artificial-intelligence, regulation, financial-services, governance, low-code, citizen-development, non-functional-requirements, eu-ai-act, apra, rbnz, fma, privacy-act, fair-trading, new-zealand-legislation, concentration-risk]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
---

# Global AI agent regulation in financial services: NFR obligations and low-code citizen-development controls

## Research Question

What regulatory obligations do financial-services regulators globally — including the European Union (EU), Australia, New Zealand (NZ), the United States (US), and the United Kingdom (UK) — impose on Artificial Intelligence (AI) agents and agentic systems used in regulated processes (credit, insurance, payments, and advice), what non-functional requirements (NFRs) such as explainability, auditability, robustness, and human oversight do those obligations mandate, and how do those requirements apply when business users create and deploy agents using low-code platforms such as Microsoft Copilot Studio?

## Scope

**In scope:**
- European Union AI Act (Regulation (EU) 2024/1689): high-risk AI system classification, conformity assessment obligations, technical documentation, human oversight, data governance, and change management requirements for AI in credit, insurance, and financial-advice processes.
- Australian Prudential Regulation Authority (APRA) CPG 234 (Information Security) and emerging APRA AI governance guidance: obligations on regulated entities deploying AI in material business processes.
- Reserve Bank of New Zealand (RBNZ) named financial-stability concerns attributable to AI: model error, privacy exposure, cyber-exposure, market distortions, and third-party AI concentration risk — all identified as live exposure vectors, not hypothetical.
- Financial Markets Authority (FMA) supervisory signals on AI governance for NZ-regulated entities.
- New Zealand existing legislation already imposing obligations on AI-enabled processes: Privacy Act 2020 (data handling and automated decision obligations), Fair Trading Act 1986 (FTA) (misleading or deceptive conduct by AI-driven communications), and Companies Act 1993 (directors' duties and accountability obligations for material AI-driven decisions).
- US federal financial regulators: Office of the Comptroller of the Currency (OCC), Consumer Financial Protection Bureau (CFPB), Federal Reserve, Federal Deposit Insurance Corporation (FDIC), and Securities and Exchange Commission (SEC) guidance and enforcement signals on AI in financial services.
- UK Financial Conduct Authority (FCA) and Prudential Regulation Authority (PRA) AI-specific guidance and the cross-sector AI and Digital Regulation principles.
- Canadian Office of the Superintendent of Financial Institutions (OSFI) B-10 Technology and Cyber Risk Guideline as a secondary comparator.
- Non-functional requirement categories commonly imposed across these frameworks: explainability, auditability, robustness, fairness/bias controls, security, privacy by design, and human oversight.
- Specific implications for low-code citizen-development scenarios: what obligations attach when a business user (not an engineer) builds and deploys an AI agent via a platform such as Microsoft Copilot Studio.

**Out of scope:**
- General data protection law (e.g. GDPR) except where it intersects directly with AI-specific requirements.
- Technical implementation details or feature documentation for Microsoft Copilot Studio itself.
- Non-financial-services sectors (health, education, law) except as direct analogues that illuminate financial-services obligations.
- AI model training and fine-tuning techniques unrelated to regulatory compliance obligations.

**Constraints:**
- Prioritise published, citable primary sources: legislative text, regulator guidance documents, consultation papers, and enforcement actions.
- Distinguish binding requirements from non-binding guidance (supervisory expectations, principles, and consultation proposals) with explicit labels.
- All sources must include URLs.
- Focus on requirements that are either already in force or scheduled to take effect within 24 months of the research date.

## Context

The EU AI Act classifies AI systems used in credit and insurance decisions as high-risk, imposing conformity assessments, technical documentation, human oversight, and change management obligations before deployment. APRA has published CPG 234 and is actively consulting on AI governance expectations for Australian Prudential-regulated entities. In New Zealand, RBNZ has specifically named model error, privacy exposure, cyber-exposure, market distortions, and third-party AI concentration risk as live financial-stability concerns — none of these are hypothetical. FMA has similarly signalled that AI in regulated processes is under supervisory scrutiny. Critically, NZ already has a binding legislative floor that applies regardless of whether AI-specific guidance has been issued: the Privacy Act 2020 imposes obligations on automated data handling; the Fair Trading Act 1986 (FTA) catches misleading or deceptive conduct by AI-driven communications; and the Companies Act 1993 creates directors' duties over material AI-driven decisions. Simultaneously, low-code AI agent platforms — most visibly Microsoft Copilot Studio — are being made available directly to business users in regulated financial services firms, who can build and deploy autonomous agents without engineering or compliance involvement. The practical risk is that the speed and accessibility of low-code tooling outpaces compliance readiness, exposing institutions to liability under both existing legislation and emerging AI-specific frameworks for systems that were never formally risk-assessed. Understanding which specific obligations apply — and whether they attach to the builder, the deployer, or the institution — is a prerequisite for safe adoption. A related governance item (`2026-04-24-business-led-low-code-agent-governance.md`) addresses conditions for durable value; this item addresses the binding regulatory floor.

## Approach

1. Map the EU AI Act high-risk AI system provisions applicable to financial services: identify the specific annexes and articles governing credit, insurance, and financial-advice AI systems; extract the conformity assessment, technical documentation, human oversight, and logging requirements; determine whether these obligations apply to a Copilot Studio-built agent deployed in those contexts.
2. Review APRA CPG 234 and any APRA AI governance consultation material to extract what Australian Prudential-regulated entities are required or expected to do when deploying AI in material business processes; compare the specificity of obligations to the EU AI Act.
3. Map the NZ existing legislative obligations that already apply to AI-enabled processes in financial services — Privacy Act 2020 (automated decision-making, data handling), Fair Trading Act 1986 (FTA) (misleading or deceptive conduct by AI-generated communications), Companies Act 1993 (directors' duties over material AI-driven decisions) — and extract what each requires of a regulated entity deploying an AI agent today, before any NZ-specific AI regulation is enacted.
4. Search FMA and RBNZ published speeches, consultation papers, and guidance notes (2022–2026) to document the RBNZ's named financial-stability concerns (model error, privacy exposure, cyber-exposure, market distortions, third-party AI concentration risk) and the FMA's supervisory signals on AI governance; characterise the exposure these concerns create for a bank deploying ungoverned agents in process-critical workflows.
5. Survey US federal financial regulator guidance: OCC Model Risk Management (SR 11-7), CFPB AI guidance, the joint agency statement on AI in financial services, and any recent enforcement actions related to algorithmic decision-making in credit or insurance.
6. Review UK FCA and PRA AI-specific guidance, including the FCA/PRA Discussion Paper DP5/22 on AI and ML in UK financial services, and the cross-sector AI and Digital Regulation principles published by the UK's Digital Regulation Cooperation Forum (DRCF).
7. Extract the common NFR categories that appear across two or more frameworks and characterise the minimum compliance posture they collectively imply for an institution deploying AI agents in regulated processes.
8. Synthesise the specific implications for low-code citizen-development: which frameworks address the builder–deployer–institution responsibility split; what controls (approval gates, risk classification, documentation, testing) must exist before a business user can legitimately deploy an agent in a regulated process; and whether any framework has issued specific guidance on low-code or no-code AI tooling.

## Sources

Starting points — papers, articles, videos, repos, docs.
**Every source must include a URL.** Use `[Display Name](https://url)` for named sources or a bare `https://url` for direct links. Sources without URLs cannot be verified or linked on the site.

- [ ] [EU AI Act full text (Regulation (EU) 2024/1689)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) — Annexes III, VIII, and Articles 9–17 covering high-risk system obligations; human oversight (Article 14); technical documentation (Annex IV); conformity assessment (Article 43)
- [ ] [EU AI Act high-risk system classification guidance — European Commission](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) — Commission guidance on which AI use cases fall within Annex III high-risk classification
- [ ] [APRA CPG 234 Information Security (July 2019)](https://www.apra.gov.au/sites/default/files/cpg_234_information_security_july_2019.pdf) — operative guidance on information security risk management for APRA-regulated entities; applicable to AI system security controls
- [ ] [APRA — AI in financial services — Discussion Paper or Letters (2024–2026)](https://www.apra.gov.au/) — search APRA website for AI governance consultation material and supervisory letters
- [ ] [RBNZ — AI in regulated processes — speeches and guidance (2023–2026)](https://www.rbnz.govt.nz/) — Reserve Bank speeches and guidance notes on AI governance expectations; named financial-stability concerns: model error, privacy, cyber-exposure, market distortions, third-party AI concentration risk
- [ ] [FMA — AI in regulated processes — speeches and guidance (2023–2026)](https://www.fma.govt.nz/) — Financial Markets Authority NZ speeches, consultation papers, and guidance on AI in regulated financial services
- [ ] [New Zealand Privacy Act 2020](https://www.legislation.govt.nz/act/public/2020/0031/latest/LMS23223.html) — obligations on automated data handling and decisions affecting individuals; directly applicable to AI agents processing personal information
- [ ] [Fair Trading Act 1986 (New Zealand)](https://www.legislation.govt.nz/act/public/1986/0121/latest/DLM96439.html) — prohibition on misleading or deceptive conduct; applies to AI-generated communications in financial services
- [ ] [Companies Act 1993 (New Zealand)](https://www.legislation.govt.nz/act/public/1993/0105/latest/DLM319570.html) — directors' duties relevant to accountability for material AI-driven decisions made by or on behalf of the company
- [ ] [OCC Model Risk Management Guidance (SR 11-7 equivalent — OCC Bulletin 2011-12)](https://www.occ.gov/news-issuances/bulletins/2011/bulletin-2011-12.html) — US model risk management framework applicable to AI models in credit and financial decisions
- [ ] [Joint Agency Statement on AI in Financial Services (US federal agencies, 2021)](https://www.occ.gov/news-issuances/news-releases/2021/nr-ia-2021-100a.pdf) — OCC, FDIC, CFPB, NCUA, Federal Reserve joint request for information on AI in financial services
- [ ] [CFPB — AI and algorithmic decision-making in consumer financial services (2022–2025)](https://www.consumerfinance.gov/data-research/research-reports/) — Bureau guidance and enforcement signals on explainability obligations and adverse-action requirements for AI credit decisions
- [ ] [UK FCA/PRA Discussion Paper DP5/22 — AI and Machine Learning in UK financial services (2022)](https://www.bankofengland.co.uk/prudential-regulation/publication/2022/october/machine-learning-in-uk-financial-services) — PRA/FCA joint paper on AI governance expectations; data governance, model risk, explainability
- [ ] [UK DRCF — AI and Digital Regulation cross-sector principles (2023)](https://www.gov.uk/government/publications/digital-regulation-cooperation-forum-workplan-2023-to-2024) — cross-regulator AI principles including FCA, PRA, ICO, CMA
- [ ] [OSFI B-10 Technology and Cyber Risk Guideline (2023)](https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/technology-cyber-risk-guideline) — Canadian AI and technology risk expectations for federally regulated financial institutions
- [ ] [NIST AI Risk Management Framework (AI RMF) 1.0](https://doi.org/10.6028/NIST.AI.100-1) — US voluntary framework; widely cited in regulatory guidance as NFR reference; Map, Measure, Manage functions

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

1.
2.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

- **Assumption:** ... **Justification:** ...

### Analysis

### Risks, Gaps, and Uncertainties

-

### Open Questions

-

---

## Output

*(Fill in when completing — what was produced as a result of this research?)*

- Type: # skill | tool | agent | knowledge | backlog-item
- Description:
- Links:
