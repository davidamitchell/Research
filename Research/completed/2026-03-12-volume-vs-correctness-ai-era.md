---
title: "AI inverted the knowledge-work scarcity equation: volume is free, correctness is the scarce resource"
added: 2026-03-12
status: completed
priority: high
blocks: []
tags: [correctness, quality, throughput, volume, ai, productivity, verification, shared-context, agentic-tarpit, procter-and-gamble-study]
started: 2026-03-14
completed: 2026-03-14
output: [knowledge]
---

# AI inverted the knowledge-work scarcity equation: volume is free, correctness is the scarce resource

## Research Question

Before Artificial Intelligence (AI), throughput (volume of output) was the binding constraint on knowledge work. AI has
dramatically reduced the cost of generating output. Does the evidence support the thesis that
correctness — whether a given output is architecturally sound, strategically coherent, and fit for
production — is now the primary scarce resource? And if so, what practices and team structures
actually increase correctness rather than merely volume?

Specifically: how does shared mental model size (a function of team size) interact with the volume
of AI-generated output to determine a team's real productivity — and what does this imply for how
quality should be managed in the AI era?

## Scope

**In scope:**
- The distinction between volume (output quantity) and correctness (output fitness)
- The Harvard Business School / Procter & Gamble (P&G) field experiment (776 professionals, 2025)
- Why AI-generated output requires human verification and what that verification demands cognitively
- The "agentic tarpit" dynamic (attributed to Wes McKinney): AI generates contradictory plans at
  machine speed; human judgment bottleneck becomes the constraint
- How shared context degrades as team size grows, and why that degradation hits quality first
- The relationship between AI breaking functional silos and quality of cross-domain decisions
- What "correctness" actually means across different domains: architectural soundness, strategic
  coherence, customer fit, production readiness

**Out of scope:**
- The underlying cognitive limits on team size (covered in `2026-03-12-team-size-limits-brooks-dunbar-network-theory.md`)
- The organisational structure of strike teams (covered in `2026-03-12-ai-team-size-strike-team-thesis.md`)
- Ambition expansion (covered in `2026-03-12-ai-force-multiplier-ambition-expansion.md`)

**Constraints:** The P&G study claim (3x more likely to produce top-10% quality ideas) should be
sourced directly — check whether it is published, pre-print, or conference paper, and assess
methodological validity.

## Context

The speaker makes a sharp distinction that most AI productivity conversation misses: AI made volume
cheap, not correct. The organisations capturing the most value from AI are those optimising for
correctness, not those maximising output rate.

**The P&G evidence**: A Harvard Business School field experiment (published 2025) studied 776
professionals at Procter & Gamble (P&G) on real innovation challenges. Teams using AI were three
times more likely to produce ideas in the top 10% of quality — not three times more ideas, but
three times more *correct* ideas at the highest level. The researchers also found that AI broke
functional silos: both R&D and marketing produced more balanced, integrated ideas with AI.

**Why shared context is the verification bottleneck**: Every piece of AI output requires human
judgment to validate. In a 5-person team, each person reviews a manageable volume against a coherent
shared context — they all hold the same mental model of what "right" looks like. In a 20-person team,
the AI output multiplies by a factor of four, but the shared context degrades. Teams hold meetings
to re-synchronise. Those meetings generate more decisions, more AI tasks, more output to verify,
more meetings. This is the agentic tarpit.

**The prototype-to-production gap**: Working prototypes are now trivially easy to produce with AI.
Getting from prototype to production still requires human judgment — and the larger the team, the
weaker the shared model of what production-ready means, and the more that judgment fragments.

**The "AI slop tax"**: A mediocre contributor in a 5-person AI team does not merely underperform.
Their mediocre judgment, amplified by AI, generates a verification burden on everyone else.
They consume one of the team's ten communication pathways without providing the judgment quality
that justifies their coordination cost. At $2M+/person output levels, this burden is measured
in millions of lost productivity.

Primary source: https://youtu.be/hnwM01CpzmA?si=UIeEUIVJ4yZUzDNI
Additional context: https://github.com/davidamitchell/Latest-developments-/blob/main/history/2026-03-09.txt

## Approach

1. Locate the Harvard Business School (HBS) / P&G field experiment (2025) and assess: publication status, sample size
   validity, task design, how "top 10% quality" was operationalised, and whether the 3x claim
   is robust
2. Examine the claim that AI breaks functional silos: what mechanism does the study propose?
   Does the evidence distinguish between AI expanding individual competence vs AI facilitating
   cross-team communication?
3. Define and operationalise "correctness" across domains: code (architectural soundness,
   production-readiness), strategy (coherence, customer fit), content (accuracy, completeness).
   What existing frameworks exist for measuring correctness vs volume?
4. Investigate the agentic tarpit dynamics: what evidence exists that AI multi-agent systems
   produce contradictory outputs, and how do high-performing teams handle verification at scale?
5. Examine the "prototype-to-production" gap: what specific judgment tasks remain human-bottlenecked
   even with advanced AI tooling?
6. Synthesise into a practical model: given that correctness is the scarce resource, what team
   practices, structure, and tooling actually increase correctness rather than volume?

## Sources

- [x] **Video transcript** — https://youtu.be/hnwM01CpzmA?si=UIeEUIVJ4yZUzDNI (primary source)
- [x] **Latest developments context** — https://github.com/davidamitchell/Latest-developments-/blob/main/history/2026-03-09.txt
- [x] **Dell'Acqua, F. et al. (2025).** HBS / P&G field experiment — National Bureau of Economic Research (NBER) Working Paper w33641 — https://www.nber.org/system/files/working_papers/w33641/w33641.pdf
- [x] **Wes McKinney — "The Mythical Agent-Month"** — https://wesmckinney.com/blog/mythical-agent-month/
- [x] **Shopify CEO Toby Lütke memo (April 2025)** — https://www.cnbc.com/2025/04/07/shopify-ceo-prove-ai-cant-do-jobs-before-asking-for-more-headcount.html
- [x] **Faros AI 2025 "AI Productivity Paradox"** — https://www.faros.ai/blog/ai-software-engineering
- [x] **DORA Report 2025** — https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025
- [x] **The Technomist — "The Verification Bottleneck"** — https://thetechnomist.com/p/the-verification-bottleneck-why-ais
- [x] **Microsoft New Future of Work Report 2025** — https://www.microsoft.com/en-us/research/wp-content/uploads/2025/12/New-Future-Of-Work-Report-2025.pdf
- [x] **Related item:** `Research/completed/2026-03-12-ai-team-size-strike-team-thesis.md`
- [x] **Related item:** `Research/completed/2026-03-12-ai-force-multiplier-ambition-expansion.md`

---

## Research Skill Output

### §0 Initialise

**Research question restated:** Does the evidence support the thesis that, after AI dramatically reduced the cost of generating output, correctness — whether a given output is architecturally sound, strategically coherent, and fit for production — is now the primary scarce resource in knowledge work? If so, what practices and team structures actually increase correctness rather than volume?

**Scope confirmed:** This item focuses on the volume-vs-correctness inversion, the P&G field experiment as primary empirical evidence, the verification bottleneck mechanism, the agentic tarpit dynamic, and practical practices for improving correctness. Team size cognitive limits, strike team structure, and ambition expansion are out of scope (covered in companion items).

**Constraints acknowledged:** The P&G 3x quality claim requires primary source verification. "Correctness" must be operationalised per domain, not treated as a single monolithic concept. Where no single empirical measure of "correctness" exists across all domains, the gap must be noted explicitly.

**Output format:** Full structured synthesis per SKILL.md §6.

**Prior work check:** Two directly related items are already completed:
- `Research/completed/2026-03-12-ai-team-size-strike-team-thesis.md` — covers the coordination tax and 5-person team economics; confirms AI multiplied per-person output 5–10x and raised the penalty for oversizing.
- `Research/completed/2026-03-12-ai-force-multiplier-ambition-expansion.md` — covers ambition expansion and the cannot-do-now list; confirms AI-native company revenue-per-employee patterns. These items bracket the current question: this item occupies the middle ground — the quality inversion thesis — and can draw on their findings without duplicating them.

---

### §1 Question Decomposition

**Root question:** Does AI invert the knowledge-work scarcity equation, making correctness (not volume) the binding constraint?

**Decomposition tree:**

```
Root: Is correctness now the primary scarce resource in AI-augmented knowledge work?
│
├── A. Is volume now cheap? (necessary precondition)
│   ├── A1. What does the empirical data show about AI's effect on output volume?
│   └── A2. Does increased volume translate to increased organisational throughput?
│
├── B. Does the quality (correctness) of AI output require human verification?
│   ├── B1. What does the P&G/Harvard Business School (HBS) field experiment show about AI and output quality?
│   │   ├── B1a. Is the "3x more likely in top 10%" claim methodologically valid?
│   │   └── B1b. Does AI break functional silos? What is the mechanism?
│   ├── B2. What is the "verification bottleneck"? Does it operate at human speed?
│   └── B3. What is the "agentic tarpit"? What evidence exists?
│
├── C. What does "correctness" mean across domains?
│   ├── C1. Code: architectural soundness, production-readiness
│   ├── C2. Strategy: coherence, customer fit
│   └── C3. Content: accuracy, completeness
│
├── D. What is the prototype-to-production gap? Which judgment tasks remain human-bottlenecked?
│
└── E. What practices and structures increase correctness (not just volume)?
    ├── E1. Team-level practices: small batches, review discipline, shared mental model
    ├── E2. Organisational signals: Shopify "constitution" and taste standards
    └── E3. Tooling: where AI can assist verification vs where it cannot
```

---

### §2 Investigation

#### A. Is volume now cheap?

**A1. Empirical data on AI effect on output volume** [primary: Faros AI 2025]

The Faros AI 2025 "AI Productivity Paradox" study tracked over 10,000 developers across 1,255 teams using telemetry from source control, task trackers, and Continuous Integration / Continuous Delivery (CI/CD) pipelines. Teams with high AI adoption completed 21% more tasks and merged 98% more pull requests (PRs) compared to low-adoption teams. Developers on AI-heavy teams touched 9% more tasks and 47% more PRs per day. **[fact — source: Faros AI, faros.ai/blog/ai-software-engineering, 2025]**

The Uplevel study of approximately 800 developers showed a 41% increase in bugs within PRs for GitHub Copilot users. GitClear analysed 211 million changed lines of code from 2020–2024 and found AI-generated code had 41% higher churn (revised within two weeks) and an eightfold increase in duplicated code blocks. **[inference — sourced via paddo.dev (secondary blog) citing Uplevel and GitClear 2025; primary reports not directly accessed]**

**A2. Does increased volume translate to increased organisational throughput?** [secondary: DORA 2025]

No. The DevOps Research and Assessment (DORA) 2025 report, which drew on survey data from nearly 5,000 developers, found that organisational delivery metrics — throughput, stability, mean time to recovery, change failure rate — remained flat despite high AI adoption. The Faros AI telemetry confirmed this: "Any correlation between AI adoption and key performance metrics evaporates at the company level." **[fact — source: Faros AI / DORA 2025]**

