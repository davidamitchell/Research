# 2026-07-20 -- Add backlog item (aws-agentcore-knowledge-context-layer)

**Completed:**
- `Research/backlog/2026-07-20-aws-agentcore-knowledge-context-layer.md` — added from issue #630; asks what AWS AgentCore capabilities and AWS-native services are required to design and operate a Knowledge Context Layer (KCL) that continuously acquires, curates, evolves, and serves enterprise knowledge to AI agents through ontologies, knowledge graphs, GraphRAG, and governed interfaces.

**PR feedback addressed (2026-07-20):**
- Created `Research/backlog/2026-07-20-tbox-abox-graphrag.md` — prerequisite item covering Terminological Box (TBox) / Assertional Box (ABox) design patterns for GraphRAG, with `blocks: [2026-07-20-aws-agentcore-knowledge-context-layer]` so the research loop cannot start the AWS KCL item until TBox/ABox design questions are resolved.
- Updated `aws-agentcore-knowledge-context-layer`: added `2026-07-20-tbox-abox-graphrag` to `cites` (explicit dependency) and added `backlog-item` to `output` so the completed research can propose update RQs for related completed items.

## Mini-Retro

1. **Did the process work?** Yes. The issue stated a clear research intent and the research-question skill's five-test check (Specific, Answerable, Scoped, Motivated, Decomposable) passed without revision. The existing completed items on AWS Bedrock (`2026-05-17-aws-bedrock-capabilities`), AgentCore (`2026-05-17-aws-bedrock-agentcore-suite-capabilities`), and KG-RAG migration (`2026-07-05-vector-rag-to-ontology-kg-rag-migration`) provided enough context to set accurate `cites:` and `related:` frontmatter fields and to define what is genuinely in scope versus already covered. PR feedback correctly identified a missing ontology-layer prerequisite (TBox/ABox design) that should be resolved before the AWS-specific implementation design starts.
2. **What slowed down or went wrong?** Initial item had `blocks: []` because the issue's stated "dependencies on other backlog rq" referred to already-completed items. The TBox/ABox prerequisite was not stated in the issue but was identified during review as a necessary schema-design step before the implementation item can be usefully executed.
3. **What single change would prevent this next time?** When an issue references an AWS implementation item that involves ontology design, proactively check whether the schema-layer design (TBox/ABox partitioning) is already covered by a completed item or needs a prerequisite backlog item. In this case it was not, and the gap was caught in review.
4. **Is this a pattern?** Partial — this is similar to the known pattern of missing prerequisite items when a research question builds on concepts not yet fully resolved, but specific to ontology-layer design as a precursor to implementation-layer design.
