---
title: "Trusting Trust and AI Corpus Contamination"
added: 2026-03-15
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [ai, epistemology, trust, corpus-contamination, prompt-injection, large-language-model, knowledge, security]
started: ~
completed: ~
output: [knowledge]
---

# Trusting Trust and AI Corpus Contamination

## Research Question

Ken Thompson's "Trusting Trust" argument shows that you cannot verify a compiler by reading its source code if the compiler was compiled by a compromised toolchain — the contamination lives in the binary, not the source. What is the web-scale analogue for Artificial Intelligence (AI)-generated content, and what does it mean for epistemology, knowledge verification, and trust when roughly half of all text on the web is now AI-generated and that proportion is growing?

## Scope

**In scope:**
- Thompson's original "Reflections on Trusting Trust" (1984) argument and its core insight about self-replicating corruption
- The structural analogy: AI-generated content → web corpus → training data → new AI-generated content (the closed loop)
- Current estimates of the fraction of web text that is AI-generated and trajectory projections
- Epistemological implications: what does "citing sources" mean when the cited sources may themselves be AI-generated and cross-indexed as authoritative?
- The relationship to prompt injection: how corpus-level contamination differs from document-level injection attacks
- Existing detection approaches and their fundamental limitations (document-level vs corpus-level)
- Prior work on data poisoning, model collapse, and self-referential training loops

**Out of scope:**
- Implementation details of specific AI detection tools
- Legal or copyright aspects of AI-generated text
- Misinformation and disinformation research beyond the epistemic verification problem

**Constraints:** Publicly accessible web sources, papers, and essays. No paywalled content unless freely available preprints exist.

## Context

Ken Thompson's 1984 Turing Award lecture "Reflections on Trusting Trust" is one of the most important security arguments ever made: a compiler can be made to insert a backdoor into every program it compiles — including itself — and no amount of source-code inspection can detect it because the corruption lives in the toolchain, not the source. The only defence is trust in the chain of custody of every binary ever run.

We are now in a structurally identical situation on the web. If roughly half of all text on the web is AI-generated — and that fraction is growing — then:

1. Web crawlers ingest that content as authoritative text.
2. That content enters the training corpora of the next generation of AI models.
3. Those models generate new content that references and is consistent with the AI-generated material already in the corpus.
4. Checking whether a document is internally consistent or "cites sources" cannot distinguish AI-generated-citing-AI-generated from genuine human knowledge, because the sources it cites were themselves produced by the same loop.

This is directly analogous to Thompson's insight: the corruption is at the corpus level, not the document level, and document-level inspection cannot detect it. The epistemological implication is significant: what does it mean to "know" something that was learned from a self-referential generative loop?

This question is also related to prompt injection: just as an adversary can inject instructions into a prompt context to hijack AI behaviour, a contaminated corpus can inject false priors into a model's world-model at training time.

## Approach

1. Read and summarise Thompson's "Reflections on Trusting Trust" — extract the core logical structure of the self-replicating trust argument.
2. Survey current estimates of AI-generated web content fraction (e.g., recent studies, Common Crawl analyses, industry reports) — what is the current best estimate and what is the projected trajectory?
3. Investigate the "model collapse" and "self-referential training" literature — what happens to models trained on AI-generated data, and does this support the corpus-contamination analogy?
4. Examine the epistemological implications — how do philosophers of knowledge (and practitioners of evidence-based reasoning) characterise the problem of circular or self-referential sources?
5. Explore the relationship to prompt injection — how does corpus-level contamination compare structurally to prompt-level injection as an attack surface?
6. Survey detection approaches and their limitations — why is detecting AI-generated content at the document level insufficient, and is there any corpus-level detection work?
7. Synthesise: what does this mean practically for anyone who relies on web-retrieved information as evidence, including AI agents, researchers, journalists, and knowledge workers?

## Sources

- [ ] Ken Thompson, "Reflections on Trusting Trust" (1984) — https://www.cs.cmu.edu/~rdriley/487/papers/Thompson_1984_ReflectionsonTrustingTrust.pdf
- [ ] Shumailov et al., "The Curse of Recursion: Training on Generated Data Makes Models Forget" (2023) — model collapse paper, arXiv:2305.17493
- [ ] Vykopal et al., "Disinformation Capabilities of Large Language Models" (2023) — AI-generated disinformation scale
- [ ] NewsGuard / Originality.ai reports on AI-generated web content proportions
- [ ] Riley Goodside / Simon Willison writing on prompt injection and corpus-level risks
- [ ] Wikipedia: Trusting Trust — https://en.wikipedia.org/wiki/Trusting_trust_attack

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

3–5 sentences. What is the answer to the research question? State the key conclusion directly.

### Key Findings

Ordered list. Each finding is a specific, evidence-backed claim.

1.
2.

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

- Type: knowledge
- Description:
- Links:
