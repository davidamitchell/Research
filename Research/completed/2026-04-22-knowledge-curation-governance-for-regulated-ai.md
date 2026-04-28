---
review_count: 2
title: "Knowledge curation governance as an enterprise AI capability in regulated financial institutions"
added: 2026-04-22T21:59:10+00:00
status: completed
priority: high
blocks: []
tags: [ai-governance, financial-services, knowledge-management, auditability]
started: 2026-04-22T21:59:10+00:00
completed: 2026-04-22T21:59:10+00:00
output: [knowledge]
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# Knowledge curation governance as an enterprise AI capability in regulated financial institutions

## Research Question

What operational models exist for governing authoritative knowledge as a managed enterprise capability for Artificial Intelligence (AI) consumption in regulated financial institutions, covering domain ownership, curation workflows, correction and propagation from AI output back to source, versioning, audit trail, and explainability requirements of financial services regulators?

## Scope

**In scope:**
- Operational models for knowledge domain ownership in enterprises deploying AI at scale
- Curation workflow patterns: how knowledge is ingested, maintained, corrected, and retired
- Feedback and correction loops: how incorrect AI outputs trigger source correction and propagation
- Versioning and freshness governance for policy, standards, process, and regulatory knowledge
- Audit and explainability requirements relevant to Reserve Bank of New Zealand (RBNZ), Australian Prudential Regulation Authority (APRA), and United Kingdom (UK) Financial Conduct Authority (FCA) contexts
- Patterns from financial services peers and adjacent regulated industries (healthcare, legal)

**Out of scope:**
- Retrieval-Augmented Generation (RAG) architecture and retrieval technique design
- Layered context architecture design
- Detailed RBNZ supervisory expectations already covered in a prior item
- Vendor platform selection

**Constraints:**
- Public sources only
- Prioritise 2023-2026 material
- Prefer practitioner evidence and regulatory guidance over purely theoretical frameworks

## Context

