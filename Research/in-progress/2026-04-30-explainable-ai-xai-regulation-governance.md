---
title: "Explainable Artificial Intelligence (XAI): current research state, leading institutions, and regulatory intersection in heavily regulated industries"
added: 2026-04-30T06:42:30+00:00
status: reviewing
priority: high  # low | medium | high
blocks: []
tags: [agentic-ai, governance, regulation, financial-services, healthcare, eu-ai-act, audit, model-risk]
started: 2026-05-01T02:24:45+00:00
completed: ~
output: [knowledge]  # skill | tool | agent | knowledge | backlog-item
cites: [2026-04-24-ai-agent-regulation-global-financial-services, 2026-04-22-ai-governance-assurance-change-control-verification, 2026-02-28-ai-control-testing-and-assurance]
related: [2026-02-28-rbnz-ai-supervisory-expectations, 2026-04-22-knowledge-curation-governance-for-regulated-ai, 2026-04-30-human-bias-ai-trust-rlhf-sycophancy]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Explainable Artificial Intelligence (XAI): current research state, leading institutions, and regulatory intersection in heavily regulated industries

## Research Question

What is the current state of Explainable Artificial Intelligence (XAI) research, who leads it and what are the primary techniques, and how does XAI intersect with regulatory obligations, audit requirements, and accountability for automated decisions made by Artificial Intelligence (AI) agents in heavily regulated industries such as financial services and healthcare?

## Scope

**In scope:**
- Definition and taxonomy of Explainable Artificial Intelligence (XAI): how it differs from interpretability; key technique families (post-hoc, ante-hoc; local, global; model-agnostic, model-specific)
- Leading research groups, institutions, funded programmes, and published benchmarks in XAI as of 2024-2026
- Regulatory frameworks that explicitly require or incentivise explanations for AI-driven decisions: European Union (EU) Artificial Intelligence Act (AI Act), General Data Protection Regulation (GDPR) Article 22, Federal Reserve Supervisory Letter (SR) 11-7, Basel-adjacent model-risk expectations, Australian Prudential Regulation Authority (APRA) CPS 230, United Kingdom (UK) Bank of England and Financial Conduct Authority (FCA) guidance, and International Organization for Standardization (ISO)/International Electrotechnical Commission (IEC) 42001
- How XAI applies to audit trail design and third-line review for automated decisions in financial services and healthcare
- XAI challenges in agentic AI systems where the decision chain is distributed across multiple models or tools

**Out of scope:**
- Full algorithmic derivations of individual XAI methods (SHapley Additive exPlanations (SHAP), Local Interpretable Model-agnostic Explanations (LIME), Gradient-weighted Class Activation Mapping (Grad-CAM), and related methods), technique survey only
- XAI for consumer-facing applications outside regulated contexts
- Hardware-level explainability
- Fairness and bias auditing as a separate discipline, referenced only where it intersects explainability obligations

**Constraints:**
- Primary focus on published research and regulatory guidance from 2020 onwards; earlier foundational work cited only for context
- English-language sources; non-English regulatory documents accepted where official translations exist

## Context

Regulated sectors increasingly need explanation, traceability, and human-review mechanisms for automated decisions, but the strongest current obligations are framed as governance and accountability controls rather than mandates to adopt any single XAI technique. [inference; source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689; https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/explaining-decisions-made-with-artificial-intelligence/part-1-the-basics-of-explaining-ai/legal-framework/; https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm]

This item builds on prior repository work showing that regulated AI deployment already depends on auditability, change control, and explicit human accountability, and asks where current XAI research does and does not satisfy those control surfaces. [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-24-ai-agent-regulation-global-financial-services.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-ai-governance-assurance-change-control-verification.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-02-28-ai-control-testing-and-assurance.md]

## Approach

1. **Define XAI** - Distinguish Explainable Artificial Intelligence from interpretability; map the taxonomy of techniques by scope (local/global), timing (ante-hoc/post-hoc), and model dependency (model-agnostic/model-specific). Identify the most-cited survey papers as anchor references.
2. **Survey leading researchers and institutions** - Identify the research programmes, standards bodies, and canonical papers that shaped the current field, and avoid unsupported league-table claims about institutional dominance.
3. **Review technique landscape** - Survey the primary XAI method families: SHAP, LIME, attention-based explanations, counterfactual explanations, Concept Activation Vectors (CAVs), and rule extraction. Note known limitations such as faithfulness-versus-plausibility trade-offs and explanation instability.
4. **Map regulatory requirements** - Identify which regulations impose XAI-adjacent obligations, what they specifically require (right to information, logging, model documentation, audit trail, human review), and how organisations are currently meeting these obligations.
5. **Audit and accountability intersection** - Examine how XAI outputs are used, or should be used, in first-line validation, second-line model risk management, and third-line audit. Review published guidance from the Bank of England, FCA, APRA, ISO, and related bodies on AI auditability.
6. **Agentic AI and XAI** - Identify the specific XAI challenges that arise when decisions are produced by multi-step agentic systems: attribution across steps, causal tracing, explanation aggregation, and whether mechanistic interpretability is yet usable as a governance control.

## Sources

