# 2026-05-20 -- Fix graph/search UI regressions + Playwright tests

**Completed:**
- `scripts/build_site.py` — stabilized graph simulation by switching weighted spring rest length to inverse scaling and adding velocity caps.
- `scripts/search/src/search-runtime.js` — unified search matching with the existing keyword matcher used by browse/all-items pages and removed worker bootstrap dependency for page search.
- `tests/test_build_site.py` — added regression assertions for graph stabilization and shared search matcher usage.
- `tests/ui/site-ui.spec.js` + `playwright.config.mjs` — added generated-site UI tests for graph visibility and landing/search consistency.
- `docs-adr/0017-search-matcher-and-playwright-ui-regression-tests.md` — recorded dependency and behavior decision.
- `CHANGELOG.md` + `docs-adr/README.md` — documented and indexed the change.

## Mini-Retro

1. **Did the process work?** Yes. Baseline checks, focused failing tests, minimal JS fixes, and generated-site Playwright coverage produced a verifiable fix.
2. **What slowed down or went wrong?** Playwright browsers were not installed on the runner initially, and the first UI locator was too brittle.
3. **What single change would prevent this next time?** Add `npx playwright install chromium` as an explicit setup step in future UI-testing sessions or CI jobs that run Playwright.
4. **Is this a pattern?** Yes — environment bootstrap for browser-based tests is recurring whenever Playwright is introduced in a fresh runner.
5. **Does any documentation need updating?** Yes; updated `CHANGELOG.md` and added ADR-0017 to capture the matcher and test-framework decision.
6. **Do the default instructions need updating?** Not required for this slice; current instructions already mandate generated-content verification and non-trivial testing.
