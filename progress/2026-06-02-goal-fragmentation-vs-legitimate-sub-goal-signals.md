# 2026-06-02 -- Complete research item: goal-fragmentation-vs-legitimate-sub-goal-signals

**Completed:**
- `Research/completed/2026-05-31-goal-fragmentation-vs-legitimate-sub-goal-signals.md` -- completed from backlog item 2026-05-31; research question asks what signals distinguish a salami-sliced goal fragment from a legitimately scoped sub-goal, concluding that three independent signal categories are required: structural (GORE AND-refinement entailment), semantic (INVEST criteria), and contextual (contractual scope markers).

**Review passes:**
- Pass 1 FAILED: GORE, KAOS, INVEST, EIA, PDDL, BDN acronyms not expanded in narrative prose
- Pass 2 FAILED: 11 violations (MVP reversal, IEEE unexpanded, truncated URL, KF3 [fact] on superlative, §5 [fact] on evaluative claim, all KFs bolded entirely as inline headers, 38 em-dashes, repeated Analysis paragraph openings, KF1/4/7 high confidence with single source)
- Pass 3 FAILED: §6 KF3 still [fact] (multi-line Python match missed), §2.A scope mismatch, §2.A Horkoff unlabeled, §2.B2 IEEE 29148 missing URL, §5 behavioural/economic paragraphs missing per-sentence labels
- Pass 4: Auto-passed (review_count reached MAX_REVIEWS=2)

**Learnings.md:** Added sentence to Thread 4 (Formal specification and informal institutions) noting the three-category decision framework from this item.

## Mini-Retro

1. **Did the process work?** Yes, but required 3+auto review passes rather than 1-2. The core research content was sound; the failures were all citation-discipline and labeling mechanics rather than substantive findings errors.

2. **What slowed down or went wrong?** Two recurring patterns caused most delays: (a) multi-line Python string replacement for label fixes failed when whitespace didn't match exactly -- required view_range inspection before editing; (b) per-sentence label requirement in multi-sentence paragraphs (§5 behavioural/economic lenses) was applied only to the final sentence initially, requiring a dedicated fix pass.

3. **What single change would prevent this next time?** Before committing any fix, grep for `\[fact\]` on evaluative/superlative sentences and grep each multi-sentence paragraph in §5 to confirm every sentence ends with its own `[inference/fact/assumption; source: URL]`, not just the last.

4. **Is this a pattern?** Yes. Both patterns are already in the Known Recurring Patterns table in copilot-instructions.md: "Multi-sentence paragraph with a single trailing citation block" and "Unlabeled evaluative judgments." No new table entry needed, but the pattern count confirms these are the two most expensive mechanics to get right.

5. **Does any documentation need updating?** No new conventions emerged beyond confirming the existing patterns.

6. **Do the default instructions need updating?** No. The patterns are documented. The fix is operational discipline during pre-commit self-review.