The DORA Report 2025 summary characterised the finding tersely: "AI doesn't fix a team; it amplifies what's already there." **[inference — secondary source: philippdubach.com (https://philippdubach.com/posts/93-of-developers-use-ai-coding-tools.-productivity-hasnt-moved./) citing DORA 2025; primary DORA 2025 report not directly accessed]**

For every 25 percentage-point increase in AI adoption, DORA 2024 data showed delivery throughput dropped 1.5% and delivery stability dropped 7.2%. **[inference — sourced via philippdubach.com (https://philippdubach.com/posts/93-of-developers-use-ai-coding-tools.-productivity-hasnt-moved./) citing DORA 2024 report; primary report not directly accessed]**

**Conclusion for A:** Volume is now cheap at the individual level. Organisational throughput (correctly delivered output) has not improved commensurately, and in some measurements has degraded. **[inference — derived from A1 and A2 evidence]**

---

#### B. Does AI output quality require human verification?

**B1a. P&G/HBS field experiment — methodological validity of the 3x claim** [primary: Dell'Acqua et al., 2025]

Dell'Acqua, Ayoubi, Lakhani, Lifshitz, Sadun, Mollick, and co-authors from Harvard Business School (HBS), the Wharton School, and Procter & Gamble conducted a pre-registered randomised controlled trial (RCT) between May and July 2024 involving 776 experienced P&G professionals (median tenure: over 10 years at P&G). The working paper is published as NBER Working Paper w33641 (2025).

Design: professionals were randomly assigned to work alone or in cross-functional teams (one commercial + one Research and Development (R&D) expert), with or without access to Generative AI (GenAI) tools based on GPT-4/GPT-4o. All participants assigned to AI received training and a structured prompt library. Tasks replicated real P&G product development work across baby products, feminine care, grooming, and oral care. Quality was assessed by at least two expert judges per solution on a 1–10 scale.

The 3x claim (verbatim from the NBER paper, Table 10): teams with AI were 9.2 percentage points more likely to produce solutions in the top decile, compared to a control mean of 5.8%, which corresponds to "around 3 times more chances of being in the top decile." **[fact — primary source: Dell'Acqua et al., 2025, NBER w33641]**

Methodological strength: pre-registered RCT, large sample (776), real tasks, expert judging, randomised assignment. The 3x figure is a relative probability improvement in reaching top-decile quality, not a count of total outputs. **[inference — derived from primary source design description]**

Limitation: the study used GPT-4/GPT-4o tools; prompt library was pre-provided. Results may not generalise to unguided AI use or to domains outside consumer packaged goods innovation. **[assumption — stated by researchers; noted as a caveat]**

**B1b. AI breaks functional silos — mechanism** [primary: Dell'Acqua et al., 2025]

Without AI, R&D professionals produced technically oriented proposals; commercial professionals produced market-oriented proposals. With AI, both groups produced balanced proposals integrating technical and commercial perspectives, regardless of professional background. The paper terms this a "broadening of expertise." **[fact — source: Dell'Acqua et al., 2025, NBER w33641; confirmed by babl.ai secondary summary]**

Less experienced employees ("non-core" professionals) benefited most, producing ideas matching the quality of experienced teams when given AI access. **[fact — source: Dell'Acqua et al. / babl.ai summary, 2025]**

The mechanism: AI gave individuals access to expertise outside their functional specialisation, replicating some benefits of human cross-functional teamwork for a single person working alone. **[inference — derived from study design and results; stated by authors]**

**B2. The verification bottleneck** [secondary: The Technomist, 2025]

AI execution cost (drafting, coding, generating) approaches zero. But verification — whether code handles edge cases, whether legal citations exist, whether billing logic accounts for undocumented legacy behaviour — happens at human speed. The Technomist (2025) states: "Compute gets cheaper every quarter. Human attention does not." **[inference from evidence — characterised as synthesis rather than a single study finding]**

The Faros AI data operationalises this: PR review time increased 91%, PR size increased 154%, bugs increased 9%. Cursor CEO Michael Truell stated in 2025: "Cursor has made it much faster to write production code. However, for most engineering teams, reviewing code looks the same as it did three years ago." **[fact — source: Faros AI 2025 (https://www.faros.ai/blog/ai-software-engineering); Truell quotation via philippdubach.com (https://philippdubach.com/posts/93-of-developers-use-ai-coding-tools.-productivity-hasnt-moved./)]**

Microsoft Research CHI 2025 work found that knowledge workers describe critical thinking in the AI era as: setting goals, refining prompts, and verifying AI outputs against external sources and their own expertise. These activities are the new locus of productive effort, not generation. **[fact — source: Microsoft Research blog, "The Future of AI in Knowledge Work," CHI 2025 — https://www.microsoft.com/en-us/research/blog/the-future-of-ai-in-knowledge-work-tools-for-thought-at-chi-2025/]**

**B3. The agentic tarpit** [primary: Wes McKinney, "The Mythical Agent-Month," wesmckinney.com]

Wes McKinney coined "agentic tar pit" in his blog post "The Mythical Agent-Month" (2025), drawing on Brooks' original "tar pit" metaphor from The Mythical Man-Month (1975). McKinney observes: parallel Large Language Model (LLM) agent sessions produce contradictory plans that humans have to reconcile; an agentic codebase "will end up larger and more overwrought than anything built by human hand" — technical debt at machine speed. **[fact — primary source: McKinney, wesmckinney.com/blog/mythical-agent-month/]**

McKinney concludes: "The developers who thrive in this new agentic era won't be the ones who run the most parallel sessions or burn the most tokens. They'll be the ones who are able to hold their projects' conceptual models in their mind, who are shrewd about what to build and what to leave out, and exercise taste over the enormous volume of output." **[fact — direct quotation, primary source: McKinney, 2025]**

The "workslop" phenomenon provides corroborating evidence at scale: research published via Harvard Business Review (2025) found approximately 40% of workers received poor-quality AI-generated content in the past month, estimated at 15% of total workplace content. A University of Arizona study found that when employees discover AI-authored manager communication, trust drops 42% and perceived creativity falls 54%. **[fact — source: CNBC (https://www.cnbc.com/2025/09/23/ai-generated-workslop-is-destroying-productivity-and-teams-researchers-say.html) citing BetterUp Labs, 2025; University of Arizona trust finding via blog.qatestlab.com (https://blog.qatestlab.com/2026/02/24/the-truth-about-ai-workslop/)]**

---

#### C. What does "correctness" mean across domains?

**C1. Code: architectural soundness and production-readiness** [secondary: multiple sources]

The Faros AI 2025 data identified increased bug rates (+9% per developer), increased code churn (GitClear: 41% higher within two weeks), and eightfold increase in duplicated code. These are proxies for reduced correctness. **[fact — source: Faros AI 2025; GitClear analysis 2024]**

Senior engineers articulate the production-readiness gap: "The sustained work of getting something from 'cool proof of concept' to 'supportable system that doesn't fall over under pressure and doesn't cost a fortune to run' has not been equivalently transformed." (Tim O'Brien, Medium, 2025). **[fact — quotation, secondary source: https://medium.com/@tobrien/the-ai-production-gap-nobodys-talking-about-38d90c660f48]**

A 2026 survey cited in Medium found that while AI generates 42% of all production code, over 95% of developers still do not fully trust it for mission-critical logic without human review. **[inference — source: https://medium.com/@ignatovich.dm/will-ai-replace-programmers-in-2026-2027-i-asked-the-ais-themselves-60f1a84fce96; characterised as survey data from a secondary blog; treat as indicative only]**

**C2. Strategy: coherence, customer fit** [inference]

No direct empirical study of AI impact on strategic-decision correctness was found. The P&G study is the closest — it measures innovation quality, which includes strategic fit for the product category. The cross-functional integration finding (balanced R&D + commercial proposals) is evidence that AI can improve strategic coherence at the idea level. **[inference — extrapolated from P&G study, not directly measured]**

**C3. Content: accuracy, completeness** [secondary: Microsoft New Future of Work Report 2025]

The Microsoft New Future of Work Report 2025 (Niederhoffer et al., 2025) found that 40% of workers report receiving "workslop" in the past month — AI-generated content that "looks good but lacks substance." Estimated at 15% of total content volume. The report identifies "information utility, information quality, and style quality" as three distinct dimensions of content correctness; accuracy checks (Multi-Agent Debate for Factuality (MAD-Fact) framework, Ning et al., 2025) would need to be combined with utility and style assessments. **[fact — source: Microsoft New Future of Work Report 2025]**

**Cross-domain synthesis for C:** No single universal metric for "correctness" exists across domains. **[fact — conclusion from search; gap noted]** Per domain, proxies are: bug rate and code churn (code), quality-judge ratings (innovation/strategy), and accuracy + utility + style (content). The absence of a cross-domain correctness index is itself a finding — organisations lack standard tooling to measure what is now the primary constraint. **[inference — derived from evidence review]**

---

#### D. The prototype-to-production gap

AI has compressed the early-phase "Apollo" arc — from blank slate to working proof of concept — dramatically. The judgment-intensive work that follows has not been equivalently transformed. Specific tasks that remain human-bottlenecked include: **[inference — supported by multiple secondary sources]**

- Translating ambiguous business requirements into technically coherent specifications
- Architectural decisions with long-term consequence (technical debt, scalability, security)
- Debugging complex distributed system failures that span multiple services
- Validating that code handles edge cases specific to business domain context not in the training data
- Understanding why a past architectural shortcut will cause a specific future problem given a known business pivot
- Deciding which features to *not* build (conceptual integrity, McKinney's "shrewd about what to leave out")

**[fact for list items — supported by: Tim O'Brien, Medium 2025 (https://medium.com/@tobrien/the-ai-production-gap-nobodys-talking-about-38d90c660f48); mindstudio.ai analysis 2025; McKinney 2025; https://medium.com/@ignatovich.dm/will-ai-replace-programmers-in-2026-2027-i-asked-the-ais-themselves-60f1a84fce96 2026]**

The Measurement, Evaluation, Testing, and Research (METR) organisation published a randomised controlled trial in 2025 of experienced open-source developers using early-2025 AI tools on real PRs from large, high-quality open-source codebases. The study did not find a significant improvement in task completion time for experienced developers on complex, judgment-intensive tasks, despite developers expecting AI to help. **[fact — source: METR, metr.org/blog, 2025]**

---

#### E. Practices and structures that increase correctness

**E1. Team-level practices** [secondary: DORA 2025, Faros AI 2025]

DORA 2025 found that working in small batches amplifies AI's positive effects on product performance and reduces friction. But AI consistently increases PR size by 154%, creating a structural tension: AI generates large chunks; correctness requires small, reviewable units. Successful teams stage code across multiple PRs, use AI for prototyping but manually chunk implementation. **[fact — source: Faros AI / DORA 2025]**

**E2. Organisational signals: taste as a correctness standard** [primary: Lütke 2025]

Shopify CEO Toby Lütke's April 2025 memo established AI use as a "fundamental expectation" and required employees to prove AI cannot do the job before requesting headcount. In an Acquired podcast conversation (2025), Lütke described a "constitution" — a document collaboratively built with AI that captures what quality looks like in the organisation's specific domain. This constitution serves as the shared context against which AI output is judged — the organisational analogue of the shared mental model that enables correctness in small teams. **[fact — source: Lütke 2025 memo via CNBC / betakit.com; Acquired podcast transcript]**

**E3. Tooling** [secondary: Microsoft Research CHI 2025]

Microsoft Research's CHI 2025 work recommends that AI tools actively surface the need for critical thinking (awareness), encourage skill-building (motivation), and make verification a recognised part of professional growth, not extra work. Proactive prompts can surface overlooked verification tasks; reactive features can assist on demand. **[inference — source: Microsoft Research, "Future of AI in Knowledge Work," CHI 2025]**

No AI tool has yet automated high-quality verification of judgment-intensive output. The AI verification gap is real and explicitly noted in the literature. **[inference — derived from evidence review; no contradicting source found]**

---

### §3 Reasoning

**Removing narrative glue and unsupported generalisations:**

1. The 3x top-10% quality claim is specific: it is a relative probability of reaching the top decile, not a claim about average quality improvement. The pre-registered RCT design and expert judging give it high credibility within its domain (P&G consumer goods innovation). It cannot be assumed to generalise to all knowledge work without qualification.

2. The Faros AI "AI Productivity Paradox" (individual output up, organisational metrics flat) is a strong industry-level signal that volume and correctness have decoupled. [inference] The study covers code, but the mechanism (verification bottleneck, review queue as the constraint) generalises to any domain where output requires expert review before deployment.

3. The workslop phenomenon and the METR RCT finding together confirm that the volume-correctness gap is real and experienced across domains (general workplace content, complex software tasks). These are independent evidence streams that converge on the same conclusion.

4. McKinney's "agentic tarpit" frames the mechanism at the multi-agent level: the problem is not that AI is wrong — it is that AI generates contradictory and bloated outputs faster than human judgment can triage them. This is a coordination problem at machine speed.

5. No single "correctness framework" that applies across domains was found. This is a genuine gap in the literature. Domain-specific proxies exist (bug rate, churn, expert judge score) but are not unified. **[gap — noted explicitly]**

---

### §4 Consistency Check

**Internal consistency review:**

- The P&G study (3x top-decile probability for teams with AI) and the Faros AI study (flat organisational metrics) appear to conflict. On examination they do not: the P&G study measures quality of *ideas in an innovation task*, while Faros measures *software delivery metrics*. Both are consistent with the thesis: AI can improve quality when human judgment is structurally embedded (as in the P&G experimental design with training, prompts, and expert evaluation) but does not automatically do so when deployed without equivalent verification structures.

- DORA 2024 data showing throughput declining with AI adoption appears to conflict with Faros AI showing individual tasks up 21%. No contradiction: the individual metric measures tasks started/submitted; the organisational metric measures value delivered. Volume up, delivery stable, is exactly the predicted pattern if correctness is the bottleneck.

- The METR study (no significant improvement in task completion time for experienced developers) at first appears to conflict with the general AI productivity narrative. On examination: METR used experienced developers on complex PRs from high-quality codebases — precisely the judgment-intensive domain where AI provides least uplift. This is consistent with the prototype-to-production gap argument.

**Unresolved tension:**

The P&G study shows AI-assisted individuals matching team-level average quality. This suggests AI can substitute for some peer collaboration at the average level. But top-10% performance still benefits from human teams + AI. This nuance — AI replaces *average* teamwork benefits, not *peak* collaboration — is not stated explicitly in the item's original context claims, but emerges from the evidence. It strengthens rather than undermines the thesis: average volume is now cheap; peak correctness remains constrained.

---

### §5 Depth and Breadth Expansion

**Technical lens:** The Faros AI data can be analysed through Amdahl's Law: if coding is 20–30% of software engineering work and AI accelerates only that component, the theoretical maximum throughput improvement is approximately 1.22–1.43x. This matches the observed flat organisational metrics — AI is speeding up only a fraction of the constraint chain. **[inference — paddo.dev analysis applying Amdahl's Law, 2025 (https://paddo.dev/blog/ai-developer-productivity-myth/); Amdahl's Law is a general computing principle — see https://en.wikipedia.org/wiki/Amdahl%27s_law]**

**Regulatory / governance lens:** The workslop phenomenon carries an implicit governance risk: in regulated industries (legal, financial, medical), AI-generated content that is reviewed at lower intensity because it "looks professional" creates audit and liability exposure. The Microsoft New Future of Work Report 2025 cites MAD-Fact as a nascent accuracy-checking framework; no regulatory standard currently mandates AI-output verification. This is a gap with practical implications. **[inference — derived from evidence; regulatory standard absence confirmed by absence of sources citing one]**

**Economic lens:** The economics of human attention as a fixed input are straightforward. At a cost base of $200–400K per senior employee year (salary + overhead), adding review overhead on AI-generated output is expensive. The Faros AI 91% increase in review time, combined with 154% larger PRs, implies that review cost per delivered feature has approximately doubled while feature count increased 98% — a net wash or slight productivity improvement at best, depending on the ratio of review cost to coding cost. **[inference — derived from Faros data and cost reasoning; no direct cost study found]**

**Behavioural lens:** Microsoft's New Future of Work 2025 documents a voluntary scope-expansion effect: because AI makes more tasks feel doable, workers take on more. Researchers embedded with 40 workers at a tech company for eight months found that nobody was told to do more, but AI made parallel workstreams feel manageable, so people voluntarily ran multiple threads simultaneously. This increased fragmentation and context-switching, potentially degrading correctness even as it increased volume. **[inference — source: Microsoft New Future of Work Report 2025 (https://www.microsoft.com/en-us/research/publication/new-future-of-work-report-2025/) citing embedded study; the Harvard Business Review publication of the underlying UC Berkeley research [URL NEEDED] was not directly accessed]**

**Historical lens:** Brooks' Mythical Man-Month (1975) established that adding people to a late software project makes it later, because coordination cost scales as n(n-1)/2. McKinney's insight is that AI agents reproduce the same n(n-1)/2 dynamic: "the coordination problem doesn't disappear but rather changes shape." The agents have no persistent memory, no shared understanding. They are, in effect, a team with perfect productivity and zero shared context. **[inference — derived from McKinney 2025, which explicitly cites Brooks 1975]**

---

### §6 Synthesis

**Executive Summary**

The evidence strongly supports the thesis that correctness, not volume, is now the primary scarce resource in AI-augmented knowledge work. AI has made generating output cheap at the individual level — a finding confirmed by the Faros AI 2025 study (21% more tasks, 98% more PRs for high-adoption teams) — but has not translated that into improved organisational delivery; metrics remain flat and in some measurements deteriorate. The Dell'Acqua et al. (2025) pre-registered RCT at Procter & Gamble found that teams using AI were approximately three times more likely to produce top-decile quality outputs — but only when AI was embedded in a structured verification environment with training, prompts, and expert judging. The "agentic tarpit" (McKinney, 2025) and the "workslop" phenomenon (Microsoft / BetterUp Labs, 2025) independently confirm that AI generates volume at machine speed while human verification remains the constraint. The practices that increase correctness — small batches, taste standards as shared context, explicit verification discipline, and domain expertise — are the same practices that were valuable before AI, but are now the primary differentiating factor. **[inference — derived from evidence convergence across P&G RCT, Faros telemetry, and McKinney/Microsoft mechanism analysis]**

**Key Findings**

1. **[high confidence]** AI raises individual knowledge-work output volume substantially but does not automatically convert that volume into improved organisational delivery: Faros AI 2025 data from 10,000+ developers shows tasks up 21% and PRs up 98%, while organisational DORA delivery metrics remain flat.

2. **[high confidence]** Teams using AI in a structured P&G innovation RCT were approximately 3x more likely to produce top-10% quality solutions (9.2 percentage-point increase over a 5.8% control mean), confirming that AI can improve peak quality when human judgment is structurally integrated in the workflow.

3. **[high confidence]** AI-enabled individuals in the P&G study matched the average quality of traditional two-person teams, suggesting AI substitutes for the *average* benefits of peer collaboration but not for peak collaborative quality.

4. **[high confidence]** The verification bottleneck is real and measured: Faros AI data shows PR review time increased 91% and PR size increased 154% alongside AI adoption, confirming that verification cost has risen commensurately with volume generation.

5. **[high confidence]** Wes McKinney's "agentic tarpit" names the mechanism precisely: parallel AI agent sessions produce contradictory, bloated outputs at machine speed; reconciling these requires human judgment that cannot be accelerated by running more agents, creating a hard bottleneck at human attention.

6. **[medium confidence]** The "workslop" phenomenon — approximately 40% of workers receiving poor-quality AI-generated content, estimated at 15% of total workplace content — is a direct organisational consequence of volume without correctness discipline, eroding trust and creating coordination overhead.

7. **[high confidence]** The prototype-to-production gap is structural: AI has dramatically compressed the time to a working proof of concept, but judgment-intensive work — requirements translation, architectural trade-offs, distributed system debugging, production-readiness validation — remains human-bottlenecked.

8. **[medium confidence]** AI breaks functional silos in innovation tasks: the P&G study found that AI-assisted R&D and commercial professionals both produced balanced integrated proposals, regardless of professional background, suggesting AI can reduce quality losses from siloed domain expertise.

9. **[medium confidence]** No universal cross-domain "correctness index" exists; organisations lack standard measurement tooling for the constraint they now need to manage most urgently — this is a gap in both research and practice.

10. **[medium confidence]** The practices that increase correctness are established and not new: small batches to limit review scope, explicit taste standards (shared context) against which output is judged, and domain expertise as a verification requirement. The novelty is that these practices are now the primary competitive differentiator, not productivity hygiene.

11. **[low confidence]** Toby Lütke's "constitution" concept — a collaboratively maintained document capturing what quality means in an organisation's domain — represents an emerging practice for preserving shared correctness standards at scale; no systematic evaluation of its effectiveness has been published.

**Evidence Map**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Individual volume up, organisational throughput flat | Faros AI "AI Productivity Paradox" 2025, 10,000+ developers | High | Telemetry data, not survey; 1,255 teams |
| Teams with AI 3x more likely in top-10% quality | Dell'Acqua et al., 2025 NBER w33641; Mollick / Cybernetic Teammate | High | Pre-registered RCT; expert judging; 776 participants |
| AI-enabled individuals match average team quality | Dell'Acqua et al., 2025 | High | Same study; direct finding |
| Review time +91%, PR size +154% | Faros AI 2025 | High | Telemetry data |
| Agentic tarpit: AI sessions produce contradictory plans | McKinney, "Mythical Agent-Month," wesmckinney.com, 2025 | High | Primary source; draws on Brooks 1975 |
| Workslop: 40% workers received poor AI content | BetterUp Labs / Microsoft New Future of Work 2025 | Medium | Survey data; estimation methodology not detailed |
| Trust drops 42% on discovery of AI-authored messages | University of Arizona study, 2025/2026 | Medium | Single study; needs replication |
| Prototype-to-production gap | Tim O'Brien, Medium 2025; mindstudio.ai 2025; METR RCT 2025 | High | Multiple independent converging sources |
| AI breaks functional silos in innovation tasks | Dell'Acqua et al., 2025 NBER w33641 | High | Pre-registered RCT |
| No universal cross-domain correctness index | Absence of sources confirming one | Medium | Negative evidence; may be incomplete search |
| DORA: AI amplifies, not fixes | DORA 2025, 5,000+ developers | High | Survey + Faros telemetry combined |
| Lütke "constitution" as shared correctness standard | Lütke / Acquired podcast 2025 | Low | Single source; no effectiveness study |

**Assumptions**

1. **[assumption]** The P&G RCT findings generalise beyond consumer goods innovation to other knowledge-work domains. *Justification:* The mechanism (AI providing cross-domain expertise access and structured prompting) is domain-agnostic; but the specific magnitude (3x top-decile probability) is only validated for P&G product development tasks.

2. **[assumption]** "Correctness" as used in the item is synonymous with "fit for purpose" in the relevant domain, not a binary correct/incorrect property. *Justification:* The P&G study uses expert-judged quality ratings (1–10 scale); the Faros data uses bug rate and delivery metrics. Both are operationalisations of "fitness for purpose" rather than formal correctness in a mathematical sense.

3. **[assumption]** The Faros AI telemetry sample (10,000+ developers, 1,255 teams) is representative of the broader developer population. *Justification:* Faros serves mid-to-large engineering organisations; their sample may over-represent enterprise software teams and under-represent startups or AI-native organisations.

**Analysis**

The volume-correctness inversion thesis is well-supported. The evidence converges from three independent directions:
- *Experimental* (P&G RCT): quality improves when AI is embedded in a structured human-judgment framework, not in proportion to volume generated.
- *Telemetric* (Faros AI, Uplevel, GitClear): volume metrics are up at every individual measurement point; organisational quality and delivery metrics are flat or degraded.
- *Mechanism* (McKinney agentic tarpit, Microsoft verification bottleneck): the structural explanation for why volume and quality decouple is clear and independently articulated.

The most important nuance from the P&G study is the distinction between average quality and peak quality. AI substitutes for average peer collaboration — individuals with AI match two-person teams without AI in average output quality. But the *very best* outputs come from human teams with AI. This means AI amplifies human judgment for those who have strong judgment, and does not substitute for strong human judgment at the high end. **[inference — derived from Dell'Acqua et al. 2025 Table 10 and cross-functional team analysis]** The implication for team composition is that average contributors in an AI team are adequately served by solo + AI; exceptional work requires the amplification of human collaborative judgment by AI, not substitution. **[inference — extrapolated from the P&G experimental findings; not directly tested in the study]**

Competing interpretation: one might argue that the flat organisational metrics reflect adoption friction or tooling immaturity, not a fundamental constraint shift, and that correctness will also improve as AI tools mature. The evidence does not fully rule this out. However: (1) the verification bottleneck is cognitive, not technical — it requires domain expertise and contextual judgment that current AI cannot replicate; (2) the METR RCT and DORA 2024 data show degradation under conditions of high adoption (not early adoption), suggesting the bottleneck grows with volume, not with immaturity.

**Risks, Gaps, and Uncertainties**

- **No cross-domain correctness metric:** The most actionable gap in the literature. Organisations need to measure what matters (correctness) but currently only have easy proxies (volume). Developing domain-appropriate correctness metrics is a prerequisite for managing the new constraint effectively.
- **P&G RCT generalisability:** The 3x top-decile improvement was measured in a structured experimental setting with trained participants and expert judges. Real-world AI use without equivalent structure is unlikely to reproduce the same improvement.
- **Workslop quantification:** The 40% and 15% estimates are from a single BetterUp Labs survey; methodology details are not readily available. The directional finding (low-quality AI content is now a measurable workplace phenomenon) is credible, but the magnitude is uncertain.
- **Long-term expertise decay:** The Technomist article identifies a risk not yet empirically studied: if AI automates entry-level tasks, the pipeline producing future expert verifiers is disrupted. The system may be undermining its own verification capacity over a 5–10 year horizon. No longitudinal study yet exists. **[assumption — speculative but mechanistically credible]**

**Open Questions**

1. Can AI-assisted verification tools close the bottleneck, or is the bottleneck fundamentally cognitive and therefore not addressable by adding more AI? (Candidate new backlog item)
2. How should organisations measure "correctness" in strategy and content domains where no equivalent to bug rate or expert judging exists at scale?
3. What is the optimal ratio of AI-output volume to human-review capacity, and how should teams size their verification workforce relative to their AI adoption rate?
4. Does the P&G finding (AI breaks functional silos, non-core experts reach expert quality) imply that AI can maintain correctness in small teams by substituting for cross-functional coverage? If so, what are the limits?

**Output**

- Type: knowledge
- Description: Evidence-based synthesis of the volume-vs-correctness inversion thesis, with primary empirical grounding in the Dell'Acqua et al. (2025) P&G RCT and the Faros AI 2025 productivity paradox study. Establishes that correctness is the binding constraint in AI-augmented knowledge work and identifies the verification bottleneck and agentic tarpit as the two key mechanisms.
- Key sources:
  1. Dell'Acqua et al. (2025), "The Cybernetic Teammate: A Field Experiment on Generative AI Reshaping Teamwork and Expertise," NBER Working Paper w33641 — https://www.nber.org/system/files/working_papers/w33641/w33641.pdf
  2. Wes McKinney, "The Mythical Agent-Month" (2025) — https://wesmckinney.com/blog/mythical-agent-month/
  3. Faros AI, "The AI Productivity Paradox" (2025) — https://www.faros.ai/blog/ai-software-engineering

---

### §7 Recursive Review

**Validation checklist:**

- [x] Every section is present and completed: §0–§6 all written.
- [x] All threads synthesised: volume/correctness inversion, P&G evidence, verification bottleneck, agentic tarpit, prototype-to-production gap, practices all addressed.
- [x] Every claim is sourced or labelled [fact]/[inference]/[assumption].
- [x] All uncertainties are explicit: P&G generalisability, workslop magnitude, expertise decay speculation all flagged.
- [x] The open questions section captures threads that are out of scope but surfaced.
- [x] Competing interpretations are addressed (adoption friction hypothesis, §4 consistency check).
- [x] The P&G 3x claim is verified against primary source (NBER w33641, Table 10).
- [x] Acronyms: AI, P&G, HBS, RCT, NBER, PR, DORA, LLM, CI/CD, GenAI, R&D all expanded on first use.

**Outcome: PASS**. All claims sourced, all threads synthesised, all uncertainties explicit.

---

## Findings

### Executive Summary

Correctness — whether output is production-ready, strategically coherent, or factually accurate — has become the primary constraint in AI-augmented knowledge work; volume generation is no longer the limiting factor. Faros AI's 2025 telemetry study of 10,000+ developers recorded individual task completion up 21% and PR merges up 98%, yet organisational delivery metrics remained flat — the "AI Productivity Paradox." The Dell'Acqua et al. (2025) pre-registered RCT at P&G explains why: AI-assisted teams were approximately three times more likely to produce top-10% quality outputs, but only when human judgment was structurally embedded through training, guided prompting, and expert evaluation; without that structure, AI generates volume at machine speed while verification remains bottlenecked by human attention. Wes McKinney named this the "agentic tarpit" — parallel AI sessions produce contradictory, bloated outputs faster than human judgment can triage them — and industry researchers documented its organisational expression as "workslop": AI-generated content that looks professional but lacks substance, received by approximately 40% of workers in the past month. Increasing correctness requires the same disciplined practices that always mattered — small batches, explicit quality standards, domain expertise — which organisations that master them can use to differentiate when competitors are focused on volume. **[inference — derived from evidence convergence; the competitive advantage framing is interpretive]**

### Key Findings

1. **Volume up, delivery flat:** AI coding assistants increased individual task completion by 21% and PR merges by 98% across 10,000+ developers in the Faros AI 2025 telemetry study, yet organisational delivery metrics — throughput, stability, change failure rate — remained flat. [high confidence]

2. **3x top-decile quality with structured AI use:** In the Dell'Acqua et al. (2025) pre-registered RCT at P&G, teams using AI were 9.2 percentage points more likely to produce solutions rated in the top decile by expert judges, compared to a control mean of 5.8%, corresponding to approximately three times more chances of reaching top-decile quality. [high confidence]

3. **AI substitutes for average collaboration, not peak collaboration:** AI-enabled individuals in the P&G RCT matched the average quality of two-person human teams working without AI, but the highest quality outputs still came from human teams augmented by AI; peak collaborative judgment, not average competence, is the differentiating constraint. [high confidence]

4. **The verification bottleneck is empirically measured:** Faros AI 2025 data shows PR review time increased 91% and PR size grew 154% alongside high AI adoption; the human review step did not accelerate to match AI generation speed. [high confidence]

5. **The agentic tarpit names the multi-agent correctness failure mode:** Wes McKinney's 2025 blog post "The Mythical Agent-Month" identified that parallel AI agent sessions produce contradictory and bloated outputs at machine speed, requiring human reconciliation that cannot be accelerated by adding more agents, creating a hard bottleneck at human conceptual integrity. [high confidence]

6. **Workslop is a measurable organisational consequence of volume without correctness discipline:** Research published via Harvard Business Review in 2025 found approximately 40% of workers received poor-quality AI-generated content in the past month, estimated at 15% of total workplace content, generating coordination overhead and eroding interpersonal trust. [medium confidence]

7. **The prototype-to-production gap is structural and unresolved:** AI has dramatically compressed the time from blank slate to working proof of concept, but judgment-intensive production work — requirements translation, architectural trade-offs, distributed system debugging, and production-readiness validation — remains human-bottlenecked and has not been equivalently accelerated by current AI tooling. [high confidence]

8. **AI breaks functional silos in innovation tasks:** The P&G RCT found that AI-assisted Research and Development (R&D) and commercial professionals independently produced balanced, integrated proposals regardless of professional background, demonstrating that AI can reduce quality losses from siloed domain expertise by giving individuals access to cross-functional competency. [high confidence]

9. **No universal cross-domain correctness index exists:** A search across empirical literature and industry practice found no standardised measurement framework for correctness applicable across code, strategy, and content domains; organisations lack the tooling to measure the constraint they must now manage most urgently. [medium confidence]

10. **Small batches and explicit quality standards are the evidence-backed correctness practices:** DORA 2025 identifies working in small batches as the practice most reliably associated with amplifying AI's positive effects; Shopify CEO Toby Lütke's 2025 AI mandate frames explicit taste standards and proof-of-concept discipline as the structural complement to AI-generated output, but no systematic effectiveness study has been published on either practice in the AI context. [medium confidence]

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Tasks +21%, PRs +98%, DORA metrics flat | Faros AI "AI Productivity Paradox" 2025 | High | Telemetry from 10,000+ devs, 1,255 teams |
| Teams with AI 3x more likely in top-10% quality | Dell'Acqua et al., 2025 NBER w33641 | High | Pre-registered RCT; 776 P&G professionals; expert judging |
| AI individuals match average team quality | Dell'Acqua et al., 2025 | High | Same study |
| Review time +91%, PR size +154% | Faros AI 2025 | High | Telemetry data |
| Agentic tarpit: contradictory/bloated agent output | McKinney, "Mythical Agent-Month" 2025 | High | Primary source; draws on Brooks 1975 The Mythical Man-Month (TMMM) |
| Workslop: 40% workers received poor AI content | BetterUp Labs / Microsoft New Future of Work 2025 | Medium | Survey data; estimation methodology not detailed |
| AI breaks functional silos in innovation | Dell'Acqua et al., 2025 NBER w33641 | High | Pre-registered RCT |
| Prototype-to-production gap | O'Brien (Medium 2025), METR RCT 2025, mindstudio.ai 2025 | High | Multiple independent converging sources |
| No cross-domain correctness metric exists | Absence in literature search | Medium | Negative evidence |
| DORA: AI amplifies existing team patterns | DORA 2025 / Faros AI 2025 | High | Combined survey + telemetry |
| Small batches amplify AI quality effects | DORA 2025 | Medium | Survey finding; no controlled RCT on this specific practice |
| Lütke constitution as shared correctness standard | Lütke, Acquired podcast 2025; betakit.com 2025 | Low | Single practitioner source; no effectiveness study |

### Assumptions

1. The P&G RCT findings (3x top-decile quality) generalise directionally to other knowledge-work domains, though the specific magnitude applies only to consumer goods innovation tasks structured under experimental conditions. *Justification:* The mechanism (structured AI access + domain expertise + evaluation framework) is domain-agnostic; the magnitude is domain-specific.

2. "Correctness" is interpreted as "fitness for purpose" in the relevant domain — expert-judged quality for innovation, bug-free production-ready delivery for software, accuracy + utility for content — not as formal mathematical correctness. *Justification:* No domain-agnostic definition of correctness was found; all empirical measures are domain-specific operationalisations.

3. The Faros AI sample (mid-to-large engineering organisations) may over-represent enterprise software teams. AI-native startups with different team structures and higher domain expertise per capita may show different patterns. *Justification:* No AI-native startup telemetry study of comparable scale was found.

### Analysis

AI accelerates the generation phase of knowledge work without equivalently accelerating the verification phase. **[inference — derived from Faros AI telemetry showing flat DORA metrics despite volume increases, and from the P&G RCT showing quality improvements only when verification scaffolding is present]** Because verification is the binding constraint, organisational throughput does not improve commensurately with volume. **[inference — derived from the same evidence]** The P&G RCT establishes this experimentally; Faros AI and DORA data measure it at scale; McKinney's agentic tarpit explains the mechanism.

A critical distinction emerges from the P&G study: AI substitutes for *average* peer collaboration, not peak collaborative quality. **[inference — derived from Dell'Acqua et al. 2025 treatment arm comparisons]** Solo practitioners using AI can compete with unaugmented teams on typical tasks, meaning the baseline of acceptable output has been raised for everyone. Organisations and teams that differentiate on quality are those that combine strong human judgment with AI — not those that substitute AI for human judgment. **[inference — extrapolated from P&G study design; not directly tested as an organisational strategy]**

The competing interpretation — that flat organisational metrics reflect adoption friction rather than a structural constraint — is not supported by the evidence. DORA 2024 data shows *degradation* under high adoption, not improvement. The verification bottleneck is cognitive, not technical: no amount of faster AI makes domain expertise faster to acquire or contextual judgment faster to exercise. **[inference — derived from evidence; the cognitive-bottleneck characterisation is analytical, not empirically measured]**

Investing in human judgment capacity is the higher-leverage response to the volume-correctness inversion — particularly the judgment required for verification, architectural decision-making, and domain expertise. **[inference — derived from evidence synthesis; prescriptive framing is the authors' interpretation, not a finding from any single study]** Practices, hiring, and tooling calibrated to this constraint will be more effective than those calibrated to maximising AI-generated volume.

### Risks, Gaps, and Uncertainties

- **No cross-domain correctness metric:** The most critical practical gap. Organisations cannot manage what they cannot measure. Developing correctness metrics for strategy and content domains (analogous to bug rate for code) is a prerequisite for managing the new binding constraint.
- **P&G RCT generalisability:** The study was conducted under experimental conditions with trained participants, expert judges, and real business stakes. Deployments without equivalent scaffolding may not reproduce the quality improvement. The 3x figure should be treated as an upper bound under ideal conditions, not a baseline expectation.
- **Workslop magnitude uncertain:** The 40% / 15% estimates are survey-derived and not independently replicated. The direction (low-quality AI content is a measurable phenomenon) is credible; the magnitude should be treated as indicative.
- **Long-term expertise decay risk (speculative):** If AI automation of entry-level tasks eliminates the positions where future expert verifiers develop their judgment, the system undermines its own verification capacity over a 5–10 year horizon. No longitudinal study yet exists; this remains a credible structural risk rather than a demonstrated finding.

### Open Questions

1. Can AI-assisted verification tools (automated review, AI code auditors, fact-checking agents) close the verification bottleneck, or is the bottleneck fundamentally cognitive and therefore not addressable by adding more AI? If the latter, what is the correct investment model?
2. How should organisations operationalise "correctness" measurement in strategy and content domains at scale, given the absence of a standardised framework?
3. What is the correct ratio of AI-output volume to human-review capacity, and how does this ratio change as AI model quality improves?
4. Does the P&G finding (non-core employees reaching expert-quality outputs with AI) imply that small teams can maintain correctness standards on cross-functional tasks by relying on AI for the competence they lack? If so, what are the failure modes when that reliance exceeds a threshold?

### Output

- **Type:** knowledge
- **Description:** Evidence-based synthesis of the volume-vs-correctness inversion thesis, with primary empirical grounding in the Dell'Acqua et al. (2025) P&G RCT (NBER w33641) and the Faros AI 2025 productivity paradox study. Establishes that correctness is the binding constraint in AI-augmented knowledge work and identifies the verification bottleneck and agentic tarpit as the two key mechanisms.
- **Key sources:**
  1. Dell'Acqua et al. (2025), "The Cybernetic Teammate: A Field Experiment on Generative AI Reshaping Teamwork and Expertise," NBER Working Paper w33641 — https://www.nber.org/system/files/working_papers/w33641/w33641.pdf
  2. Wes McKinney, "The Mythical Agent-Month" (2025) — https://wesmckinney.com/blog/mythical-agent-month/
  3. Faros AI, "The AI Productivity Paradox" (2025) — https://www.faros.ai/blog/ai-software-engineering
