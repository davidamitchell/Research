---
title: "What is the minimal viable schema for an Artificial Intelligence Bill of Materials (AIBOM) for agentic workloads, how should it align with CycloneDX and Software Package Data Exchange (SPDX) standards, and what new property types are required?"
added: 2026-05-06T08:52:41+00:00
status: reviewing
priority: high  # low | medium | high
blocks: [2026-05-06-aibom-declared-construction-practice]  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [agentic-ai, security, supply-chain, governance, llm, ai-governance]
started: 2026-05-06T11:00:55+00:00
completed: ~
output: [knowledge]  # skill | tool | agent | knowledge | backlog-item
cites: [2026-05-06-aibom-sbom-conceptual-gaps-theory, 2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain, 2026-05-06-aibom-runtime-generation-divergence-theory, 2026-05-06-aibom-identity-delegation-trust-theory]
related: [2026-05-06-aibom-declared-construction-practice, 2026-05-06-aibom-runtime-generation-divergence-theory, 2026-05-06-aibom-effectiveness-risk-mitigation-limits]
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# What is the minimal viable schema for an Artificial Intelligence Bill of Materials (AIBOM) for agentic workloads, how should it align with CycloneDX and Software Package Data Exchange (SPDX) standards, and what new property types are required?

## Research Question

What is the minimal viable set of schema properties required to describe agentic Artificial Intelligence (AI) system dependencies in a useful, standards-aligned Artificial Intelligence Bill of Materials (AIBOM), specifically, how should existing CycloneDX Machine Learning Bill of Materials (ML-BOM) and Software Package Data Exchange (SPDX) 3.0 AI profile schema be extended to represent deterministic versus non-deterministic components, mutable versus immutable dependencies, prompts, Retrieval-Augmented Generation (RAG) indexes, memory, and identity-bound versus ambient execution contexts?

## Scope

**In scope:**
- Analysis of CycloneDX ML-BOM and CycloneDX 1.7 object-model fields and their applicability to agentic components
- Analysis of SPDX 3.0 AI and Dataset profiles for agentic AI coverage
- Proposed schema extensions for component types not covered, prompts, system instructions, RAG knowledge-base snapshots, memory schemas, tool permission-scope manifests, and model configuration, such as temperature, sampling parameters, and context window
- Versioning and fingerprinting strategies for mutable components, prompt Secure Hash Algorithm 256 (SHA-256) hash, RAG index digest, memory schema version, and signed instruction artefacts
- Property-type design, deterministic versus non-deterministic, mutability classification, and execution-context binding
- Comparative analysis of current academic and industry AIBOM schema proposals

**Out of scope:**
- Runtime or observed AIBOM, covered in `2026-05-06-aibom-runtime-generation-divergence-theory` and `2026-05-06-aibom-runtime-capture-opentelemetry-practice`
- Platform-specific schema extraction implementations, covered in `2026-05-06-aibom-declared-construction-practice`
- Full identity and attribution schema design, covered in `2026-05-06-aibom-identity-delegation-trust-theory`

**Constraints:**
- Must evaluate against at least two existing standards, CycloneDX and SPDX, rather than proposing an entirely new schema from scratch
- Standards evidence must be current, 2023 or later, except where older foundational guidance is still the defining source
- Proposed properties must be practically populable from accessible design-time artefacts rather than requiring runtime capture

## Context

