# 2026-03-20 — Research Loop (vl-jepa-concept-prediction)

**Completed:**

Research item:
- `Research/completed/2026-03-16-vl-jepa-concept-prediction.md` — completed; VL-JEPA predicts semantic answer embeddings from visual input and optional text queries rather than generating answer tokens directly, and the paper reports stronger matched-condition results with about 50 percent fewer trainable parameters than a token-generative baseline. For developer consumers of GitHub Copilot and Claude Code, the practical takeaway is not direct model access but a workflow pattern: separate multimodal perception from planning and decode to text only when a human or downstream tool needs it.

Sources consulted:
- https://arxiv.org/abs/2512.10942 (VL-JEPA paper abstract and benchmark summary)
- https://openreview.net/pdf?id=BZ5a1r-kVsf (Yann LeCun world-model thesis and JEPA framing)
- https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/provide-visual-inputs (GitHub Copilot visual-input developer surface)

## Mini-Retro

1. **Did the process work?** Yes. The item was already in `reviewing` with `review_count: 1`, so resuming from the existing state and completing it was straightforward.
2. **What slowed down or went wrong?** The main source gap was the unavailable Meta AI VL-JEPA landing page, which meant the item had to rely on the arXiv paper and related primary sources instead of a canonical Meta summary page.
3. **What single change would prevent this next time?** A lightweight source-availability check at the start of research would surface dead official links earlier and reduce rework during synthesis.
4. **Is this a pattern?** Mildly. Official landing pages disappearing or returning `404` is a recurring research-source reliability issue, but it fits existing source-discipline guidance rather than requiring a new pattern.
