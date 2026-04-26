# 2026-04-26 -- Research Loop + All Items site page (systems-capability-debt-agentic-ai-risk-synthesis)

**Completed:**

Research item:
- `Research/completed/2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis.md` -- completed; the item concludes that the full causal chain from systems capability debt through workaround estates to amplified agentic-AI risk is best understood as a novel synthesis rather than a pre-existing named framework. The strongest published bridge is the shadow-information-technology literature, while Basel and National Institute of Standards and Technology (NIST) governance material plus agentic-AI control literature provide the risk and amplification layers.

Site tooling:
- `scripts/build_site.py` -- added `build_all_items()` function and "All" nav entry; generates `docs/all.html` on merge to main via the `build_site.yml` workflow. The page lists all completed research items grouped by month, most recent first, reusing the existing `render_card()`, card-grid, tag pill, and CSS components.

Sources consulted:
- https://link.springer.com/article/10.1007/s10257-020-00472-6 (shadow information technology transition from unmet need to business-managed systems)
- https://www.academia.edu/9093645/On_the_Emergence_of_Shadow_IT_A_Transaction_Cost_Based_Approach (transaction-cost explanation for shadow information technology emergence)
- https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/ (machine-speed autonomy, permission scope, and human-approval bottlenecks in agentic systems)

## Mini-Retro

1. **Did the process work?** Yes for the research item. The `docs/` conflict surfaced because generated HTML was committed to the feature branch, which is prohibited by the instructions — the `build_site.yml` workflow regenerates `docs/` on every push to `main`. The fix (reverting all `docs/` changes and leaving only `scripts/build_site.py`) resolved it cleanly.
2. **What slowed down or went wrong?** The first draft review surfaced several comparative and absence-based claims that were still written as facts, plus a few mirrored-section parity gaps after fixes. The `docs/` commit added unnecessary noise to the PR diff.
3. **What single change would prevent this next time?** Run `git status` before committing and confirm no `docs/` files are staged — this is already in the Slice Completion Checklist but was not followed for the site-tooling step.
4. **Is this a pattern?** Yes — "Never commit `docs/` changes on a feature branch" is an existing Non-Negotiable Constraint (#8 in the Quick Reference). No instruction change needed; adherence needs to improve.
5. **Does any documentation need updating?** `CHANGELOG.md` updated with the new `build_all_items()` feature.
6. **Do the default instructions need updating?** No new convention emerged that is not already covered.