- [fact; source: https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom] The National Telecommunications and Information Administration (NTIA) defines a Software Bill of Materials (SBOM) as a formal record containing component details and supply-chain relationships for software.
- [fact; source: https://cyclonedx.org/capabilities/mlbom/; https://raw.githubusercontent.com/CycloneDX/specification/master/schema/bom-1.7.schema.json; https://spdx.github.io/spdx-spec/v3.0.1/model/AI/AI/; https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/; https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Classes/DatasetPackage/] CycloneDX and SPDX already model AI-relevant artefacts such as machine-learning models, datasets, model cards, hyperparameters, and package relationships.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-sbom-conceptual-gaps-theory.html; https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html] The unresolved design problem is not whether AIBOM needs more metadata, but which minimal typed extensions are necessary so prompts, retrieval surfaces, tool permissions, memory schemas, and execution bindings become auditable design-time artefacts instead of hidden behaviour.

## Approach

1. **Standards survey:** map CycloneDX ML-BOM, CycloneDX 1.7 object-model, and SPDX 3.0 AI and Dataset profile surfaces to the agentic component taxonomy from `2026-05-06-aibom-sbom-conceptual-gaps-theory`.
2. **Gap property design:** for each uncovered component, design a minimal schema extension with property name, type, cardinality, allowed values, and a standards-aligned placement.
3. **Mutability and versioning model:** evaluate hashes, Merkle-tree digests, semantic versioning, and signatures for mutable or semi-mutable artefacts.
4. **Execution-context binding:** assess how an AIBOM should declare that one agent configuration runs with a specific model, prompt, tool manifest, retrieval snapshot, and memory schema.
5. **Schema proposal:** write a minimal viable AIBOM example in JavaScript Object Notation (JSON) or YAML Ain't Markup Language (YAML), extending CycloneDX and mapping the same concepts to SPDX.

## Sources

- [x] [National Telecommunications and Information Administration (2021) The Minimum Elements for a Software Bill of Materials (SBOM)](https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom) - foundational minimum-elements framing for a bill of materials
- [x] [CycloneDX (2026) Introduction to AI/ML-BOM](https://cyclonedx.org/capabilities/mlbom/) - official CycloneDX statement of current AI and machine-learning bill-of-materials coverage
- [x] [CycloneDX (2026) CycloneDX Object Model Overview](https://cyclonedx.org/specification/overview/) - official object-model guidance for components, services, dependencies, formulation, declarations, and extension points
- [x] [CycloneDX (2025) CycloneDX 1.7 JSON Schema](https://raw.githubusercontent.com/CycloneDX/specification/master/schema/bom-1.7.schema.json) - reference schema showing native component types, model-card support, component data, properties, services, and formulation
- [x] [Rutkows (2025) Proposed changes for Machine Learning Bill of Materials (MLBOM) schema for CycloneDX 2.0](https://github.com/CycloneDX/specification/issues/702) - current CycloneDX ML-BOM working-group issue showing unresolved model and agent-card gaps
- [x] [Rutkows (2023) Add modelCard to Service definition](https://github.com/CycloneDX/specification/issues/268) - evidence that AI service endpoints do not fit neatly into top-level component modelling alone
- [x] [Bardenstein (2023) Add a libraries or dependencies field to the machine-learning-model component](https://github.com/CycloneDX/specification/issues/282) - evidence that even current machine-learning-model dependency expression remains incomplete
- [x] [SPDX (2024) SPDX Specification 3.0.1 AI Profile](https://spdx.github.io/spdx-spec/v3.0.1/model/AI/AI/) - formal AI profile summary and profile-conformance rules
- [x] [SPDX (2024) SPDX Specification 3.0.1 AIPackage](https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/) - official AI package class and properties
- [x] [SPDX (2024) SPDX Specification 3.0.1 DatasetPackage](https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Classes/DatasetPackage/) - official dataset package class and properties
- [x] [SPDX (2024) SPDX Specification 3.0.1 Extension Profile](https://spdx.github.io/spdx-spec/v3.0.1/model/Extension/Extension/) - official extension base class for SPDX profile extensions
- [x] [SPDX AI Working Group (2026) SPDX AI Profile Usage Examples](https://github.com/spdx/spdx-examples/blob/master/ai/README.md) - current example index showing SPDX AI example scope
- [x] [SPDX AI Working Group (2026) Example 02](https://github.com/spdx/spdx-examples/blob/master/ai/example02/README.md) - concrete SPDX AI example using `dependsOn`, `generates`, `hasDataFile`, `hasDocumentation`, `testedOn`, and `trainedOn`
- [x] [GenAI Security Project (2026) Open Worldwide Application Security Project (OWASP) AIBOM Generator](https://github.com/GenAI-Security-Project/aibom-generator) - practical AIBOM generator aligned to CycloneDX 1.6 and compatible with the SPDX AI profile
- [x] [Open Worldwide Application Security Project (OWASP) AIBOM (2026) Making AI Systems Transparent, Auditable, and Secure](https://owaspaibom.org/) - community framing for AIBOM goals and transparency outcomes
- [x] [Suriyawongkul et al. (2025) Implementing AI Bill of Materials (AI BOM) with SPDX 3.0](https://arxiv.org/abs/2504.16743) - formal guide arguing for AI-BOM expansion beyond software-only SBOM semantics
- [x] [Rajbahadur et al. (2026) Building an Open AIBOM Standard in the Wild](https://arxiv.org/abs/2510.07070) - experience report on extending SPDX with 36 AI and Dataset fields
- [x] [David Mitchell (2026) Why does Software Bill of Materials (SBOM) fail as a complete inventory model for agentic AI workloads, and what new conceptual abstractions are required?](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-sbom-conceptual-gaps-theory.html) - prior completed corpus item defining the conceptual gaps that this schema must close
- [x] [David Mitchell (2026) What security capabilities are required in an enterprise AI system to address prompt injection, RAG-based attacks, model supply chain compromise, and data exfiltration?](https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html) - prior completed corpus item establishing why prompts, retrieval, and tool manifests are security-relevant artefacts
- [x] [David Mitchell (2026) How can a runtime-observed AIBOM be generated for an agentic AI system, and how much does it diverge from the declared design-time AIBOM?](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html) - adjacent corpus item defining the declared-versus-observed boundary
- [x] [David Mitchell (2026) How should identity, delegation chains, and permission scopes be formally modelled in an AIBOM schema?](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html) - adjacent corpus item on identity and permission bindings

## Related

- [Why does Software Bill of Materials (SBOM) fail as a complete inventory model for agentic Artificial Intelligence (AI) workloads, and what new conceptual abstractions are required?](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-sbom-conceptual-gaps-theory.html)
- [How can a runtime-observed Artificial Intelligence Bill of Materials (AIBOM) be generated for an agentic Artificial Intelligence (AI) system, and how much does it diverge from the declared design-time AIBOM?](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html)
- [How should identity, delegation chains, and permission scopes be formally modelled in an Artificial Intelligence Bill of Materials (AIBOM) schema to enable end-to-end attribution across agentic Artificial Intelligence (AI) systems?](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0 to 5 are the investigation, and Section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: What is the smallest standards-aligned AIBOM schema that can declare the semantically active design-time artefacts of an agentic AI system, and how should that schema map to CycloneDX and SPDX without forking either standard?
- Scope: Standards coverage, extension-point design, mutable-artefact versioning, execution-context binding, and a worked minimal schema example.
- Constraints: Use CycloneDX and SPDX as the base, keep design-time only, and prefer properties and classes that can be populated from accessible artefacts.
- Output: knowledge.
- Prior completed items reviewed: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-sbom-conceptual-gaps-theory.html ; https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html

### §1 Question Decomposition

- **Root question:** Which minimum set of schema objects and typed properties must an AIBOM add so an agentic system's design-time behaviour-shaping artefacts become interoperable, inspectable, and standards-aligned?
  - **A. Current standards coverage**
    - A1. Which CycloneDX 1.7 objects can already represent models, data, services, dependencies, and process formulation?
    - A2. Which SPDX 3.0 AI and Dataset profile classes already cover models, datasets, and lifecycle relationships?
  - **B. Uncovered agentic artefacts**
    - B1. Which agentic artefacts materially shape behaviour but are not first-class in current standards?
    - B2. Are those artefacts design-time accessible or only runtime observable?
  - **C. Extension strategy**
    - C1. Which gaps can CycloneDX close with existing `properties`, `component`, `service`, `data`, and `formulation` structures?
    - C2. Which gaps require an SPDX extension profile or new classes rather than simple reuse of `AIPackage` and `DatasetPackage`?
  - **D. Property design**
    - D1. Which new typed properties are strictly necessary for agentic semantics, mutability, determinism, and execution binding?
    - D2. Which proposed properties can be populated from stable artefacts rather than speculative runtime state?
  - **E. Worked schema**
    - E1. What does a minimal CycloneDX-aligned example look like for model, prompt, tool manifest, RAG snapshot, memory schema, and orchestration config?
    - E2. How should that same design be interpreted in SPDX terms?

### §2 Investigation

#### Source substitutions and failed-search notes

- Search note: query `"Toward a Framework for Agentic AI Provenance"` -> no matching primary source found in this session; the seeded `https://arxiv.org/abs/2407.01392` link resolves to an unrelated computer-vision paper and was not used as evidence.
- Search note: query `"AIBOM: Towards a Standard Bill of Materials for AI Systems"` -> no matching primary source found in this session; replaced with the accessible AIBOM standards sources `https://arxiv.org/abs/2504.16743` and `https://arxiv.org/abs/2510.07070`.

#### A. What CycloneDX and SPDX already cover

- [fact; source: https://raw.githubusercontent.com/CycloneDX/specification/master/schema/bom-1.7.schema.json] The CycloneDX 1.7 JSON schema includes native component types `machine-learning-model` and `data`, and its `component` object supports `modelCard`, `data`, `properties`, `hashes`, `externalReferences`, `components`, and `signature`.
- [fact; source: https://cyclonedx.org/specification/overview/; https://raw.githubusercontent.com/CycloneDX/specification/master/schema/bom-1.7.schema.json] CycloneDX models external tools and endpoints as `services`, dependency edges as `dependencies`, and creation or deployment process structure as `formulation`, `workflow`, `task`, and `step`.
- [fact; source: https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/; https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Classes/DatasetPackage/] SPDX 3.0.1 defines both `AIPackage` and `DatasetPackage` as subclasses of `/Software/Package`, which means AI models and datasets inherit package-style identity, version, supplier, release time, and download-location semantics.
- [fact; source: https://github.com/spdx/spdx-examples/blob/master/ai/README.md; https://github.com/spdx/spdx-examples/blob/master/ai/example02/README.md] Current SPDX AI examples already show lifecycle relationships such as `dependsOn`, `generates`, `hasDataFile`, `hasDocumentation`, `testedOn`, and `trainedOn`.
- [fact; source: https://github.com/GenAI-Security-Project/aibom-generator; https://owaspaibom.org/] The OWASP AIBOM effort currently operationalizes AIBOM generation as CycloneDX 1.6 JSON compatible with the SPDX AI profile and focuses on model cards, configurations, repository files, and completeness scoring for model-centred assets.
- [inference; source: https://cyclonedx.org/capabilities/mlbom/; https://raw.githubusercontent.com/CycloneDX/specification/master/schema/bom-1.7.schema.json; https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/; https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Classes/DatasetPackage/; https://github.com/GenAI-Security-Project/aibom-generator] Both standards currently cover models, datasets, and training metadata better than they cover deployed agent configuration, prompt templates, tool permission manifests, retrieval snapshots, or memory schemas.

#### B. Evidence that current AI-BOM coverage is still incomplete for agentic systems

- [fact; source: https://github.com/CycloneDX/specification/issues/702] CycloneDX issue 702, opened for ML-BOM work toward CycloneDX 2.0, explicitly tracks unresolved changes around model parameters, training considerations, required hyperparameters, and an additional consideration for future `system cards` and `agent cards`.
- [fact; source: https://github.com/CycloneDX/specification/issues/268] CycloneDX issue 268 argues that AI capabilities increasingly appear as service endpoints and therefore current model-card placement on components alone is insufficient for AI services.
- [fact; source: https://github.com/CycloneDX/specification/issues/282] CycloneDX issue 282 proposes adding explicit machine-learning-model library or dependency fields because current model components do not adequately express framework dependencies such as PyTorch, Open Neural Network Exchange (ONNX), Transformers, or Diffusers.
- [fact; source: https://arxiv.org/abs/2504.16743] Suriyawongkul et al. argue that AI projects require a broader bill of materials than software alone, including algorithms, data-collection methods, frameworks and libraries, licensing information, and standard compliance.
- [fact; source: https://arxiv.org/abs/2510.07070] Rajbahadur et al. report that the SPDX AIBOM extension effort added 36 new AI and Dataset fields and frames the resulting specification around datasets, models, provenance, and iterative training artefacts.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-sbom-conceptual-gaps-theory.html; https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html] Prior completed repository work establishes that prompts, retrieved context, tool-path permissions, delegated authority, and memory state are semantically active artefacts that materially change an agent's effective behaviour and risk surface.
- [inference; source: https://github.com/CycloneDX/specification/issues/702; https://github.com/CycloneDX/specification/issues/268; https://github.com/CycloneDX/specification/issues/282; https://arxiv.org/abs/2504.16743; https://arxiv.org/abs/2510.07070] The agentic design gap is therefore not merely more model metadata, but a missing way to declare non-code artefacts and control surfaces that shape behaviour at design time.

#### C. Minimal extension strategy that stays aligned with existing standards

- [fact; source: https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom] NTIA minimum elements center on component identity, supplier, version, dependency relationship, author, and timestamp information.
- [fact; source: https://cyclonedx.org/specification/overview/; https://raw.githubusercontent.com/CycloneDX/specification/master/schema/bom-1.7.schema.json] CycloneDX already provides three flexible alignment surfaces for agentic AIBOM design, namely typed components and services, graph edges through dependencies, and process structure through formulation workflows and tasks, plus open-ended `properties` arrays on all three.
- [fact; source: https://spdx.github.io/spdx-spec/v3.0.1/model/Extension/Extension/; https://spdx.github.io/spdx-spec/v3.0.1/model/AI/AI/] SPDX 3.0.1 provides a formal extension namespace and profile structure, while its AI profile remains centred on package and relationship semantics.
- [inference; source: https://cyclonedx.org/specification/overview/; https://raw.githubusercontent.com/CycloneDX/specification/master/schema/bom-1.7.schema.json; https://spdx.github.io/spdx-spec/v3.0.1/model/Extension/Extension/; https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/; https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Classes/DatasetPackage/] The smallest standards-aligned path is asymmetric: CycloneDX can express a minimal agentic AIBOM today with existing objects plus namespaced properties, while SPDX likely needs an AIBOM extension profile with a few new classes or properties because its current AI surface is more strongly typed around packages.
- [inference; source: https://github.com/GenAI-Security-Project/aibom-generator; https://arxiv.org/abs/2504.16743; https://arxiv.org/abs/2510.07070] This asymmetric strategy preserves near-term interoperability with current CycloneDX tooling while still giving SPDX a clear formalization path that avoids overloading generic text fields.

#### D. Minimal new property types required for agentic semantics

- [inference; source: https://raw.githubusercontent.com/CycloneDX/specification/master/schema/bom-1.7.schema.json; https://github.com/CycloneDX/specification/issues/702; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-sbom-conceptual-gaps-theory.html] A minimal AIBOM needs a typed semantic-role property, for example `aibom:componentClass`, because native component types do not distinguish prompt templates, system instructions, retrieval snapshots, memory schemas, agent configurations, or tool capability manifests from generic `data` and `service` objects.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-sbom-conceptual-gaps-theory.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html] A minimal AIBOM needs `aibom:mutability` with values such as `immutable`, `versioned-mutable`, and `runtime-mutable`, because declared artefacts differ in whether a digest alone is sufficient, whether version plus digest is required, or whether only schema and snapshot policy can be declared at design time.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-sbom-conceptual-gaps-theory.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html] A minimal AIBOM needs `aibom:determinism` with values such as `deterministic`, `stochastic`, and `environment-dependent`, because agentic execution combines fully replayable configuration objects with non-deterministic models and externally varying retrieval or service results.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html; https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html] A minimal AIBOM needs `aibom:contextBinding` with values such as `identity-bound`, `policy-bound`, and `ambient`, because the same tool or retrieval source carries different governance meaning depending on whether access is tied to a delegated principal, a fixed policy object, or implicit environment credentials.
- [inference; source: https://raw.githubusercontent.com/CycloneDX/specification/master/schema/bom-1.7.schema.json; https://cyclonedx.org/specification/overview/; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html] A minimal AIBOM needs `aibom:snapshotStrategy`, because existing hashes and signatures can record content integrity, but mutable resources such as retrieval corpora and memory schemas still require a declared statement of how the design-time snapshot is identified, for example `content-hash`, `merkle-root`, `schema-version`, or `external-reference`.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html; https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html] A minimal AIBOM needs `aibom:approvalScopeRef` or an equivalent permission-manifest reference, because agentic risk depends not only on which tools exist but on which operations the declared configuration is allowed to invoke through them.

#### E. Versioning and fingerprinting strategy for mutable artefacts

- [fact; source: https://cyclonedx.org/specification/overview/; https://raw.githubusercontent.com/CycloneDX/specification/master/schema/bom-1.7.schema.json] CycloneDX already supports cryptographic hashes, signatures, provenance-oriented external references, and formulation records for how artefacts were built or deployed.
- [inference; source: https://raw.githubusercontent.com/CycloneDX/specification/master/schema/bom-1.7.schema.json; https://github.com/CycloneDX/specification/issues/702] Prompt templates and system-instruction files should be treated as immutable or versioned-mutable `data` components whose canonical fingerprint is a content hash plus version, because their full text is normally available at design time.
- [inference; source: https://raw.githubusercontent.com/CycloneDX/specification/master/schema/bom-1.7.schema.json; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html] Retrieval corpora should be represented as versioned-mutable `data` components whose canonical fingerprint is a corpus snapshot identifier plus a Merkle-tree digest or equivalent aggregate digest, because a single file hash rarely captures a distributed or chunked index faithfully.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html] Memory should be split into a declared memory schema and a runtime memory state, because the schema is design-time stable enough to version and hash, while the live state belongs in runtime AIBOM rather than in the minimal declared schema.
- [inference; source: https://github.com/CycloneDX/specification/issues/702; https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/] Model configuration values such as temperature, top-p, seed policy, and context window should be versioned as explicit configuration objects rather than as prose, because current standards and working-group issues already treat required hyperparameters as materially important but not yet sufficiently structured.

#### F. Worked minimal schema proposal

- [inference; source: https://raw.githubusercontent.com/CycloneDX/specification/master/schema/bom-1.7.schema.json; https://cyclonedx.org/specification/overview/; https://github.com/CycloneDX/specification/issues/702; https://spdx.github.io/spdx-spec/v3.0.1/model/Extension/Extension/] The following minimal example stays within CycloneDX 1.7, uses only existing object types plus namespaced properties, and exposes the same design as an SPDX extension-profile candidate.

```yaml
bomFormat: CycloneDX
specVersion: "1.7"
version: 1
metadata:
  component:
    type: application
    name: support-agent
    version: "1.0.0"
components:
  - bom-ref: model:gpt-4.1
    type: machine-learning-model
    name: gpt-4.1
    version: "2026-04-01"
    modelCard:
      modelParameters:
        - name: context_window
          value: "128000"
    properties:
      - name: aibom:determinism
        value: stochastic
      - name: aibom:mutability
        value: immutable
  - bom-ref: prompt:system
    type: data
    name: support-agent-system-prompt
    version: "3.2.1"
    hashes:
      - alg: SHA-256
        content: 2b3f...deadbeef
    data:
      - type: configuration
        name: system-prompt.txt
    properties:
      - name: aibom:componentClass
        value: system-instruction
      - name: aibom:determinism
        value: deterministic
      - name: aibom:mutability
        value: versioned-mutable
      - name: aibom:snapshotStrategy
        value: content-hash
  - bom-ref: rag:kb-snapshot
    type: data
    name: support-kb-snapshot
    version: "2026-05-06"
    externalReferences:
      - type: distribution
        url: https://example.internal/kb/snapshots/2026-05-06
    properties:
      - name: aibom:componentClass
        value: rag-corpus-snapshot
      - name: aibom:mutability
        value: versioned-mutable
      - name: aibom:determinism
        value: environment-dependent
      - name: aibom:snapshotStrategy
        value: merkle-root
  - bom-ref: memory:schema
    type: data
    name: support-agent-memory-schema
    version: "1.4.0"
    properties:
      - name: aibom:componentClass
        value: memory-schema
      - name: aibom:mutability
        value: versioned-mutable
      - name: aibom:snapshotStrategy
        value: schema-version
services:
  - bom-ref: service:crm
    name: crm-api
    endpoints:
      - https://crm.example.internal
    properties:
      - name: aibom:componentClass
        value: tool-capability-manifest
      - name: aibom:contextBinding
        value: identity-bound
      - name: aibom:approvalScopeRef
        value: policy:crm-read-ticket-update
dependencies:
  - ref: metadata.component
    dependsOn:
      - model:gpt-4.1
      - prompt:system
      - rag:kb-snapshot
      - memory:schema
      - service:crm
formulation:
  - bom-ref: workflow:agent-config
    workflows:
      - bom-ref: workflow:triage
        name: support-triage
        resourceReferences:
          - ref: model:gpt-4.1
          - ref: prompt:system
          - ref: rag:kb-snapshot
          - ref: memory:schema
          - ref: service:crm
        properties:
          - name: aibom:componentClass
            value: agent-configuration
          - name: aibom:contextBinding
            value: policy-bound
```

- [inference; source: https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/; https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Classes/DatasetPackage/; https://spdx.github.io/spdx-spec/v3.0.1/model/Extension/Extension/; https://github.com/spdx/spdx-examples/blob/master/ai/example02/README.md] The closest SPDX mapping is to keep the model as `AIPackage`, the retrieval corpus as `DatasetPackage`, the prompt and memory schema as AIBOM extension classes or extension-tagged packages, the tool manifest as a referenced service or software package plus permission metadata, and the orchestration configuration as an AIBOM extension class connected through explicit relationships.

### §3 Reasoning

- [fact; source: https://raw.githubusercontent.com/CycloneDX/specification/master/schema/bom-1.7.schema.json; https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/; https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Classes/DatasetPackage/] The standards evidence is strong that current schemas already support model, dataset, dependency, and basic provenance objects.
- [inference; source: https://github.com/CycloneDX/specification/issues/702; https://github.com/CycloneDX/specification/issues/268; https://github.com/CycloneDX/specification/issues/282; https://arxiv.org/abs/2510.07070] The gap evidence is strongest where standards maintainers themselves are still debating agent-card, service-model, and dependency semantics, which supports an extension-first strategy rather than a claim that the problem is already solved in core schemas.
- [inference; source: https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom; https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html] The minimum viable schema should include only artefacts that both materially alter behaviour and can be stably referenced at design time, because that preserves NTIA-like practicality while still surfacing the control surfaces that create agentic risk.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html] This design deliberately excludes live memory state, retrieved chunks, and transient tool outputs from the declared schema because those are runtime-evidence problems rather than design-time inventory problems.
- [assumption; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html; https://github.com/GenAI-Security-Project/aibom-generator] The minimal schema assumes that real agent platforms can externalize prompt artefacts, tool policies, and model configuration into versioned files or policy objects instead of burying them in unstructured code paths.

### §4 Consistency Check

- [fact; source: https://raw.githubusercontent.com/CycloneDX/specification/master/schema/bom-1.7.schema.json; https://cyclonedx.org/specification/overview/] CycloneDX is the stronger near-term delivery target because its reference schema already exposes flexible `properties`, service objects, data objects, and formulation workflows without waiting for a new profile release.
- [fact; source: https://spdx.github.io/spdx-spec/v3.0.1/model/Extension/Extension/; https://spdx.github.io/spdx-spec/v3.0.1/model/AI/AI/] SPDX is the stronger long-term semantic target because it supports profile-based formalization and extension classes, even though its current AI profile remains package-centric.
- [inference; source: https://raw.githubusercontent.com/CycloneDX/specification/master/schema/bom-1.7.schema.json; https://spdx.github.io/spdx-spec/v3.0.1/model/Extension/Extension/] There is no contradiction between these positions because one recommendation concerns immediate serialization practice and the other concerns a cleaner formalization path for future standardization.
- [inference; source: https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html] There is also no contradiction between minimum viability and agentic specificity, because the final proposal adds six design-time properties and reuses existing hash, version, dependency, and workflow surfaces rather than introducing a wholly new graph model.

### §5 Depth and Breadth Expansion

- [inference; source: https://github.com/CycloneDX/specification/issues/702; https://github.com/CycloneDX/specification/issues/268; https://github.com/CycloneDX/specification/issues/282] **Technical lens:** the main technical debt is not absence of graph structure, since CycloneDX and SPDX both already express relationships, but absence of typed semantics for prompt, service-mediated model use, and mutable context artefacts.
- [inference; source: https://arxiv.org/abs/2510.07070; https://arxiv.org/abs/2504.16743] **Standards-process lens:** current AIBOM standardization work is still actively extending existing BOM ecosystems rather than replacing them, so a proposal that aligns with extension mechanisms is more adoption-realistic than a novel standalone schema.
- [inference; source: https://github.com/GenAI-Security-Project/aibom-generator; https://owaspaibom.org/] **Economic lens:** implementation cost stays lower if the minimal schema rides existing CycloneDX exporters and validators, because producers can add a small property taxonomy before they invest in richer runtime capture.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html] **Governance lens:** the highest-value additions are not more model-card prose but typed declarations for prompts, retrieval snapshots, and permission-bound tools, because those are the design surfaces where approval and risk posture actually change.

### §6 Synthesis

**Executive summary:**

- [inference; source: https://raw.githubusercontent.com/CycloneDX/specification/master/schema/bom-1.7.schema.json; https://cyclonedx.org/specification/overview/; https://spdx.github.io/spdx-spec/v3.0.1/model/Extension/Extension/] A minimal viable AIBOM for agentic workloads should not invent a new bill-of-materials standard, but should reuse CycloneDX and SPDX for core inventory structure and add a small extension layer for agentic artefacts and control semantics.
- [inference; source: https://raw.githubusercontent.com/CycloneDX/specification/master/schema/bom-1.7.schema.json; https://github.com/CycloneDX/specification/issues/702; https://github.com/CycloneDX/specification/issues/268] CycloneDX is the better immediate serialization target because its existing component, service, dependency, formulation, and property surfaces can already express the minimal schema without waiting for a new release.
- [inference; source: https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/; https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Classes/DatasetPackage/; https://spdx.github.io/spdx-spec/v3.0.1/model/Extension/Extension/] SPDX should be the long-term formalization target through an AIBOM extension profile, because current AI and Dataset profiles remain package-centric and do not yet make prompt, orchestration, or memory-schema artefacts first-class.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html] The minimum new property set is six fields, semantic class, mutability, determinism, context binding, snapshot strategy, and approval-scope reference, because those six cover the design-time semantics that standard SBOM fields and current AI profiles still miss.

**Key findings:**

1. [inference; source: https://raw.githubusercontent.com/CycloneDX/specification/master/schema/bom-1.7.schema.json; https://cyclonedx.org/specification/overview/] A minimal viable AIBOM for agentic workloads can stay CycloneDX-aligned today by reusing `component`, `service`, `dependency`, and `formulation` objects and by adding namespaced properties rather than requiring a new core component type immediately.
2. [fact; source: https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/; https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Classes/DatasetPackage/; https://spdx.github.io/spdx-spec/v3.0.1/model/Extension/Extension/] SPDX 3.0.1 already provides strong package-level coverage for models and datasets, but a complete agentic AIBOM still needs an extension profile because prompt, orchestration, and memory-schema artefacts are not first-class classes in the current AI profile.
3. [fact; source: https://github.com/CycloneDX/specification/issues/702; https://github.com/CycloneDX/specification/issues/268; https://github.com/CycloneDX/specification/issues/282] CycloneDX's own open issues show that AI service modelling, model dependency declaration, fixed hyperparameters, and future agent-card semantics remain unresolved, which is direct evidence that agentic schema design is still extension territory rather than settled standard practice.
4. [inference; source: https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-sbom-conceptual-gaps-theory.html] The minimal agentic extension should add only behaviour-shaping artefacts that can be stably identified at design time, model, prompt or instruction, retrieval snapshot, memory schema, tool manifest, and orchestration config, because that preserves NTIA-style practicality while closing the most important conceptual gaps.
5. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html; https://raw.githubusercontent.com/CycloneDX/specification/master/schema/bom-1.7.schema.json] Mutability and fingerprinting should reuse existing hash, version, external-reference, and signature fields wherever possible, while a new `snapshotStrategy` property records whether an artefact is pinned by content hash, Merkle-tree digest, schema version, or external snapshot identifier.
6. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html; https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html] Memory state and live retrieval results should not be part of the minimal declared AIBOM, because they are runtime-evidence surfaces, but the memory schema and retrieval snapshot policy must be declared so the runtime object can later be compared against approved design intent.
7. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html; https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html] Execution binding is a first-class design concern, so a minimal AIBOM must declare whether each tool or context surface is identity-bound, policy-bound, or ambient, and it must reference the approval scope that constrains the declared tool path.
8. [inference; source: https://github.com/GenAI-Security-Project/aibom-generator; https://arxiv.org/abs/2504.16743; https://arxiv.org/abs/2510.07070] The most adoption-realistic path is a two-step standardization strategy, ship a CycloneDX 1.7 profile today with a lightweight AIBOM property taxonomy, then upstream the same semantics into an SPDX AIBOM extension profile as current AIBOM working-group efforts mature.

**Evidence map:**

| claim | source | confidence | notes |
|---|---|---|---|
| [inference] CycloneDX can serialize the minimal schema today through existing objects plus namespaced properties. | https://raw.githubusercontent.com/CycloneDX/specification/master/schema/bom-1.7.schema.json ; https://cyclonedx.org/specification/overview/ | high | Native extension surface exists |
| [fact] SPDX AI and Dataset profiles remain package-centric and need extension for prompt and orchestration artefacts. | https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/ ; https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Classes/DatasetPackage/ ; https://spdx.github.io/spdx-spec/v3.0.1/model/Extension/Extension/ | high | Strong normative model evidence |
| [fact] CycloneDX maintainers are still discussing AI service, dependency, hyperparameter, and agent-card gaps. | https://github.com/CycloneDX/specification/issues/702 ; https://github.com/CycloneDX/specification/issues/268 ; https://github.com/CycloneDX/specification/issues/282 | medium | Issue tracker, not ratified standard |
| [inference] The minimal extension surface should include model, prompt or instruction, retrieval snapshot, memory schema, tool manifest, and orchestration config. | https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-sbom-conceptual-gaps-theory.html | medium | Minimality judgement |
| [inference] `snapshotStrategy` is necessary because existing hash fields alone do not explain how mutable artefacts are pinned. | https://raw.githubusercontent.com/CycloneDX/specification/master/schema/bom-1.7.schema.json ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html | medium | Derived from mutable-context gap |
| [inference] Runtime memory state and live retrieval results belong in runtime AIBOM, not in the minimal declared schema. | https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html ; https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html | medium | Declared-versus-observed boundary |
| [inference] Context binding and approval-scope reference are required to make tool and retrieval surfaces governance-relevant at design time. | https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html ; https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html | medium | Cross-item synthesis |
| [inference] The best adoption path is CycloneDX property taxonomy now and SPDX extension profile next. | https://github.com/GenAI-Security-Project/aibom-generator ; https://arxiv.org/abs/2504.16743 ; https://arxiv.org/abs/2510.07070 | medium | Standards-process judgement |

**Assumptions:**

- [assumption; source: https://github.com/GenAI-Security-Project/aibom-generator; https://github.com/CycloneDX/specification/issues/702] Producers can externalize prompt templates, tool manifests, and orchestration configurations into versioned artefacts rather than keeping them only as opaque application code. Justification: current AIBOM tooling and CycloneDX working-group discussions already assume extractable model and configuration metadata.
- [assumption; source: https://raw.githubusercontent.com/CycloneDX/specification/master/schema/bom-1.7.schema.json; https://spdx.github.io/spdx-spec/v3.0.1/model/Extension/Extension/] Namespaced AIBOM properties will be acceptable as an interim serialization strategy before the semantics become part of a formal shared profile. Justification: both ecosystems expose explicit extension mechanisms for this style of incremental evolution.

**Analysis:**

- [inference; source: https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom; https://raw.githubusercontent.com/CycloneDX/specification/master/schema/bom-1.7.schema.json; https://spdx.github.io/spdx-spec/v3.0.1/model/Extension/Extension/] The evidence supports a minimum-viable design that preserves existing BOM identity and dependency semantics while adding only the smallest new agentic layer needed to classify semantically active artefacts and their control meaning.
- [inference; source: https://github.com/CycloneDX/specification/issues/702; https://github.com/CycloneDX/specification/issues/268; https://github.com/CycloneDX/specification/issues/282; https://arxiv.org/abs/2510.07070] CycloneDX is operationally ahead for serialization flexibility, but SPDX is procedurally ahead for formal profile evolution, so the design should deliberately map one conceptual schema across both ecosystems rather than forcing one standard to behave like the other.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html; https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html] The core trade-off is between design-time stability and runtime completeness: the minimal declared schema must stop at artefacts that can be approved and versioned before execution, while leaving live context, memory state, and retrieval results to a linked runtime AIBOM rather than overloading one artefact with both purposes.
- [inference; source: https://raw.githubusercontent.com/CycloneDX/specification/master/schema/bom-1.7.schema.json; https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/; https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Classes/DatasetPackage/] The resulting design is minimal not because it is small in line count, but because every retained field answers one of six concrete questions, what class of artefact is this, how stable is it, how deterministic is it, how is it pinned, how is it bound to authority, and which approved operations does it enable?

**Risks, gaps, uncertainties:**

- [fact; source: https://github.com/CycloneDX/specification/issues/702] CycloneDX agent-card semantics are still open working-group territory, so any current `aibom:componentClass=agent-configuration` convention is an interim design rather than a ratified standard field.
- [fact; source: https://spdx.github.io/spdx-spec/v3.0.1/model/Extension/Extension/] SPDX extension mechanics are clear at the namespace level, but this item does not yet specify a fully formal AIBOM extension ontology with machine-readable class definitions.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html] Retrieval snapshot digest design remains partly unsettled because different vector stores and indexing pipelines expose different levels of reproducible corpus identity.
- [inference; source: https://github.com/GenAI-Security-Project/aibom-generator; https://owaspaibom.org/] Practical tool support is currently model-centred, so prompt, memory-schema, and tool-manifest extraction workflows may lag the schema until practice implementations catch up.

**Open questions:**

- [inference; source: https://github.com/CycloneDX/specification/issues/702; https://arxiv.org/abs/2510.07070] Should future standards define a first-class `agent-configuration` object, or is a property-taxonomy approach sufficient if formulation workflows are already available?
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html] What is the most reproducible digest method for heterogeneous RAG indexes that mix raw source files, chunking parameters, embeddings, and ranking metadata?
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html] Should approval-scope references point to external policy objects only, or should BOM-native permission manifests become first-class cross-standard objects?

### §7 Recursive Review

- Audit status: prior-work scan completed, sources normalized to URL-backed display names, and broken seeded sources were replaced with accessible standards sources.
- Audit status: all factual and inferential claims in `## Research Skill Output` are labelled, and the `## Findings` section mirrors the Section 6 synthesis.
- [inference; source: https://raw.githubusercontent.com/CycloneDX/specification/master/schema/bom-1.7.schema.json; https://spdx.github.io/spdx-spec/v3.0.1/model/Extension/Extension/; https://github.com/CycloneDX/specification/issues/702] Overall confidence remains medium because the base standards and extension points are clear, but agent-specific field convergence is still incomplete in the live standards processes.

---

## Findings

### Executive Summary

A minimal viable AIBOM for agentic workloads should reuse CycloneDX and SPDX for core inventory structure and add only a small extension layer for agentic artefacts and control semantics, rather than introducing a separate bill-of-materials standard. [inference; source: https://raw.githubusercontent.com/CycloneDX/specification/master/schema/bom-1.7.schema.json; https://cyclonedx.org/specification/overview/; https://spdx.github.io/spdx-spec/v3.0.1/model/Extension/Extension/]
CycloneDX is the better immediate serialization target because its existing component, service, dependency, formulation, and property surfaces can already express the minimal schema without waiting for a new release. [inference; source: https://raw.githubusercontent.com/CycloneDX/specification/master/schema/bom-1.7.schema.json; https://github.com/CycloneDX/specification/issues/702; https://github.com/CycloneDX/specification/issues/268]
SPDX should be the long-term formalization target through an AIBOM extension profile, because current AI and Dataset profiles remain package-centric and do not yet make prompt, orchestration, or memory-schema artefacts first-class. [inference; source: https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/; https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Classes/DatasetPackage/; https://spdx.github.io/spdx-spec/v3.0.1/model/Extension/Extension/]
The minimum new property set is six fields, semantic class, mutability, determinism, context binding, snapshot strategy, and approval-scope reference, because those six cover the design-time semantics that standard SBOM fields and current AI profiles still miss. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html; https://raw.githubusercontent.com/CycloneDX/specification/master/schema/bom-1.7.schema.json]

### Key Findings

1. **A minimal viable AIBOM for agentic workloads can stay CycloneDX-aligned today by reusing `component`, `service`, `dependency`, and `formulation` objects and by adding namespaced properties rather than requiring a new core component type immediately.** ([inference]; high confidence; source: https://raw.githubusercontent.com/CycloneDX/specification/master/schema/bom-1.7.schema.json; https://cyclonedx.org/specification/overview/)
2. **SPDX 3.0.1 already provides strong package-level coverage for models and datasets, but a complete agentic AIBOM still needs an extension profile because prompt, orchestration, and memory-schema artefacts are not first-class classes in the current AI profile.** ([fact]; high confidence; source: https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/; https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Classes/DatasetPackage/; https://spdx.github.io/spdx-spec/v3.0.1/model/Extension/Extension/)
3. **CycloneDX's own open issues show that AI service modelling, model dependency declaration, fixed hyperparameters, and future agent-card semantics remain unresolved, which is direct evidence that agentic schema design is still extension territory rather than settled standard practice.** ([fact]; medium confidence; source: https://github.com/CycloneDX/specification/issues/702; https://github.com/CycloneDX/specification/issues/268; https://github.com/CycloneDX/specification/issues/282)
4. **The minimal agentic extension should add only behaviour-shaping artefacts that can be stably identified at design time, model, prompt or instruction, retrieval snapshot, memory schema, tool manifest, and orchestration config, because that preserves NTIA-style practicality while closing the most important conceptual gaps.** ([inference]; medium confidence; source: https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-sbom-conceptual-gaps-theory.html)
5. **Mutability and fingerprinting should reuse existing hash, version, external-reference, and signature fields wherever possible, while a new `snapshotStrategy` property records whether an artefact is pinned by content hash, Merkle-tree digest, schema version, or external snapshot identifier.** ([inference]; medium confidence; source: https://raw.githubusercontent.com/CycloneDX/specification/master/schema/bom-1.7.schema.json; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html)
6. **Memory state and live retrieval results should not be part of the minimal declared AIBOM, because they are runtime-evidence surfaces, but the memory schema and retrieval snapshot policy must be declared so the runtime object can later be compared against approved design intent.** ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html; https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html)
7. **Execution binding is a first-class design concern, so a minimal AIBOM must declare whether each tool or context surface is identity-bound, policy-bound, or ambient, and it must reference the approval scope that constrains the declared tool path.** ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html; https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html)
8. **The most adoption-realistic path is a two-step standardization strategy, ship a CycloneDX 1.7 profile today with a lightweight AIBOM property taxonomy, then upstream the same semantics into an SPDX AIBOM extension profile as current AIBOM working-group efforts mature.** ([inference]; medium confidence; source: https://github.com/GenAI-Security-Project/aibom-generator; https://arxiv.org/abs/2504.16743; https://arxiv.org/abs/2510.07070)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] CycloneDX can serialize the minimal schema today through existing objects plus namespaced properties. | https://raw.githubusercontent.com/CycloneDX/specification/master/schema/bom-1.7.schema.json ; https://cyclonedx.org/specification/overview/ | high | Native extension surface exists |
| [fact] SPDX AI and Dataset profiles remain package-centric and need extension for prompt and orchestration artefacts. | https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/ ; https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Classes/DatasetPackage/ ; https://spdx.github.io/spdx-spec/v3.0.1/model/Extension/Extension/ | high | Strong normative model evidence |
| [fact] CycloneDX maintainers are still discussing AI service, dependency, hyperparameter, and agent-card gaps. | https://github.com/CycloneDX/specification/issues/702 ; https://github.com/CycloneDX/specification/issues/268 ; https://github.com/CycloneDX/specification/issues/282 | medium | Issue tracker, not ratified standard |
| [inference] The minimal extension surface should include model, prompt or instruction, retrieval snapshot, memory schema, tool manifest, and orchestration config. | https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-sbom-conceptual-gaps-theory.html | medium | Minimality judgement |
| [inference] `snapshotStrategy` is necessary because existing hash fields alone do not explain how mutable artefacts are pinned. | https://raw.githubusercontent.com/CycloneDX/specification/master/schema/bom-1.7.schema.json ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html | medium | Derived from mutable-context gap |
| [inference] Runtime memory state and live retrieval results belong in runtime AIBOM, not in the minimal declared schema. | https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html ; https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html | medium | Declared-versus-observed boundary |
| [inference] Context binding and approval-scope reference are required to make tool and retrieval surfaces governance-relevant at design time. | https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html ; https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html | medium | Cross-item synthesis |
| [inference] The best adoption path is CycloneDX property taxonomy now and SPDX extension profile next. | https://github.com/GenAI-Security-Project/aibom-generator ; https://arxiv.org/abs/2504.16743 ; https://arxiv.org/abs/2510.07070 | medium | Standards-process judgement |

### Assumptions

- **Assumption:** Producers can externalize prompt templates, tool manifests, and orchestration configurations into versioned artefacts rather than keeping them only as opaque application code. [assumption; source: https://github.com/GenAI-Security-Project/aibom-generator; https://github.com/CycloneDX/specification/issues/702] **Justification:** current AIBOM tooling and CycloneDX working-group discussions already assume extractable model and configuration metadata.
- **Assumption:** Namespaced AIBOM properties are an acceptable interim serialization strategy before the semantics become part of a formal shared profile. [assumption; source: https://raw.githubusercontent.com/CycloneDX/specification/master/schema/bom-1.7.schema.json; https://spdx.github.io/spdx-spec/v3.0.1/model/Extension/Extension/] **Justification:** both ecosystems expose explicit extension mechanisms for this style of incremental evolution.

### Analysis

The evidence supports a minimum-viable design that preserves existing BOM identity and dependency semantics while adding only the smallest new agentic layer needed to classify semantically active artefacts and their control meaning. [inference; source: https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom; https://raw.githubusercontent.com/CycloneDX/specification/master/schema/bom-1.7.schema.json; https://spdx.github.io/spdx-spec/v3.0.1/model/Extension/Extension/]
CycloneDX is operationally ahead for serialization flexibility, but SPDX is procedurally ahead for formal profile evolution, so the design should deliberately map one conceptual schema across both ecosystems rather than forcing one standard to behave like the other. [inference; source: https://github.com/CycloneDX/specification/issues/702; https://github.com/CycloneDX/specification/issues/268; https://github.com/CycloneDX/specification/issues/282; https://arxiv.org/abs/2510.07070]
The core trade-off is between design-time stability and runtime completeness: the minimal declared schema must stop at artefacts that can be approved and versioned before execution, while leaving live context, memory state, and retrieval results to a linked runtime AIBOM rather than overloading one artefact with both purposes. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html; https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html]
The resulting design is minimal not because it is short, but because every retained field answers one of six concrete questions, what class of artefact is this, how stable is it, how deterministic is it, how is it pinned, how is it bound to authority, and which approved operations does it enable. [inference; source: https://raw.githubusercontent.com/CycloneDX/specification/master/schema/bom-1.7.schema.json; https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/; https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Classes/DatasetPackage/]

```yaml
bomFormat: CycloneDX
specVersion: "1.7"
components:
  - bom-ref: model:gpt-4.1
    type: machine-learning-model
    name: gpt-4.1
    properties:
      - name: aibom:determinism
        value: stochastic
  - bom-ref: prompt:system
    type: data
    name: support-agent-system-prompt
    hashes:
      - alg: SHA-256
        content: 2b3f...deadbeef
    properties:
      - name: aibom:componentClass
        value: system-instruction
      - name: aibom:mutability
        value: versioned-mutable
      - name: aibom:snapshotStrategy
        value: content-hash
services:
  - bom-ref: service:crm
    name: crm-api
    properties:
      - name: aibom:contextBinding
        value: identity-bound
      - name: aibom:approvalScopeRef
        value: policy:crm-read-ticket-update
formulation:
  - workflows:
      - name: support-triage
        properties:
          - name: aibom:componentClass
            value: agent-configuration
```

### Risks, Gaps, and Uncertainties

- CycloneDX agent-card semantics are still open working-group territory, so any current `aibom:componentClass=agent-configuration` convention is an interim design rather than a ratified standard field. [fact; source: https://github.com/CycloneDX/specification/issues/702]
- SPDX extension mechanics are clear at the namespace level, but this item does not yet specify a fully formal AIBOM extension ontology with machine-readable class definitions. [fact; source: https://spdx.github.io/spdx-spec/v3.0.1/model/Extension/Extension/]
- Retrieval snapshot digest design remains partly unsettled because different vector stores and indexing pipelines expose different levels of reproducible corpus identity. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html]
- Practical tool support is currently model-centred, so prompt, memory-schema, and tool-manifest extraction workflows may lag the schema until practice implementations catch up. [inference; source: https://github.com/GenAI-Security-Project/aibom-generator; https://owaspaibom.org/]

### Open Questions

- Should future standards define a first-class `agent-configuration` object, or is a property-taxonomy approach sufficient if formulation workflows are already available? [inference; source: https://github.com/CycloneDX/specification/issues/702; https://arxiv.org/abs/2510.07070]
- What is the most reproducible digest method for heterogeneous RAG indexes that mix raw source files, chunking parameters, embeddings, and ranking metadata? [inference; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html]
- Should approval-scope references point to external policy objects only, or should BOM-native permission manifests become first-class cross-standard objects? [inference; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html]

---

## Output

- Type: knowledge
- Description: A standards-aligned minimal AIBOM schema proposal for agentic workloads, including a CycloneDX 1.7 serialization strategy, an SPDX extension path, and a worked schema example. [inference; source: https://raw.githubusercontent.com/CycloneDX/specification/master/schema/bom-1.7.schema.json; https://spdx.github.io/spdx-spec/v3.0.1/model/Extension/Extension/; https://arxiv.org/abs/2510.07070]
- Links:
  - https://raw.githubusercontent.com/CycloneDX/specification/master/schema/bom-1.7.schema.json
  - https://spdx.github.io/spdx-spec/v3.0.1/model/AI/Classes/AIPackage/
  - https://arxiv.org/abs/2510.07070
