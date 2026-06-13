# 2026-06-13 -- Add backlog items (local-tooling-standardization-series)

**Completed:**

- `Research/backlog/2026-06-13-local-tooling-fragmentation-threshold-measurement.md` — foundational measurement item on when fragmented local tooling stops being a net productivity win and which indicators reveal the crossover.
- `Research/backlog/2026-06-13-local-global-optima-knowledge-work-throughput.md` — systems-thinking item on how local tooling optimisation degrades organisational throughput once handoffs, queues, and shared dependencies are included.
- `Research/backlog/2026-06-13-shadow-it-custom-tooling-governance-transition.md` — governance item on documented benefits, risks, and transition paths for shadow Information Technology (IT) and custom local tooling.
- `Research/backlog/2026-06-13-platform-engineering-innersource-hybrid-standardization.md` — operating-model item on platform engineering, InnerSource, and hybrid standard-core plus local-extension patterns.
- `Research/backlog/2026-06-13-standardization-customization-balance-context-ai.md` — synthesis item on how the right balance changes by industry, maturity, size, and Artificial Intelligence (AI) agent adoption.

**Addressing:** GitHub issue #623, which asked for the provided question set to be split into sensible thematic backlog items rather than researched in one monolithic item.

**Checks run before changes:**

- `git submodule update --init .github/skills` — passed
- `python -m pip install -e ".[dev]"` — passed
- `make check` — passed
- `python -m pytest tests/ -q` — 620 passed, 2 skipped, 1 expected environment-gated failure (`TAVILY_API_KEY` unset in the sandbox)

## Mini-Retro

1. **Did the process work?** Yes. The issue was already grouped into five coherent themes, so the research-question intake step mostly involved sharpening each group into a specific, answerable backlog item and adding dependency ordering where synthesis should come later.
2. **What slowed down or went wrong?** The main friction was not decomposition but source normalization: each seeded line of inquiry needed URL-backed starting points, and some named references required lookup before they could be recorded in repository-valid form.
3. **What single change would prevent this next time?** Ask issue authors to include direct URLs for every seeded paper, article, or framework they mention when requesting a split research series.
4. **Is this a pattern?** Yes. Structured intake issues that already contain multiple thematic clusters are best handled as a backlog series with one item per cluster and an optional synthesis item that blocks on the others.
5. **Does any documentation need updating?** No. Existing intake instructions already covered this workflow and the work here only applied them.
6. **Do the default instructions need updating?** No new convention emerged beyond an already-known pattern of converting a grouped issue into a linked backlog series.
