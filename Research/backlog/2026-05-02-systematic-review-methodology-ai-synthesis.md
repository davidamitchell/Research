---
title: "What systematic review methodologies and AI-assisted synthesis tool architectures are most appropriate for cross-item synthesis of a growing file-based research corpus, and what design prevents hallucination and claim conflation across source items?"
added: 2026-05-02T06:11:10+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [agentic-ai, llm, workflow, research-tooling, knowledge-graph, evaluation]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
cites: []
related: [2026-03-03-cross-item-synthesis-meta-insights, 2026-03-12-exploration-synthesis-gap, 2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis, 2026-04-27-uelgf-synthesis-complete-framework]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# What systematic review methodologies and AI-assisted synthesis tool architectures are most appropriate for cross-item synthesis of a growing file-based research corpus, and what design prevents hallucination and claim conflation across source items?

## Research Question

What systematic review methodologies (Preferred Reporting Items for Systematic reviews and Meta-Analyses (PRISMA), Cochrane review, narrative synthesis, meta-ethnography, realist synthesis) and AI-assisted knowledge synthesis tool architectures are most appropriate for producing accurate, provenance-preserving cross-item synthesis from a growing file-based research corpus of ~200 items managed by AI agents — specifically: what synthesis methodology prevents hallucination and claim conflation across source items, what provenance-linking mechanism ensures each synthesis claim traces to specific source items, and what workflow design (GitHub Actions `workflow_dispatch`, agent prompt, output directory structure) best delivers a `synthesis-prompt.md` and `synthesis-loop.yml` implementation for W-0051?

## Scope

**In scope:**
- Systematic review methodologies: PRISMA (Preferred Reporting Items for Systematic reviews and Meta-Analyses) reporting standard, Cochrane review protocol, narrative synthesis, meta-ethnography, and realist synthesis — their core steps and applicability to LLM-based synthesis
- AI-assisted synthesis tools: STORM synthesis pipeline, LlamaIndex summary index, Langchain map-reduce, Elicit AI (systematic review assistant), Consensus (evidence synthesis AI) — architecture and hallucination prevention mechanisms
- Provenance-linking: how synthesis claims trace back to specific source items (cites: field, inline references, evidence map); what minimum provenance record is required for a synthesis item to be auditable
- Hallucination prevention: retrieval-augmented generation (RAG) with source-grounded generation, citation verification steps, and contradiction detection across source items
- Contradiction detection: how conflicting findings across source items should be handled (flagged, excluded, resolved with reasoning)
- Workflow design: `synthesis-loop.yml` trigger design (manual `workflow_dispatch` only, never scheduled), input parameters (source_items: comma-separated slugs, synthesis_question), and output directory structure (`Knowledge/`)
- `synthesis-prompt.md` structure: analogous to `research-prompt.md` but for multi-item synthesis — §§ structure, perspective requirements, citation requirements

**Out of scope:**
- Quantitative meta-analysis (statistical pooling of effect sizes) — not applicable to qualitative/mixed-methods corpus
- Full-text semantic search index (covered by W-0025 deferred item)
- Automated source item selection (manual input of source_items required for synthesis)
- Authoring workflow (papers and frameworks — covered by W-0052)

**Constraints:**
- Expand all acronyms on first use
- The synthesis workflow must never run on schedule — only `workflow_dispatch` (owner-initiated)
- Each synthesis claim must be traceable to at least one source item slug
- Implementation language is Python 3.11+ for any scripting; GitHub Actions for the workflow

## Context

W-0051 in `BACKLOG.md` proposes a synthesis workflow to produce `Knowledge/` items that integrate findings across multiple primary research items. The BACKLOG item specifies the structural outcome (`Knowledge/` directory, `synthesis-prompt.md`, `synthesis-loop.yml`) but not the methodology — specifically: what systematic review methodology prevents hallucination and claim conflation, and what provenance-linking mechanism ensures synthesis claims are traceable. This research item grounds those design decisions in evidence from systematic review methodology and AI-assisted synthesis tool architectures before W-0051 implementation begins.

## Approach

1. **Systematic review methodology survey**: Review PRISMA, Cochrane protocols, narrative synthesis, meta-ethnography, and realist synthesis; identify core steps (inclusion/exclusion criteria, data extraction, synthesis, quality assessment) and assess which are adaptable to LLM-based automated synthesis.
2. **AI-assisted synthesis tool architecture review**: Study STORM's synthesis pipeline, LlamaIndex document summary index, Langchain map-reduce, Elicit AI, and Consensus; document how each prevents hallucination and conflation, and what provenance-linking mechanisms they use.
3. **Hallucination prevention evidence**: Search for empirical studies on LLM hallucination in multi-document synthesis; identify which architectural choices (RAG grounding, citation verification, abstractive vs extractive summarisation) most reliably reduce cross-item claim conflation.
4. **Provenance-linking design**: Define the minimum provenance record for a synthesis claim (source item slug, claim label, evidence quote or reference); assess whether inline citations, a `cites:` frontmatter field, and an evidence map table together satisfy auditability requirements.
5. **Contradiction detection design**: Define how conflicting findings across source items should be identified (LLM comparison, frontmatter contradiction field) and handled in the synthesis output (flagged as tension, excluded with reasoning, resolved with explanation).
6. **Workflow and prompt structure design**: Propose `synthesis-loop.yml` trigger, input parameters, and `synthesis-prompt.md` §§ structure; compare against `research-prompt.md` to identify shared patterns and differences.
7. **Architecture Decision Record (ADR) identification**: Identify which design decisions warrant ADRs before W-0051 implementation.

## Sources

- [ ] [Page et al. (2021) PRISMA 2020 explanation and elaboration: updated guidance and exemplars for reporting systematic reviews](https://www.bmj.com/content/372/bmj.n160) — PRISMA reporting standard for systematic reviews; core methodology steps
- [ ] [Cochrane Handbook for Systematic Reviews of Interventions (2023)](https://training.cochrane.org/handbook) — Cochrane protocol for data extraction, synthesis, and quality assessment
- [ ] [Shao et al. (2024) Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models (STORM)](https://arxiv.org/abs/2402.14207) — STORM synthesis pipeline; multi-perspective evidence integration
- [ ] [LlamaIndex documentation — Multi-Document Agents](https://docs.llamaindex.ai/en/stable/examples/agent/multi_document_agents/) — LlamaIndex architecture for cross-document synthesis with provenance
- [ ] [Elicit AI — Systematic Review Assistant](https://elicit.com/) — AI-assisted systematic review tool; evidence extraction and synthesis approach
- [ ] [Maynard et al. (2005) Qualitative Methods in Social Research — Narrative Synthesis Guidance](https://www.york.ac.uk/media/crd/Narrative_Synthesis_Guidance.pdf) — narrative synthesis methodology for qualitative cross-study integration

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

-

### §1 Question Decomposition

-

### §2 Investigation

-

### §3 Reasoning

-

### §4 Consistency Check

-

### §5 Depth and Breadth Expansion

-

### §6 Synthesis

**Executive summary:**

**Key findings:**

**Evidence map:**

**Assumptions:**

**Analysis:**

**Risks, gaps, uncertainties:**

**Open questions:**

### §7 Recursive Review

-

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

### Key Findings

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

### Analysis

### Risks, Gaps, and Uncertainties

-

### Open Questions

-

---

## Output

*(Fill in when completing — what was produced as a result of this research?)*

- Type: # skill | tool | agent | knowledge | backlog-item
- Description:
- Links:
