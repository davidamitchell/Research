# 2026-05-03 — W-0059 Process Evaluation Harness

**Completed:**
- `scripts/eval_harness.py` — process evaluation harness with sampling, extraction, prompt building, deterministic scoring, and JSON + Markdown report output
- `tests/test_eval_harness.py` — 57 unit tests; all passing
- `.github/workflows/eval-harness.yml` — manual workflow dispatch
- `BACKLOG.md` — W-0059 added as `done`

**Design summary:**
The harness works in two stages: (1) prompt generation — sample N random completed items, extract context, build process prompts; (2) scoring — when LLM responses are provided, compute structural completeness (required pattern presence) and coverage overlap (word-level Jaccard vs the original Approach or Key Findings section). Three processes are included: `perspective-discovery` (§0.5b), `question-decomposition` (§1), `adversarial-challenge` (§4.5). Seeds make samples reproducible for A/B comparison of process variants.

## Mini-Retro

1. **Did the process work?** Yes. `make check` + 418 tests passing. The two-stage design (prompt bundle first, scoring second) makes the harness usable without LLM credentials.
2. **What slowed down or went wrong?** Two ruff lint fixes needed (f-string without placeholder; format). Both caught by `make check` before push.
3. **What single change would prevent this next time?** Run `ruff format .` before `make check` — the formatter catches the f-string and whitespace issues that the linter reports as errors.
4. **Is this a pattern?** Yes — format-before-check is a known pattern. Already in Quick Reference item 7, but the order (`ruff format` then `make check`) is not explicit. No change needed to instructions.
5. **Does any documentation need updating?** No. The harness is self-documenting via `--list-processes` and the BACKLOG entry.
6. **Do the default instructions need updating?** No new conventions emerged.
