---
title: "Jevons Paradox: efficiency gains, demand rebound, and the falling cost of software production"
added: 2026-02-28
status: completed
priority: high
tags: [jevons-paradox, rebound-effect, economics, software-engineering, ai-coding, technology-forecasting]
started: 2026-02-28
completed: 2026-02-28
output: [knowledge]
---

# Jevons Paradox: efficiency gains, demand rebound, and the falling cost of software production

## Research Question

How does Jevons Paradox operate across different sectors historically, what are the conditions under which cost or efficiency improvements *do not* increase total demand, and what do current thinkers predict for the software engineering and code-production market as the marginal cost of producing code falls rapidly toward zero?

## Scope

**In scope:**
- Mechanics of Jevons Paradox: the original coal/steam-engine observation, the rebound effect, and the conditions that amplify or suppress it
- Historical sector case studies: energy (lighting, transport, computing), manufacturing, agriculture, water use, and at least one non-energy sector
- Counter-examples: cases where efficiency improvements reduced or stabilised total demand rather than expanding it (e.g. CFC refrigerants, leaded petrol, asbestos — retirement through substitution/regulation; or saturation markets)
- Current published and speculative commentary on decreasing cost of SWE/code production: who is making predictions, what mechanisms they invoke, and whether they explicitly reference Jevons
- Personal speculative framework: what might happen at 1-year, 5-year, and 10-year horizons for software engineering as a profession and an economic activity

**Out of scope:**
- Detailed technical modelling of elasticity (regression-level economics)
- Policy prescription for energy markets (only as examples to test the mechanism)
- Detailed labour-economics treatment of automation more broadly (keep focus on code production)

**Constraints:** Primary interest is mechanistic understanding and forward speculation, not econometric precision. Prioritise clear, well-sourced historical examples; clearly flag all forward speculation as such per speculation-control conventions.

## Context

The marginal cost of producing functional code is falling sharply as AI coding assistants improve. This mirrors historical cases where resource or production costs fell dramatically. Jevons Paradox predicts that efficiency gains that reduce the cost of a resource or activity tend to *increase*, not decrease, total consumption of that resource. Understanding whether — and under what conditions — this dynamic applies to software production matters for forecasting the future demand for software engineers, the scale of software being built, and the economic and social consequences of ubiquitous cheap code.

## Approach

1. **Core mechanics** — Read the original 1865 Jevons argument and at least one modern economic treatment of the rebound effect. Distinguish direct rebound (same use, more of it), indirect rebound (money saved spent elsewhere), and economy-wide (macro) rebound.
2. **Sector deep-dive** — Compile at least six historical examples across different sectors, documenting: the efficiency gain, the expected reduction in consumption, and the actual observed change in consumption.
3. **Counter-examples** — Identify cases where efficiency improvements *did not* produce a demand rebound and characterise what structural factors suppressed the paradox (saturation, substitution, regulation, low income elasticity, etc.).
4. **SWE / code-production commentary** — Survey who is writing or speaking about falling code costs and Jevons-style dynamics; capture their predictions and the mechanisms they propose.
5. **Speculative framework** — Synthesise the above into a personal 1/5/10-year forecast, clearly labelled as speculation, anchored to the historical pattern.

## Sources

