# 2026-05-20 -- Vector search stack redesign

**Completed:**
- `/home/runner/work/Research/Research/scripts/generate_index.py` — added build-time vector index generation using Sentence Transformers.
- `/home/runner/work/Research/Research/scripts/build_site.py` — switched search-index output to vector payload, added search runtime asset copying, and wired search/landing pages to module runtime.
- `/home/runner/work/Research/Research/scripts/search/src/search-worker.js` — added Web Worker for model loading, Orama index creation, and vector query execution.
- `/home/runner/work/Research/Research/scripts/search/src/search-runtime.js` — added lazy browser-side search controller with debounce and loading states.
- `/home/runner/work/Research/Research/scripts/search/build_search_assets.mjs` and `/home/runner/work/Research/Research/package.json` — added frontend bundling and dependencies (`@orama/orama`, `@xenova/transformers`, `esbuild`).
- `/home/runner/work/Research/Research/.github/workflows/build_site.yml` — added Node setup plus frontend asset build steps before site generation.
- `/home/runner/work/Research/Research/pyproject.toml` — added `sentence-transformers` dependency.
- `/home/runner/work/Research/Research/tests/test_build_site.py` — added/updated tests for vector-search script wiring and index enrichment behavior.

## Mini-Retro

1. **Did the process work?** Yes. The existing search architecture was isolated enough in `build_site.py` to swap indexing and wiring cleanly.
2. **What slowed down or went wrong?** Initial npm dependency pin for `@orama/orama` used a non-existent version and had to be corrected.
3. **What single change would prevent this next time?** Check npm package versions (`npm view <pkg> version`) before writing `package.json`.
4. **Is this a pattern?** Yes, version pin mistakes can recur when adding frontend dependencies to a primarily Python repository.
5. **Does any documentation need updating?** Not yet beyond workflow/build changes included in code; no additional user-facing docs were required for this slice.
6. **Do the default instructions need updating?** No new repository-wide instruction was identified beyond existing validation and dependency checks.
