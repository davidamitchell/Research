# 2026-03-19 — Research Loop (trusting-trust-ai-corpus-contamination)

**Completed:**

Research item:
- `Research/completed/2026-03-15-trusting-trust-ai-corpus-contamination.md` — completed; the item concludes that the best web-scale analogue of Thompson's trusting-trust problem is recursive corpus contamination rather than a literal backdoor. It also narrows the prevalence claim: accessible evidence supports substantial synthetic saturation of the web, but not a settled claim that half of all web text is AI-generated, and it argues that provenance now matters for source independence as well as freshness.

Sources consulted:
- https://www.cs.cmu.edu/afs/cs/academic/class/15712-f08/www/lectures/Thompson84lecture.pdf (Ken Thompson's original trusting-trust lecture)
- https://www.nature.com/articles/s41586-024-07566-y (Nature paper on model collapse under recursive training)
- https://arxiv.org/abs/2504.08755 (Estimate of AI-generated text share on active web pages)

## Mini-Retro

1. **Did the process work?** Yes — the structured research workflow produced a solid first draft, and the second external review pass succeeded after targeted fixes.
2. **What slowed down or went wrong?** The review workflow surfaced stricter-than-expected requirements for inline sourcing and speculation labels inside `## Findings`, and the local checkout repeatedly carried the unstaged backlog-file deletion from `research start`, which blocked `git pull --rebase` until stashed.
3. **What single change would prevent this next time?** Add a pre-draft checklist item to treat `## Context` and every subsection of `## Findings` as citation-disciplined prose with inline labels/sources, not as looser summary text.
4. **Is this a pattern?** Yes — review failures for missing inline sourcing/speculation control are an established pattern in this repo, while the unstaged move from `research start` looks like a repeatable workflow nuisance worth remembering.
