---
review_count: 2
title: "Are Human Brains Just Prediction Machines? Comparing Predictive Processing and Large Language Model Next-Token Generation"
added: 2026-03-18
status: completed
priority: medium  # low | medium | high
blocks: []
tags: [neuroscience, cognitive-science, llm, predictive-processing, predictive-coding, next-token-prediction, world-models, consciousness, free-energy-principle]
started: 2026-03-22
completed: 2026-03-22
output: [knowledge]
---

# Are Human Brains Just Prediction Machines? Comparing Predictive Processing and Large Language Model Next-Token Generation

## Research Question

What is the fundamental difference between the predictive processing account of human cognition — in which the brain continuously generates and updates a generative model of the world — and Large Language Model (LLM) next-token prediction, and does this difference matter for understanding intelligence, meaning, and consciousness?

Supporting questions:
- What does the Predictive Processing (PP) / Predictive Coding (PC) framework say about how the brain works, and how well is it supported by neuroscience evidence?
- How does LLM next-token generation actually work, and in what specific ways does it differ from the PP account?
- Is "generating a model of the world" meaningfully different from "predicting the next token in a sequence"?
- What role does embodiment, action, and the Free Energy Principle (FEP) play in the PP account that has no analogue in LLMs?
- What do the similarities and differences imply about consciousness, understanding, and the plausibility of general intelligence emerging from next-token prediction?

## Scope

**In scope:**
- The Predictive Processing / Predictive Coding framework (Helmholtz, Friston, Clark, Seth) — the claim that perception and cognition are fundamentally generative model-based prediction
- Karl Friston's Free Energy Principle (FEP) as the unifying mathematical framework for PP
- Andy Clark's "Surfing Uncertainty" / "Being There" framing of PP and embodied cognition
- Anil Seth's work on "controlled hallucination" and the beast machine thesis
- LLM next-token generation mechanics: autoregressive Transformer (AT) architecture, self-supervised pre-training, temperature/sampling, emergent capabilities
- Mechanistic interpretability research bearing on whether LLMs develop internal world models (Nanda et al., Grokking, linear representation probes)
- The "stochastic parrot" critique (Bender et al., 2021) and responses to it
- Philosophical framing: symbol grounding, intentionality, understanding vs. prediction

**Out of scope:**
- Reinforcement learning from human feedback (RLHF) or instruction tuning mechanics (unless directly relevant to the world-model question)
- Detailed implementation of specific LLM architectures beyond what is needed to contrast with PP
- Clinical neurology, pharmacology, or pathological cases unless they illuminate the core question
- The engineering question of "how to build better Artificial Intelligence (AI)" — this is a conceptual/scientific research item

**Constraints:** Publicly accessible sources. Neuroscience and cognitive science literature (Friston, Clark, Seth, Helmholtz). LLM mechanistic interpretability papers (arXiv, 2020–2026). Web search for recent debate and synthesis pieces.

## Context

The issue that seeds this item draws a sharp contrast: LLMs are "random next token generators" while humans "constantly generate models of the world." This intuition maps onto a genuine scientific debate.

The Predictive Processing (PP) framework, developed by Karl Friston and popularised by Andy Clark and Anil Seth, claims that the brain is fundamentally a generative model that predicts sensory inputs and updates itself based on prediction error. Under this view, perception is not passive reception — it is active hypothesis testing. The brain hallucinates a best guess about reality and is corrected by surprise.

