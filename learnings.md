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
- `Research/completed/2026-03-10-dikw-transformation-functions.md` — the K→W transformation is the least formalised in DIKW; this explains why intent alignment is structurally harder than correctness
- Goodhart's Law (documented in intent alignment item): optimising a measurable proxy for a goal is equivalent to stopping at Knowledge and calling it Wisdom

**Open thread:** Is there a formal account of the K→W transformation that could be applied to agent alignment? Dependent types and refinement types address specification precision (K layer); what would a type system for *purpose alignment* look like?

---

## Thread 2 — Transaction costs are the organisational equivalent of coordination overhead

**The learning:** Coase's transaction cost argument explains organisational form the same way that intent specification explains agent behaviour overhead: when the cost of defining, verifying, and enforcing a contract exceeds the cost of internalising the function, you bring it inside the boundary. For software organisations, this is the foundational logic behind platform teams, internal APIs, and team interaction modes. Culture (North's informal institutions) reduces coordination costs without contracts — exactly as shared intent reduces prompt engineering overhead in agent systems. Team Topologies' three interaction modes (collaboration, X-as-a-Service, facilitation) map directly onto Williamson's governance structures (hybrid, market, quasi-hierarchical), providing a practical translation from economic theory to software team design. Four organisational invariants are necessary conditions for any stable organisation: (i) clear residual claimancy, (ii) authority commensurate with accountability, (iii) information flows matching decision rights, and (iv) shared purpose as informal institution. Violation of any one produces a characteristic and predictable failure mode.

**Evidence:**
- `Research/completed/2026-03-10-nature-of-the-firm-coase-organisations.md` — Coase (1937), Williamson (1981), North (1990) synthesis; Team Topologies as TCE-in-software; four organisational invariants; fitness functions for firms; BU decision framework
- `Research/completed/2026-03-02-transaction-costs.md` — foundational TCE mechanics (Coase, Williamson, North, Ostrom); speculative SWE/AI extensions
- `Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md` — agent harness architectures mirror team coordination patterns; tool access, memory, and context management are internal coordination mechanisms
- Team Topologies interaction modes — three interaction modes map directly to Coase's three governance modes (confirmed by Amazon two-pizza teams and Spotify squads-tribes evidence)

**Open thread:** The dynamic version of Coase's boundary model (when and how to restructure as the cost landscape changes) is under-specified. The "institutional adaptability" fitness function is named but no decision-trigger framework exists. Measuring transaction costs in software development contexts (cost per PR review cycle, specification uncertainty costs) remains an open empirical gap.

---

## Thread 3 — The DIKW pyramid describes organisational learning velocity

**The learning:** An organisation's competitive advantage is not its data or its information — it is the speed at which it moves *up* the DIKW stack. Data-rich, insight-poor organisations are stuck at the D→I transition. Knowledge-rich, wisdom-poor organisations make technically correct but strategically wrong decisions. The transformation functions at each level are the bottlenecks. Understanding which transformation is rate-limiting in any given organisation is a more precise diagnostic than generic "data maturity" frameworks.

**Evidence:**
- `Research/completed/2026-03-10-dikw-transformation-functions.md` — the research question directly addresses this
- `Research/completed/2026-03-03-knowledge-representation-agent-context.md` — representation structures affect the quality of the I→K transformation (GraphRAG, RAPTOR, hierarchical summarisation)
- `Research/completed/2026-03-03-knowledge-retention-active-recall.md` — knowledge decays; without active recall mechanisms, the K layer degrades back toward I
- `Research/completed/2026-02-27-information-synthesis-entropy.md` — information-theoretic framing: synthesis is entropy reduction; the D→I transformation is lossy by design

**Open thread:** Can the DIKW transformation functions be instrumented in an AI-assisted research system? E.g., is each fetch→synthesise→link cycle a measurable D→I→K step? What would a K→W step look like in this corpus?

---

## Thread 4 — Formal specification and informal institutions are complementary, not competing

