---
title: "Which citation-discipline and evidence-verification checks in `research-review-prompt.md` could OpenFactCheck automate or augment, and what would an integrated pipeline look like?"
added: 2026-05-06T09:03:23+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: [2026-05-06-research-review-process-improvement]  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [fact-checking, hallucinations, evaluation, research-quality, llm]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
cites: []          # slugs of items this item directly depends on or quotes
related: [2026-05-02-automated-claim-verification-academic-literature, 2026-05-02-adversarial-review-methods-ai-research-quality, 2026-03-02-research-quality-assurance-methodology]
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# Which citation-discipline and evidence-verification checks in `research-review-prompt.md` could OpenFactCheck automate or augment, and what would an integrated pipeline look like?

## Research Question

The citation-discipline step in `research-review-prompt.md` requires every claim to carry a `[fact]`, `[inference]`, or `[assumption]` label plus a supporting URL, and is currently enforced by a Large Language Model (LLM) judge operating zero-shot on the full document. What capabilities does OpenFactCheck provide — specifically its claim decomposition, evidence retrieval, and verdict labelling stages — that could automate or augment this check, and what would a practical GitHub Actions integration look like?

## Scope

**In scope:**
- Comparison of OpenFactCheck's capabilities against the citation-discipline check in `research-review-prompt.md`: where it matches, where it falls short
- Practical integration pathways: API, CLI, self-hosted, GitHub Actions integration
- OpenFactCheck's core architecture: pipeline stages, claim extraction, evidence retrieval, verdict labelling
- Supported verification models and retrieval backends (web search, knowledge bases, retrieved documents)
- Evaluation benchmarks and known accuracy/precision/recall figures
- Licensing, maintenance status, and community adoption

**Out of scope:**
- General survey of all automated fact-checking tools (covered by related items)
- OpenFactCheck's political misinformation use cases unless directly relevant to research quality workflows
- Fine-tuning or training new verifier models

**Constraints:**
- Primary sources preferred: official documentation, published papers, GitHub repository
- Evaluate applicability specifically against the five citation-discipline checks in `research-review-prompt.md`
- Recency: tool is under active development; flag any findings older than 12 months

## Context

This repository's research review process (`research-review-prompt.md`) applies citation-discipline checks manually: every claim must be labelled `[fact]`, `[inference]`, or `[assumption]`, every source must have a URL, and unsupported generalisations trigger violations. These checks are currently enforced by an Large Language Model (LLM) judge running the review prompt. OpenFactCheck is an open-source framework specifically designed to verify factual claims in LLM outputs. Understanding its capabilities directly informs whether it could replace, supplement, or validate the existing LLM-judge approach, and whether automated fact verification is a tractable improvement to research quality in this repo.

## Approach

1. **Gap analysis against current review process:** Map OpenFactCheck's pipeline stages onto the citation-discipline and speculation-control checks in `research-review-prompt.md`. Where does it add value? Where does it fall short?

2. **Tool survey:** What does OpenFactCheck do — what pipeline stages does it implement, what claim types does it handle, and what evidence sources does it query?

3. **Technical architecture:** How is OpenFactCheck structured internally — is it modular, what are the extension points, and what does a complete verification run look like end-to-end?

4. **Accuracy and benchmarks:** What published evaluation results exist for OpenFactCheck on standard fact-checking benchmarks? How does it perform on academic and technical claims (the primary claim type in this repo)?

5. **Integration feasibility:** Can OpenFactCheck run in a GitHub Actions environment without external API credentials? What are the infrastructure requirements and cost implications?

## Sources

- [ ] [OpenFactCheck Platform](https://openfactcheck.com/) — official platform; starting point for capability overview
- [ ] [Wang et al. (2024) OpenFactCheck: A Unified Framework for Factuality Evaluation of LLMs](https://arxiv.org/abs/2405.05583) — primary academic paper describing architecture, benchmarks, and evaluation results
- [ ] [OpenFactCheck GitHub Repository](https://github.com/hasaniqbal777/OpenFactCheck) — source code, documentation, and issue tracker; authoritative technical reference
- [ ] [Min et al. (2023) FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation](https://arxiv.org/abs/2305.14251) — related foundational work that OpenFactCheck builds on; necessary context for understanding claim decomposition

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
