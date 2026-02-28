---
title: "Information synthesis: non-lossy compression, entropy, and information theory"
added: 2026-02-27
status: backlog
priority: high
tags: [synthesis, information-theory, entropy, compression, ai]
started: ~
completed: ~
output: [knowledge, skill]
---

# Information synthesis: non-lossy compression, entropy, and information theory

## Question / Hypothesis

What is the best way to synthesise information from multiple sources in a manner that is minimally lossy — preserving the most signal while compressing volume — drawing on information theory, entropy, and compression research?

## Context

The core challenge of research is not gathering information but synthesising it. As research corpus grows, naive summarisation (LLM summary of each source) loses context and introduces hallucination. Better approaches exist:

- **Information theory**: measure the entropy of a document; high-entropy sections carry more information and should be preserved
- **Semantic compression**: identify redundancy across sources; only keep deltas
- **Chain-of-density** prompting: iteratively compress while tracking what is dropped
- **Graph-based synthesis**: model claims as nodes, evidence as edges

This is a foundational research question that should inform how we build the synthesis layer of the tooling.

## Scope

**In scope:**
- Literature review of information-theoretic approaches to text compression
- Survey of LLM prompting techniques for synthesis (chain-of-density, compression prompting)
- Evaluation of semantic deduplication approaches

**Out of scope:**
- Implementation of a full synthesis pipeline (that is Epic 4+)

## Approach

1. Review Shannon entropy and its application to text
2. Review chain-of-density and related prompting techniques
3. Review graph-based synthesis (knowledge graphs)
4. Synthesise recommendations into an ADR or knowledge note

## Sources

- [ ] Shannon, C.E. (1948). A Mathematical Theory of Communication
- [ ] Adams et al. (2023). From Sparse to Dense: GPT-4 Summarization with Chain of Density Prompting — https://arxiv.org/abs/2309.04269
- [ ] Meng et al. (2022). ROME / knowledge editing in transformers
- [ ] Information bottleneck method (Tishby et al.)

## Findings

*(Fill in when completing. Follow the research skill synthesis structure.)*

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

- Type: knowledge, skill
- Description: Synthesis approach recommendation; potentially a `synthesis` skill for the Skills repo
