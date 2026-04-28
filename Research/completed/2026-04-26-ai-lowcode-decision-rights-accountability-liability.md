---
review_count: 2
title: "How should decision rights, accountability, and liability be structured for Artificial Intelligence (AI) systems and low-code applications in enterprise environments?"
added: 2026-04-26T10:11:11+00:00
status: completed
priority: high
blocks: [2026-04-26-human-in-the-loop-ai-automated-workflows, 2026-04-26-ai-agent-control-plane-architecture-enterprise, 2026-04-26-ai-lowcode-governance-maturity-model]
tags: [decision-rights, accountability, liability, raci, governance, ai-systems, low-code, enterprise-governance, operational-risk, escalation]
started: 2026-04-26T18:16:34+00:00
completed: 2026-04-26T18:31:47+00:00
output: [knowledge]
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# How should decision rights, accountability, and liability be structured for Artificial Intelligence (AI) systems and low-code applications in enterprise environments?

## Research Question

How should decision rights, accountability, and liability be structured for AI systems and low-code applications in enterprise environments, specifically, who should be empowered to approve new use cases, who owns system behaviour in production, how should formal Responsible-Accountable-Consulted-Informed (RACI) structures and escalation paths be defined, what separation of duties is required, and how should legal and operational liability boundaries be delineated across business, technology, and risk functions?

## Scope

**In scope:**
- Decision rights design: who can approve a new AI or low-code use case, self-service, delegated authority, or committee approval, under what conditions each approval model applies, and what approval criteria are required
- Production accountability: who owns the behaviour of an AI or low-code system after deployment, business owner, technology owner, or shared accountability, and what ownership means operationally, including monitoring obligation, incident response, and remediation authority
- RACI frameworks adapted for AI and low-code governance: how standard RACI models need to be modified to address the non-deterministic and continuously changing nature of AI system behaviour
- Escalation paths: what triggers escalation, who receives it, and what the expected response time and authority at each escalation level is
- Separation of duties: what activities must be performed by different people or teams, for example, the team that builds an AI system should not be the same team that approves its deployment
- Liability: how operational and legal liability for AI-driven decisions is allocated when the decision crosses organisational boundaries or produces harm, in the context of the European Union (EU) AI Act, product liability law, and prudential operational-risk frameworks

**Out of scope:**
- Technical enforcement mechanisms for accountability (covered by Q3/Q16)
- Observability tools that enable accountability tracing (covered by Q4)
- Regulatory compliance mapping in full (covered by Q15)
- Per-use-case risk assessment design (covered by Q5)

**Constraints:**
- Must produce structures that are operable by business and risk professionals, not just technology teams
- Must be grounded in the regulatory context established in Q15, including the European Union (EU) AI Act, Australian Prudential Regulation Authority (APRA) Prudential Standard CPS 230, and the Digital Operational Resilience Act (DORA)
- Findings must address the practical challenge of accountability for systems whose behaviour changes over time without explicit change events

## Context

- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-24-business-led-low-code-agent-governance.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] Ungoverned AI and low-code proliferation is usually an accountability problem before it is a tooling problem, because bounded low-code governance, central control planes, and the National Institute of Standards and Technology (NIST) Artificial Intelligence (AI) Risk Management Framework (AI RMF) all assume named authorities, review paths, and stop rights.
- [fact; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26; https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554] The design challenge is to allocate clear responsibilities for approval, oversight, monitoring, escalation, and remediation across business, technology, risk, and legal actors, because current regulatory texts place different duties on deployers, providers, senior managers, boards, and management bodies rather than on one generic "AI owner."

Cross-references:
- Q5: `2026-04-26-ai-lowcode-risk-tier-classification-controls`
- Q15: `2026-04-26-ai-lowcode-regulatory-compliance-alignment`
- Q9: `2026-04-26-human-in-the-loop-ai-automated-workflows`
- Q16: `2026-04-26-ai-agent-control-plane-architecture-enterprise`
- Q8: `2026-04-26-ai-governance-cost-performance-delivery-impact`

## Approach

1. **RACI model adaptation:** Review standard governance and operating-model precedents and assess how they must be modified for AI and low-code systems, specifically, how to handle non-deterministic outputs, accountability for systems that change behaviour after deployment, and outputs produced by third-party platforms.
2. **Approval model design:** Analyse the design space for use-case approval, self-service below a controlled threshold, delegated approval inside defined risk classes, and committee approval for high-risk or cross-boundary use cases. Identify precedents from model risk management and Information Technology Infrastructure Library (ITIL)-style change governance.
3. **Production ownership definition:** Define what production ownership means for AI and low-code systems, including monitoring, incident response, performance review, remediation, and decommissioning, and how ownership transfers when personnel change.
4. **Separation of duties:** Define which activities must be separated, design, build, approve, deploy, monitor, and audit, and what the minimum team structure is to achieve effective separation.
5. **Liability analysis:** Review the EU AI Act, the withdrawn AI Liability Directive proposal, the current EU Product Liability Directive, and prudential operational-risk frameworks to characterise how legal liability for AI-driven harm is currently allocated.
6. **Escalation path design:** Propose an escalation path model covering trigger conditions, escalation levels, expected response windows, and authority at each level.
7. **Synthesis:** Produce a governance accountability structure, approval matrix, lifecycle decision-rights model, and escalation path suitable for adoption as an enterprise governance artefact.

