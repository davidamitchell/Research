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

*(to be filled in)*

## Output

- Type: knowledge, skill
- Description: Synthesis approach recommendation; potentially a `synthesis` skill for the Skills repo
