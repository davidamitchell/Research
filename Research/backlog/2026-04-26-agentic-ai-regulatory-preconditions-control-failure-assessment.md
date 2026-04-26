---
title: "Regulatory and standards preconditions for agentic AI deployment: does incomplete access control and data governance constitute a control failure?"
added: 2026-04-26
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [agentic-ai, regulatory-compliance, control-failure, access-control, data-governance, regulated-banking, nz-rbnz, pci-dss, apra-cps-230, dora, iso-42001, nist, basel-committee, operational-risk]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
---

# Regulatory and standards preconditions for agentic AI deployment: does incomplete access control and data governance constitute a control failure?

## Research Question

Under applicable regulatory and standards frameworks — including Australian Prudential Regulation Authority (APRA) CPS 230, the EU Digital Operational Resilience Act (DORA), Payment Card Industry Data Security Standard (PCI-DSS) v4, ISO 42001, NIST SP 800-207, NIST SP 800-53, Basel Committee operational resilience principles, UK Financial Conduct Authority (FCA) and Prudential Regulation Authority (PRA) Artificial Intelligence (AI) guidance, and ISO 31000 — what organisational preconditions are required before deploying agentic AI automation, and does deploying agentic AI into an environment with incomplete least-privilege access control, an unclassified data estate, ungoverned citizen development, and unresolved systems capability debt constitute a current or foreseeable control failure?

## Scope

**In scope:**
- What each named framework requires, explicitly or implicitly, as organisational preconditions for safe agentic AI deployment
- Whether incomplete access control and data governance constitutes a control failure (not merely a governance gap) under each framework
- The specific language and provisions most useful for a board risk committee presentation and a regulator relationship context
- Gaps in the current regulatory landscape where the argument must rely on principles and inference rather than explicit provision
- Assessment of how regulators in comparable jurisdictions are likely to close those gaps
- Frameworks to assess: APRA CPS 230, DORA, PCI-DSS v4, ISO 42001, NIST SP 800-207 (Zero Trust Architecture (ZTA)), NIST SP 800-53, Basel Committee on Banking Supervision operational resilience principles, UK FCA and PRA AI guidance, ISO 31000
- Context: a New Zealand Crown-owned bank subject to Reserve Bank of New Zealand (RBNZ) prudential supervision, NZ Privacy Act 2020, and PCI-DSS; operating Microsoft 365 with Copilot and Copilot Studio and building agentic capability on AWS Bedrock; with existing access control debt, a partially classified data estate, a citizen development surface predating agentic AI, and systems capability gaps historically bridged by manual processes and ungoverned tooling

**Out of scope:**
- AI model safety or alignment frameworks not directly relevant to enterprise deployment governance
- Theoretical novelty of the synthesis argument (covered by the companion Q1 item)
- Empirical evidence on systems capability debt costs and citizen development causation (covered by the companion Q2 item)
- RBNZ-specific guidance (assumed as primary regulatory context; this item focuses on comparators and broader frameworks)
- Implementation details of specific technical controls

**Constraints:**
- Prioritise official framework text and official guidance documents over secondary commentary
- Assess each framework individually before synthesising cross-framework findings
- The "control failure vs. governance gap" distinction is legally and regulatorily significant — be precise about which frameworks support which characterisation
- Sources must be current versions of each framework (not superseded versions)

## Context

An argument is being constructed that deploying write-capable agentic AI automation into a regulated financial institution's environment while access control is incomplete, data is unclassified, citizen development is ungoverned, and systems capability debt remains unaddressed may constitute a control failure under existing frameworks — not merely a governance gap. The specific risk is that agentic AI removes the implicit rate-limiting controls that human-speed operation provides (attention, fatigue, friction, working hours) without replacing them with engineered controls, changing the risk profile of the existing access and data estate from chronic and manageable to acute and potentially catastrophic. This argument needs to be made credibly to a board risk committee and defensibly in a regulator relationship context. The organisation is a New Zealand Crown-owned bank; the regulatory environment is RBNZ-supervised, but APRA CPS 230 and DORA are relevant as Trans-Tasman and leading-jurisdiction comparators respectively, and the other frameworks (PCI-DSS v4, ISO 42001, NIST, Basel Committee, ISO 31000) are directly applicable.

## Approach

