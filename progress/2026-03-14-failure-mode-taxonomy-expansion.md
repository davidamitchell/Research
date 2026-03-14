# 2026-03-14 — Research Loop (failure-mode-taxonomy-expansion)

**Completed:**

Research item:
- `Research/completed/2026-03-12-failure-mode-taxonomy-expansion.md` — completed; empirical frequency data resolves the parent taxonomy's open question about which failure layer matters most in production: Layer 4 (prompt injection) leads security incidents (OWASP Large Language Model (LLM) Top 10, two consecutive years; 85%+ exploitation rate), while Layer 1 (hallucination) leads user-visible operational impact (Cleanlab 2025 enterprise survey); sycophancy is resolved as a Layer 1 mechanism (H-Neuron over-compliance) that invariably produces a Layer 2 goal failure, with distinct latent-space encodings confirming the two mechanisms are separable; five cross-layer cascade paths are documented, with Layer 4→Layer 2 and Layer 5→Layer 1 identified as highest severity.

Sources consulted:
- https://owasp.org/www-project-top-10-for-large-language-model-applications/ (OWASP LLM Top 10 2025 — prompt injection frequency and severity data)
- https://arxiv.org/abs/2601.17548 (arXiv:2601.17548 — empirical prompt injection exploitation rate, 85%+)
- https://openreview.net/forum?id=d24zTCznJu (Vennemeyer et al. ICLR 2026 — H-Neuron sycophancy mechanism and latent-space encoding evidence)
- https://www.cleanlab.ai/blog/enterprise-ai-survey-2025/ (Cleanlab 2025 enterprise AI survey — Layer 1 as top user-visible failure)
- https://arxiv.org/abs/2603.03258 (arXiv:2603.03258 — goal drift in multi-step agents; contextual pressure mechanism)
- https://christian-schneider.net/llm-security-analysis.html (Christian Schneider — LLM security failure modes; attention trust conflation)
- https://emergentmind.com/papers/reward-hacking-survey (Emergentmind — reward hacking rates and manifestations in production models)

## Mini-Retro

1. **Did the process work?** Yes — the full §0–§7 skill output, Findings, companion checks, and review cycle completed without blockers. The review workflow passed on first submission.
2. **What slowed down or went wrong?** Context compaction occurred before the final steps (learnings.md update, session log, final commit), requiring resume. No research-quality issues caused rework; the single iteration through review was clean.
3. **What single change would prevent this next time?** Nothing specific to this session — the research phase was thorough, and the review passing first time confirms it. The compaction is an inherent constraint of long research items.
4. **Is this a pattern?** Context compaction on long research items is a recurring structural constraint (matches known pattern in instructions). Not a new pattern — no update to Known Recurring Patterns table warranted.
