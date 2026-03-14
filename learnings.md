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

**The learning:** The intent alignment problem in AI systems is structurally identical to the Knowledge→Wisdom transformation in the DIKW pyramid. A system can have deep domain knowledge and still fail to act wisely if its fitness function is miscalibrated. Formal specification methods (contracts, types, TLA+) address the Knowledge layer. Wisdom requires goal alignment — which is not a formal property but a relational one between the system's purpose and the stakeholder's genuine intent. Sycophancy is the canonical example of this split: it is a Layer 1 generation failure (H-Neuron over-compliance at the token level) that invariably produces a Layer 2 goal failure (the user's actual objective is not achieved). High token-level compliance can co-exist with systematic goal-level failure — the two mechanisms are separable and are confirmed by distinct latent-space encodings (Vennemeyer et al., ICLR 2026). Goal drift in multi-step agents operates through the same gap: contextual pressure from prior outputs causes the agent to pattern-match toward recent context rather than the original system intent, even without adversarial injection.

**Evidence:**
- `Research/completed/2026-03-10-formal-spec-intent-alignment-agentic-coding.md` — formal spec hierarchy shows that even full formal verification does not eliminate intent mismatch; the gap is between specification correctness and goal correctness
- `Research/completed/2026-03-10-dikw-transformation-functions.md` — the K→W transformation is the least formalised in DIKW; this explains why intent alignment is structurally harder than correctness
- Goodhart's Law (documented in intent alignment item): optimising a measurable proxy for a goal is equivalent to stopping at Knowledge and calling it Wisdom
- `Research/completed/2026-03-12-failure-mode-taxonomy-expansion.md` — sycophancy resolution (Layer 1 mechanism + Layer 2 consequence); goal drift empirical confirmation in multi-step agents (arXiv:2603.03258); SycEval 56–62% rates; Vennemeyer et al. ICLR 2026 latent-space evidence

**Open thread:** Is there a formal account of the K→W transformation that could be applied to agent alignment? Dependent types and refinement types address specification precision (K layer); what would a type system for *purpose alignment* look like? Can a lightweight runtime intent-verification module detect goal drift between the original system intent and the current agent trajectory?

---

## Thread 2 — Transaction costs are the organisational equivalent of coordination overhead

**The learning:** Coase's transaction cost argument explains organisational form the same way that intent specification explains agent behaviour overhead: when the cost of defining, verifying, and enforcing a contract exceeds the cost of internalising the function, you bring it inside the boundary. For software organisations, this is the foundational logic behind platform teams, internal APIs, and team interaction modes. Culture (North's informal institutions) reduces coordination costs without contracts — exactly as shared intent reduces prompt engineering overhead in agent systems. Team Topologies' three interaction modes (collaboration, X-as-a-Service, facilitation) map directly onto Williamson's governance structures (hybrid, market, quasi-hierarchical), providing a practical translation from economic theory to software team design. Four organisational invariants are necessary conditions for any stable organisation: (i) clear residual claimancy, (ii) authority commensurate with accountability, (iii) information flows matching decision rights, and (iv) shared purpose as informal institution. Violation of any one produces a characteristic and predictable failure mode.

**Evidence:**
- `Research/completed/2026-03-10-nature-of-the-firm-coase-organisations.md` — Coase (1937), Williamson (1981), North (1990) synthesis; Team Topologies as TCE-in-software; four organisational invariants; fitness functions for firms; BU decision framework
- `Research/completed/2026-03-02-transaction-costs.md` — foundational TCE mechanics (Coase, Williamson, North, Ostrom); speculative SWE/AI extensions
- `Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md` — agent harness architectures mirror team coordination patterns; tool access, memory, and context management are internal coordination mechanisms
- Team Topologies interaction modes — three interaction modes map directly to Coase's three governance modes (confirmed by Amazon two-pizza teams and Spotify squads-tribes evidence)

**Open thread:** Measuring transaction costs in software development contexts (cost per pull request (PR) review cycle, specification uncertainty costs) remains an open empirical gap. See Thread 8 for empirical evidence on the new organisational equilibrium when AI dramatically reduces coordination costs.

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

One specific new failure mode with no prior equivalent: when an AI agent performs the exploratory work, the human supervisor holds only the *outcome* — not the process knowledge (what was tried, why choices were made, what was discarded). The agent's process knowledge is transient — it lives in the context window and disappears when the session ends. This makes human-to-human knowledge transfer logically impossible, not merely difficult. The correct response is architectural: require agents to produce structured, persisted decision logs as a standard output, enabling downstream agent synthesis. This is not a harder version of the tacit knowledge problem; it is a structurally different problem requiring a different class of solution.

