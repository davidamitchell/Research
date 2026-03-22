# 2026-03-22 — Research Loop (layered-org-llm-architecture)

**Completed:**

Research item:
- `Research/completed/2026-03-19-layered-org-llm-architecture.md` — completed; the evidence supports a layered enterprise customisation pattern built around retrieval, selective parameter-efficient adaptation, and verifier layers instead of training an organisation-specific model from scratch. Public cases such as Harvey, Glean, and the published Morgan Stanley summary reinforce that enterprises are customising the system stack around base models rather than replacing them wholesale.

Sources consulted:
- https://arxiv.org/abs/2106.09685 (LoRA paper on low-rank adaptation for efficient fine-tuning)
- https://arxiv.org/abs/2305.14314 (QLoRA paper on memory-efficient adapter training)
- https://www.harvey.ai/blog/expanding-harveys-model-offerings (Harvey product post showing layered multi-model routing in practice)

## Mini-Retro

1. **Did the process work?** Yes. The start → draft → review → complete loop worked end-to-end, and the second review pass correctly surfaced only edge-case citation-discipline issues.
2. **What slowed down or went wrong?** The review rubric is stricter than a normal editorial pass: it caught repetition across sections, uncited synthesis-table rows, and abbreviation-expansion edge cases such as `F1` and `ML`.
3. **What single change would prevent this next time?** Add an explicit pre-draft check for Findings tables and assumption bullets so every row and justification carries both a label and inline sources before the first review run.
4. **Is this a pattern?** Yes. It matches the repository's known pattern that research review failures cluster around acronym expansion and citation discipline rather than missing substance.
