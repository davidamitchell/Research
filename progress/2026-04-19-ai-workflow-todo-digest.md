# 2026-04-19 -- Research Loop (ai-workflow-todo-digest)

**Completed:**

Research item:
- `Research/completed/2026-04-03-ai-workflow-todo-digest.md` -- completed; the strongest checked pattern was a scheduled digest pipeline over one canonical task source with schema-first extraction and bounded push delivery. The item also clarified that memory systems complement retrieval and continuity, but do not replace scheduled digests because they do not solve proactive surfacing or timing on their own.

Sources consulted:
- https://zapier.com/apps/notion/integrations/slack (official Notion-to-Slack automation documentation)
- https://n8n.io/workflows/10286-ai-meeting-summary-and-action-item-tracker-with-notion-slack-and-gmail/ (public structured digest workflow with explicit extraction fields)
- https://link.springer.com/article/10.1007/s41233-023-00060-9 (Human-Computer Interaction review on interruption and proactive delivery timing)

## Mini-Retro

1. **Did the process work?** Yes, but only after a full review-driven tightening pass on evidence labels, confidence levels, and citation quality.
2. **What slowed down or went wrong?** The first draft under-audited non-obvious review surfaces: Context prose, Evidence Map rows, and claims that indirectly depended on an inaccessible seed video transcript.
3. **What single change would prevent this next time?** Add an explicit self-review rule that Context and Evidence Map prose need the same claim-label and source-binding audit as Findings, and forbid inaccessible seed media from being cited as direct support for downstream factual claims.
4. **Is this a pattern?** Yes, it matches the broader citation-discipline failure class already seen in this repository, even though this instance was about claim surfaces and source accessibility rather than acronym expansion.

## Applied improvements

- Updated `research-prompt.md` to add a dedicated Context and Evidence Map audit rule, including a check that inaccessible seed media cannot be used as direct support for downstream factual claims.

## Pending skill improvements

- Mirror the new Context/Evidence Map audit rule into `.github/skills/research/SKILL.md` when the Skills submodule is next updated in `davidamitchell/Skills`.
