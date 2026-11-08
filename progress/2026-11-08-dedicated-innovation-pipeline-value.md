# 2026-11-08 -- Research Loop (dedicated-innovation-pipeline-value)

**Completed:**

Research item:
- `Research/completed/2026-11-07-dedicated-innovation-pipeline-value.md` -- completed; a dedicated pipeline buys protected funding and a defined sponsor, with scaling the weakest part in the IBM, Xerox, and Pre-Cert cases. Microsoft throughput came from shared platform and federated ownership, and no source compares pipeline versus emergent lodging head to head.

Sources consulted:
- https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf (IBM Emerging Business Opportunities case)
- https://exp-platform.com/Documents/2017-05%20ICSE2017_EvolutionOfExP.pdf (Microsoft experimentation growth model)
- https://blogs.bing.com/search-quality-insights/2013/8/Large-Scale-Experimentation-at-Bing/ (Bing experiment success rate)
- https://www.gsb.stanford.edu/faculty-research/publications/intraorganizational-ecology-strategy-making-organizational-adaptation (Burgelman, Intel)
- https://www.computerhistory.org/siliconengine/bell-labs-licenses-transistor-technology/ (Bell Labs transistor licensing)

## Mini-Retro

1. **Did the process work?** Yes. Two review passes ran; pass 1 found six violations, all fixed, and pass 2 flagged one residual citation gap, also fixed.
2. **What slowed down or went wrong?** The first review trigger ran against a remote `main` lacking the commit because the push was rejected; the run had to be cancelled and re-triggered. Separately, an Analysis sentence cited a detail (a senior-executive "passion" quote) that was never recorded in §2.
3. **What single change would prevent this next time?** Verify `git push` succeeded before triggering the review workflow, and confirm every Analysis detail appears in §2.
4. **Is this a pattern?** The Key Finding that merges a factual clause and a derived clause under one `[fact]` label matches a known pattern in the instructions. The push-rejected-then-trigger sequence is new.

## Applied improvements

- Make check reports 4 pre-existing unformatted files outside this change; left untouched.
