# 2026-05-20 -- Align thread semantics with ontology direction

**Completed:**
- `scripts/build_site.py` — removed implicit tag-cluster thread generation from `detect_threads()`; threads now come from explicit `thread:` progression and concept clusters.
- `tests/test_build_site.py` — replaced implicit-thread expectations with tests asserting tag overlap does not create threads.
- `docs-adr/0015-gemini-ai-theme-enrichment.md` — added amendment note clarifying thread semantics change.

## Mini-Retro

1. **Did the process work?** Yes. A failing test first made the behavior shift safe and explicit.
2. **What slowed down or went wrong?** Fresh runner lacked dev dependencies (`pytest` missing), so validation had to pause for setup.
3. **What single change would prevent this next time?** Always run `pip install -e ".[dev]"` before the first test command in fresh sessions.
4. **Is this a pattern?** Yes; it recurs on fresh runners and is already documented as a recurring setup step.
5. **Does any documentation need updating?** Yes; ADR-0015 was amended to preserve the ontology/thread intent.
6. **Do the default instructions need updating?** No new instruction needed; existing guidance already covers setup and thread/ontology intent capture.