## Sources

- [x] [European Union (EU) AI Act, Regulation (EU) 2024/1689](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689) - canonical legal text for provider, deployer, documentation, logging, and post-market obligations
- [x] [EU AI Act Service Desk, Article 9](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-9) - current summary of provider risk-management obligations for high-risk AI systems
- [x] [EU AI Act Service Desk, Article 12](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12) - current summary of logging and traceability obligations
- [x] [EU AI Act Service Desk, Article 14](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14) - current summary of human-oversight obligations and stop or override rights
- [x] [EU AI Act Service Desk, Article 26](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26) - current summary of deployer obligations, including monitoring, competent human oversight, log retention, and suspension of risky use
- [x] [EU AI Act Service Desk, Article 72](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-72) - current summary of provider post-market monitoring obligations
- [x] [Proposal for an AI Liability Directive, COM(2022)496](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A52022PC0496) - historical proposal used only to describe the withdrawn approach to AI-specific civil-liability reform
- [x] [European Commission 2025 Work Programme Annexes](https://commission.europa.eu/document/download/7617998c-86e6-4a74-b33c-249e8a7938cd_en?filename=COM_2025_45_1_annexes_EN.pdf) - official Commission source showing that COM(2022)496 had no foreseeable agreement and would be reassessed rather than adopted as proposed
- [x] [Directive (EU) 2024/2853 on liability for defective products](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024L2853) - current EU product-liability text confirming that software and AI systems can be products and that software developers or producers can be treated as manufacturers
- [x] [APRA Prudential Standard CPS 230, Operational Risk Management](https://handbook.apra.gov.au/standard/cps-230) - prudential source for board accountability, senior-management roles, incident escalation, testing, and service-provider oversight
- [x] [Digital Operational Resilience Act (DORA), Regulation (EU) 2022/2554](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554) - financial-sector source for management-body accountability, clear roles, audit, change control, and continuous framework review
- [x] [Federal Reserve SR 26-2, Revised Guidance on Model Risk Management](https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm) - current official guidance that supersedes SR 11-7 and preserves the model-risk precedent for clear governance, independent challenge, and risk-based lifecycle review
- [x] [NIST Artificial Intelligence (AI) Risk Management Framework (AI RMF) 1.0](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10) - foundational governance framework for AI risk management
- [x] [NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) - authoritative subcategories for governance, accountability, roles, monitoring, and decommissioning
- [x] [Control Objectives for Information and Related Technologies (COBIT) resources](https://www.isaca.org/resources/cobit) - public evidence that COBIT remains a live enterprise-governance framework with AI-governance material, although the detailed RACI content is not publicly exposed on this page
- [x] [Enterprise AI use-case routing frameworks](https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-use-case-routing-frameworks.html) - prior completed repository work on three-lane intake routing, governance checkpoints, and escalation signals
- [x] [Business-led low-code agent governance: conditions for durable value versus fragmentation in regulated environments](https://davidamitchell.github.io/Research/research/2026-04-24-business-led-low-code-agent-governance.html) - prior completed repository work on bounded low-code governance and intake controls
- [x] [What control-plane architecture is required to manage AI agents and low-code systems as distributed, semi-autonomous actors within enterprise environments?](https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html) - prior completed repository work on control-plane separation, policy propagation, and feedback loops
- [x] [Enterprise AI platform operating models: organisational structure and ownership](https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-platform-operating-models.html) - prior completed repository work on hub-and-spoke ownership and central governance roles

## Related

- [Business-led low-code agent governance: conditions for durable value versus fragmentation in regulated environments](https://davidamitchell.github.io/Research/research/2026-04-24-business-led-low-code-agent-governance.html)
- [What control-plane architecture is required to manage AI agents and low-code systems as distributed, semi-autonomous actors within enterprise environments?](https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html)
- [Enterprise AI platform operating models: organisational structure and ownership](https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-platform-operating-models.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0-5 are the investigation, and Section 6 seeds the Findings section below.)*

### §0 Initialise

- [fact; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26; https://handbook.apra.gov.au/standard/cps-230] **Research question restated:** This item asks how enterprises should assign approval rights, production accountability, separation of duties, escalation authority, and liability boundaries for AI systems and low-code applications so that decisions remain governable after deployment.
- [fact; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554; https://handbook.apra.gov.au/standard/cps-230] **Scope confirmed:** the investigation covers decision rights, production ownership, RACI adaptation, escalation, separation of duties, and liability allocation across business, technology, risk, and legal actors.
- [fact; source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554; https://handbook.apra.gov.au/standard/cps-230] **Constraint confirmed:** the result must be operable in regulated enterprises, align with current provider and deployer obligations, and work even when system behaviour evolves between explicit change events.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-24-business-led-low-code-agent-governance.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-platform-operating-models.html] **Prior work cross-reference:** prior completed items already established that low-code value depends on bounded intake and central governance, that AI control planes need separated policy and execution layers, and that enterprise AI operating models usually require a central hub with shared control responsibilities.
- [fact; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26] **Output format confirmed:** knowledge, specifically a tiered approval model, lifecycle decision-rights model, and escalation structure for enterprise governance.

### §1 Question Decomposition

- **Root question:** Which actors should hold approval authority, operational accountability, independent challenge authority, and external-liability awareness for AI systems and low-code applications across the lifecycle?
- **A. Governance baseline**
  - A1. Which sources explicitly require clear roles, responsibilities, oversight, and review?
  - A2. Do those sources imply one blanket owner or multiple owners by lifecycle activity?
- **B. Approval rights**
  - B1. Which kinds of use case can be approved under bounded self-service?
  - B2. Which kinds require delegated domain approval?
  - B3. Which kinds require enterprise committee or executive approval?
- **C. Production ownership**
  - C1. What duties attach to being the production owner of an AI or low-code system?
  - C2. Which of those duties belong to the business function, the technology function, the provider, and the independent risk function?
- **D. Separation of duties**
  - D1. Which lifecycle steps should not be owned by the same team?
  - D2. What minimum independent review or assurance functions are required?
- **E. Liability**
  - E1. Which legal obligations currently fall on providers or manufacturers?
  - E2. Which legal or operational duties currently fall on deployers or regulated firms?
  - E3. What happened to the proposed AI Liability Directive?
- **F. Escalation**
  - F1. Which events must trigger escalation or suspension?
  - F2. Who needs authority to stop, override, or reapprove a system?
- **G. Synthesis**
  - G1. What approval matrix follows from the evidence?
  - G2. What lifecycle accountability model follows from the evidence?
  - G3. What escalation path is proportionate and operable?

### §2 Investigation

#### Source access and source-quality notes

- [fact; source: https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm] The seeded SR 11-7 page was stale in this environment, and the current official Federal Reserve source is SR 26-2, which explicitly supersedes SR 11-7 while preserving model-risk governance as the relevant approval and independent-challenge precedent.
- [fact; source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A52022PC0496; https://commission.europa.eu/document/download/7617998c-86e6-4a74-b33c-249e8a7938cd_en?filename=COM_2025_45_1_annexes_EN.pdf] The AI Liability Directive proposal remains accessible as a historical proposal, but the European Commission's 2025 Work Programme annex records that COM(2022)496 had no foreseeable agreement and would be reassessed rather than adopted as proposed.
- [fact; source: https://www.isaca.org/resources/cobit] The public COBIT page confirms that COBIT is still positioned as an enterprise governance framework and now includes AI-governance material, but the page does not expose the detailed governance-objective or RACI text needed for precise downstream claims.

#### A. What the governance baseline requires

- [fact; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] NIST AI RMF Govern 1.5 requires ongoing monitoring and periodic review with clearly defined organisational roles and responsibilities, Govern 2.1 requires documented and clear roles and lines of communication, and Govern 2.3 says executive leadership takes responsibility for decisions about AI-system development and deployment.
- [fact; source: https://handbook.apra.gov.au/standard/cps-230] APRA CPS 230 says the board is ultimately accountable for oversight of operational risk management, must set clear roles and responsibilities for senior managers, must receive regular updates, and must approve business continuity and service-provider policies.
- [fact; source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554] DORA says the management body must define, approve, oversee, and be responsible for the implementation of arrangements related to the information and communication technology (ICT) risk-management framework, bear ultimate responsibility for ICT risk, set clear roles and responsibilities, approve audit plans, and review the framework at least annually.
- [fact; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-9; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-72] The EU AI Act splits duties across providers and deployers, because providers must run risk management and post-market monitoring while deployers must assign competent human oversight, monitor use, retain logs under their control, and suspend use when they believe the system may present risk.
- [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26] The evidence rejects a single blanket "AI owner" and instead supports activity-based accountability, one accountable owner per lifecycle decision, plus explicit handoffs between business, technology, provider, and independent challenge functions.

#### B. What the evidence implies for approval rights

- [fact; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] NIST AI RMF Govern 1.3 says organizations should determine the needed level of risk-management activity based on risk tolerance, which supports tiering approval effort by risk rather than requiring one uniform gate.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-use-case-routing-frameworks.html; https://davidamitchell.github.io/Research/research/2026-04-24-business-led-low-code-agent-governance.html; https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-platform-operating-models.html] Prior repository work found that safe AI intake needs explicit routing signals, governance checkpoints, and bounded low-code lanes, and that the central platform hub retains control over shared policies and promotion rails.
- [fact; source: https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554] APRA and DORA both reserve ultimate accountability for framework, continuity, third-party, and audit arrangements to boards or management bodies, which means high-impact use cases cannot be treated as purely local approvals.
- [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://davidamitchell.github.io/Research/research/2026-04-24-business-led-low-code-agent-governance.html; https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554] A three-tier model follows: bounded low-risk use cases can be approved by a named business service owner using preapproved patterns, medium-risk or cross-functional use cases need delegated domain approval with technology and risk concurrence, and high-risk, rights-impacting, externally facing, or regulated use cases need enterprise committee or executive approval.

#### C. What production ownership actually means

- [fact; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26] AI Act Article 26 requires deployers to assign human oversight to natural persons with competence, training, authority, and support, to monitor operation, to retain logs under their control for an appropriate period of at least six months unless law says otherwise, and to suspend use when continued use may present risk.
- [fact; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-72] AI Act Article 72 requires providers to establish and document a post-market monitoring system that actively and systematically collects, documents, and analyses relevant performance data throughout the system lifetime.
- [fact; source: https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554] APRA CPS 230 and DORA both tie operational ownership to monitoring, incident escalation, testing, change control, framework review, and remediation with clear accountabilities.
- [inference; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-72; https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554] Production ownership therefore has at least two internal seats: a business service owner accountable for continued business use, exception handling, and human decisions taken on the system's output, and a technology system owner accountable for runtime reliability, logging, controlled change, defect remediation, and execution of stop or rollback actions.
- [inference; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-72; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024L2853] When the enterprise uses a third-party AI product, the internal technology owner does not absorb the vendor's provider or manufacturer duties; instead, the enterprise must track provider obligations separately and integrate them into vendor-management and incident-escalation processes.

#### D. What separation of duties is required

- [fact; source: https://handbook.apra.gov.au/standard/cps-230] APRA CPS 230 requires independent review of operational risk management, periodic internal-audit assurance over business continuity, and timely remediation with clear accountabilities.
- [fact; source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554] DORA says larger financial entities should be able to organize ICT risk management according to a three-lines-of-defence model, maintain internal-audit review, and apply controlled change management with approvals and verification.
- [fact; source: https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm] The Federal Reserve's current model-risk guidance keeps the model-risk-management precedent alive by emphasizing strong governance, clear roles, risk-based practices, and independent validation and challenge rather than self-approval by model builders.
- [inference; source: https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554; https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm; https://davidamitchell.github.io/Research/research/2026-04-24-business-led-low-code-agent-governance.html] The minimum viable separation of duties is to split sponsor and use-case owner, build and configuration owner, independent approver, runtime operator, and audit or assurance reviewer, because the same team should not both create a system and give final independent risk approval for it.

#### E. What current law says about liability boundaries

- [fact; source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689] The AI Act states that existing rights and remedies for compensation remain unaffected and fully applicable, which means AI-governance structures must coexist with existing product-liability, contract, and tort frameworks rather than replace them.
- [fact; source: https://commission.europa.eu/document/download/7617998c-86e6-4a74-b33c-249e8a7938cd_en?filename=COM_2025_45_1_annexes_EN.pdf; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A52022PC0496] The proposed AI Liability Directive was not adopted, so it is useful as context on the policy problem but not as a statement of current live obligations.
- [fact; source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024L2853] Directive (EU) 2024/2853 says liability without fault remains the core product-liability mechanism, treats software and AI systems as products, and says a developer or producer of software, including AI-system providers within the meaning of the AI Act, should be treated as a manufacturer.
- [inference; source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024L2853; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-72] Internal accountability maps can allocate operational duties and contractual indemnity pathways, but they cannot erase statutory provider or manufacturer liability for defective products, and they cannot erase deployer duties to monitor and suspend risky use.

#### F. What escalation has to cover

- [fact; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14] AI Act Article 14 requires human-oversight measures that let authorised natural persons understand limitations, detect anomalies, interpret outputs, decide not to use a system, disregard or reverse outputs, and interrupt operation safely.
- [fact; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26] AI Act Articles 12 and 26 tie escalation to logging, traceability, monitoring, and suspension when risk appears in use.
- [fact; source: https://handbook.apra.gov.au/standard/cps-230] APRA CPS 230 requires operational incidents and near misses to be identified, escalated, recorded, and addressed in a timely manner, and requires notification to APRA within 72 hours after awareness of an incident likely to have material financial impact or material impact on critical operations.
- [fact; source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554] DORA requires ICT incidents, lessons from testing, and lessons from real-life incidents to be incorporated continuously into the ICT risk-assessment and framework-review process.
- [inference; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26; https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554] A practical enterprise escalation model should define at least three levels: operational response by the business and technology owners for anomalies or threshold breaches, domain-risk escalation for customer, legal, or control impacts, and executive or committee escalation for serious incidents, rights impacts, regulatory-reporting triggers, or unresolved disputes about continued operation.

### §3 Reasoning

- [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554] The convergent pattern across AI risk management, prudential operational-risk governance, and digital-resilience law is that authority has to be explicit, review has to be periodic, and top-level management remains accountable for the framework even when local teams execute.
- [inference; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-72] Because the AI Act gives deployers and providers different live duties, a workable internal model cannot collapse approval, use, runtime operation, and provider oversight into one owner label.
- [inference; source: https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm; https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554] Independent challenge remains necessary even when AI systems are built on low-code or vendor-managed platforms, because governance, model risk, and operational resilience all treat self-approval as structurally weak.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-24-business-led-low-code-agent-governance.html; https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-platform-operating-models.html] The right governance artefact is therefore a tiered matrix, not a slogan about "shared accountability," because enterprise work needs named decision rights for each lifecycle step and named escalation recipients when those steps fail.

### §4 Consistency Check

- [fact; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-72] **Potential tension checked:** the AI Act gives both providers and deployers monitoring duties, but the duties are different rather than contradictory, provider duties concern post-market compliance of the product, while deployer duties concern safe use in context.
- [fact; source: https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554] **Potential tension checked:** APRA and DORA reserve ultimate accountability to boards or management bodies while still requiring management and operational roles underneath them, which supports layered accountability rather than local autonomy without oversight.
- [fact; source: https://commission.europa.eu/document/download/7617998c-86e6-4a74-b33c-249e8a7938cd_en?filename=COM_2025_45_1_annexes_EN.pdf; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024L2853] **Potential tension checked:** there is no contradiction between the withdrawn AI Liability Directive proposal and the 2024 Product Liability Directive, because the former is historical context and the latter is current law.
- [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554] The synthesis is internally consistent if "accountability" is defined by decision class and control surface rather than by system in the abstract.

### §5 Depth and Breadth Expansion

- [inference; source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024L2853] **Regulatory lens:** legal exposure now turns less on whether an enterprise wrote its own model and more on whether it is acting as provider, deployer, or manufacturer and whether the software or AI system was defective or used unsafely.
- [inference; source: https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554] **Operational-resilience lens:** accountability design has to survive outages, provider failures, and incident reporting windows, so escalation and stop authority are as important as approval rights at intake.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-24-business-led-low-code-agent-governance.html; https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-platform-operating-models.html] **Organisational lens:** the temptation to call accountability "shared" usually masks missing ownership, and the more robust pattern is one accountable business owner plus one accountable technical owner with an independent challenge function outside both.
- [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14] **Behavioural lens:** explicit human-override authority matters because automation bias and ambiguity about who may interrupt a system are predictable failure modes when AI outputs are treated as self-validating.

### §6 Synthesis

*(This section seeds the Findings below.)*

**Executive summary:**

- [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26; https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554] Decision rights for enterprise AI and low-code systems should be tiered by risk and boundary crossing, and production accountability should be split by lifecycle decision rather than assigned to one blanket "system owner."
- [inference; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-72; https://handbook.apra.gov.au/standard/cps-230] The minimum workable production model is a named business service owner accountable for justified use and human decisions taken on outputs, a named technology system owner accountable for runtime reliability and controlled change, and an independent risk or assurance function that can challenge, block, or escalate.
- [fact; source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024L2853; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689; https://commission.europa.eu/document/download/7617998c-86e6-4a74-b33c-249e8a7938cd_en?filename=COM_2025_45_1_annexes_EN.pdf] Current legal liability is not determined by internal RACI charts alone, because the AI Liability Directive proposal was not adopted, the AI Act leaves existing remedies in place, and the current Product Liability Directive treats software and AI systems as products whose developers or providers can be manufacturers.
- [inference; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26; https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554] The best governance artefact is therefore a package of three linked matrices, approval, lifecycle accountability, and escalation, with explicit stop authority, incident triggers, and senior review thresholds.

**Key findings:**

1. [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-use-case-routing-frameworks.html; https://davidamitchell.github.io/Research/research/2026-04-24-business-led-low-code-agent-governance.html; https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554] **High confidence:** Approval rights should be tiered so that bounded low-risk use cases can move under preapproved patterns with named business approval, medium-risk or cross-functional use cases need delegated domain approval with technology and risk concurrence, and high-risk or regulated use cases require enterprise committee or executive sign-off.
2. [inference; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-72; https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554] **High confidence:** No single actor can honestly own enterprise AI behaviour end to end, because business use decisions, runtime operation, and provider compliance are different obligations, so the accountable owner must be defined separately for each lifecycle decision.
3. [inference; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26; https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554] **High confidence:** Production ownership means continuous monitoring, incident escalation, log retention, controlled change, remediation tracking, and decommissioning authority, not merely sponsoring the use case at launch.
4. [inference; source: https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554; https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm] **High confidence:** Effective separation of duties requires that the team building or configuring a system cannot also be the final independent approver or assurance reviewer, because prudential, resilience, and model-risk precedents all require independent challenge.
5. [inference; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26; https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554] **High confidence:** Escalation paths should be trigger-based and include explicit stop or override authority for anomalies, harmful outputs, control failures, serious incidents, material changes, and provider or regulator notifications.
6. [fact; source: https://commission.europa.eu/document/download/7617998c-86e6-4a74-b33c-249e8a7938cd_en?filename=COM_2025_45_1_annexes_EN.pdf; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024L2853; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689] **High confidence:** Internal accountability maps do not displace external legal liability, because the AI Liability Directive proposal was not adopted, the AI Act preserves existing remedies, and the current Product Liability Directive applies no-fault defective-product liability to software and AI systems.
7. [fact; source: https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554] **High confidence:** In regulated entities, boards or management bodies remain ultimately accountable for the control framework itself even when day-to-day approvals and operations are delegated to business, technology, and risk teams.
8. [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-platform-operating-models.html] **Medium confidence:** Standard RACI remains useful only if it is converted into a lifecycle matrix with named natural persons and explicit handoffs, because a static one-row "A" column hides the multi-surface reality of AI governance.

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Tiered approval rights are required. | https://airc.nist.gov/airmf-resources/airmf/5-sec-core/<br>https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-use-case-routing-frameworks.html<br>https://davidamitchell.github.io/Research/research/2026-04-24-business-led-low-code-agent-governance.html<br>https://handbook.apra.gov.au/standard/cps-230<br>https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554 | high | Risk tolerance, bounded intake, and senior approval duties converge on three approval tiers. |
| [inference] Accountability must be split by lifecycle decision. | https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26<br>https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-72<br>https://handbook.apra.gov.au/standard/cps-230<br>https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554 | high | Deployer, provider, business, and technology duties are distinct. |
| [inference] Production ownership means continuous operational duty. | https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26<br>https://handbook.apra.gov.au/standard/cps-230<br>https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554 | high | Monitoring, logs, incidents, changes, and remediation define ownership. |
| [inference] Separation of duties requires independent challenge. | https://handbook.apra.gov.au/standard/cps-230<br>https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554<br>https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm | high | Builders should not self-approve high-impact systems. |
| [inference] Escalation needs explicit stop and override rights. | https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14<br>https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26<br>https://handbook.apra.gov.au/standard/cps-230<br>https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554 | high | Anomalies, serious incidents, and control failures must trigger escalation. |
| [fact] Current law keeps external liability outside internal RACI charts. | https://commission.europa.eu/document/download/7617998c-86e6-4a74-b33c-249e8a7938cd_en?filename=COM_2025_45_1_annexes_EN.pdf<br>https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024L2853<br>https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689 | high | The AI Liability Directive proposal is historical only, while software product liability is current law. |
| [fact] Boards or management bodies retain ultimate framework accountability. | https://handbook.apra.gov.au/standard/cps-230<br>https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554 | high | Delegation of operations does not remove top-level accountability. |
| [inference] Lifecycle matrices are stronger than static RACI labels. | https://airc.nist.gov/airmf-resources/airmf/5-sec-core/<br>https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html<br>https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-platform-operating-models.html | medium | AI governance spans intake, runtime, and oversight surfaces. |

**Assumptions:**

- None.

**Analysis:**

- [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554] The strongest evidence came from sources that allocate responsibility directly, NIST for AI governance design, APRA and DORA for regulated operational-accountability patterns, and the AI Act for live provider and deployer duties.
- [inference; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-72; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024L2853] Legal-liability analysis was weighted toward current binding texts, so the withdrawn AI Liability Directive proposal was treated as context while the current AI Act and Product Liability Directive were treated as live allocation mechanisms.
- [inference; source: https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm; https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554] Model-risk and operational-resilience precedents were used to resolve the approval and independence questions because they already deal with complex systems that need expert build teams, independent challenge, and senior management accountability.

**Risks, gaps, uncertainties:**

- [fact; source: https://www.isaca.org/resources/cobit] Public COBIT material did not expose the detailed governance-objective or RACI text, so COBIT influenced framing only at the framework level and not at the detailed matrix level.
- [inference; source: https://commission.europa.eu/document/download/7617998c-86e6-4a74-b33c-249e8a7938cd_en?filename=COM_2025_45_1_annexes_EN.pdf; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024L2853] The European liability landscape may evolve again if the Commission later tables a new AI-specific civil-liability instrument, so the current liability guidance should be treated as correct for 2026 but not necessarily permanent.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-24-business-led-low-code-agent-governance.html; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] The exact threshold between bounded self-service and delegated approval still depends on the risk-tier framework in Q5, so the approval tiers are structurally strong but still need calibration thresholds.

**Open questions:**

- How should Q5's risk-tier framework define the exact boundary between bounded self-service and delegated approval for internal productivity agents?
- How should vendor contracts, indemnities, and insurance be structured once the vendor-constraints item is complete?
- How should human-in-the-loop requirements from Q9 differ by approval tier and by high-risk category?

### §7 Recursive Review

- [fact; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26; https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024L2853] Every substantive claim in Sections 0 through 6 is either sourced to current primary material or labeled as inference, and the synthesis keeps legal, operational, and organisational responsibilities distinct.
- [fact; source: https://commission.europa.eu/document/download/7617998c-86e6-4a74-b33c-249e8a7938cd_en?filename=COM_2025_45_1_annexes_EN.pdf; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A52022PC0496] The main ambiguity, the status of the AI Liability Directive proposal, was resolved by treating the proposal as historical context and the Commission annex as the current status source.
- [inference; source: https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14] The resulting model is coherent because it gives each major control surface, approval, use, runtime, independent challenge, and escalation, one accountable seat without pretending those seats collapse into one actor.

---

## Findings

### Executive Summary

[inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26; https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554] Decision rights for enterprise AI and low-code systems should be tiered by risk and boundary crossing, and production accountability should be split by lifecycle decision rather than assigned to one blanket "system owner." [inference; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-72; https://handbook.apra.gov.au/standard/cps-230] The minimum workable production model is a named business service owner accountable for justified use and human decisions taken on outputs, a named technology system owner accountable for runtime reliability and controlled change, and an independent risk or assurance function that can challenge, block, or escalate. [fact; source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024L2853; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689; https://commission.europa.eu/document/download/7617998c-86e6-4a74-b33c-249e8a7938cd_en?filename=COM_2025_45_1_annexes_EN.pdf] Current legal liability is not determined by internal RACI charts alone, because the AI Liability Directive proposal was not adopted, the AI Act leaves existing remedies in place, and the current Product Liability Directive treats software and AI systems as products whose developers or providers can be manufacturers. [inference; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26; https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554] The best governance artefact is therefore a package of three linked matrices, approval, lifecycle accountability, and escalation, with explicit stop authority, incident triggers, and senior review thresholds.

### Key Findings

1. [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-use-case-routing-frameworks.html; https://davidamitchell.github.io/Research/research/2026-04-24-business-led-low-code-agent-governance.html; https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554] **High confidence:** Approval rights should be tiered so that bounded low-risk use cases can move under preapproved patterns with named business approval, medium-risk or cross-functional use cases need delegated domain approval with technology and risk concurrence, and high-risk or regulated use cases require enterprise committee or executive sign-off.
2. [inference; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-72; https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554] **High confidence:** No single actor can honestly own enterprise AI behaviour end to end, because business use decisions, runtime operation, and provider compliance are different obligations, so the accountable owner must be defined separately for each lifecycle decision.
3. [inference; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26; https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554] **High confidence:** Production ownership means continuous monitoring, incident escalation, log retention, controlled change, remediation tracking, and decommissioning authority, not merely sponsoring the use case at launch.
4. [inference; source: https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554; https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm] **High confidence:** Effective separation of duties requires that the team building or configuring a system cannot also be the final independent approver or assurance reviewer, because prudential, resilience, and model-risk precedents all require independent challenge.
5. [inference; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26; https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554] **High confidence:** Escalation paths should be trigger-based and include explicit stop or override authority for anomalies, harmful outputs, control failures, serious incidents, material changes, and provider or regulator notifications.
6. [fact; source: https://commission.europa.eu/document/download/7617998c-86e6-4a74-b33c-249e8a7938cd_en?filename=COM_2025_45_1_annexes_EN.pdf; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024L2853; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689] **High confidence:** Internal accountability maps do not displace external legal liability, because the AI Liability Directive proposal was not adopted, the AI Act preserves existing remedies, and the current Product Liability Directive applies no-fault defective-product liability to software and AI systems.
7. [fact; source: https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554] **High confidence:** In regulated entities, boards or management bodies remain ultimately accountable for the control framework itself even when day-to-day approvals and operations are delegated to business, technology, and risk teams.
8. [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-platform-operating-models.html] **Medium confidence:** Standard RACI remains useful only if it is converted into a lifecycle matrix with named natural persons and explicit handoffs, because a static one-row "A" column hides the multi-surface reality of AI governance.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Tiered approval rights are required. | https://airc.nist.gov/airmf-resources/airmf/5-sec-core/<br>https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-use-case-routing-frameworks.html<br>https://davidamitchell.github.io/Research/research/2026-04-24-business-led-low-code-agent-governance.html<br>https://handbook.apra.gov.au/standard/cps-230<br>https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554 | high | Risk tolerance, bounded intake, and senior approval duties converge on three approval tiers. |
| [inference] Accountability must be split by lifecycle decision. | https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26<br>https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-72<br>https://handbook.apra.gov.au/standard/cps-230<br>https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554 | high | Deployer, provider, business, and technology duties are distinct. |
| [inference] Production ownership means continuous operational duty. | https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26<br>https://handbook.apra.gov.au/standard/cps-230<br>https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554 | high | Monitoring, logs, incidents, changes, and remediation define ownership. |
| [inference] Separation of duties requires independent challenge. | https://handbook.apra.gov.au/standard/cps-230<br>https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554<br>https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm | high | Builders should not self-approve high-impact systems. |
| [inference] Escalation needs explicit stop and override rights. | https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14<br>https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26<br>https://handbook.apra.gov.au/standard/cps-230<br>https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554 | high | Anomalies, serious incidents, and control failures must trigger escalation. |
| [fact] Current law keeps external liability outside internal RACI charts. | https://commission.europa.eu/document/download/7617998c-86e6-4a74-b33c-249e8a7938cd_en?filename=COM_2025_45_1_annexes_EN.pdf<br>https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024L2853<br>https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689 | high | The AI Liability Directive proposal is historical only, while software product liability is current law. |
| [fact] Boards or management bodies retain ultimate framework accountability. | https://handbook.apra.gov.au/standard/cps-230<br>https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554 | high | Delegation of operations does not remove top-level accountability. |
| [inference] Lifecycle matrices are stronger than static RACI labels. | https://airc.nist.gov/airmf-resources/airmf/5-sec-core/<br>https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html<br>https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-platform-operating-models.html | medium | AI governance spans intake, runtime, and oversight surfaces. |

### Assumptions

- None.

### Analysis

[inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554] The strongest evidence came from sources that allocate responsibility directly, NIST for AI governance design, APRA and DORA for regulated operational-accountability patterns, and the AI Act for live provider and deployer duties. [inference; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-72; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024L2853] Legal-liability analysis was weighted toward current binding texts, so the withdrawn AI Liability Directive proposal was treated as context while the current AI Act and Product Liability Directive were treated as live allocation mechanisms. [inference; source: https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm; https://handbook.apra.gov.au/standard/cps-230; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554] Model-risk and operational-resilience precedents were used to resolve the approval and independence questions because they already deal with complex systems that need expert build teams, independent challenge, and senior management accountability.

### Risks, Gaps, and Uncertainties

- [fact; source: https://www.isaca.org/resources/cobit] Public COBIT material did not expose the detailed governance-objective or RACI text, so COBIT influenced framing only at the framework level and not at the detailed matrix level.
- [inference; source: https://commission.europa.eu/document/download/7617998c-86e6-4a74-b33c-249e8a7938cd_en?filename=COM_2025_45_1_annexes_EN.pdf; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024L2853] The European liability landscape may evolve again if the Commission later tables a new AI-specific civil-liability instrument, so the current liability guidance should be treated as correct for 2026 but not necessarily permanent.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-24-business-led-low-code-agent-governance.html; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] The exact threshold between bounded self-service and delegated approval still depends on the risk-tier framework in Q5, so the approval tiers are structurally strong but still need calibration thresholds.

### Open Questions

- How should Q5's risk-tier framework define the exact boundary between bounded self-service and delegated approval for internal productivity agents?
- How should vendor contracts, indemnities, and insurance be structured once the vendor-constraints item is complete?
- How should human-in-the-loop requirements from Q9 differ by approval tier and by high-risk category?

---

## Output

- Type: knowledge
- Description: A tiered approval model, lifecycle accountability model, and escalation structure for enterprise AI and low-code governance, grounded in current AI Act, product-liability, prudential, and resilience obligations.
- Links:
  - https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26
  - https://handbook.apra.gov.au/standard/cps-230
  - https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024L2853
