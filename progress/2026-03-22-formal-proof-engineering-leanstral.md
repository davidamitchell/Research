# 2026-03-22 — Research Loop (formal-proof-engineering-leanstral)

**Completed:**

Research item:
- `Research/completed/2026-03-18-formal-proof-engineering-leanstral.md` — completed; Leanstral appears to be a meaningful but narrow advance in Lean 4-based proof engineering rather than a general solution to agent safety. The strongest conclusion is that theorem-prover agents can deepen assurance for explicitly formalised properties, but they must still sit inside a wider guardrail stack that includes permissions, approval gates, backups, and operational discipline.

Sources consulted:
- https://mistral.ai/news/leanstral (official Leanstral announcement and positioning)
- https://lean-lang.org/doc/reference/latest/ (Lean 4 reference for kernel-checked proofs and tooling)
- https://www.tomshardware.com/tech-industry/artificial-intelligence/claude-code-deletes-developers-production-setup-including-its-database-and-snapshots-2-5-years-of-records-were-nuked-in-an-instant (incident summary for the Claude Code infrastructure-loss case)

## Mini-Retro

1. **Did the process work?** Yes. The file-based research loop, draft transition, external review workflow, and completion move all worked as designed.
2. **What slowed down or went wrong?** The first review pass exposed citation-discipline problems around shorthand references and local-path citations, and the second pass still annotated a fail even though the repository auto-passed on pass 2. Tavily-backed live testing also remained blocked by API quota exhaustion.
3. **What single change would prevent this next time?** Add a stricter local pre-review check that rejects shorthand citations like "sources above" and local repository paths inside audited sections before the first draft commit.
4. **Is this a pattern?** Yes. It matches the repository's known recurring pattern that research reviews fail most often on citation discipline and review-rubric compliance rather than on the underlying research content.