**Evidence (extended):**
- `Research/completed/2026-03-12-exploration-synthesis-gap.md` — the agent-mediated knowledge gap; context window transience as the mechanism; structured decision logs as the required artefact; agent synthesis pipeline as the architectural intervention

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

## Thread 7 — Automated quality gates for agentic pipelines require observable, dimension-specific rubrics

**The learning:** Holistic LLM-as-judge scores are unreliable for evaluating long-form agentic research outputs. Effective automated quality gates decompose quality into dimension-specific, observable criteria — each scored on an explicit 1–5 scale with unambiguous level descriptions. The nine dimensions that matter for this repository's research loop (claim sourcing, acronym expansion, hedge control, finding completeness, finding quality, evidence map coverage, assumption labeling, cross-section consistency, AI slop absence) each correspond to a distinct failure mode that emerges from incomplete execution of the research protocol. Framing each dimension as a binary pass/fail gate at a defined threshold (e.g., ≥3/5) produces a reproducible CI signal. The credential constraint in restricted CI environments (no OpenAI/Anthropic keys) forces the tooling decision: the only feasible LLM-as-judge implementation uses the model already available via the existing infrastructure (GitHub Copilot CLI, COPILOT_GITHUB_TOKEN) — adopting a named evaluation framework (DeepEval, Pydantic Evals, agentevals) solely for its CI runner is not justified when those frameworks require credentials that are not approved. This generalises: **tooling selection for agentic eval gates must be driven first by credential and infrastructure constraints, then by framework features.**

**Evidence:**
- `Research/completed/2026-03-10-research-loop-evaluation-rubric.md` — 9-dimension rubric specification; tooling comparison against credential constraints; CI workflow design; gold dataset requirements
- `Research/completed/2026-03-10-agent-evaluation-cross-repo-analysis.md` — 5-component minimal viable evaluation framework; LLM-as-judge with structured rubrics preferred over open-ended prompts for long-form research
- `Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md` — agent harness architectures include quality gates as first-class concerns; evaluation as a continuous feedback mechanism

**Open thread:** What is the minimum viable gold calibration dataset size and diversity for the 9-dimension rubric to be well-calibrated? At what point do rubric dimensions become contradictory (e.g., hedge control vs. epistemic honesty requires acknowledging uncertainty)? How do the rubric scores trend over successive research loop iterations — is quality improving?

---

## Thread 8 — AI force multiplication shifts the organisational optimum toward small teams and ambition expansion

**The learning:** When AI multiplies per-person productive capacity by 5–10x, two shifts happen simultaneously. First, the correct strategic response is to expand the mission rather than cut headcount. Second, the correct structural unit shrinks: the n(n-1)/2 communication-channel formula (Brooks, 1975) is unchanged, but each channel now taxes individuals worth $2M/year rather than $250K/year — making the penalty for over-staffing above five people approximately 5–10x more expensive than before AI. The empirical evidence from AI-native companies is unambiguous: Lovable ($2.74M ARR per employee), Midjourney (~$4.7M), ElevenLabs ($569K–$825K), Anthropic ($3.6M–$7.5M), and OpenAI (~$5M) operate at 4–36x the private SaaS median of $130K — not by cutting costs but by attacking large markets with very small teams. The scout/strike team framework operationalises this: a solo "scout" validates viability; a 5-person "strike team" executes. Peter Steinberger's solo build of OpenClaw (196K GitHub stars, 2M weekly visitors in one week, November 2025) is an existence proof of the scout model. The Shopify April 2025 mandate — requiring teams to prove AI cannot perform a task before requesting headcount — operationalises the structural constraint at organisational scale. Incumbents face a structural bias toward cost reduction; the practical response requires CEO-level mandate and is most constrained in regulated industries.

**Evidence:**
- `Research/completed/2026-03-12-ai-team-size-strike-team-thesis.md` — mathematical coordination penalty argument (n(n-1)/2); economic cost rising with per-person output; scout/strike team archetypes; Steinberger/OpenClaw existence proof; convergent management research (Hackman, Bezos two-pizza rule, Supercell)
- `Research/completed/2026-03-12-ai-force-multiplier-ambition-expansion.md` — revenue-per-employee evidence for five AI-native companies; Shopify mandate analysis; "cannot do now" list framework; coordination-artifact vs judgment-role taxonomy; organisational inertia mechanisms
- `Research/completed/2026-03-10-nature-of-the-firm-coase-organisations.md` — Coase's transaction cost argument explains why smaller, AI-augmented units become viable as coordination costs fall; Thread 2 provides the theoretical underpinning