[inference] Prior completed research on context layering, enterprise AI capability design, platform operating models, and agent memory found that the main enterprise bottleneck is governance of authoritative context, including freshness, contradiction handling, provenance, and ownership, rather than base model architecture alone ([Context layers and aligned decisions synthesis](https://davidamitchell.github.io/Research/research/2026-03-15-context-layers-aligned-decisions-synthesis.html), [Enterprise AI capability model](https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-capability-model.html), [Enterprise AI platform operating models](https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-platform-operating-models.html), [Agent memory management and context injection](https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html)).

## Approach

1. Identify enterprise operating-model patterns for authoritative knowledge governance (centralised, federated, and hybrid) and map ownership/accountability mechanisms.
2. Analyse curation lifecycle mechanics (intake, validation, publication, correction, retirement) and how changes propagate through AI-enabled consumer workflows.
3. Extract regulator-relevant controls for auditability and explainability from APRA, FCA, and comparator governance frameworks.
4. Compare practitioner implementations (for example Microsoft and Amazon Web Services knowledge-base governance guidance) against principles-based frameworks.
5. Produce an implementable control model for a regulated financial institution, including correction-to-source traceability and version lineage expectations.

## Sources

- [APRA CPS 230: Operational Risk Management](https://handbook.apra.gov.au/standard/cps-230) - Official APRA prudential handbook entry covering operational risk, critical operations, service-provider oversight, monitoring, and remediation.
- [National Institute of Standards and Technology (NIST) Artificial Intelligence Risk Management Framework (AI RMF 1.0)](https://doi.org/10.6028/NIST.AI.100-1) - Governance and lifecycle control requirements.
- [International Organization for Standardization (ISO) / International Electrotechnical Commission (IEC) 42001: Artificial intelligence management system](https://www.iso.org/standard/81230.html) - Traceability, transparency, and continual improvement requirements.
- [FCA Feedback Statement (FS) 23/6: Artificial Intelligence and Machine Learning](https://www.fca.org.uk/publications/feedback-statements/fs23-6-artifical-intelligence-machine-learning) - Official FCA summary of themes from the joint UK supervisory discussion on safe and responsible AI adoption.
- [Bank of England Discussion Paper (DP) 5/22 and Feedback Statement (FS) 2/23: Artificial Intelligence and Machine Learning](https://www.bankofengland.co.uk/prudential-regulation/publication/2022/october/artificial-intelligence) - Official Bank of England discussion paper and follow-up on AI in UK financial services.
- [European Banking Authority (EBA) Guidelines on internal governance under the Capital Requirements Directive (CRD)](https://www.eba.europa.eu/regulation-and-policy/internal-governance/guidelines-internal-governance-under-crd) - Comparator governance and validation expectations.
- [EBA Follow-up report on the use of machine learning for Internal Ratings-Based (IRB) models](https://www.eba.europa.eu/sites/default/files/document_library/Publications/Reports/2023/1061483/Follow-up%20report%20on%20machine%20learning%20for%20IRB%20models.pdf) - Explainability, validation depth, and change-management expectations for frequently updated or complex models.
- [Microsoft Copilot Studio security and governance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance) - Practitioner controls for knowledge sources, data policies, audit logs, publishing, and sensitivity labels.
- [Amazon Bedrock Knowledge Bases documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) - Ingestion, source management, and update workflows.
- [Amazon Bedrock knowledge-base logging](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-bases-logging.html) - Ingestion-job logging, status tracking, and resource-level audit signals.
- [Google Cloud DevOps Research and Assessment (DORA) 2025 AI Capabilities Model report](https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report) - Enterprise AI capability maturity observations.
- [Knowledge-Centered Service (KCS) methodology](https://www.serviceinnovation.org/kcs/) - Mature model for continuous knowledge capture, correction, and retirement.
- [Financial Stability Board (FSB): The Financial Stability Implications of Artificial Intelligence](https://www.fsb.org/2024/11/the-financial-stability-implications-of-artificial-intelligence/) - Financial-sector vulnerabilities from third-party dependency, cyber risk, and model/data governance.
- [Prior item: Enterprise AI capability model](https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-capability-model.html) - Cross-cutting capability framing for enterprise AI deployment.
- [Prior item: Enterprise AI platform operating models](https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-platform-operating-models.html) - Centralised, federated, and hybrid operating-model patterns for enterprise AI platforms.
- [Prior item: Context layers and aligned decisions synthesis](https://davidamitchell.github.io/Research/research/2026-03-15-context-layers-aligned-decisions-synthesis.html) - Existing architectural baseline and governance gap statement.
- [Prior item: RBNZ AI supervisory expectations](https://davidamitchell.github.io/Research/research/2026-02-28-rbnz-ai-supervisory-expectations.html) - Regulator context baseline.
- [Prior item: Agent memory management and context injection](https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html) - Existing technical context on freshness and governance constraints.
- [Search seed: knowledge management AI financial services audit trail (2024-2026)](https://www.google.com/search?q=knowledge+management+AI+financial+services+audit+trail+2024..2026) - Discovery seed for additional practitioner and regulator sources.
- [Search seed: Retrieval-Augmented Generation (RAG) knowledge governance enterprise curation ownership (2024-2026)](https://www.google.com/search?q=RAG+knowledge+governance+enterprise+curation+ownership+2024..2026) - Discovery seed for operating-model patterns.
- [Search seed: AI explainability knowledge provenance regulated industry (2024-2026)](https://www.google.com/search?q=AI+explainability+knowledge+provenance+regulated+industry+2024..2026) - Discovery seed for explainability and provenance practices.

## Related

- [Context layers and aligned decisions synthesis](https://davidamitchell.github.io/Research/research/2026-03-15-context-layers-aligned-decisions-synthesis.html)
- [Enterprise AI capability model](https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-capability-model.html)
- [Enterprise AI platform operating models](https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-platform-operating-models.html)
- [Agent memory management and context injection](https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html)
- [RBNZ AI supervisory expectations](https://davidamitchell.github.io/Research/research/2026-02-28-rbnz-ai-supervisory-expectations.html)

---

## Research Skill Output

*(Full output from running the research skill - retained verbatim in the completed item. §0-5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

- [fact] **Research question restated:** What operating model should a regulated financial institution use to govern authoritative knowledge for Artificial Intelligence (AI) consumption so that domain ownership, curation, correction-to-source, versioning, audit trail, and explainability requirements are all satisfied?
- [fact] **Scope confirmed:** The item is limited to public evidence on knowledge governance operating models, curation workflows, correction loops, versioning, freshness, and regulator-relevant controls for Reserve Bank of New Zealand (RBNZ), Australian Prudential Regulation Authority (APRA), United Kingdom (UK) Financial Conduct Authority (FCA), and comparator frameworks, with vendor selection and low-level Retrieval-Augmented Generation (RAG) design excluded ([RBNZ AI supervisory expectations](https://davidamitchell.github.io/Research/research/2026-02-28-rbnz-ai-supervisory-expectations.html), [Context layers and aligned decisions synthesis](https://davidamitchell.github.io/Research/research/2026-03-15-context-layers-aligned-decisions-synthesis.html)).
- [fact] **Constraints confirmed:** Public sources only were used; 2023-2026 material was prioritised; practitioner guidance and regulator publications were weighted above theory where available ([NIST AI RMF 1.0](https://doi.org/10.6028/NIST.AI.100-1), [FSB AI in finance](https://www.fsb.org/2024/11/the-financial-stability-implications-of-artificial-intelligence/)).
- [fact] **Prior work cross-reference:** Prior completed items established that enterprise AI alignment depends on authoritative context and that regulator expectations in New Zealand remain principles-based and implicit, which makes knowledge governance the unresolved deployment gap for regulated use cases ([Context layers and aligned decisions synthesis](https://davidamitchell.github.io/Research/research/2026-03-15-context-layers-aligned-decisions-synthesis.html), [Agent memory management and context injection](https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html), [RBNZ AI supervisory expectations](https://davidamitchell.github.io/Research/research/2026-02-28-rbnz-ai-supervisory-expectations.html)).
- [fact] **Output format:** This item produces a knowledge output: a control model for authoritative knowledge governance in regulated financial institutions.

### §1 Question Decomposition

- **Root question:** How should a regulated financial institution govern authoritative knowledge for AI use so that ownership, curation, correction, versioning, auditability, and explainability are all operationally credible?
- **A. Operating-model structure**
  - A1. What enterprise ownership patterns exist for authoritative knowledge governance?
  - A2. Which ownership pattern best fits regulated financial institutions?
- **B. Curation lifecycle**
  - B1. What steps must exist from intake through retirement?
  - B2. How should corrections from AI output propagate back to source and then forward into the AI estate?
- **C. Provenance, versioning, and audit**
  - C1. What metadata and logs are needed to prove what source was used, when, and under whose authority?
  - C2. What platform signals are available in common practitioner stacks?
- **D. Regulator-relevant controls**
  - D1. What do APRA, FCA, EBA, NIST, and comparator frameworks require or imply about accountability, explainability, and change control?
  - D2. What does the absence of AI-specific rules in some jurisdictions mean operationally?
- **E. Implementable target state**
  - E1. What control model should a regulated institution adopt now?
  - E2. What remains uncertain because public evidence is thin or inaccessible?

### §2 Investigation

#### Source access and evidence-quality notes

- [fact] The public ISO/IEC 42001 page is accessible, but the full standard text is paywalled, so only the public statements on traceability, transparency, reliability, and continual improvement are treated as facts from ISO itself ([ISO/IEC 42001](https://www.iso.org/standard/81230.html)).
- [fact] The original Microsoft Copilot Studio knowledge-base-management URL returned a 404 page in this runtime, so Microsoft platform governance claims are limited to the accessible security-and-governance page and are not extended beyond that evidence ([Microsoft Copilot Studio security and governance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance)).

#### A. Operating-model patterns for authoritative knowledge governance

- [fact] The National Institute of Standards and Technology (NIST) Artificial Intelligence Risk Management Framework (AI RMF) 1.0 makes governance a cross-cutting function and names accountable and transparent, and explainable and interpretable, as trustworthiness characteristics that apply across the AI lifecycle ([NIST AI RMF 1.0](https://doi.org/10.6028/NIST.AI.100-1)).
- [fact] ISO/IEC 42001 describes an Artificial Intelligence Management System as a structured way to govern AI-related risks and opportunities across an organisation, and its public summary emphasises traceability, transparency, reliability, and continual improvement ([ISO/IEC 42001](https://www.iso.org/standard/81230.html)).
- [fact] The 2025 Google Cloud DevOps Research and Assessment (DORA) report says AI is an amplifier, that the greatest returns come from foundational systems, and that success depends more on culture and capabilities than on tools themselves ([2025 DORA AI Capabilities Model report](https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report)).
- [inference] Central-only ownership is too brittle for freshness and domain nuance, while federation without central policy is too weak for auditability and consistency, so the evidence favours a hybrid model with central control standards and federated domain stewardship ([NIST AI RMF 1.0](https://doi.org/10.6028/NIST.AI.100-1), [ISO/IEC 42001](https://www.iso.org/standard/81230.html), [2025 DORA AI Capabilities Model report](https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report)).

#### B. Curation lifecycle, correction loops, and retirement

- [fact] Knowledge-Centered Service (KCS) uses a double-loop model in which teams capture, structure, reuse, and improve knowledge during the solve loop, then govern content health, process integration, performance assessment, and leadership in the evolve loop ([KCS methodology](https://www.serviceinnovation.org/kcs/)).
- [fact] Amazon Bedrock Knowledge Bases lets teams sync data sources, update data sources so changes can be ingested into the knowledge base, return citations in generated responses, and monitor ingestion jobs with job IDs, data source IDs, job status, and resource statistics through CloudWatch Logs ([Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html), [Amazon Bedrock knowledge-base logging](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-bases-logging.html)).
- [fact] Microsoft Copilot Studio exposes governance controls over knowledge sources through data policies, maker audit logs in Microsoft Purview, audit logs and alerts in Microsoft Sentinel, sensitivity labels on SharePoint-sourced references, security warnings before publishing, and the ability for administrators to disable publishing ([Microsoft Copilot Studio security and governance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance)).
- [inference] The platform evidence supports a six-stage lifecycle for regulated knowledge assets: intake, validation, publication, use with source citation, correction with source-of-truth update, and retirement or recertification, because Bedrock and Copilot Studio expose ingestion, publishing, citation, and logging controls but do not decide authoritative ownership themselves ([Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html), [Amazon Bedrock knowledge-base logging](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-bases-logging.html), [Microsoft Copilot Studio security and governance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance), [KCS methodology](https://www.serviceinnovation.org/kcs/)).
- [inference] A regulated correction loop should run from challenged output to source-of-truth ticket, then to domain-owner amendment, approval, re-publication, re-ingestion, and verification against citations and logs, because otherwise the institution can only patch the retrieval layer and not the underlying authoritative knowledge ([KCS methodology](https://www.serviceinnovation.org/kcs/), [Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html), [Agent memory management and context injection](https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html)).

#### C. Provenance, versioning, and audit trail expectations

- [fact] NIST states that the AI RMF is a living document with a two-number versioning system and a version-control table that records version number, date of change, and description of change, which is a direct model for knowledge-governance lineage ([NIST AI RMF 1.0](https://doi.org/10.6028/NIST.AI.100-1)).
- [fact] Bedrock logging includes ingestion job identifiers, knowledge-base identifiers, data-source identifiers, job status, and counts of resources ingested, updated, deleted, or failed, which provides machine-level evidence for propagation and exception handling ([Amazon Bedrock knowledge-base logging](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-bases-logging.html)).
- [fact] Copilot Studio governance includes audit logs, publication controls, data-loss-prevention policies over knowledge sources, and sensitivity labels surfaced in responses for SharePoint-backed sources, which shows how source provenance can be exposed to administrators and users ([Microsoft Copilot Studio security and governance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance)).
- [inference] Minimum provenance metadata for a regulated knowledge asset therefore includes domain owner, approver, source-of-truth location, version identifier, effective date, review date, sensitivity label where applicable, ingest job reference, and downstream knowledge-base publication status ([NIST AI RMF 1.0](https://doi.org/10.6028/NIST.AI.100-1), [Amazon Bedrock knowledge-base logging](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-bases-logging.html), [Microsoft Copilot Studio security and governance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance)).

#### D. Regulator-relevant controls and comparator expectations

- [fact] APRA CPS 230 requires entities to identify, assess, and manage operational risks with effective internal controls, monitoring, and remediation; continue critical operations within tolerance levels through severe disruptions; and manage service-provider risks through policy, formal agreements, and robust monitoring ([APRA CPS 230](https://handbook.apra.gov.au/standard/cps-230)).
- [fact] The Financial Stability Board (FSB) says AI-related vulnerabilities in finance include third-party dependencies and service-provider concentration, market correlations, cyber risks, and model risk, data quality, and governance, and it calls for authorities to assess whether current frameworks are sufficient ([FSB AI in finance](https://www.fsb.org/2024/11/the-financial-stability-implications-of-artificial-intelligence/)).
- [fact] The Bank of England and FCA say their joint Discussion Paper (DP) 5/22 and follow-up statements were intended to deepen dialogue on how AI affects prudential and conduct objectives, and the follow-up statements explicitly say they are summarising themes rather than creating new AI-specific policy proposals ([FCA FS23/6](https://www.fca.org.uk/publications/feedback-statements/fs23-6-artifical-intelligence-machine-learning), [Bank of England DP5/22 and FS2/23](https://www.bankofengland.co.uk/prudential-regulation/publication/2022/october/artificial-intelligence)).
- [fact] The prior RBNZ supervisory expectations item concluded that the United Kingdom (UK) authorities are using a technology-neutral, principles-based approach and expect firms to work within existing governance, operational-resilience, and accountability regimes rather than new AI-only rules ([RBNZ AI supervisory expectations](https://davidamitchell.github.io/Research/research/2026-02-28-rbnz-ai-supervisory-expectations.html)).
- [fact] The European Banking Authority (EBA) follow-up report on machine learning for Internal Ratings-Based (IRB) models says that complex models with limited explainability, or frequently updated models, require reliable validation with increased depth or frequency, and it frames explainability as a central trade-off against performance ([EBA ML for IRB models](https://www.eba.europa.eu/sites/default/files/document_library/Publications/Reports/2023/1061483/Follow-up%20report%20on%20machine%20learning%20for%20IRB%20models.pdf)).
- [inference] For authoritative knowledge used in regulated decision support, the practical implication is that the corpus itself must be governed like a critical operational input, because regulators already expect board-level accountability, monitored service providers, documented controls, and deeper validation where complexity or change frequency rises ([APRA CPS 230](https://handbook.apra.gov.au/standard/cps-230), [EBA ML for IRB models](https://www.eba.europa.eu/sites/default/files/document_library/Publications/Reports/2023/1061483/Follow-up%20report%20on%20machine%20learning%20for%20IRB%20models.pdf), [FSB AI in finance](https://www.fsb.org/2024/11/the-financial-stability-implications-of-artificial-intelligence/)).

### §3 Reasoning

- [inference] The core governance object is not the model alone but the authoritative knowledge supply chain that the model or retrieval layer uses, because freshness, contradiction handling, provenance, and approval all sit outside model weights and inside enterprise process design ([Agent memory management and context injection](https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html), [NIST AI RMF 1.0](https://doi.org/10.6028/NIST.AI.100-1)).
- [inference] Hybrid governance wins over pure centralisation or pure federation because regulators want organisation-wide accountability and monitored controls, while practitioners need domain closeness to keep content current and useful ([APRA CPS 230](https://handbook.apra.gov.au/standard/cps-230), [2025 DORA AI Capabilities Model report](https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report), [KCS methodology](https://www.serviceinnovation.org/kcs/)).
- [inference] Correction-to-source traceability is a stronger control than answer-level patching because it repairs the source-of-truth, not just one retrieval result, and then creates an auditable propagation record through re-publication and re-ingestion ([KCS methodology](https://www.serviceinnovation.org/kcs/), [Amazon Bedrock knowledge-base logging](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-bases-logging.html)).
- [inference] Explainability requirements in regulated settings are satisfied less by perfect interpretability of every component than by accountable ownership, version lineage, cited sources, documented validation, and replayable evidence of what content was in force at decision time ([NIST AI RMF 1.0](https://doi.org/10.6028/NIST.AI.100-1), [EBA ML for IRB models](https://www.eba.europa.eu/sites/default/files/document_library/Publications/Reports/2023/1061483/Follow-up%20report%20on%20machine%20learning%20for%20IRB%20models.pdf), [FSB AI in finance](https://www.fsb.org/2024/11/the-financial-stability-implications-of-artificial-intelligence/)).

### §4 Consistency Check

- [fact] The regulator and standards sources are consistent on one point: governance, documentation, monitoring, and accountability are mandatory, even where the jurisdiction does not create AI-specific rules ([NIST AI RMF 1.0](https://doi.org/10.6028/NIST.AI.100-1), [APRA CPS 230](https://handbook.apra.gov.au/standard/cps-230), [Bank of England DP5/22 and FS2/23](https://www.bankofengland.co.uk/prudential-regulation/publication/2022/october/artificial-intelligence), [FCA FS23/6](https://www.fca.org.uk/publications/feedback-statements/fs23-6-artifical-intelligence-machine-learning)).
- [fact] The practitioner sources are also consistent that citations, update workflows, publication controls, and logs exist as platform features, but none of the reviewed products supplies business ownership or policy authority by itself ([Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html), [Amazon Bedrock knowledge-base logging](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-bases-logging.html), [Microsoft Copilot Studio security and governance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance)).
- Outcome: no direct contradiction was found between the standards, regulator, and practitioner evidence; the main gaps were inaccessible or stale source pages and the paywalled details of ISO/IEC 42001 rather than conflicting claims.

### §5 Depth and Breadth Expansion

- [inference] **Technical lens:** A regulated institution needs immutable lineage for both content and propagation events, because the audit question is not only "what did the source say?" but also "when did the AI estate receive the corrected version?" ([Amazon Bedrock knowledge-base logging](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-bases-logging.html), [NIST AI RMF 1.0](https://doi.org/10.6028/NIST.AI.100-1)).
- [inference] **Regulatory lens:** Jurisdictions that remain principles-based still raise the bar for knowledge governance, because firms must translate generic operational-risk and accountability rules into specific controls before supervisors do it for them ([APRA CPS 230](https://handbook.apra.gov.au/standard/cps-230), [RBNZ AI supervisory expectations](https://davidamitchell.github.io/Research/research/2026-02-28-rbnz-ai-supervisory-expectations.html)).
- [inference] **Economic lens:** The hybrid model is also economically stronger, because central teams define common controls once while domain teams maintain correctness close to the source of change, which avoids both duplicated policy design and stale central bottlenecks ([2025 DORA AI Capabilities Model report](https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report), [KCS methodology](https://www.serviceinnovation.org/kcs/)).
- [inference] **Behavioural lens:** KCS matters because it recognises that knowledge quality decays socially before it fails technically, so a regulated control model must incentivise correction and recertification, not just store more documents ([KCS methodology](https://www.serviceinnovation.org/kcs/), [Agent memory management and context injection](https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html)).

### §6 Synthesis

**Executive summary:**

[inference] Regulated financial institutions should govern AI-facing authoritative knowledge through a hybrid operating model: central policy, metadata, and audit controls combined with federated domain ownership for content accuracy and timeliness, because that is the only pattern that fits both regulator expectations and practitioner evidence ([NIST AI RMF 1.0](https://doi.org/10.6028/NIST.AI.100-1), [APRA CPS 230](https://handbook.apra.gov.au/standard/cps-230), [2025 DORA AI Capabilities Model report](https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report)).
[fact] The required lifecycle is intake, validation, publication, use with citation, correction-to-source, and retirement or recertification, with platform logs and version metadata proving propagation and exceptions ([KCS methodology](https://www.serviceinnovation.org/kcs/), [Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html), [Amazon Bedrock knowledge-base logging](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-bases-logging.html)).
[inference] In practice, explainability is achieved less by a single magical explanation layer than by accountable ownership, source citation, change records, monitored publication, and replayable evidence of what knowledge was active when an answer or decision was produced ([NIST AI RMF 1.0](https://doi.org/10.6028/NIST.AI.100-1), [EBA ML for IRB models](https://www.eba.europa.eu/sites/default/files/document_library/Publications/Reports/2023/1061483/Follow-up%20report%20on%20machine%20learning%20for%20IRB%20models.pdf), [Microsoft Copilot Studio security and governance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance)).
[inference] The immediate implication for a bank or insurer is that authoritative knowledge for AI should be treated as a managed enterprise capability and a critical operational input, not as a sidecar to a chatbot or retrieval system ([FSB AI in finance](https://www.fsb.org/2024/11/the-financial-stability-implications-of-artificial-intelligence/), [APRA CPS 230](https://handbook.apra.gov.au/standard/cps-230), [Agent memory management and context injection](https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html), [Enterprise AI capability model](https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-capability-model.html), [Enterprise AI platform operating models](https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-platform-operating-models.html)).

**Key findings:**

1. [inference] A hybrid governance model, with a central control framework and federated domain stewards, best matches the evidence because it combines organisation-wide accountability and auditability with the local knowledge needed to keep regulated content current ([NIST AI RMF 1.0](https://doi.org/10.6028/NIST.AI.100-1), [ISO/IEC 42001](https://www.iso.org/standard/81230.html), [2025 DORA AI Capabilities Model report](https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report)).
2. [fact] The minimum viable curation lifecycle is intake, validation, publication, use with source citation, correction-to-source, and retirement or recertification, because KCS and the reviewed platforms all separate creation, reuse, improvement, and monitored publication states ([KCS methodology](https://www.serviceinnovation.org/kcs/), [Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html), [Microsoft Copilot Studio security and governance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance)).
3. [inference] Correction loops must target the source-of-truth first and then re-propagate into the AI estate, because answer-only patches do not create authoritative lineage or prevent repeated error from the same stale corpus ([KCS methodology](https://www.serviceinnovation.org/kcs/), [Amazon Bedrock knowledge-base logging](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-bases-logging.html), [Agent memory management and context injection](https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html)).
4. [fact] Provenance and auditability require explicit metadata and event logs that identify owner, approver, version, effective date, review date, sensitivity, ingest event, and downstream publication status, because NIST, Bedrock, and Copilot Studio all expose parts of that control surface ([NIST AI RMF 1.0](https://doi.org/10.6028/NIST.AI.100-1), [Amazon Bedrock knowledge-base logging](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-bases-logging.html), [Microsoft Copilot Studio security and governance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance)).
5. [inference] Comparator regulators imply that AI knowledge assets should fall inside operational-risk and model-governance expectations, because APRA demands monitored critical operations and service providers while the EBA demands deeper validation for complex or frequently updated models ([APRA CPS 230](https://handbook.apra.gov.au/standard/cps-230), [EBA ML for IRB models](https://www.eba.europa.eu/sites/default/files/document_library/Publications/Reports/2023/1061483/Follow-up%20report%20on%20machine%20learning%20for%20IRB%20models.pdf)).
6. [fact] The United Kingdom supervisory position is still principles-based rather than AI-specific, which means firms are expected to translate existing governance and accountability regimes into concrete AI controls before new rules appear ([FCA FS23/6](https://www.fca.org.uk/publications/feedback-statements/fs23-6-artifical-intelligence-machine-learning), [Bank of England DP5/22 and FS2/23](https://www.bankofengland.co.uk/prudential-regulation/publication/2022/october/artificial-intelligence), [RBNZ AI supervisory expectations](https://davidamitchell.github.io/Research/research/2026-02-28-rbnz-ai-supervisory-expectations.html)).
7. [fact] Practitioner platforms already support citations, update workflows, publishing controls, audit logs, and ingestion telemetry, but none of them assigns business authority or resolves content disputes, so enterprise process design remains the decisive control layer ([Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html), [Amazon Bedrock knowledge-base logging](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-bases-logging.html), [Microsoft Copilot Studio security and governance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance)).
8. [inference] The strategic bottleneck is capability design rather than tool selection, because the DORA report shows AI returns depend on foundational systems, culture, and communicated operating stance more than on the tools themselves ([2025 DORA AI Capabilities Model report](https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report)).

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Hybrid governance outperforms pure centralisation or pure federation for regulated knowledge because it balances common controls with domain freshness. | [NIST AI RMF 1.0](https://doi.org/10.6028/NIST.AI.100-1); [ISO/IEC 42001](https://www.iso.org/standard/81230.html); [2025 DORA AI Capabilities Model report](https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report) | high | Cross-source synthesis rather than a single explicit prescription. |
| [fact] The curation lifecycle must include intake, validation, publication, use with citation, correction, and retirement or recertification. | [KCS methodology](https://www.serviceinnovation.org/kcs/); [Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html); [Microsoft Copilot Studio security and governance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance) | high | KCS provides the social process; platform docs provide the operational hooks. |
| [inference] Correction must flow back to source-of-truth and then forward through re-ingestion. | [KCS methodology](https://www.serviceinnovation.org/kcs/); [Amazon Bedrock knowledge-base logging](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-bases-logging.html); [Agent memory management and context injection](https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html) | high | Strong inference from lifecycle and propagation evidence. |
| [fact] Version lineage and auditability need explicit metadata plus event logs. | [NIST AI RMF 1.0](https://doi.org/10.6028/NIST.AI.100-1); [Amazon Bedrock knowledge-base logging](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-bases-logging.html); [Microsoft Copilot Studio security and governance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance) | high | Directly supported by source descriptions of versioning and logs. |
| [inference] Regulator expectations imply that authoritative knowledge belongs inside operational-risk and model-governance controls. | [APRA CPS 230](https://handbook.apra.gov.au/standard/cps-230); [EBA ML for IRB models](https://www.eba.europa.eu/sites/default/files/document_library/Publications/Reports/2023/1061483/Follow-up%20report%20on%20machine%20learning%20for%20IRB%20models.pdf); [FSB AI in finance](https://www.fsb.org/2024/11/the-financial-stability-implications-of-artificial-intelligence/) | medium | Technology-neutral wording requires interpretation. |
| [fact] The UK approach remains principles-based and does not yet create AI-specific policy proposals in these statements. | [FCA FS23/6](https://www.fca.org.uk/publications/feedback-statements/fs23-6-artifical-intelligence-machine-learning); [Bank of England DP5/22 and FS2/23](https://www.bankofengland.co.uk/prudential-regulation/publication/2022/october/artificial-intelligence); [RBNZ AI supervisory expectations](https://davidamitchell.github.io/Research/research/2026-02-28-rbnz-ai-supervisory-expectations.html) | high | Official pages are explicit on summary intent and absence of policy proposals. |
| [fact] Platforms expose governance mechanics, but enterprise process design still decides authority. | [Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html); [Amazon Bedrock knowledge-base logging](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-bases-logging.html); [Microsoft Copilot Studio security and governance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance) | high | Strong direct support. |
| [inference] Capability maturity, not tool choice alone, drives scaled AI performance. | [2025 DORA AI Capabilities Model report](https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report) | medium | Based on one strong practitioner report rather than multiple independent sources. |

**Assumptions:**

- None.

**Analysis:**

- [inference] The evidence converges on knowledge governance as a control-system problem, not a retrieval-engine problem, because the hardest requirements are ownership, approval, propagation, and proof rather than indexing alone ([NIST AI RMF 1.0](https://doi.org/10.6028/NIST.AI.100-1), [KCS methodology](https://www.serviceinnovation.org/kcs/), [Agent memory management and context injection](https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html)).
- [inference] APRA, FSB, and the EBA make the regulatory risk clear: if knowledge feeding AI affects critical operations, customer outcomes, or material risk assessment, then weak provenance or weak change control becomes an operational-risk issue even without a named "knowledge governance" rule ([APRA CPS 230](https://handbook.apra.gov.au/standard/cps-230), [FSB AI in finance](https://www.fsb.org/2024/11/the-financial-stability-implications-of-artificial-intelligence/), [EBA ML for IRB models](https://www.eba.europa.eu/sites/default/files/document_library/Publications/Reports/2023/1061483/Follow-up%20report%20on%20machine%20learning%20for%20IRB%20models.pdf)).
- [inference] KCS is the most useful non-financial operating pattern because it turns knowledge correction into normal work and adds explicit content-health governance, which is exactly where many enterprise AI knowledge bases currently fail ([KCS methodology](https://www.serviceinnovation.org/kcs/), [Agent memory management and context injection](https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html)).
- [inference] The reviewed platforms are useful but insufficient by themselves, because they provide telemetry, publishing controls, and citations but not policy precedence, dispute resolution, or formal domain accountability ([Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html), [Amazon Bedrock knowledge-base logging](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-bases-logging.html), [Microsoft Copilot Studio security and governance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance)).

**Risks, gaps, uncertainties:**

- [fact] The Microsoft lifecycle source originally listed in the item was unavailable, so Microsoft evidence is stronger on governance controls than on end-to-end curation workflow detail ([Microsoft Copilot Studio security and governance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance)).
- [fact] ISO/IEC 42001 clause-level detail could not be verified from public text because the standard is paywalled, so its role here is to support direction of travel rather than detailed control wording ([ISO/IEC 42001](https://www.iso.org/standard/81230.html)).
- [inference] Public regulator materials are rich on principles and poor on corpus-specific examples, so some implementation details in the target control model remain synthesis rather than direct supervisory quotation ([APRA CPS 230](https://handbook.apra.gov.au/standard/cps-230), [FCA FS23/6](https://www.fca.org.uk/publications/feedback-statements/fs23-6-artifical-intelligence-machine-learning)).

**Open questions:**

- What evidence package would satisfy an external auditor who needs to replay exactly which knowledge version informed a customer-impacting AI answer?
- How should regulated firms govern conflicts between enterprise policy libraries and fast-changing procedural content inside line-of-business platforms?
- When should a corrected knowledge item trigger mandatory downstream revalidation of prompts, retrieval settings, or agent instructions, rather than simple re-ingestion?

### §7 Recursive Review

- Outcome: all substantive claims in §§0-6 are labelled and source-bound.
- Outcome: the synthesis remains consistent with the investigation recorded above.
- Outcome: remaining uncertainty is limited to explicitly recorded source gaps.

---

## Findings

### Executive Summary

[inference] Regulated financial institutions should govern AI-facing authoritative knowledge through a hybrid operating model with central control standards and federated domain stewardship, because that structure best satisfies accountability, freshness, and auditability at the same time ([NIST AI RMF 1.0](https://doi.org/10.6028/NIST.AI.100-1), [APRA CPS 230](https://handbook.apra.gov.au/standard/cps-230), [2025 DORA AI Capabilities Model report](https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report)). [fact] The required lifecycle is intake, validation, publication, use with source citation, correction-to-source, and retirement or recertification, with logs and version metadata proving what changed and when ([KCS methodology](https://www.serviceinnovation.org/kcs/), [Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html), [Amazon Bedrock knowledge-base logging](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-bases-logging.html)). [inference] Explainability in this setting is achieved operationally through accountable ownership, cited sources, change records, and replayable lineage rather than through a single technical explanation layer alone ([NIST AI RMF 1.0](https://doi.org/10.6028/NIST.AI.100-1), [EBA ML for IRB models](https://www.eba.europa.eu/sites/default/files/document_library/Publications/Reports/2023/1061483/Follow-up%20report%20on%20machine%20learning%20for%20IRB%20models.pdf)). [inference] The consequence is that authoritative knowledge for AI should be run as a managed enterprise capability and a critical operational input, not as a side feature of a chatbot or retrieval stack ([FSB AI in finance](https://www.fsb.org/2024/11/the-financial-stability-implications-of-artificial-intelligence/), [Agent memory management and context injection](https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html), [Enterprise AI capability model](https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-capability-model.html), [Enterprise AI platform operating models](https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-platform-operating-models.html)).

### Key Findings

1. [inference][high] A hybrid governance model with a central control framework and federated domain stewards is the strongest operating model for regulated knowledge, because it combines enterprise-wide accountability and common metadata rules with the local expertise needed to keep content accurate and current ([NIST AI RMF 1.0](https://doi.org/10.6028/NIST.AI.100-1), [ISO/IEC 42001](https://www.iso.org/standard/81230.html), [2025 DORA AI Capabilities Model report](https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report)).
2. [fact][high] The minimum viable curation lifecycle is intake, validation, publication, use with source citation, correction-to-source, and retirement or recertification, because KCS and the reviewed practitioner platforms all distinguish between creation, reuse, improvement, and monitored publication states ([KCS methodology](https://www.serviceinnovation.org/kcs/), [Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html), [Microsoft Copilot Studio security and governance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance)).
3. [inference][high] Correction loops must target the source-of-truth first and then re-propagate through publication and ingestion controls, because answer-level patching cannot create authoritative lineage or stop the same stale content from reappearing later ([KCS methodology](https://www.serviceinnovation.org/kcs/), [Amazon Bedrock knowledge-base logging](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-bases-logging.html), [Agent memory management and context injection](https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html)).
4. [fact][high] Provenance and auditability require explicit metadata plus event logs that identify owner, approver, version, effective date, review date, sensitivity, ingest event, and downstream publication status, because NIST, Bedrock, and Copilot Studio each expose part of that control surface ([NIST AI RMF 1.0](https://doi.org/10.6028/NIST.AI.100-1), [Amazon Bedrock knowledge-base logging](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-bases-logging.html), [Microsoft Copilot Studio security and governance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance)).
5. [inference][medium] Comparator regulators imply that authoritative knowledge assets should fall inside operational-risk and model-governance expectations, because APRA demands monitored critical operations and service providers while the EBA demands deeper validation for complex or frequently updated models ([APRA CPS 230](https://handbook.apra.gov.au/standard/cps-230), [EBA ML for IRB models](https://www.eba.europa.eu/sites/default/files/document_library/Publications/Reports/2023/1061483/Follow-up%20report%20on%20machine%20learning%20for%20IRB%20models.pdf), [FSB AI in finance](https://www.fsb.org/2024/11/the-financial-stability-implications-of-artificial-intelligence/)).
6. [fact][high] The United Kingdom supervisory stance remains principles-based rather than AI-specific, which means firms are expected to translate existing governance, accountability, and operational-resilience regimes into concrete AI controls before dedicated rulebooks appear ([FCA FS23/6](https://www.fca.org.uk/publications/feedback-statements/fs23-6-artifical-intelligence-machine-learning), [Bank of England DP5/22 and FS2/23](https://www.bankofengland.co.uk/prudential-regulation/publication/2022/october/artificial-intelligence), [RBNZ AI supervisory expectations](https://davidamitchell.github.io/Research/research/2026-02-28-rbnz-ai-supervisory-expectations.html)).
7. [fact][high] Practitioner platforms already support citations, update workflows, publishing controls, audit logs, and ingestion telemetry, but none of them assigns business authority or resolves content disputes, so enterprise process design remains the decisive control layer ([Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html), [Amazon Bedrock knowledge-base logging](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-bases-logging.html), [Microsoft Copilot Studio security and governance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance)).
8. [inference][medium] The strategic bottleneck is capability design rather than tool selection, because the DORA report finds that AI returns depend more on foundational systems, culture, and communicated operating stance than on the tools themselves ([2025 DORA AI Capabilities Model report](https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report)).

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Hybrid governance outperforms pure centralisation or pure federation for regulated knowledge because it balances common controls with domain freshness. | [NIST AI RMF 1.0](https://doi.org/10.6028/NIST.AI.100-1); [ISO/IEC 42001](https://www.iso.org/standard/81230.html); [2025 DORA AI Capabilities Model report](https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report) | high | Cross-source synthesis. |
| [fact] The curation lifecycle must include intake, validation, publication, use with citation, correction, and retirement or recertification. | [KCS methodology](https://www.serviceinnovation.org/kcs/); [Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html); [Microsoft Copilot Studio security and governance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance) | high | Social method plus platform hooks. |
| [inference] Correction must flow back to source-of-truth and then forward through re-ingestion. | [KCS methodology](https://www.serviceinnovation.org/kcs/); [Amazon Bedrock knowledge-base logging](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-bases-logging.html); [Agent memory management and context injection](https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html) | high | Strong inference from propagation evidence. |
| [fact] Version lineage and auditability need explicit metadata plus event logs. | [NIST AI RMF 1.0](https://doi.org/10.6028/NIST.AI.100-1); [Amazon Bedrock knowledge-base logging](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-bases-logging.html); [Microsoft Copilot Studio security and governance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance) | high | Direct source support. |
| [inference] Regulator expectations imply that authoritative knowledge belongs inside operational-risk and model-governance controls. | [APRA CPS 230](https://handbook.apra.gov.au/standard/cps-230); [EBA ML for IRB models](https://www.eba.europa.eu/sites/default/files/document_library/Publications/Reports/2023/1061483/Follow-up%20report%20on%20machine%20learning%20for%20IRB%20models.pdf); [FSB AI in finance](https://www.fsb.org/2024/11/the-financial-stability-implications-of-artificial-intelligence/) | medium | Technology-neutral wording requires interpretation. |
| [fact] The UK approach remains principles-based and does not yet create AI-specific policy proposals in these statements. | [FCA FS23/6](https://www.fca.org.uk/publications/feedback-statements/fs23-6-artifical-intelligence-machine-learning); [Bank of England DP5/22 and FS2/23](https://www.bankofengland.co.uk/prudential-regulation/publication/2022/october/artificial-intelligence); [RBNZ AI supervisory expectations](https://davidamitchell.github.io/Research/research/2026-02-28-rbnz-ai-supervisory-expectations.html) | high | Official pages are explicit on summary intent. |
| [fact] Platforms expose governance mechanics, but enterprise process design still decides authority. | [Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html); [Amazon Bedrock knowledge-base logging](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-bases-logging.html); [Microsoft Copilot Studio security and governance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance) | high | Strong direct support. |
| [inference] Capability maturity, not tool choice alone, drives scaled AI performance. | [2025 DORA AI Capabilities Model report](https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report) | medium | Supported by one strong practitioner source. |

### Assumptions

- None.

### Analysis

[inference] The evidence was weighted toward official standards, regulator publications, and platform documentation, with prior completed items used only where they already synthesised those primary sources or filled jurisdictional context gaps ([NIST AI RMF 1.0](https://doi.org/10.6028/NIST.AI.100-1), [APRA CPS 230](https://handbook.apra.gov.au/standard/cps-230), [RBNZ AI supervisory expectations](https://davidamitchell.github.io/Research/research/2026-02-28-rbnz-ai-supervisory-expectations.html)). [inference] The main trade-off is between central control and domain freshness, and the hybrid model resolves it better than either extreme because central teams standardise metadata, evidence, and audit while domain stewards keep content authoritative and current ([2025 DORA AI Capabilities Model report](https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report), [KCS methodology](https://www.serviceinnovation.org/kcs/)). [inference] Competing interpretations of explainability were resolved by treating explainability as an operational evidence package, not as a requirement for every component to be simple, because the regulator and standards sources consistently emphasise accountability, documentation, validation, and monitoring rather than a single interpretability technique ([NIST AI RMF 1.0](https://doi.org/10.6028/NIST.AI.100-1), [EBA ML for IRB models](https://www.eba.europa.eu/sites/default/files/document_library/Publications/Reports/2023/1061483/Follow-up%20report%20on%20machine%20learning%20for%20IRB%20models.pdf), [FSB AI in finance](https://www.fsb.org/2024/11/the-financial-stability-implications-of-artificial-intelligence/)).

### Risks, Gaps, and Uncertainties

- [fact] The original Microsoft knowledge-base-management source was unavailable, so Microsoft evidence in this item is stronger on security, audit, and publishing controls than on detailed lifecycle guidance ([Microsoft Copilot Studio security and governance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance)).
- [fact] ISO/IEC 42001 clause-level detail could not be validated from public text because the standard is paywalled, so it supports direction of travel rather than clause-specific design choices ([ISO/IEC 42001](https://www.iso.org/standard/81230.html)).
- [inference] Public supervisory material is rich on principles and thin on corpus-specific examples, so some elements of the final control model are necessarily synthesis rather than direct quotation from a regulator ([APRA CPS 230](https://handbook.apra.gov.au/standard/cps-230), [FCA FS23/6](https://www.fca.org.uk/publications/feedback-statements/fs23-6-artifical-intelligence-machine-learning)).

### Open Questions

- What evidence package would satisfy an external auditor who needs to replay exactly which knowledge version informed a customer-impacting AI answer?
- How should regulated firms govern conflicts between enterprise policy libraries and fast-changing procedural content inside line-of-business platforms?
- When should a corrected knowledge item trigger mandatory downstream revalidation of prompts, retrieval settings, or agent instructions, rather than simple re-ingestion?

---

## Output

- Type: knowledge
- Description: Control model and evidence-backed findings for governing authoritative knowledge as an enterprise AI capability in regulated financial institutions.
- Links:
  - [APRA CPS 230](https://handbook.apra.gov.au/standard/cps-230)
  - [NIST AI RMF 1.0](https://doi.org/10.6028/NIST.AI.100-1)
  - [KCS methodology](https://www.serviceinnovation.org/kcs/)
