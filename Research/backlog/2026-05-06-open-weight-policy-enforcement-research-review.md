---
title: "What are open-weight reasoning models trained for policy enforcement (such as gpt-oss-safeguard), how do they classify text against customizable policies, and how applicable are they to implementing automated research review rules in this repository?"
added: 2026-05-06T09:03:23+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: medium  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [governance, llm, evaluation, research-quality, fact-checking, agentic-ai]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
cites: []          # slugs of items this item directly depends on or quotes
related: [2026-05-06-openfactcheck-automated-fact-verification, 2026-05-02-adversarial-review-methods-ai-research-quality, 2026-03-02-research-quality-assurance-methodology]
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# What are open-weight reasoning models trained for policy enforcement (such as gpt-oss-safeguard), how do they classify text against customizable policies, and how applicable are they to implementing automated research review rules in this repository?

## Research Question

What are open-weight reasoning models trained for policy-based text classification (exemplified by gpt-oss-safeguard), how do they work technically — training approach, policy specification format, inference mechanism — and how applicable are they to encoding and enforcing the structured research review rules in this repository's `research-review-prompt.md` as a machine-checkable, customisable policy?

## Scope

**In scope:**
- gpt-oss-safeguard's design: open-weight status, training methodology, policy specification format, and classification output schema
- The broader class of open-weight policy enforcement models — what distinguishes them from general-purpose LLMs and from fine-tuned classifiers
- Accuracy and policy adherence benchmarks for policy classification tasks
- How a custom policy could encode the six review dimensions in `research-review-prompt.md` (citation-discipline, speculation-control, remove-AI-slop, acronym expansion, source URL completeness, evidence labelling)
- Integration feasibility: model size, inference hardware requirements, open-weight licence, self-hosting on GitHub Actions runners
- Comparison with the current approach of passing `research-review-prompt.md` as a zero-shot prompt to a general-purpose LLM

**Out of scope:**
- Safety and content moderation use cases unrelated to research review quality
- Reinforcement Learning from Human Feedback (RLHF) training methodology in depth (in scope only as it affects policy adherence)
- Proprietary closed-weight safety classifiers (e.g. OpenAI Moderation API)

**Constraints:**
- gpt-oss-safeguard must be confirmed as genuinely open-weight (weights publicly available) before any integration recommendation
- Benchmarks must be drawn from independently reproducible evaluations
- Self-hosting feasibility must be assessed against GitHub Actions runner specifications (16 GB RAM baseline)

## Context

This repository's research review pipeline (`research-review-prompt.md`) currently uses a general-purpose LLM instructed via a long, structured prompt to check research items against six dimensions. This approach is powerful but expensive, non-deterministic, and difficult to version as a formal policy. Open-weight policy enforcement models represent a newer paradigm: rather than prompting a general-purpose model, a small specialist model is trained to classify text according to a strict, customisable policy schema. gpt-oss-safeguard is cited as an example of this class. If such models can encode the research review rubric as a versioned, testable policy, they could make the review pipeline cheaper, more consistent, and auditable — directly addressing a known limitation in the current process.

## Approach

1. **Model identity and lineage:** What exactly is gpt-oss-safeguard? Is it a single model, a family, or a training methodology? Who produced it, what is its open-weight licence, and what is its current maintenance status?

2. **Policy specification format:** How are policies specified — natural language, structured schema, or a fine-tuning dataset format? How granular can a policy be?

3. **Classification accuracy:** What published accuracy, precision, and recall figures exist for gpt-oss-safeguard on policy classification tasks? How does it compare to zero-shot prompting a general-purpose LLM?

4. **Policy mapping exercise:** Map the six research review dimensions in `research-review-prompt.md` onto a hypothetical gpt-oss-safeguard policy. Which dimensions are a good fit for policy classification? Which require generative reasoning that a classifier cannot provide?

5. **Self-hosting feasibility:** Can gpt-oss-safeguard run within GitHub Actions resource limits? What inference library and hardware are required?

## Sources

- [ ] [Microsoft gpt-oss-safeguard Model Card and Repository](https://huggingface.co/microsoft/gpt-oss-safeguard) — primary source; model card, weights, policy schema documentation, and licence
- [ ] [Inan et al. (2023) Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations](https://arxiv.org/abs/2312.06674) — foundational paper for the open-weight policy enforcement model paradigm; contextualises gpt-oss-safeguard
- [ ] [Rebedea et al. (2023) NeMo Guardrails: A Toolkit for Controllable and Safe LLM Applications](https://arxiv.org/abs/2310.10501) — related approach to policy enforcement via structured guardrails; alternative design point
- [ ] [OpenAI (2024) A Practical Guide to Building Classifiers with LLMs](https://platform.openai.com/docs/guides/text-classification) — comparative baseline: zero-shot classification with general-purpose LLMs

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
