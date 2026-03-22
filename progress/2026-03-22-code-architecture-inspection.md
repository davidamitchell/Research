# 2026-03-22 — Research Loop (code-architecture-inspection)

**Completed:**

Research item:
- `Research/completed/2026-03-22-code-architecture-inspection.md` — completed; the item concludes that cross-repository architecture inspection works best as a layered pipeline: deterministic extractors gather structural facts first, policy and fitness-function layers evaluate drift second, and Copilot-skill or RepoSwarm-style agents synthesize those facts into reviewable blueprints last. It also finds that no single tool provides complete architecture truth, so durable implementations compose dependency surfaces, provenance-preserving normalization, policy checks, and remediation tooling rather than relying on one architecture prompt or dashboard.

Sources consulted:
- https://raw.githubusercontent.com/github/awesome-copilot/main/skills/architecture-blueprint-generator/SKILL.md (GitHub Copilot architecture skill definition)
- https://raw.githubusercontent.com/reposwarm/reposwarm/main/README.md (RepoSwarm multi-repo architecture workflow overview)
- https://raw.githubusercontent.com/sverweij/dependency-cruiser/main/README.md (dependency-cruiser dependency analysis capabilities)

## Mini-Retro

1. **Did the process work?** Yes. The research loop, draft push, automated review, fix pass, completion move, and synthesis update all worked end-to-end.
2. **What slowed down or went wrong?** The main slowdown was the review workflow surfacing citation-discipline issues late in the process, especially shorthand citations, claim-bearing table notes, and uncited reflective sections that looked harmless on manual review.
3. **What single change would prevent this next time?** Add a stricter pre-draft self-check for claim-bearing table notes, recursive-review bullets, and assumption justifications so citation problems are caught before the first external review run.
4. **Is this a pattern?** Yes. It matches the repository's known recurring pattern that review failures often come from claim-bearing sections outside the obvious Findings bullets, especially citation discipline and labeling in tables and review/meta sections.
