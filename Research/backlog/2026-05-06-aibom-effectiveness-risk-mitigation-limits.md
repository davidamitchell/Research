---
title: "What security and governance risks can an AI Bill of Materials (AIBOM) realistically mitigate for agentic AI workloads — and where does it create false assurance?"
added: 2026-05-06T08:52:41+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: medium  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [agentic-ai, security, governance, supply-chain, llm, ai-governance, risk]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
cites: [2026-05-06-aibom-sbom-conceptual-gaps-theory, 2026-05-06-aibom-schema-design-standards-alignment, 2026-05-06-aibom-runtime-generation-divergence-theory, 2026-05-06-aibom-identity-delegation-trust-theory, 2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain]
related: [2026-05-06-aibom-sbom-conceptual-gaps-theory, 2026-05-06-aibom-schema-design-standards-alignment, 2026-05-06-aibom-runtime-generation-divergence-theory, 2026-05-06-aibom-identity-delegation-trust-theory, 2026-05-06-aibom-declared-construction-practice, 2026-05-06-aibom-runtime-capture-opentelemetry-practice, 2026-05-06-aibom-platform-observability-control-comparison, 2026-05-06-aibom-regulatory-eu-ai-act-intersection]
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# What security and governance risks can an AI Bill of Materials (AIBOM) realistically mitigate for agentic AI workloads — and where does it create false assurance?

## Research Question

What categories of security and governance risk can an AI Bill of Materials (AIBOM) — both declared design-time and runtime-observed variants — realistically mitigate for agentic AI workloads, what metrics can quantify that mitigation, and where does an apparently complete AIBOM create dangerous false assurance by leaving behavioural, inferential, and emergent risks invisible?

## Scope

**In scope:**
- Structural risk mitigation: dependency graph vulnerabilities, known-compromised component detection, version drift alerts — analogous to SBOM (Software Bill of Materials) use cases
- Behavioural risk visibility gaps: prompt injection, tool misuse, Retrieval-Augmented Generation (RAG) poisoning, and runtime manipulation that bypass even a complete AIBOM
- Drift risk categories: model version drift, RAG knowledge base staleness, external tool API changes, memory corruption — and which are detectable via AIBOM vs. invisible
- False assurance scenarios: red-team exercises documenting how an attacker can fully compromise an agentic system despite a valid, up-to-date AIBOM
- Metric proposals: percentage of runtime dependencies captured, drift detection latency, risk signal accuracy rate, reproducibility fidelity score, blast radius reduction from AIBOM-informed controls
- Inference opacity: the fundamental limits on what can be known about a model's reasoning process regardless of AIBOM completeness

**Out of scope:**
- Platform-specific implementation details (covered in the practice items)
- Regulatory compliance obligations (covered in `2026-05-06-aibom-regulatory-eu-ai-act-intersection`)
- AIBOM schema design (covered in `2026-05-06-aibom-schema-design-standards-alignment`)

**Constraints:**
- Must distinguish clearly between structural risks (where AIBOM helps) and behavioural/inferential risks (where it does not)
- Red-team scenarios must be sourced or grounded in documented attack patterns — not hypothetical
- Must build on findings from the theory and practice items in this series; this item synthesises across them

## Context

AIBOM investment is only justified if the security and governance value is clear and quantified. There is a risk that organisations invest heavily in AIBOM generation and achieve structural supply chain transparency while remaining exposed to the behavioural and emergent risks that actually dominate agentic AI threat models — prompt injection, RAG poisoning, tool substitution, emergent capability use. Understanding the exact boundary between "what AIBOM helps with" and "what AIBOM cannot help with" is critical for calibrating investment, setting appropriate operator expectations, and identifying where complementary controls (runtime guardrails, red-teaming, behavioural monitoring) are essential. This item synthesises across the series and is intended to produce actionable guidance for security teams considering AIBOM adoption.

## Approach

1. **Risk taxonomy and AIBOM coverage mapping:** Build a structured taxonomy of agentic AI security and governance risks (drawing on the prior security threat model in `2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain`). For each risk category, assess: does AIBOM provide (a) full visibility, (b) partial visibility, (c) no visibility, or (d) active false assurance?

2. **Structural risk mitigation analysis:** Document in detail where AIBOM genuinely reduces risk — component vulnerability detection, version pinning enforcement, dependency graph anomaly detection. Estimate the blast radius reduction achievable.

3. **False assurance scenarios:** Document concrete scenarios where a complete, well-formed AIBOM provides false assurance. Specifically: (a) prompt injection succeeds despite a valid AIBOM because the injected instruction is not a "component", (b) RAG poisoning succeeds because the knowledge base version has not changed, (c) emergent tool misuse occurs because the tool was legitimately declared.

4. **Inference opacity boundary:** Analyse where the fundamental opacity of neural network inference creates an irreducible visibility gap that no AIBOM schema can address — and what this means for governance frameworks that depend on complete explainability.

5. **Metric proposals:** Define a minimal set of metrics that quantify AIBOM effectiveness: (a) runtime dependency capture rate, (b) drift detection latency (time from state change to alert), (c) blast radius reduction (quantified by attack surface reduction from version-pinned components), (d) AIBOM coverage completeness score. Identify what baseline data is required to compute each.

## Sources

- [ ] [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — OWASP LLM Top 10; the most authoritative categorisation of LLM security risks; used to anchor the risk taxonomy
- [ ] [NIST AI Risk Management Framework 1.0](https://www.nist.gov/system/files/documents/2023/01/26/AI%20RMF%201.0.pdf) — NIST AI RMF governance framework; reference for governance risk categories and measurement requirements
- [ ] [Greshake et al. (2023) Not What You Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/abs/2302.12173) — seminal academic paper on indirect prompt injection attacks; provides concrete false-assurance scenario where AIBOM provides no protection
- [ ] [Perez & Ribeiro (2022) Ignore Previous Prompt: Attack Techniques For Language Models](https://arxiv.org/abs/2211.09527) — academic paper documenting prompt injection techniques that bypass static inventory controls
- [ ] [Microsoft Threat Model for Agentic AI](https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/) — Microsoft security team's taxonomy of agentic AI failure modes; reference for structural vs behavioural risk boundary
- [ ] [Anthropic Model Card — Claude](https://www.anthropic.com/model-card) — Anthropic model card; example of what inference opacity disclosure currently looks like and what remains undisclosed
- [ ] [National Telecommunications and Information Administration (NTIA) SBOM Framing Working Group — Use Cases](https://www.ntia.gov/files/ntia/publications/sbom_use_cases_roles_benefits_nov2019.pdf) — NTIA SBOM use cases; baseline for mapping which SBOM value propositions transfer to AIBOM and which do not

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
