# 2026-05-20 -- Complete research item (how-do-activation-energy-barriers-shape-knowledge-seeking-behaviour)

**Completed:**
- `Research/completed/2026-05-19-how-do-activation-energy-barriers-shape-knowledge-seeking-behaviour.md` -- completed the item after research-review pass; the final synthesis concludes that knowledge seeking is often blocked at the first-contact step by expertise-discovery cost, access uncertainty, and social-image risk, and that organisations lower those threshold costs with expert directories, scheduled access, peer mentoring, and psychologically safe coaching.
- `learnings.md` -- updated Thread 2 to capture first-contact transaction costs as a distinct coordination-overhead mechanism.
- `research-prompt.md` -- tightened the self-review checklist to force explicit audits of unsupported ranking and magnitude wording before draft submission.

**Important sources:**
- [Borgatti and Cross (2003) A Relational View of Information Seeking and Learning in Social Networks](https://doi.org/10.1287/mnsc.49.4.432.14428)
- [Lee (2002) The Social Costs of Seeking Help](https://doi.org/10.1177/0021886302381002)
- [Edmondson (1999) Psychological Safety and Learning Behavior in Work Teams](https://doi.org/10.2307/2666999)

## Mini-Retro

1. **Did the process work?** Yes. The draft-review-fix-review-complete loop caught the main overclaiming problems before completion and produced a tighter final synthesis.
2. **What slowed down or went wrong?** The first review failure came from comparative and magnitude wording that reached beyond what the cited sources directly quantified, especially where the sources supported a mechanism but not a ranking.
3. **What single change would prevent this next time?** Add an explicit self-review check for ranking and magnitude phrases such as "most reliably," "strongest," and "falls sharply," and require direct comparative evidence before keeping them.
4. **Is this a pattern?** Yes. It is the same class as earlier comparative-claim and confidence-alignment review failures, so it should be treated as a recurring review-risk pattern rather than a one-off miss.
5. **Does any documentation need updating?** Yes. `research-prompt.md` now includes an explicit magnitude-and-ranking wording audit in the self-review checklist.
6. **Do the default instructions need updating?** No change needed in `.github/copilot-instructions.md`; the sharper guard belongs in the research prompt and possibly the upstream read-only research skill.

## Pending skill improvements

- `.github/skills/research/SKILL.md` is read-only in this repository. The same ranking-and-magnitude wording guard may be worth proposing upstream in `davidamitchell/Skills` if this failure mode appears again.
