# 2026-05-01 -- Research Loop (human-oversight-ai-software-development)

**Completed:**

Research item:
- `Research/completed/2026-05-01-human-oversight-ai-software-development.md` -- completed; the item concludes that human oversight remains an effective software-quality gate mainly because expert review, ownership, and maintenance responsibility still constrain what can be safely accepted into a codebase. It also narrows the operational claim: the strongest support is for selective escalation of review intensity as coupling, ambiguity, and failure cost rise, not for a universally benchmarked fixed review protocol.

Sources consulted:
- https://www.research.ibm.com/journal/sj/153/ibmsj1503C.pdf (Fagan inspections reprint on early defect removal and inspection economics)
- https://link.springer.com/article/10.1007/s10664-015-9381-9 (McIntosh et al. on code-review coverage, participation, and reviewer expertise)
- https://www.microsoft.com/en-us/research/publication/dont-touch-my-code-examining-the-effects-of-ownership-on-software-quality/ (ownership and software-quality evidence)

## Mini-Retro

1. **Did the process work?** Yes, but only after the review loop forced the policy recommendations to stay inside what the evidence actually supported.
2. **What slowed down or went wrong?** I over-compressed governance guidance, prior-item synthesis, and software-review heuristics into claims that read more benchmarked than they really were.
3. **What single change would prevent this next time?** Nothing beyond the existing review loop; it surfaced the overclaim quickly enough.
4. **Is this a pattern?** Partly, but it is already covered by the repo's emphasis on confidence-evidence alignment and source-bounded synthesis rather than a new undocumented pattern.