LLMs are trained to minimise next-token prediction loss across massive text corpora. They learn statistical regularities in language. A surface reading says: "that's just autocomplete." A more careful reading asks: what representations must a model develop to predict text well at scale? Mechanistic interpretability research has found evidence for linear world-model features in LLMs — structured internal representations of entities, spatial relations, and temporal states (https://proceedings.iclr.cc/paper_files/paper/2024/file/0a6059857ae5c82ea9726ee9282a7145-Paper-Conference.pdf). This is not nothing.

The question is whether these are the same phenomenon at different scales and substrates, superficially similar but fundamentally different, or somewhere between those poles. The answer has implications for how we think about intelligence, meaning, and the plausibility of understanding emerging from prediction.

This item connects to prior work on AI memory (`2026-03-17-ai-memory-systems-rag-neuroscience`) and neurological context management (`2026-03-15-neurological-context-management`), but its core focus is the conceptual and scientific gap between the two prediction paradigms.

## Approach

1. **PP framework summary** — survey the Predictive Processing / Predictive Coding literature. What is the core claim? What evidence supports it? How does the Free Energy Principle (FEP) unify perception, action, and learning under a single mathematical framework? Draw on Friston (2010), Clark (2016), Seth (2021).
2. **LLM mechanics summary** — describe next-token prediction in autoregressive Transformers. What is the training objective? What representations emerge? What does the evidence from mechanistic interpretability say about internal world models in LLMs?
3. **Structural comparison** — identify the key architectural and functional differences: embodiment and action-orientation in PP vs. passive text generation in LLMs; continuous online learning and prediction error minimisation in PP vs. batch pre-training in LLMs; hierarchical generative models in PP vs. attention-based sequence models in LLMs.
4. **World-model question** — what does it mean to "generate a model of the world"? Is LLM in-context reasoning a form of world modelling? What is the evidence for and against LLMs having grounded, structured world models?
5. **Consciousness and understanding** — what does the PP account say about consciousness (Seth's "controlled hallucination")? Does the PP framework imply that a sufficiently good predictive model could be conscious? What are the implications for LLMs?
6. **Synthesis** — produce Executive Summary, Key Findings, and Evidence Map.

## Sources

- [x] Karl Friston (2010) — "The free-energy principle: a unified brain theory?" — *Nature Reviews Neuroscience* — https://doi.org/10.1038/nrn2787
- [x] Andy Clark (2013) — "Whatever next? Predictive brains, situated agents, and the future of cognitive science" — *Behavioral and Brain Sciences* — https://www.fil.ion.ucl.ac.uk/~karl/Whatever%20next.pdf
- [x] Anil Seth interview (2021) — "Anil Seth Finds Consciousness in Life's Push Against Entropy" — *Quanta Magazine* — https://www.quantamagazine.org/anil-seth-finds-consciousness-in-lifes-push-against-entropy-20210930/
- [x] Anil Seth interview (2023) — "Reality is a controlled hallucination" — CCCB Lab — https://www.cccb.org/en/w/articles/anil-seth-reality-is-a-controlled-hallucination
- [ ] Jakob Hohwy (2013) — *The Predictive Mind* — Oxford University Press
- [x] Rao & Ballard (1999) — "Predictive coding in the visual cortex" — *Nature Neuroscience* — https://www.cs.utexas.edu/~dana/nn.pdf
- [x] Vaswani et al. (2017) — "Attention Is All You Need" — *Neural Information Processing Systems (NeurIPS) 2017* — https://papers.neurips.cc/paper/7181-attention-is-all-you-need.pdf
- [x] Brown et al. (2020) — "Language Models are Few-Shot Learners" — arXiv:2005.14165 — https://arxiv.org/pdf/2005.14165
- [x] Bender et al. (2021) — "On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?" — *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency* — https://doi.org/10.1145/3442188.3445922
- [x] Gurnee & Tegmark (2024) — "Language Models Represent Space and Time" — *International Conference on Learning Representations (ICLR) 2024* — https://proceedings.iclr.cc/paper_files/paper/2024/file/0a6059857ae5c82ea9726ee9282a7145-Paper-Conference.pdf
- [x] Kambhampati (2024) — "Can Large Language Models Reason and Plan?" — *Annals of the New York Academy of Sciences* — https://doi.org/10.1111/nyas.15125
- [x] Open Encyclopedia of Cognitive Science entry — "The free energy principle" — https://oecs.mit.edu/pub/my8vpqih
- [x] Prior completed research: `Research/completed/2026-03-17-ai-memory-systems-rag-neuroscience.md`
- [x] Prior completed research: `Research/completed/2026-03-15-neurological-context-management.md`
- [x] Prior completed research: `Research/completed/2026-02-28-predictive-processing-active-inference.md`

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

- [fact] The research question is whether the predictive processing account of brains and Large Language Model (LLM) next-token generation are the same kind of prediction system, and whether any difference changes how we should think about intelligence, meaning, and consciousness. Sources: https://doi.org/10.1038/nrn2787 ; https://papers.neurips.cc/paper/7181-attention-is-all-you-need.pdf
- [fact] The in-scope comparison is between Predictive Processing (PP) / Predictive Coding (PC) plus the Free Energy Principle (FEP) on one side, and autoregressive Transformer (AT) language modeling on the other, with explicit attention to embodiment, action, world models, and consciousness. Sources: https://doi.org/10.1038/nrn2787 ; https://www.fil.ion.ucl.ac.uk/~karl/Whatever%20next.pdf ; https://papers.neurips.cc/paper/7181-attention-is-all-you-need.pdf
- [fact] The main accessible sources are Friston's 2010 review, Clark's 2013 synthesis, Rao and Ballard's 1999 cortical model, Seth's public interviews explaining controlled hallucination and the life-consciousness link, Vaswani et al. on Transformer mechanics, Brown et al. on large-scale autoregressive language modeling, Gurnee and Tegmark on linear spatiotemporal structure in LLMs, Bender et al. on the stochastic-parrot critique, and Kambhampati on reasoning and planning limits. Sources: https://doi.org/10.1038/nrn2787 ; https://www.fil.ion.ucl.ac.uk/~karl/Whatever%20next.pdf ; https://www.cs.utexas.edu/~dana/nn.pdf ; https://www.quantamagazine.org/anil-seth-finds-consciousness-in-lifes-push-against-entropy-20210930/ ; https://www.cccb.org/en/w/articles/anil-seth-reality-is-a-controlled-hallucination ; https://papers.neurips.cc/paper/7181-attention-is-all-you-need.pdf ; https://arxiv.org/pdf/2005.14165 ; https://proceedings.iclr.cc/paper_files/paper/2024/file/0a6059857ae5c82ea9726ee9282a7145-Paper-Conference.pdf ; https://doi.org/10.1145/3442188.3445922 ; https://doi.org/10.1111/nyas.15125
- Prior-work cross-reference was completed before investigation against the related completed items named in `## Context`.
- [inference] The output format should separate empirical support from interpretation because the literature supports a strong distinction between "prediction as embodied control" and "prediction as text compression," but leaves some room for disagreement about how much latent world structure text-only training can induce. Sources: https://doi.org/10.1038/nrn2787 ; https://doi.org/10.1111/nyas.15125 ; https://proceedings.iclr.cc/paper_files/paper/2024/file/0a6059857ae5c82ea9726ee9282a7145-Paper-Conference.pdf

### §1 Question Decomposition

1. What does PP claim the brain is doing at the computational level?
   1.1. What are the core roles of hierarchical generative models, top-down predictions, and bottom-up prediction errors?
   1.2. What does active inference add beyond passive predictive coding?
   1.3. How much direct empirical support exists for this picture?
2. What does LLM next-token generation actually optimize?
   2.1. How do Transformer decoders generate outputs one token at a time?
   2.2. What does large-scale autoregressive training plausibly teach the model internally?
3. Are these two "prediction" regimes structurally equivalent?
   3.1. Is predicting sensory input for embodied control the same as predicting the next token in text?
   3.2. What is the role of embodiment, action, and online error correction in each case?
4. Do LLMs learn world models?
   4.1. What evidence suggests linear or structured internal representations?
   4.2. What evidence suggests those representations are still limited, ungrounded, or non-planning in character?
5. What follows for meaning, understanding, and consciousness?
   5.1. What does the stochastic-parrot critique imply?
   5.2. What does Seth's biological framing imply about consciousness in non-embodied predictors?

### §2 Investigation

#### A. Predictive Processing as embodied generative control

- [fact] Friston's abstract states that a free-energy principle can account for action, perception, and learning, and that several global brain theories may be unified by optimization of value or its complement, surprise. Source: https://pubmed.ncbi.nlm.nih.gov/20068583/
- [fact] Clark's 2013 synthesis states that brains support perception and action by constantly attempting to match incoming sensory inputs with top-down expectations using a hierarchical generative model that minimizes prediction error in a bidirectional cortical cascade. Source: https://www.fil.ion.ucl.ac.uk/~karl/Whatever%20next.pdf
- [fact] Rao and Ballard's 1999 paper proposes that feedback connections carry predictions of lower-level activity while feedforward connections carry residual errors between predictions and actual lower-level activity. Source: https://www.cs.utexas.edu/~dana/nn.pdf
- [fact] Rao and Ballard report that a hierarchical predictive coding network trained on natural images developed simple-cell-like receptive fields and extra-classical receptive-field effects, supporting the claim that prediction and residual error can explain cortical response structure. Source: https://www.cs.utexas.edu/~dana/nn.pdf
- [fact] The Open Encyclopedia of Cognitive Science states that in the neuroscience reading of the FEP, perception and learning make brain and body more like the world, while action makes the world more like the agent; this modeling tradition is called active inference. Source: https://oecs.mit.edu/pub/my8vpqih
- [inference] PP is not merely "the brain guesses what comes next." It is a closed sensorimotor control scheme in which prediction serves perception, learning, and action under conditions of bodily survival and environmental coupling. Sources: https://doi.org/10.1038/nrn2787 ; https://www.fil.ion.ucl.ac.uk/~karl/Whatever%20next.pdf ; https://oecs.mit.edu/pub/my8vpqih

#### B. LLM next-token generation as autoregressive sequence modeling

- [fact] Vaswani et al. describe the Transformer as an encoder-decoder architecture in which the decoder generates an output sequence one element at a time and is auto-regressive, consuming previously generated symbols as input when generating the next symbol. Source: https://papers.neurips.cc/paper/7181-attention-is-all-you-need.pdf
- [fact] Vaswani et al. state that masking in the decoder ensures predictions for position *i* depend only on known outputs at positions less than *i*, preserving the auto-regressive property. Source: https://papers.neurips.cc/paper/7181-attention-is-all-you-need.pdf
- [fact] Brown et al. describe Generative Pre-trained Transformer (GPT)-3 as a 175-billion-parameter autoregressive language model and frame its task-agnostic capability as emerging from large-scale pretraining on text followed by inference-time conditioning without weight updates. Source: https://arxiv.org/pdf/2005.14165
- [fact] Brown et al. also describe in-context learning as adaptation within the forward pass from textual instructions or demonstrations rather than online learning from direct environmental action. Source: https://arxiv.org/pdf/2005.14165
- [inference] The training objective of an LLM is to model conditional token distributions over text sequences, not to keep a body within viable states, reduce sensory surprise through action, or maintain a Markov blanket through embodied control. Sources: https://papers.neurips.cc/paper/7181-attention-is-all-you-need.pdf ; https://arxiv.org/pdf/2005.14165 ; https://oecs.mit.edu/pub/my8vpqih

#### C. Shared abstraction: prediction can force latent structure

- [fact] Gurnee and Tegmark report evidence that LLMs learn linear representations of space and time across multiple scales, that these representations are robust to prompting variations, and that they are unified across different entity types. Source: https://proceedings.iclr.cc/paper_files/paper/2024/file/0a6059857ae5c82ea9726ee9282a7145-Paper-Conference.pdf
- [fact] Gurnee and Tegmark explicitly state that such spatiotemporal representations are not themselves a dynamic causal world model, but are basic ingredients required in a more comprehensive model. Source: https://proceedings.iclr.cc/paper_files/paper/2024/file/0a6059857ae5c82ea9726ee9282a7145-Paper-Conference.pdf
- [fact] Brown et al. show that scaling autoregressive language models increases few-shot and in-context performance across many language tasks, indicating that next-token prediction can induce broad transferable structure even without task-specific fine-tuning. Source: https://arxiv.org/pdf/2005.14165
- [inference] It is false to say that LLMs are "just autocomplete" if that phrase means they only memorize local surface statistics; the available evidence supports richer internal structure than trivial n-gram continuation. Sources: https://arxiv.org/pdf/2005.14165 ; https://proceedings.iclr.cc/paper_files/paper/2024/file/0a6059857ae5c82ea9726ee9282a7145-Paper-Conference.pdf
- [inference] It is also too strong to equate those latent text-induced structures with the embodied generative models posited by PP, because the evidence shows partial structure recovery rather than a full action-guiding model of a lived environment. Sources: https://proceedings.iclr.cc/paper_files/paper/2024/file/0a6059857ae5c82ea9726ee9282a7145-Paper-Conference.pdf ; https://doi.org/10.1038/nrn2787 ; https://www.fil.ion.ucl.ac.uk/~karl/Whatever%20next.pdf

#### D. Why the two systems are not functionally identical

- [fact] Clark argues that predictive processing offers a unifying model of perception and action, not just passive recognition, and repeatedly frames the brain as a prediction machine in the service of adaptive success. Source: https://www.fil.ion.ucl.ac.uk/~karl/Whatever%20next.pdf
- [fact] The Open Encyclopedia of Cognitive Science says action, under active inference, makes the world more like the agent, whereas perception and learning make the agent more like the world. Source: https://oecs.mit.edu/pub/my8vpqih
- [fact] Brown et al. describe in-context learning inside a text interaction loop and do not describe direct online weight updates from physical action or sensorimotor correction during deployment. Source: https://arxiv.org/pdf/2005.14165
- [inference] The central functional asymmetry is that PP prediction is world-facing and policy-relevant, whereas LLM next-token prediction is corpus-facing and completion-relevant. Both are predictive, but they predict under different objective functions, different feedback loops, and different notions of error. Sources: https://doi.org/10.1038/nrn2787 ; https://www.fil.ion.ucl.ac.uk/~karl/Whatever%20next.pdf ; https://papers.neurips.cc/paper/7181-attention-is-all-you-need.pdf ; https://arxiv.org/pdf/2005.14165
- [inference] A brain that predicted perfectly but could not act would fail at the biological job PP is meant to explain, whereas an LLM can fulfill its training objective without ever acting in the world beyond producing the next token. Sources: https://oecs.mit.edu/pub/my8vpqih ; https://papers.neurips.cc/paper/7181-attention-is-all-you-need.pdf

#### E. Meaning, planning, and the limits of text-only success

- [fact] Bender et al. argue that ever-larger language models create environmental, opportunity-cost, and bias risks, and they urge researchers to move beyond the assumption that scale alone should define progress. Source: https://doi.org/10.1145/3442188.3445922
- [fact] Bender et al. frame the concern that language model performance can be mistaken for language understanding when systems are trained on web-scale text without grounded reference to the world or to stakeholder harms. Source: https://doi.org/10.1145/3442188.3445922
- [fact] Kambhampati writes that LLMs are trained to predict the distribution of the *n*th token given *n-1* previous tokens and argues that nothing in their training and use suggests principled reasoning of the sort required for planning. Source: https://arxiv.org/html/2403.04121v2
- [fact] Kambhampati further argues that LLMs are better understood as approximate retrieval systems or non-veridical memories than as systems that reliably execute principled search-based planning. Source: https://arxiv.org/html/2403.04121v2
- [inference] Current evidence supports the claim that next-token prediction can yield useful abstractions and competent behavior in many domains, but does not by itself justify claims of grounded understanding, robust planning, or semantic parity with embodied cognition. Sources: https://doi.org/10.1145/3442188.3445922 ; https://doi.org/10.1111/nyas.15125 ; https://proceedings.iclr.cc/paper_files/paper/2024/file/0a6059857ae5c82ea9726ee9282a7145-Paper-Conference.pdf

#### F. Consciousness and Seth's biological constraint

- [fact] Seth says consciousness is not present despite our nature as flesh-and-blood living machines, but because of that nature. Source: https://www.quantamagazine.org/anil-seth-finds-consciousness-in-lifes-push-against-entropy-20210930/
- [fact] Seth says the FEP is not itself a theory about consciousness, but it is relevant because brains use predictive models to regulate body temperature and keep bodies alive. Source: https://www.quantamagazine.org/anil-seth-finds-consciousness-in-lifes-push-against-entropy-20210930/
- [fact] Seth's CCCB interview describes reality as a controlled hallucination in which experience is content predicted from the inside out, constrained by sensory information in a way useful for the organism. Source: https://www.cccb.org/en/w/articles/anil-seth-reality-is-a-controlled-hallucination
- [fact] Seth also says the root of consciousness is the brain's perception of the physiological state of the body and warns against conflating consciousness with intelligence. Source: https://www.cccb.org/en/w/articles/anil-seth-reality-is-a-controlled-hallucination
- [inference] Seth's account does not imply that any sufficiently accurate predictor is conscious. It ties conscious experience specifically to organism-level, body-regulating predictive control, especially interoceptive regulation, which current text-only LLMs do not possess. Sources: https://www.quantamagazine.org/anil-seth-finds-consciousness-in-lifes-push-against-entropy-20210930/ ; https://www.cccb.org/en/w/articles/anil-seth-reality-is-a-controlled-hallucination

#### G. Source conflicts, limits, and integration

- [inference] The most decision-relevant pro-LLM world-model source in this set is Gurnee and Tegmark, but even that paper explicitly limits its claim to basic ingredients rather than a full dynamic causal world model. Sources: https://proceedings.iclr.cc/paper_files/paper/2024/file/0a6059857ae5c82ea9726ee9282a7145-Paper-Conference.pdf ; https://doi.org/10.1111/nyas.15125
- [inference] The most decision-relevant skeptical source in this set is Kambhampati, who argues that planning competence is not supported by the training objective alone and should not be inferred from surface task performance. Sources: https://doi.org/10.1111/nyas.15125 ; https://doi.org/10.1145/3442188.3445922
- [inference] These positions are not fully contradictory. They are best read as saying that text-only next-token prediction can induce partial latent models of regularities in the world, but that such models are neither fully grounded nor sufficient evidence for principled reasoning, embodied understanding, or consciousness. Sources: https://proceedings.iclr.cc/paper_files/paper/2024/file/0a6059857ae5c82ea9726ee9282a7145-Paper-Conference.pdf ; https://doi.org/10.1111/nyas.15125 ; https://doi.org/10.1145/3442188.3445922
- [assumption] Public interviews and open-access syntheses are acceptable stand-ins for Seth's and Clark's inaccessible books for this item's core claims. **Justification:** the claims used here are directly stated in accessible interviews or papers and are sufficient for the comparison task, but a future deep dive into their full philosophical arguments should consult the books directly.

### §3 Reasoning

- [fact] The evidence supports a layered distinction: PP is well-supported as a framework for hierarchical predictive perception and action in brains, while Transformer language modeling is well-supported as an auto-regressive sequence model over tokens. Sources: https://www.cs.utexas.edu/~dana/nn.pdf ; https://www.fil.ion.ucl.ac.uk/~karl/Whatever%20next.pdf ; https://papers.neurips.cc/paper/7181-attention-is-all-you-need.pdf
- [inference] Because each framework uses "prediction" to solve a different problem, superficial verbal similarity is not enough to treat them as the same kind of architecture. Sources: https://doi.org/10.1038/nrn2787 ; https://papers.neurips.cc/paper/7181-attention-is-all-you-need.pdf
- [fact] The strongest commonality is that both systems can compress regularities into latent representations that support better future predictions. Sources: https://doi.org/10.1038/nrn2787 ; https://arxiv.org/pdf/2005.14165 ; https://proceedings.iclr.cc/paper_files/paper/2024/file/0a6059857ae5c82ea9726ee9282a7145-Paper-Conference.pdf
- [inference] The decisive disanalogy is not "biological vs silicon" but "embodied, action-coupled control of worldly and bodily states" versus "text-conditioned continuation over a static training distribution." Sources: https://www.fil.ion.ucl.ac.uk/~karl/Whatever%20next.pdf ; https://arxiv.org/pdf/2005.14165 ; https://oecs.mit.edu/pub/my8vpqih
- [inference] Claims that LLMs have no world model at all overstate the skeptical case, while claims that next-token prediction alone closes the gap to brain-like understanding overstate the optimistic case. Sources: https://proceedings.iclr.cc/paper_files/paper/2024/file/0a6059857ae5c82ea9726ee9282a7145-Paper-Conference.pdf ; https://doi.org/10.1111/nyas.15125

### §4 Consistency Check

- [fact] No source in the consulted set disputes that Transformer decoders are auto-regressive token predictors. Sources: https://papers.neurips.cc/paper/7181-attention-is-all-you-need.pdf ; https://arxiv.org/pdf/2005.14165
- [fact] No source in the consulted set supports the claim that current LLMs have bodily interoception, autonomous active inference, or organism-level survival control. Sources: https://arxiv.org/pdf/2005.14165 ; https://doi.org/10.1111/nyas.15125 ; https://www.quantamagazine.org/anil-seth-finds-consciousness-in-lifes-push-against-entropy-20210930/
- [fact] The strongest tension is between evidence for latent spatiotemporal representations and arguments that LLMs do not thereby achieve grounded understanding or principled planning. Sources: https://proceedings.iclr.cc/paper_files/paper/2024/file/0a6059857ae5c82ea9726ee9282a7145-Paper-Conference.pdf ; https://doi.org/10.1111/nyas.15125 ; https://doi.org/10.1145/3442188.3445922
- [inference] That tension is resolved by distinguishing "partial internal structure" from "embodied generative control" and "surface task success" from "principled reasoning." Sources: https://proceedings.iclr.cc/paper_files/paper/2024/file/0a6059857ae5c82ea9726ee9282a7145-Paper-Conference.pdf ; https://doi.org/10.1111/nyas.15125 ; https://doi.org/10.1145/3442188.3445922

### §5 Depth and Breadth Expansion

- [fact] Technically, PP explains how agents maintain adaptive coupling to the world by predicting and correcting sensory and bodily states, whereas LLMs explain how a model can compress textual regularities into a high-capacity representation space. Sources: https://www.fil.ion.ucl.ac.uk/~karl/Whatever%20next.pdf ; https://arxiv.org/pdf/2005.14165
- [inference] Philosophically, this means the key dispute is not whether prediction matters, but whether meaning requires grounding in action and organismic stakes rather than pattern compression alone. Sources: https://www.fil.ion.ucl.ac.uk/~karl/Whatever%20next.pdf ; https://doi.org/10.1145/3442188.3445922
- [inference] Historically, PP inherits Helmholtzian perception-as-inference and Fristonian active inference, while modern LLMs inherit statistical language modeling and scale-driven representation learning; the lineages intersect on prediction but diverge on function. Sources: https://www.fil.ion.ucl.ac.uk/~karl/Whatever%20next.pdf ; https://arxiv.org/pdf/2005.14165
- [inference] Behaviorally, a brain's predictions are constantly disciplined by proprioception, interoception, and the cost of being wrong in the world, whereas an LLM's predictions are primarily disciplined by text distribution mismatch and, at deployment time, prompt constraints. Sources: https://oecs.mit.edu/pub/my8vpqih ; https://arxiv.org/pdf/2005.14165
- [fact] Conceptually, Seth's distinction between intelligence and consciousness blocks the common shortcut from "predictive competence" to "sentience." Source: https://www.cccb.org/en/w/articles/anil-seth-reality-is-a-controlled-hallucination

### §6 Synthesis

**Executive summary:**

- [inference] Human brains are not just next-token predictors in a richer medium; predictive processing is an embodied control architecture that uses hierarchical generative models to regulate perception, action, and bodily viability, whereas current LLMs optimize auto-regressive text prediction over symbol sequences. Sources: https://doi.org/10.1038/nrn2787 ; https://www.fil.ion.ucl.ac.uk/~karl/Whatever%20next.pdf ; https://papers.neurips.cc/paper/7181-attention-is-all-you-need.pdf ; https://arxiv.org/pdf/2005.14165
- [fact] The neuroscience evidence supports predictive coding as a substantive account of cortical organization, and the machine-learning evidence supports next-token prediction as a powerful route to broad latent structure in text models. Sources: https://www.cs.utexas.edu/~dana/nn.pdf ; https://proceedings.iclr.cc/paper_files/paper/2024/file/0a6059857ae5c82ea9726ee9282a7145-Paper-Conference.pdf
- [inference] The overlap matters because it explains why LLMs can exhibit partial world-model-like structure and surprisingly general competence, but the difference matters more because text-only sequence prediction lacks embodiment, online action, interoception, and survival-grounded error correction. Sources: https://proceedings.iclr.cc/paper_files/paper/2024/file/0a6059857ae5c82ea9726ee9282a7145-Paper-Conference.pdf ; https://doi.org/10.1111/nyas.15125 ; https://www.quantamagazine.org/anil-seth-finds-consciousness-in-lifes-push-against-entropy-20210930/
- [inference] For intelligence, the best-supported conclusion is that next-token prediction can generate meaningful competence without closing the whole gap to embodied understanding; for consciousness, Seth's own framework points away from treating current LLMs as candidates simply because they predict well. Sources: https://doi.org/10.1145/3442188.3445922 ; https://www.cccb.org/en/w/articles/anil-seth-reality-is-a-controlled-hallucination ; https://www.quantamagazine.org/anil-seth-finds-consciousness-in-lifes-push-against-entropy-20210930/

**Key findings:**

1. [inference] **Confidence: high.** Predictive Processing (PP) and Large Language Model (LLM) next-token prediction share a generic commitment to prediction, but they solve different problems because PP uses prediction to control perception and action in an embodied organism while LLMs use prediction to continue token sequences in text. Sources: https://doi.org/10.1038/nrn2787 ; https://www.fil.ion.ucl.ac.uk/~karl/Whatever%20next.pdf ; https://papers.neurips.cc/paper/7181-attention-is-all-you-need.pdf ; https://arxiv.org/pdf/2005.14165
2. [fact] **Confidence: high.** The strongest neuroscience evidence supports predictive coding at the cortical-architecture level, where top-down pathways carry predictions and bottom-up pathways carry residual error signals in hierarchical processing. Sources: https://www.cs.utexas.edu/~dana/nn.pdf ; https://www.fil.ion.ucl.ac.uk/~karl/Whatever%20next.pdf
3. [fact] **Confidence: high.** Transformer language models generate outputs auto-regressively from prior tokens and can improve through scale into broad in-context competence, but their documented mechanism remains sequence modeling over text rather than embodied active inference. Sources: https://papers.neurips.cc/paper/7181-attention-is-all-you-need.pdf ; https://arxiv.org/pdf/2005.14165
4. [inference] **Confidence: medium.** Evidence that LLMs encode linear spatial and temporal structure shows that next-token prediction can induce partial world-model ingredients, but that evidence stops short of demonstrating a grounded, dynamic, action-ready model of the world. Sources: https://proceedings.iclr.cc/paper_files/paper/2024/file/0a6059857ae5c82ea9726ee9282a7145-Paper-Conference.pdf ; https://doi.org/10.1111/nyas.15125
5. [inference] **Confidence: high.** The strongest current critiques are persuasive that text-only prediction alone does not warrant claims of principled reasoning, planning, or human-like understanding, because success on completion tasks can coexist with non-veridical memory and weak grounding. Sources: https://doi.org/10.1145/3442188.3445922 ; https://doi.org/10.1111/nyas.15125
6. [inference] **Confidence: medium.** Prediction can support intelligence-like competence in both brains and LLMs, but the meaning of that competence differs because brains predict to keep an organism viable in the world whereas LLMs predict to compress and continue symbol streams. Sources: https://doi.org/10.1038/nrn2787 ; https://arxiv.org/pdf/2005.14165 ; https://oecs.mit.edu/pub/my8vpqih
7. [inference] **Confidence: high.** Seth's account of consciousness strengthens the conclusion that current LLMs should not be treated as conscious on the basis of next-token prediction alone, because his theory ties experience to embodied, interoceptive regulation in living systems rather than to generic predictive success. Sources: https://www.quantamagazine.org/anil-seth-finds-consciousness-in-lifes-push-against-entropy-20210930/ ; https://www.cccb.org/en/w/articles/anil-seth-reality-is-a-controlled-hallucination

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] PP and LLMs are both predictive but not functionally equivalent systems. | https://doi.org/10.1038/nrn2787 ; https://www.fil.ion.ucl.ac.uk/~karl/Whatever%20next.pdf ; https://papers.neurips.cc/paper/7181-attention-is-all-you-need.pdf ; https://arxiv.org/pdf/2005.14165 | high | Common prediction vocabulary hides different objectives and feedback loops. |
| [fact] Predictive coding has direct support from hierarchical cortical modeling with prediction/error pathway separation. | https://www.cs.utexas.edu/~dana/nn.pdf ; https://www.fil.ion.ucl.ac.uk/~karl/Whatever%20next.pdf | high | Rao and Ballard plus Clark give both model detail and synthesis. |
| [fact] Transformer LLMs are auto-regressive token predictors with broad in-context competence. | https://papers.neurips.cc/paper/7181-attention-is-all-you-need.pdf ; https://arxiv.org/pdf/2005.14165 | high | Mechanism is clear and well documented. |
| [inference] LLMs learn some world-model ingredients, but not a full grounded world model. | https://proceedings.iclr.cc/paper_files/paper/2024/file/0a6059857ae5c82ea9726ee9282a7145-Paper-Conference.pdf ; https://doi.org/10.1111/nyas.15125 | medium | Probe evidence is real but limited by what it demonstrates. |
| [inference] Text-only prediction does not by itself establish principled reasoning or human-like understanding. | https://doi.org/10.1145/3442188.3445922 ; https://doi.org/10.1111/nyas.15125 | high | Independent skeptical lines converge on this point. |
| [inference] Brain-style prediction and LLM-style prediction yield different kinds of intelligence because their tasks differ. | https://doi.org/10.1038/nrn2787 ; https://arxiv.org/pdf/2005.14165 ; https://oecs.mit.edu/pub/my8vpqih | medium | Strong conceptual support, but still partly interpretive. |
| [inference] Seth's framework does not support treating current LLMs as conscious predictors. | https://www.quantamagazine.org/anil-seth-finds-consciousness-in-lifes-push-against-entropy-20210930/ ; https://www.cccb.org/en/w/articles/anil-seth-reality-is-a-controlled-hallucination | high | Consciousness is tied to embodied interoceptive regulation, not generic prediction. |

**Assumptions:**

- [assumption] Clark's 2013 open-access paper is a sufficient proxy for the inaccessible 2016 *Surfing Uncertainty* book for the claims used here. **Justification:** the core hierarchical-generative-model and action-oriented claims appear directly in the 2013 paper.
- [assumption] Seth's public interviews are sufficient to support the consciousness comparison in this item. **Justification:** the comparison depends on his explicit public claims that consciousness is rooted in biological embodiment and that the FEP is not itself a theory of consciousness.

**Analysis:**

- [inference] The fairest comparison is not "brains versus autocomplete" or "brains and LLMs are the same." The evidence supports a middle position: next-token prediction can recover surprisingly rich internal structure, but the structure is learned under a fundamentally different control problem than the one PP is designed to explain. Sources: https://proceedings.iclr.cc/paper_files/paper/2024/file/0a6059857ae5c82ea9726ee9282a7145-Paper-Conference.pdf ; https://doi.org/10.1038/nrn2787
- [inference] This difference matters for meaning because PP treats representation as inseparable from active engagement with the world, whereas LLM training allows useful abstraction to emerge without direct worldly action but also leaves grounding and truth-tracking fragile. Sources: https://www.fil.ion.ucl.ac.uk/~karl/Whatever%20next.pdf ; https://doi.org/10.1145/3442188.3445922
- [inference] This difference matters for intelligence because many tasks reward latent structure and pattern compression, so LLMs can appear broadly capable, but planning- and embodiment-heavy domains reveal the absence of the sensorimotor loop that PP treats as central. Sources: https://arxiv.org/pdf/2005.14165 ; https://doi.org/10.1111/nyas.15125
- [inference] This difference matters most for consciousness because Seth's argument runs from life and bodily self-maintenance to experience, not from generic predictive accuracy to experience. Sources: https://www.quantamagazine.org/anil-seth-finds-consciousness-in-lifes-push-against-entropy-20210930/ ; https://www.cccb.org/en/w/articles/anil-seth-reality-is-a-controlled-hallucination

**Risks, gaps, uncertainties:**

- [fact] This item did not consult the full books by Clark, Hohwy, or Seth directly because they were not publicly accessible within the session constraints. Sources: https://www.fil.ion.ucl.ac.uk/~karl/Whatever%20next.pdf ; https://www.quantamagazine.org/anil-seth-finds-consciousness-in-lifes-push-against-entropy-20210930/ ; https://www.cccb.org/en/w/articles/anil-seth-reality-is-a-controlled-hallucination
- [fact] Gurnee and Tegmark's evidence is probe-based and therefore supports decodability more directly than causal use. Sources: https://proceedings.iclr.cc/paper_files/paper/2024/file/0a6059857ae5c82ea9726ee9282a7145-Paper-Conference.pdf
- [fact] Kambhampati's paper is an important skeptical synthesis, but it argues at a conceptual level more than through a single decisive benchmark. Sources: https://doi.org/10.1111/nyas.15125
- [inference] Future multimodal or embodied AI systems could narrow some of the gaps identified here, so the conclusions are strongest for current text-only autoregressive LLMs rather than for all conceivable predictive AI systems. Sources: https://www.cccb.org/en/w/articles/anil-seth-reality-is-a-controlled-hallucination ; https://doi.org/10.1111/nyas.15125

**Open questions:**

- Which empirical benchmark would best distinguish "latent world structure from text" from "grounded action-ready world model" in a way both mechanistic interpretability and planning researchers would accept?
- How much embodiment is actually necessary for meaning-like understanding: sensorimotor grounding, persistent tool use, interoception analogues, or full biological self-maintenance?
- Could an artificial system satisfy Seth-like consciousness criteria without biology if it possessed robust interoceptive self-modeling and survival-relevant embodiment?

### §7 Recursive Review

- Every claim in §§0–6 is labeled as [fact], [inference], or [assumption].
- The final synthesis introduces no claims that are absent from the investigation and reasoning sections.
- The acronym audit was completed against the full document text, with first-use expansions confirmed for LLM, PP, PC, FEP, AT, GPT, and AI.
- [fact] The main unresolved limits are source-access gaps for some books and the still-open dispute about how much latent structure is sufficient for genuine world modeling. Sources: https://proceedings.iclr.cc/paper_files/paper/2024/file/0a6059857ae5c82ea9726ee9282a7145-Paper-Conference.pdf ; https://doi.org/10.1111/nyas.15125
- [inference] The note is ready to seed Findings because the strongest conclusion survives the main skeptical and optimistic counterarguments without depending on any inaccessible source. Sources: https://doi.org/10.1038/nrn2787 ; https://doi.org/10.1111/nyas.15125 ; https://www.quantamagazine.org/anil-seth-finds-consciousness-in-lifes-push-against-entropy-20210930/

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

[inference] Human brains are not just next-token predictors in a richer medium; predictive processing is an embodied control architecture that uses hierarchical generative models to regulate perception, action, and bodily viability, whereas current Large Language Models (LLMs) optimize auto-regressive text prediction over symbol sequences. Sources: https://doi.org/10.1038/nrn2787 ; https://www.fil.ion.ucl.ac.uk/~karl/Whatever%20next.pdf ; https://papers.neurips.cc/paper/7181-attention-is-all-you-need.pdf ; https://arxiv.org/pdf/2005.14165

[fact] The neuroscience evidence supports predictive coding as a substantive account of cortical organization, and the machine-learning evidence supports next-token prediction as a powerful route to broad latent structure in text models. Sources: https://www.cs.utexas.edu/~dana/nn.pdf ; https://proceedings.iclr.cc/paper_files/paper/2024/file/0a6059857ae5c82ea9726ee9282a7145-Paper-Conference.pdf

[inference] The overlap matters because it explains why LLMs can exhibit partial world-model-like structure and surprisingly general competence, but the difference matters more because text-only sequence prediction lacks embodiment, online action, interoception, and survival-grounded error correction. Sources: https://proceedings.iclr.cc/paper_files/paper/2024/file/0a6059857ae5c82ea9726ee9282a7145-Paper-Conference.pdf ; https://doi.org/10.1111/nyas.15125 ; https://www.quantamagazine.org/anil-seth-finds-consciousness-in-lifes-push-against-entropy-20210930/

[inference] For intelligence, the best-supported conclusion is that next-token prediction can generate meaningful competence without closing the whole gap to embodied understanding; for consciousness, Seth's own framework points away from treating current LLMs as candidates simply because they predict well. Sources: https://doi.org/10.1145/3442188.3445922 ; https://www.cccb.org/en/w/articles/anil-seth-reality-is-a-controlled-hallucination ; https://www.quantamagazine.org/anil-seth-finds-consciousness-in-lifes-push-against-entropy-20210930/

### Key Findings

1. [inference] **Confidence: high.** Predictive Processing (PP) and Large Language Model (LLM) next-token prediction share a generic commitment to prediction, but they solve different problems because PP uses prediction to control perception and action in an embodied organism while LLMs use prediction to continue token sequences in text. Sources: https://doi.org/10.1038/nrn2787 ; https://www.fil.ion.ucl.ac.uk/~karl/Whatever%20next.pdf ; https://papers.neurips.cc/paper/7181-attention-is-all-you-need.pdf ; https://arxiv.org/pdf/2005.14165
2. [fact] **Confidence: high.** The strongest neuroscience evidence supports predictive coding at the cortical-architecture level, where top-down pathways carry predictions and bottom-up pathways carry residual error signals in hierarchical processing. Sources: https://www.cs.utexas.edu/~dana/nn.pdf ; https://www.fil.ion.ucl.ac.uk/~karl/Whatever%20next.pdf
3. [fact] **Confidence: high.** Transformer language models generate outputs auto-regressively from prior tokens and can improve through scale into broad in-context competence, but their documented mechanism remains sequence modeling over text rather than embodied active inference. Sources: https://papers.neurips.cc/paper/7181-attention-is-all-you-need.pdf ; https://arxiv.org/pdf/2005.14165
4. [inference] **Confidence: medium.** Evidence that LLMs encode linear spatial and temporal structure shows that next-token prediction can induce partial world-model ingredients, but that evidence stops short of demonstrating a grounded, dynamic, action-ready model of the world. Sources: https://proceedings.iclr.cc/paper_files/paper/2024/file/0a6059857ae5c82ea9726ee9282a7145-Paper-Conference.pdf ; https://doi.org/10.1111/nyas.15125
5. [inference] **Confidence: high.** The strongest current critiques are persuasive that text-only prediction alone does not warrant claims of principled reasoning, planning, or human-like understanding, because success on completion tasks can coexist with non-veridical memory and weak grounding. Sources: https://doi.org/10.1145/3442188.3445922 ; https://doi.org/10.1111/nyas.15125
6. [inference] **Confidence: medium.** Prediction can support intelligence-like competence in both brains and LLMs, but the meaning of that competence differs because brains predict to keep an organism viable in the world whereas LLMs predict to compress and continue symbol streams. Sources: https://doi.org/10.1038/nrn2787 ; https://arxiv.org/pdf/2005.14165 ; https://oecs.mit.edu/pub/my8vpqih
7. [inference] **Confidence: high.** Seth's account of consciousness strengthens the conclusion that current LLMs should not be treated as conscious on the basis of next-token prediction alone, because his theory ties experience to embodied, interoceptive regulation in living systems rather than to generic predictive success. Sources: https://www.quantamagazine.org/anil-seth-finds-consciousness-in-lifes-push-against-entropy-20210930/ ; https://www.cccb.org/en/w/articles/anil-seth-reality-is-a-controlled-hallucination

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] PP and LLMs are both predictive but not functionally equivalent systems. | https://doi.org/10.1038/nrn2787 ; https://www.fil.ion.ucl.ac.uk/~karl/Whatever%20next.pdf ; https://papers.neurips.cc/paper/7181-attention-is-all-you-need.pdf ; https://arxiv.org/pdf/2005.14165 | high | Common prediction vocabulary hides different objectives and feedback loops. |
| [fact] Predictive coding has direct support from hierarchical cortical modeling with prediction/error pathway separation. | https://www.cs.utexas.edu/~dana/nn.pdf ; https://www.fil.ion.ucl.ac.uk/~karl/Whatever%20next.pdf | high | Rao and Ballard plus Clark give both model detail and synthesis. |
| [fact] Transformer LLMs are auto-regressive token predictors with broad in-context competence. | https://papers.neurips.cc/paper/7181-attention-is-all-you-need.pdf ; https://arxiv.org/pdf/2005.14165 | high | Mechanism is clear and well documented. |
| [inference] LLMs learn some world-model ingredients, but not a full grounded world model. | https://proceedings.iclr.cc/paper_files/paper/2024/file/0a6059857ae5c82ea9726ee9282a7145-Paper-Conference.pdf ; https://doi.org/10.1111/nyas.15125 | medium | Probe evidence is real but limited by what it demonstrates. |
| [inference] Text-only prediction does not by itself establish principled reasoning or human-like understanding. | https://doi.org/10.1145/3442188.3445922 ; https://doi.org/10.1111/nyas.15125 | high | Independent skeptical lines converge on this point. |
| [inference] Brain-style prediction and LLM-style prediction yield different kinds of intelligence because their tasks differ. | https://doi.org/10.1038/nrn2787 ; https://arxiv.org/pdf/2005.14165 ; https://oecs.mit.edu/pub/my8vpqih | medium | Strong conceptual support, but still partly interpretive. |
| [inference] Seth's framework does not support treating current LLMs as conscious predictors. | https://www.quantamagazine.org/anil-seth-finds-consciousness-in-lifes-push-against-entropy-20210930/ ; https://www.cccb.org/en/w/articles/anil-seth-reality-is-a-controlled-hallucination | high | Consciousness is tied to embodied interoceptive regulation, not generic prediction. |

