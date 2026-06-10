# 2026-06-10 -- Research Loop (togaf-motivation-architecture-driver-goal-requirement)

**Completed:**

Research item:
- `Research/completed/2026-05-31-togaf-motivation-architecture-driver-goal-requirement.md` — completed; TOGAF's motivation architecture is a taxonomy only: it names eight element types and five named relationships but specifies no validation rules, no cardinality constraints, and no formal semantics. The Motivation Extension is optional and the entire Driver-to-Requirement chain can be omitted from a TOGAF-compliant architecture. An automated goal validation system must therefore supply its own completeness and consistency rules from outside the framework (e.g. from GORE machinery or goal specification schemas).

Sources consulted:
- https://pubs.opengroup.org/architecture/togaf9-doc/arch/chap22.html (TOGAF 9.2 Architecture Content Metamodel; login-gated; accessed via secondary references)
- https://help.ardoq.com/en/articles/534168-frameworks-resources-togaf-v9-2-architecture-content-metamodel (Ardoq TOGAF metamodel reference — motivation element definitions and relationships)
- https://coe.qualiware.com/resources/togaf/9-1/part4-contentframework/content-metamodel/ (QualiWare CoE TOGAF 9.1 content metamodel reference — optional module status and tailoring)
- https://blog.coursemonster.com/what-has-changed-in-togaf-10/ (TOGAF 10 structural changes vs 9.2)
- https://togaf.visual-paradigm.com/2025/02/18/comprehensive-guide-to-togaf-10-enhancements-and-key-differences-from-togaf-9-2/ (TOGAF 9.2 vs 10 comparison)

## Mini-Retro

1. **Did the process work?** Yes. The item had already passed the automated review (review_count: 1, OVERALL: PASS) when this session began, so the work was to complete, update learnings.md, and commit.
2. **What slowed down or went wrong?** Nothing significant. The `python -m src.main research complete` command required using just the filename rather than the full path; this is a known quirk.
3. **What single change would prevent this next time?** Nothing to change — the handoff from the prior session was clean and the review log was unambiguous.
4. **Is this a pattern?** The `complete` command path sensitivity is a known minor friction but not worth a code change; the workaround (bare filename) is reliable.
