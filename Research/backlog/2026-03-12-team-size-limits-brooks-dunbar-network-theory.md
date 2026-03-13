---
title: "Three disciplines, one answer: Brooks, Dunbar, and network theory on why 5 is the coordination limit"
added: 2026-03-12
status: backlog
priority: high
blocks: []
tags: [brooks-law, dunbar-number, network-theory, team-size, coordination-overhead, graph-theory, evolutionary-psychology, software-engineering, military]
started: ~
completed: ~
output: [knowledge]
---

# Three disciplines, one answer: Brooks, Dunbar, and network theory on why 5 is the coordination limit

## Research Question

Software engineering (Fred Brooks, 1975), evolutionary psychology (Robin Dunbar, 1992), and graph
theory each independently arrive at the same structural limit: approximately 5 people for a
high-coordination working unit. What is the mechanistic explanation from each discipline, how
well does the empirical evidence hold up, and what does the convergence tell us about the
deep nature of the constraint?

Is this limit cognitive (neocortex capacity), mathematical (exponential edge growth), or social
(trust formation dynamics) — or are these three descriptions of the same underlying phenomenon?

## Scope

**In scope:**
- Brooks' Law: the original formulation and the communication-path mathematics behind it
- Dunbar's hierarchy of social group sizes (5, 15, 50, 150) and the neocortex size argument
- The n(n-1)/2 formula for undirected communication pathways in a team of n people
- Military empirical confirmation: US Army fire team (4+1), squad, platoon, company structure
- Bezos' two-pizza rule as an independent practitioner convergence
- How each discipline frames the root cause: cognitive limit vs coordination overhead vs trust bandwidth
- Whether the three framings reduce to a single underlying mechanism

**Out of scope:**
- What AI changes about these limits (covered in `2026-03-12-ai-team-size-strike-team-thesis.md`)
- Organisational responses and ambition expansion (covered in `2026-03-12-ai-force-multiplier-ambition-expansion.md`)
- Quality vs throughput (covered in `2026-03-12-volume-vs-correctness-ai-era.md`)

**Constraints:** Privilege primary sources (Brooks 1975, Dunbar 1992, military field manuals) over
secondary commentary. Be precise about what each source actually claims vs what the speaker attributes
to them.

## Context

The speaker cites three independent convergences on the 5-person coordination limit:

**Network mathematics**: Communication pathways between n people = n(n-1)/2. At 5 people: 10 pathways
(manageable — each person holds the full map in their head). At 10: 45. At 20: 190. The combinatorial
explosion makes shared context impossible above ~5 without hierarchical structure.

**Dunbar (1992)**: Robin Dunbar's research on primate neocortex size established layered cognitive
limits on relationship complexity: ~5 for a core trust group, ~15 for deep trust, ~50 for meaningful
working relationships, ~150 for stable social connections (Dunbar's Number). The mechanism is
cognitive: the human neocortex can only maintain a limited number of active social relationships
at the depth required for high-context coordination.

**Brooks (1975)**: In *The Mythical Man-Month*, Fred Brooks observed that adding engineers to a late
software project makes it later. The underlying mechanism is that every new person adds (n-1)
new communication channels that must be maintained, and the training/onboarding cost of the new
person consumes existing team capacity before they can contribute. The coordination overhead
overwhelms the added capacity.

**Military confirmation**: US Army field structure empirically validates the same hierarchy. A fire
team is 4 soldiers plus a team leader (5 total). Squads, platoons, and companies scale up in layers
that track Dunbar's 15/50/150 levels almost exactly. The military's validation is significant because
their stakes are high enough to test empirically and iteratively over centuries.

The convergence across evolutionary psychology, software engineering, and military science suggests
the limit is not cultural or domain-specific but structural — a property of human cognitive
architecture meeting combinatorial mathematics.

Primary source: https://youtu.be/hnwM01CpzmA?si=UIeEUIVJ4yZUzDNI
Additional context: https://github.com/davidamitchell/Latest-developments-/blob/main/history/2026-03-09.txt

## Approach

1. Read and summarise Brooks' original argument in *The Mythical Man-Month* chapters on team size;
   verify the precise claim attributed to him and check whether subsequent empirical studies confirmed it
2. Read Dunbar's 1992 paper ("Neocortex size as a constraint on group size in primates"); verify the
   5/15/50/150 numbers and the neocortex mechanism; check how well the claim has held up in subsequent
   cognitive science
3. Work through the n(n-1)/2 formula: build a small table (n=2 through n=20) to make the combinatorial
   explosion concrete; identify the inflection points
4. Verify the US Army fire team structure claim and trace the structural layers (fire team → squad →
   platoon → company); check whether the rationale given in military doctrine matches Dunbar's framing
5. Investigate whether Bezos formally cited Dunbar or independently arrived at the two-pizza rule
6. Synthesise: are the three constraints (cognitive, social, mathematical) the same phenomenon or
   independently operating limits that happen to converge near 5?

## Sources

- [ ] **Video transcript** — https://youtu.be/hnwM01CpzmA?si=UIeEUIVJ4yZUzDNI (primary source)
- [ ] **Latest developments context** — https://github.com/davidamitchell/Latest-developments-/blob/main/history/2026-03-09.txt
- [ ] **Brooks, F.P. (1975).** *The Mythical Man-Month: Essays on Software Engineering.* Addison-Wesley. (original Brooks' Law)
- [ ] **Dunbar, R.I.M. (1992).** "Neocortex size as a constraint on group size in primates." *Journal of Human Evolution*, 22(6), 469–493.
- [ ] **Dunbar, R.I.M. (1993).** "Coevolution of neocortical size, group size and language in humans." *Behavioral and Brain Sciences*, 16(4), 681–694.
- [ ] **US Army Field Manual FM 3-21.8** — Infantry Rifle Platoon and Squad (for fire team structure)
- [ ] **Gladwell, M. (2000).** *The Tipping Point* — chapter on Dunbar's Number and the 150-person rule [secondary source]
- [ ] **Related item:** `Research/backlog/2026-03-12-ai-team-size-strike-team-thesis.md`
- [ ] **Related item:** `Research/backlog/2026-03-12-volume-vs-correctness-ai-era.md`
- [ ] **Related item:** `Research/backlog/2026-03-12-ai-force-multiplier-ambition-expansion.md`
