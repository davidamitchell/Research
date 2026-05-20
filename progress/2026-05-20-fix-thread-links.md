# 2026-05-20 -- Fix broken thread links

**Completed:**
- `scripts/build_site.py` — added `make_unique_slug()` and applied it to explicit/concept thread slug generation so thread URLs are always non-empty and collision-safe.
- `tests/test_build_site.py` — added regression tests for non-ASCII explicit thread titles and slug-collision handling.

## Mini-Retro

1. **Did the process work?** Yes. Repro via failing regression tests gave a clear path to a minimal, robust fix.
2. **What slowed down or went wrong?** Test execution initially failed because dev dependencies were missing on the fresh runner.
3. **What single change would prevent this next time?** Run `pip install -e ".[dev]"` immediately at session start before the first test command.
4. **Is this a pattern?** Yes, this setup issue is recurring on fresh runners.
5. **Does any documentation need updating?** No additional docs required; behavior remains internal URL-hardening with test coverage.
6. **Do the default instructions need updating?** No; current instructions already capture this environment setup pattern.
