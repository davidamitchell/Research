# 2026-05-18 — Add backlog items: epistemology-to-agentic dependency chain

**Completed:**

- `Research/backlog/2026-05-18-rq1-1-popper-falsifiability.md` — added from issue; asks how Popper's falsifiability criterion can be mathematically formalised to distinguish mechanistic models from interpolators
- `Research/backlog/2026-05-18-rq1-2-deutsch-hard-to-vary.md` — added from issue; asks for formal criteria measuring internal logical constraints of explanatory mechanisms via Deutsch's hard-to-vary framework
- `Research/backlog/2026-05-18-rq1-3-instrumentalism-failure-modes.md` — added from issue; asks what the operational failure modes of instrumentalism are when applied to complex dynamic systems under distribution shift
- `Research/backlog/2026-05-18-rq2-1-erm-causal-blindness.md` — added from issue; asks how Empirical Risk Minimisation (ERM) guarantees in-distribution accuracy while being blind to causal mechanisms needed for OOD generalisation
- `Research/backlog/2026-05-18-rq2-2-duhem-quine-underdetermination.md` — added from issue; asks how the Duhem-Quine thesis formalises the multiple-interpolation problem and what quantitative metrics identify true mechanism matching
- `Research/backlog/2026-05-18-rq2-3-predictive-model-fragility.md` — added from issue; asks how dynamical systems theory characterises the structural stability difference between mechanistic and purely predictive models under noise
- `Research/backlog/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md` — added from issue; asks for the formal information-theoretic limits preventing observational models from executing interventions or counterfactuals
- `Research/backlog/2026-05-18-rq3-1-llm-statistical-vs-causal.md` — added from issue; asks to what extent LLMs optimise for token distribution rather than constructing internal causal models
- `Research/backlog/2026-05-18-rq3-2-stochastic-parrot-ood.md` — added from issue; asks how the Stochastic Parrot hypothesis manifests when LLMs face OOD logical prompts requiring structural intervention
- `Research/backlog/2026-05-18-rq3-3-cot-counterfactual-limits.md` — added from issue; asks what the empirical limits of Chain-of-Thought (CoT) prompting are when trying to force counterfactual resolution
- `Research/backlog/2026-05-18-rq4-1-agentic-loop-explanatory-reach.md` — added from issue; asks whether an LLM wrapped in an agentic loop introduces true explanatory reach or merely delays failure
- `Research/backlog/2026-05-18-rq4-2-adversarial-error-propagation.md` — added from issue; asks how adversarial inputs propagate error through agentic verification and strategy phases
- `Research/backlog/2026-05-18-rq4-3-ood-generalization-agentic.md` — added from issue; asks for formal OOD generalisation bounds for agentic architectures under non-deterministic tool outputs
- `Research/backlog/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.md` — added from issue; asks how stochastic agentic failure modes differ fundamentally from deterministic coded system failure modes
- `Research/backlog/2026-05-18-rq5-2-flexibility-vs-predictability-auditability.md` — added from issue; asks how the flexibility–predictability tradeoff affects auditability and formal verification of agentic production pipelines
- `Research/backlog/2026-05-18-rq6-1-halting-problem-static-analysis.md` — added from issue; asks how the Halting Problem and Rice's Theorem formalise the absolute boundary of static analysis for coded systems
- `Research/backlog/2026-05-18-rq6-2-state-explosion-chaos-theory.md` — added from issue; asks how state space explosion and deterministic chaos mirror ML model fragility under perturbation
- `Research/backlog/2026-05-18-rq6-3-complexity-horizon-classical-systems.md` — added from issue; asks how the Complexity Horizon of microservice architectures creates opacity equivalent to neural network opacity
- `Research/backlog/2026-05-18-agentic-explainability-vs-traditional.md` — added from issue (extra item 1); asks whether agentic systems are inherently less explainable than equivalently scoped deterministic coded systems
- `Research/backlog/2026-05-18-agentic-production-tradeoffs.md` — added from issue (extra item 2); asks what is concretely lost and gained by inserting agentic systems into production workflows

## Dependency Chain Structure

The 20 items form a directed acyclic graph with two tracks converging:

```
Phase 1 (Foundational Epistemology)
  RQ 1.1 → RQ 1.2 → RQ 1.3 → Phase 2
  RQ 1.1 → RQ 6.1 (Phase 6 parallel track)

Phase 2 (Mathematics of Curve-Fitting vs. Mechanisms)
  RQ 1.3 → RQ 2.1 → RQ 2.2 → RQ 2.4
                   → RQ 2.3 → RQ 2.4
  RQ 2.4 → Phase 3

Phase 3 (Epistemic Gap in LLMs)
  RQ 2.4 → RQ 3.1 → RQ 3.2 → RQ 3.3 → Phase 4

Phase 4 (Agentic Loops)
  RQ 3.3 → RQ 4.1 → RQ 4.2 → RQ 4.3 → RQ 5.1

Phase 6 (Inherent Unpredictability of Coded Systems — parallel track)
  RQ 1.1 → RQ 6.1 → RQ 6.2 → RQ 6.3 → RQ 5.1

Phase 5 (Convergence: Stochastic vs. Non-Stochastic)
  RQ 4.3 + RQ 6.3 → RQ 5.1 → RQ 5.2

Synthesis Items
  RQ 5.1 + RQ 5.2 + RQ 6.3 → agentic-explainability-vs-traditional
  agentic-explainability + RQ 5.2 + RQ 6.3 → agentic-production-tradeoffs
```

## Mini-Retro

1. **Did the process work?** Yes. The issue was clear about the structure of phases and the sequential dependency. Translating the six phases plus two additional items into 20 backlog files with correct `blocks` and `cites` chains was straightforward once the slug naming convention was decided.

2. **What slowed down or went wrong?** Phase 5 (RQ 5.1) depends on both Phase 4 (RQ 4.3) AND Phase 6 (RQ 6.3), creating a convergent dependency. The `blocks` field on RQ 6.3 and RQ 4.3 both point to RQ 5.1, and RQ 5.1's `cites` field references both. This required careful ordering — Phase 6 was set to branch off Phase 1 (RQ 1.1 → RQ 6.1) so it can run in parallel with Phases 2–4 and converge at Phase 5.

3. **What single change would prevent this next time?** A dependency graph diagram in the session notes before writing any files would have made the convergence structure visible earlier and prevented any re-checking.

4. **Is this a pattern?** Research programmes with parallel tracks converging at synthesis points are common. The existing template handles this well via `blocks` and `cites`; the discipline required is to decide the parallel track's entry point explicitly before writing files.

5. **Does any documentation need updating?** No — the template and frontmatter schema handle this use case correctly.

6. **Do the default instructions need updating?** No changes warranted.