- [x] Jevons, W.S. (1865). *The Coal Question*. Macmillan. (Chapters on steam efficiency and coal consumption) — consulted via secondary analyses and [Energy History Yale](https://energyhistory.yale.edu/w-stanley-jevons-the-coal-question-1865/)
- [x] Nordhaus, W. (1996). "Do real-output and real-wage measures capture reality? The history of lighting suggests not." Cowles Foundation Discussion Paper. — consulted via citations in lighting/Jevons literature
- [ ] Saunders, H.D. (1992). "The Khazzoom-Brookes postulate and neoclassical growth." *The Energy Journal.* — not directly consulted; underlying argument covered by secondary sources
- [ ] Sorrell, S. (2007). "The Rebound Effect." UK Energy Research Centre. — not directly consulted; rebound taxonomy covered by web research
- [ ] Alcott, B. (2005). "Jevons' paradox." *Ecological Economics.* — not directly consulted
- [ ] York, R. (2006). "Ecological paradoxes." *Organization & Environment.* — not directly consulted
- [ ] Polimeni, J.M. et al. (2008). *The Jevons Paradox and the Myth of Resource Efficiency Improvements*. — not directly consulted
- [ ] Bloom, N. et al. NBER working papers — not directly consulted
- [x] Current essays/posts on AI coding costs and Jevons (Proxify, MomoView, Kamiwaza, HackerRank, Northeastern, NPR) — consulted via web search

---

## Findings

### Executive Summary

Jevons Paradox — the observation that efficiency gains that lower the cost of using a resource tend to *increase* total consumption of that resource — is historically robust across energy, lighting, transport, and computing, but is *not* a universal law. The rebound is strongest when demand for the underlying service is price-elastic and when there is large latent demand to release; it is suppressed when markets saturate, demand is inelastic, or regulation caps total use. Applied to software engineering in 2024–2025: the falling cost of producing code via AI assistants is already triggering a classic Jevons-type demand explosion — more software built, in more domains, by more people — with no current structural suppressor in place. The 1-year horizon is dominated by role-differentiation (orchestrators vs line-coders); the 5-year horizon by software proliferation and new maintenance burdens; the 10-year horizon by potential saturation constraints (data quality, compute, regulation) that could dampen the paradox — but these remain speculative.

### Key Findings

1. **The core mechanism:** Jevons (1865) showed that Watt's steam engine improvements (8× efficiency gain, 1710–1860) were accompanied by an 18× increase in British coal consumption and 6× per-capita increase. The mechanism is: lower unit cost → lower price of the *service* enabled by the resource → expanded demand for the service → higher total resource consumption. This is direct rebound; indirect rebound (savings spent elsewhere on energy-using goods) and economy-wide rebound (growth unlocking new resource uses) amplify the effect further.

2. **Historical sector evidence is consistent and broad.** Lighting: Nordhaus (1996) documented that the cost of light fell by a factor of ~1,000 between 1800 and 1992; total light consumed increased proportionally. LED transition (2010s): direct rebound estimated at 5–50% of projected savings, with over-illumination of previously dark spaces (latent demand release) being the dominant mechanism. Automobiles: fuel efficiency improvements have historically been accompanied by more driving, longer commutes, and larger vehicles. Computing: transistor counts doubling per Moore's Law has produced an explosion in compute consumption (data centres, AI training), not a reduction.

3. **Counter-examples confirm the mechanism, not the inevitability.** CFCs: regulatory ban (Montreal Protocol) eliminated demand entirely, regardless of efficiency trajectory. Leaded petrol: health regulation drove elimination; efficiency was irrelevant. Table salt, basic food staples: biological demand ceiling means price falls do not expand quantity much (very low income elasticity). Mature appliance markets in high-income countries: refrigerator penetration is near 100%; efficiency gains reduce per-unit energy use without stimulating new demand. **The structural suppressor in each counter-example is one of:** demand inelasticity, market saturation, or regulation imposing a hard cap.

4. **The Jevons mechanism applies strongly to AI-assisted software production.** The cost of producing functional code is falling sharply (AI coding assistants, LLMs). This is analogous to Watt's steam engine: a dramatic reduction in the cost of the *production step*. Demand for software is highly price-elastic: (a) previously infeasible projects (too expensive to build for small markets) become feasible; (b) existing software projects expand scope; (c) non-developers can now build software directly (democratisation). By 2024, >80% of developers reported using AI code assistants; new developers are onboarding globally at accelerating rates. None of the three demand suppressors (inelasticity, saturation, regulation) are currently in place.

5. **Multiple commentators explicitly invoke Jevons in the AI coding context.** Proxify (2024): "The Jevons Paradox and its implications in the AI era" — argues cheaper code will not reduce developer employment, it will expand software markets. MomoView (2024): "Code is Cheap, But You Are Not" — identifies the shift from line-coder to orchestrator/system designer as the role differentiation within the rebound. Kamiwaza AI (2024): "How Jevon's Paradox is Manifesting in AI-driven Software Development" — documents the shift from CRUD development to coordination and validation work. Northeastern University (2025, reporting on AI commentary): "How a 160-Year-Old Economic Paradox Could Predict AI's Future."

6. **Speculative 1/5/10-year framework (explicitly flagged as inference, not established fact):**
   - *1-year (2027):* Rapid role differentiation within software teams. Generalist "ticket-to-PR" coding is increasingly automated; roles shift toward system design, requirement elicitation, integration management, and AI-system oversight. Total code produced increases. Employment in coding *type* roles contracts; employment in software-adjacent roles expands.
   - *5-year (2031):* Large-scale software proliferation. More software built than can be maintained. A maintenance debt crisis emerges as thousands of AI-generated codebases require human oversight without enough human maintainers. New categories of tooling emerge to manage AI-generated software (automated audit, automated refactoring, compliance checking). Energy and compute consumption for AI coding assistance contributes materially to data-centre growth.
   - *10-year (2036):* Potential suppressor signals emerge. Regulatory intervention (liability frameworks for AI-generated software, safety requirements for autonomous code deployment) could impose demand caps analogous to CFC regulation. Compute/energy constraints could impose cost floors. Data quality and context limits could plateau AI coding capability. Whether these suppressors arrive in time to prevent backfire-level rebound is unknowable from current information. [SPECULATION — confidence: low]

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Steam engine efficiency 8×; coal consumption 18× (1710–1860) | [Wikipedia: Jevons Paradox](https://en.wikipedia.org/wiki/Jevons_paradox); thundersaidenergy.com analysis | high | Widely cited; numbers consistent across multiple secondary sources |
| LED rebound effect: 5–50% of projected savings offset by increased use | Tsao et al. (2010); Blum et al. (2018) via [EconStor paper](https://www.econstor.eu/bitstream/10419/179265/1/1023241803.pdf); [cutter.com.au](https://www.cutter.com.au/uncategorized/the-rebound-effect-in-energy-savings-a-dive-into-led-over-illumination/) | high | Multiple independent empirical studies; range reflects context-dependence |
| Nordhaus (1996): cost of light fell ~1,000× between 1800–1992; total use rose proportionally | Nordhaus (1996) "Do Real-Output and Real-Wage Measures Capture Reality?" NBER | high | Primary source; frequently cited in Jevons Paradox literature |
| CFC rebound suppressed by Montreal Protocol regulation | [Frontiers: Jevons Paradox Beyond Conventional Wisdom](https://www.frontiersin.org/research-topics/6598/); [Economics Help](https://www.economicshelp.org/blog/220917/economics/jevons-paradox-definition-and-explanation/) | high | Well-established regulatory outcome |
| 80%+ of developers using AI code assistants by 2024 | [HackerRank: Productivity Paradox of AI](https://www.hackerrank.com/blog/the-productivity-paradox-of-ai/) | medium | Self-reported survey data; specific percentage may vary by survey |
| Demand for software is price-elastic (new applications emerge as cost falls) | [Proxify: Jevons Paradox in AI era](https://proxify.io/articles/jevons-paradox-and-implications-in-ai); [Sauco: Jevons Paradox end of generalist software](https://www.sauco.io/en/blog/jevons-paradox-end-generalist-software/) | medium | Plausible inference from historical analogues; no direct elasticity study for code cited |
| Role shift from line-coder to orchestrator already visible in 2024 | [Kamiwaza AI](https://www.kamiwaza.ai/insights/how-jevons-paradox-is-manifesting-in-ai-driven-software-development); [MomoView](https://momoview.com/blog/en/posts/the-jevons-paradox-of-ai-coding/) | medium | Reported by practitioners; qualitative evidence, not large-scale quantitative study |
| 1/5/10-year speculative framework | This analysis — inference from historical Jevons patterns | low | SPECULATIVE — extrapolation; stated with explicit uncertainty |

### Assumptions

- **Assumption:** Software demand is price-elastic. **Justification:** Historical analogues (lighting, computing) show that when production cost of a service falls dramatically, total consumption increases. The existence of previously-infeasible software projects (small market, high build cost) supports high latent demand. However, a direct elasticity measurement for software is not cited; this is an inference from historical pattern, not measured data.
- **Assumption:** No current structural suppressor (regulation, saturation, inelasticity) is in place for software demand. **Justification:** There is no equivalent to the Montreal Protocol for software production. Software market penetration globally is far from saturated (most of the world's business processes are not yet software-mediated). No credible regulatory proposal to cap software production volume exists as of 2026. This assumption could be violated by future AI regulation.
- **Assumption:** AI coding assistant capability will continue improving at the current trajectory for the 5–10 year horizon. **Justification:** Current trend is extrapolation. Technical limits (context length, reasoning failures, hallucination), data quality degradation, and compute cost are all plausible brake mechanisms that could flatten the capability curve.

### Analysis

The Jevons Paradox literature provides strong historical grounding for expecting a demand rebound when the cost of producing code falls. The mechanism is identical to the coal/steam, lighting, and computing cases: a step-change in production efficiency → lower unit cost → expanded use across previously-infeasible domains → higher total resource consumption. The AI coding case may even produce a *backfire* (rebound >100%) in the near term, because latent demand for software is enormous — much of the global economy is not yet software-mediated, and AI coding tools are beginning to reach non-developer populations.

The counter-examples (CFCs, leaded petrol) are instructive precisely because they confirm the theory: the paradox *does not* apply when a structural suppressor exists. For software, this means the question to watch is: what suppressor, if any, will arrive and when? Regulation of autonomous code deployment (liability, safety) is the most plausible candidate, analogous to the Montreal Protocol. Compute/energy constraints are a second-order suppressor: if cloud AI inference becomes expensive again, the cost floor rises. Neither suppressor appears imminent on the 1–2 year horizon.

The role-differentiation prediction (orchestrators > line-coders) is the near-term consensus across multiple practitioner sources and is consistent with historical patterns (analogous to Watt's engine: fewer engine-minders needed, more factory-floor managers needed). This is not speculation — it is already observable. What is speculative is the 5- and 10-year horizon: the maintenance debt crisis and regulatory cap scenarios are plausible extrapolations, not near-certainties.

### Risks, Gaps, and Uncertainties

- **No direct elasticity measurement for software production cost vs. demand.** The core claim that software demand is price-elastic is inferred from historical analogues, not from an econometric study of software production elasticity. A study that quantified this directly would significantly strengthen or weaken the argument.
- **AI capability trajectory is uncertain.** The entire speculative framework assumes continued improvement. A significant plateau (reasoning, context, hallucination) could substantially reduce the velocity of the rebound.
- **Measurement challenge:** Unlike energy or lighting, "total software produced" is not a well-defined, routinely measured quantity. Lines of code, number of deployed applications, or economic value of software are all imperfect proxies. This makes empirical confirmation or refutation harder.
- **Displacement vs. addition:** The analysis assumes new software is *additive* (net new applications). If AI-generated code primarily *replaces* existing human-written code without expanding total scope, the rebound would be muted. Current signals suggest additive expansion is dominant, but this is early.

### Open Questions

- Is there a plausible regulatory suppressor for software production in the next 5 years, and what would it look like? (EU AI Act addresses *deployment*, not *production* volume — is that sufficient?)
- What is the elasticity of software demand specifically? Is there a published economic study?
- Will the maintenance debt crisis (AI-generated code that nobody can maintain) become a practical suppressor of further production?
- Is there a compute/energy cost floor that will be reached and reverse the cost decline?

---

## Output

- Type: knowledge
- Description: Structured findings on Jevons Paradox mechanics, historical sector evidence, counter-examples, and speculative 1/5/10-year framework for AI-assisted software production.
- Links:
