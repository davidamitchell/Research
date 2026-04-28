---
title: "AI for Control Testing, Gap Identification, and Policies/Standards Reviews"
added: 2026-03-03T02:26:48+00:00
status: completed
priority: high
tags: [ai-strategy, grc, control-testing, compliance-automation, internal-audit, risk-management, financial-services]
started: 2026-03-03T02:26:48+00:00
completed: 2026-03-03T02:26:48+00:00
output: [knowledge]
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
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

- [x] IAASB: Technology position papers and ISA revisions for AI use in audit (2023–2025) — https://www.iaasb.org/
- [x] PCAOB: Inspection findings on automated audit tools — https://pcaobus.org/
- [ ] ISACA: COBIT and audit automation guidance — https://www.isaca.org/resources/cobit
- [x] IIA (Institute of Internal Auditors): AI in internal audit position papers (2024–2025)
- [x] AuditBoard, Diligent (Galvanize), LogicGate, ServiceNow GRC product documentation
- [x] Big-4 audit firm publications: KPMG Clara Audit, EY Helix, PwC Halo, Deloitte OmniAI
- [ ] DORA Article 24–27: ICT operational resilience testing — AI-assisted testing implications — https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R2554
- [x] RBNZ: Any supervisory expectations on automated assurance or model-generated evidence — https://www.rbnz.govt.nz/
- [ ] Gartner / Forrester: GRC platform market reports 2024–2025

---

## Findings

### Executive Summary

AI-assisted control testing and regulatory gap analysis have moved from aspiration to active commercial deployment. Every major GRC platform (AuditBoard, ServiceNow, Diligent, LogicGate) and all four Big-4 audit firms (KPMG Clara, EY Helix, PwC Halo/Aura, Deloitte Omnia) have production AI capabilities for automated control testing, workpaper generation, and continuous monitoring as of 2024–2025. The regulatory standard-setter position — from IAASB, PCAOB, and FRC — is that AI-generated audit evidence is acceptable provided it is validated, documented, and subject to human professional judgment; no regulator has prohibited it. RBNZ has flagged systemic risks from AI adoption broadly but has not issued prescriptive guidance on AI-assisted assurance; the intersection with BS11 outsourcing obligations remains the primary governance constraint for NZ-supervised entities.

### Key Findings

1. **GRC platforms deliver continuous control monitoring in production.** AuditBoard's Accelerate (launched 2025) automates sample selection, evidence gathering, and workpaper generation for internal audit teams. ServiceNow GRC deploys AI agents for end-to-end compliance workflows, continuous monitoring, and anomaly detection. Vanta and Drata automate up to 90% of evidence collection with hourly test execution across SOC 2, ISO 27001, HIPAA, and PCI-DSS frameworks.

2. **All four Big-4 firms have embedded AI in their external audit platforms.** KPMG Clara integrates generative AI for risk assessment, substantive testing, and documentation review, paired with MindBridge transaction scoring for anomaly detection. EY Helix deploys GL and cycle analyzers for full-population transactional testing. PwC Halo for Journals uses ML to flag unusual transactions. Deloitte Omnia deploys GenAI and agentic AI for documentation review, financial statement navigation, and memo drafting. All four maintain human-in-the-loop requirements for final audit conclusions.

3. **Regulatory gap analysis has a mature specialist vendor market.** Deloitte's automated gap analysis tool uses GenAI to compare regulatory text (DORA, EU AI Act, CRR) against internal policies, outputting structured gap reports. Kodex AI maps DORA, PSD3, and custom frameworks against internal policies with regulatory traceability. Trustero completes full gap assessments in under two hours against DORA and NIST, replacing consulting projects that previously took months. RiskCognition reports >92% accuracy versus manual review in European bank DORA deployments.

4. **IAASB formally adopted a Technology Position in October 2024.** The position mandates ongoing monitoring and updating of standards to address AI and machine learning in audit. Under existing ISAs, AI-generated evidence is acceptable if it meets the "sufficient and appropriate" standard (ISA 500). Auditors must validate tools before use, apply professional skepticism to outputs, and document their assessment proportionally to tool complexity. ISQM 1 quality management standards govern firm-level certification of automated tools.