**The learning:** Formal methods (contracts, types, verification) address the *specification layer* — ensuring that what is built matches what is specified. Informal institutions (culture, norms, shared purpose) address the *intent layer* — ensuring that what is specified matches what is genuinely wanted. North's argument that informal institutions are the primary transaction cost reducers is the macroeconomic parallel to the finding in `2026-03-10-formal-spec-intent-alignment-agentic-coding.md` that no formal method eliminates intent mismatch. Both point to the same conclusion: the formal layer is necessary but not sufficient; the informal layer is primary. Engineering conventions and standards (AGENTS.md, CLAUDE.md, coding standards, architectural decision records) are informal institutions in North's precise sense: they reduce per-interaction coordination cost without requiring explicit negotiation, and are a more reliable predictor of team coordination efficiency than formal documentation mandates alone.

**Evidence:**
- `Research/completed/2026-03-10-formal-spec-intent-alignment-agentic-coding.md` — formal specification hierarchy; the specification layer does not address goal correctness
- `Research/completed/2026-03-10-nature-of-the-firm-coase-organisations.md` — North (1990) on informal institutions as primary cost reducers; engineering culture as informal institution; institutional coherence as a fitness function
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

## Thread 6 — Adversarial collaboration: agents with a shared goal but different competencies and time horizons

**The learning:** A system of agents — human or AI — that share a goal but deliberately occupy different competency domains and time horizons produces better outcomes than a single generalist. Each agent type covers a different DIKW transformation and a different time horizon. The adversarial element is not opposition but deliberate perspective diversity: each agent challenges the others' blind spots rather than agreeing toward local optima. The 15 agent types below are a working taxonomy — each occupies a distinct position in the competency × time-horizon space, and each corresponds to a different layer of the DIKW pyramid.

| Agent | Primary concern | Time horizon | DIKW layer |
|---|---|---|---|
| Designer | User experience, systemic coherence | Sprint → quarter | Information → Knowledge |
| SRE | Reliability, availability, observability | Operational (hours–weeks) | Data → Information |
| Tester | Correctness, edge cases, coverage | Sprint | Data → Information |
| Security | Threat surface, vulnerabilities, compliance | Immediate + long (architectural) | Knowledge |
| Performance — speed/resource | Latency, throughput, resource cost | Sprint → quarter | Data → Information |
| Performance — ROI | Return on investment, cost/benefit | Quarterly → annual | Information → Knowledge |
| Performance — goal achievement | OKR delivery, outcomes vs. outputs | Quarterly → annual | Knowledge → Wisdom |
| Strategic alignment | Are we building the right thing? | Multi-year | Wisdom |
| Insight capture | What have we learned? Retain the signal. | Continuous / retrospective | Knowledge |
| Researcher | What don't we know? Unknown unknowns. | Long / pre-competitive | Knowledge → Wisdom |
| Architecture | Technical structure, coupling, evolution | Medium → long | Knowledge |
| Architecture alignment | Is the tech consistent with strategic direction? | Long | Knowledge → Wisdom |
| Values alignment | Is this consistent with our principles? | Permanent | Wisdom |
| Change impact assessment | What breaks? What changes for users and systems? | Immediate | Data → Information |
| Risk assessment | What could go wrong? Probability and severity? | Variable (sprint → long) | Knowledge |

Values alignment and strategic alignment agents are the explicit K→W gatekeepers — their role is to ensure that what the collective *knows how to build* is aligned with what it *genuinely should build*. Their absence is not a neutral omission; it is a structural guarantee that wisdom-layer decisions will be made by whoever happens to be loudest or fastest.

**Evidence:**
- `Research/completed/2026-03-10-adversarial-agents-shared-goals-multi-perspective.md` — the full research item for this pattern, including the agent taxonomy, time-horizon mapping, and DIKW layer mapping
- `Research/completed/2026-03-08-bbc-five-case-model.md` — the BBC Five Case Model as a formalised adversarial-perspectives framework (five mandated lenses: strategic, economic, commercial, financial, management)
- `Research/completed/2026-03-10-nature-of-the-firm-coase-organisations.md` — Williamson's asset specificity explains why each agent type is internalised; North's informal institutions explain how their interaction protocol reduces coordination costs
- `Research/completed/2026-03-10-formal-spec-intent-alignment-agentic-coding.md` — formal specification covers the K layer; adversarial agents supply the informal W layer that formal methods cannot

**Open thread:** What is the minimal viable interaction protocol for a set of adversarial agents? The BBC Five Case Model mandates five cases but does not specify a resolution mechanism. How do you prevent the values alignment agent from becoming a permanent veto? What is the right quorum rule, and who holds the casting decision?

---

*Last updated: 2026-03-13*
