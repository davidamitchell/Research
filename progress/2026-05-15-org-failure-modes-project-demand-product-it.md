# 2026-05-15 -- Research Loop (org-failure-modes-project-demand-product-it)

**Completed:**

Research item:
- `Research/completed/2026-05-14-org-failure-modes-project-demand-product-it.md` -- completed; the item found that project-based demand over long-lived product teams is repeatedly associated with over-commitment, backlog fragmentation, weak product stewardship, and slower feedback loops. The strongest evidence came from large-enterprise transition reports and case studies showing that annual project budgeting, project reporting, and feature-led business cases keep reintroducing queueing and ownership conflict inside teams that are supposed to operate as durable products. The strongest supported mitigation was continuously funded build-and-run teams, one visible backlog for all work, and governance focused on outcome and capacity review rather than project-by-project gates.

Sources consulted:
- https://info.planview.com/rs/456-QCH-520/images/Planview_2023-Project-to-Product-State-of-the-Industry-Report.pdf (survey and systems-data evidence on project-to-product maturity, annual budgets, and demand-capacity mismatch)
- https://itrevolution.com/articles/project-to-product-transformation-case-study-global-media-service-provider/ (case study on backlog unification, epic funding, and product-management friction during transition)
- https://less.works/blog/2026/02/20/project-based-funding-in-product-development (hybrid project-funding/product-development model and its flexibility costs)

## Mini-Retro

1. **Did the process work?** Yes. The evidence base was good enough to answer the question once the hybrid funding examples, survey data, and adjacent completed items were combined.
2. **What slowed down or went wrong?** The research-review workflow passed on substance but initially failed to persist `review_count` because `main` moved during the workflow push, and the second-pass auto-pass path still emitted useful log violations that needed manual reading.
3. **What single change would prevent this next time?** Nothing in the repository needs changing from this item alone; the main lesson was procedural, namely to keep treating the review log as authoritative even when the workflow conclusion is green.
4. **Is this a pattern?** Yes. It matches the known recurring pattern that the review workflow conclusion can disagree with the real audit result in the log, especially on the second-pass auto-pass path.