5. **PCAOB is updating standards to address AI in audit.** In 2024 the PCAOB issued a spotlight publication on AI use and signalled amendments to AS 1105 (audit evidence) and AS 2301 (audit procedures). The aggregate Part I.A deficiency rate for Big 4 firms fell to 20% in 2024 (from 26% in 2023), partially attributable to technology adoption. The PCAOB's position is that AI supplements but does not replace human auditors; professional skepticism and quality controls must encompass AI tool outputs.

6. **No standard-setter has prohibited AI-generated assurance evidence; all require human oversight.** The FRC published landmark guidance in 2025 providing illustrative examples of AI-enabled audit evidence and required certification/testing processes. The universal governance model is: AI executes testing and generates outputs; a qualified human reviews, applies judgment, and takes ownership of the conclusion. Delegation of the conclusion itself to AI — with no human review — is not accepted under any current framework.

7. **IIA's September 2024 AI Auditing Framework provides the practitioner governance model.** The updated framework covers AI strategy, cyber risks, vendor controls, ethics, bias, and staff training, organised along the Three Lines Model. It addresses both organisations auditing AI and organisations deploying AI in internal audit itself. AI use in internal audit more than doubled in adoption (15% to 40% within a year per IIA data), with upskilling identified as the primary constraint on further adoption.

8. **Disclosed practitioner case studies show meaningful efficiency gains.** Baker Tilly documented a financial institution using GenAI to automate compliance testing, extracting unstructured data and mapping it into compliance models with real-time monitoring. RSM documented a global bank using intelligent automation for control testing, shifting auditors from data gathering to risk-centric fieldwork. Global banks have implemented centralised AI model inventory platforms, enabling transparency and auditability of AI decision-making across compliance, risk, and audit functions.

9. **RBNZ has flagged AI systemic risks but has not issued prescriptive assurance guidance.** The May 2025 Financial Stability Report "Rise of the Machines" identifies third-party AI concentration risk, model transparency, and data governance as primary concerns. RBNZ expects regulated entities to maintain transparency and auditability of AI outputs, validate results before they inform compliance actions, and manage AI vendor dependency under BS11 outsourcing obligations. No specific standard for AI-generated audit evidence has been issued.

10. **The governance gap for Type 3 agents (delegated authority) remains open.** Current frameworks are explicit that AI can generate testing workpapers, sample recommendations, and gap analyses (Type 2), but the final determination that a control is "operating effectively" must be made or owned by a qualified human. The governance question — what reviewer competency is required, what documentation suffices, and whether the determination constitutes an outsourced function under BS11 — is not yet resolved by any regulator.

11. **NZ-supervised entities can access the full vendor and Big-4 landscape.** All four Big-4 firms operate in NZ and their global AI audit platforms are deployed here. ServiceNow, AuditBoard, LogicGate, Vanta, and Drata are all available to NZ enterprises. Specialist DORA gap analysis tools have less immediate NZ relevance (DORA is EU-specific), but the equivalent analysis against RBNZ standards (BS11, BS2A) could be built on the same tooling approach.

