# 2026-07-20 — Add backlog items from issue #634 (multiple research questions — ontologies and knowledge extraction in agentic memory)

**Completed:**
- `Research/backlog/2026-07-20-hybrid-memory-integration-ontology-llm-weights.md` — added from issue #634; asks how AI agents can synchronize structured ontologies and knowledge graphs with latent LLM weight knowledge, and what architectural patterns bridge this "hybrid memory" gap
- `Research/backlog/2026-07-20-episodic-semantic-consolidation-agents.md` — added from issue #634; asks what techniques enable agents to generalize from specific episodic experiences to durable semantic memory entries (closing the "consolidation gap")
- `Research/backlog/2026-07-20-autonomous-knowledge-curation-truth-maintenance.md` — added from issue #634; asks what autonomous mechanisms exist for deciding which extracted knowledge to retain, resolving contradictions (truth maintenance), and managing ontology noise — blocks on `2026-07-20-episodic-semantic-consolidation-agents`

## Research Question Skill — Five-Test Results

All three questions were checked against the Specific / Answerable / Scoped / Motivated / Decomposable criteria before creating backlog items:

**Hybrid memory integration:**
- Specific: the synchronization between symbolic KGs and LLM weights, not "memory" in general
- Answerable: active research area with 2022–2026 literature
- Scoped: excludes fine-tuning, in-weights editing, schema design, and AWS implementation
- Motivated: conflicting knowledge stores cause hallucination, stale facts, and traceability loss
- Decomposable: read-through, write-through, conflict detection, authoritative-source policy, evaluation

**Episodic-to-semantic consolidation:**
- Specific: the generalization step from logged experience to ontological fact
- Answerable: systems like MemoryBank and Generative Agents demonstrate current approaches
- Scoped: excludes in-weights fine-tuning and downstream curation (separate item)
- Motivated: without consolidation, episodic memory degrades to a growing searchable log with no agent learning
- Decomposable: extraction, clustering, threshold policy, continual learning, benchmarks

**Autonomous curation and truth maintenance:**
- Specific: retention decision, contradiction resolution, noise management in autonomous agents
- Answerable: classical Truth Maintenance System (TMS) literature plus modern neural-symbolic approaches
- Scoped: excludes human-supervised curation (covered by `2026-04-22`) and schema design
- Motivated: agents without curation accumulate ontology drift and conflicting beliefs over time
- Decomposable: retention policy, Justification-based TMS (JTMS)/Assumption-based TMS (ATMS) applicability, conflict detection, conflict resolution, noise filtering, provenance

## Dependency rationale

The curation item (`2026-07-20-autonomous-knowledge-curation-truth-maintenance`) blocks on the consolidation item (`2026-07-20-episodic-semantic-consolidation-agents`) because curation can only be designed once the extraction/generalization pipeline produces candidate knowledge. The hybrid memory item has no blocking dependency — it focuses on the structural integration layer and can be investigated in parallel.

## Mini-Retro

1. **Did the process work?** Yes. The issue provided a detailed three-section analysis of the problem space, making it straightforward to map each section to a distinct, scoped research question. All three questions passed the five-test quality check without requiring major revision.
2. **What slowed down or went wrong?** The `.github/skills/` submodule was not initialised in the agent environment, so the research-question skill was applied from the documented process rather than reading `SKILL.md` directly. This is the expected fallback.
3. **What single change would prevent this next time?** Nothing structural — the fallback is documented and works. Initialising the submodule before agent runs would save the lookup overhead, but the research loop already handles this.
4. **Is this a pattern?** Yes — the submodule absence in the coding agent environment is a known recurring pattern. Already documented.
5. **Does any documentation need updating?** No — the three backlog items follow the established template and convention; no process changes required.
6. **Do the default instructions need updating?** No new convention emerged from this session.