1. **Framework-by-framework precondition analysis** — For each named framework, extract the explicit provisions or principles that bear on: (a) preconditions for deploying automated systems acting on behalf of users; (b) access control and least-privilege requirements; (c) data classification and governance requirements; (d) third-party and technology risk management; (e) operational resilience and severe-but-plausible scenario requirements.
2. **Control failure vs. governance gap assessment** — For each framework, assess whether the described environment (incomplete access control, unclassified data, ungoverned citizen development, unresolved systems capability debt) constitutes a current control failure, a foreseeable control failure, or a governance gap; note the specific provisions or principles that support each characterisation.
3. **Board and regulator language extraction** — Identify the specific language, provisions, and cross-framework patterns most useful for a board risk committee presentation and a regulator relationship; prioritise provisions that are explicit, enforceable, or precedent-backed.
4. **Regulatory gap mapping** — Identify where the argument must rely on principles and inference rather than explicit provision; assess how each named regulator or standards body is likely to close those gaps based on consultation papers, speeches, and stated regulatory direction.
5. **APRA CPS 230 deep dive** — As the primary Trans-Tasman comparator and likely RBNZ influence, analyse CPS 230's treatment of technology risk, operational risk management systems, and the principle that critical operations must remain resilient to severe-but-plausible scenarios; assess applicability to the agentic AI deployment scenario.
6. **DORA deep dive** — As the leading jurisdiction standard for digital operational resilience, analyse DORA's Information and Communication Technology (ICT) risk management framework, third-party risk provisions, and the requirement for pre-deployment risk assessment; assess whether agentic AI operating across an unclassified data estate would satisfy DORA's ICT risk requirements.
7. **Zero trust and credential delegation** — Analyse NIST SP 800-207 specifically regarding agentic credential delegation operating across an environment with incomplete least-privilege implementation; assess whether this constitutes an architectural violation of zero trust principles and how that maps to regulatory control requirements.
8. **ISO 31000 risk management failure** — Assess whether the failure to evaluate and remediate known foundational risk (access control debt, data classification gaps, ungoverned citizen development) before deploying capability that amplifies that risk constitutes a risk management failure under ISO 31000's principles and guidelines.

## Sources

- [ ] [APRA CPS 230 — Operational Risk Management (effective 1 July 2025)](https://www.apra.gov.au/sites/default/files/2023-07/Prudential%20Standard%20CPS%20230%20Operational%20Risk%20Management.pdf) — APRA's operational risk management standard; primary Trans-Tasman regulatory comparator
- [ ] [DORA — EU Digital Operational Resilience Act (Regulation (EU) 2022/2554)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554) — EU digital operational resilience framework; leading jurisdiction standard
- [ ] [PCI Security Standards Council — PCI-DSS v4.0](https://www.pcisecuritystandards.org/document_library/) — Payment card data security standard; directly applicable to the organisation
- [ ] [ISO 42001:2023 — Artificial Intelligence Management Systems](https://www.iso.org/standard/81230.html) — AI management system standard; assess organisational preconditions for AI deployment
- [ ] [NIST SP 800-207 — Zero Trust Architecture (2020)](https://doi.org/10.6028/NIST.SP.800-207) — Zero trust architecture standard; assess credential delegation and least-privilege requirements
- [ ] [NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations](https://doi.org/10.6028/NIST.SP.800-53r5) — Security controls framework; assess automated system controls
- [ ] [Basel Committee on Banking Supervision — Principles for Operational Resilience (2021)](https://www.bis.org/bcbs/publ/d516.pdf) — Operational resilience principles; assess severe-but-plausible scenario requirements
- [ ] [UK FCA — Discussion Paper DP5/22: Artificial Intelligence and Machine Learning](https://www.fca.org.uk/publication/discussion/dp22-4.pdf) — UK FCA AI governance discussion paper; common law comparator jurisdiction
- [ ] [UK PRA — SS1/23: Model Risk Management Principles for Banks](https://www.bankofengland.co.uk/prudential-regulation/publication/2023/april/model-risk-management-principles-for-banks-ss) — PRA model risk management; relevant to AI model governance in banking
- [ ] [ISO 31000:2018 — Risk Management Guidelines](https://www.iso.org/standard/65694.html) — Risk management principles and guidelines; assess failure to remediate known foundational risk
- [ ] [RBNZ — Guidance on technology and cyber risk for banks](https://www.rbnz.govt.nz/regulation-and-supervision/oversight-of-banks/banking-supervision-handbook) — Primary regulatory context; baseline for comparator analysis
- [ ] [NIST AI RMF 1.0 — Artificial Intelligence Risk Management Framework](https://airc.nist.gov/Home) — US AI governance framework; assess agentic deployment preconditions

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
