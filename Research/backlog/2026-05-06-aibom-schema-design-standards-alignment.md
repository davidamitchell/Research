---
title: "What is the minimal viable schema for an AI Bill of Materials (AIBOM) for agentic workloads — how should it align with CycloneDX and SPDX standards, and what new property types are required?"
added: 2026-05-06T08:52:41+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: [2026-05-06-aibom-declared-construction-practice]  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [agentic-ai, security, supply-chain, governance, llm, ai-governance]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
cites: [2026-05-06-aibom-sbom-conceptual-gaps-theory, 2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain]
related: [2026-05-06-aibom-sbom-conceptual-gaps-theory, 2026-05-06-aibom-declared-construction-practice, 2026-05-06-aibom-runtime-generation-divergence-theory, 2026-05-06-aibom-effectiveness-risk-mitigation-limits]
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# What is the minimal viable schema for an AI Bill of Materials (AIBOM) for agentic workloads — how should it align with CycloneDX and SPDX standards, and what new property types are required?

## Research Question

What is the minimal viable set of schema properties required to describe agentic Artificial Intelligence (AI) system dependencies in a useful, standards-aligned AI Bill of Materials (AIBOM) — specifically, how should existing CycloneDX Machine Learning Bill of Materials (ML-BOM) and SPDX 3.0 AI profile schema be extended to represent deterministic vs. non-deterministic components, mutable vs. immutable dependencies (prompts, Retrieval-Augmented Generation (RAG) indexes, memory), and identity-bound vs. ambient execution contexts?

## Scope

**In scope:**
- Analysis of CycloneDX ML-BOM and CycloneDX Agent BOM proposal schema fields and their applicability to agentic components
- Analysis of SPDX 3.0 AI and Dataset profiles for agentic AI coverage
- Proposed schema extensions for component types not covered: prompts/system instructions, RAG knowledge base snapshots, memory schemas, tool permission scope manifests, model configuration (temperature, sampling parameters, context window)
- Versioning and fingerprinting strategies for mutable components (prompt hash, RAG index digest, memory schema version)
- Property type design: deterministic vs. non-deterministic flag, mutability classification, execution context binding
- Comparative analysis of any existing academic AIBOM schema proposals

**Out of scope:**
- Runtime/observed AIBOM (covered in `2026-05-06-aibom-runtime-generation-divergence-theory` and `2026-05-06-aibom-runtime-capture-opentelemetry-practice`)
- Platform-specific schema extraction implementations (covered in `2026-05-06-aibom-declared-construction-practice`)
- Identity and attribution schema (covered in `2026-05-06-aibom-identity-delegation-trust-theory`)

**Constraints:**
- Must evaluate against at least two existing standards (CycloneDX and SPDX) rather than proposing an entirely new schema from scratch
- Source documentation for standards must be current (2023 or later)
- Practical feasibility of schema properties must be assessed — do not propose properties that cannot be populated from accessible artefacts

## Context

The SBOM (Software Bill of Materials) ecosystem has converged around CycloneDX and SPDX as the dominant standards. Any AIBOM schema that cannot map to or extend one of these formats faces adoption friction and tooling incompatibility. At the same time, agentic AI systems introduce dependency types — prompts, RAG knowledge bases, memory schemas — that neither standard adequately models today. This item defines what a well-formed, minimally useful AIBOM schema looks like, grounding the answer in the actual CycloneDX and SPDX extension mechanisms. It builds on the conceptual gap analysis in `2026-05-06-aibom-sbom-conceptual-gaps-theory` and produces the schema design that the practice item `2026-05-06-aibom-declared-construction-practice` will implement against a real platform.

## Approach

1. **Standards survey:** Map all existing CycloneDX ML-BOM fields and SPDX 3.0 AI profile fields to the agentic component taxonomy from `2026-05-06-aibom-sbom-conceptual-gaps-theory`. Identify which components have adequate coverage and which have none.

2. **Gap property design:** For each component with inadequate coverage, design a minimal schema extension: property name, type, cardinality, allowed values, and a worked example. Assess whether the extension fits within CycloneDX's `properties` extension mechanism or requires a new component type in the specification.

