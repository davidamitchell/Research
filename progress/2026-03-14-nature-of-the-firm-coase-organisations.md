# 2026-03-14 — Research Loop (nature-of-the-firm-coase-organisations)

**Completed:**

Research item:
- `Research/completed/2026-03-10-nature-of-the-firm-coase-organisations.md` — completed; synthesises Coase (1937), Williamson (1981), and North (1990) to explain why organisations exist as transaction cost minimisers. Maps Team Topologies' three interaction modes directly onto Williamson's governance structures, establishes four organisational invariants (residual claimancy clarity, authority-accountability alignment, information-decision alignment, shared purpose), and defines fitness functions for firms applied to software team design, API boundaries, and platform strategy.

Sources consulted:
- https://www.jstor.org/stable/2626876 (Coase 1937 — The Nature of the Firm, JSTOR)
- https://acawiki.org/The_economics_of_organization:_The_transaction_cost_approach (Williamson 1981 — Transaction Cost Approach, AcaWiki)
- https://www.nobelprize.org/prizes/economic-sciences/1993/north/lecture/ (North 1993 Nobel lecture on institutions and economic performance)

## Mini-Retro

1. **Did the process work?** Partially. The research was completed and reviewed in a prior session; this session resumed from `status: reviewing` with no open review issues (OVERALL: PASS) and completed the item. The stale backlog copy required cleanup via `git rm`.
2. **What slowed down or went wrong?** The research-review.yml workflow has been consistently returning `conclusion: failure` for recent runs. No violations issue was created, which satisfies the OVERALL: PASS criterion, but the workflow failure pattern warrants investigation. A duplicate copy of the item existed in both `Research/backlog/` and `Research/in-progress/` — this appears to be a leftover from the prior session that started the item without cleaning up the backlog file.
3. **What single change would prevent this next time?** The `research start` CLI command should ensure the backlog file is removed (or at least warn) after moving to in-progress. Alternatively, verify that the previous session's `git add -A` + commit step ran before the loop exited.
4. **Is this a pattern?** The stale backlog copy is new. The review workflow failure is a recurring issue noted in previous progress logs (the workflow infrastructure problem, not a research quality fail). Worth investigating if the research-review.yml workflow needs a fix.
