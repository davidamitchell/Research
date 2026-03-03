---
title: "AI for Control Testing, Gap Identification, and Policies/Standards Reviews"
added: 2026-02-28
status: completed
priority: high
tags: [ai-strategy, grc, control-testing, compliance-automation, internal-audit, risk-management, financial-services]
started: 2026-03-03
completed: 2026-03-03
output: [knowledge]
---

# AI for Control Testing, Gap Identification, and Policies/Standards Reviews

## Research Question

Which organisations are using AI to automate control testing, identify control gaps, or conduct policies and standards reviews — and what does the current vendor, practitioner, and regulatory landscape look like for AI-assisted assurance in financial services?

## Scope

**In scope:**
- Automated control testing: AI systems that sample, execute, or evaluate control performance continuously or periodically
- Control gap identification: AI analysis of control frameworks against current practice to surface deficiencies
- Policies and standards reviews: AI tools that parse internal policies, regulatory standards, and frameworks to identify gaps, conflicts, or outdated provisions
- Vendor landscape: who is building and selling these tools (e.g. AuditBoard, Galvanize/Diligent, ServiceNow GRC, KPMG Clara, Deloitte OmniAI, PwC Halo, EY Helix)
- Practitioner case studies: how internal audit, compliance, and operational risk functions are deploying these tools
- NZ financial services context: RBNZ-supervised entities, Big-4 audit firms operating in NZ

**Out of scope:**
- AI as a risk management tool in the credit/fraud/AML sense — covered by `ai-strategy-risk-reduction-focus.md`
- AI security applications — covered by `ai-strategy-security-focus.md`
- General GRC platform capabilities not involving AI

**Constraints:** Focus on production deployments or credible pilots, not vendor marketing claims. Prefer disclosed outcomes and governance models over white-paper descriptions.

## Context

The AI strategy research item (completed 2026-02-28) identified a four-type use-case typology. Control testing automation sits primarily in Type 2 (agentic builders that generate artefacts) and Type 3 (delegated authority agents — AI making a determination such as "this control is operating effectively"). The governance architecture for Type 3 control testing agents is an open question: who reviews AI-generated assurance conclusions, and what is the regulatory acceptability of AI-assisted audit evidence?

This is a high-priority area because: (a) it is commercially active now, not aspirational; (b) it affects the external audit and internal assurance functions of regulated entities; (c) it directly intersects with RBNZ BS11 (outsourcing), RBNZ BS2A (internal capital adequacy), and DORA (ICT risk controls testing) obligations.

## Approach

1. **Vendor landscape scan** — identify the 8–10 major platforms and what specific AI-assisted assurance capabilities they claim (continuous control monitoring, policy-to-standard gap analysis, automated testing workpaper generation).
2. **Practitioner evidence** — find disclosed case studies from internal audit, compliance, or risk functions describing actual deployments: what was automated, what outcomes were achieved, what governance was in place.
3. **Regulatory acceptability** — review guidance from audit standard-setters (IAASB, PCAOB, AUASB) and prudential regulators on AI-generated assurance evidence. Is AI-assisted control testing evidence acceptable? What oversight is required?
4. **Gap identification tooling** — specifically focus on AI tools that ingest regulatory standards (e.g. DORA, PCI-DSS, NIST CSF) and compare against internal policy/control inventories to surface gaps.
5. **NZ applicability** — which vendors, frameworks, and governance models are directly relevant to NZ-supervised institutions?

## Sources

- [ ] IAASB: Technology position papers and ISA revisions for AI use in audit (2023–2025)
- [ ] PCAOB: Inspection findings on automated audit tools
- [ ] ISACA: COBIT and audit automation guidance
- [ ] IIA (Institute of Internal Auditors): AI in internal audit position papers (2024–2025)
- [ ] AuditBoard, Diligent (Galvanize), LogicGate, ServiceNow GRC product documentation
- [ ] Big-4 audit firm publications: KPMG Clara Audit, EY Helix, PwC Halo, Deloitte OmniAI
- [ ] DORA Article 24–27: ICT operational resilience testing — AI-assisted testing implications
- [ ] RBNZ: Any supervisory expectations on automated assurance or model-generated evidence
- [ ] Gartner / Forrester: GRC platform market reports 2024–2025

