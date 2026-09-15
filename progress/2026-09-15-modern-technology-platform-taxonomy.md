# 2026-09-15 -- Complete research item (modern-technology-platform-taxonomy)

**Completed:**
- `Research/completed/2026-09-14-modern-technology-platform-taxonomy.md` -- answers "what
  fundamentally distinguishes a 'platform' from a tool, product, or infrastructure, across
  software, data, infrastructure, and Internal Developer Platform (IDP) domains?" with a
  four-condition test synthesised from three independent literatures: modular
  information-hiding interfaces (Baldwin and Clark), self-service consumption and product
  governance (Cloud Native Computing Foundation (CNCF), Fowler/Bottcher), and multi-party
  value creation (Rochet and Tirole's two-sided-market economics). Adds organisational
  implications via Conway's Law, the golden-path pattern, and DevOps Research and Assessment
  (DORA) 2024 survey evidence on the conditional nature of platform-adoption productivity
  gains.
- `learnings.md` Thread 12 updated with a new corollary and evidence entry: the
  four-condition test is a boundary-defining layer that sits beneath the taxonomy,
  traceability, and maturity layers the thread already documents.

**Sources consulted:** Baldwin & Clark *Design Rules* (MIT Press), Rochet & Tirole
"Platform Competition in Two-Sided Markets" (Toulouse repository), Gawer & Cusumano
(MIT DSpace open-access manuscript), Eisenmann/Parker/Van Alstyne HBR article, Martin
Fowler / Bottcher "What I Talk About When I Talk About Platforms", CNCF TAG App Delivery
Platforms White Paper, Conway's Law original text, DORA 2024 State of DevOps report,
Team Topologies cognitive-load framing, Microsoft Learn platform-engineering capability
model, ISO/IEC/IEEE 42010, plus three related completed items (InnerSource-hybrid,
Software Factory, Data Product Ontology).

**Review cycle:** Two automated review passes ran, both flagged as `FAIL`, both counted
toward the `review_count` cap of 2 -- the item proceeded to completion once the cap was
reached, per the workflow's design (no issue is raised at the cap; the review log content
is still authoritative and was used to keep fixing quality issues even after the cap was
hit). Pass 1's *first* attempted commit was rejected by a concurrent `docs: rebuild site`
push (known race-condition pattern) and never landed on `main`, so the real pass 1 was the
second trigger. Violations fixed across the two landed passes: unexpanded "IDE" acronym;
"DORA" and "ISO/IEC/IEEE" expanded out of first-use order; three Key Findings/Evidence Map
rows labelled "high confidence" on a single source each (downgraded to "medium", including
two Evidence Map rows not originally caught by the automated report but found during
self-review); two `§5 Depth and Breadth Expansion` sentences labelled `[fact]` for
interpretive analogical claims (relabelled `[inference]`, with the fact/inference split
made explicit within each sentence pair); an Executive Summary/`§6 Synthesis` sentence
labelled `[fact]` while its Findings mirror was correctly `[inference]` for the same
claim (fixed by splitting the sentence into a `[fact]` premise and an `[inference]`
conclusion, applied to both mirrors); a Key Finding collapsing a `[fact]` clause and an
`[inference]` mapping clause under one label (split into two labelled clauses); and three
consecutive Key Findings sharing an identical "[X] is distinguished from a platform by the
absence of..." opening (varied to break the structural-repetition pattern).

## Mini-Retro

1. **Did the process work?** Yes. The mandated self-review checklist (acronym ordering,
   URL-to-Sources completeness, em-dash scan, cross-reference engagement) caught several
   issues before the first automated review ran, and the two-pass review/fix loop caught
   the remainder. The item reached a defensible "medium confidence" overall rating with
   every Key Finding individually labelled and sourced.

2. **What slowed down or went wrong?** The first review-workflow commit was silently lost
   to a push race with the concurrent `docs: rebuild site` workflow -- the run showed a
   `FAIL` verdict in its logs but the `review_count` frontmatter increment never reached
   `main`, so re-triggering was required to get a countable pass. This is an already-known
   pattern (see the copilot-instructions.md "research-review.yml's own commit-and-push step
   races..." row), and it recurred exactly as documented: verifying `git log origin/main --
   <item path>` after each triggered review, not just the run's pass/fail status, was
   necessary to know whether the pass actually counted.

3. **What single change would prevent this next time?** None beyond what's already
   documented -- the existing guidance (check `origin/main` history for the review commit,
   not just the run's log) was sufficient once applied. No new class of failure was
   discovered this session; the epistemic-label-boundary issues (fact-vs-inference on
   interpretive analogies, and one Executive-Summary/Findings label mismatch) are instances
   of already-documented patterns rather than a new one, and the Key-Findings structural-
   repetition instance is the same rule already documented for Assumptions blocks, now
   confirmed to also apply to Key Findings lists.

4. **Is this a pattern?** The push-race pattern is already tracked. The
   fact/inference-on-interpretive-analogy pattern is a specific instance of the general
   "Epistemic Label Boundary" rule in the research skill and doesn't yet warrant its own
   table row, but if it recurs on a future item it should be added explicitly (the specific
   trigger is: a sentence draws an analogy or maps one framework's structure onto another
   domain, and that mapping itself -- not just the source claims it draws on -- needs its
   own `[inference]` label).
