# 2026-05-11 — Gemini AI theme enrichment pipeline

**Completed:**
- `src/pipeline/__init__.py` — new package init
- `src/pipeline/_gemini.py` — Gemini client factory, rate limiter, model cascade (ported from Latest-developments-)
- `scripts/enrich_items.py` — backfill script: adds `ai_themes` frontmatter to completed items
- `.github/workflows/enrich-items.yml` — `workflow_dispatch` trigger for backfill and single-item enrichment
- `config/sources.yaml` — added `gemini.gemini_model: gemini-3-flash`
- `pyproject.toml` — added `google-genai>=1.0.0` to dependencies
- `tests/test_pipeline_gemini.py` — 22 unit tests for `_gemini.py` (47 total pass, 1 integration skipped)
- `tests/test_enrich_items.py` — 26 unit tests for `enrich_items.py`
- `docs-adr/0015-gemini-ai-theme-enrichment.md` — ADR for new dependency, workflow, and schema change
- `.github/copilot-instructions.md` — added `GEMINI_API_KEY` to credentials table

## Mini-Retro

1. **Did the process work?** Partially. The initial implementation used bare httpx REST calls instead of the `google-genai` SDK. The model cascade also used wrong model IDs (`gemini-3.0-flash` instead of `gemini-3-flash`). These were caught by the owner redirecting to the canonical sibling repo (`Latest-developments-`).

2. **What slowed down or went wrong?** Two root causes: (a) the first implementation did not check the sibling repo's established pattern before starting — the `Latest-developments-` repo had already solved this problem with `_HeaderCapturingClient`, `_RateLimiter`, and `_ModelCascade`; (b) `make check` revealed several ruff violations that required a second pass (N806 uppercase variable, E741 ambiguous name, unsorted imports, unused import).

3. **What single change would prevent this next time?** Before building a new integration with an external API, check whether any sibling repo already has a working implementation. The copilot-instructions explicitly say to look at `Latest-developments-` for the Gemini pipeline pattern.

4. **Is this a pattern?** Yes — re-implementing what already exists in a sibling repo is a recurring risk when starting a new session without reading the full context. The fix is: read copilot-instructions first, then search sibling repos before writing a line of new integration code.

5. **Does any documentation need updating?** Yes — ADR-0015 written. `GEMINI_API_KEY` added to the credentials table. `docs-adr/README.md` updated.

6. **Do the default instructions need updating?** The copilot-instructions already say to check `Latest-developments-` for the Gemini pipeline pattern (implicitly, via the ADR references). No change needed — the issue was failing to read the instructions before starting.
