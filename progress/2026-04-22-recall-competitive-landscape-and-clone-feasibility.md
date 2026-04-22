# 2026-04-22 -- Research Loop (recall-competitive-landscape-and-clone-feasibility)

**Completed:**

Research item:
- `Research/completed/2026-04-22-recall-competitive-landscape-and-clone-feasibility.md` -- completed; Recall's public product surface is broader than a simple read-it-later tool because it combines capture, summarization, chat, auto-organization, linked knowledge, review workflows, and export. The strongest internal clone path is a web-first build on `Personal-Assistant-` plus this repository's ingestion patterns, with a deliberately narrower first release focused on save, summarize, search, chat, note, and export rather than full Recall parity.

Sources consulted:
- https://www.getrecall.ai (Recall homepage and positioning)
- https://docs.getrecall.ai/getting-started/5-linking-content (Recall linking and graph features)
- https://github.com/davidamitchell/Personal-Assistant-/blob/main/README.md (Closest internal codebase for a clone)

## Mini-Retro

1. **Did the process work?** Yes, the draft-review loop caught several classification and terminology issues that were easier to fix before completion than after publication.
2. **What slowed down or went wrong?** The review workflow surfaced additional domain-term and confidence-level issues on the second pass, and the workflow's write-back commit required another rebase before the final push.
3. **What single change would prevent this next time?** Expand or plainly define domain terms such as "graph database," "active recall," and "spaced repetition" at their first use during the initial draft instead of waiting for review feedback.
4. **Is this a pattern?** Yes, it is adjacent to the existing recurring pattern around acronym and terminology discipline: first-use clarity failures are still a common review trigger even when source coverage is otherwise strong.

## Applied improvements

- Tightened the completed item so domain-specific terms are defined at first use, evaluative claims stay labeled as inferences, and strategic recommendations use confidence levels consistent with the evidence.
- Updated `research-prompt.md` so the inline domain-term clarity check now explicitly calls out "graph database," "active recall," and "spaced repetition" as first-use terms to define or source.
