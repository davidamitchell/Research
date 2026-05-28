# 2026-05-28 — Semantic Domain Emergence in Enterprise Ontology

**Item completed:** `Research/completed/2026-05-27-semantic-domain-emergence-enterprise-ontology.md`

## What was done

- Read item in full; confirmed research question, scope, approach, and 8 seed sources.
- Scanned `Research/completed/` for prior work; identified 5 relevant completed items: `free-energy-entropy-and-life`, `predictive-processing-active-inference`, `which-network-structures-bottleneck-or-accelerate-knowledge-flow`, `data-product-ontology`, `ontology-world-model-llm-prediction-forcing-functions`.
- Conducted §0–§7 structured research across four branches: (A) graph theory and network modularity, (B) cognitive stabilisation analogues, (C) organisational semantic stabilisation, (D) enterprise governance mechanisms.
- Key findings: semantic domains emerge via modularity maximisation (Louvain algorithm); PDP attractor dynamics and free energy minimisation provide theoretical grounding; four enterprise failure modes (scope creep, fragmentation, terminological pollution, ownership diffusion); four governance countermeasures (SKOS/OWL equivalence mapping, boundary objects, cross-domain approval gates, drift audits).
- Seeded full Findings from §6 Synthesis.
- Applied companion skill checks (citation-discipline, speculation-control, remove-ai-slop, peer-reviewer).
- Committed draft; triggered `research-review.yml` (pass 1).
- **Pass 1 FAIL:** Four violation classes: Louvain `[fact]`+sole Wikipedia, OWL/SKOS unexpanded, Hutchins 1995 wrong URL, full-sentence bold on all 10 KFs, KF#3 confidence medium vs low, unlabeled evaluative claims in §5 and §6 Analysis.
- Applied fixes: downgraded Louvain → `[inference]` + Blondel 2008 source, expanded OWL/SKOS, fixed Hutchins URL, stripped bold from all 10 KFs, KF#3 medium→low, labeled §5 and §6 Analysis evaluative claims with `[inference; source: URL]`.
- Committed fixes; triggered `research-review.yml` (pass 2).
- **Pass 2 PASS.**
- Pulled rebase; ran `python -m src.main research complete` — item moved to `Research/completed/`.
- Updated `learnings.md` Thread 22 with new item evidence and extended open thread.

## Mini-Retro

1. **Did the process work?** Yes — §0–§7 research loop, draft commit, review, fix, re-review, and complete all proceeded in correct sequence. The automated review correctly caught real violations; the fix cycle was targeted and did not require a third pass.

2. **What slowed down or went wrong?** The most time-intensive part was the pass-1 review fix cycle. The full-sentence bold anti-pattern affected all 10 Key Findings — a wholesale structural issue, not an isolated slip. The Louvain claim was borderline (graph-partition algorithms are described by many secondary sources, but the Blondel 2008 paper is the primary source; should have cited it directly in §2.A). The Hutchins 1995 URL was incorrectly matched to a Rumelhart & McClelland citation — a copy-paste error from source lookup.

3. **What single change would prevent this next time?** Run `grep -c "^\d+\. \*\*"` on the KFs before triggering the first review pass. The full-sentence bold is already in the Known Recurring Patterns table and is a zero-effort automated check. Not running it cost a full review cycle.

4. **Is this a pattern?** Yes — full-sentence bold in Key Findings has appeared in multiple items. It is in the Known Recurring Patterns table. The pre-commit self-review checklist already covers it. The gap is that the check was not run before the first draft commit in this session.

5. **Does any documentation need updating?** No new conventions emerged. The Known Recurring Patterns table already captures all four violation classes that failed. `learnings.md` Thread 22 updated with new item.

6. **Do the default instructions need updating?** No new conventions. The pre-commit self-review in the instructions explicitly lists full-sentence bold as a check. Adherence was the gap, not coverage.
