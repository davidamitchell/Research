---
review_count: 1
title: "Why does Software Bill of Materials (SBOM) fail as a complete inventory model for agentic Artificial Intelligence (AI) workloads, and what new conceptual abstractions are required?"
added: 2026-05-06T08:52:41+00:00
status: reviewing
priority: high  # low | medium | high
blocks: [2026-05-06-aibom-schema-design-standards-alignment, 2026-05-06-aibom-runtime-generation-divergence-theory, 2026-05-06-aibom-declared-construction-practice]  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [agentic-ai, governance, llm, security, supply-chain, knowledge-graph, ai-governance]
started: 2026-05-06T10:35:10+00:00
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
cites: [2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain, 2026-05-06-aibom-runtime-generation-divergence-theory, 2026-05-06-aibom-identity-delegation-trust-theory]
related: [2026-04-26-permission-safe-rag-enterprise-information-architecture, 2026-04-26-ai-lowcode-observability-telemetry-governance, 2026-04-22-ai-governance-assurance-change-control-verification]
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# Why does Software Bill of Materials (SBOM) fail as a complete inventory model for agentic Artificial Intelligence (AI) workloads, and what new conceptual abstractions are required?

## Research Question

Why do traditional Software Bill of Materials (SBOM) concepts fail to adequately describe the dependency, provenance, and runtime composition of agentic Artificial Intelligence (AI) systems, and what fundamentally new abstractions, graph structures, mutable dependency types, and non-deterministic component representations, are required in an Artificial Intelligence Bill of Materials (AIBOM) to close those gaps?

## Scope

**In scope:**
- Analysis of what SBOM was designed to capture and where those assumptions break for agentic AI workloads
- Identification of component types unique to agentic AI: prompts, system instructions, Retrieval-Augmented Generation (RAG) indexes, memory schemas, tool permission scopes, model weights, and inference configurations
- Mutable versus immutable dependency distinctions, specifically how agentic AI introduces dependencies that change at runtime, such as RAG retrievals, memory state, and tool outputs, with no close analogue in traditional software supply chains
- Non-deterministic output as a supply-chain property, specifically stochastic model outputs that cannot be versioned like compiled binaries
- Graph-based representations, specifically whether a flat or package-style component inventory is adequate or whether agentic flows require directed graphs across agent, tool, retrieval, memory, and identity surfaces
- Review of existing academic and industry literature on AIBOM conceptual framing

**Out of scope:**
- Implementation of any AIBOM tooling
- Deep dive into specific platform capability comparisons
- Regulatory compliance obligations

**Constraints:**
- Focus on conceptual and theoretical analysis, using implementations only as illustrative examples
- Prefer primary sources: standards documents, official specification pages, and peer-reviewed or formal research
- Expand every acronym on first use in the document body

## Context

