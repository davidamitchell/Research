# 2026-05-20 -- Rebuild gh pages content request

**Completed:**
- Ran local site rebuild pipeline on branch `copilot/fix-ai-themes-in-graph`:
  - `npm run build:search-assets`
  - `python scripts/build_site.py`
- Confirmed full static site generation completed successfully.
- Cleared generated `docs/` deltas afterward to keep the feature branch free of committed generated site output.

## Mini-Retro

1. **Did the process work?** Yes. After installing missing JS and Python dependencies, the full site build completed end-to-end.
2. **What slowed down or went wrong?** First attempt failed because `esbuild` was not installed locally; second attempt failed because `sentence-transformers` was not installed.
3. **What single change would prevent this next time?** Run dependency bootstrap first (`npm install` and `pip install -e ".[dev]"`) before invoking the site rebuild.
4. **Is this a pattern?** Yes, fresh runner sessions frequently miss one or both dependency sets.
5. **Does any documentation need updating?** No additional docs update required; build requirements are already captured in workflow and repository notes.
6. **Do the default instructions need updating?** No; existing instructions already require avoiding `docs/` commits on feature branches.