- [x] [European Union Artificial Intelligence Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) - primary legal text for high-risk AI obligations, logging, transparency, human oversight, and robustness.
- [x] [European Union General Data Protection Regulation](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng) - primary legal text for Articles 13 to 15 and 22 on automated decisions and meaningful information.
- [x] [Information Commissioner's Office Legal framework for explaining decisions made with AI](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/explaining-decisions-made-with-artificial-intelligence/part-1-the-basics-of-explaining-ai/legal-framework/) - regulator guidance connecting GDPR duties to explanations, human intervention, and Data Protection Impact Assessments.
- [x] [Article 29 Working Party Guidelines on Automated individual decision-making and Profiling](https://ec.europa.eu/newsroom/article29/item-detail.cfm?item_id=612053) - official European guidance endorsed by the European Data Protection Board (EDPB).
- [x] [Federal Reserve Supervisory Letter SR 11-7 Guidance on Model Risk Management](https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm) - primary United States (US) model-risk-management guidance.
- [x] [Phillips et al. (2021) Four Principles of Explainable Artificial Intelligence](https://doi.org/10.6028/NIST.IR.8312) - National Institute of Standards and Technology (NIST) reference for explanation, meaningful explanation, explanation accuracy, and knowledge limits.
- [x] [Arrieta et al. (2020) Explainable Artificial Intelligence (XAI): Concepts, taxonomies, opportunities and challenges toward responsible AI](https://doi.org/10.1016/j.inffus.2019.12.012) - survey anchor for XAI taxonomy and method families.
- [x] [Doshi-Velez and Kim (2017) Towards a rigorous science of interpretable machine learning](https://doi.org/10.48550/arXiv.1702.08608) - foundational framing for interpretability and evaluation.
- [x] [Ribeiro et al. (2016) Why Should I Trust You?: Explaining the Predictions of Any Classifier](https://doi.org/10.48550/arXiv.1602.04938) - foundational local explanation method.
- [x] [Lundberg and Lee (2017) A Unified Approach to Interpreting Model Predictions](https://doi.org/10.48550/arXiv.1705.07874) - foundational SHAP paper.
- [x] [Kim et al. (2018) Interpretability Beyond Feature Attribution: Quantitative Testing with Concept Activation Vectors (TCAV)](https://doi.org/10.48550/arXiv.1711.11279) - concept-based explanation technique.
- [x] [Defense Advanced Research Projects Agency Explainable Artificial Intelligence program](https://www.darpa.mil/program/explainable-artificial-intelligence) - public programme overview for the most influential early explainability funding initiative.
- [x] [Bank of England Artificial Intelligence Public-Private Forum final report](https://www.bankofengland.co.uk/-/media/boe/files/fintech/ai-public-private-forum-final-report.pdf) - UK financial-services discussion of explainability, model risk, and governance.
- [x] [Bank of England DP5/22 Artificial Intelligence and Machine Learning](https://www.bankofengland.co.uk/prudential-regulation/publication/2022/october/artificial-intelligence) - UK regulator discussion paper on AI governance in financial services.
- [x] [Bank of England FS2/23 Artificial Intelligence and Machine Learning](https://www.bankofengland.co.uk/prudential-regulation/publication/2023/october/artificial-intelligence-and-machine-learning) - UK regulator feedback statement referencing the Artificial Intelligence Public-Private Forum and existing-framework approach.
- [x] [Australian Prudential Regulation Authority Operational risk management](https://www.apra.gov.au/operational-risk-management) - official landing page for CPS 230 and related operational-risk and material-service-provider controls.
- [x] [International Organization for Standardization and International Electrotechnical Commission 42001:2023 AI management systems](https://www.iso.org/standard/42001) - official public summary of the first international AI management-system standard.
- [x] [Anthropic Tracing the thoughts of a language model](https://www.anthropic.com/research/tracing-thoughts-language-model) - official mechanistic-interpretability research summary relevant to agentic-system explainability limits.
- [x] [FDA Artificial Intelligence Enabled Device Software Functions: Lifecycle Management and Marketing Submission Recommendations](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/artificial-intelligence-enabled-device-software-functions-lifecycle-management-and-marketing) - United States Food and Drug Administration (FDA) draft guidance on lifecycle controls for AI enabled medical devices.
- [x] [AI agent regulation in financial services (internal related research)](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-24-ai-agent-regulation-global-financial-services.md) - prior repository work on explainability, auditability, and human-oversight obligations.
- [x] [AI governance assurance and change control verification (internal related research)](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-ai-governance-assurance-change-control-verification.md) - prior repository work on audit evidence and change governance.
- [x] [AI control testing and assurance (internal related research)](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-02-28-ai-control-testing-and-assurance.md) - prior repository work on human accountability for AI-generated assurance artefacts.

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0 to 5 are the investigation, section 6 seeds the Findings section below.)*

### §0 Initialise

- [fact; source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689; https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm; https://www.bankofengland.co.uk/-/media/boe/files/fintech/ai-public-private-forum-final-report.pdf] **Research question restated:** this item asks which XAI methods and institutions matter most today, and whether current regulated-sector obligations are really asking for technical explainers, governance controls, or both.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-24-ai-agent-regulation-global-financial-services.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-ai-governance-assurance-change-control-verification.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-02-28-ai-control-testing-and-assurance.md] Prior completed items already establish that regulated AI deployment depends on auditability, change control, and named human accountability, so this item focuses on where XAI methods support those requirements and where they do not.
- [fact; source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689; https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/explaining-decisions-made-with-artificial-intelligence/part-1-the-basics-of-explaining-ai/legal-framework/; https://www.apra.gov.au/operational-risk-management] The scope is cross-sector but weighted toward financial services, with healthcare included where official sources clearly address AI enabled medical devices or high-risk medical uses.
- [fact; source: https://doi.org/10.6028/NIST.IR.8312; https://doi.org/10.1016/j.inffus.2019.12.012] The output format is a knowledge item that combines taxonomy, governance, and current research limitations rather than a benchmark ranking or product comparison.

### §1 Question Decomposition

- **Root question:** What does current XAI research actually provide, and how does that map to explainability and accountability duties in regulated industries?
- **A. Taxonomy**
  - A1. How do the canonical sources distinguish explainability from interpretability?
  - A2. Which technique axes, local versus global, ante-hoc versus post-hoc, model-agnostic versus model-specific, are stable across the survey literature?
- **B. Research frontier and leadership**
  - B1. Which institutions and programmes demonstrably shaped the field through funding, standards, or canonical methods?
  - B2. Is there evidence for a single dominant frontier institution, or is the field better described as a distributed research ecosystem?
- **C. Technique landscape**
  - C1. What do SHAP, LIME, and TCAV each explain?
  - C2. Which limitations recur across the research and standards material?
- **D. Regulation and governance**
  - D1. What do GDPR and the UK Information Commissioner's Office require for automated decisions?
  - D2. What does the EU AI Act require for high-risk uses in credit, insurance, and medical devices?
  - D3. What do financial-services governance sources require for model review, auditability, and service-provider controls?
- **E. Audit and accountability**
  - E1. Where can XAI methods strengthen first-line validation, second-line model risk review, and third-line audit?
  - E2. Why do governance controls remain necessary even when explanation methods are available?
- **F. Agentic systems**
  - F1. Why are multi-step agentic systems harder to explain than single-model predictions?
  - F2. Does current mechanistic-interpretability work solve the regulated-sector explanation problem yet?

### §2 Investigation

#### A. Taxonomy and definitions

- [fact; source: https://doi.org/10.1016/j.inffus.2019.12.012; https://doi.org/10.48550/arXiv.1702.08608] The survey literature treats XAI as a family of methods for making model behaviour understandable, while interpretability is the broader goal or property being pursued rather than a single standardised technique.
- [fact; source: https://doi.org/10.1016/j.inffus.2019.12.012] Arrieta et al. organise XAI by model-specific versus model-agnostic approaches, local versus global scope, and pre-model, intrinsic, or post-hoc explanation timing.
- [fact; source: https://doi.org/10.6028/NIST.IR.8312] NIST frames explainability around four properties, explanation, meaningful explanation, explanation accuracy, and knowledge limits, which makes audience fit and fidelity part of the definition rather than optional extras.

#### B. Leading institutions and agenda setters

- [fact; source: https://www.darpa.mil/program/explainable-artificial-intelligence] Defense Advanced Research Projects Agency (DARPA) helped set the modern research agenda by funding an explicit Explainable Artificial Intelligence program aimed at more explainable models, human trust, and human-computer explanation dialogue.
- [fact; source: https://doi.org/10.6028/NIST.IR.8312] NIST is a standards-setting anchor for the field because it translated explainability into auditable principles rather than into a single preferred algorithm.
- [fact; source: https://doi.org/10.48550/arXiv.1602.04938; https://doi.org/10.48550/arXiv.1705.07874; https://doi.org/10.48550/arXiv.1711.11279] The canonical method papers came from multiple research environments rather than one lab, with LIME, SHAP, and TCAV each emerging from different author groups and problem framings.
- [inference; source: https://www.darpa.mil/program/explainable-artificial-intelligence; https://doi.org/10.6028/NIST.IR.8312; https://doi.org/10.48550/arXiv.1602.04938; https://doi.org/10.48550/arXiv.1705.07874; https://doi.org/10.48550/arXiv.1711.11279] The defensible description of leadership is therefore distributed, public research programmes and standards bodies shaped the agenda, while academia and industry-linked researchers supplied the most widely reused techniques.

#### C. Technique families and limitations

- [fact; source: https://doi.org/10.48550/arXiv.1602.04938] LIME explains a particular prediction by fitting a locally interpretable surrogate model around that prediction.
- [fact; source: https://doi.org/10.48550/arXiv.1705.07874] SHAP assigns feature-importance values to a particular prediction and presents itself as a unifying additive framework with desirable consistency properties.
- [fact; source: https://doi.org/10.48550/arXiv.1711.11279] TCAV explains model behaviour in terms of human-defined concepts rather than raw features, which makes it useful when stakeholders reason in concepts such as "stripes" or clinical attributes instead of pixels or coefficients.
- [fact; source: https://doi.org/10.48550/arXiv.1702.08608; https://doi.org/10.6028/NIST.IR.8312] The foundational literature repeatedly warns that explanation quality depends on the audience, the decision context, and whether the explanation is actually faithful to the underlying model process.
- [inference; source: https://doi.org/10.48550/arXiv.1602.04938; https://doi.org/10.48550/arXiv.1705.07874; https://doi.org/10.48550/arXiv.1711.11279; https://doi.org/10.6028/NIST.IR.8312] No single XAI technique satisfies all regulated-sector needs because local feature attribution, local surrogate explanations, and concept-based explanations illuminate different parts of the problem.

#### D. GDPR and information rights

- [fact; source: https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng; https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/explaining-decisions-made-with-artificial-intelligence/part-1-the-basics-of-explaining-ai/legal-framework/] GDPR Articles 13 to 15 require meaningful information about the logic involved, plus the significance and envisaged consequences, when solely automated decision-making with legal or similarly significant effects is in scope.
- [fact; source: https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng; https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/explaining-decisions-made-with-artificial-intelligence/part-1-the-basics-of-explaining-ai/legal-framework/] GDPR Article 22 gives people the right not to be subject to solely automated decisions with legal or similarly significant effects, subject to exceptions and safeguards including human intervention, expression of view, and contesting the decision.
- [fact; source: https://ec.europa.eu/newsroom/article29/item-detail.cfm?item_id=612053; https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/explaining-decisions-made-with-artificial-intelligence/part-1-the-basics-of-explaining-ai/legal-framework/] Official European and UK guidance interprets these duties as explanation and contestability duties, not as a requirement to disclose source code or a full mathematical description of the model.

#### E. EU AI Act and regulated-sector product controls

- [fact; source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689] The EU AI Act treats AI systems used to evaluate the creditworthiness of natural persons or establish their credit score, and AI systems used to evaluate risk, pricing, or underwriting in health and life insurance, as high-risk uses.
- [fact; source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689] The EU AI Act also treats qualifying medical-device and in-vitro-diagnostic Artificial Intelligence systems covered by Annex II product legislation as high-risk when third-party conformity assessment applies.
- [fact; source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689] For high-risk systems, the Act requires logging capabilities, user-facing information, human oversight, technical documentation, and appropriate accuracy, robustness, and cybersecurity controls.
- [inference; source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689; https://doi.org/10.6028/NIST.IR.8312] The EU AI Act therefore operationalises explainability mainly through process controls and documentation obligations, while leaving the choice of concrete XAI technique open.

#### F. Financial-services governance and audit

- [fact; source: https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm] SR 11-7 requires model validation to include evaluation of conceptual soundness, ongoing monitoring, and outcomes analysis, and it treats effective challenge as a central governance mechanism.
- [fact; source: https://www.bankofengland.co.uk/-/media/boe/files/fintech/ai-public-private-forum-final-report.pdf; https://www.bankofengland.co.uk/prudential-regulation/publication/2022/october/artificial-intelligence; https://www.bankofengland.co.uk/prudential-regulation/publication/2023/october/artificial-intelligence-and-machine-learning] UK financial-services material treats explainability as part of model-risk management, governance, and accountability rather than as a stand-alone technical compliance exercise.
- [fact; source: https://www.apra.gov.au/operational-risk-management] APRA's operational-risk framework emphasises critical operations, material service providers, disruption tolerance, and notification obligations, which pull AI systems into traceability and accountability controls even though the standard is technology-neutral.
- [fact; source: https://www.iso.org/standard/42001] The public summary of ISO/IEC 42001 presents traceability, transparency, reliability, and continual improvement as core management-system benefits for organisational AI governance.
- [inference; source: https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm; https://www.bankofengland.co.uk/-/media/boe/files/fintech/ai-public-private-forum-final-report.pdf; https://www.apra.gov.au/operational-risk-management; https://www.iso.org/standard/42001] These governance sources converge on the same practical requirement: organisations must be able to reconstruct what the model or system did, why it was allowed to do it, and who is accountable for the decision.

#### G. Healthcare-specific controls

- [fact; source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689; https://www.fda.gov/regulatory-information/search-fda-guidance-documents/artificial-intelligence-enabled-device-software-functions-lifecycle-management-and-marketing] In healthcare, the most visible current controls are not generic "right to explanation" rules but regulated-device obligations around lifecycle management, documentation, monitoring, and high-risk classification.
- [inference; source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689; https://www.fda.gov/regulatory-information/search-fda-guidance-documents/artificial-intelligence-enabled-device-software-functions-lifecycle-management-and-marketing] Healthcare regulation therefore resembles financial-services regulation in one important way: explainability matters most where it supports safety, reviewability, and post-deployment accountability.

#### H. Agentic AI and mechanistic interpretability

- [fact; source: https://www.anthropic.com/research/tracing-thoughts-language-model] Anthropic's 2025 mechanistic-interpretability work shows that internal circuit tracing can reveal planning, multilingual conceptual processing, and fabricated reasoning in a modern language model.
- [fact; source: https://www.anthropic.com/research/tracing-thoughts-language-model] Anthropic also states that the current method captures only a fraction of total computation, requires hours of human effort on short prompts, and does not yet scale cleanly to long reasoning chains.
- [inference; source: https://www.anthropic.com/research/tracing-thoughts-language-model; https://doi.org/10.6028/NIST.IR.8312; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689] Mechanistic interpretability is therefore promising as a research path for agentic-system explanation, but it is not yet a practical substitute for logs, workflow provenance, human review, and bounded authority in regulated production systems.

#### I. Prior-work cross-reference

- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-24-ai-agent-regulation-global-financial-services.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-ai-governance-assurance-change-control-verification.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-02-28-ai-control-testing-and-assurance.md] Prior completed items in this repository already showed that regulated AI deployment depends on explainability-adjacent control surfaces such as audit trails, human oversight, model-risk governance, and traceable change control.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-24-ai-agent-regulation-global-financial-services.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-ai-governance-assurance-change-control-verification.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-02-28-ai-control-testing-and-assurance.md; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689] This item strengthens those conclusions by showing that mainstream regulation also defines explainability mostly through governance artefacts, user information, and intervention rights rather than through a prescribed explanation algorithm.

#### J. Source-qualification notes

- [assumption; source: https://www.iso.org/standard/42001] The public ISO page is sufficient for high-level claims about management-system intent, but not for clause-level claims about specific explainability controls inside ISO/IEC 42001.
- [assumption; source: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/artificial-intelligence-enabled-device-software-functions-lifecycle-management-and-marketing] The FDA draft-guidance landing page is used as evidence for lifecycle-management expectations, not as evidence of final binding healthcare rules.

### §3 Reasoning

- [fact; source: https://doi.org/10.6028/NIST.IR.8312; https://doi.org/10.48550/arXiv.1702.08608] The research literature and standards material agree that explanation quality depends on fidelity and audience fit, not merely on producing any explanation artifact.
- [fact; source: https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689; https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm] The strongest regulatory sources impose rights, safeguards, logging, documentation, monitoring, and oversight duties, but they do not mandate SHAP, LIME, TCAV, or any other named method.
- [inference; source: https://doi.org/10.48550/arXiv.1602.04938; https://doi.org/10.48550/arXiv.1705.07874; https://doi.org/10.48550/arXiv.1711.11279; https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm] XAI methods are therefore best understood as evidence-generating tools for governance and audit, not as direct substitutes for model governance or accountability assignment.
- [inference; source: https://www.anthropic.com/research/tracing-thoughts-language-model; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689] Agentic systems intensify the gap because explanation must cover a chain of model invocations, tool calls, and handoffs rather than a single prediction event.

### §4 Consistency Check

- [fact; source: https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng; https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/explaining-decisions-made-with-artificial-intelligence/part-1-the-basics-of-explaining-ai/legal-framework/] GDPR and the ICO focus on information, safeguards, and contestability for significant solely automated decisions.
- [fact; source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689] The EU AI Act adds system-level product and lifecycle controls for high-risk uses.
- [fact; source: https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm; https://www.bankofengland.co.uk/-/media/boe/files/fintech/ai-public-private-forum-final-report.pdf; https://www.apra.gov.au/operational-risk-management] Financial-services guidance uses model-risk-management and operational-risk language rather than XAI language.
- [inference; source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689; https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm; https://www.apra.gov.au/operational-risk-management] These regimes are complementary rather than contradictory because all of them route back to traceability, human review, and accountable governance.
- [inference; source: https://www.anthropic.com/research/tracing-thoughts-language-model] The only material unresolved tension is between the growing technical ambition of agentic systems and the immature state of scalable internal-mechanism explanation.

### §5 Depth and Breadth Expansion

- [inference; source: https://doi.org/10.6028/NIST.IR.8312; https://www.bankofengland.co.uk/-/media/boe/files/fintech/ai-public-private-forum-final-report.pdf] **Technical lens:** regulated explanation needs differ by audience, because an auditor, validator, supervisor, clinician, and affected customer do not need the same artifact.
- [inference; source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689; https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/explaining-decisions-made-with-artificial-intelligence/part-1-the-basics-of-explaining-ai/legal-framework/] **Regulatory lens:** law and regulation usually ask for reviewability, intervention, and disclosure fit for purpose, not for complete epistemic transparency of the underlying model.
- [inference; source: https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm; https://www.apra.gov.au/operational-risk-management; https://www.iso.org/standard/42001] **Operational lens:** the control burden is organisational as much as technical, because institutions must own model inventories, monitoring, service-provider risk, documentation, and escalation paths.
- [inference; source: https://www.anthropic.com/research/tracing-thoughts-language-model; https://doi.org/10.6028/NIST.IR.8312] **Behavioural lens:** plausible explanations are not automatically faithful explanations, which is why regulated use cannot rely on model self-description alone.

### §6 Synthesis

**Executive summary:**

Current regulation in heavily regulated industries requires explainability mainly as a governance capability, not as a mandate to use any single Explainable Artificial Intelligence (XAI) method. [inference; source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689; https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/explaining-decisions-made-with-artificial-intelligence/part-1-the-basics-of-explaining-ai/legal-framework/; https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm] The strongest current obligations converge on logging, technical documentation, meaningful user information, human intervention, monitoring, and named accountability. [fact; source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689; https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng; https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm] SHAP, LIME, TCAV, and related techniques are useful components of that governance stack, especially for validation, challenge, and explanation artifacts tailored to different audiences, but none of them by itself satisfies the full regulated-sector burden. [inference; source: https://doi.org/10.48550/arXiv.1602.04938; https://doi.org/10.48550/arXiv.1705.07874; https://doi.org/10.48550/arXiv.1711.11279; https://doi.org/10.6028/NIST.IR.8312] For agentic AI systems, current internal-mechanism research is promising but still too immature to replace workflow provenance, bounded authority, and human review. [inference; source: https://www.anthropic.com/research/tracing-thoughts-language-model; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689]

**Key findings:**

1. **The current XAI field is best described as a taxonomy of complementary explanation methods rather than a single dominant technique, with stable axes such as local versus global, ante-hoc versus post-hoc, and model-specific versus model-agnostic appearing across the survey literature.** ([fact]; high confidence; source: https://doi.org/10.1016/j.inffus.2019.12.012; https://doi.org/10.48550/arXiv.1702.08608)
2. **Public research leadership in XAI is distributed across agenda-setting programmes and standards bodies such as DARPA and NIST, while widely reused methods such as LIME, SHAP, and TCAV came from different author groups rather than one frontier institution.** ([inference]; high confidence; source: https://www.darpa.mil/program/explainable-artificial-intelligence; https://doi.org/10.6028/NIST.IR.8312; https://doi.org/10.48550/arXiv.1602.04938; https://doi.org/10.48550/arXiv.1705.07874; https://doi.org/10.48550/arXiv.1711.11279)
3. **Named XAI techniques explain different things, because LIME provides local surrogate explanations, SHAP assigns local feature contributions, and TCAV maps internal behaviour to human concepts.** ([fact]; high confidence; source: https://doi.org/10.48550/arXiv.1602.04938; https://doi.org/10.48550/arXiv.1705.07874; https://doi.org/10.48550/arXiv.1711.11279)
4. **Data-protection rules do not require source-code disclosure, but they do require meaningful information, significance, consequences, and contestability when solely automated decisions have legal or similarly significant effects on a person.** ([fact]; high confidence; source: https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng; https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/explaining-decisions-made-with-artificial-intelligence/part-1-the-basics-of-explaining-ai/legal-framework/; https://ec.europa.eu/newsroom/article29/item-detail.cfm?item_id=612053)
5. **The EU AI Act classifies creditworthiness, life and health insurance, and qualifying medical-device uses as high-risk and attaches logging, user information, human oversight, technical documentation, and robustness obligations to those systems.** ([fact]; high confidence; source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689)
6. **Financial-services governance sources treat explainability as part of model-risk management and auditability, because SR 11-7, the Bank of England material, APRA CPS 230, and ISO/IEC 42001 all emphasise documentation, monitoring, effective challenge, critical operations, and traceable accountability.** ([inference]; high confidence; source: https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm; https://www.bankofengland.co.uk/-/media/boe/files/fintech/ai-public-private-forum-final-report.pdf; https://www.bankofengland.co.uk/prudential-regulation/publication/2022/october/artificial-intelligence; https://www.bankofengland.co.uk/prudential-regulation/publication/2023/october/artificial-intelligence-and-machine-learning; https://www.apra.gov.au/operational-risk-management; https://www.iso.org/standard/42001)
7. **In practice, XAI is most defensible in regulated audit and review when it is used as supporting evidence for validation, challenge, and review decisions, because no reviewed framework allows an explanation artifact to replace human accountability for a consequential decision.** ([inference]; medium confidence; source: https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm; https://www.bankofengland.co.uk/-/media/boe/files/fintech/ai-public-private-forum-final-report.pdf; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-02-28-ai-control-testing-and-assurance.md)
8. **Agentic systems create a harder explanation problem than single-model prediction systems, because decision responsibility is spread across prompts, model calls, tool invocations, and handoffs, while current mechanistic-interpretability work still captures only a partial and labor-intensive view of internal computation.** ([inference]; medium confidence; source: https://www.anthropic.com/research/tracing-thoughts-language-model; https://doi.org/10.6028/NIST.IR.8312; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] XAI taxonomy is multi-axis rather than single-method. | https://doi.org/10.1016/j.inffus.2019.12.012; https://doi.org/10.48550/arXiv.1702.08608 | high | Survey-level anchor. |
| [fact] Field leadership is distributed across DARPA, NIST, and multiple author groups. | https://www.darpa.mil/program/explainable-artificial-intelligence; https://doi.org/10.6028/NIST.IR.8312; https://doi.org/10.48550/arXiv.1602.04938; https://doi.org/10.48550/arXiv.1705.07874; https://doi.org/10.48550/arXiv.1711.11279 | high | No unsupported league table. |
| [fact] LIME, SHAP, and TCAV explain different aspects of behaviour. | https://doi.org/10.48550/arXiv.1602.04938; https://doi.org/10.48550/arXiv.1705.07874; https://doi.org/10.48550/arXiv.1711.11279 | high | Technique differences only. |
| [fact] GDPR requires meaningful information and safeguards for covered automated decisions. | https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng; https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/explaining-decisions-made-with-artificial-intelligence/part-1-the-basics-of-explaining-ai/legal-framework/; https://ec.europa.eu/newsroom/article29/item-detail.cfm?item_id=612053 | high | Rights and safeguards focus. |
| [fact] The EU AI Act assigns high-risk obligations to finance and healthcare uses such as creditworthiness, health and life insurance, and qualifying medical devices. | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689 | high | Logging, information, oversight, robustness. |
| [fact] Financial-services governance sources prioritise monitoring, challenge, and accountability. | https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm; https://www.bankofengland.co.uk/-/media/boe/files/fintech/ai-public-private-forum-final-report.pdf; https://www.bankofengland.co.uk/prudential-regulation/publication/2022/october/artificial-intelligence; https://www.bankofengland.co.uk/prudential-regulation/publication/2023/october/artificial-intelligence-and-machine-learning; https://www.apra.gov.au/operational-risk-management; https://www.iso.org/standard/42001 | high | Technology-neutral governance emphasis. |
| [inference] XAI artifacts support review but do not replace accountable human decision ownership. | https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm; https://www.bankofengland.co.uk/-/media/boe/files/fintech/ai-public-private-forum-final-report.pdf; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-02-28-ai-control-testing-and-assurance.md | medium | Governance inference from reviewed sources. |
| [inference] Agentic-system explainability remains immature relative to current compliance needs. | https://www.anthropic.com/research/tracing-thoughts-language-model; https://doi.org/10.6028/NIST.IR.8312; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689 | medium | Research frontier, not settled control. |

**Assumptions:**

- **Assumption:** The public ISO summary is sufficient for high-level governance claims, but not for clause-by-clause obligations. **Justification:** the accessible official ISO page describes management-system purpose, traceability, transparency, and continual improvement, but the full standard text is paywalled.
- **Assumption:** The FDA draft-guidance landing page is adequate evidence for a current regulatory direction in healthcare, but not for a final binding obligation. **Justification:** the guidance is official and current, but still draft and not the sole basis of the healthcare conclusion.

**Analysis:**

The key interpretive move is to separate explanation methods from explanation obligations. [inference; source: https://doi.org/10.48550/arXiv.1702.08608; https://doi.org/10.6028/NIST.IR.8312] The methods literature asks how to make model behaviour more understandable, while the legal and supervisory material asks what an institution must disclose, document, review, monitor, and be accountable for. [fact; source: https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689; https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm] That distinction explains why regulators rarely name SHAP or LIME directly: they regulate the control objective, not the internal analytics implementation. [inference; source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689; https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm]

The evidence also points to audience-specific explanation as the practical operating model. [inference; source: https://doi.org/10.6028/NIST.IR.8312; https://www.bankofengland.co.uk/-/media/boe/files/fintech/ai-public-private-forum-final-report.pdf] A customer-facing explanation under GDPR is not the same artifact as a validator's challenge package under SR 11-7 or a technical dossier under the EU AI Act, even when they concern the same system. [fact; source: https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng; https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689] For regulated institutions, the right answer is therefore layered explanation, one set of artifacts for affected individuals, another for supervisors and auditors, and another for internal engineering and model-risk teams. [inference; source: https://doi.org/10.6028/NIST.IR.8312; https://www.bankofengland.co.uk/-/media/boe/files/fintech/ai-public-private-forum-final-report.pdf; https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm]

Agentic systems remain the sharpest open edge because explanation scope now includes orchestration and tool-use provenance, not just model output rationale. [inference; source: https://www.anthropic.com/research/tracing-thoughts-language-model; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689] Current mechanistic-interpretability work is valuable evidence that internal reasoning can sometimes be inspected, but it is not yet cheap, complete, or standardised enough to serve as the primary control for regulated deployment. [inference; source: https://www.anthropic.com/research/tracing-thoughts-language-model; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689]

**Risks, gaps, uncertainties:**

- Publicly accessible evidence for ISO/IEC 42001 is summary-level rather than clause-level, so this item does not make detailed claims about exact internal control wording. [fact; source: https://www.iso.org/standard/42001]
- The healthcare portion is narrower than the financial-services portion because the strongest accessible evidence in this session is the EU AI Act and official FDA lifecycle guidance, not a broad set of healthcare-sector supervisory statements. [fact; source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689; https://www.fda.gov/regulatory-information/search-fda-guidance-documents/artificial-intelligence-enabled-device-software-functions-lifecycle-management-and-marketing]
- The research question asks who "leads" XAI, but public evidence supports a distributed leadership answer better than a ranked list of top institutions. [inference; source: https://www.darpa.mil/program/explainable-artificial-intelligence; https://doi.org/10.6028/NIST.IR.8312; https://doi.org/10.48550/arXiv.1602.04938; https://doi.org/10.48550/arXiv.1705.07874; https://doi.org/10.48550/arXiv.1711.11279]
- Mechanistic interpretability is advancing quickly, so the current judgment that it is not yet a deployable compliance control could change materially within one or two research cycles. [inference; source: https://www.anthropic.com/research/tracing-thoughts-language-model]

**Open questions:**

- Which explanation artifact set is sufficient for third-line audit of a multi-agent production workflow that spans multiple models and external tools?
- Do any regulators move from technology-neutral explainability obligations toward named technical control expectations for agentic systems?
- Which healthcare regulators outside the European Union and the United States publish the clearest operational expectations for explainability in AI-enabled clinical workflows?

### §7 Recursive Review

- Claim-label audit: complete
- URL-backed citation audit: complete
- Acronym expansion audit: XAI, AI, EU, AI Act, GDPR, EDPB, SR, NIST, DARPA, SHAP, LIME, TCAV, APRA, UK, FCA, ISO, FDA
- Findings and §6 synthesis parity: complete
- Overall confidence: medium

---

## Findings

### Executive Summary

Current regulation in heavily regulated industries requires explainability mainly as a governance capability, not as a mandate to use any single Explainable Artificial Intelligence (XAI) method. [inference; source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689; https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/explaining-decisions-made-with-artificial-intelligence/part-1-the-basics-of-explaining-ai/legal-framework/; https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm] The strongest current obligations converge on logging, technical documentation, meaningful user information, human intervention, monitoring, and named accountability. [fact; source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689; https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng; https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm] SHAP, Local Interpretable Model-agnostic Explanations (LIME), Testing with Concept Activation Vectors (TCAV), and related techniques are useful components of that governance stack, especially for validation, challenge, and audience-specific explanation artifacts, but none of them by itself satisfies the full regulated-sector burden. [inference; source: https://doi.org/10.48550/arXiv.1602.04938; https://doi.org/10.48550/arXiv.1705.07874; https://doi.org/10.48550/arXiv.1711.11279; https://doi.org/10.6028/NIST.IR.8312] For agentic AI systems, current internal-mechanism research is promising but still too immature to replace workflow provenance, bounded authority, and human review. [inference; source: https://www.anthropic.com/research/tracing-thoughts-language-model; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689]

### Key Findings

1. **The current XAI field is best described as a taxonomy of complementary explanation methods rather than a single dominant technique, with stable axes such as local versus global, ante-hoc versus post-hoc, and model-specific versus model-agnostic appearing across the survey literature.** ([fact]; high confidence; source: https://doi.org/10.1016/j.inffus.2019.12.012; https://doi.org/10.48550/arXiv.1702.08608)
2. **Public research leadership in XAI is distributed across agenda-setting programmes and standards bodies such as DARPA and NIST, while widely reused methods such as LIME, SHAP, and TCAV came from different author groups rather than one frontier institution.** ([inference]; high confidence; source: https://www.darpa.mil/program/explainable-artificial-intelligence; https://doi.org/10.6028/NIST.IR.8312; https://doi.org/10.48550/arXiv.1602.04938; https://doi.org/10.48550/arXiv.1705.07874; https://doi.org/10.48550/arXiv.1711.11279)
3. **Named XAI techniques explain different things, because LIME provides local surrogate explanations, SHAP assigns local feature contributions, and TCAV maps internal behaviour to human concepts.** ([fact]; high confidence; source: https://doi.org/10.48550/arXiv.1602.04938; https://doi.org/10.48550/arXiv.1705.07874; https://doi.org/10.48550/arXiv.1711.11279)
4. **Data-protection rules do not require source-code disclosure, but they do require meaningful information, significance, consequences, and contestability when solely automated decisions have legal or similarly significant effects on a person.** ([fact]; high confidence; source: https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng; https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/explaining-decisions-made-with-artificial-intelligence/part-1-the-basics-of-explaining-ai/legal-framework/; https://ec.europa.eu/newsroom/article29/item-detail.cfm?item_id=612053)
5. **The EU AI Act classifies creditworthiness, life and health insurance, and qualifying medical-device uses as high-risk and attaches logging, user information, human oversight, technical documentation, and robustness obligations to those systems.** ([fact]; high confidence; source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689)
6. **Financial-services governance sources treat explainability as part of model-risk management and auditability, because SR 11-7, the Bank of England material, APRA CPS 230, and ISO/IEC 42001 all emphasise documentation, monitoring, effective challenge, critical operations, and traceable accountability.** ([inference]; high confidence; source: https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm; https://www.bankofengland.co.uk/-/media/boe/files/fintech/ai-public-private-forum-final-report.pdf; https://www.bankofengland.co.uk/prudential-regulation/publication/2022/october/artificial-intelligence; https://www.bankofengland.co.uk/prudential-regulation/publication/2023/october/artificial-intelligence-and-machine-learning; https://www.apra.gov.au/operational-risk-management; https://www.iso.org/standard/42001)
7. **In practice, XAI is most defensible in regulated audit and review when it is used as supporting evidence for validation, challenge, and review decisions, because no reviewed framework allows an explanation artifact to replace human accountability for a consequential decision.** ([inference]; medium confidence; source: https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm; https://www.bankofengland.co.uk/-/media/boe/files/fintech/ai-public-private-forum-final-report.pdf; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-02-28-ai-control-testing-and-assurance.md)
8. **Agentic systems create a harder explanation problem than single-model prediction systems, because decision responsibility is spread across prompts, model calls, tool invocations, and handoffs, while current mechanistic-interpretability work still captures only a partial and labor-intensive view of internal computation.** ([inference]; medium confidence; source: https://www.anthropic.com/research/tracing-thoughts-language-model; https://doi.org/10.6028/NIST.IR.8312; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] XAI taxonomy is multi-axis rather than single-method. | https://doi.org/10.1016/j.inffus.2019.12.012; https://doi.org/10.48550/arXiv.1702.08608 | high | Survey-level anchor. |
| [fact] Field leadership is distributed across DARPA, NIST, and multiple author groups. | https://www.darpa.mil/program/explainable-artificial-intelligence; https://doi.org/10.6028/NIST.IR.8312; https://doi.org/10.48550/arXiv.1602.04938; https://doi.org/10.48550/arXiv.1705.07874; https://doi.org/10.48550/arXiv.1711.11279 | high | No unsupported league table. |
| [fact] LIME, SHAP, and TCAV explain different aspects of behaviour. | https://doi.org/10.48550/arXiv.1602.04938; https://doi.org/10.48550/arXiv.1705.07874; https://doi.org/10.48550/arXiv.1711.11279 | high | Technique differences only. |
| [fact] GDPR requires meaningful information and safeguards for covered automated decisions. | https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng; https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/explaining-decisions-made-with-artificial-intelligence/part-1-the-basics-of-explaining-ai/legal-framework/; https://ec.europa.eu/newsroom/article29/item-detail.cfm?item_id=612053 | high | Rights and safeguards focus. |
| [fact] The EU AI Act assigns high-risk obligations to finance and healthcare uses such as creditworthiness, health and life insurance, and qualifying medical devices. | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689 | high | Logging, information, oversight, robustness. |
| [fact] Financial-services governance sources prioritise monitoring, challenge, and accountability. | https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm; https://www.bankofengland.co.uk/-/media/boe/files/fintech/ai-public-private-forum-final-report.pdf; https://www.bankofengland.co.uk/prudential-regulation/publication/2022/october/artificial-intelligence; https://www.bankofengland.co.uk/prudential-regulation/publication/2023/october/artificial-intelligence-and-machine-learning; https://www.apra.gov.au/operational-risk-management; https://www.iso.org/standard/42001 | high | Technology-neutral governance emphasis. |
| [inference] XAI artifacts support review but do not replace accountable human decision ownership. | https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm; https://www.bankofengland.co.uk/-/media/boe/files/fintech/ai-public-private-forum-final-report.pdf; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-02-28-ai-control-testing-and-assurance.md | medium | Governance inference from reviewed sources. |
| [inference] Agentic-system explainability remains immature relative to current compliance needs. | https://www.anthropic.com/research/tracing-thoughts-language-model; https://doi.org/10.6028/NIST.IR.8312; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689 | medium | Research frontier, not settled control. |

### Assumptions

- **Assumption:** The public ISO summary is sufficient for high-level governance claims, but not for clause-by-clause obligations. **Justification:** the accessible official ISO page describes management-system purpose, traceability, transparency, and continual improvement, but the full standard text is paywalled.
- **Assumption:** The FDA draft-guidance landing page is adequate evidence for a current regulatory direction in healthcare, but not for a final binding obligation. **Justification:** the guidance is official and current, but still draft and not the sole basis of the healthcare conclusion.

### Analysis

The key interpretive move is to separate explanation methods from explanation obligations. [inference; source: https://doi.org/10.48550/arXiv.1702.08608; https://doi.org/10.6028/NIST.IR.8312] The methods literature asks how to make model behaviour more understandable, while the legal and supervisory material asks what an institution must disclose, document, review, monitor, and be accountable for. [fact; source: https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689; https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm] That distinction explains why regulators rarely name SHAP or LIME directly: they regulate the control objective, not the internal analytics implementation. [inference; source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689; https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm]

The evidence also points to audience-specific explanation as the practical operating model. [inference; source: https://doi.org/10.6028/NIST.IR.8312; https://www.bankofengland.co.uk/-/media/boe/files/fintech/ai-public-private-forum-final-report.pdf] A customer-facing explanation under GDPR is not the same artifact as a validator's challenge package under SR 11-7 or a technical dossier under the EU AI Act, even when they concern the same system. [fact; source: https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng; https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689] For regulated institutions, the right answer is therefore layered explanation: one set of artifacts for affected individuals, another for supervisors and auditors, and another for internal engineering and model-risk teams. [inference; source: https://doi.org/10.6028/NIST.IR.8312; https://www.bankofengland.co.uk/-/media/boe/files/fintech/ai-public-private-forum-final-report.pdf; https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm]

Agentic systems remain the sharpest open edge because explanation scope now includes orchestration and tool-use provenance, not just model output rationale. [inference; source: https://www.anthropic.com/research/tracing-thoughts-language-model; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689] Current mechanistic-interpretability work is valuable evidence that internal reasoning can sometimes be inspected, but it is not yet cheap, complete, or standardised enough to serve as the primary control for regulated deployment. [inference; source: https://www.anthropic.com/research/tracing-thoughts-language-model; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689]

### Risks, Gaps, and Uncertainties

- Publicly accessible evidence for ISO/IEC 42001 is summary-level rather than clause-level, so this item does not make detailed claims about exact internal control wording. [fact; source: https://www.iso.org/standard/42001]
- The healthcare portion is narrower than the financial-services portion because the strongest accessible evidence in this session is the EU AI Act and official FDA lifecycle guidance, not a broad set of healthcare-sector supervisory statements. [fact; source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689; https://www.fda.gov/regulatory-information/search-fda-guidance-documents/artificial-intelligence-enabled-device-software-functions-lifecycle-management-and-marketing]
- The research question asks who "leads" XAI, but public evidence supports a distributed leadership answer better than a ranked list of top institutions. [inference; source: https://www.darpa.mil/program/explainable-artificial-intelligence; https://doi.org/10.6028/NIST.IR.8312; https://doi.org/10.48550/arXiv.1602.04938; https://doi.org/10.48550/arXiv.1705.07874; https://doi.org/10.48550/arXiv.1711.11279]
- Mechanistic interpretability is advancing quickly, so the current judgment that it is not yet a deployable compliance control could change materially within one or two research cycles. [inference; source: https://www.anthropic.com/research/tracing-thoughts-language-model]

### Open Questions

- Which explanation artifact set is sufficient for third-line audit of a multi-agent production workflow that spans multiple models and external tools?
- Do any regulators move from technology-neutral explainability obligations toward named technical control expectations for agentic systems?
- Which healthcare regulators outside the European Union and the United States publish the clearest operational expectations for explainability in AI-enabled clinical workflows?

### Output

- Type: knowledge
- Description: Cross-sector synthesis of XAI research, leading institutions, and the way current regulation turns explainability into logging, documentation, oversight, and auditability duties.
- Links:
  - https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689
  - https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng
  - https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm

---

## Output

- Type: knowledge
- Description: Cross-sector synthesis of XAI research, leading institutions, and the way current regulation turns explainability into logging, documentation, oversight, and auditability duties.
- Links:
  - https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689
  - https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng
  - https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm
