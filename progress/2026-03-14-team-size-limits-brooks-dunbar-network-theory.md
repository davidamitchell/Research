# 2026-03-14 — Research Loop (team-size-limits-brooks-dunbar-network-theory)

**Completed:**

Research item:
- `Research/completed/2026-03-12-team-size-limits-brooks-dunbar-network-theory.md` — completed; Brooks (1975) establishes a quadratic coordination cost principle (n(n-1)/2) but does not identify 5 as the optimal team size; Dunbar's (1992) 5-person inner circle is the least empirically robust layer in his framework, with a 2021 Stockholm University study finding confidence intervals too wide (2–520) to support a hard cognitive limit; the US Army fire team is 4 soldiers (not 5), and military doctrine does not cite cognitive neuroscience; the three disciplines converge in direction (small teams outperform in high-context coordination) but through distinct mechanisms rather than as three descriptions of the same phenomenon.

Sources consulted:
- https://web.eecs.umich.edu/~weimerw/2018-481/readings/mythical-man-month.pdf (Brooks 1975 *The Mythical Man-Month* — primary source for n(n-1)/2 formula)
- https://pdodds.w3.uvm.edu/files/papers/others/1993/dunbar1993a.pdf (Dunbar 1993 — primary source for neocortex/group-size mechanism)
- https://pmc.ncbi.nlm.nih.gov/articles/PMC8103230/ (Lindenfors et al. 2021 — primary empirical challenge to Dunbar's number)
- https://www.army.mil/ranks/ (US Army official ranks page — fire team = 4 soldiers, primary source)
- https://aws.amazon.com/executive-insights/content/amazon-two-pizza-team/ (Bezos two-pizza rule — AWS Executive Insights)

## Mini-Retro

1. **Did the process work?** Yes. The research skill loop ran cleanly: question decomposition, evidence gathering across primary sources, consistency check identifying the fire team correction and the Dunbar empirical challenge, synthesis, acronym audit, review pass on first submission.

2. **What slowed down or went wrong?** The video primary source (YouTube transcript) was not directly accessible as a transcript; content was reconstructed from the item's context section and the GitHub daily digest. This is an inherent limitation of the current tooling. No research workflow errors.

3. **What single change would prevent this next time?** The transcript fetcher (`python -m src.main fetch`) uses a different command signature than attempted (`fetch-transcript`). Checking the available subcommands before attempting the fetch would save a failed call. The item's Sources checklist already notes this workaround is needed.

4. **Is this a pattern?** Yes — this matches the known pattern of YouTube transcript inaccessibility at research time. The item context sections already account for this by reconstructing speaker claims in prose. No new pattern to add.
