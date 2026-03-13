---
title: "AI inverted the knowledge-work scarcity equation: volume is free, correctness is the scarce resource"
added: 2026-03-12
status: backlog
priority: high
blocks: []
tags: [correctness, quality, throughput, volume, ai, productivity, verification, shared-context, agentic-tarpit, procter-and-gamble-study]
started: ~
completed: ~
output: [knowledge]
---

# AI inverted the knowledge-work scarcity equation: volume is free, correctness is the scarce resource

## Research Question

Before AI, throughput (volume of output) was the binding constraint on knowledge work. AI has
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

1. Locate the HBS / P&G field experiment (2025) and assess: publication status, sample size
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

- [ ] **Video transcript** — https://youtu.be/hnwM01CpzmA?si=UIeEUIVJ4yZUzDNI (primary source)
- [ ] **Latest developments context** — https://github.com/davidamitchell/Latest-developments-/blob/main/history/2026-03-09.txt
- [ ] **Dell'Acqua, F. et al. (2025).** Harvard Business School (HBS) / P&G field experiment — locate full paper via HBS Working Knowledge or Social Science Research Network (SSRN)
- [ ] **Wes McKinney on the "agentic tarpit"** — original article/post (locate primary source)
- [ ] **Shopify "constitution" reference** (Toby Lütke) — original memo or interview defining taste standards in a federated org
- [ ] **Related item:** `Research/backlog/2026-03-12-ai-team-size-strike-team-thesis.md`
- [ ] **Related item:** `Research/backlog/2026-03-12-team-size-limits-brooks-dunbar-network-theory.md`
- [ ] **Related item:** `Research/backlog/2026-03-12-ai-force-multiplier-ambition-expansion.md`