---

## Findings

### Executive Summary

AI-assisted control testing and compliance assurance is commercially active in 2024–2025, not aspirational. A tiered vendor landscape has emerged: standalone GRC platforms (AuditBoard, ServiceNow, LogicGate), Big 4 proprietary platforms (KPMG Clara, EY.ai, PwC Aura, Deloitte Omnia), and specialised regulatory intelligence tools (Regology). Disclosed outcomes from production deployments include 60% faster audit cycles, $2M annual savings, and 90% reductions in documentation burden. Regulatory standard-setters (IAASB, PCAOB, IIA) are actively updating frameworks to accommodate AI-generated assurance evidence, but no regulator has yet declared AI-assisted control testing evidence unconditionally acceptable — human oversight and professional judgment remain mandatory. For NZ financial institutions, the RBNZ has raised AI financial stability concerns but has not published AI-specific assurance guidance; existing operational risk and BS11 outsourcing frameworks apply.

### Key Findings

1. **The GRC AI market is production-active.** AuditBoard launched "Accelerate" (2025) integrating agentic AI for continuous monitoring and evidence gathering; ServiceNow GRC offers AI-powered automated control testing; LogicGate introduced a dedicated AI Governance Solution (April 2024) including automated cross-framework gap analysis. These are deployed products, not pilots.

2. **Big 4 audit firms have deployed AI at scale.** EY integrated AI across 160,000+ audit engagements (2025), deploying automated tie-out checks and guided control workflows. KPMG Clara is used by 90,000 auditors for transaction scoring and automated substantive testing design. Deloitte Omnia and PwC Aura support agentic AI for multi-step audit procedures including controls testing.

3. **Disclosed outcomes are material.** A documented global bank deployment reported: 60% faster audit cycles, $2M annual savings, 40% GRC cost reduction, 90% reduction in documentation burden. A North American lender using AI compliance monitoring reduced violations by 47% and cut audit prep time by 80% while achieving 100% population coverage (vs. prior 3% manual sample). HSBC's ML-based transaction monitoring detected 2–4× more suspicious activity and reduced false alerts by 60%.

4. **AI enables full-population testing, replacing sampling.** The primary structural change AI brings to control testing is elimination of sampling: AI-enabled systems can test 100% of transactions continuously, replacing periodic point-in-time sampling. The IIA's September 2024 AI Auditing Framework update explicitly addresses this shift and positions it as an improvement to audit quality.

5. **IAASB published a Technology Position Statement in October 2024** with eight guiding actions, committing to remove barriers to AI use in ISAs, introduce technology-enabled procedure requirements, and run a continuous gap analysis ("Catalog of Issues") of existing standards. No AI-specific ISA revision has been finalised; the Position is a strategic commitment to act, not yet a changed standard.

6. **PCAOB's July 2024 GenAI Spotlight found that GenAI use in external audits is currently limited to administrative tasks**, not core control testing. Recurring PCAOB inspection deficiencies persist in IT control testing and reliance on system-generated evidence — problems predating AI that AI adoption has not yet resolved. The PCAOB explicitly states AI must augment, not replace, professional judgment.

7. **The IIA's 2024 Global Internal Audit Standards (effective January 2025) require technology integration** in internal audit planning and execution. The IIA AI Auditing Framework (September 2024 update) provides a Three Lines Model structure for AI governance and audit, including checklists for AI strategy, data security, vendor controls, and ongoing monitoring.

8. **Regulatory acceptability of AI-generated assurance evidence is unsettled.** Neither IAASB, PCAOB, nor AUASB has issued a definitive position on whether AI-generated control testing outputs constitute sufficient audit evidence under existing ISA 500 series standards. The current consensus is that auditors must document AI tool governance, understand outputs, apply professional skepticism, and retain final judgment — meaning AI evidence is acceptable as support, not as a standalone conclusion.

9. **DORA (effective January 17, 2025) implicitly requires automation for ICT resilience testing coverage.** DORA mandates comprehensive, risk-based resilience testing programs including vulnerability assessments, scenario testing, and threat-led penetration testing every three years for significant institutions. The breadth of DORA's testing obligations creates a compliance driver to adopt AI and automated tooling — manual-only approaches are practically insufficient at the required scale and frequency.

