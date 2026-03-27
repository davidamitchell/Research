# 2026-03-27 -- Research Loop (measuring-opportunity-cost)

**Completed:**

Research item:
- `Research/completed/2026-03-26-measuring-opportunity-cost.md` -- completed; opportunity cost is structurally harder to measure than direct costs because accrual accounting, quarterly KPIs, and procurement frameworks are designed to record realised transactions, not foregone ones. Cognitive biases (loss aversion ~2.25x, present bias) then amplify the structural gap. The most tractable interventions are pre-decision baselines and marketing mix modelling as counterfactual tools.

Sources consulted:
- https://hbr.org/2017/02/finally-proof-that-managing-for-the-long-term-pays-off (McKinsey/FCLTGlobal long-term management study: 47% more revenue, 81% more economic profit over 2001–2014)
- https://www.simplypsychology.org/prospect-theory.html (Kahneman and Tversky prospect theory and loss aversion)
- https://blog.iese.edu/martinezdealbeniz/files/2023/05/Omnichannel_20220425_web.pdf (IESE omnichannel counterfactual analysis)

## Mini-Retro

1. **Did the process work?** Mostly yes. Web research produced solid empirical evidence across all five approach threads. The §0-§7 skill output was complete and coherent. The review cycle caught genuine violations and forced quality improvements.

2. **What slowed down or went wrong?** Two main blockers: (a) the git stash/pull interaction caused repeated unstaged-change errors that required stash-and-pop on every pull; (b) the first review pass returned OVERALL: FAIL with 8 violations, requiring a second pass. The most common violations were missing [inference] labels on causal claims and domain-only citations without full URLs. The volume of citations requiring specific URLs (22+ in §2) was underestimated going in.

3. **What single change would prevent this next time?** Add full URLs at the point of writing §2 citations rather than cleaning them up post-review. Treating every "source: domain.com" as a violation at time of writing would eliminate the citation-URL violation class entirely.

4. **Is this a pattern?** Yes — citation URL incompleteness is a recurring review failure pattern noted in the repository instructions (flagged 19+ times across previous reviews). The root cause is writing citations informally during investigation and not converting them to specific URLs before the self-review step. The fix is to enforce the URL requirement during §2 writing, not as a post-hoc cleanup.
