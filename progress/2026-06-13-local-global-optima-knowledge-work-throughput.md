# 2026-06-13 -- local-global-optima-knowledge-work-throughput

**Completed:**
- `Research/completed/2026-06-13-local-global-optima-knowledge-work-throughput.md` — primary research item completed; establishes that local tooling optimisation in knowledge-work pipelines degrades whole-system throughput when shared constraint capacity is not raised commensurately; Faros AI telemetry (22,000 developers, 2026) and DORA 2025 confirm the TOC-predicted queue-overflow pattern in AI-assisted software delivery; three amplifying interdependency surfaces identified (approval/review queues, tight coupling, change-management gates); three corrective levers established (platform engineering, WIP limits/small batches, architectural decoupling).
- `learnings.md` — Thread 18 updated with new evidence item and an additional open-question about non-linearity in the local-to-global loss relationship.

## Mini-Retro

1. **Did the process work?** The research process worked well: §§0–7 produced a well-structured, evidence-backed item. The review cycle took four passes (two natural passes + two auto-pass triggers) due to accumulated citation and labelling violations. The fixes were systematic once identified.

2. **What slowed down or went wrong?**
   - Wikipedia was co-cited as a claim source throughout; the review correctly rejected this on every pass. Wikipedia-in-claims is now explicitly in the Known Recurring Patterns table.
   - An edit accidentally deleted §6 KF3-6 by providing too-broad `old_str` to a replacement; had to restore them in a subsequent pass.
   - Multiple label transitions from `[fact]` to `[inference]` were required across passes because Forte Labs (secondary practitioner) and Wikipedia (tertiary) were repeatedly used as claim sources without an independent primary source.
   - KF2 causal language ("caused by") inside a `[fact]` label was flagged correctly by `speculation-control`; the Faros telemetry is correlational, not experimental.

3. **What single change would prevent this next time?** Before writing any TOC or practitioner-synthesis claims as `[fact]`, verify the citation qualifies as a primary or peer-reviewed secondary source. Forte Labs and Wikipedia never qualify; change to `[inference]` on first write and avoid the multi-pass correction cycle.

4. **Is this a pattern?** Yes — this matches the Known Recurring Patterns table entries for:
   - Wikipedia as sole source for `[fact]` claims
   - Secondary practitioner sources (Forte Labs, Team Topologies) used for `[fact]` labels
   - KF2 causal-in-fact pattern: correlational data labelled `[fact]` with embedded causal claim

5. **Does any documentation need updating?** The Known Recurring Patterns table in `.github/copilot-instructions.md` already covers the Wikipedia-as-sole-source pattern. The correlational-data-with-causal-claim pattern should be checked for coverage.

6. **Do the default instructions need updating?** Adding a pre-draft rule: "Before labelling any claim `[fact]`, verify the cited source is a primary data source or peer-reviewed secondary. Forte Labs, Team Topologies, and Wikipedia do not qualify for `[fact]` labels."