### Assumptions

- [assumption] Clark's 2013 open-access paper is a sufficient proxy for the inaccessible 2016 *Surfing Uncertainty* book. **Justification:** the core hierarchical-generative-model and action-oriented claims used here appear directly in the 2013 paper.
- [assumption] Seth's public interviews are sufficient to support the consciousness comparison in this item. **Justification:** the comparison depends on his explicit public claims that consciousness is rooted in biological embodiment and that the FEP is not itself a theory of consciousness.

### Analysis

[inference] The fairest comparison is not "brains versus autocomplete" or "brains and LLMs are the same." The evidence supports a middle position: next-token prediction can recover surprisingly rich internal structure, but the structure is learned under a fundamentally different control problem than the one predictive processing is designed to explain. Sources: https://proceedings.iclr.cc/paper_files/paper/2024/file/0a6059857ae5c82ea9726ee9282a7145-Paper-Conference.pdf ; https://doi.org/10.1038/nrn2787

[inference] For meaning, predictive processing treats representation as inseparable from active engagement with the world, whereas LLM training allows useful abstraction to emerge without direct worldly action but also leaves grounding and truth-tracking fragile. Sources: https://www.fil.ion.ucl.ac.uk/~karl/Whatever%20next.pdf ; https://doi.org/10.1145/3442188.3445922

