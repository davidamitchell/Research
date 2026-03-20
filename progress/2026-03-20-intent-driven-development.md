# 2026-03-20 — Research Loop (intent-driven-development)

**Completed:**

Research item:
- `Research/completed/2026-03-16-intent-driven-development.md` — completed; the item concludes that Intent Driven Development (IDD) is currently an emerging intent-first, validation-heavy practice rather than a settled standalone standard. It finds that the strongest public implementations layer goals, boundaries, policies, context, tests, and contracts together, with StrongDM Factory providing the clearest radical example and with standardized schemas, policy protocols, and comparative outcome evidence still unresolved.

Sources consulted:
- https://factory.strongdm.ai/ (StrongDM Factory narrative and operating principles)
- https://keyholesoftware.com/intent-driven-development-build-first-documentation/ (conservative enterprise framing of Intent Driven Development)
- https://martinfowler.com/bliki/TestDrivenDevelopment.html (baseline definition of Test Driven Development for comparison)

## Mini-Retro

1. **Did the process work?** Yes. The start → research → draft → review → complete loop worked as intended, and the review workflow successfully wrote back `review_count: 1`.
2. **What slowed down or went wrong?** The main slowdown was formatting discipline: the first full draft needed a follow-up pass to make sure claim labels were explicit throughout `## Research Skill Output`, and the local backlog-file deletion briefly blocked `git pull --rebase`.
3. **What single change would prevent this next time?** Add a lightweight pre-draft lint step that checks for unlabeled factual claims inside `## Research Skill Output` before the first draft commit.
4. **Is this a pattern?** Yes. This matches the repository's known pattern that acronym and citation/label discipline are the most common review failure points; this run hit the same class of formatting-risk issue even though it was fixed before the external review failed.
