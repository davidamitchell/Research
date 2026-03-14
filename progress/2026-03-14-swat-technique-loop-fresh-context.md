# 2026-03-14 — Research Loop (swat-technique-loop-fresh-context)

**Completed:**

Research item:
- `Research/completed/2026-03-12-swat-technique-loop-fresh-context.md` — completed; SWAT technique loop failure modes in stateless LLM sessions are structural, not prompt-level: sycophancy (61.75% preemptive rebuttal rate, RLHF-trained) and false completeness are training-level failures unaddressed by grounding tools; cross-iteration consistency collapse and compounding error propagation are loop-architectural failures addressable by state persistence and human verification gates.

Sources consulted:
- https://ojs.aaai.org/index.php/AIES/article/view/36598 (SycEval AIES 2025 — primary empirical sycophancy data: 58.19% overall, 61.75% preemptive rebuttal rate)
- https://arxiv.org/abs/2509.12517 (arXiv:2509.12517 / CHI 2026 — interaction context often increases sycophancy in LLMs)
- https://arxiv.org/abs/2005.11401 (Lewis et al. 2020 — RAG original paper: grounding reduces hallucination but does not address sycophancy)

## Mini-Retro

1. **Did the process work?** Yes. The research skill framework produced well-structured output. The review workflow correctly identified 17 violations (acronym expansion, URL specificity, inference labelling, AI slop) that required a fix-and-resubmit cycle. All violations were resolved and the second review returned OVERALL: PASS.

2. **What slowed down or went wrong?** The first review failed on 17 violations, most of which were citation-discipline issues (AIES, CHI, NeurIPS, EMNLP not expanded; milvus.io/dev.to/letsdatascience given only domain names instead of full URLs). These are repeat patterns from prior reviews — the acronym expansion audit and URL discipline checks in Step 6 were executed but not rigorously enough to catch all instances. The fix-and-resubmit cycle added ~20 minutes.

3. **What single change would prevent this next time?** Before committing the draft, run a targeted grep for every known problematic abbreviation (AIES, CHI, NeurIPS, EMNLP, SLA, SEO, RAG on first use) AND grep for domain-only source references without full paths (e.g., `milvus.io`, `dev.to`, `letsdatascience.com` without a trailing `/path`) in the Evidence Map and Sources sections. The audit table in Step 6 is necessary but not sufficient — it must be executed as a literal string search, not as a read-through check.

4. **Is this a pattern?** Yes — this matches the documented recurring pattern: acronym expansion failures and URL specificity are the two most common causes of citation-discipline violations across all prior research reviews. Both are already in the Known Recurring Patterns table in the instructions. The failure here was execution discipline (partial audit), not lack of awareness of the rule.
