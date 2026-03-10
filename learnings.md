# Learnings

A living synthesis document. Each section captures a cross-cutting insight that spans multiple research items. These are not conclusions — they are the emergent themes that appear when completed research is read together. Updated whenever a new research item adds signal to an existing thread.

---

## How to use this document

Each entry has:
- **The learning**: a specific, synthesised claim — not a vague observation
- **Evidence**: which completed research items support it (with links)
- **Open thread**: what still needs investigation

Entries here should be *denser* than any individual research item because they synthesise across items. If a thread becomes substantial enough, it warrants its own backlog item.

---

## Thread 1 — Intent alignment is the Knowledge→Wisdom gap

**The learning:** The intent alignment problem in AI systems is structurally identical to the Knowledge→Wisdom transformation in the DIKW pyramid. A system can have deep domain knowledge and still fail to act wisely if its fitness function is miscalibrated. Formal specification methods (contracts, types, TLA+) address the Knowledge layer. Wisdom requires goal alignment — which is not a formal property but a relational one between the system's purpose and the stakeholder's genuine intent.

**Evidence:**
- `Research/completed/2026-03-10-formal-spec-intent-alignment-agentic-coding.md` — formal spec hierarchy shows that even full formal verification does not eliminate intent mismatch; the gap is between specification correctness and goal correctness
- `Research/backlog/2026-03-10-dikw-transformation-functions.md` — the K→W transformation is the least formalised in DIKW; this explains why intent alignment is structurally harder than correctness
- Goodhart's Law (documented in intent alignment item): optimising a measurable proxy for a goal is equivalent to stopping at Knowledge and calling it Wisdom

**Open thread:** Is there a formal account of the K→W transformation that could be applied to agent alignment? Dependent types and refinement types address specification precision (K layer); what would a type system for *purpose alignment* look like?

---

## Thread 2 — Transaction costs are the organisational equivalent of coordination overhead

**The learning:** Coase's transaction cost argument explains organisational form the same way that intent specification explains agent behaviour overhead: when the cost of defining, verifying, and enforcing a contract exceeds the cost of internalising the function, you bring it inside the boundary. For software organisations, this is the foundational logic behind platform teams, internal APIs, and team interaction modes. Culture (North's informal institutions) reduces coordination costs without contracts — exactly as shared intent reduces prompt engineering overhead in agent systems.

**Evidence:**
- `Research/backlog/2026-03-10-nature-of-the-firm-coase-organisations.md` — Coase (1937), Williamson (1981), North (1990) synthesis
- `Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md` — agent harness architectures mirror team coordination patterns; tool access, memory, and context management are internal coordination mechanisms
- Team Topologies interaction modes (referenced in Coase item) — three interaction modes map to Coase's three governance modes

**Open thread:** What is the transaction cost of *changing* an organisational boundary? Coase describes equilibrium; the dynamic version (when and how to restructure) is less well-developed. Building Evolutionary Architectures' fitness function concept may provide the mechanism.

---

## Thread 3 — The DIKW pyramid describes organisational learning velocity

**The learning:** An organisation's competitive advantage is not its data or its information — it is the speed at which it moves *up* the DIKW stack. Data-rich, insight-poor organisations are stuck at the D→I transition. Knowledge-rich, wisdom-poor organisations make technically correct but strategically wrong decisions. The transformation functions at each level are the bottlenecks. Understanding which transformation is rate-limiting in any given organisation is a more precise diagnostic than generic "data maturity" frameworks.

**Evidence:**
- `Research/backlog/2026-03-10-dikw-transformation-functions.md` — the research question directly addresses this
- `Research/completed/2026-03-03-knowledge-representation-agent-context.md` — representation structures affect the quality of the I→K transformation (GraphRAG, RAPTOR, hierarchical summarisation)
- `Research/completed/2026-03-03-knowledge-retention-active-recall.md` — knowledge decays; without active recall mechanisms, the K layer degrades back toward I
- `Research/completed/2026-02-27-information-synthesis-entropy.md` — information-theoretic framing: synthesis is entropy reduction; the D→I transformation is lossy by design

**Open thread:** Can the DIKW transformation functions be instrumented in an AI-assisted research system? E.g., is each fetch→synthesise→link cycle a measurable D→I→K step? What would a K→W step look like in this corpus?

---

## Thread 4 — Formal specification and informal institutions are complementary, not competing

**The learning:** Formal methods (contracts, types, verification) address the *specification layer* — ensuring that what is built matches what is specified. Informal institutions (culture, norms, shared purpose) address the *intent layer* — ensuring that what is specified matches what is genuinely wanted. North's argument that informal institutions are the primary transaction cost reducers is the macroeconomic parallel to the finding in `2026-03-10-formal-spec-intent-alignment-agentic-coding.md` that no formal method eliminates intent mismatch. Both point to the same conclusion: the formal layer is necessary but not sufficient; the informal layer is primary.

**Evidence:**
- `Research/completed/2026-03-10-formal-spec-intent-alignment-agentic-coding.md` — formal specification hierarchy; the specification layer does not address goal correctness
- `Research/backlog/2026-03-10-nature-of-the-firm-coase-organisations.md` — North (1990) on informal institutions as primary cost reducers; culture > contracts
- `Research/completed/2026-03-08-context-engineering-first-principles.md` — context engineering for AI agents: system prompts and conventions are informal institutions for agent behaviour

**Open thread:** What is the minimal viable formal layer for a given domain? The intent alignment item shows that full formal verification is impractical at scale. What is the right *combination* of formal + informal for a software team? For an agentic system?

---

## Thread 5 — Agent memory architecture mirrors organisational knowledge management

**The learning:** The episodic/semantic/procedural memory taxonomy for AI agents directly parallels the knowledge management challenge in human organisations. Episodic memory (what happened in this conversation/project) decays without recall mechanisms. Semantic memory (general world knowledge) requires structured representation to be retrievable. Procedural memory (how to do things) must be validated and kept current. The same failure modes appear at both scales: context loss, knowledge silos, outdated procedures. The solutions also converge: active recall, structured representation, regular synthesis.

**Evidence:**
- `Research/completed/2026-03-02-agent-memory-management-context-injection.md` — memory taxonomy and failure modes for AI agents
- `Research/completed/2026-03-03-knowledge-retention-active-recall.md` — active recall mechanisms to prevent K layer decay
- `Research/completed/2026-03-03-knowledge-representation-agent-context.md` — structured representation for I→K
- `Research/completed/2026-03-03-knowledge-linking-connected-corpus.md` — backlinks and cross-references as the connective tissue of a knowledge corpus

**Open thread:** Is there a unified memory architecture that works for both agents and human knowledge management? The distinction between "agent memory" (milliseconds–weeks) and "organisational memory" (months–decades) is one of timescale and fidelity, not structure.

---

*Last updated: 2026-03-10*
