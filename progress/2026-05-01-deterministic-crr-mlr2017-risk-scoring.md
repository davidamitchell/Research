# 2026-05-01 -- Research Loop (deterministic-crr-mlr2017-risk-scoring)

**Completed:**

Research item:
- `Research/completed/2026-04-30-deterministic-crr-mlr2017-risk-scoring.md` -- completed; deterministic weighted customer risk rating models are legally compatible with the United Kingdom's Money Laundering Regulations 2017 because they are auditable, proportionate, and easy to justify to supervisors, but public evidence does not show that static onboarding bands alone predict suspicious outcomes well. The item concludes that hybrid models are the best-supported next step because they preserve deterministic governance controls while adding behavioral and ongoing-monitoring signals that static weights miss.

Sources consulted:
- https://www.legislation.gov.uk/uksi/2017/692/regulation/18 (United Kingdom statutory risk-assessment requirement)
- https://www.legislation.gov.uk/uksi/2017/692/regulation/28 (United Kingdom statutory customer-due-diligence and monitoring requirement)
- https://www.bis.org/bcbs/publ/d353.pdf (Basel Committee guidance on customer risk profiles and ongoing monitoring)

## Mini-Retro

1. **Did the process work?** Yes; the research-loop flow worked as intended, and one review/fix cycle was enough to get the item through.
2. **What slowed down or went wrong?** Two seeded sources were inaccessible from this runtime, and the first review caught one unlabeled access note plus one over-strong confidence assignment.
3. **What single change would prevent this next time?** Nothing beyond applying the existing self-review checklist earlier and more literally before the first draft commit.
4. **Is this a pattern?** Yes; it matches the existing recurring pattern around citation-discipline and confidence-evidence alignment, rather than introducing a new class of failure.
