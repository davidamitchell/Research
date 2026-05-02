# 2026-05-02 -- Research Loop (self-modifying-agent-architectures)

**Completed:**

Research item:
- `Research/completed/2026-05-01-self-modifying-agent-architectures.md` -- completed; the item concludes that live self-modification is a real coding-agent capability with clear local adaptation value, but current evidence supports it as an expert-oriented, governance-heavy control surface rather than a proven general default. It also identifies a bounded middle path, in-session extension authoring under explicit permissions and visible mutation boundaries, as the most plausible compromise worth testing next.

Sources consulted:
- https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md (Pi runtime extension surface and reload model)
- https://intelligence.org/files/Corrigibility.pdf (formal corrigibility constraints on self-modifying agents)
- https://aider.chat/docs/usage/commands.html (bounded comparison harness with explicit user-steered control)

## Mini-Retro

1. **Did the process work?** Yes, but only after the external review surfaced two over-strong comparative claims and one missing citation discipline check on assumption bullets.
2. **What slowed down or went wrong?** The first draft treated a comparative ranking as too settled and left `[assumption]` bullets in `## Research Skill Output` without URL-backed source anchors, which the review workflow correctly rejected.
3. **What single change would prevent this next time?** Add an explicit self-review rule that every visible `[assumption]` bullet in `## Research Skill Output`, especially `§0` working hypotheses and `§6 Assumptions`, must carry URL-backed source context.
4. **Is this a pattern?** Yes. It matches the repository's existing citation-discipline failure pattern rather than a genuinely new class of problem.

## Applied improvements

- Updated `research-prompt.md` to add an explicit `Assumption-source audit` check in the self-review checklist so future sessions do not leave visible `[assumption]` bullets without URL-backed source context.
