# 2026-03-14 — Research Loop (financial-forecasting-it-run-costs)

**Completed:**

Research item:
- `Research/completed/2026-03-13-financial-forecasting-it-run-costs.md` — completed; best practices for financially responsible forecasting of Information Technology (IT) operational run costs, covering the Technology Business Management (TBM) Council V4 cost taxonomy, eight canonical required assumptions, three complementary uncertainty-quantification techniques (scenario analysis, sensitivity/tornado, Monte Carlo simulation), correlated error compounding over multi-year horizons, and regulatory disclosure obligations under International Financial Reporting Standards (IFRS) IAS 1.125, US Generally Accepted Accounting Principles (GAAP) ASC 275, Securities and Exchange Commission (SEC) Management's Discussion and Analysis (MD&A), Sarbanes-Oxley Act (SOX) 302/404, UK Financial Reporting Council (FRC) 2022 thematic, and EU Prospectus Regulation 2017/1129.

Sources consulted:
- https://www.tbmcouncil.org/ (TBM Council V4 taxonomy — IT cost pool definitions)
- https://www.ifrs.org/issued-standards/list-of-standards/ias-1-presentation-of-financial-statements/ (IAS 1 paragraph 125 — estimation uncertainty disclosure requirements)
- https://www.sec.gov/rules/interp/33-8350.htm (SEC FR-72 — MD&A guidance on critical accounting estimates and "reasonably likely" threshold)
- https://pcaobus.org/Standards/AS/Pages/AS2101.aspx (PCAOB AS 2101 — audit risk assessment referencing IT controls)
- https://www.finops.org/introduction/what-is-finops/ (FinOps Foundation — cloud cost optimisation and unit economics practices)
- https://www.isaca.org/resources/cobit (ISACA COBIT 2019 APO06 — IT financial management objectives)

## Mini-Retro

1. **Did the process work?** Yes. Context compaction interrupted the `cat >>` heredoc write mid-session, but the write had completed before the shell was terminated. File verification on resume confirmed 491 lines with all expected sections intact. The rest of the pipeline (draft → push → review → complete) ran without issues.
2. **What slowed down or went wrong?** Context compaction during a long heredoc write caused uncertainty about whether the append had succeeded. The 30-second initial_wait for the bash sync command was too short for a 600-line heredoc; the command was backgrounded and the session was compacted before completion was confirmed.
3. **What single change would prevent this next time?** For large file writes, use `filesystem-write_file` or split into multiple smaller writes with explicit verification after each chunk, rather than a single large heredoc in a sync bash call with a short initial_wait.
4. **Is this a pattern?** Yes — this is a new variant of the "long-running heredoc write + compaction = unknown state" problem. It warrants noting as a recurring pattern: verify file state as the first action after any session resume, not as a nice-to-have.