- [fact; source: https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom] The National Telecommunications and Information Administration (NTIA) defines an SBOM as a formal record of component details and supply-chain relationships used in building software.
- [fact; source: https://cyclonedx.org/capabilities/mlbom/; https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/; https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Classes/DatasetPackage/] CycloneDX and SPDX have already widened bill-of-materials coverage to models, datasets, hyperparameters, preprocessing, explainability, and compliance metadata, which means the active design question is no longer whether AI-specific fields are needed.
- [inference; source: https://arxiv.org/abs/2504.16743; https://www.w3.org/TR/prov-overview/; https://arxiv.org/abs/2508.02866] The unresolved problem is whether a package-style inventory model can represent agentic systems whose effective dependencies, prompts, retrieved context, decisions, and authority paths are only fully known during execution.

## Approach

1. **SBOM foundational assumptions audit:** identify what SBOM and current AI-BOM extensions formally model, and where those models remain package-centric.
2. **Agentic AI component taxonomy:** enumerate component classes that materially shape agentic behaviour, including prompts, retrieval corpora, memory, tools, and delegated authority.
3. **Failure-mode analysis:** map each agentic component class to the specific SBOM assumption it breaks and the governance consequence of that mismatch.
4. **Graph adequacy assessment:** test whether package-style inventory plus relationships is sufficient, or whether a provenance-oriented graph is the necessary abstraction.
5. **AIBOM abstraction synthesis:** derive the minimum new node, edge, property, and temporal abstractions needed for a conceptually complete AIBOM.

## Sources

- [x] [National Telecommunications and Information Administration (2021) The Minimum Elements for a Software Bill of Materials (SBOM)](https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom) - foundational SBOM definition and minimum-elements framing
- [x] [CycloneDX Machine Learning Bill of Materials (AI/ML-BOM)](https://cyclonedx.org/capabilities/mlbom/) - official CycloneDX description of AI and machine-learning bill-of-materials coverage
- [x] [SPDX Specification 3.0.1 AIPackage](https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/) - official SPDX class for Artificial Intelligence packages and trained models
- [x] [SPDX Specification 3.0.1 DatasetPackage](https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Classes/DatasetPackage/) - official SPDX class for datasets used in software or to train and test AI packages
- [x] [OWASP AIBOM](https://owaspaibom.org/) - OWASP initiative describing AIBOM as an auditability and traceability layer for AI systems
- [x] [GenAI Security Project AIBOM Generator](https://github.com/GenAI-Security-Project/aibom-generator) - official repository showing current AIBOM tooling scope, output format, and standards alignment
- [x] [Suriyawongkul et al. (2025) Implementing AI Bill of Materials (AI BOM) with SPDX 3.0](https://arxiv.org/abs/2504.16743) - academic report arguing that AI projects require a broader bill of materials than software alone
- [x] [Bommasani et al. (2021) On the Opportunities and Risks of Foundation Models](https://arxiv.org/abs/2108.07258) - foundation-model properties, downstream inheritance, and emergent capability framing
- [x] [National Institute of Standards and Technology (NIST) AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - official lifecycle and trustworthiness framing for Artificial Intelligence systems
- [x] [World Wide Web Consortium (W3C) PROV Overview](https://www.w3.org/TR/prov-overview/) - provenance model for entities, activities, agents, derivation, reproducibility, and versioning
- [x] [Souza et al. (2025) PROV-AGENT: Unified Provenance for Tracking AI Agent Interactions in Agentic Workflows](https://arxiv.org/abs/2508.02866) - provenance model for prompts, responses, decisions, and workflow context in agentic systems
- [x] [David Mitchell (2026) AI security threat model for prompt injection, Retrieval-Augmented Generation (RAG), supply chain, and exfiltration](https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html) - prior repository item on structural retrieval and tool-path risk
- [x] [David Mitchell (2026) Runtime-observed AIBOM and declared-versus-observed divergence theory](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html) - adjacent repository item on runtime provenance and divergence
- [x] [David Mitchell (2026) AIBOM identity, delegation, and trust theory](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html) - adjacent repository item on authority, delegation, and permission objects

## Related

- [How can a runtime-observed Artificial Intelligence Bill of Materials (AIBOM) be generated for an agentic Artificial Intelligence (AI) system, and how much does it diverge from the declared design-time AIBOM?](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html)
- [How should identity, delegation chains, and permission scopes be formally modelled in an Artificial Intelligence Bill of Materials (AIBOM) schema to enable end-to-end attribution across agentic Artificial Intelligence (AI) systems?](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html)
- [What security capabilities are required in an enterprise Artificial Intelligence (AI) system to address prompt injection, Retrieval-Augmented Generation (RAG)-based attacks, model supply chain compromise, and data exfiltration beyond basic Application Programming Interface (API) access controls and audit logging?](https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0 to 5 are the investigation, and Section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: Why does SBOM stop short of being a complete inventory model for agentic AI systems, and which new abstractions does AIBOM need to represent mutable context, provenance, graph structure, and non-deterministic execution?
- Scope: SBOM assumptions, agentic component taxonomy, failure modes, graph adequacy, and required AIBOM abstractions.
- Constraints: Stay conceptual, prioritize primary sources, and distinguish declared package metadata from runtime-observed execution state.
- Output: knowledge.
- Prior completed items reviewed: https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html ; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html

### §1 Question Decomposition

- **Root question:** Why is a traditional software bill of materials incomplete for agentic AI, and what must replace or extend its core abstractions?
  - **A. SBOM baseline**
    - A1. What does SBOM formally describe in NTIA and current standards practice?
    - A2. How do CycloneDX and SPDX extend that baseline for AI components?
  - **B. AI-specific pressure on the model**
    - B1. Which AI properties already exceed software-only inventory semantics?
    - B2. Which agentic properties exceed even current AI package metadata?
  - **C. Failure modes**
    - C1. Which agentic component classes are mutable, semantically active, or runtime-discovered?
    - C2. Which governance or security blind spots follow when those classes are absent from the inventory model?
  - **D. Representation**
    - D1. Is package metadata plus component relationships enough?
    - D2. When is a provenance-oriented graph the necessary abstraction?
  - **E. New abstractions**
    - E1. Which new node and edge types are required?
    - E2. Which new properties, especially mutability, determinism, authority, and temporality, are required?
    - E3. Should declared design-time and runtime-observed AIBOMs be distinct but linked artifacts?

### §2 Investigation

#### Source substitutions and failed-search notes

- Search note: query `"Toward a Framework for Agentic AI Provenance"` -> seeded URL `https://arxiv.org/abs/2407.01392` resolved to unrelated paper title `Diffusion Forcing`; no matching primary source found in this session.
- Source substitution: seeded OWASP project URL returned `404`; replaced with `https://owaspaibom.org/` and the official generator repository at `https://github.com/GenAI-Security-Project/aibom-generator`.
- Source substitution: seeded NIST PDF URL returned `404`; replaced with the official framework landing page at `https://www.nist.gov/itl/ai-risk-management-framework`.

#### A. What SBOM and current AI-BOM standards formally model

- [fact; source: https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom] NTIA defines an SBOM as a formal record containing component details and supply-chain relationships for software.
- [fact; source: https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/] SPDX 3.0.1 defines `AIPackage` as metadata added to a package to describe an AI application or trained AI model, and the class remains a subclass of `/Software/Package`.
- [fact; source: https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/] SPDX `AIPackage` adds AI-specific fields such as autonomy type, hyperparameters, training information, model explainability, metric thresholds, standard compliance, and type of model, while still requiring package-style properties such as version, supplier, release time, and download location.
- [fact; source: https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Classes/DatasetPackage/] SPDX 3.0.1 defines `DatasetPackage` as metadata added to a dataset used in software or to train or test an AI package, with fields for collection process, preprocessing, update mechanism, known bias, confidentiality, and sensitive personal information.
- [fact; source: https://cyclonedx.org/capabilities/mlbom/] CycloneDX's AI and machine-learning bill-of-materials capability states that it represents datasets, models, configurations, dataset provenance, and training methodologies so organizations can assess bias, data integrity, model security, and related risks.
- [inference; source: https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom; https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/; https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Classes/DatasetPackage/; https://cyclonedx.org/capabilities/mlbom/] The common design center across NTIA SBOM, SPDX AI classes, and CycloneDX AI and machine-learning bill-of-materials is still declared artifact metadata, specifically package-like objects with associated properties, rather than execution-specific state or causal run history.

#### B. Why AI already stretches software-only inventory semantics

- [fact; source: https://arxiv.org/abs/2504.16743] Suriyawongkul et al. state that AI projects face unique challenges beyond software security and therefore require a broader bill of materials covering algorithms, data-collection methods, frameworks and libraries, licensing information, and standards compliance.
- [fact; source: https://arxiv.org/abs/2108.07258] Bommasani et al. argue that foundation models create emergent capabilities, incentivize homogenization, and cause defects in the base model to be inherited by downstream adapted models.
- [fact; source: https://www.nist.gov/itl/ai-risk-management-framework] The National Institute of Standards and Technology (NIST) frames AI risk management as incorporation of trustworthiness considerations into the design, development, use, and evaluation of AI products, services, and systems.
- [inference; source: https://arxiv.org/abs/2504.16743; https://arxiv.org/abs/2108.07258; https://www.nist.gov/itl/ai-risk-management-framework] Even before agentic orchestration is introduced, AI systems push beyond software-only inventory semantics because model lineage, training data, evaluation context, inherited downstream behavior, and lifecycle governance all materially affect system risk.

#### C. What agentic AI adds beyond current AI package metadata

- [fact; source: https://owaspaibom.org/] OWASP describes AIBOM as visibility into datasets, methodologies, and training processes so that AI systems become auditable, traceable, and trustworthy.
- [fact; source: https://github.com/GenAI-Security-Project/aibom-generator] The official OWASP AIBOM Generator currently extracts metadata from models hosted on Hugging Face and generates CycloneDX 1.6 JSON output compatible with the SPDX AI Profile.
- [fact; source: https://arxiv.org/abs/2508.02866] Souza et al. introduce PROV-AGENT, Unified Provenance for Tracking AI Agent Interactions in Agentic Workflows, and state that existing provenance methods fail to capture and relate prompts, responses, and decisions with the broader workflow context and downstream outcomes in agentic workflows.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html] The completed repository threat-model item found that retrieved documents and tool paths create structural prompt, retrieval, and execution risks because untrusted content can alter what the model does once it enters context.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html] The completed repository identity item found that delegated authority, trust-domain crossings, and edge-bound permission manifests have to be represented explicitly for end-to-end attribution.
- [inference; source: https://arxiv.org/abs/2508.02866; https://github.com/GenAI-Security-Project/aibom-generator; https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html] Agentic AI adds semantically active and runtime-discovered dependencies, specifically prompts, system instructions, retrieved context, tool arguments and outputs, memory state, delegated authority, and external observations, that current package-centered AI-BOM tools only partially cover.

#### D. Why a provenance-oriented graph is the necessary abstraction

- [fact; source: https://www.w3.org/TR/prov-overview/] World Wide Web Consortium (W3C) PROV defines provenance as information about entities, activities, and people involved in producing a thing, and it explicitly includes identifying objects, attributing them, representing processing steps, reproducibility, versioning, and derivation.
- [fact; source: https://arxiv.org/abs/2508.02866] PROV-AGENT extends World Wide Web Consortium (W3C) PROV for agentic workflows and argues that prompts, responses, and decisions must be integrated into end-to-end workflow provenance to answer transparency and reliability questions.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html] The completed runtime-divergence item concluded that a runtime AIBOM is best modelled as a causality graph plus state snapshots, because declared structure and realized execution diverge across retrieval, memory, authority, topology, and control-policy surfaces.
- [inference; source: https://www.w3.org/TR/prov-overview/; https://arxiv.org/abs/2508.02866; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html] Package metadata plus ordinary component relationships is insufficient for agentic AI because the main governance questions are causal and temporal, specifically which prompt, retrieval result, memory state, actor, and tool invocation jointly produced a decision or action.
- [inference; source: https://www.w3.org/TR/prov-overview/; https://arxiv.org/abs/2508.02866; https://www.nist.gov/itl/ai-risk-management-framework] A complete AIBOM therefore needs graph semantics for entities, activities, and actors, plus linkage between declared design intent and runtime-observed provenance, rather than one static list of parts.

#### E. New conceptual abstractions required in a complete AIBOM

- [inference; source: https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/; https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Classes/DatasetPackage/; https://arxiv.org/abs/2508.02866; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html] A complete AIBOM needs more node types than software packages, at minimum software artifact, model artifact, dataset or retrieval corpus, prompt or instruction artifact, orchestration or policy object, tool or external service, memory object, runtime event, and identity or authority object.
- [inference; source: https://www.w3.org/TR/prov-overview/; https://arxiv.org/abs/2508.02866; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html] A complete AIBOM also needs typed relationships such as `trained_on`, `configured_by`, `prompted_by`, `retrieved_from`, `invoked`, `delegated_to`, `derived_from`, and `observed_in_run`, because dependency alone does not distinguish semantic control, information flow, or authority transfer.
- [inference; source: https://arxiv.org/abs/2108.07258; https://www.nist.gov/itl/ai-risk-management-framework; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html] Required property classes include mutability, determinism, evaluation or approval status, trust domain, data sensitivity, effective permission scope, and runtime variability envelope, because static version identifiers do not capture stochastic outputs or context-dependent behavior.
- [inference; source: https://www.w3.org/TR/prov-overview/; https://arxiv.org/abs/2508.02866; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html] The final conceptual move is to separate the declared design-time AIBOM from runtime-observed AIBOM instances, then link them through stable identifiers and provenance edges so auditors can compare approved structure against realized execution.

### §3 Reasoning

- [fact; source: https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom; https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/; https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Classes/DatasetPackage/; https://cyclonedx.org/capabilities/mlbom/] The reviewed standards directly support the claim that current SBOM and AI-BOM practice is centered on declared artifacts and their metadata.
- [fact; source: https://arxiv.org/abs/2504.16743; https://arxiv.org/abs/2108.07258; https://www.nist.gov/itl/ai-risk-management-framework] The reviewed research directly supports the claim that AI systems introduce risk-relevant properties beyond ordinary software packages, especially data lineage, inherited model defects, and lifecycle-specific trustworthiness concerns.
- [fact; source: https://arxiv.org/abs/2508.02866; https://www.w3.org/TR/prov-overview/] The provenance literature directly supports the claim that entities, activities, actors, derivations, and processing steps are the right primitives for reconstructing how an output or action came to exist.
- [inference; source: https://github.com/GenAI-Security-Project/aibom-generator; https://arxiv.org/abs/2508.02866; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html] The gap between current AIBOM tooling and a complete agentic AIBOM is therefore not just missing fields, but a missing ontological layer for runtime context, causality, and authority.
- [assumption; source: https://arxiv.org/abs/2508.02866; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html] A future AIBOM implementation will be able to bind declared identifiers to runtime provenance strongly enough to compare design intent with execution history, even though no universal identifier scheme was found in the reviewed sources.

### §4 Consistency Check

- [fact; source: https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom] SBOM is not purely a flat list, because NTIA explicitly includes supply-chain relationships, so the argument here is narrowed to package-centered inventory semantics rather than claiming SBOM has no relationship model.
- [fact; source: https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/; https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Classes/DatasetPackage/] SPDX AI support does not eliminate the argument, because the reviewed AI classes still inherit software-package structure even while adding richer AI metadata.
- [inference; source: https://www.w3.org/TR/prov-overview/; https://arxiv.org/abs/2508.02866] The graph claim remains supported after that narrowing, because provenance graphs answer causal and temporal questions that package subclassing does not answer.
- [inference; source: https://arxiv.org/abs/2504.16743; https://github.com/GenAI-Security-Project/aibom-generator] The reviewed evidence supports retaining SBOM as one sublayer inside AIBOM rather than treating AIBOM as a total replacement for software component inventory.

### §5 Depth and Breadth Expansion

- [inference; source: https://www.w3.org/TR/prov-overview/; https://arxiv.org/abs/2508.02866] **Technical lens:** the decisive abstraction shift is from package declaration to provenance graph, because agentic correctness and auditability depend on reconstructing causal paths across prompts, retrieval, tools, and actors.
- [inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://owaspaibom.org/] **Regulatory and governance lens:** lifecycle trustworthiness and auditability pressures make runtime linkage important, because design-time inventory alone cannot explain what the system actually did.
- [inference; source: https://github.com/GenAI-Security-Project/aibom-generator; https://cyclonedx.org/capabilities/mlbom/] **Economic and implementation lens:** current tooling will likely evolve incrementally from model-centric metadata extraction toward richer graph and runtime capture, because ecosystem momentum is already behind CycloneDX and SPDX-compatible formats.
- [inference; source: https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom; https://arxiv.org/abs/2504.16743] **Historical lens:** AIBOM appears to follow the same pattern as SBOM's early development, starting from component transparency and then expanding once new risk surfaces become operationally material.
- [inference; source: https://arxiv.org/abs/2108.07258; https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html] **Behavioural lens:** prompts, retrieved context, and tool authority matter because human reviewers and downstream systems often treat model outputs as grounded, which means missing provenance around those inputs creates avoidable trust errors.

### §6 Synthesis

**Executive summary:**

- Traditional SBOM is not a complete inventory model for agentic AI because it is optimized for declared software artifacts and component relationships, while agentic execution depends materially on mutable context, delegated authority, and stochastic model behavior that appear only during runtime. [inference; source: https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom; https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/; https://arxiv.org/abs/2508.02866; https://arxiv.org/abs/2108.07258]
- Current AI-oriented extensions such as CycloneDX AI and machine-learning bill-of-materials, SPDX `AIPackage` and `DatasetPackage`, and the OWASP AIBOM Generator widen coverage to models, datasets, hyperparameters, and training metadata, but they still inherit package-style inventory semantics rather than full execution-provenance semantics. [inference; source: https://cyclonedx.org/capabilities/mlbom/; https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/; https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Classes/DatasetPackage/; https://github.com/GenAI-Security-Project/aibom-generator]
- A complete AIBOM therefore needs a typed graph model that links software artifacts, models, datasets, prompts, retrieval corpora, tools, memory state, and identity or permission objects through explicit derivation, invocation, delegation, and retrieval edges, then pairs that declared graph with runtime-observed provenance. [inference; source: https://www.w3.org/TR/prov-overview/; https://arxiv.org/abs/2508.02866; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html]
- The decisive conceptual shift is from a bill of packaged parts to a bill of governed capability plus realized execution path, because only that combined abstraction can explain what the system was allowed to do, what context it actually used, and why a given output or action occurred. [inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://www.w3.org/TR/prov-overview/; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html]

**Key findings:**

1. **NTIA SBOM and the reviewed SPDX AI extensions remain package-centered inventory models, because even the AI-specific classes are defined as metadata added to software-package objects rather than as first-class runtime activities or provenance graphs.** ([inference]; high confidence; source: https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom; https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/; https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Classes/DatasetPackage/)
2. **CycloneDX AI and machine-learning bill-of-materials, SPDX AI classes, and the OWASP AIBOM Generator materially extend software transparency to models, datasets, hyperparameters, preprocessing, and training metadata, but they still do not by themselves represent prompts, decisions, retrieval results, or executed authority paths as the core inventory object.** ([inference]; high confidence; source: https://cyclonedx.org/capabilities/mlbom/; https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/; https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Classes/DatasetPackage/; https://github.com/GenAI-Security-Project/aibom-generator)
3. **Agentic AI introduces semantically active and mutable dependencies, including prompts, system instructions, retrieved context, tool outputs, memory state, and delegated permission scope, that are governance-relevant even when they are not versioned artifacts in the traditional software sense.** ([inference]; medium confidence; source: https://arxiv.org/abs/2508.02866; https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html)
4. **Foundation-model inheritance, lifecycle trustworthiness requirements, and context-dependent execution mean that a static package inventory cannot fully explain AI system behavior, because risk also depends on model lineage, data provenance, evaluation context, and downstream runtime conditions.** ([inference]; medium confidence; source: https://arxiv.org/abs/2504.16743; https://arxiv.org/abs/2108.07258; https://www.nist.gov/itl/ai-risk-management-framework)
5. **A provenance-oriented graph is the necessary core abstraction for complete agentic AIBOMs, because the central audit questions concern entities, activities, actors, derivations, and causal processing steps rather than package membership alone.** ([inference]; medium confidence; source: https://www.w3.org/TR/prov-overview/; https://arxiv.org/abs/2508.02866)
6. **A conceptually complete AIBOM needs new node types, relationship types, and property classes, specifically runtime events, prompt artifacts, memory objects, authority objects, retrieval edges, delegation edges, mutability labels, determinism labels, trust domains, and variability envelopes, because package version identifiers cannot represent those semantics.** ([inference]; medium confidence; source: https://www.w3.org/TR/prov-overview/; https://arxiv.org/abs/2508.02866; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html)
7. **The strongest design pattern is therefore a layered model in which classical SBOM remains one sublayer for software artifacts, the declared AIBOM captures approved graph structure and semantics, and runtime-observed AIBOM instances capture what actually executed in a specific run.** ([inference]; medium confidence; source: https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom; https://arxiv.org/abs/2504.16743; https://www.w3.org/TR/prov-overview/; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] NTIA SBOM and SPDX AI classes remain package-centered inventory models. | https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom ; https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/ ; https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Classes/DatasetPackage/ | high | AI classes still inherit software-package structure |
| [inference] Current AI-BOM extensions widen metadata scope but do not yet make runtime execution the core inventory object. | https://cyclonedx.org/capabilities/mlbom/ ; https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/ ; https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Classes/DatasetPackage/ ; https://github.com/GenAI-Security-Project/aibom-generator | high | Richer metadata, still repository or package oriented |
| [inference] Agentic AI adds mutable and semantically active dependencies that ordinary artifact inventory does not capture well. | https://arxiv.org/abs/2508.02866 ; https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html | medium | Prompts, retrieval, tools, memory, and authority are runtime-shaping objects |
| [inference] Static package inventory cannot fully explain AI behavior because lifecycle, lineage, and context also matter. | https://arxiv.org/abs/2504.16743 ; https://arxiv.org/abs/2108.07258 ; https://www.nist.gov/itl/ai-risk-management-framework | medium | AI risk exceeds software dependency inventory |
| [inference] Provenance-oriented graphs are the necessary abstraction for complete agentic AIBOMs. | https://www.w3.org/TR/prov-overview/ ; https://arxiv.org/abs/2508.02866 | medium | Graphs answer causal, temporal, and attribution questions |
| [inference] Complete AIBOMs require new node, edge, and property classes for runtime semantics. | https://www.w3.org/TR/prov-overview/ ; https://arxiv.org/abs/2508.02866 ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html | medium | Schema shape is synthetic rather than standardized |
| [inference] The best architecture is a layered model of SBOM sublayer, declared AIBOM, and runtime-observed AIBOM instances. | https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom ; https://arxiv.org/abs/2504.16743 ; https://www.w3.org/TR/prov-overview/ ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html | medium | Preserves software inventory while adding execution truth |

**Assumptions:**

- [assumption; source: https://arxiv.org/abs/2508.02866; https://owaspaibom.org/; https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html] Prompts, system instructions, memory state, and delegated permission objects should be treated as inventory-relevant components even when current BOM standards do not yet define canonical classes for all of them.
- [assumption; source: https://www.w3.org/TR/prov-overview/; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html] Declared AIBOM identifiers can be linked to runtime provenance strongly enough to support approved-versus-executed comparison in practice, even though no reviewed universal identifier scheme covers every agentic surface.

**Analysis:**

- The strongest rival interpretation is that AIBOM only needs more fields inside existing SPDX and CycloneDX objects. The evidence rejects that narrow view, because the reviewed AI classes and current OWASP generator still model the core unit as a package or repository artifact, while the provenance sources show that agentic audit questions are about events, decisions, and actors. [inference; source: https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/; https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Classes/DatasetPackage/; https://github.com/GenAI-Security-Project/aibom-generator; https://arxiv.org/abs/2508.02866]
- The second rival interpretation is that static AIBOM plus generic logs is sufficient. That view was rejected because W3C PROV and PROV-AGENT both center explicit causal relationships among entities, activities, and actors, and the adjacent runtime-divergence item shows that retrieval, memory, authority, and topology diverge across runs in ways that simple logging does not normalize into one auditable object. [inference; source: https://www.w3.org/TR/prov-overview/; https://arxiv.org/abs/2508.02866; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html]
- The correct synthesis is therefore additive rather than replacement-oriented. Classical SBOM remains useful for software libraries, frameworks, and conventional dependencies inside an AI system, but it becomes only one layer inside a broader AIBOM whose central object is governed capability plus realized execution path. [inference; source: https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom; https://arxiv.org/abs/2504.16743; https://www.w3.org/TR/prov-overview/]

**Risks, gaps, uncertainties:**

- [inference; source: https://github.com/GenAI-Security-Project/aibom-generator; https://owaspaibom.org/; https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/] No reviewed standard or tool yet provides a canonical agentic AIBOM schema covering prompts, tools, memory, delegated authority, and runtime state in one stable specification.
- [inference; source: https://arxiv.org/abs/2508.02866; https://www.w3.org/TR/prov-overview/] Dedicated academic literature on agentic provenance is still thin relative to the maturity of software-provenance standards, so the graph recommendation relies on one recent agentic paper plus broader provenance standards.
- [inference; source: https://arxiv.org/abs/2108.07258; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html] The conceptual treatment of non-determinism is still incomplete, especially around how to version prompt semantics, preserve enough runtime context for audit, and express acceptable variance across repeated runs.

**Open questions:**

- How should prompts and system instructions be versioned so that semantic changes, not only text edits, become auditable?
- What minimum runtime snapshot is sufficient for retrieval results, memory state, and tool outputs without over-collecting sensitive data?
- Should stochastic behavior in AIBOM be represented as a variability envelope, a replay record, or a policy-bound set of acceptable outcomes?

### §7 Recursive Review

- Metadata: Prior-work sweep completed across adjacent completed items on prompt and retrieval security, runtime divergence, identity and delegation, observability, and permission-safe retrieval.
- Metadata: Acronym audit completed for Software Bill of Materials (SBOM), Artificial Intelligence (AI), Artificial Intelligence Bill of Materials (AIBOM), Retrieval-Augmented Generation (RAG), National Telecommunications and Information Administration (NTIA), National Institute of Standards and Technology (NIST), and World Wide Web Consortium (W3C) PROV.
- Metadata: Findings and Section 6 contain the same substantive claims, confidence levels, and source sets.
- Metadata: Remaining uncertainty is concentrated in schema standardization, runtime identifier binding, and non-determinism representation rather than in the core conclusion that package-centered SBOM semantics are incomplete for agentic AI.

---

## Findings

### Executive Summary

Traditional Software Bill of Materials (SBOM) is not a complete inventory model for agentic Artificial Intelligence (AI) because it is optimized for declared software artifacts and component relationships, while agentic execution depends materially on mutable context, delegated authority, and stochastic model behavior that appear only during runtime. [inference; source: https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom; https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/; https://arxiv.org/abs/2508.02866; https://arxiv.org/abs/2108.07258]

Current AI-oriented extensions such as CycloneDX AI and machine-learning bill-of-materials, SPDX `AIPackage` and `DatasetPackage`, and the OWASP AIBOM Generator widen coverage to models, datasets, hyperparameters, and training metadata, but they still inherit package-style inventory semantics rather than full execution-provenance semantics. [inference; source: https://cyclonedx.org/capabilities/mlbom/; https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/; https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Classes/DatasetPackage/; https://github.com/GenAI-Security-Project/aibom-generator]

A complete AIBOM therefore needs a typed graph model that links software artifacts, models, datasets, prompts, retrieval corpora, tools, memory state, and identity or permission objects through explicit derivation, invocation, delegation, and retrieval edges, then pairs that declared graph with runtime-observed provenance. [inference; source: https://www.w3.org/TR/prov-overview/; https://arxiv.org/abs/2508.02866; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html]

The decisive conceptual shift is from a bill of packaged parts to a bill of governed capability plus realized execution path, because only that combined abstraction can explain what the system was allowed to do, what context it actually used, and why a given output or action occurred. [inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://www.w3.org/TR/prov-overview/; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html]

### Key Findings

1. **NTIA SBOM and the reviewed SPDX AI extensions remain package-centered inventory models, because even the AI-specific classes are defined as metadata added to software-package objects rather than as first-class runtime activities or provenance graphs.** ([inference]; high confidence; source: https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom; https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/; https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Classes/DatasetPackage/)
2. **CycloneDX AI and machine-learning bill-of-materials, SPDX AI classes, and the OWASP AIBOM Generator materially extend software transparency to models, datasets, hyperparameters, preprocessing, and training metadata, but they still do not by themselves represent prompts, decisions, retrieval results, or executed authority paths as the core inventory object.** ([inference]; high confidence; source: https://cyclonedx.org/capabilities/mlbom/; https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/; https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Classes/DatasetPackage/; https://github.com/GenAI-Security-Project/aibom-generator)
3. **Agentic AI introduces semantically active and mutable dependencies, including prompts, system instructions, retrieved context, tool outputs, memory state, and delegated permission scope, that are governance-relevant even when they are not versioned artifacts in the traditional software sense.** ([inference]; medium confidence; source: https://arxiv.org/abs/2508.02866; https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html)
4. **Foundation-model inheritance, lifecycle trustworthiness requirements, and context-dependent execution mean that a static package inventory cannot fully explain AI system behavior, because risk also depends on model lineage, data provenance, evaluation context, and downstream runtime conditions.** ([inference]; medium confidence; source: https://arxiv.org/abs/2504.16743; https://arxiv.org/abs/2108.07258; https://www.nist.gov/itl/ai-risk-management-framework)
5. **A provenance-oriented graph is the necessary core abstraction for complete agentic AIBOMs, because the central audit questions concern entities, activities, actors, derivations, and causal processing steps rather than package membership alone.** ([inference]; medium confidence; source: https://www.w3.org/TR/prov-overview/; https://arxiv.org/abs/2508.02866)
6. **A conceptually complete AIBOM needs new node types, relationship types, and property classes, specifically runtime events, prompt artifacts, memory objects, authority objects, retrieval edges, delegation edges, mutability labels, determinism labels, trust domains, and variability envelopes, because package version identifiers cannot represent those semantics.** ([inference]; medium confidence; source: https://www.w3.org/TR/prov-overview/; https://arxiv.org/abs/2508.02866; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html)
7. **The strongest design pattern is therefore a layered model in which classical SBOM remains one sublayer for software artifacts, the declared AIBOM captures approved graph structure and semantics, and runtime-observed AIBOM instances capture what actually executed in a specific run.** ([inference]; medium confidence; source: https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom; https://arxiv.org/abs/2504.16743; https://www.w3.org/TR/prov-overview/; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] NTIA SBOM and SPDX AI classes remain package-centered inventory models. | https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom ; https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/ ; https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Classes/DatasetPackage/ | high | AI classes still inherit software-package structure |
| [inference] Current AI-BOM extensions widen metadata scope but do not yet make runtime execution the core inventory object. | https://cyclonedx.org/capabilities/mlbom/ ; https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/ ; https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Classes/DatasetPackage/ ; https://github.com/GenAI-Security-Project/aibom-generator | high | Richer metadata, still repository or package oriented |
| [inference] Agentic AI adds mutable and semantically active dependencies that ordinary artifact inventory does not capture well. | https://arxiv.org/abs/2508.02866 ; https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html | medium | Prompts, retrieval, tools, memory, and authority are runtime-shaping objects |
| [inference] Static package inventory cannot fully explain AI behavior because lifecycle, lineage, and context also matter. | https://arxiv.org/abs/2504.16743 ; https://arxiv.org/abs/2108.07258 ; https://www.nist.gov/itl/ai-risk-management-framework | medium | AI risk exceeds software dependency inventory |
| [inference] Provenance-oriented graphs are the necessary abstraction for complete agentic AIBOMs. | https://www.w3.org/TR/prov-overview/ ; https://arxiv.org/abs/2508.02866 | medium | Graphs answer causal, temporal, and attribution questions |
| [inference] Complete AIBOMs require new node, edge, and property classes for runtime semantics. | https://www.w3.org/TR/prov-overview/ ; https://arxiv.org/abs/2508.02866 ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html | medium | Schema shape is synthetic rather than standardized |
| [inference] The best architecture is a layered model of SBOM sublayer, declared AIBOM, and runtime-observed AIBOM instances. | https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom ; https://arxiv.org/abs/2504.16743 ; https://www.w3.org/TR/prov-overview/ ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html | medium | Preserves software inventory while adding execution truth |

### Assumptions

- **Assumption:** Prompts, system instructions, memory state, and delegated permission objects should be treated as inventory-relevant components even when current BOM standards do not yet define canonical classes for all of them. **Justification:** they materially affect agent behaviour, provenance, and auditability in agentic workflows. [assumption; source: https://arxiv.org/abs/2508.02866; https://owaspaibom.org/; https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html]
- **Assumption:** Declared AIBOM identifiers can be linked to runtime provenance strongly enough to support approved-versus-executed comparison in practice. **Justification:** that linkage is required for governance, but no reviewed universal identifier scheme covers every agentic surface. [assumption; source: https://www.w3.org/TR/prov-overview/; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html]

### Analysis

The strongest rival interpretation is that AIBOM only needs more fields inside existing SPDX and CycloneDX objects. The evidence rejects that narrow view, because the reviewed AI classes and current OWASP generator still model the core unit as a package or repository artifact, while the provenance sources show that agentic audit questions are about events, decisions, and actors. [inference; source: https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/; https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Classes/DatasetPackage/; https://github.com/GenAI-Security-Project/aibom-generator; https://arxiv.org/abs/2508.02866]

The second rival interpretation is that static AIBOM plus generic logs is sufficient. That view was rejected because W3C PROV and PROV-AGENT both center explicit causal relationships among entities, activities, and actors, and the adjacent runtime-divergence item shows that retrieval, memory, authority, and topology diverge across runs in ways that simple logging does not normalize into one auditable object. [inference; source: https://www.w3.org/TR/prov-overview/; https://arxiv.org/abs/2508.02866; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html]

The correct synthesis is therefore additive rather than replacement-oriented. Classical SBOM remains useful for software libraries, frameworks, and conventional dependencies inside an AI system, but it becomes only one layer inside a broader AIBOM whose central object is governed capability plus realized execution path. [inference; source: https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom; https://arxiv.org/abs/2504.16743; https://www.w3.org/TR/prov-overview/]

### Risks, Gaps, and Uncertainties

- A reviewed standard or toolset still does not provide a canonical agentic AIBOM schema covering prompts, tools, memory, delegated authority, and runtime state in one stable specification. [inference; source: https://github.com/GenAI-Security-Project/aibom-generator; https://owaspaibom.org/; https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/]
- Dedicated academic literature on agentic provenance is still thin relative to the maturity of software-provenance standards, so the graph recommendation relies on one recent agentic paper plus broader provenance standards. [inference; source: https://arxiv.org/abs/2508.02866; https://www.w3.org/TR/prov-overview/]
- The conceptual treatment of non-determinism is still incomplete, especially around how to version prompt semantics, preserve enough runtime context for audit, and express acceptable variance across repeated runs. [inference; source: https://arxiv.org/abs/2108.07258; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html]

### Open Questions

- How should prompts and system instructions be versioned so that semantic changes, not only text edits, become auditable?
- What minimum runtime snapshot is sufficient for retrieval results, memory state, and tool outputs without over-collecting sensitive data?
- Should stochastic behavior in AIBOM be represented as a variability envelope, a replay record, or a policy-bound set of acceptable outcomes?

---

## Output

- Type: knowledge
- Description: Traditional SBOM remains a useful software-component sublayer, but a complete AIBOM for agentic AI needs graph and runtime-provenance abstractions for mutable context, delegated authority, and non-deterministic execution. [inference; source: https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom; https://www.w3.org/TR/prov-overview/; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html]
- Links:
  - https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom
  - https://www.w3.org/TR/prov-overview/
  - https://arxiv.org/abs/2508.02866
