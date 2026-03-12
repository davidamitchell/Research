---
title: "AI amplified the coordination tax: the 5-person strike team as the structural unit of the AI era"
added: 2026-03-12
status: backlog
priority: high
blocks: []
tags: [team-size, ai, coordination-overhead, strike-team, organisational-design, productivity, ai-native]
started: ~
completed: ~
output: [knowledge]
---

# AI amplified the coordination tax: the 5-person strike team as the structural unit of the AI era

## Research Question

AI has increased per-person output by 5–10x. If coordination cost scales with the square of team size
(see `2026-03-12-team-size-limits-brooks-dunbar-network-theory.md`), what is the correct structural
unit for an AI-augmented organisation, and how does the increased per-person output change the
economics of every additional hire?

Specifically: does the evidence support the thesis that the penalty for exceeding a 5-person team
has risen by the same order of magnitude as per-person productivity — and what does that imply for
how organisations should be designed today?

## Scope

**In scope:**
- The mathematical relationship between per-person output and the coordination cost of each additional person
- Revenue-per-employee data for AI-native companies vs traditional SaaS benchmarks
- The "scout" (solo) and "strike team" (5-person) archetypes and when each is correct
- How AI changes the consequences of wrong team size without changing the underlying cognitive limits
- The argument that meetings are a symptom of wrong team size, not a root cause in themselves

**Out of scope:**
- Detailed analysis of why the cognitive limit is 5 (covered in `2026-03-12-team-size-limits-brooks-dunbar-network-theory.md`)
- The ambition-expansion strategic response (covered in `2026-03-12-ai-force-multiplier-ambition-expansion.md`)
- The volume-vs-correctness quality inversion (covered in `2026-03-12-volume-vs-correctness-ai-era.md`)

**Constraints:** Focus on the economic/structural argument, not the underlying neuroscience or software
engineering history.

## Context

The speaker argues that AI note-taking apps and AI-assisted meetings are attacking the wrong problem.
Meetings multiply not because of meeting culture but because teams are structurally too large. The
underlying cause is that AI increased output per person without decreasing coordination overhead per person.

Before AI: a 5-person team produced X output. Adding a 6th person gave more capacity with diminishing
returns — coordination overhead grew faster than output, but the tax was manageable when each person
produced ~$250K/year in enterprise value.

After AI: the same 5-person team produces 5–10x more. At $2–3M per person per year, the coordination
cost of a 6th person is no longer a minor tax — it is, in the speaker's framing, a catastrophe. The
penalty for over-staffing has risen by the same order of magnitude as individual productivity.

This is the main thesis connecting the other items in this set. The three supporting pillars are:
1. The science of why 5 is the right number (Brooks, Dunbar, network math)
2. Why correctness is now more valuable than volume (the quality inversion)
3. Why the correct response is ambition expansion, not headcount reduction

Primary source: https://youtu.be/hnwM01CpzmA?si=UIeEUIVJ4yZUzDNI
Additional context: https://github.com/davidamitchell/Latest-developments-/blob/main/history/2026-03-09.txt

## Approach

1. Validate the claim that AI-native companies run 5–10x the revenue-per-employee of traditional SaaS:
   look up Lovable, Midjourney, ElevenLabs, Anthropic, OpenAI employee counts vs ARR
2. Examine the mathematical relationship: if coordination cost = n(n-1)/2 pathways and each pathway
   has a cost proportional to per-person output, what happens to total coordination cost when output
   multiplies 5x?
3. Evaluate the scout / strike team archetypes: is there evidence that solo and 5-person teams
   outperform larger teams on correctness-sensitive tasks in an AI-augmented setting?
4. Assess the specific claim that Shopify's Toby Lütke identified "10x loss of productivity with each
   addition beyond five" — find and evaluate the primary source
5. Review the Peter Steinberger / Open Claw case study as an existence proof of the scout model

## Sources

- [ ] **Video transcript** — https://youtu.be/hnwM01CpzmA?si=UIeEUIVJ4yZUzDNI (primary source)
- [ ] **Latest developments context** — https://github.com/davidamitchell/Latest-developments-/blob/main/history/2026-03-09.txt
- [ ] **Lovable ARR/employee data** — public reporting on Lovable (fka GPT Engineer) growth metrics
- [ ] **Midjourney headcount vs revenue** — public reporting (c. 2023–2025)
- [ ] **ElevenLabs headcount vs ARR** — public reporting
- [ ] **Shopify Toby Lütke productivity claim** — original memo or interview (spring 2025)
- [ ] **Brooks, F.P. (1975).** *The Mythical Man-Month.* Addison-Wesley. (coordination overhead claim)
- [ ] **Wes McKinney on the "agentic tarpit"** — original source/article
- [ ] **Related item:** `Research/backlog/2026-03-12-team-size-limits-brooks-dunbar-network-theory.md`
- [ ] **Related item:** `Research/backlog/2026-03-12-volume-vs-correctness-ai-era.md`
- [ ] **Related item:** `Research/backlog/2026-03-12-ai-force-multiplier-ambition-expansion.md`