12. **Full-population testing is displacing sample-based testing in automated control environments.** Where AI can access complete transaction populations, audit approaches have shifted from statistical sampling to exhaustive testing. This improves control assurance but raises new questions about what constitutes a meaningful control test and what the auditor adds when the system executes and evaluates every transaction.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| AuditBoard Accelerate automates sample selection, evidence gathering, workpaper generation | AuditBoard product page; PR Newswire launch announcement 2025 | high | Production product, verifiable feature list |
| ServiceNow AI agents provide end-to-end compliance workflows and continuous monitoring | ServiceNow Audit Management product page; XenonStack analysis | high | Production platform |
| Vanta/Drata automate up to 90% of evidence collection with hourly test execution | Vanta product documentation; Bright Defense comparison | high | Vendor-stated; corroborated by independent comparison |
| KPMG Clara embeds GenAI for risk assessment, substantive testing, and documentation | KPMG press release July 2024; Accountancy Age | high | Disclosed by KPMG with July 2024 launch date |
| EY Helix deploys GL and cycle analyzers for full-population transactional testing | EY Helix product page | high | Long-standing product; specific capabilities disclosed |
| Deloitte Omnia deploys agentic AI for documentation and risk identification | Deloitte press release 2025 | high | Disclosed by Deloitte |
| Deloitte automated gap analysis tool compares DORA/EU AI Act against internal policies | Deloitte Germany product page | high | Publicly documented product |
| RiskCognition reports >92% accuracy vs manual review in European bank DORA deployments | RiskCognition case study | medium | Single vendor case study; not independently verified |
| Trustero completes gap assessments in <2 hours vs multi-month consulting projects | Trustero blog | medium | Vendor claim; plausible given NLP-based automation |
| IAASB Technology Position adopted October 2024 | IAASB website announcement | high | Primary source |
| AI-generated evidence acceptable under ISA 500 if sufficient, appropriate, validated | IAASB standards; CPAB-CCRC 2024 publication | high | Consistent across multiple standard-setter sources |
| PCAOB signalling AS 1105 and AS 2301 amendments for AI | SEC speech August 2024; PCAOB publication | high | Primary source |
| Big 4 deficiency rate fell to 20% in 2024, partially attributed to technology | PCAOB preliminary inspection results | high | PCAOB-disclosed |
| FRC published landmark AI audit guidance in 2025 | FRC news release | high | Primary source |
| IIA AI Auditing Framework updated September 2024 | IIA website; Weaver implementation guide | high | Primary source corroborated |
| AI internal audit adoption rose from 15% to 40% | IIA CEO voice article | medium | Survey-based; self-reported |
| Baker Tilly financial institution GenAI compliance testing case study | Baker Tilly insights publication | high | Named practitioner case study |
| RBNZ "Rise of the Machines" May 2025 identifies third-party AI concentration risk | RBNZ Financial Stability Report May 2025 | high | Primary source |
| RBNZ BS11 applies to AI vendor relationships as outsourcing | RBNZ BS11 standard + RBNZ AI commentary | medium | Inference from existing BS11 scope; RBNZ has not explicitly confirmed |
| No regulator has prohibited AI-generated audit evidence | Review of IAASB, PCAOB, FRC, RBNZ outputs | high | Confirmed by absence of prohibition across all reviewed sources |

### Assumptions

- **Assumption:** Vendor-disclosed capabilities reflect production features, not roadmap items. **Justification:** Only features with named launch dates or verifiable product pages were included; roadmap items were excluded from findings.
- **Assumption:** "Human-in-the-loop" requirements described in regulatory guidance are enforced at the professional judgment level, not codified as specific procedural rules. **Justification:** No reviewed standard specifies exactly what human review must consist of; IAASB and PCAOB use principles-based language about "professional skepticism" and "ownership of conclusions."
- **Assumption:** RBNZ BS11 outsourcing requirements apply to AI-as-a-service control testing tools. **Justification:** BS11 applies to material outsourcing of significant functions; automated control testing affecting regulatory reporting would likely qualify, but RBNZ has not explicitly confirmed this interpretation.
- **Assumption:** NZ-supervised entities can access global vendor platforms without restriction. **Justification:** No NZ-specific import or data sovereignty restriction on GRC SaaS identified, though data residency obligations may limit where testing data can be processed.

### Analysis

The vendor and practitioner landscape has bifurcated. Horizontal GRC platforms (AuditBoard, ServiceNow, Vanta, Drata, LogicGate) focus on continuous automated control monitoring — evidence collection, exception flagging, and test execution at scale. Specialist gap analysis tools (Deloitte, Kodex AI, Trustero, RiskCognition) focus on comparing regulatory text against internal policy inventories using NLP. Big-4 audit firms sit across both: they use proprietary platforms for external audit (Clara, Helix, Halo, Omnia) and have built or licensed specialist gap analysis tools for advisory engagements.