10. **The RBNZ has not published AI-specific assurance or control testing guidance.** The May 2025 RBNZ Financial Stability Report pre-release "Rise of the Machines" flagged AI financial stability risks (model opacity, vendor concentration, data integrity) and signalled that existing prudential frameworks (BS11 outsourcing, operational risk) apply to AI deployments. No standalone AI rulebook exists. The RBNZ expects boards to demonstrate AI risk is being managed within current frameworks.

11. **NZ-specific AI control testing deployments are not publicly disclosed.** Major NZ financial institutions (banks, insurers) are subject to the same international vendor offerings as global peers but no NZ-specific case studies or RBNZ-directed programmes are publicly documented. Big 4 firms operate NZ practices with access to global AI audit platforms (KPMG Clara, EY.ai, PwC Aura), making international AI capabilities available to NZ-supervised entities.

12. **Governance architecture for Type 3 AI assurance determinations is an open industry question.** When AI makes a determination ("this control is operating effectively"), the review and escalation path — who signs off, what documentation is required, what constitutes adequate human oversight — is not yet standardised across the industry. Vendors and audit firms are developing proprietary governance frameworks but no authoritative standard exists.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| AuditBoard Accelerate agentic AI in production 2025 | AuditBoard press release (prnewswire.com, Oct 2024; BusinessWire Oct 2024) | high | Product announcement with feature descriptions |  
| EY integrated AI across 160,000+ audit engagements | EY Newsroom press release, April 2025 | high | Primary source from the firm |
| KPMG Clara used by 90,000 auditors | Accountancy Age, July 2024; KPMG "All eyes on AI in audit 2024" | high | Consistent across two sources |
| Global bank: 60% faster audits, $2M savings, 40% GRC cost reduction | skan.ai CCM ebook (vendor white paper) | medium | Vendor-sourced; outcome claims not independently verified |
| North American lender: 47% violations drop, 80% audit prep reduction | rccbpo.com case study | medium | Vendor-sourced; methodology not detailed |
| HSBC: 2–4× fraud detection, 60% false alert reduction | Google Cloud blog (HSBC/Google Cloud partnership) | high | Co-published by financial institution |
| IAASB Technology Position Statement October 2024, 8 guiding actions | IAASB official publications (iaasb.org) | high | Primary regulatory source |
| PCAOB GenAI in audits limited to admin tasks (July 2024) | PCAOB Staff Spotlight, July 2024 (pcaobus.org) | high | Primary regulatory source |
| IIA AI Auditing Framework September 2024 update | IIA official publication (theiia.org) | high | Primary professional standards source |
| DORA effective January 17, 2025; TLPT every 3 years for significant institutions | EBA DORA pages; Skadden analysis | high | Primary regulation + credible legal analysis |
| RBNZ no standalone AI rulebook; existing frameworks apply | RBNZ FSR pre-release "Rise of the Machines" (May 2025); insurance/fintech press | high | Primary regulatory communication |
| LogicGate AI Governance Solution with automated gap analysis (April 2024) | LogicGate press release (prnewswire.com, April 2024); SiliconANGLE | high | Product launch with feature description |

### Assumptions

- **Assumption:** Vendor-reported case study outcomes (skan.ai, rccbpo.com) are directionally accurate even if not independently verified. **Justification:** Multiple independent vendor sources report consistent order-of-magnitude improvements; the direction of effect (faster, cheaper, more coverage) is corroborated by Big 4 firm reports and academic literature on continuous monitoring.
- **Assumption:** RBNZ BS11 and operational risk standards are the primary NZ regulatory frameworks governing AI assurance deployments in financial services. **Justification:** RBNZ has explicitly stated that existing frameworks apply; BS11 covers outsourced services (including AI vendors) and operational risk frameworks cover model risk.
- **Assumption:** DORA is not directly applicable to NZ-domiciled entities. **Justification:** DORA is EU regulation. However, NZ-registered subsidiaries of EU parent groups may be subject to group-level DORA compliance requirements, and DORA is influencing global assurance standards that will affect NZ audit firms.

### Analysis

The evidence resolves into three tiers of deployment maturity:

