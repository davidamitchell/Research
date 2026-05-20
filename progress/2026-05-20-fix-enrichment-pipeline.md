# 2026-05-20 -- Fix enrichment pipeline graph/prompt/workflow integration

**Completed:**
- `/home/runner/work/Research/Research/scripts/build_site.py` — added `ai_themes` extraction in loaders, graph node field wiring, `theme-overlap` edge generation, graph relationship validation, graph UI filter/color support, and search index theme text.
- `/home/runner/work/Research/Research/scripts/enrich_items.py` — replaced 400-char summary prompt input with structured Research Question + Scope + Findings context extraction and markdown-to-plain-text cleanup.
- `/home/runner/work/Research/Research/.github/workflows/enrich-items.yml` — removed `push` trigger and replaced silent push (`|| true`) with pull-rebase-push semantics.
- `/home/runner/work/Research/Research/docs-adr/0015-gemini-ai-theme-enrichment.md` — added a dated amendment documenting trigger rollback and the graph/prompt design updates.
- `/home/runner/work/Research/Research/tests/test_enrich_items.py` and `/home/runner/work/Research/Research/tests/test_build_site.py` — updated coverage for prompt context extraction, theme-overlap graph behavior, and ai_themes loading.

## Mini-Retro

1. **Did the process work?** Yes. The issue was reproducible from code inspection and resolved with targeted changes and tests.
2. **What slowed down or went wrong?** Playwright screenshot capture could not run because the browser profile was locked by another process in the environment.
3. **What single change would prevent this next time?** Start UI verification with an isolated Playwright browser context or pre-clear existing browser sessions.
4. **Is this a pattern?** It appears occasionally in shared runner environments; not yet a repeated repository-specific pattern.
5. **Does any documentation need updating?** ADR-0015 was updated with a dated amendment; no additional user-facing README changes were required for this fix scope.
6. **Do the default instructions need updating?** No new durable convention emerged beyond existing guidance.
