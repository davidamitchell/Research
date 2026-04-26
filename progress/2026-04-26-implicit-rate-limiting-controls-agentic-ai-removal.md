# 2026-04-26 -- Research Loop (implicit-rate-limiting-controls-agentic-ai-removal)

**Completed:**

Research item:
- `Research/completed/2026-04-26-implicit-rate-limiting-controls-agentic-ai-removal.md` -- completed; the item found that reviewed operational-risk, automation-risk, and Artificial Intelligence (AI) governance frameworks govern adjacent explicit controls but do not explicitly name the removal of implicit human rate limiters as a control problem. The strongest support came from operational-resilience frameworks plus analogues from the Flash Crash, Robotic Process Automation (RPA), and normal accident theory, which together show that once human pacing disappears institutions usually have to rebuild pauses, segmentation, monitoring, and exception routing deliberately.

Sources consulted:
- https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32022R2554 (Digital Operational Resilience Act (DORA) primary text)
- https://www.sec.gov/files/marketevents-report.pdf (U.S. Securities and Exchange Commission (SEC) and Commodity Futures Trading Commission (CFTC) Flash Crash report)
- https://press.princeton.edu/books/paperback/9780691004129/normal-accidents (Charles Perrow normal accident theory overview)

## Mini-Retro

1. **Did the process work?** Yes, the research-and-review loop worked and the second review pass cleared after the remaining §2 notes were rewritten as labeled, source-bound claims.
2. **What slowed down or went wrong?** The strictest failure mode was not the research itself but the reviewer's treatment of §2 access/search notes as ordinary claim-bearing prose even when they were drafted as metadata fragments.
3. **What single change would prevent this next time?** Treat §2 access notes and failed-search summaries as labeled, source-bound prose from the first draft, then keep purely runtime metadata out of visible sentences unless the review prompt explicitly requires it.
4. **Is this a pattern?** Yes, this matches the existing recurring pattern around claim-label discipline and shows that the same rule also applies to research-process notes inside §2.

## Applied improvements

- Updated `research-prompt.md` so §2 access notes and failed-search notes are explicitly treated as claim-bearing prose for review purposes unless removed from visible text.

## Pending skill improvements

- Mirror the same clarification into `.github/skills/research/SKILL.md` §2 / finalisation guidance once the skills submodule can be updated through the `davidamitchell/Skills` repository.
