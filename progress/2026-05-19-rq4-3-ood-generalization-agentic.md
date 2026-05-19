# 2026-05-19 -- Research Loop (rq4-3-ood-generalization-agentic)

**Completed:**

Research item:
- `Research/completed/2026-05-18-rq4-3-ood-generalization-agentic.md` -- completed; the item concludes that unconstrained production shift gives tool-using Large Language Model systems no non-vacuous universal bound on out-of-distribution performance. The strongest available guarantees are narrower: bounded-shift target-risk bounds, calibrated abstention or set coverage, and online adaptation, with stochastic tool outputs remaining an irreducible reliability floor.

Sources consulted:
- https://www.alexkulesza.com/pubs/adapt_mlj10.pdf (Ben-David et al. domain-adaptation target-risk bound)
- https://proceedings.neurips.cc/paper/2021/hash/c5c1cb0bebd56ae38817b251ad72bedb-Abstract.html (Ye et al. impossibility result for arbitrary out-of-distribution generalisation)
- https://arxiv.org/abs/2208.08401 (Gibbs and Candès on online conformal adaptation under arbitrary distribution shift)

## Mini-Retro

1. **Did the process work?** Mostly yes. The research path was straightforward once the formal-bounds layer was grounded in Ben-David, Ye, and conformal-shift sources.
2. **What slowed down or went wrong?** The first review pass caught small but real format issues: `RQ` was unexpanded in the title, one system-level transfer claim was labeled too strongly, and `§7` review metadata was phrased as sentences instead of pure metadata.
3. **What single change would prevent this next time?** Make the prompt require bare `key: value` metadata lines in `§7 Recursive Review` instead of bullet-sentence phrasing.
4. **Is this a pattern?** Yes. It matches recurring review friction where evidence is adequate but a small formatting or epistemic-label detail still triggers a failure.

## Applied improvements

- Updated `research-prompt.md` §2c2 so `§7 Recursive Review` uses bare `key: value` metadata fragments instead of sentence-like bullets.
