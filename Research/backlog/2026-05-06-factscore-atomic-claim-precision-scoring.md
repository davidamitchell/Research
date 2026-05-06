---
title: "What is FActScore, how does it compute precision scores for atomic factual claims in language model outputs, and what are the implications for automated quality scoring of research items in this repository?"
added: 2026-05-06T09:03:23+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [fact-checking, hallucinations, evaluation, research-quality, llm]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
cites: []          # slugs of items this item directly depends on or quotes
related: [2026-05-06-openfactcheck-automated-fact-verification, 2026-05-02-automated-claim-verification-academic-literature, 2026-03-05-llm-hallucination-mechanisms]
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# What is FActScore, how does it compute precision scores for atomic factual claims in language model outputs, and what are the implications for automated quality scoring of research items in this repository?

## Research Question

What is FActScore (Factuality Assessment at Claim Granularity), developed at the University of Washington, how does it decompose Large Language Model (LLM) outputs into atomic claims and compute a precision score against a knowledge source, and what are the practical implications for implementing a quantitative factual quality score for completed research items in this repository?

## Scope

**In scope:**
- FActScore's core methodology: atomic claim decomposition, knowledge source selection, precision calculation, and aggregation
- Published accuracy and inter-annotator agreement results from the original University of Washington paper
- FActScore's retrieval-augmented verification approach and its dependency on a knowledge corpus
- How FActScore's atomic claim precision aligns with the `[fact]` / `[inference]` / `[assumption]` labelling convention in this repository's research item template
- Integration feasibility: Python package, API, compute requirements, and open-source licence
- Limitations: entity bias, knowledge cutoff sensitivity, claim granularity calibration

**Out of scope:**
- Building a custom FActScore variant (in scope only if the feasibility assessment is positive)
- Coverage recall metrics (FActScore measures precision only — recall is a separate problem)
- General LLM hallucination survey (addressed in related items)

**Constraints:**
- Primary source is the original University of Washington paper and the official GitHub repository
- Accuracy figures must be drawn from reproducible evaluations with named benchmarks
- Applicability assessment must be grounded in the actual research item format used in this repo

## Context

This repository's research items require every factual claim to be labelled `[fact]`, `[inference]`, or `[assumption]` with a source. The automated research review then checks for unsourced claims and incorrect labels — a process that is currently LLM-based and inherently imprecise. FActScore offers a complementary approach: decompose long-form generated text into atomic claims and compute the percentage that can be verified against a knowledge source. This is directly analogous to the existing citation-discipline check, but produces a quantitative score rather than a pass/fail verdict. Understanding FActScore's methodology is a prerequisite for deciding whether to incorporate precision scoring into the research review pipeline.

## Approach

1. **Core methodology:** How does FActScore decompose text into atomic claims? What counts as "atomic"? How is the knowledge source queried, and how is the verification verdict determined?

2. **Precision score semantics:** What does a FActScore precision value of X% mean in practice? How does it relate to the number of unsupported claims in a document?

3. **Knowledge source sensitivity:** How much does FActScore's score vary with the choice of knowledge corpus (Wikipedia, web retrieval, domain-specific corpora)? What corpus would be appropriate for this repository's research items?

4. **Alignment with the existing review rubric:** Map FActScore's atomic claim categories onto the `[fact]` / `[inference]` / `[assumption]` taxonomy. Are they compatible? What would be lost or gained by adopting precision scoring?

5. **Integration feasibility:** Is FActScore available as a standalone Python package? What are the compute and API dependencies? Is it feasible to run in a GitHub Actions workflow?

## Sources

- [ ] [Min et al. (2023) FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation](https://arxiv.org/abs/2305.14251) — primary paper; defines the methodology, benchmarks, and precision score semantics
- [ ] [FActScore GitHub Repository](https://github.com/shmsw25/FActScore) — official implementation; Python package, documentation, and usage examples
- [ ] [Wang et al. (2024) OpenFactCheck: A Unified Framework for Factuality Evaluation of LLMs](https://arxiv.org/abs/2405.05583) — positions FActScore within the broader automated fact-checking ecosystem; cross-reference with OpenFactCheck item
- [ ] [Lee et al. (2022) Factuality Enhanced Language Models for Open-Ended Text Generation](https://arxiv.org/abs/2206.04624) — earlier foundational work on factuality evaluation; historical context for FActScore's design choices

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
