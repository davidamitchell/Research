# 2026-04-30 -- Add backlog items: Explainable AI (XAI) regulation and governance (and two related items)

**Completed:**
- `Research/backlog/2026-04-30-explainable-ai-xai-regulation-governance.md` — added from issue; asks what the current state of Explainable Artificial Intelligence (XAI) research is, who leads it and what the primary techniques are, and how XAI intersects with regulatory obligations, audit requirements, and accountability for automated decisions in heavily regulated industries such as financial services and healthcare
- `Research/backlog/2026-04-30-human-bias-ai-trust-rlhf-sycophancy.md` — added from PR comment; asks to what extent humans systematically over-trust AI-generated explanations, covering automation bias, Reinforcement Learning from Human Feedback (RLHF)-induced sycophancy in post-training, and the polysemantic nature of hidden-layer neurons (h-neurons) as revealed by mechanistic interpretability research
- `Research/backlog/2026-04-30-orthogonality-thesis-ai-alignment-interpretability.md` — added from PR comment; asks what the orthogonality thesis is, what the current evidence for and against it is, and what its practical implications are for XAI — specifically whether explaining *what* a model did is sufficient when the thesis implies we cannot infer *why* from capability alone

The `related` field of `2026-04-30-explainable-ai-xai-regulation-governance.md` was updated to cross-link the two new items.

**Note on skills submodule:** The `.github/skills/` submodule was not initialised in the agent environment. The research-question skill process was applied from the documented instructions in `.github/copilot-instructions.md`. Items created using the documented template and process.

## Mini-Retro

1. **Did the process work?** Yes. The original issue framing translated cleanly. The PR comment added two closely related topics that warranted separate items given their distinct scope: human cognitive bias is empirical and governance-focused; the orthogonality thesis is philosophical/alignment-focused with regulatory implications. Keeping them separate preserves the single-question principle.

2. **What slowed down or went wrong?** Nothing significant. The tag vocabulary (`docs/tag-vocabulary.md`) doesn't include `explainability`, `audit`, `cognitive-bias`, `rlhf`, or `mechanistic-interpretability` as canonicalised tags. All added as new tags across the three items. If these appear in further items, they should be reviewed for canonicalisation in the next tag-report run.

3. **What single change would prevent this next time?** Nothing to fix — the process worked. The one gap is the expanding tag vocabulary; if `mechanistic-interpretability` or `rlhf` appear in more items, raise a BACKLOG entry to canonicalise them.

4. **Is this a pattern?** No new pattern. Consistent with the multi-question backlog intake sessions from 2026-04-26.
