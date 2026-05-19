# 2026-05-19 -- Research Loop (rq3-2-stochastic-parrot-ood)

**Completed:**

Research item:
- `Research/completed/2026-05-18-rq3-2-stochastic-parrot-ood.md` -- completed; the item concludes that current Large Language Models fail predictably when prompts require structural intervention, counterfactual reasoning, or genuinely novel multi-step composition. Grokking and analogy results still matter, but they narrow the claim to "partial abstraction with brittle portability" rather than overturning the broader out-of-distribution failure record.

Sources consulted:
- https://arxiv.org/abs/2410.05229 (GSM-Symbolic arithmetic-robustness benchmark)
- https://arxiv.org/abs/2405.00622 (CaLM causal-reasoning benchmark)
- https://arxiv.org/abs/2212.09196 (Webb et al. analogical-reasoning counterevidence)

## Mini-Retro

1. **Did the process work?** Yes. The research-review workflow caught several subtle epistemic-label and definition-source issues that were easier to miss in self-review than in the automated pass.
2. **What slowed down or went wrong?** The workflow only incremented `review_count` on the second pass, and the first two review logs surfaced new violations in small batches, so the item needed multiple draft-fix-review loops.
3. **What single change would prevent this next time?** Add authoritative definition sources for central domain terms earlier in the draft, especially when the first use appears in the Executive Summary or Findings rather than in the source list.
4. **Is this a pattern?** Yes. It matches the existing recurring pattern around acronym and first-use definition failures in research items, with the same root cause applied to domain terms rather than abbreviations.

## Applied improvements

- Updated `research-prompt.md` to require authoritative causal-hierarchy definition sources when intervention or counterfactual terms first appear in Findings or in `§2 Investigation` scope-defining prose.
