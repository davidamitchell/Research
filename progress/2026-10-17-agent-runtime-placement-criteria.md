# 2026-10-17 — Add backlog item (agent-runtime-placement-criteria)

**Completed:**
- `Research/backlog/2026-10-17-agent-runtime-placement-criteria.md` — added from issue #671; defines a research question and comparison framework for deciding where regulated software-engineering agent workloads should run.

## Mini-Retro

1. **Did the process work?** Yes. The research-question quality check confirmed the request is specific, answerable, scoped, motivated, and decomposable.
2. **What slowed down or went wrong?** The skills submodule needed initialization before its research-question skill could be read. `ruff check` passed, but formatting checks found four violations in existing completed research items; the test suite had one failure because `TAVILY_API_KEY` was not set (620 passed, 2 skipped).
3. **What single change would prevent this next time?** Initialize the skills submodule at session start when it is empty.
4. **Is this a pattern?** No evidence of a recurring issue in this session.
5. **Does any documentation need updating?** No; this request only adds a research backlog item.
6. **Do the default instructions need updating?** No new convention or constraint emerged.
