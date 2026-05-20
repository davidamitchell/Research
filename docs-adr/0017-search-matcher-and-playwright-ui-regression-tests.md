# ADR-0017: Shared keyword matcher for site search and Playwright UI regression tests

Date: 2026-05-20
Status: accepted

## Context

Issue #575 reported two user-facing regressions on generated GitHub Pages output:

1. The graph view appeared unstable ("bounces around and then goes away").
2. The Search tab appeared non-functional for users.

The search page used a browser-side semantic worker that depended on model loading and worker bootstrap, while other pages (`browse`, `all-items`, and tag pages) used the inline `scoreSearchMatch` keyword matcher. This violated the requirement that search behavior be consistent across the site.

We also needed executable UI regression coverage against generated pages (not just generator-unit assertions).

## Decision

1. Use the same keyword matcher (`normalizeForSearch`, tokenization, and `scoreSearchMatch`) in `scripts/search/src/search-runtime.js` that is already used by browse-style pages.
2. Remove the runtime dependency on browser worker bootstrap for page-level search interaction; the runtime now fetches `search-index.json` and performs the same keyword scoring directly.
3. Add Playwright as a dev dependency (`@playwright/test`) with repository-owned UI regression tests and a local generated-site web server in `playwright.config.mjs`.
4. Keep the graph force simulation implementation in `scripts/build_site.py` but stabilize it by using inverse rest-length scaling with edge weight and velocity caps.

## Consequences

### Positive
- Search behavior is consistent across landing and search pages and aligned with existing browse-page matcher semantics.
- Search functionality no longer depends on client-side model bootstrap to return results.
- UI regressions now have executable Playwright coverage against generated pages.
- Graph layout is more stable under weighted edges and does not collapse visually after simulation settles.

### Negative / Trade-offs
- Added a new JavaScript dev dependency (`@playwright/test`) and browser-install requirement for local UI test execution.
- Playwright tests add runtime to validation when run.

### Neutral
- `search-worker.js` remains part of built assets but is no longer required by the runtime entry path.