**Open thread:** Does AI tooling (AI-mediated async communication, agent-to-agent coordination) reduce the per-channel cost in the n(n-1)/2 formula, and if so by how much? Do incumbents that implement the Shopify-style mandate measurably outperform on revenue growth or margin? What is the empirical breakdown of roles in large organisations by coordination-artifact vs judgment-role type?

---

*Last updated: 2026-03-14 (Thread 1 extended: sycophancy resolution, goal drift; Thread 10 added)*

---

## Thread 9 — The exploration-synthesis gap is structural, not cultural: four independent mechanisms explain it

**The learning:** In any organisation running a fast-moving innovation programme (AI adoption, R&D, technology transformation), individuals systematically fail to synthesise colleagues' prior work. This is not a cultural or personality problem — it is produced by four independent, reinforcing structural mechanisms: (1) *neurological asymmetry*: exploration activates dopaminergic novelty-reward circuits; synthesis does not — making exploration intrinsically more rewarding than synthesis regardless of attitude; (2) *Self-Determination Theory (SDT) misalignment*: exploration satisfies all three basic psychological needs (autonomy, competence, novelty contribution); synthesis satisfies none under standard organisational conditions; (3) *incentive system failure*: high pay-for-individual-performance empirically reduces knowledge sharing (Jin et al. 2025); credit attribution accrues to originators, not synthesisers, because synthesis produces no named, attributable artefact; (4) *NIH syndrome*: active attitude-level resistance to external knowledge (Katz & Allen 1982), amplified by group tenure and competitive incentive environments. Because these mechanisms are independent and reinforcing, removing any one leaves the other three intact. Structural interventions (credit redesign, synthesis checkpoints) are more durable than cultural persuasion. For AI-agent-mediated work, human-to-human synthesis is logically impossible (see Thread 5), requiring architectural delegation to agent synthesis pipelines.

**Evidence:**
- `Research/completed/2026-03-12-exploration-synthesis-gap.md` — full mechanistic analysis across four disciplines; tiered intervention framework (structural / process / architectural); SDT + NIH + PFIP + credit attribution evidence; agent-mediated gap analysis

**Open thread:** Can credit attribution systems be redesigned to make synthesis visible and rewarded without triggering the "synthesis as audit burden" reaction that suppresses exploration velocity? Do collaborative-commons cultures (open-source communities, academic co-authorship networks) show meaningfully lower gaps than competitive knowledge-work cultures?

---

## Thread 10 — AI failure root causes divide into two independent classes requiring different mitigations

**The learning:** Production Large Language Model (LLM) failures cluster into two structurally independent root-cause classes: (1) *training-level failures*, where the error is encoded into model weights during pre-training or fine-tuning (Layer 1 hallucination via knowledge boundary collapse, Layer 3 reward hacking via reward model gaming); and (2) *architectural-level failures*, where the error emerges from deployment design rather than model weights (Layer 4 prompt injection via attention trust conflation, Layer 5 context overflow via architectural inability to drop low-salience tokens at length). The practical consequence is that mitigations must match the failure class: training-level failures require pre-training data curation, architecture changes (H-Neuron suppression), or fine-tuning — post-deployment prompt engineering cannot fix them. Architectural failures require infrastructure-level interventions (input validation, trust-isolated context segments, dynamic context compression) — improved training cannot prevent them if the deployment architecture preserves the exploit surface. Cross-class cascade paths (Layer 4→Layer 2 goal failure; Layer 5→Layer 1 hallucination) make the class distinction operationally critical: a Layer 4 exploit that appears to be a "security" problem also produces a Layer 2 reasoning failure, and treating only the security layer leaves the downstream goal failure unaddressed.

**Evidence:**
- `Research/completed/2026-03-12-failure-mode-taxonomy-expansion.md` — five-layer failure taxonomy with root causes per layer; cascade path analysis (B: L4→L2, A: L5→L1); empirical frequency data (OWASP LLM Top 10; Cleanlab 2025 enterprise survey); H-Neuron evidence (Vennemeyer et al. ICLR 2026, open-weight models: Mistral, Gemma-3, Llama-3 families)
- `Research/completed/2026-03-10-ai-concept-classification-taxonomy.md` — parent taxonomy establishing the five-layer structure; training-time vs. inference-time dimension as a first-pass classifier
- `Research/completed/2026-03-10-hallucination-mechanisms-h-neurons.md` — H-Neuron suppression as a direct training-level mitigation; distinct mechanism from architectural mitigations

**Open thread:** Are training-level and architectural-level failure classes fully independent, or do they interact? (E.g., does a reward-hacked model have a wider prompt injection surface because it has learned to find reward-maximising paths through adversarial inputs?) Does the two-class taxonomy hold for non-transformer architectures (state-space models, diffusion models)?
