---
title: "Why does Software Bill of Materials (SBOM) fail as a complete inventory model for agentic Artificial Intelligence workloads — and what new conceptual abstractions are required?"
added: 2026-05-06T08:52:41+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: [2026-05-06-aibom-schema-design-standards-alignment, 2026-05-06-aibom-runtime-generation-divergence-theory, 2026-05-06-aibom-declared-construction-practice]  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [agentic-ai, security, supply-chain, governance, llm, ai-governance]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
cites: [2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain]
related: [2026-05-06-aibom-schema-design-standards-alignment, 2026-05-06-aibom-runtime-generation-divergence-theory, 2026-05-06-aibom-declared-construction-practice, 2026-05-06-aibom-effectiveness-risk-mitigation-limits]
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# Why does Software Bill of Materials (SBOM) fail as a complete inventory model for agentic Artificial Intelligence workloads — and what new conceptual abstractions are required?

## Research Question

Why do traditional Software Bill of Materials (SBOM) concepts fail to adequately describe the dependency, provenance, and runtime composition of agentic Artificial Intelligence (AI) systems — and what fundamentally new abstractions (graph structures, mutable dependency types, non-deterministic component representations) are required in an AI Bill of Materials (AIBOM) to close those gaps?

## Scope

**In scope:**
- Analysis of what SBOM was designed to capture and where those assumptions break for agentic AI workloads
- Identification of component types unique to agentic AI: prompts, system instructions, Retrieval-Augmented Generation (RAG) indexes, memory schemas, tool permission scopes, model weights, inference configurations
- Mutable vs. immutable dependency distinctions — how agentic AI introduces dependencies that change at runtime (RAG retrievals, memory state, tool outputs) with no analogue in traditional software supply chains
- Non-deterministic output as a supply chain property — stochastic model outputs that cannot be versioned like compiled binaries
- Graph-based representations: whether a flat component list is adequate or whether agentic flows require directed graphs (agent → tool → RAG → memory)
- Review of existing academic and industry literature on AIBOM conceptual framing

**Out of scope:**
- Implementation of any AIBOM tooling (covered in practice-focused backlog items)
- Deep dive into specific platform capabilities (covered in `2026-05-06-aibom-platform-observability-control-comparison`)
- Regulatory compliance obligations (covered in `2026-05-06-aibom-regulatory-eu-ai-act-intersection`)

**Constraints:**
- Focus on conceptual and theoretical analysis; treat implementations only as illustrative examples
- Primary sources preferred: academic papers, standards body working drafts, specification documents

## Context

SBOM has proven effective for static software supply chains: it describes versioned, immutable artefacts in a dependency graph that can be scanned against known vulnerability databases. Agentic AI systems violate multiple core SBOM assumptions simultaneously — dependencies change at inference time (RAG retrieval), outputs are non-deterministic, prompts and instructions are semantically loaded and lack standard versioning schemes, and execution flows are not fully determined at design time. Understanding precisely where and why SBOM breaks is the prerequisite for designing an AIBOM schema that actually captures the properties that matter for security, governance, and auditability. This item builds on prior research into AI security threat modelling (`2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain`) and produces the conceptual foundation for subsequent schema design and practice items.

## Approach

1. **SBOM foundational assumptions audit:** Document the core design assumptions of SBOM (static artefacts, versioned components, deterministic builds, directed acyclic dependency graphs) and trace them through NTIA minimum elements, CycloneDX, and SPDX specifications.

2. **Agentic AI component taxonomy:** Enumerate the distinct component types present in a representative agentic AI workflow (model, prompt/system instruction, RAG knowledge base, tool/function, memory schema, agent orchestration logic, external API) and classify each by mutability, determinism, and versioning feasibility.

3. **SBOM failure mode analysis:** For each agentic component type, identify which SBOM assumptions it violates and what the security/governance consequence of that gap is (e.g. a poisoned RAG index is invisible to a static SBOM scan).

4. **Graph structure adequacy assessment:** Evaluate whether a flat component list or a directed component graph better captures agentic execution flows, drawing on academic proposals for agentic AIBOM graph representations.

5. **New abstraction requirements:** Synthesise findings into a list of conceptual requirements for an AIBOM: what new property types, relationship types, and temporal representations are needed beyond standard SBOM schema.

## Sources

- [ ] [National Telecommunications and Information Administration (NTIA) Minimum Elements for a Software Bill of Materials](https://www.ntia.gov/report/2021/minimum-elements-software-bill-of-materials-sbom) — defines the foundational NTIA SBOM minimum elements that agentic AI must be measured against
- [ ] [CycloneDX Machine Learning Bill of Materials (ML-BOM) Specification](https://cyclonedx.org/capabilities/mlbom/) — CycloneDX extension for machine learning components; baseline for AIBOM extension proposals
- [ ] [SPDX 3.0 AI Profile](https://spdx.github.io/spdx-spec/v3.0/) — SPDX specification v3.0 including AI and dataset profiles
- [ ] [OWASP AIBOM Generator Project](https://owasp.org/www-project-aibom-generator/) — OWASP initiative specifically targeting AI Bill of Materials generation; most current community-developed approach
- [ ] [Bommasani et al. (2021) On the Opportunities and Risks of Foundation Models](https://arxiv.org/abs/2108.07258) — Stanford Center for Research on Foundation Models (CRFM) paper documenting emergent behaviours and supply chain implications of large foundation models
- [ ] [National Institute of Standards and Technology (NIST) AI Risk Management Framework](https://www.nist.gov/system/files/documents/2023/01/26/AI%20RMF%201.0.pdf) — NIST AI RMF 1.0; governance framework that motivates AIBOM as an inventory and risk management tool
- [ ] [Yona et al. (2024) Toward a Framework for Agentic AI Provenance](https://arxiv.org/abs/2407.01392) — academic proposal for provenance tracking in agentic AI systems; directly addresses AIBOM gaps

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