**Tier 1 — Production at scale (high confidence):** Transaction monitoring, anomaly detection, and AML controls testing. HSBC and similar institutions have deployed these in production with disclosed outcomes. The technology is mature, the regulatory position is settled (these are analytical tools, not assurance conclusions), and the governance model is clear (human review of flagged items).

**Tier 2 — Production with governance questions (medium confidence):** Audit workpaper generation, control testing documentation, evidence gathering, and policy-to-standard gap analysis. Big 4 platforms and GRC vendors are deploying these. The technology works; the regulatory question is whether AI-generated outputs constitute audit evidence under ISA standards. The current answer is "yes, with appropriate oversight" but the specifics are not yet codified.

**Tier 3 — Early stage (lower confidence):** Agentic AI making assurance determinations ("this control is effective") without contemporaneous human review. This is the frontier that PCAOB, IAASB, and IIA are watching. No standard-setter has approved autonomous assurance conclusions.

The PCAOB's finding that GenAI is limited to administrative tasks in external audits (July 2024) should be read against Big 4 claims of AI in control testing: the gap is likely explained by the distinction between GenAI specifically (LLM-based tools, which are in admin use) and ML/analytics tools (which are in substantive use for transaction scoring, anomaly detection, and evidence gathering). Both are "AI" but the regulatory caution applies primarily to generative outputs.

For NZ financial institutions, the actionable conclusion is: international AI assurance tooling is accessible via Big 4 audit firms and GRC vendors; the primary governance requirement is to ensure AI tools are explainable, outputs are reviewed by qualified professionals, and vendor relationships are covered under existing BS11 third-party risk management frameworks. The RBNZ has not introduced new requirements, but the expectation that boards can demonstrate AI risk management within existing frameworks creates a de facto assurance obligation.

### Risks, Gaps, and Uncertainties

- **Regulatory codification lag:** IAASB's Technology Position is a commitment to update standards, not updated standards. The gap analysis process is ongoing. Until ISA revisions are finalised, practitioners are working without clear rules on AI evidence acceptability.
- **Vendor outcome claims are largely self-reported:** The $2M savings and 60% efficiency figures come from vendor white papers. Independent academic evaluation of production AI control testing deployments is sparse.
- **NZ-specific data is absent:** No publicly disclosed NZ financial institution AI assurance programme exists. The NZ context is inferred from international evidence and RBNZ's general AI risk statements.
- **Type 3 governance (autonomous determinations) is unsolved:** The industry is building governance frameworks for AI assurance conclusions in real time. Early frameworks from IIA and Big 4 firms are proprietary and non-comparable.
- **DORA applicability to NZ entities is indirect:** NZ entities in EU parent groups may face DORA compliance pressures not yet reflected in NZ supervisory guidance.

### Open Questions

- When the IAASB finalises ISA revisions to accommodate AI evidence, what documentation and oversight requirements will be codified? Will the standard require specific AI model governance disclosures in audit workpapers?
- Does RBNZ intend to publish AI-specific prudential guidance (similar to APRA CPG 234 for cyber)? The May 2025 FSR commentary suggests awareness but no timeline.
- What is the minimum viable governance model for Type 3 AI control testing in a NZ-supervised entity — specifically, what constitutes adequate human oversight of an AI-generated assurance conclusion?
- How does AI control testing interact with external auditor reliance on internal audit work (ISA 610)? If internal audit uses AI, does that change the external auditor's assessment of the quality of internal audit's work?

---

## Output

- Type: knowledge
- Description: Landscape of AI-assisted control testing and assurance: vendor tiers, Big 4 deployments, measurable outcomes, regulatory standard-setter positions (IAASB, PCAOB, IIA), NZ-specific context (RBNZ), and DORA implications. Identifies governance gaps and open questions for NZ financial institutions.
- Links:
  - https://www.iaasb.org/publications/technology-position-statement (IAASB Technology Position Statement, October 2024)
  - https://auditboard.com/blog/auditboard-launches-accelerate-delivering-enterprise-grade-ai-automation-for-grc-teams (AuditBoard Accelerate launch)
  - https://www.rbnz.govt.nz/hub/publications/financial-stability-report/2025/may/ai-pre-release/rise-of-the-machines (RBNZ FSR AI pre-release, May 2025)
