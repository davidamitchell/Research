# 2026-05-19 -- Research Loop (rq2-1-erm-causal-blindness)

**Completed:**

Research item:
- `Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md` -- completed; the item shows that Empirical Risk Minimisation guarantees low error only on new samples from the same distribution, not on environment change. It then connects that narrow guarantee to spurious-correlation failure, positions Invariant Risk Minimisation as one formal correction, and links the result back to the repository's earlier mechanism-versus-interpolation and instrumentalism work.

Sources consulted:
- https://moodle2.units.it/pluginfile.php/757668/mod_resource/content/1/Shalev-Shwartz%20and%20Ben-David%20-%20Understanding%20Machine%20Learning.pdf (ERM, overfitting, and PAC definitions)
- https://arxiv.org/abs/1907.02893 (IRM objective, invariance examples, and OOD framing)
- https://arxiv.org/abs/2102.11107 (causal representation learning framing for robustness beyond i.i.d. settings)

## Mini-Retro

1. **Did the process work?** Yes. The loop produced a usable draft quickly, and the review workflow surfaced the exact places where source scope and first-use term clarity needed tightening.
2. **What slowed down or went wrong?** The main friction was repeated review failures on central theoretical terms and confidence calibration in the synthesis, not on the evidence gathering itself.
3. **What single change would prevent this next time?** Force an explicit self-review of the first sentence in `§6 Synthesis` and the Findings Executive Summary so that central terms are defined in plain language or linked to an authoritative definition before the first review run.
4. **Is this a pattern?** Yes. It matches the repository's recurring pattern where review failures come from first-use clarity and citation-discipline issues rather than from missing sources.

## Applied improvements

- Updated `research-prompt.md` to add an explicit first-sentence audit for `§6 Synthesis` and the Findings Executive Summary, targeting central theoretical terms such as ERM, PAC learning, IRM, causal mechanism, invariant structure, and out-of-distribution generalisation.
