# 2026-05-12 -- Add backlog item (graph-db-saas-knowledge-ontology)

**Completed:**
- `Research/backlog/2026-05-12-graph-db-saas-knowledge-ontology.md` — added from issue "Research into graph dbs for knowledge ontology"; asks which hosted Software-as-a-Service (SaaS) graph database platforms are suitable for building and querying a knowledge ontology, and how they compare on data model, query language, pricing, and integration.

## Mini-Retro

1. **Did the process work?** Yes. The issue provided a clear topic (graph databases for knowledge ontology) and a clear deployment constraint (hosted SaaS). The five-test quality check passed after expanding the vague "research into graph dbs" into a precise, decomposable question.
2. **What slowed down or went wrong?** The skills submodule was not initialised, so the `research-question` SKILL.md could not be read directly. The manual fallback process from the instructions was applied instead.
3. **What single change would prevent this next time?** Running `git submodule update --init` at session start would make the skill available. This is already documented in the instructions — no new rule needed.
4. **Is this a pattern?** Yes — the submodule not being initialised is a recurring situation in cloud agent sessions. The fallback is clear and documented.
