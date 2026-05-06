---
title: "How can a runtime-observed AI Bill of Materials (AIBOM) be generated for an agentic AI system — and how much does it diverge from the declared design-time AIBOM?"
added: 2026-05-06T08:52:41+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: [2026-05-06-aibom-runtime-capture-opentelemetry-practice]  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [agentic-ai, security, observability, llm, governance, runtime-monitoring]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
cites: [2026-05-06-aibom-sbom-conceptual-gaps-theory, 2026-04-26-ai-lowcode-observability-telemetry-governance]
related: [2026-05-06-aibom-sbom-conceptual-gaps-theory, 2026-05-06-aibom-runtime-capture-opentelemetry-practice, 2026-05-06-aibom-schema-design-standards-alignment, 2026-05-06-aibom-platform-observability-control-comparison]
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# How can a runtime-observed AI Bill of Materials (AIBOM) be generated for an agentic AI system — and how much does it diverge from the declared design-time AIBOM?

## Research Question

How can a dynamic, runtime-observed AI Bill of Materials (AIBOM) be generated for an agentic AI system — capturing execution traces, transient Retrieval-Augmented Generation (RAG) retrievals, tool call outputs, and memory state at decision points — and what formal models describe the divergence between a declared design-time AIBOM and what actually executes at inference time?

## Scope

**In scope:**
- Theoretical models for runtime AIBOM generation: event sourcing analogies, execution trace schemas, causality graph capture
- What constitutes "ground truth" for a non-deterministic agent run: snapshots vs. full causality graphs vs. aggregated statistical representations
- Divergence taxonomy: classifying the types of divergence between declared and observed AIBOM (schema drift, version drift, tool scope expansion, RAG retrieval variation, memory state divergence)
- Replayability analysis: which parts of an agent run can be replayed deterministically, which cannot, and what that means for auditability
- Analogies from distributed systems tracing (OpenTelemetry semantic conventions) and event sourcing patterns that can be adapted for AIBOM
- Academic literature on runtime attestation and provenance tracking for AI

**Out of scope:**
- Platform-specific tooling implementations (covered in `2026-05-06-aibom-runtime-capture-opentelemetry-practice`)
- Schema design for the declared AIBOM (covered in `2026-05-06-aibom-schema-design-standards-alignment`)
- Identity and attribution modelling (covered in `2026-05-06-aibom-identity-delegation-trust-theory`)

**Constraints:**
- Focus on formal/conceptual modelling; treat specific platform APIs as examples only
- Must address stochastic behaviour explicitly — do not assume determinism as a simplifying condition
- Recency: field is moving fast; prefer 2023+ sources

## Context

A declared AIBOM describes what an agentic system is configured to use; a runtime AIBOM describes what it actually used during a specific execution. These two representations will always diverge to some degree — RAG retrieves different chunks on each call, tool APIs return varying results, memory state accumulates — and that divergence is precisely where the most consequential risks live (RAG poisoning, tool substitution, model drift). Before building runtime AIBOM capture tooling, the field needs formal models of: (1) what a runtime AIBOM should capture, (2) how divergence should be represented and measured, and (3) what "good enough" looks like for security and governance purposes. This item builds on the conceptual analysis in `2026-05-06-aibom-sbom-conceptual-gaps-theory` and directly informs the practice item `2026-05-06-aibom-runtime-capture-opentelemetry-practice`.

## Approach

1. **Runtime AIBOM capture model:** Define what events, at what granularity, constitute a complete runtime AIBOM for one agent execution cycle. Model this as an event stream and identify the minimum required event types (model invocation, tool call, RAG retrieval, memory read/write, external API call).

2. **Ground truth problem:** Analyse the epistemological challenge of defining "ground truth" for a non-deterministic run. Compare: (a) snapshot at decision points, (b) full causality graph with all inputs/outputs, (c) statistical summary across multiple runs. Evaluate each against auditability, storage cost, and reproducibility requirements.

3. **Divergence taxonomy:** Construct a taxonomy of declared-vs-observed AIBOM divergence types. For each type, define: trigger (what causes it), detection method, security relevance, and governance response.

4. **Replayability analysis:** Assess which components of an agent run can be recorded and replayed deterministically (tool call inputs, model prompt) vs. which are inherently non-reproducible (model sampling, external API state). Evaluate implications for incident response and forensic auditing.

5. **Distributed systems analogies:** Map OpenTelemetry trace concepts (span, parent span, trace context) and event sourcing concepts (event, aggregate, projection) onto the runtime AIBOM model to identify reusable patterns and gaps.

## Sources

- [ ] [OpenTelemetry Specification — Semantic Conventions for Generative AI](https://opentelemetry.io/docs/specs/semconv/gen-ai/) — OpenTelemetry semantic conventions for Large Language Model (LLM) spans; the most mature industry standard for runtime AI trace capture
- [ ] [OpenTelemetry Project](https://opentelemetry.io/) — umbrella specification for distributed tracing, metrics, and logs that forms the substrate for runtime AIBOM capture
- [ ] [Yona et al. (2024) Toward a Framework for Agentic AI Provenance](https://arxiv.org/abs/2407.01392) — academic framework for provenance tracking specifically addressing non-deterministic agentic executions
- [ ] [AWS Bedrock Agent Trace Events](https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html) — AWS documentation for Bedrock agent execution traces; primary example of what production runtime trace data looks like
- [ ] [Fowler (2005) Event Sourcing Pattern](https://martinfowler.com/eaaDev/EventSourcing.html) — foundational description of event sourcing; relevant as a design pattern analogy for runtime AIBOM capture
- [ ] [Mödinger et al. (2024) Provenance-Aware Machine Learning Systems](https://arxiv.org/abs/2404.10209) — academic survey of provenance tracking in machine learning pipelines; directly relevant to runtime AIBOM generation models
- [ ] [National Institute of Standards and Technology (NIST) AI Risk Management Framework — Govern Function](https://www.nist.gov/system/files/documents/2023/01/26/AI%20RMF%201.0.pdf) — NIST AI RMF governance requirements that runtime AIBOMs must satisfy

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
