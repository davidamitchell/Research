# 2026-05-16 -- Research Loop (reference-architecture-definition-frameworks-detail)

**Completed:**

Research item:
- `Research/completed/2026-05-16-reference-architecture-definition-frameworks-detail.md` -- completed; the item concludes that a practical reference architecture is a reusable architecture description built from stakeholder-oriented views, components, flows, and constraints rather than an implementation blueprint. It also separates conceptual, logical, and implementation architecture levels and clarifies that stakeholder requests for a "reference architecture" often conflate vocabulary, reusable pattern, and bounded implementation needs.

Sources consulted:
- https://www.iso.org/standard/74393.html (ISO/IEC/IEEE 42010 architecture-description structure)
- https://www.opengroup.org/architecture/togaf7-doc/arch/p4/views/vus_intro.htm (The Open Group views and viewpoints guidance)
- https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-service-web-app/basic-web-app (Azure reference architecture example with workflow, components, and considerations)

## Mini-Retro

1. **Did the process work?** Yes, but only after the review loop forced tighter separation between direct facts, cross-source synthesis, and pure metadata fragments in `§7`.
2. **What slowed down or went wrong?** The main drag was review churn on comparative framework claims and on first-use term-definition handling inside Findings, plus the need to keep `§6 Synthesis` and `## Findings` mirrored while fixing both.
3. **What single change would prevent this next time?** Nothing in `research-prompt.md`; the existing checks were sufficient once the review log surfaced the exact violations.
4. **Is this a pattern?** Yes. It matches the known pattern that research reviews most often fail on citation discipline, acronym or term first use, and comparative synthesis claims that should default to `[inference]`.

## Pending skill improvements

- `.github/skills/research/SKILL.md` should add an explicit reminder that `§7 Recursive Review` lines must remain pure metadata fragments unless they are fully labeled and source-bound.
- `.github/skills/citation-discipline/SKILL.md` should add a sharper rule that cross-source comparisons such as "framework A is structural while framework B is operational" default to `[inference]`, even when each individual source is authoritative.
