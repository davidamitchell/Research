# 2026-03-13 — Research Loop (nature-of-the-firm-coase-organisations)

**Completed:**

Research item:
- `Research/completed/2026-03-10-nature-of-the-firm-coase-organisations.md` — completed; synthesises Coase (1937), Williamson (1981), and North (1990) into a practical organisational design framework, maps Team Topologies' four team types and three interaction modes directly onto Williamson's governance structures, and derives four structural invariants and five fitness functions for organisations. Applied to software organisations, API design, platform teams, and business unit governance.

Sources consulted:
- https://www.jstor.org/stable/2626876 (Coase 1937 "The Nature of the Firm" — JSTOR entry)
- https://acawiki.org/The_economics_of_organization:_The_transaction_cost_approach (Williamson 1981 AcaWiki summary)
- https://www.nobelprize.org/prizes/economic-sciences/1993/north/lecture/ (North 1993 Nobel Prize lecture)
- https://www.ebsco.com/research-starters/business-and-management/transaction-cost-theory (EBSCO Transaction Cost Theory reference)
- https://teamtopologies.com/key-concepts (Team Topologies key concepts)
- https://martinfowler.com/bliki/TeamTopologies.html (Martin Fowler — Team Topologies)
- https://aws.amazon.com/executive-insights/content/amazon-two-pizza-team/ (Amazon two-pizza teams — first-party)
- https://derekarmstrong.dev/books/building-evolutionary-architectures/ (Building Evolutionary Architectures fitness functions summary)
- https://www.infoq.com/articles/fitness-functions-architecture/ (InfoQ fitness functions article)
- https://academic.oup.com/book/25306 (Penrose 1959 — Oxford Academic)

## Mini-Retro

1. **Did the process work?** Yes. The research skill sections produced a coherent framework. Prior art in `2026-03-02-transaction-costs.md` provided a strong foundation that avoided re-researching known TCE mechanics. The review passed OVERALL: PASS on first submission.

2. **What slowed down or went wrong?** The Tavily MCP server was unavailable (invalid API key). Fell back to web_search tool without interruption. No material slowdown.

3. **What single change would prevent this next time?** Nothing to change — the fallback to web_search worked cleanly. The Tavily outage is an infrastructure issue, not a process issue.

4. **Is this a pattern?** The Tavily API key failure has appeared in prior sessions. It is a known recurring issue that the web_search fallback handles adequately.
