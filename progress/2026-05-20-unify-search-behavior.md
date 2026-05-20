# 2026-05-20 -- Unify search behavior across pages

**Completed:**
- `scripts/build_site.py` — unified browse, landing, and search page matching semantics via shared search utilities (`normalizeSearchText`, `scoreSearchMatch`, `debounce`), added token-form expansion and acronym aliases, and switched all search inputs to debounced matching.
- `tests/test_build_site.py` — added regression coverage asserting all search scripts share the same matcher/debounce logic.

## Mini-Retro

1. **Did the process work?** Yes. Adding a failing test first helped lock the requirement that all search scripts use one matching approach.
2. **What slowed down or went wrong?** Fresh-runner dependency gaps (`pytest` missing) and formatting checks required extra cycles.
3. **What single change would prevent this next time?** Install dev dependencies (`pip install -e ".[dev]"`) before the first test/lint command.
4. **Is this a pattern?** Yes, this environment bootstrap issue is recurring.
5. **Does any documentation need updating?** No user-facing behavior docs required beyond the code/test updates in this slice.
6. **Do the default instructions need updating?** No; current instructions already capture setup and validation expectations.
