# 2026-05-12 -- Complete research item (hardware-load-inference-performance)

**Completed:**
- `Research/completed/2026-05-12-hardware-load-inference-performance.md` — completed the research item after review; conclusion: inference reliability shifts mainly at scheduler, memory, and numerical-path thresholds rather than at a single utilization percentage.
- `learnings.md` — updated Thread 18 to capture LLM serving as a concrete backpressure and constraint-management case.

**Key sources:**
- [Agrawal et al. (2024) Taming Throughput-Latency Tradeoff in Large Language Model Inference with Sarathi-Serve](https://arxiv.org/abs/2403.02310)
- [Kwon et al. (2023) Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180)
- [Yuan et al. (2025) Understanding and Mitigating Numerical Sources of Nondeterminism in Large Language Model Inference](https://arxiv.org/abs/2506.09501)

## Mini-Retro

1. **Did the process work?** Yes. The research-to-review loop worked once the item was tightened to the repo's exact citation and domain-term rules.
2. **What slowed down or went wrong?** The review workflow surfaced several prose-level failures that were easy to miss locally, especially authoritative first-use definitions and review-metadata phrasing.
3. **What single change would prevent this next time?** Treat §7 as pure metadata fragments from the start and add authoritative first-use definition sources for serving metrics and specialist terms before the first draft commit.
4. **Is this a pattern?** Yes. First-use terminology and review-only metadata wording are recurring failure modes in this repository's research workflow.
5. **Does any documentation need updating?** `learnings.md` did; this item added a concrete LLM-serving example to the constraint-management thread, so that update was made in this session.
6. **Do the default instructions need updating?** Not yet. The existing instructions already name acronym and domain-term expansion as common failures; the issue here was execution, not missing guidance.
