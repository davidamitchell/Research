# 2026-04-30 -- Add backlog item: Explainable AI (XAI) regulation and governance

**Completed:**
- `Research/backlog/2026-04-30-explainable-ai-xai-regulation-governance.md` — added from issue; asks what the current state of Explainable Artificial Intelligence (XAI) research is, who leads it and what the primary techniques are, and how XAI intersects with regulatory obligations, audit requirements, and accountability for automated decisions in heavily regulated industries such as financial services and healthcare

**Note on skills submodule:** The `.github/skills/` submodule was not initialised in the agent environment. The research-question skill process was applied from the documented instructions in `.github/copilot-instructions.md`. Items created using the documented template and process.

## Mini-Retro

1. **Did the process work?** Yes. The issue framing ("what is it, who's leading the research, latest stance, overlap with regulation and auditing") translated cleanly into a compound but decomposable research question. The five-test quality check (Specific, Answerable, Scoped, Motivated, Decomposable) passed without needing significant revision. The only rewrite was combining the issue's implied sub-topics into a single well-scoped question rather than leaving them as a bullet list.

2. **What slowed down or went wrong?** Nothing significant. The tag vocabulary (`docs/tag-vocabulary.md`) doesn't include `explainability` or `audit` as canonicalised tags — both were added as new tags to this item. If these appear in more items, they should be reviewed for canonicalisation in the next tag-report run.

3. **What single change would prevent this next time?** Nothing to fix — the process worked. The one gap is that `explainability` and `audit` are not in the canonical tag vocabulary; if either appears in two or more further items, raise a BACKLOG entry to canonicalise them via `scripts/tag_report.py`.

4. **Is this a pattern?** No new pattern. Consistent with the multi-question backlog intake sessions from 2026-04-26.
