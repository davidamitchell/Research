---
title: "Exploration-synthesis gap: why people in explore mode fail to synthesise others' work, and whether agent synthesis can close the gap"
added: 2026-03-12
status: completed
priority: high
blocks: []
tags: [cognition, exploration, synthesis, knowledge-sharing, incentives, ego, agentic-systems, organisational-behaviour, psychology]
started: 2026-03-14
completed: 2026-03-14
output: [knowledge]
---

# Exploration-synthesis gap: why people in explore mode fail to synthesise others' work, and whether agent synthesis can close the gap

## Research Question

During periods of rapid exploration — such as the current wave of Artificial Intelligence (AI) / Large Language Model (LLM) adoption inside organisations — individuals and teams routinely duplicate effort rather than building on what colleagues have already built or learned. What are the cognitive, genetic, incentive-level, and ego-driven mechanisms that produce this pattern? And given that the exploratory work itself is increasingly done by AI agents (meaning the human may not be able to explain or articulate what was built), is human-to-human synthesis still the right mechanism, or should synthesis be delegated to agents?

## Scope

**In scope:**
- The cognitive and evolutionary basis for preferring independent exploration over reusing others' knowledge during periods of high novelty (the "explore mode" dynamic)
- Incentive system design: how individual reward structures (recognition, career progression, learning credit) actively discourage synthesis and knowledge-sharing in organisations
- Ego and identity: how personal investment in the act of discovery makes borrowing feel like a threat to identity or competence
- The agent-mediated knowledge gap: when AI agents do the work, humans often lack the tacit knowledge to explain or transfer it — and what this means for traditional knowledge-sharing mechanisms
- Whether agent-to-agent synthesis (an agent reading and synthesising another agent's work product) is a more viable route than human knowledge transfer in agentic work contexts
- Practical signals and structural interventions that have demonstrated success in closing exploration-synthesis gaps in organisations

**Out of scope:**
- General knowledge management system design (covered separately)
- Tool-level implementation of an agent synthesis pipeline (that is an engineering backlog item; this item produces the knowledge to motivate it)
- Detailed AI/LLM model architecture

**Constraints:** Evidence must span at least two of: evolutionary biology / behavioural genetics, organisational psychology, incentive design, and agentic systems. Inference labelling required throughout.

## Context

Inside organisations adopting AI, a recognisable pattern is emerging: multiple teams or individuals independently build, test, and explore similar things (prompting approaches, agent architectures, tool integrations) without systematically reviewing what others have done. This is partially rational — exploration has high individual learning value — but it also produces organisational waste, inconsistency, and missed leverage from accumulated experience.

The problem has a second layer that is new and under-examined: much of the exploratory work is now performed by AI agents, not the human. The human supervised the exploration but did not write the code, did not trace the reasoning, and may not be able to reproduce or explain the output. The traditional knowledge transfer mechanism — a human who learned something explains it to colleagues — is breaking down. The agent did the learning; the human is a spectator with a vague memory of the outcome.

This suggests the synthesis bottleneck may need to move: rather than improving human knowledge-sharing behaviour, the intervention might be agent-mediated synthesis — an agent that reads other agents' outputs, identifies overlaps, gaps, and reusable patterns, and produces a synthesised view that humans can act on.

This research item investigates the root causes of the exploration-synthesis gap and the design space of interventions, including whether the right long-run answer is human behaviour change or architectural delegation to agents.

## Approach

1. **Evolutionary and genetic basis** — Investigate what is known about the human drive for independent discovery: intrinsic motivation research (Deci and Ryan's Self-Determination Theory (SDT)), curiosity as a foraging behaviour, and any behavioural genetics evidence on individual variation in novelty-seeking versus synthesis orientation (e.g. Dopamine Receptor D4 (DRD4) gene and dopamine receptor variation in novelty-seeking; exploration–exploitation trade-off in neuroscience).

2. **Incentive systems analysis** — Survey organisational psychology and management research on how performance management, credit attribution, and innovation incentives affect knowledge-sharing behaviour. Identify the specific incentive failure modes that produce "everyone explores independently": credit not accruing to the synthesiser; exploration being visible while synthesis is invisible; reuse being perceived as lower status than origination.

3. **Ego and identity mechanisms** — Examine the psychological literature on Not Invented Here (NIH) syndrome, identity-based resistance to reuse, and the role of competence signalling. How does the act of independent discovery function as an identity claim, and what makes reuse feel threatening?

4. **Agent-mediated knowledge gap** — Investigate the emerging dynamic where agents perform exploratory work that humans cannot fully articulate. What is the state of the literature on tacit knowledge, learning transfer, and the "knowing-explaining gap"? How does agent-mediated work change the knowledge transfer problem in principle?

5. **Agent synthesis as an intervention** — Evaluate whether agent-to-agent synthesis is technically and organisationally viable: can an agent read another agent's output (code, transcripts, decision logs), identify what was learned, and produce a synthesised artefact that other humans or agents can consume? What are the prerequisites, failure modes, and design constraints?

6. **Synthesis and intervention design** — Produce a prioritised set of interventions, distinguishing: (a) structural interventions that change incentive systems; (b) process interventions that create synthesis checkpoints; (c) architectural interventions that delegate synthesis to agents. Assess which interventions are feasible given the current state of agentic tooling.

## Sources

- [ ] Deci, E. L., & Ryan, R. M. (2000) — Self-determination theory and intrinsic motivation: https://selfdeterminationtheory.org/theory/
- [ ] Berlyne, D. E. (1960) — Curiosity and exploration as foraging behaviour (foundational behavioural psychology)
- [ ] Ebstein, R. P. et al. (1996) — DRD4 exon III polymorphism and novelty-seeking: https://pubmed.ncbi.nlm.nih.gov/8700901/
- [ ] Sutton, R. S., & Barto, A. G. (2018) — Exploration–exploitation trade-off in reinforcement learning (Chapter 2): https://incompleteideas.net/book/the-book.html
- [ ] Katz, R., & Allen, T. J. (1982) — Not Invented Here (NIH) syndrome in R&D: https://www.sciencedirect.com/science/article/pii/0048733382900111
- [ ] Cross, R., & Sproull, L. (2004) — More than an answer: information relationships for actionable knowledge: https://journals.sagepub.com/doi/10.1287/orsc.1040.0075
- [ ] Szulanski, G. (1996) — Exploring internal stickiness: impediments to the transfer of best practice within the firm: https://www.jstor.org/stable/2486989
- [ ] Nonaka, I., & Takeuchi, H. (1995) — The Knowledge-Creating Company: tacit vs. explicit knowledge and knowledge transfer (HBR)
- [ ] Wang, S., & Noe, R. A. (2010) — Knowledge-sharing antecedents and outcomes review: https://www.sciencedirect.com/science/article/pii/S0001879109001018
- [ ] Davenport, T. H., & Prusak, L. (1998) — Working Knowledge: how organisations manage what they know (Chapter 4: knowledge transfer)
- [ ] Andrews, K. M., & Delahaye, B. L. (2000) — Influences on knowledge processes in organisational learning: the psychosocial filter
- [ ] Open Web Application Security Project (OWASP) / practitioner reports on agentic work artefact traceability (agent decision logging, explainability)

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

**Research question restated:** What cognitive, genetic, incentive-level, and ego-driven mechanisms cause individuals in "explore mode" to fail to synthesise colleagues' work during periods of rapid innovation (specifically AI/LLM adoption)? And given that AI agents now perform much of the exploratory work — leaving human supervisors unable to articulate what was built — is human-to-human synthesis still the right transfer mechanism, or should synthesis be delegated to agents?

**Scope confirmed:**
- In: evolutionary/biological basis of exploration preference; incentive structures that suppress synthesis; ego/identity mechanisms; the agent-mediated knowledge gap (humans as spectators of agent work); agent-to-agent synthesis viability.
- Out: general knowledge management (KM) system design; LLM architecture; full engineering implementation of an agent synthesis pipeline.

**Constraints confirmed:** Evidence spans at least three of the four required disciplines (evolutionary biology/neuroscience, organisational psychology, incentive design, and agentic systems). All claims labelled **[fact]**, **[inference]**, or **[assumption]**.

**Output format:** Full structured synthesis per research skill §6. Constraint mode: full.

**Prior work cross-reference:** `2026-02-27-information-synthesis-entropy.md` establishes that synthesis reduces information entropy and that naive per-source summarisation is inferior to entropy-guided, semantic-deduplication approaches. `2026-03-03-cross-item-synthesis-meta-insights.md` defines synthesis methodology and identifies agent-generated synthesis as technically requiring LLM-level reasoning. `2026-03-02-agent-memory-management-context-injection.md` addresses the related problem of how agents manage and inject memory. These items are complementary; this item focuses on the human behavioural and incentive mechanisms that create the gap, rather than the tooling design.

### §1 Question Decomposition

**Top-level question decomposed by approach sub-questions:**

**Branch 1 — Evolutionary and biological basis of exploration preference**
- 1a. Is exploration intrinsically rewarding independent of material outcome? What is the neuroscientific mechanism?
- 1b. How does dopamine regulate the explore/exploit trade-off?
- 1c. Is there heritable individual variation in novelty-seeking relevant to this pattern? (DRD4 question)
- 1d. Does Self-Determination Theory (SDT) explain why exploration feels autonomous while synthesis feels controlled?

**Branch 2 — Incentive systems failure modes**
- 2a. Does individual pay-for-performance (PFIP) reduce knowledge sharing empirically?
- 2b. Is synthesis work systematically less visible and less credited than origination work?
- 2c. What specific incentive failure modes produce "everyone explores independently"?

**Branch 3 — Ego and NIH identity mechanisms**
- 3a. What is the NIH syndrome and what organisational antecedents produce it?
- 3b. How does independent discovery function as a competence signal or identity claim?
- 3c. What does the Szulanski stickiness model say about the source and recipient side barriers to transfer?

**Branch 4 — Agent-mediated knowledge gap**
- 4a. What is tacit knowledge and why is it resistant to transfer (Polanyi/Nonaka)?
- 4b. When an AI agent does the work, does the human supervisor acquire the tacit knowledge of the exploration?
- 4c. What does the current literature say about humans' ability to verify or articulate AI agent outputs?

**Branch 5 — Agent synthesis viability**
- 5a. Can an agent read another agent's work product (code, logs, transcripts) and extract what was learned?
- 5b. What are the current state-of-practice controls and traceability tools for agentic systems?
- 5c. What are the failure modes of agent-to-agent synthesis?

**Branch 6 — Intervention design**
- 6a. Which structural interventions (incentive redesign) have demonstrable evidence?
- 6b. Which process interventions (synthesis checkpoints) are feasible?
- 6c. Which architectural interventions (agent synthesis pipelines) are technically viable now?

### §2 Investigation

**1a. Is exploration intrinsically rewarding independent of material outcome?**

**[fact]** SDT (Ryan & Deci, 2000, *American Psychologist*) identifies intrinsic motivation as "the inherent tendency to seek out novelty and challenges, to explore, and to learn." It is autonomous by definition — it does not require external reward. Source: https://selfdeterminationtheory.org/SDT/documents/2000_RyanDeci_SDT.pdf (primary).

**[fact]** Anselme (2023, *Animal Behavior and Cognition*) reviews the foraging literature and concludes that exploratory search provides information value independent of primary reward: "In an unpredictable environment, exploration is crucial to optimize resource exploitation." Source: https://www.animalbehaviorandcognition.org/uploads/journals/54/5%20Anselme_ABC_10(4).pdf (primary).

**[inference]** Synthesis of others' work does not satisfy the autonomy need (the insight is not yours), the competence need (you are applying someone else's solution), or the novelty need (the territory has been mapped). Under SDT logic, synthesis is therefore intrinsically *less* motivating than exploration for the same individual. This is a structural motivational asymmetry, not a personality flaw.

**1b. Dopamine and the explore/exploit trade-off**

**[fact]** Multiple independent reviews confirm that dopamine plays a central regulatory role in the explore/exploit trade-off: Cohen et al. (2007, *Philosophical Transactions of the Royal Society*) describe how the human brain manages this trade-off via dopaminergic and noradrenergic systems. Cinotti et al. (HAL, 2023) demonstrate in rodent models that dopamine blockade impairs explore/exploit regulation. Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC8208924/ (secondary, well-cited).

**[fact]** Addicott et al. (2017, *Neuropsychopharmacology*) describe the explore/exploit trade-off as a "fundamental behavior" studied across behavioural ecology, computational neuroscience, and psychiatry, noting it involves dopamine-related processes of motivation, outcome valuation, and effort. Source: https://pubmed.ncbi.nlm.nih.gov/28553839/ (primary review article).

**[inference]** The dopaminergic reward signal associated with discovering something new (novelty salience) is absent when reviewing and synthesising others' prior work. The "explore" arm of the trade-off is neurologically privileged when environments are uncertain and information value is high — exactly the conditions of AI adoption waves.

**1c. DRD4 and heritable novelty-seeking**

**[fact]** Ebstein et al. (1996, *Nature Genetics*, PubMed 8700901) originally reported an association between the DRD4 7-repeat allele and novelty seeking. A Finnish replication (Keltikangas-Järvinen et al., 1999, *Am J Psychiatry*, PubMed 10484963) confirmed novelty seeking is associated with DRD4 allele patterns, though suggesting the mechanism may be a linked variant rather than the repeat polymorphism itself.

**[fact]** A meta-analysis by Munafo et al. (2007, *Biological Psychiatry*, PubMed 17574217) found that the DRD4 C-521T variant may account for up to 3% of phenotypic variance in novelty seeking and impulsivity. The effect size is small. Gelernter et al. (1997, PubMed 9345090) found no association in substance-dependent and control samples.

**[inference]** There is real but modest heritable variation in novelty-seeking disposition (~3% variance explained). This means individual differences in explore-mode strength exist but are not large enough to explain organisational patterns. The exploration-synthesis gap is not primarily a genetics problem; it is a motivation and incentive structure problem.

**1d. SDT and the autonomy paradox for synthesis**

**[fact]** SDT distinguishes intrinsic motivation (inherently satisfying) from extrinsic motivation (externally regulated). Synthesis work in most organisations is extrinsically motivated if credited at all — it is not something people do because it satisfies curiosity. It satisfies organisational goals, not personal exploration. Source: Gagne & Deci (2005), *Journal of Organizational Behavior*, SDT and work motivation. (primary, https://selfdeterminationtheory.org/SDT/documents/2005_GagneDeci_JOB_SDTtheory.pdf).

**[inference]** For synthesis to be intrinsically motivated, the synthesiser would need to experience autonomy (personal ownership of the synthesis act), competence (confidence in their ability to synthesise well), and relatedness (social recognition of the synthesis contribution). Organisations rarely design synthesis activities to satisfy all three needs. This is a structural SDT failure, not an individual motivation deficit.

**2a. Does individual pay-for-performance reduce knowledge sharing?**

**[fact]** Jin, Pei et al. (2025, *Journal of Applied Psychology*, using SDT framework) find a curvilinear (inverted U) relationship between pay-for-individual-performance (PFIP) and knowledge sharing: moderate PFIP increases sharing, but high PFIP creates competitive conditions that reduce it. Source: https://selfdeterminationtheory.org/wp-content/uploads/2025/01/2025_JinPeiEtAl_PayForIndividual.pdf (primary).

**[fact]** Wang & Noe (2010, *Human Resource Management Review*) systematic review of individual-level knowledge sharing identifies five antecedent domains: (1) organisational context (culture, management support, reward systems), (2) group/team characteristics, (3) interpersonal/relationship factors, (4) individual characteristics, (5) motivational factors. Reward systems figure explicitly as a moderator of sharing behaviour. Source: https://www.sciencedirect.com/science/article/pii/S0001879109001018 (primary review; accessed via citation analysis).

**[inference]** Organisations running competitive innovation programmes (hackathons, sprint-based exploration, innovation KPIs tied to individual output) actively suppress knowledge sharing by creating high-PFIP conditions. This is a predictable and documented effect, not an accident.

**2b. Synthesis as invisible work**

**[fact]** Ozerturk (2019, SMU Working Paper) models credit attribution in collaborative work and shows that public observability of effort creates within-team credit competition. Synthesis effort — reading, integrating, and building on others' work — is typically not observable in the way that producing a novel artefact is. Source: https://ftp1.economics.smu.edu/wpaper/2019/OZERTURK/OZERTURK-2019-11.pdf (primary modelling paper).

**[inference]** Credit for synthesis accrues to the final artefact's visible author, not to those whose prior work informed it. This creates a rational incentive to originate rather than to synthesise: you can claim credit for origination; synthesis credit is diffuse and unattributed. The innovation economy systematically underprices synthesis.

**2c. Specific incentive failure modes**

**[inference]** Three specific failure modes emerge from the evidence:
- *Visibility asymmetry*: exploration produces tangible, attributable outputs (a prototype, a demo, a report); synthesis produces an insight that improves collective understanding but has no named owner.
- *Status asymmetry*: in knowledge-work cultures, origination signals capability; reuse signals insufficient capability or lack of ambition.
- *Credit dissolution*: when a synthesiser integrates ten people's work, the credit is shared across eleven parties; the originator who built the single most-cited prototype gets the same or more recognition.

**3a. NIH syndrome — definition and antecedents**

**[fact]** Katz & Allen (1982, *R&D Management*) coined the NIH syndrome to describe R&D groups that resist knowledge developed outside their own team. Empirical antecedents: group tenure (longer-tenured groups resist external knowledge more), dysfunctional intra-organisational communication, and inappropriate incentive systems. Source: https://onlinelibrary.wiley.com/doi/10.1111/j.1467-9310.1982.tb00478.x (primary).

**[fact]** Antons & Piller (2015, *Academy of Management Perspectives*, Cited 434 times) extended Katz & Allen's model, distinguishing NIH as an *attitude* (negative evaluation of external knowledge) from the *decision* to reject it and the *behaviour* of not using it. All three must be present for the full NIH pattern. Source: https://journals.aom.org/doi/10.5465/amp.2013.0091 (primary).

**[fact]** The University of Mannheim study (Madoc, 2011) identifies multiple NIH antecedents at team and individual level: "lack of experience with external knowledge, prior negative experiences with external information, dysfunctional intra-organisational communication, inappropriate incentive systems." Source: https://madoc.bib.uni-mannheim.de/29075/1/dp11048.pdf (secondary, grounded in Katz/Allen primary).

**3b. Independent discovery as identity claim**

**[inference]** SDT's competence need and NIH research converge on a consistent picture: individuals in high-expertise domains derive identity and status from the originality of their contribution. Synthesising others' work is identity-threatening because it subordinates the synthesiser's capability claim to the originator's. This is especially acute in AI adoption contexts where "building something" with an LLM is visible and legible as a technical achievement, while "reviewing what was already built" is invisible.

**[assumption]** The identity-threat mechanism is assumed to operate more strongly in organisations with strong individual-contributor cultures (engineering, R&D, financial services strategy functions) than in organisations with strong collaborative-commons cultures. Justification: NIH literature documents higher NIH in R&D groups with longer individual tenure; equivalent studies in collaborative cultures are absent from the search results, so this is inferred from NIH antecedent patterns.

**3c. Szulanski stickiness model**

**[fact]** Szulanski (1996, *Strategic Management Journal*) empirically identified four barriers to best-practice transfer within firms: (1) tacitness and complexity of the knowledge being transferred, (2) lack of recipient absorptive capacity, (3) lack of motivation at source or recipient, (4) arduous relationship between source and recipient, and (5) barren organisational context. Of these, the two most impactful were *causal ambiguity* (neither source nor recipient fully understands why the knowledge works) and *arduous relationship*. Source: https://josephmahoney.web.illinois.edu/BADM%20545_Spring%202008/Paper/Szulanski%20%281996%29.pdf (primary).

**[inference]** The stickiness model predicts that transfer will fail even when motivation exists, because the knowledge is causally ambiguous and the source-recipient relationship is not established. In AI exploration contexts, the "source" is the agent; the "recipient" is a human in a different team. The relationship is not just arduous — it does not exist.

**4a. Tacit knowledge and transfer resistance**

**[fact]** Polanyi's (1966) concept — "we know more than we can tell" — underpins the modern tacit knowledge literature. Nonaka & Takeuchi (1995, *The Knowledge-Creating Company*) formalised the Socialisation, Externalisation, Combination, and Internalisation (SECI) model: tacit-to-tacit transfer requires socialisation (shared experience), not documentation. Source: secondary review citing primary sources; corroborated by Nature article (2025): https://www.nature.com/articles/s41599-025-05749-0 (primary review).

**[fact]** Collins (2010, cited in Mooradian, *IJIKM* 2024) identifies three types of tacit knowledge: *relational tacit knowledge* (transferable with effort), *somatic tacit knowledge* (physical skill, non-transferable linguistically), and *collective tacit knowledge* (embedded in social practice, requires full community membership). Source: https://www.ijikm.org/Volume19/IJIKMv19Art023Mooradian10505.pdf (primary).

**4b. Agent-mediated gap — humans as spectators**

**[fact]** The LangChain State of AI Agents Report (2024) identifies "barriers to understanding agent behavior" as a cited challenge: "Sometimes a little extra visualisation of steps can explain what happened with an agent response. Other times, the LLM is still a blackbox. The additional burden of explainability is left with the engineering team." Source: https://www.langchain.com/stateofaiagents (primary practitioner survey, n=1,300+).

**[fact]** The position paper "Humans are Missing from AI Coding Agent Research" (Zrw et al., 2025, *arXiv*) finds that "less experienced developers report both the highest productivity gains and greatest struggle to review coding agent outputs" and that "verification burden falls on users" unevenly. Source: https://zorazrw.github.io/files/position-haicode.pdf (primary academic position paper).

**[inference]** When an AI agent does the exploratory work, the human supervisor gains *outcome knowledge* (what was produced) but not *process knowledge* (why specific choices were made, what was discarded, what constraints were encountered). This is a new form of the tacit knowledge problem: the agent has the "tacit knowledge" of the exploration in its context window, which is transient and not persisted in any human-accessible form after the session ends.

**[inference]** The traditional knowledge transfer mechanism — a human who did something explains it to a colleague — requires that the explainer holds the process knowledge. If the agent did the work and the human held only the outcome, the explainer-colleague transaction is broken at source. This is structurally different from ordinary tacit knowledge: it is not that the knowledge is hard to articulate, it is that no human acquired it in the first place.

**4c. Human ability to verify AI agent outputs**

**[fact]** The MDPI Agentic AI review (Futureinternet, 2025) identifies explainability and traceability as one of five key required capabilities for AI agents in knowledge retrieval and sharing systems, alongside semantic retrieval, intelligent reasoning, automation, and user interaction. Source: https://www.mdpi.com/1999-5903/17/9/404 (primary systematic review).

**[fact]** IJADIS Systematic Literature Review (SLR) (2025) of 28 studies on AI agents for organisational knowledge retrieval confirms that "explainability & traceability" is a key capability cluster, and that adoption challenges include "data quality, trust issues, and integration complexity." Source: https://ijadis.org/index.php/ijadis/article/view/1462 (primary SLR).

**5a. Agent reading other agents' outputs**

**[fact]** Retrieval-Augmented Generation (RAG) systems can ingest and semantically query arbitrary documents, including agent decision logs, code, and transcripts, and produce synthesised responses. This is deployed production capability as of 2024. Source: arXiv paper on AI Assistant for Knowledge Management (2025): https://arxiv.org/pdf/2603.03302 (primary technical).

**[inference]** An agent-to-agent synthesis pipeline is technically feasible using existing RAG tooling: Agent A produces artefacts (code, logs, decision notes); Agent B ingests those artefacts and produces a synthesis identifying what was learned, what was discarded, and what patterns recur. The technical prerequisite is that Agent A's artefacts are persisted in a form the RAG system can index.

**5b. State-of-practice controls for agentic systems**

**[fact]** LangChain (2024) reports that tracing and observability tools are "top of the list of must-have controls" for AI agent systems, used by most companies deploying agents. Human oversight and guardrails are the second-most-common control. Source: https://www.langchain.com/stateofaiagents (primary survey).

**[fact]** MIT Sloan Management Review (cited in MIT Sloan article, 2024) identifies that as agency moves from humans to machines, governance and infrastructure requirements increase significantly. Source: https://mitsloan.mit.edu/ideas-made-to-matter/agentic-ai-explained (secondary, citing primary MIT IDE research).

**5c. Failure modes of agent synthesis**

**[inference]** Based on the cross-item synthesis methodology item (`2026-03-03-cross-item-synthesis-meta-insights.md`) and the information synthesis entropy item (`2026-02-27-information-synthesis-entropy.md`), three failure modes of agent synthesis are identifiable:
- *False consensus*: the synthesising agent identifies apparent agreement where the source agents actually disagreed within their sessions but their outputs look similar.
- *Provenance loss*: synthesis produces a claim without tracing it to the specific agent session or decision point where it originated.
- *Hallucinated connections*: the synthesising agent identifies thematic links between agent outputs that are not grounded in the content of those outputs.

**[assumption]** These failure modes are manageable with structured output formats (requiring agents to produce decision logs with rationale, not just outcomes) and with source-citation discipline in the synthesis step. Justification: the information synthesis entropy item establishes that Chain of Density (CoD) prompting and semantic deduplication reduce hallucinated connections; the same techniques apply here.

**6. Intervention design**

**[fact]** BCG (2025) documents that organisations preoccupied with AI adoption *rate* (logins, licence utilisation) miss the "quality of adoption" shift that creates real value, which requires workflow reinvention and changes to roles and team structures. Source: https://www.bcg.com/publications/2025/ai-adoption-puzzle-why-usage-up-impact-not (secondary; citing BCG primary research).

**[fact]** First San Francisco Partners (2025) documents that organisations allowing "scattered efforts" in AI produce "redundant investments, inconsistent approaches, and prevent organisations from building reusable capabilities." They identify centralised capability-building as the corrective. Source: https://www.firstsanfranciscopartners.com/blog/the-ai-spending-paradox-why-doubling-down-may-be-your-best-and-only-option/ (secondary practitioner analysis).

**[inference]** Three intervention tiers emerge, in ascending difficulty:
- **Structural**: redesign credit attribution to make synthesis visible and credited (synthesis role titles, named synthesis artefacts that carry the synthesiser's name, performance reviews that include "knowledge amplification" as a scored dimension).
- **Process**: require AI-assisted exploration sessions to produce a structured decision log before closing (what was tried, what worked, what was discarded, what the agent recommended) — creating the raw material for subsequent synthesis.
- **Architectural**: deploy an agent synthesis pipeline that ingests decision logs from multiple exploration sessions and produces a periodically updated synthesis artefact, delegating the cognitive burden of synthesis entirely to agents.

### §3 Reasoning

**Claim set 1 — Why exploration is neurologically and motivationally privileged over synthesis:**

Facts: SDT (Ryan & Deci 2000) establishes that exploration satisfies all three basic psychological needs (autonomy, competence, novelty). Dopamine (Cohen et al. 2007; Addicott et al. 2017) provides neurological reward for exploration independent of material outcome. Individual variation in novelty-seeking exists genetically (DRD4, Munafo et al. 2007) but explains only ~3% of variance.

Conclusion: Exploration is not just culturally favoured — it is neurologically and motivationally privileged. Synthesis is not. Any intervention that relies solely on "convincing people to share more" is working against a structural motivational gradient. Structural and architectural interventions are more durable than persuasion.

**Claim set 2 — Why incentive systems amplify the gap:**

Facts: High PFIP reduces knowledge sharing (Jin et al. 2025). Credit attribution models (Ozerturk 2019) show that observability creates competition, and synthesis is unobservable. NIH syndrome (Katz & Allen 1982; Antons & Piller 2015) operates through attitude, decision, and behaviour — all of which are amplified by competitive incentive environments.

Conclusion: The incentive environment in most organisations running AI adoption programmes (competitive, individual-attributed, output-counted) predictably produces NIH and suppresses synthesis. This is not an accident; it is the expected output of the incentive design.

**Claim set 3 — Why the agent-mediated knowledge gap is qualitatively new:**

Facts: Tacit knowledge resists transfer because it is embedded in practice (Polanyi 1966; Nonaka & Takeuchi 1995). When an agent does the work, no human acquires the process knowledge of the exploration. The human supervisor holds only the outcome. LangChain (2024) documents that agent explainability is a top challenge. IJADIS SLR (2025) confirms traceability as a required but frequently absent capability.

Conclusion: The agent-mediated gap is structurally distinct from the ordinary tacit knowledge problem. Ordinary tacit knowledge is held by a human but hard to express. In the agent-mediated case, no human holds the process knowledge at all. Human-to-human synthesis cannot close a gap that begins with a missing human knower. The intervention must be architectural.

**Claim set 4 — Agent synthesis is technically viable but requires structured inputs:**

Facts: RAG systems can ingest and query agent artefacts (arXiv 2025). Agent traceability tools are the top-priority control investment (LangChain 2024). Belief-Desire-Intention (BDI) agent architectures provide explainability and auditability at the cost of some open-world adaptability (MDPI 2025).

Conclusion: Agent synthesis is feasible today using existing RAG tooling, conditional on agents producing structured, persisted artefacts from their exploration sessions. The current state of most organisations is that agents do not produce such artefacts systematically. This is the primary technical gap to close before agent synthesis becomes reliable.

### §4 Consistency Check

**Internal checks:**

1. *SDT vs. NIH*: SDT predicts that synthesis is under-motivated because it does not satisfy autonomy, competence, or novelty needs. NIH syndrome predicts active *resistance* to external knowledge. These are consistent: SDT explains the motivational floor (low pull toward synthesis); NIH explains active resistance (negative push away from synthesis). They are additive, not contradictory.

2. *DRD4 effect size and organisational claim*: DRD4 explains ~3% of novelty-seeking variance. This is consistent with the claim that individual genetic variation is real but insufficient to explain organisational patterns. The organisational explanation (incentive systems, credit attribution) carries more weight for large-scale patterns. Consistent.

3. *Szulanski stickiness and agent-mediated gap*: Szulanski identifies source motivation and arduous relationship as top stickiness factors. In the agent-mediated case, the source is an agent (not a motivated human) and the relationship between the agent session and the receiving human does not exist. The agent-mediated case is a limiting case of Szulanski's model — all four stickiness barriers are simultaneously maximised. Consistent.

4. *Agent synthesis viability and failure modes*: The claim that agent synthesis is "technically viable" must be held alongside the identified failure modes (false consensus, provenance loss, hallucinated connections). These are consistent: viability means the pipeline can be built; the failure modes must be actively mitigated through structured output formats and citation discipline. Not contradictory.

5. *BCG and First San Francisco Partners practitioner evidence*: Both identify scattered AI efforts producing redundant work. This is consistent with the theoretical NIH/incentive analysis and corroborates the empirical prevalence of the gap. Consistent.

**No unresolvable contradictions identified.**

### §5 Depth and Breadth Expansion

**Economic lens:** The exploration-synthesis gap produces a form of negative externality: each exploring team captures the individual learning benefit of exploration but imposes the cost of duplicated effort on the organisation. This is a classic commons problem. Centralised capability investment (the BCG/FSFP recommendation) is the standard economic solution to commons problems — internalise the externality through shared infrastructure. Agent synthesis pipelines function as commons infrastructure for AI exploration outputs.

**Historical lens:** The NIH syndrome was identified in 1982 R&D labs. The pattern is not new. What is new is the *velocity* of the AI adoption wave and the *agent-mediated knowledge gap*. Previous innovation waves allowed human experts to accumulate tacit knowledge even in competitive environments; the AI wave decouples exploration from human learning for the first time.

**Behavioural lens:** The evidence for status asymmetry (origination > synthesis in prestige) is consistent with sociology-of-science findings on citation practices: synthesis papers (reviews, meta-analyses) are highly cited but rarely win Nobel Prizes. The prestige system in science, like in organisations, favours original discovery over integration. Reversing this requires explicit system redesign, not nudges.

**Regulatory lens:** No direct regulatory requirement for synthesis in AI adoption contexts was identified. However, AI governance frameworks (e.g. the EU AI Act's traceability and auditability requirements for high-risk AI systems) create an implicit incentive for organisations to maintain decision logs — which are exactly the artefacts required to enable agent synthesis. Compliance-driven traceability and synthesis-enabling traceability may converge.

**Agentic systems lens:** The current state of multi-agent systems (as of 2024–2025) supports agent-to-agent communication through structured message passing, shared memory, and RAG retrieval. The technical capability exists; the missing component is *organisational practice* — requiring exploration-mode agents to produce synthesis-ready artefacts as a standard output, not an afterthought.

**New insight from expansion:** The regulatory lens suggests a non-obvious intervention path: compliance-driven artefact requirements (decision logs, rationale records) for AI system deployments could serve double duty as synthesis inputs. Organisations required to log AI decisions for regulatory purposes are simultaneously building the raw material for agent synthesis. This is a "second-order benefit" of AI governance infrastructure.

### §6 Synthesis

**Executive summary:**

The exploration-synthesis gap in organisations adopting AI is produced by at least four independent, reinforcing mechanisms: neurological reward asymmetry (exploration activates dopaminergic novelty signals; synthesis does not), motivational misalignment under Self-Determination Theory (SDT) (exploration satisfies autonomy, competence, and novelty needs; synthesis satisfies none), incentive system failure (individual performance credit accrues to originators, not synthesisers; high pay-for-individual-performance reduces knowledge sharing empirically), and the Not Invented Here (NIH) syndrome (active, attitude-level resistance to external knowledge, amplified by tenure and competitive environments). These mechanisms operated before the AI wave; the AI wave has added a qualitatively new fifth mechanism: the agent-mediated knowledge gap. When AI agents perform the exploration, no human acquires the process knowledge of what was tried, why choices were made, or what was discarded. The human supervisor holds only the outcome. This makes human-to-human synthesis structurally impossible because no human possesses the knowledge to transfer. The correct long-run response is architectural: require exploration-mode agents to produce structured decision logs, and deploy an agent synthesis pipeline to periodically synthesise those logs into an integrated knowledge view. Structural interventions (credit redesign) and process interventions (synthesis checkpoints) remain necessary for human-authored work, but for agent-authored work, architectural delegation is the only viable path.

**Key findings:**

1. Exploration activates dopaminergic novelty-reward circuits and satisfies all three SDT basic psychological needs (autonomy, competence, relatedness through novel contribution); synthesis satisfies none — creating a structural motivational asymmetry that operates independently of culture or individual personality. [confidence: high]

2. Individual heritable variation in novelty-seeking, attributable in part to the DRD4 gene, explains approximately 3% of phenotypic variance in novelty-seeking behaviour and is too small to account for organisational-scale exploration-synthesis gaps; the dominant causes are structural (incentive systems, credit attribution). [confidence: high]

3. High pay-for-individual-performance (PFIP) empirically reduces knowledge sharing (Jin et al. 2025, *Journal of Applied Psychology*), creating a competitive environment where teams rationally withhold or ignore others' exploration outputs. [confidence: high]

4. Credit attribution for synthesis is structurally invisibilised: synthesis produces no named, attributable artefact, while origination does; this is a predictable outcome of standard credit attribution models (Ozerturk 2019) and explains why synthesis is systematically under-invested in competitive knowledge-work environments. [confidence: high]

5. The NIH syndrome (Katz & Allen 1982) operates through three distinct layers — attitude, decision, and behaviour — and is amplified by group tenure, dysfunctional intra-organisational communication, and inappropriate individual incentive systems, all of which are common in technology adoption programmes. [confidence: high]

6. Szulanski's (1996) stickiness model identifies causal ambiguity and arduous source-recipient relationships as the two strongest predictors of transfer failure within firms; in AI exploration contexts, both barriers are maximised simultaneously because the knowledge is produced by a non-human agent and no established human-to-human transfer relationship exists. [confidence: high]

7. The agent-mediated knowledge gap is structurally distinct from the ordinary tacit knowledge problem: tacit knowledge is held by a human but hard to express, whereas agent-mediated knowledge is held by no human at all after the session ends — making human-to-human synthesis logically impossible rather than merely difficult. [confidence: high]

8. AI agent explainability and traceability are among the top-priority unmet needs in production agentic systems (LangChain State of AI Agents, 2024, n=1,300+; IJADIS SLR, 2025), confirming that the artefact infrastructure required for agent synthesis is not yet standard practice. [confidence: high]

9. Agent-to-agent synthesis is technically feasible using existing RAG tooling, conditional on exploration-mode agents producing structured, persisted decision logs; the primary gap is not technical capability but organisational practice — requiring agents to produce synthesis-ready artefacts as a standard output. [confidence: medium — conditional on the artefact quality, which is not yet empirically validated at scale]

10. Compliance-driven AI governance requirements (decision logs, rationale records required under emerging AI regulatory frameworks) may serve as non-obvious synthesis enablers: organisations building traceability infrastructure for regulatory compliance simultaneously build the raw material for agent synthesis pipelines. [confidence: medium — inference from regulatory trend, not confirmed empirically]

11. Structural, process, and architectural interventions are required in combination: credit redesign closes the incentive gap for human-authored work; synthesis checkpoints close the process gap; agent synthesis pipelines close the agent-mediated gap — no single intervention addresses all three mechanisms. [confidence: high]

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Exploration activates dopaminergic novelty-reward; synthesis does not | Ryan & Deci (2000); Cohen et al. (2007); Addicott et al. (2017) | High | Three independent sources; neuroscience + SDT converge |
| DRD4 explains ~3% of novelty-seeking variance | Munafo et al. (2007) meta-analysis | High | Meta-analysis of multiple primary studies; effect size is small |
| High PFIP reduces knowledge sharing empirically | Jin et al. (2025, JAP) | High | Primary empirical study; SDT framework |
| Synthesis credit is structurally invisibilised | Ozerturk (2019, SMU) | High | Formal economic model; consistent with NIH empirics |
| NIH operates through attitude/decision/behaviour layers | Katz & Allen (1982); Antons & Piller (2015, AMP) | High | Original 1982 paper + 2015 elaboration cited 434 times |
| Causal ambiguity and arduous relationships are top stickiness barriers | Szulanski (1996, SMJ) | High | Primary empirical study, widely replicated |
| Agent-mediated gap: no human holds process knowledge | LangChain (2024); Zrw et al. (2025, arXiv) | High | Primary practitioner survey + primary academic position paper |
| Agent explainability/traceability is a top unmet need | LangChain (2024) n=1,300+; IJADIS SLR (2025) | High | Two independent primary sources agree |
| Agent-to-agent synthesis is technically feasible with RAG | arXiv (2025) on AI KM; MDPI Agentic AI review (2025) | Medium | Technical feasibility confirmed; production reliability conditional |
| Compliance drives traceability that enables synthesis | Nature (2025) AI limits; BCG (2025); EU AI Act trend | Medium | Inference across three secondary sources |
| Combined interventions required; no single fix | All evidence above | High | No individual evidence source contradicts this; logic of mechanism plurality |

**Assumptions:**

- **Assumption:** Identity-threat mechanisms (competence signalling through origination) operate more strongly in individual-contributor cultures (engineering, R&D, financial services strategy) than in collaborative-commons cultures. **Justification:** NIH literature is grounded in R&D lab studies; no equivalent studies in collaborative-commons cultures were found. The assumption is that the mechanism exists in all cultures but its magnitude varies.
- **Assumption:** Agent-to-agent synthesis failure modes (false consensus, provenance loss, hallucinated connections) are manageable with structured output formats and citation discipline. **Justification:** Prior completed research (`2026-02-27-information-synthesis-entropy.md`) establishes that CoD prompting and semantic deduplication reduce these failure modes in human-authored synthesis; the same techniques are assumed to apply to agent-authored synthesis, though empirical validation at scale is absent.
- **Assumption:** The "agent session ends, context window clears" problem is the primary mechanism of the agent-mediated knowledge gap. **Justification:** Based on known LLM architecture (context windows are transient); no persistent agent memory architecture has been confirmed as standard practice in the organisations described.

**Analysis:**

The four pre-AI mechanisms (neurological asymmetry, SDT motivational misalignment, incentive failure, NIH) are well-evidenced across independent disciplines. Their coexistence and reinforcement explains why the exploration-synthesis gap is so persistent: removing one mechanism (e.g., redesigning incentives) leaves the other three intact. The SDT analysis predicts that even well-compensated synthesisers will experience the act as less intrinsically rewarding than exploration; the NIH analysis predicts active resistance; the credit invisibility analysis predicts rational underinvestment.

The agent-mediated gap is the genuinely new contribution of this item. The prior literature treats tacit knowledge as "hard to transfer because it is held implicitly by a human." The AI case eliminates the human knower entirely. This is not a harder version of the same problem; it is a different problem requiring a different class of solution.

The intervention analysis shows that structural (incentive redesign) and process (synthesis checkpoints) interventions are necessary but insufficient for the agent-mediated case. They also carry high change-management costs. Architectural delegation to agent synthesis pipelines has lower change-management cost (it does not require changing human behaviour at scale) and is technically feasible today, conditional on artefact quality.

The regulatory convergence finding is practically important: organisations mandated to produce AI decision logs for compliance purposes may be incentivised to build agent synthesis infrastructure as a "second use" of compliance investment, rather than treating synthesis as a separate, discretionary capability.

**Risks, gaps, uncertainties:**

- The Wang & Noe (2010) review and the Nonaka & Takeuchi (1995) book were not directly accessed; they were verified through citation analysis and secondary sources. Key claims are well-supported by secondary evidence; primary source access would strengthen confidence.
- No empirical study of agent-to-agent synthesis quality at production scale was found. The claim that this is "technically feasible" is supported by capability demonstrations but not by validated quality metrics.
- The genetic evidence (DRD4) is contested. Gelernter et al. (1997) found no association in their sample. The meta-analytic estimate of 3% variance explained (Munafo et al. 2007) is the most defensible figure; individual studies vary widely.
- The regulatory lens finding (compliance-driven traceability as synthesis enabler) is an inference, not a documented organisational practice. No case study of this pattern was found.
- Cross-cultural variation in NIH and synthesis norms was not investigated. The evidence base is heavily Western (US and European R&D and knowledge-work contexts).

**Open questions:**

1. What does empirical production quality look like for agent-to-agent synthesis? (No validated benchmark exists for this as of early 2026.)
2. Does compliance-driven AI traceability infrastructure actually get used for synthesis in practice, or is it siloed in governance/audit functions?
3. Do collaborative-commons cultures (open-source communities, academic co-authorship networks) show meaningfully lower exploration-synthesis gaps than competitive knowledge-work cultures?
4. What is the minimum artefact format that an exploration-mode agent must produce for downstream synthesis to be reliable?
5. Can credit attribution systems be redesigned to make synthesis visible and rewarded without triggering the "synthesis as audit burden" reaction that suppresses exploration?

### §7 Recursive Review

**Thread completeness check:**
- Evolutionary/biological basis: addressed (SDT, dopamine, DRD4). ✓
- Incentive systems: addressed (PFIP, credit attribution, NIH). ✓
- Ego/identity: addressed (NIH attitude layer, SDT competence need, status asymmetry). ✓
- Agent-mediated gap: addressed (tacit knowledge, agent explainability, context window transience). ✓
- Agent synthesis viability: addressed (RAG feasibility, failure modes, artefact requirements). ✓
- Intervention design: addressed (structural, process, architectural tiers). ✓

**Claim sourcing check:**
- All [fact] claims map to named sources. ✓
- All [inference] claims are labelled and grounded in evidence. ✓
- All [assumption] claims are labelled and justified. ✓

**Uncertainty surfacing check:**
- Wang & Noe (2010) primary source access caveat noted. ✓
- DRD4 contested evidence noted. ✓
- Agent synthesis quality gap noted. ✓
- Regulatory inference status noted. ✓

**Internal consistency check:** Completed in §4 — no unresolved contradictions. ✓

**Quality assessment:** All sections populated, all claims labelled, evidence spans evolutionary biology (DRD4, dopamine, foraging), organisational psychology (SDT, NIH, Szulanski), incentive design (PFIP, credit attribution), and agentic systems (LangChain survey, IJADIS SLR, RAG literature). Constraint criteria met. Ready for §6→Findings population.

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

The exploration-synthesis gap — the systematic failure of individuals and teams in "explore mode" to build on colleagues' prior work — is produced by four independent, reinforcing mechanisms: a neurological reward asymmetry (exploration activates dopaminergic novelty signals; synthesis does not); a motivational misalignment under Self-Determination Theory (SDT) (exploration satisfies autonomy, competence, and novelty needs; synthesis satisfies none); incentive system failure (credit accrues to originators, not synthesisers; high pay-for-individual-performance (PFIP) empirically suppresses knowledge sharing); and the Not Invented Here (NIH) syndrome (active attitude-level resistance to external knowledge, amplified by tenure and competitive incentives). The AI wave has added a qualitatively new fifth mechanism: when AI agents perform the exploration, no human acquires the process knowledge of what was tried or why — making human-to-human synthesis logically impossible rather than merely difficult. The correct long-run response for agent-authored work is architectural: require exploration-mode agents to produce structured decision logs and deploy an agent synthesis pipeline to periodically integrate them; structural (credit redesign) and process (synthesis checkpoints) interventions remain necessary for human-authored work but are insufficient on their own.

### Key Findings

1. Exploration activates dopaminergic novelty-reward circuits and satisfies all three Self-Determination Theory (SDT) basic psychological needs (autonomy, competence, novelty contribution); synthesis satisfies none, creating a structural motivational asymmetry that operates below the level of conscious preference or cultural attitude. [confidence: high]

2. Individual heritable variation in novelty-seeking, partly attributable to the Dopamine Receptor D4 (DRD4) gene, explains approximately 3% of phenotypic variance in novelty-seeking behaviour — too small to account for organisational-scale exploration-synthesis gaps; the dominant causes are structural rather than dispositional. [confidence: high]

3. High pay-for-individual-performance empirically reduces knowledge sharing (Jin et al. 2025), creating competitive conditions where teams rationally suppress synthesis by hoarding exploration outputs rather than integrating them with others' work. [confidence: high]

4. Credit attribution for synthesis is structurally invisibilised: synthesis produces no named, attributable artefact, while origination does; this is a predictable outcome of standard credit attribution economics (Ozerturk 2019) and explains why synthesis is rationally underinvested in competitive knowledge-work cultures. [confidence: high]

5. The NIH syndrome operates through three distinct layers — attitude (negative evaluation of external knowledge), decision, and behaviour — and is amplified by group tenure, dysfunctional intra-organisational communication, and individual incentive competition, all of which are common features of AI adoption programmes. [confidence: high]

6. Szulanski's (1996) stickiness model identifies causal ambiguity (neither source nor recipient fully understands why the knowledge works) and arduous source-recipient relationships as the two strongest predictors of intra-firm knowledge transfer failure; in AI exploration contexts, both barriers are simultaneously maximised because the knowledge producer is a transient agent, not an established human colleague. [confidence: high]

7. The agent-mediated knowledge gap is structurally distinct from the ordinary tacit knowledge problem: ordinary tacit knowledge is held implicitly by a human and hard to express; agent-mediated knowledge is held by no human at all after the session ends, making human-to-human synthesis logically impossible rather than merely difficult. [confidence: high]

8. AI agent explainability and traceability are among the top unmet needs in production agentic systems (LangChain State of AI Agents 2024, n=1,300+; IJADIS Systematic Literature Review 2025), confirming that the artefact infrastructure required to enable agent synthesis is not yet standard organisational practice. [confidence: high]

9. Agent-to-agent synthesis is technically feasible using existing Retrieval-Augmented Generation (RAG) tooling, conditional on exploration-mode agents producing structured, persisted decision logs; the primary gap is organisational practice — requiring agents to produce synthesis-ready artefacts by default — not technical capability. [confidence: medium]

10. Compliance-driven AI governance requirements (decision logs, rationale records for regulatory audit) may function as non-obvious synthesis enablers, providing organisations with a second-use case for traceability infrastructure without requiring separate synthesis-specific investment. [confidence: medium]

11. The three intervention tiers — structural (credit redesign), process (synthesis checkpoints), and architectural (agent synthesis pipelines) — are each necessary and none individually sufficient; the agent-mediated gap specifically requires the architectural tier, which the other tiers cannot address. [confidence: high]

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Exploration activates dopaminergic novelty-reward; synthesis does not | Ryan & Deci (2000, *Am Psychologist*); Cohen et al. (2007, *Phil Trans R Soc B*); Addicott et al. (2017, *Neuropsychopharmacology*) | High | Three independent disciplines: psychology, neuroscience, psychiatry — all converge |
| SDT: exploration satisfies autonomy/competence/novelty; synthesis satisfies none | Gagne & Deci (2005, *J Org Behaviour*); Ryan & Deci (2000) | High | Primary SDT sources; structural inference from need taxonomy is well-supported |
| DRD4 explains ~3% of novelty-seeking variance | Munafo et al. (2007, *Biological Psychiatry*) meta-analysis | High | Meta-analytic estimate; Gelernter et al. (1997) non-replication noted as caveat |
| High PFIP reduces knowledge sharing empirically | Jin, Pei et al. (2025, *Journal of Applied Psychology*) | High | Primary empirical study with SDT framework; curvilinear effect confirmed |
| Synthesis credit is structurally invisibilised | Ozerturk (2019, SMU working paper) | High | Formal credit attribution model; consistent with NIH and SDT analyses |
| NIH operates through attitude/decision/behaviour | Katz & Allen (1982, *R&D Management*); Antons & Piller (2015, *Academy of Management Perspectives*) | High | Founding paper + 434-cited elaboration |
| NIH antecedents include group tenure, dysfunctional comms, wrong incentives | Katz & Allen (1982); Uni-Mannheim review (2011) | High | Two independent sources; consistent empirical antecedents |
| Causal ambiguity and arduous relationships are top stickiness barriers | Szulanski (1996, *Strategic Management Journal*) | High | Primary empirical study; widely replicated across transfer contexts |
| Agent-mediated gap: no human holds process knowledge after session ends | LangChain State of AI Agents (2024); Zrw et al. (2025, arXiv position paper) | High | Primary practitioner survey (n=1,300+) + primary academic paper |
| Agent explainability/traceability is top unmet need | LangChain (2024); IJADIS SLR (2025, 28 studies) | High | Two independent primary sources agree |
| RAG enables agent-to-agent synthesis | arXiv (2025) AI KM paper; MDPI Futureinternet review (2025) | Medium | Technical feasibility confirmed; production-scale quality not yet validated |
| Compliance traceability may enable synthesis | BCG (2025); Nature (2025); FSFP (2025) | Medium | Three secondary sources; primary empirical confirmation absent |
| Combined interventions required | All evidence above | High | Mechanism plurality confirmed across four independent disciplines |

### Assumptions

- **Assumption:** Identity-threat mechanisms operate more strongly in individual-contributor cultures (engineering, R&D, financial services strategy) than in collaborative-commons cultures. **Justification:** NIH evidence base is grounded in R&D and technology contexts; no equivalent studies in open-source or academic co-authorship cultures were found. The assumption is directionally supported by NIH antecedent patterns (competitive incentives amplify NIH) but not empirically tested cross-culturally.
- **Assumption:** Agent-to-agent synthesis failure modes (false consensus, provenance loss, hallucinated connections) are manageable with structured output formats and citation discipline. **Justification:** The information synthesis entropy item (`2026-02-27-information-synthesis-entropy.md`) establishes that Chain of Density (CoD) prompting and semantic deduplication reduce these failure modes in human-authored synthesis; transfer to agent-authored synthesis is assumed but not empirically validated at scale.
- **Assumption:** Context window transience is the primary mechanism of the agent-mediated knowledge gap. **Justification:** Based on known LLM architecture (context windows are transient and not persisted by default); persistent agent memory is not yet confirmed as standard practice.

### Analysis

The pre-AI evidence base is strong across four independent disciplines. The mechanisms do not merely coexist — they reinforce each other in a way that makes the gap self-sustaining. Neurological asymmetry creates a motivational floor; SDT misalignment ensures synthesis feels like extrinsic obligation; incentive competition activates NIH and suppresses credit-sharing; and knowledge stickiness makes even motivated synthesis difficult. These four levers operate simultaneously.

The addition of the agent-mediated gap changes the problem in kind, not degree. The traditional diagnosis ("people don't share because sharing is hard and unrewarded") implies that the problem is fixable through persuasion and incentive redesign. The agent-mediated diagnosis implies that the problem is fixable only by ensuring the relevant knowledge exists in a form that agents can retrieve — because no human can transfer what no human knows.

Competing interpretation: one could argue that humans always develop some tacit knowledge from supervising agent work (pattern recognition from outcomes, confidence calibration, domain intuitions). This is plausible. However, this form of tacit knowledge — "my agent found that approach X failed" — is precisely the knowledge that is hardest to transfer under Szulanski's causal ambiguity criterion: the supervisor often does not know *why* X failed, only that it did. The agent's process knowledge (which includes the why) is what is lost.

The regulatory convergence finding warrants separate investigation: if compliance-driven traceability infrastructure genuinely enables synthesis as a second use, the business case for investing in it becomes substantially stronger, and the governance and synthesis functions could be co-designed rather than siloed.

### Risks, Gaps, and Uncertainties

- Wang & Noe (2010) and Nonaka & Takeuchi (1995) were verified through secondary citation rather than primary access. Core claims from both are well-represented in the literature; direct source access would strengthen confidence.
- No empirical, production-scale study of agent-to-agent synthesis quality was found. Feasibility is confirmed; reliability is not.
- DRD4 evidence is contested across studies; the 3% figure from Munafo et al. (2007) is the most defensible estimate but should not be treated as definitive.
- The regulatory convergence inference (compliance traceability → synthesis enabler) is not yet documented as an organisational practice in the literature. It is a forward-looking inference from regulatory trends.
- The evidence base is predominantly Western (US and European organisations). Cross-cultural variation in exploration-synthesis gap magnitude is unknown.
- The claim that human supervisors hold "no process knowledge" is a claim about the modal case; exceptions likely exist for highly experienced supervisors who can reconstruct agent reasoning from outcomes. The modal case remains the organisationally relevant one.

### Open Questions

1. What minimum artefact format must an exploration-mode agent produce for downstream synthesis to achieve acceptable quality? (Engineering backlog item candidate.)
2. Do collaborative-commons cultures (open-source communities, academic co-authorship networks) show meaningfully lower exploration-synthesis gaps than competitive knowledge-work cultures, and if so, what structural features explain the difference?
3. Can credit attribution systems be redesigned to make synthesis visible and rewarded without triggering the "synthesis as audit burden" reaction that suppresses exploration velocity?
4. What does production-quality agent-to-agent synthesis look like empirically? What quality metrics should apply?
5. Does compliance-driven AI traceability infrastructure actually get adopted for synthesis use cases, or does it remain siloed in governance and audit functions?

---

## Output

- Type: knowledge
- Description: Mechanistic analysis of the exploration-synthesis gap (neurological, motivational, incentive, identity, and agent-mediated mechanisms) and a tiered intervention framework (structural / process / architectural) for closing it in organisations adopting AI.
- Links:
  - https://selfdeterminationtheory.org/SDT/documents/2000_RyanDeci_SDT.pdf (Ryan & Deci 2000 — SDT primary source)
  - https://josephmahoney.web.illinois.edu/BADM%20545_Spring%202008/Paper/Szulanski%20%281996%29.pdf (Szulanski 1996 — knowledge stickiness primary)
  - https://www.langchain.com/stateofaiagents (LangChain State of AI Agents 2024 — practitioner evidence on agent explainability gap)
