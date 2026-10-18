# 2026-10-18 -- Research: zone-intervention-cross-effects

**Completed:**
- `Research/completed/2026-10-03-zone-intervention-cross-effects.md`: no study varies more than one zone, so independence of the pool-annotation, harness-masking, and verifier gains is conditional; a table of falsifiable independence conditions was produced. Confidence medium-low; the overlay-on-consumer test and non-coding masking comparison are absent from the literature located.
- Review: pass 1 failed on em-dashes (remove-ai-slop); pass 2 failed on search-outcome claims labelled `[fact]`, a Key Finding mismatching its §2 source wording, interpretive clauses under `[fact]`, and over-rated high confidence. All were fixed after the second review; the item was completed at the 2-pass limit without a third review.

**Sources:** Chiang and Lee 2024 (ACL Anthology), Ge et al. 2505.17762, Tan 2401.11911, Wang 2504.13079, Lindenbauer 2508.21433, Sun 2510.11967, Panickssery 2404.13076, Wataoka 2410.21819, Kim 2506.07962.

## Mini-Retro

1. **Did the process work?** Yes; verifying abstracts via the arXiv API caught author and result details early.
2. **What slowed down or went wrong?** Imported template source descriptions carried em-dashes (40 lines), failing pass 1. Search-outcome notes were labelled `[fact]` and bound to unrelated papers.
3. **What single change would prevent this next time?** Run `grep -c "—"` over the whole file and treat failed-search notes as `[assumption]`, before the first review.
4. **Is this a pattern?** Partly: unlabelled or mislabelled search-outcome claims and em-dashes in Sources descriptions recur. Documentation: no change needed beyond the above; instructions already cover both.
