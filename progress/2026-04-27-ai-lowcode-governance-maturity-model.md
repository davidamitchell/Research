# 2026-04-27 -- Research Loop (ai-lowcode-governance-maturity-model)

**Completed:**

Research item:
- `Research/completed/2026-04-26-ai-lowcode-governance-maturity-model.md` -- completed; the item concludes that the best enterprise AI and low-code governance maturity model is a five-stage hybrid that combines staged appraisal logic, AI-specific capability pillars, and governance-system baselines. It also argues that maturity claims should be evidence-based, gated by the weakest mandatory control layer, and capped by behavioural adoption rather than averaged across dimensions.

Sources consulted:
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/maturity-model-overview (public five-level AI maturity model)
- https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10 (official AI RMF 1.0 publication record)
- https://cmmiinstitute.com/learning/appraisals (public CMMI appraisal and benchmark model overview)

## Mini-Retro

1. **Did the process work?** Yes, the second review cycle passed and the research workflow behaved as expected once the synthesis claims were narrowed and the tables were made explicitly inferential and source-bound.
2. **What slowed down or went wrong?** The first review failure came from two avoidable issues: comparative wording that outran the evidence, and unlabeled synthesis tables whose rows read like settled facts instead of designed inferences.
3. **What single change would prevent this next time?** Add an explicit prompt rule that every non-Evidence-Map synthesis table in `§6 Synthesis` and `## Findings` must carry row-level epistemic labels and row-level sources.
4. **Is this a pattern?** Yes, it is adjacent to the existing claim-label failure pattern: tables hide unsupported synthesis more easily than paragraphs do, so they need to be treated as claim-bearing structures by default.

## Applied improvements

- Updated `research-prompt.md` with a new **Synthesis-table audit** rule requiring row-level labels and row-level sources for stage tables, capability matrices, progression tables, and assessment tables.

## Pending skill improvements

- Mirror the new synthesis-table audit rule into `.github/skills/research/SKILL.md` or the companion citation-discipline skill when the skills submodule can be updated from the `davidamitchell/Skills` repository.
