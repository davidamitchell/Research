# 2026-05-10 -- Research Loop (key-person-dependency-basel-risk-linkage)

**Completed:**

Research item:
- `Research/completed/2026-05-09-key-person-dependency-basel-risk-linkage.md` -- completed; Basel Committee sources support treating key-person dependency first as operational risk, then mapping it to `Execution, Delivery & Process Management` when the bottleneck threatens recurring process execution. The same dependency escalates into operational-resilience reporting when it can disrupt a critical operation, and into Basel Committee on Banking Supervision 239 risk-data control weakness when one person owns manual spreadsheet or desktop-database reporting logic.

Sources consulted:
- https://www.bis.org/bcbs/publ/d515.pdf (Basel operational-risk definition and governance framing)
- https://www.bis.org/bcbs/qisoprisknote.pdf (Basel loss-event wording for execution, delivery, and process management)
- https://www.bis.org/bcbs/publ/d516.pdf (operational-resilience dependency mapping and key-person continuity triggers)
- https://www.bis.org/publ/bcbs239.pdf (risk-data automation and manual-tool control expectations)

## Mini-Retro

1. **Did the process work?** Yes. Primary Basel sources were sufficient to build a clean mapping once the exact loss-event text for `Execution, Delivery & Process Management` was pulled in alongside the 2021 operational-risk and resilience documents.
2. **What slowed down or went wrong?** The first review workflow pass approved the content but failed to push `review_count` because `main` advanced underneath the workflow run, so the review had to be re-triggered on the new tip.
3. **What single change would prevent this next time?** Nothing new. The existing prompt already says to inspect the log, treat missing `review_count` as a failed metadata write, and re-trigger the review.
4. **Is this a pattern?** Yes. It fits the existing repository guidance not to trust workflow conclusion alone and to inspect logs plus `review_count` before proceeding.