The regulatory acceptability question has been answered in principle but not in detail. Every major standard-setter has confirmed that AI-generated evidence is acceptable under existing frameworks, provided it is validated, documented, and subject to human professional judgment. The outstanding gap is granularity: what competency must the reviewing human have? What documentation satisfies professional skepticism requirements when the AI generated the test procedure, executed it, and drafted the conclusion? These questions are being addressed incrementally through guidance (FRC 2025, IAASB 2024–2026 work programme) rather than standard revision.

The RBNZ position reflects the financial stability angle rather than an assurance standard position. RBNZ is concerned about systemic risk from AI concentration and about the reliability of AI model outputs affecting financial decisions — not specifically about whether AI-generated audit workpapers meet evidence standards. For NZ-supervised entities, the practical constraint is BS11 outsourcing governance: if AI control testing is delivered as a third-party service (SaaS), the outsourcing risk management programme must cover it. This is a well-understood governance requirement, not a novel barrier.

The most consequential open question is governance for Type 3 agents: AI that makes the determination that a control is operating effectively, not just AI that generates the evidence for a human to assess. Current frameworks stop short of endorsing this. The practitioner trajectory — moving from sampling to full-population testing, from workpaper generation to conclusion drafting — is pushing toward Type 3 faster than governance frameworks are adapting. The next 12–24 months will likely see standard-setters (IAASB, PCAOB) issue more specific guidance on what human review must consist of when AI has performed the entire test cycle.

### Risks, Gaps, and Uncertainties

- **Regulatory granularity gap:** IAASB and PCAOB have issued principles but not procedural standards for AI-assisted audit. The specific documentation, competency, and review requirements are undefined. Firms are applying their own interpretations under professional judgment.
- **RBNZ BS11 interpretation:** Whether AI-as-a-service control testing constitutes a material outsourced function under BS11 has not been confirmed by RBNZ. Entities deploying SaaS GRC tools should seek legal and regulatory affairs guidance on this classification.
- **Vendor claim verification:** Several quantitative claims (90% evidence automation, 92% accuracy, 2-hour gap assessments) come from vendor marketing materials or single case studies. Independent academic verification is limited.
- **NZ practitioner evidence thin:** No disclosed NZ-specific case studies of AI control testing deployment were identified. The NZ Big-4 offices use parent firm platforms but have not separately disclosed NZ-specific deployments or governance adaptations.
- **DORA applicability to NZ:** DORA's prescriptive ICT resilience testing requirements (Articles 24–27) do not directly apply to NZ entities unless they have EU-regulated operations. The equivalent RBNZ operational resilience expectations are less prescriptive, reducing the urgency for specialist DORA gap tooling.
- **Type 3 governance unresolved:** No regulator has issued guidance on the governance model for AI agents that make final control effectiveness determinations. This is the frontier of the assurance evolution and the highest-risk governance gap.

### Open Questions

- What level of human reviewer competency is required to provide "meaningful oversight" of AI-generated control testing conclusions, particularly where the reviewer cannot replicate the test procedure?
- How should BS11 outsourcing risk management programmes be adapted to cover SaaS GRC platforms executing control testing on behalf of supervised entities?
- Are there NZ-specific data residency obligations that restrict where GRC SaaS platforms can process testing evidence from RBNZ-supervised entities?
- When AI executes full-population testing (rather than statistical sampling), does the assurance model change — and if so, how should audit standards address it?
- At what point does automated continuous control monitoring constitute a "model" requiring model risk management governance under prudential frameworks?

---

## Output

- Type: knowledge
- Description: Structured findings on the vendor, practitioner, and regulatory landscape for AI-assisted control testing and gap analysis in financial services, with specific attention to governance models, regulatory acceptability, and NZ applicability. Key conclusion: the capability is production-ready and commercially available; the primary open question is governance for Type 3 (delegated authority) AI agents making final assurance determinations.
- Links:
  - https://www.iaasb.org/news-events/2024-10/iaasb-unveils-new-technology-position-shape-future-audit-and-assurance-standards
  - https://www.rbnz.govt.nz/hub/publications/financial-stability-report/2025/may/ai-pre-release/rise-of-the-machines
  - https://www.theiia.org/globalassets/site/content/tools/professional/aiframework-sept-2024-update.pdf