3. **Mutability and versioning model:** Design a versioning and fingerprinting scheme for mutable components. Evaluate: SHA-256 hash of prompt text, Merkle-tree digest of RAG index, semantic version of memory schema, cryptographic signature of system instruction artefact.

4. **Execution context binding:** Assess how to represent the binding between an agent identity (or execution context) and its declared component set — i.e. how the AIBOM declares "this agent instance runs with these specific prompt, model, tool, and memory versions".

5. **Schema proposal:** Write a minimal viable AIBOM schema as a JSON or YAML example extending CycloneDX ML-BOM, covering at minimum: model, prompt/system instruction, tool manifest, RAG knowledge base reference, memory schema reference, and agent orchestration configuration.

## Sources

- [ ] [CycloneDX ML-BOM Specification](https://cyclonedx.org/capabilities/mlbom/) — current CycloneDX specification for machine learning components; baseline for extension proposals
- [ ] [CycloneDX Agent BOM Proposal (GitHub)](https://github.com/CycloneDX/cyclonedx-specification/issues) — active GitHub discussions on agent-specific BOM extensions in the CycloneDX community
- [ ] [SPDX 3.0 Specification](https://spdx.github.io/spdx-spec/v3.0/) — current SPDX specification including AI and Dataset profiles
- [ ] [OWASP AIBOM Generator Project](https://owasp.org/www-project-aibom-generator/) — OWASP community project developing practical AIBOM generation tooling and schema guidance
- [ ] [Yona et al. (2024) Toward a Framework for Agentic AI Provenance](https://arxiv.org/abs/2407.01392) — academic proposal covering provenance and schema considerations for agentic AI systems
- [ ] [National Telecommunications and Information Administration (NTIA) Minimum Elements for an SBOM](https://www.ntia.gov/report/2021/minimum-elements-software-bill-of-materials-sbom) — NTIA SBOM minimum elements; reference point for "minimum viable" concept applied to AIBOM
- [ ] [Lin et al. (2024) AIBOM: Towards a Standard Bill of Materials for AI Systems](https://arxiv.org/abs/2404.01089) — academic paper directly proposing an AIBOM schema and minimum element set

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

Restate the research question. Confirm scope, constraints, and output format.

-

### §1 Question Decomposition

Approach sub-questions broken into atomic questions — each answerable with a single evidence-based claim.

-

### §2 Investigation

Evidence gathered per atomic question. Label each claim: **[fact]**, **[inference]**, or **[assumption]** with source.

-

### §3 Reasoning

Facts, inferences, and assumptions explicitly separated. No unsupported generalisations or narrative leaps.

-

### §4 Consistency Check

Internal contradictions identified and resolved (or explicitly flagged where unresolvable).

-

### §5 Depth and Breadth Expansion

Findings re-examined through relevant lenses (technical, regulatory, economic, historical, behavioural).

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

Final pass: every section justified, all threads synthesised, every claim sourced or labelled, all uncertainties explicit.

-

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

3–5 sentences. What is the answer to the research question? State the key conclusion directly. Write plain prose — no prefix labels. Bind sources as trailing inline citations: `Claim text. [inference; source: https://url]`

### Key Findings

Ordered list. Each finding is a specific, evidence-backed claim with confidence and source as a trailing parenthetical. Use **suffix style** — source at the end of the claim, not at the beginning.

1. **Claim text as a complete sentence.** (high confidence; source: https://url)
2. **Claim text as a complete sentence.** (medium confidence; source: https://url1; https://url2)

Source URLs must exactly match URLs in the `## Sources` section so the generated site can render `Author (Year)` citation links. List the primary source URL(s) from `## Sources` here.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

Explicit assumptions made during the investigation and the justification for each.

- **Assumption:** ... **Justification:** ...

### Analysis

How the evidence was weighed, what trade-offs were identified, and how competing interpretations were resolved.

### Risks, Gaps, and Uncertainties

What is still unknown? Where does the evidence fall short? What could change the conclusion?

-

### Open Questions

Questions that surfaced during research but are out of scope for this item. Each may become a new backlog item.

-

---

## Output

*(Fill in when completing — what was produced as a result of this research?)*

- Type: # skill | tool | agent | knowledge | backlog-item
- Description:
- Links:
