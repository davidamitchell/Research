# 2026-05-15 -- Complete research item (promptql-definition-foundations-related-technologies)

**Completed:**
- `Research/completed/2026-05-14-promptql-definition-foundations-related-technologies.md` — completed the PromptQL research item with a working definition, mapped its closest research foundations, and identified the adjacent technology categories needed for future evaluation.
- `progress/2026-05-15-promptql-definition-foundations-related-technologies.md` — recorded this session and review-loop follow-up.

## Mini-Retro

1. **Did the process work?** Yes, but only after several review-guided tightening passes on claim labels and citation discipline.
2. **What slowed down or went wrong?** The automated review surfaced several absence-claim and interpretation-as-fact issues late, and the workflow records failed passes by incrementing `review_count` even when the outer job exits successfully.
3. **What single change would prevent this next time?** Add an explicit pre-draft audit for absence claims and cross-source consistency judgments so they default to `[inference]` unless a source states them directly.
4. **Is this a pattern?** Yes — review failures in this repository frequently come from subtle epistemic-label mistakes rather than missing sources altogether.
