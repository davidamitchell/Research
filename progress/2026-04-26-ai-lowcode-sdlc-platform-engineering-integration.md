# 2026-04-26 -- Research Loop (ai-lowcode-sdlc-platform-engineering-integration)

**Completed:**

Research item:
- `Research/completed/2026-04-26-ai-lowcode-sdlc-platform-engineering-integration.md` -- completed; the item concludes that AI and low-code governance should reuse the same software-delivery and platform-engineering system as conventional software, with additional risk-based assurance lanes added inside shared pipelines rather than through a separate parallel process. It also shows that protected promotion controls, low-code publish restrictions, evaluation suites, IaC-managed platform objects, and internal developer platform scaffolding are the key mechanisms that keep the governed path both stronger and easier than bypass.

Sources consulted:
- https://csrc.nist.gov/pubs/sp/800/218/final (Secure Software Development Framework baseline)
- https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments (protected deployment environments and approvals)
- https://learn.microsoft.com/en-us/power-platform/alm/pipelines (low-code pipeline governance and delegated deployments)

## Mini-Retro

1. **Did the process work?** Yes. The review loop caught the exact places where synthesis had drifted into fact-labeling, and the second pass plus manual cleanup produced a stronger final item.
2. **What slowed down or went wrong?** The main slowdown was citation-discipline around process metadata and prescriptive synthesis, especially where recommendations were well supported but still needed `[inference]` rather than `[fact]`.
3. **What single change would prevent this next time?** Nothing additional is needed beyond applying the stricter "recommendation equals inference unless the source states it directly" rule from the start.
4. **Is this a pattern?** Yes. It matches the existing recurring pattern of review failures caused by citation-discipline and evidence-label precision rather than by missing raw source material.
