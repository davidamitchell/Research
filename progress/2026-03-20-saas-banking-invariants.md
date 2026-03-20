# 2026-03-20 — Research Loop (saas-banking-invariants)

**Completed:**

Research item:
- `Research/completed/2026-03-15-saas-banking-invariants.md` — completed; enterprise banking Software as a Service (SaaS) platforms such as Salesforce Financial Services Cloud (FSC) and nCino provide real value as reusable domain and operating primitives, but they do not remove customer-side integration, migration, testing, training, and governance work. The strongest conclusion is a layered buy-plus-build model: rent broad banking capability and platform primitives, then build differentiated layers where remaining lifecycle cost is justified, because Artificial Intelligence (AI)-assisted development reduces code-heavy bespoke costs without removing transformation-heavy costs.

Sources consulted:
- https://www.ncino.com/implementation (nCino implementation lifecycle and customer-side work)
- https://www.salesforce.com/company/legal/trust-and-compliance-documentation/ (Salesforce shared trust, compliance, and platform-operating documentation)
- https://www.cio.com/article/242681/calculating-the-total-cost-of-ownership-for-enterprise-software.html (lifecycle Total Cost of Ownership (TCO) cost categories)

## Mini-Retro

1. **Did the process work?** Yes. The research-loop workflow, review workflow, and state-transition commands all worked end to end once the item was brought back into a single consistent lifecycle.
2. **What slowed down or went wrong?** The repository had both an `in-progress` and an already-`completed` copy of the same item, and the first review pass exposed citation-discipline and repetition issues that required one additional edit-and-review loop.
3. **What single change would prevent this next time?** Add a preflight guard in the research loop that detects duplicate filenames across `Research/in-progress/` and `Research/completed/` before resuming an item.
4. **Is this a pattern?** Possibly. The duplicate lifecycle state does not map to an existing named pattern in the instructions, so it may warrant being captured if it recurs.