[inference] For intelligence, many tasks reward latent structure and pattern compression, so LLMs can appear broadly capable, but planning- and embodiment-heavy domains reveal the absence of the sensorimotor loop that predictive processing treats as central. Sources: https://arxiv.org/pdf/2005.14165 ; https://doi.org/10.1111/nyas.15125

[inference] For consciousness, Seth's argument runs from life and bodily self-maintenance to experience, not from generic predictive accuracy to experience. Sources: https://www.quantamagazine.org/anil-seth-finds-consciousness-in-lifes-push-against-entropy-20210930/ ; https://www.cccb.org/en/w/articles/anil-seth-reality-is-a-controlled-hallucination

### Risks, Gaps, and Uncertainties

- [fact] This item did not consult the full books by Clark, Hohwy, or Seth directly because they were not publicly accessible within the session constraints. Sources: https://www.fil.ion.ucl.ac.uk/~karl/Whatever%20next.pdf ; https://www.quantamagazine.org/anil-seth-finds-consciousness-in-lifes-push-against-entropy-20210930/ ; https://www.cccb.org/en/w/articles/anil-seth-reality-is-a-controlled-hallucination
- [fact] Gurnee and Tegmark's evidence is probe-based and therefore supports decodability more directly than causal use. Sources: https://proceedings.iclr.cc/paper_files/paper/2024/file/0a6059857ae5c82ea9726ee9282a7145-Paper-Conference.pdf
- [fact] Kambhampati's paper is an important skeptical synthesis, but it argues at a conceptual level more than through a single decisive benchmark. Sources: https://doi.org/10.1111/nyas.15125
- [inference] Future multimodal or embodied AI systems could narrow some of the gaps identified here, so the conclusions are strongest for current text-only autoregressive LLMs rather than for all conceivable predictive AI systems. Sources: https://www.cccb.org/en/w/articles/anil-seth-reality-is-a-controlled-hallucination ; https://doi.org/10.1111/nyas.15125

### Open Questions

- Which empirical benchmark would best distinguish latent world structure from grounded action-ready world model in a way both mechanistic interpretability and planning researchers would accept?
- How much embodiment is actually necessary for meaning-like understanding: sensorimotor grounding, persistent tool use, interoception analogues, or full biological self-maintenance?
- Could an artificial system satisfy Seth-like consciousness criteria without biology if it possessed robust interoceptive self-modeling and survival-relevant embodiment?

---

## Output

- Type: knowledge
- Description: Structured comparison of predictive processing in brains versus next-token prediction in Large Language Models, with a direct answer on world models, understanding, and consciousness.
- Links:
  - https://doi.org/10.1038/nrn2787
  - https://papers.neurips.cc/paper/7181-attention-is-all-you-need.pdf
  - https://www.quantamagazine.org/anil-seth-finds-consciousness-in-lifes-push-against-entropy-20210930/