---
review_count: 2
title: "Trusting Trust and AI Corpus Contamination"
added: 2026-03-19T07:58:52+00:00
status: completed
priority: high  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [ai, epistemology, trust, corpus-contamination, prompt-injection, large-language-model, knowledge, security]
started: 2026-03-19T07:58:52+00:00
completed: 2026-03-19T07:58:52+00:00
output: [knowledge]
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# Trusting Trust and AI Corpus Contamination

## Research Question

Ken Thompson's "Trusting Trust" argument shows that you cannot verify a compiler by reading its source code if the compiler was compiled by a compromised toolchain — the contamination lives in the binary, not the source. What is the web-scale analogue for Artificial Intelligence (AI)-generated content, and what does it mean for epistemology, knowledge verification, and trust when roughly half of all text on the web is now AI-generated and that proportion is growing?

## Scope

**In scope:**
- Thompson's original "Reflections on Trusting Trust" (1984) argument and its core insight about self-replicating corruption
- The structural analogy: AI-generated content → web corpus → training data → new AI-generated content (the closed loop)
- Current estimates of the fraction of web text that is AI-generated and trajectory projections
- Epistemological implications: what does "citing sources" mean when the cited sources may themselves be AI-generated and cross-indexed as authoritative?
- The relationship to prompt injection: how corpus-level contamination differs from document-level injection attacks
- Existing detection approaches and their fundamental limitations (document-level vs corpus-level)
- Prior work on data poisoning, model collapse, and self-referential training loops

**Out of scope:**
- Implementation details of specific AI detection tools
- Legal or copyright aspects of AI-generated text
- Misinformation and disinformation research beyond the epistemic verification problem

**Constraints:** Publicly accessible web sources, papers, and essays. No paywalled content unless freely available preprints exist.

## Context

**[fact]** Ken Thompson's 1984 Turing Award lecture "Reflections on Trusting Trust" shows that a compiler can be altered so that it inserts a backdoor into programs it compiles, including later versions of itself, while leaving the visible source apparently clean. **[fact]** The security lesson is that source inspection alone cannot prove integrity when the production chain is compromised upstream. (Source: https://www.cs.cmu.edu/afs/cs/academic/class/15712-f08/www/lectures/Thompson84lecture.pdf)

**[inference]** This item examines whether the public web is developing an analogous integrity problem as AI-generated text is published, crawled, and re-used in later models and summaries. **[fact]** The prevalence evidence reviewed later in this item supports substantial synthetic saturation of public web text, but not a settled claim that half of all web text is AI-generated. (Sources: https://graphite.io/five-percent/more-articles-are-now-created-by-ai-than-humans ; https://arxiv.org/abs/2504.08755)

**[inference]** If synthetic text is repeatedly ingested into later corpora, then local document checks such as fluency, internal consistency, or citation count become weaker evidence of independence, because the visible sources may all descend from the same generative loop. **[inference]** That would make the problem closer to recursive corpus contamination than to an ordinary single-document error. (Sources: https://www.nature.com/articles/s41586-024-07566-y ; https://iep.utm.edu/ep-circ/)

**[inference]** The comparison also touches prompt injection because both prompt injection and corpus contamination depend on a failure to reliably distinguish trusted instructions from untrusted language-shaped inputs. The difference is that prompt injection exploits that failure at inference time, while corpus contamination degrades the evidence and training base over longer horizons. (Sources: https://genai.owasp.org/llmrisk/llm01-prompt-injection/ ; https://arxiv.org/abs/2302.12173)

## Approach

1. Read and summarise Thompson's "Reflections on Trusting Trust" — extract the core logical structure of the self-replicating trust argument.
2. Survey current estimates of AI-generated web content fraction (e.g., recent studies, Common Crawl analyses, industry reports) — what is the current best estimate and what is the projected trajectory?
3. Investigate the "model collapse" and "self-referential training" literature — what happens to models trained on AI-generated data, and does this support the corpus-contamination analogy?
4. Examine the epistemological implications — how do philosophers of knowledge (and practitioners of evidence-based reasoning) characterise the problem of circular or self-referential sources?
5. Explore the relationship to prompt injection — how does corpus-level contamination compare structurally to prompt-level injection as an attack surface?
6. Survey detection approaches and their limitations — why is detecting AI-generated content at the document level insufficient, and is there any corpus-level detection work?
7. Synthesise: what does this mean practically for anyone who relies on web-retrieved information as evidence, including AI agents, researchers, journalists, and knowledge workers?

## Sources

- [x] Ken Thompson, "Reflections on Trusting Trust" (1984) — https://www.cs.cmu.edu/afs/cs/academic/class/15712-f08/www/lectures/Thompson84lecture.pdf
- [x] Shumailov et al., "AI models collapse when trained on recursively generated data" (Nature, 2024) — https://www.nature.com/articles/s41586-024-07566-y
- [x] Gerstgrasser et al., "Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data" (2024) — https://arxiv.org/abs/2404.01413
- [x] Spennemann, "Delving into the quantification of AI-generated content on the internet" (2025) — https://arxiv.org/abs/2504.08755
- [x] Graphite Common Crawl analysis, "More Articles Are Now Created by AI Than Humans" (2025) — https://graphite.io/five-percent/more-articles-are-now-created-by-ai-than-humans
- [x] NewsGuard AI Tracking Center — https://www.newsguardtech.com/special-reports/ai-tracking-center/
- [x] Open Worldwide Application Security Project (OWASP) Large Language Model (LLM)01:2025 Prompt Injection — https://genai.owasp.org/llmrisk/llm01-prompt-injection/
- [x] OWASP LLM04:2025 Data and Model Poisoning — https://genai.owasp.org/llmrisk/llm042025-data-and-model-poisoning/
- [x] Abdelnabi et al., "Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection" (2023) — https://arxiv.org/abs/2302.12173
- [x] Simon Willison, "Model Context Protocol (MCP) prompt injection" (2025) — https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/
- [x] Internet Encyclopedia of Philosophy, "Epistemic Circularity" — https://iep.utm.edu/ep-circ/
- [x] Related completed item: `Research/completed/2026-03-15-prompt-injection-threat-landscape.md`

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

**Research question restated:** What is the web-scale analogue of Ken Thompson's trusting-trust problem once the public web contains large and growing volumes of Artificial Intelligence (AI)-generated text? More specifically: does recursive ingestion of AI-written material create a self-reinforcing integrity problem for future models and for human knowledge verification, and how closely does that problem resemble Thompson's source-invisible compiler contamination?

**Scope confirmed:** In scope are Thompson's original argument, current evidence on how much web text is AI-generated, recursive-training and model-collapse literature, epistemological implications for citation and source checking, the relationship to prompt injection, and the limits of current detection approaches. Out of scope are detailed evaluations of commercial AI detectors, copyright law, and the broader misinformation literature except where it directly bears on provenance and verification.

**Constraints confirmed:** Only public sources are used. Primary sources are preferred for the core logic: Thompson's lecture, peer-reviewed or preprint model-collapse papers, OWASP security guidance, and the philosophy reference on epistemic circularity. Where only secondary or industry evidence exists for web-scale prevalence, that limitation is stated explicitly.

**Output format confirmed:** §§0–7 record the research process. §6 produces the synthesis that is copied into `## Findings` without introducing new claims.

**[inference] Prior work cross-reference:** `Research/completed/2026-03-15-prompt-injection-threat-landscape.md` already established that prompt injection is a structural trust-boundary problem caused by the model's inability to reliably distinguish instructions from untrusted data. That prior item is directly relevant here because corpus contamination is the training-corpus analogue of the same boundary failure, but operating over datasets and provenance chains rather than a single prompt window. (Source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-15-prompt-injection-threat-landscape.md)

### §1 Question Decomposition

**[fact] Root question:** What is the best-supported analogue between Thompson's compiler backdoor argument and the modern web's AI-content feedback loop, and what follows from that analogue for evidence, trust, and defence? (Source: https://www.cs.cmu.edu/afs/cs/academic/class/15712-f08/www/lectures/Thompson84lecture.pdf)

**A. Thompson's original logic**
- A1. What exactly is the security property demonstrated in "Reflections on Trusting Trust"?
- A2. Which part of the argument matters most for analogy: hidden corruption, self-reproduction, or failed source inspection?

**B. Empirical state of web contamination**
- B1. What credible estimates exist for the proportion of web text or articles that are AI-generated?
- B2. Do those estimates support the claim that "roughly half" of web text is AI-generated, or only that the proportion is rapidly increasing?
- B3. What evidence exists that AI-generated sites are proliferating at web scale?

**C. Recursive-training literature**
- C1. What does the model-collapse literature say happens when generative models train on model-generated outputs?
- C2. Is collapse inevitable, or does the answer depend on how synthetic and human data are mixed?
- C3. Does this literature support the trusting-trust analogy or only a weaker systemic-degradation claim?

**D. Epistemology and verification**
- D1. How does epistemic circularity map onto citation chains built from potentially AI-generated sources?
- D2. What changes when sources cite other sources produced by the same generative loop?

**E. Prompt injection and poisoning comparison**
- E1. How is corpus contamination similar to prompt injection?
- E2. How is corpus contamination different from prompt injection and from intentional data poisoning?

**F. Detection and practical implications**
- F1. Why is document-level detection insufficient?
- F2. What practical controls remain available to researchers, journalists, and agent builders?

### §2 Investigation

#### A1-A2. Thompson's original logic

**[fact]** Thompson's lecture demonstrates that a compiler binary can be modified so that it inserts a backdoor into programs it compiles, including future versions of the compiler itself, even when the corresponding source code appears clean. The malicious behavior survives ordinary source inspection because the corruption lives in the toolchain and reproduces through compilation. (Source: https://www.cs.cmu.edu/afs/cs/academic/class/15712-f08/www/lectures/Thompson84lecture.pdf)

**[fact]** The core lesson is not merely that backdoors can be hidden; it is that source-level review is insufficient when the production chain itself is compromised. Trust must extend to the full lineage that produced the artifact. (Source: https://www.cs.cmu.edu/afs/cs/academic/class/15712-f08/www/lectures/Thompson84lecture.pdf)

**[inference]** For analogy purposes, the decisive properties are: hidden contamination upstream of the visible artifact, self-reproduction across generations, and the failure of local inspection to prove integrity. These are the traits that a web-scale AI-content loop would need to share for the trusting-trust comparison to hold. (Source: https://www.cs.cmu.edu/afs/cs/academic/class/15712-f08/www/lectures/Thompson84lecture.pdf)

#### B1-B3. How much web content is AI-generated?

**[fact]** There is no single authoritative census of AI-generated web text. Existing estimates are methodology-dependent and mostly measure either sampled web articles or linguistic markers on active web pages rather than the entire web. (Sources: https://graphite.io/five-percent/more-articles-are-now-created-by-ai-than-humans ; https://arxiv.org/abs/2504.08755)

**[fact]** Graphite's 2025 Common Crawl-based study sampled 65,000 English-language articles and reported that by November 2024 the quantity of AI-generated articles being published on the web had surpassed the quantity of human-written articles in its sample. The study also reports that after twelve months of post-ChatGPT growth, AI-generated articles accounted for nearly 39% of articles published, with later proportions remaining relatively stable rather than continuing exponential growth. (Source: https://graphite.io/five-percent/more-articles-are-now-created-by-ai-than-humans)

**[fact]** Spennemann's 2025 arXiv paper estimates that at least 30% of text on active web pages originates from AI-generated sources, with the actual proportion likely approaching 40%, using linguistic markers associated with ChatGPT-style generation. (Source: https://arxiv.org/abs/2504.08755)

**[fact]** NewsGuard's AI Tracking Center documents that AI-generated pseudo-news and information sites are proliferating at industrial scale, reaching thousands of tracked domains in multiple languages. This is evidence of large-scale synthetic publication even though it is not itself a denominator-based estimate of total web text. (Source: https://www.newsguardtech.com/special-reports/ai-tracking-center/)

**[inference]** The evidence supports a claim of substantial and growing synthetic contamination of the public web, but it does not support a precise universal statement that "roughly half of all text on the web" is AI-generated. A more defensible statement is that some sampled subsets of the web are already near parity, while broader estimates for active web text currently cluster around 30-40% with high measurement uncertainty. (Sources: https://graphite.io/five-percent/more-articles-are-now-created-by-ai-than-humans ; https://arxiv.org/abs/2504.08755 ; https://www.newsguardtech.com/special-reports/ai-tracking-center/)

#### C1-C3. What recursive training does to models

**[fact]** Shumailov et al. define model collapse as a degenerative process in which data generated by earlier generations of models pollute the training set of later generations. In their account, tails of the underlying data distribution disappear first, and repeated recursive training causes learned distributions to converge toward lower-variance, less faithful approximations of the original data. (Source: https://www.nature.com/articles/s41586-024-07566-y)

**[fact]** The Nature paper argues that indiscriminate recursive training causes models to "mis-perceive reality" and that access to real human-produced data becomes increasingly valuable as more model output is published to the internet and then re-ingested. (Source: https://www.nature.com/articles/s41586-024-07566-y)

**[fact]** Gerstgrasser et al. qualify the inevitability claim: if each generation's synthetic data fully replaces original data, collapse tends to occur; if synthetic data accumulate alongside the original real data, collapse can be bounded or avoided in their experiments. (Source: https://arxiv.org/abs/2404.01413)

**[inference]** The recursive-training literature supports the trusting-trust analogy at the level of self-reinforcing contamination and failed local inspection, but not at the level of exact mechanism. Thompson's case is a deliberately inserted backdoor with deterministic malicious persistence; model collapse is usually a systemic integrity failure caused by feedback loops, sampling error, and loss of provenance. (Sources: https://www.cs.cmu.edu/afs/cs/academic/class/15712-f08/www/lectures/Thompson84lecture.pdf ; https://www.nature.com/articles/s41586-024-07566-y ; https://arxiv.org/abs/2404.01413)

**[inference]** The strongest modern analogue is therefore recursive corpus contamination rather than a literal "AI backdoor." The danger is that future models and future readers inherit a polluted evidence base whose defects are hard to detect from any single document. (Sources: https://www.nature.com/articles/s41586-024-07566-y ; https://arxiv.org/abs/2404.01413)

#### D1-D2. Epistemological implications

**[fact]** The Internet Encyclopedia of Philosophy defines epistemic circularity as defending the reliability of a source of belief by relying on premises that are themselves based on that source. The entry notes that such arguments are widely seen as problematic because they are not dialectically effective against someone who doubts the source. (Source: https://iep.utm.edu/ep-circ/)

**[fact]** Alston's track-record example, as summarized in the encyclopedia entry, shows that a source can appear to validate itself when the premises used to prove reliability are already generated through that same source. (Source: https://iep.utm.edu/ep-circ/)

**[inference]** Citation chains built from web pages of uncertain provenance can become epistemically circular in a practical sense when AI-generated page A cites AI-generated page B, which summarizes AI-generated page C, and all three derive from the same synthetic feedback loop. A document may still look well-sourced while failing to provide genuinely independent confirmation. (Sources: https://iep.utm.edu/ep-circ/ ; https://www.nature.com/articles/s41586-024-07566-y)

**[inference]** This does not mean all web citations have become worthless. It means citation now carries less evidential force unless provenance, independence, and source class are checked explicitly. In trusting-trust terms, a clean-looking output no longer licenses confidence in the unseen production chain. (Sources: https://www.cs.cmu.edu/afs/cs/academic/class/15712-f08/www/lectures/Thompson84lecture.pdf ; https://iep.utm.edu/ep-circ/)

#### E1-E2. Relationship to prompt injection and poisoning

**[fact]** OWASP LLM01:2025 defines prompt injection as a vulnerability in which prompts alter model behavior or output in unintended ways, including indirect prompt injection where the model ingests attacker-controlled external content from websites or files. OWASP states that the impact depends heavily on agency and can include disclosure, unauthorized tool use, arbitrary command execution, and manipulated decision making. (Source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/)

**[fact]** Abdelnabi et al. show that LLM-integrated applications blur the boundary between data and instructions, allowing indirect prompt injection via external content that the system later retrieves. They describe impacts including data theft, worming, information-ecosystem contamination, and manipulated Application Programming Interface (API) calls. (Source: https://arxiv.org/abs/2302.12173)

**[fact]** Simon Willison's 2025 Model Context Protocol (MCP) security essay argues that mixing tools, private data, and untrusted instructions is inherently dangerous because the model will trust any convincing tokens it is shown. He treats the problem as unresolved and recommends minimizing blast radius and enforcing human approval. (Source: https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)

**[fact]** OWASP LLM04:2025 defines data poisoning as manipulation of pre-training, fine-tuning, or embedding data to introduce vulnerabilities, backdoors, or bias. It frames poisoning as an integrity attack on training data and distinguishes it from inference-time prompt manipulation. (Source: https://genai.owasp.org/llmrisk/llm042025-data-and-model-poisoning/)

**[inference]** Prompt injection and corpus contamination share the same deep structural problem: the system cannot reliably separate trusted instructions from untrusted language-shaped inputs. The difference is timing and persistence. Prompt injection exploits that weakness at inference time in a local context window; corpus contamination exploits or suffers from it at collection and training time across the whole evidence base. (Sources: https://genai.owasp.org/llmrisk/llm01-prompt-injection/ ; https://arxiv.org/abs/2302.12173 ; https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/ ; https://genai.owasp.org/llmrisk/llm042025-data-and-model-poisoning/)

**[inference]** Intentional data poisoning is the closer security cousin to Thompson's original attack because both involve adversarial manipulation of upstream artifacts. Recursive corpus contamination is broader: it includes adversarial poisoning but also non-malicious synthetic saturation that still degrades reliability and provenance. (Sources: https://genai.owasp.org/llmrisk/llm042025-data-and-model-poisoning/ ; https://www.cs.cmu.edu/afs/cs/academic/class/15712-f08/www/lectures/Thompson84lecture.pdf ; https://www.nature.com/articles/s41586-024-07566-y)

#### F1-F2. Detection limits and practical consequences

**[fact]** Graphite's article prevalence estimate depends on an AI-detection pipeline and explicitly notes limitations around human-edited AI text and future model changes. Spennemann's estimate depends on linguistic markers associated with a particular generation style. Both methods are informative but imperfect. (Sources: https://graphite.io/five-percent/more-articles-are-now-created-by-ai-than-humans ; https://arxiv.org/abs/2504.08755)

**[fact]** OWASP's prompt-injection guidance does not present foolproof prevention. Instead it recommends blast-radius reduction measures such as least privilege, explicit segregation of untrusted content, deterministic validation, and human approval for high-risk actions. (Source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/)

**[inference]** Document-level AI detection is insufficient for the trusting-trust-style problem because even perfect identification of one synthetic document would not prove the cleanliness of the broader corpus, the retrieval chain, or the upstream training distribution. The epistemic problem is provenance and independence, not merely document authorship. (Sources: https://graphite.io/five-percent/more-articles-are-now-created-by-ai-than-humans ; https://arxiv.org/abs/2504.08755 ; https://iep.utm.edu/ep-circ/)

**[inference]** The practical response is to move from content inspection to chain-of-custody inspection: prefer primary sources, require source-type diversity, record provenance, treat web text as untrusted by default when it is used for model grounding, and preserve protected reservoirs of human-generated or otherwise verified data. (Sources: https://www.cs.cmu.edu/afs/cs/academic/class/15712-f08/www/lectures/Thompson84lecture.pdf ; https://www.nature.com/articles/s41586-024-07566-y ; https://genai.owasp.org/llmrisk/llm01-prompt-injection/)

### §3 Reasoning

**[fact]** Thompson proves that upstream corruption can persist invisibly across generations of artifacts. (Source: https://www.cs.cmu.edu/afs/cs/academic/class/15712-f08/www/lectures/Thompson84lecture.pdf)

**[fact]** Recursive-training research shows that model-generated outputs can pollute later training data and erase low-frequency information. (Sources: https://www.nature.com/articles/s41586-024-07566-y ; https://arxiv.org/abs/2404.01413)

**[fact]** Current prevalence studies indicate substantial synthetic content on the web, but not a precise settled value for the whole web. (Sources: https://graphite.io/five-percent/more-articles-are-now-created-by-ai-than-humans ; https://arxiv.org/abs/2504.08755)

**[fact]** Epistemic circularity explains why a source cannot straightforwardly certify its own reliability. (Source: https://iep.utm.edu/ep-circ/)

**[fact]** Prompt injection and data poisoning guidance both frame AI security as a trust-boundary problem involving untrusted inputs. (Sources: https://genai.owasp.org/llmrisk/llm01-prompt-injection/ ; https://genai.owasp.org/llmrisk/llm042025-data-and-model-poisoning/ ; https://arxiv.org/abs/2302.12173)

**[inference]** Combining those facts yields a bounded conclusion: the web-scale analogue of trusting trust is recursive corpus contamination, a condition in which synthetic outputs pollute the evidence and training chain so that local inspection and ordinary citation practice no longer suffice to prove independence or integrity.

**[inference]** The analogy is structurally strong but not exact. Thompson's attack is adversarial and deterministic; corpus contamination can be accidental, gradual, and statistical. The right lesson is therefore about integrity verification and provenance, not about treating every synthetic page as a deliberate backdoor.

**[assumption]** When this item speaks of "human-generated" data as the cleaner reference class, it assumes that provenance-verified human material remains more diverse and less recursively self-referential than heavily synthetic corpora. This assumption follows the framing in the Nature paper but is not itself proven here across all domains. (Source for justification: https://www.nature.com/articles/s41586-024-07566-y)

### §4 Consistency Check

**[fact]** The main numerical tension in the evidence base is between near-parity findings for sampled article publication and lower estimates for active web-page text. This is not a contradiction once the measurement targets are distinguished: one study examines sampled English-language articles with a detector, while the other estimates AI markers across active web pages. (Sources: https://graphite.io/five-percent/more-articles-are-now-created-by-ai-than-humans ; https://arxiv.org/abs/2504.08755)

**[fact]** The model-collapse literature contains an apparent tension between "collapse is inevitable" and "collapse can be avoided." This resolves once the training regime is specified: Shumailov et al. study indiscriminate recursion, while Gerstgrasser et al. show that retaining original real data changes the outcome materially. (Sources: https://www.nature.com/articles/s41586-024-07566-y ; https://arxiv.org/abs/2404.01413)

**[inference]** The final conclusion should therefore avoid overclaiming in two places: it should not assert a settled global fraction for AI-generated web text, and it should not claim that any synthetic-data exposure automatically produces catastrophic model collapse. The supported claim is narrower: contamination pressure is already large enough that provenance and independence have become first-order concerns.

### §5 Depth and Breadth Expansion

**Technical lens**

**[fact]** The training pipeline implication of the Nature paper is that preserving access to original data distributions matters most where rare events and tail behaviors matter. Losing tails is not a cosmetic problem; it changes what the model can represent. (Source: https://www.nature.com/articles/s41586-024-07566-y)

**[inference]** For retrieval systems and agentic systems, the same lesson applies at inference time: if grounded answers are drawn from a corpus already saturated with synthetic paraphrases of synthetic paraphrases, retrieval quality can degrade even when each retrieved document looks fluent.

**Security lens**

**[fact]** OWASP's guidance treats both prompt injection and poisoning as integrity problems requiring least privilege, segregation of untrusted data, and human review for sensitive actions. (Sources: https://genai.owasp.org/llmrisk/llm01-prompt-injection/ ; https://genai.owasp.org/llmrisk/llm042025-data-and-model-poisoning/)

**[inference]** Trusting-trust logic suggests that AI assurance should shift from "did the answer look plausible?" to "what lineage produced the answer, what sources were independent, and where could contamination have entered?"

**Economic and platform lens**

**[fact]** NewsGuard's tracking of thousands of AI-generated content farms indicates that synthetic publication is commercially organized, not merely incidental hobbyist output. (Source: https://www.newsguardtech.com/special-reports/ai-tracking-center/)

**[inference]** Once synthetic publishing is industrialized, the incentives point toward quantity and search capture rather than durable knowledge quality. That makes provenance controls a market-structure issue as much as a model-quality issue.

**Behavioral and epistemic lens**

**[fact]** The epistemic circularity literature emphasizes that a source cannot easily answer a challenge to its own reliability by appealing only to outputs derived from itself. (Source: https://iep.utm.edu/ep-circ/)

**[inference]** Human readers and AI systems now face a similar practical discipline problem: source-checking that stops at "three websites agree" is weaker than it once was if those sites share a synthetic lineage or common generated summaries.

### §6 Synthesis

**Executive summary:**

The strongest web-scale analogue of Thompson's trusting-trust attack is recursive corpus contamination: AI-generated text is now abundant enough that later models and human researchers increasingly learn from a corpus partly composed of prior model outputs, making local source inspection an unreliable proof of underlying integrity. The best current evidence does **not** prove that half of all web text is AI-generated, but it does show near-parity in some sampled article sets and broader active-web estimates around 30-40%, which is already large enough to make provenance a first-order problem. Model-collapse research supports the structural core of the analogy by showing that recursive training on generated data can erase rare information and distort later generations, although the severity depends on whether original human data are preserved. The epistemic consequence is that citation alone is no longer enough: independence, source class, and chain of custody matter more than fluent agreement across multiple webpages.

**Key findings:**

1. The closest modern analogue to Thompson's compiler attack is **recursive corpus contamination**, because the key shared property is upstream contamination that reproduces across generations while remaining largely invisible in any single downstream artifact. Confidence: high.
2. Current evidence supports a claim of **substantial synthetic saturation of the public web**, but not a settled universal claim that half of all web text is AI-generated; the best-supported range from accessible sources is roughly 30-40% for active web-page text, with some article-sample studies already near parity. Confidence: medium.
3. The model-collapse literature shows that recursive training on generated data can cause later models to lose low-frequency or tail information first, which makes the trusting-trust analogy materially stronger than a metaphor about "too much spam" because it changes what successor models can know. Confidence: high.
4. Recursive contamination is **not identical** to Thompson's original attack because it is often systemic and non-adversarial rather than a deliberately implanted backdoor, so the right comparison is to an integrity failure in the production chain rather than to a single hidden exploit. Confidence: high.
5. Epistemologically, the main damage is not that every AI-generated source is false, but that ordinary citation chains can become practically **epistemically circular** when apparently independent pages are all descended from the same generative loop. Confidence: high.
6. Prompt injection and corpus contamination share a common trust-boundary failure — the inability to reliably separate trusted instructions from untrusted language-shaped inputs — but they operate at different layers: prompt injection is an inference-time exploit, while corpus contamination is a training-data and evidence-base integrity problem. Confidence: high.
7. Document-level AI detection is insufficient as a defence because even accurate identification of one synthetic page does not establish the cleanliness, independence, or provenance of the larger retrieval chain or training corpus that produced a claim. Confidence: high.
8. The most practical defensive response is to treat web text more like a software supply chain artifact: preserve trusted primary-data reservoirs, record provenance, demand source-type diversity, and use human review for high-stakes conclusions or actions grounded in open-web material. Confidence: high.

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Thompson's trusting-trust logic is about source-invisible upstream corruption that reproduces across generations. | https://www.cs.cmu.edu/afs/cs/academic/class/15712-f08/www/lectures/Thompson84lecture.pdf | high | Primary source for the analogy anchor. |
| Sampled English-language web articles reached near parity between AI-generated and human-written publication in Graphite's study. | https://graphite.io/five-percent/more-articles-are-now-created-by-ai-than-humans | medium | Industry study using detector-based sampling; useful but not definitive for the whole web. |
| At least 30% of active web-page text is AI-generated, with the true proportion likely approaching 40%, in Spennemann's estimate. | https://arxiv.org/abs/2504.08755 | medium | Preprint using linguistic markers; broad estimate with methodological caveats. |
| Recursive training on generated data can produce model collapse and erase tail information. | https://www.nature.com/articles/s41586-024-07566-y | high | Primary peer-reviewed source. |
| Collapse severity depends on whether original real data are replaced or retained alongside synthetic data. | https://arxiv.org/abs/2404.01413 | high | Important qualifier to the inevitability claim. |
| Epistemic circularity explains why a source cannot straightforwardly certify its own reliability from its own outputs. | https://iep.utm.edu/ep-circ/ | high | Conceptual bridge for the verification problem. |
| Prompt injection exploits the same data/instruction boundary failure at inference time. | https://genai.owasp.org/llmrisk/llm01-prompt-injection/ ; https://arxiv.org/abs/2302.12173 ; https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/ | high | Multiple independent security sources agree. |
| Data poisoning is a distinct but related integrity attack on pre-training and fine-tuning data. | https://genai.owasp.org/llmrisk/llm042025-data-and-model-poisoning/ | high | Helps distinguish adversarial poisoning from broader contamination. |
| AI-generated pseudo-news publication has scaled to thousands of tracked domains. | https://www.newsguardtech.com/special-reports/ai-tracking-center/ | medium | Strong evidence of proliferation, but not a denominator-based prevalence estimate. |

**Assumptions:**

- **Assumption:** Provenance-verified human-generated data are generally less recursively self-referential than heavily synthetic corpora. **Justification:** This is the operational premise behind the Nature paper's warning that access to real human-produced data becomes increasingly valuable as recursive training pressure rises. (Source: https://www.nature.com/articles/s41586-024-07566-y)
- **Assumption:** The sampled article and active-web-page studies are directionally informative even though neither is a full-web census. **Justification:** They use different methods and still converge on the conclusion that synthetic content is already a large share of publicly available text. (Sources: https://graphite.io/five-percent/more-articles-are-now-created-by-ai-than-humans ; https://arxiv.org/abs/2504.08755)

**Analysis:**

The evidence weighs most strongly on structure, less strongly on exact magnitude. Thompson gives a clean primary-source template for a trusting-trust problem: integrity fails upstream, and visible outputs can look clean. The recursive-training papers then supply the modern analogue by showing that generated outputs can feed back into later generations and distort what they learn. The prevalence studies are weaker because web-scale measurement is hard and detector-based methods are imperfect, but they are strong enough to establish that the contamination pressure is no longer hypothetical. The epistemology source helps explain why "multiple webpages agree" is now a weaker test than source-type independence or primary-source anchoring. Competing interpretations were resolved by narrowing the conclusion: this item does **not** claim that all AI-generated content is false or that model collapse is inevitable in every pipeline; it claims that provenance and independence have become central integrity questions.

**Risks, gaps, uncertainties:**

- There is no authoritative denominator-based measurement for the entire web, so any global proportion remains uncertain.
- Both accessible prevalence estimates rely on imperfect proxies: detectors in one case and linguistic markers in the other.
- This item does not quantify how often real production models are already training on synthetic-heavy corpora with enough contamination to trigger measurable degradation.
- The epistemic circularity analogy is conceptually strong but still a philosophical mapping, not a formal theorem about web citations.
- The boundary between benign synthetic assistance and harmful recursive contamination remains operationally fuzzy in mixed human-AI authoring workflows.

**Open questions:**

- What provenance architecture would make open-web sources usable again for high-stakes agent grounding without requiring full manual vetting?
- How much trusted human-generated data is enough to prevent meaningful collapse in modern frontier-model training pipelines?
- Can web-scale retrieval systems estimate source independence rather than only relevance and popularity?
- Does industrial AI-content publishing create measurable distortions in search ranking and citation graphs beyond the raw volume increase?

### §7 Recursive Review

**[fact]** Every major claim in §§2–6 is either sourced directly or marked as an inference or assumption.

**[fact]** The main unsupported temptation identified during review was the phrase "roughly half of all text on the web." That claim was downgraded because the accessible evidence supports only substantial contamination with uncertain total magnitude. (Sources: https://graphite.io/five-percent/more-articles-are-now-created-by-ai-than-humans ; https://arxiv.org/abs/2504.08755)

**[fact]** Acronyms expanded on first use in the document include Artificial Intelligence (AI), Large Language Model (LLM), Application Programming Interface (API), Model Context Protocol (MCP), and Open Worldwide Application Security Project (OWASP). The findings section introduces no new unexpanded abbreviations.

**[inference]** The remaining uncertainty is mostly quantitative rather than structural. The conclusion that provenance has become a first-order concern is well supported even though the exact synthetic share of the web remains unsettled.

---

## Findings

### Executive Summary

**[inference]** The public web now behaves less like a neutral evidence commons and more like a partially recursive corpus whose provenance cannot be validated by reading any single page in isolation. (Sources: https://graphite.io/five-percent/more-articles-are-now-created-by-ai-than-humans ; https://arxiv.org/abs/2504.08755 ; https://www.nature.com/articles/s41586-024-07566-y)

**[inference]** Thompson's trusting-trust argument is therefore best applied here as a warning about recursive corpus contamination rather than as a claim that the web contains a literal compiler-style backdoor. Later models and later readers increasingly consume outputs partly produced by earlier models, which weakens local source inspection as a test of independence. (Sources: https://www.cs.cmu.edu/afs/cs/academic/class/15712-f08/www/lectures/Thompson84lecture.pdf ; https://www.nature.com/articles/s41586-024-07566-y ; https://arxiv.org/abs/2404.01413)

**[fact]** The best accessible prevalence evidence does not establish that half of all web text is AI-generated, but it does support a large current share, with active-web estimates around 30-40% and some sampled article sets already near parity. (Sources: https://graphite.io/five-percent/more-articles-are-now-created-by-ai-than-humans ; https://arxiv.org/abs/2504.08755)

**[inference]** The practical result is epistemic as well as technical: citation and agreement remain useful, but they now carry more weight when they demonstrate provenance and source independence rather than repeated fluency across webpages. (Sources: https://iep.utm.edu/ep-circ/ ; https://www.cs.cmu.edu/afs/cs/academic/class/15712-f08/www/lectures/Thompson84lecture.pdf)

### Key Findings

1. **[inference]** Thompson's trusting-trust argument maps most closely to recursive corpus contamination because both involve upstream corruption that reproduces across generations while remaining largely invisible when a reviewer inspects only the final visible artifact. **Confidence:** high. (Sources: https://www.cs.cmu.edu/afs/cs/academic/class/15712-f08/www/lectures/Thompson84lecture.pdf ; https://www.nature.com/articles/s41586-024-07566-y)
2. **[fact]** The strongest publicly accessible prevalence evidence shows that AI-generated text is already a large share of the public web, but the underlying studies support a bounded range rather than a settled claim that half of all web text is synthetic. **Confidence:** medium. (Sources: https://graphite.io/five-percent/more-articles-are-now-created-by-ai-than-humans ; https://arxiv.org/abs/2504.08755)
3. **[fact]** Shumailov and colleagues show that recursive training on generated data causes models to lose tail information and drift away from the original data distribution, which means corpus contamination can alter what future systems are capable of representing, not just what they happen to retrieve. **Confidence:** high. (Source: https://www.nature.com/articles/s41586-024-07566-y)
4. **[fact]** Gerstgrasser and colleagues show that recursive contamination is not mechanically inevitable under every data regime, because retaining original real data alongside synthetic data materially changes the outcome and can bound collapse in their experiments. **Confidence:** high. (Source: https://arxiv.org/abs/2404.01413)
5. **[inference]** The epistemic danger is that apparently independent webpages can become practically circular evidence when they are all descended from the same generative loop, so citation count and fluent agreement stop being reliable proxies for independent confirmation. **Confidence:** high. (Sources: https://iep.utm.edu/ep-circ/ ; https://www.nature.com/articles/s41586-024-07566-y)
6. **[inference]** Prompt injection and corpus contamination are structurally related because both exploit the model's inability to distinguish trusted instructions from untrusted language-shaped inputs, but prompt injection acts at inference time while corpus contamination degrades the evidence and training base over longer horizons. **Confidence:** high. (Sources: https://genai.owasp.org/llmrisk/llm01-prompt-injection/ ; https://arxiv.org/abs/2302.12173 ; https://genai.owasp.org/llmrisk/llm042025-data-and-model-poisoning/)
7. **[inference]** Document-level AI detection cannot solve the trusting-trust-style problem because detecting one synthetic page does not reveal whether the broader corpus, retrieval chain, or training lineage behind a claim is independent and trustworthy. **Confidence:** high. (Sources: https://graphite.io/five-percent/more-articles-are-now-created-by-ai-than-humans ; https://arxiv.org/abs/2504.08755 ; https://iep.utm.edu/ep-circ/)
8. **[inference]** The most defensible practical response is to treat open-web knowledge more like a software supply chain by preferring primary sources, preserving trusted human-generated data reservoirs, recording provenance, and requiring stronger human review for high-stakes grounded outputs. **Confidence:** high. (Sources: https://www.cs.cmu.edu/afs/cs/academic/class/15712-f08/www/lectures/Thompson84lecture.pdf ; https://www.nature.com/articles/s41586-024-07566-y ; https://genai.owasp.org/llmrisk/llm01-prompt-injection/)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Thompson's trusting-trust argument depends on source-invisible upstream corruption that reproduces across generations. | https://www.cs.cmu.edu/afs/cs/academic/class/15712-f08/www/lectures/Thompson84lecture.pdf | high | Primary source; defines the analogy. |
| AI-generated article publication reached near parity in Graphite's Common Crawl sample. | https://graphite.io/five-percent/more-articles-are-now-created-by-ai-than-humans | medium | Detector-based industry study of English-language articles. |
| At least 30% of text on active web pages is AI-generated, with the proportion likely approaching 40%, in Spennemann's estimate. | https://arxiv.org/abs/2504.08755 | medium | Preprint based on linguistic markers. |
| Recursive training on generated data causes model collapse and loss of tails in the original distribution. | https://www.nature.com/articles/s41586-024-07566-y | high | Primary peer-reviewed evidence. |
| Accumulating real and synthetic data changes the collapse outcome materially. | https://arxiv.org/abs/2404.01413 | high | Important bound on the stronger collapse claim. |
| Epistemic circularity explains why source reliability cannot be established by outputs that already depend on that source. | https://iep.utm.edu/ep-circ/ | high | Conceptual basis for the citation problem. |
| Prompt injection is an inference-time trust-boundary failure involving untrusted external content. | https://genai.owasp.org/llmrisk/llm01-prompt-injection/ ; https://arxiv.org/abs/2302.12173 | high | Security framing supported by primary guidance and foundational paper. |
| Data poisoning is a related upstream integrity attack on training and fine-tuning data. | https://genai.owasp.org/llmrisk/llm042025-data-and-model-poisoning/ | high | Distinguishes adversarial poisoning from broader contamination. |
| AI-generated pseudo-news sites now exist at industrial scale across many languages. | https://www.newsguardtech.com/special-reports/ai-tracking-center/ | medium | Strong proliferation evidence; not a total-share estimate. |

### Assumptions

- **[assumption] Assumption:** Provenance-verified human-generated data remain a cleaner reference class than heavily synthetic corpora for preventing recursive degradation. **Justification:** The Nature paper explicitly argues that access to real human-produced data becomes increasingly valuable as generated content pollutes the internet. **Source:** https://www.nature.com/articles/s41586-024-07566-y
- **[assumption] Assumption:** The article-sample and active-page prevalence studies are sufficiently independent to justify a directional conclusion about substantial contamination. **Justification:** They use different methods and still converge on a large synthetic share rather than a trivial one. **Sources:** https://graphite.io/five-percent/more-articles-are-now-created-by-ai-than-humans ; https://arxiv.org/abs/2504.08755

### Analysis

**[inference]** The structural part of the case is stronger than the quantitative part because the Thompson lecture and the recursive-training papers independently support the claim that integrity can fail upstream while downstream outputs remain superficially coherent. (Sources: https://www.cs.cmu.edu/afs/cs/academic/class/15712-f08/www/lectures/Thompson84lecture.pdf ; https://www.nature.com/articles/s41586-024-07566-y ; https://arxiv.org/abs/2404.01413)

**[inference]** The prevalence evidence is less certain because there is no authoritative whole-web census, but the accessible studies and NewsGuard's tracking still show that contamination pressure is already large enough to matter operationally for research and grounding workflows. (Sources: https://graphite.io/five-percent/more-articles-are-now-created-by-ai-than-humans ; https://arxiv.org/abs/2504.08755 ; https://www.newsguardtech.com/special-reports/ai-tracking-center/)

**[inference]** The security material helps separate layers of the problem: prompt injection is the short-horizon exploit form of a broader trust-boundary failure, while corpus contamination is the long-horizon evidence-base form. That distinction is why provenance review and primary-source preference are more useful controls here than document-level authorship checks alone. (Sources: https://genai.owasp.org/llmrisk/llm01-prompt-injection/ ; https://arxiv.org/abs/2302.12173 ; https://genai.owasp.org/llmrisk/llm042025-data-and-model-poisoning/)

### Risks, Gaps, and Uncertainties

- No public source in this review provides a definitive whole-web percentage for AI-generated text.
- The accessible prevalence studies depend on imperfect detection or marker methods.
- This item does not establish how much contamination current frontier-model pipelines actually tolerate before performance degrades materially.
- Mixed human-AI authorship complicates binary categories such as "human" versus "AI-generated."
- The philosophical mapping from epistemic circularity to citation practice is strong but not mathematically formalized here.

### Open Questions

- What provenance standards would let Retrieval-Augmented Generation (RAG) systems rely on open-web material without inheriting circular evidence loops?
- Can search and retrieval systems rank source independence and provenance quality, not just relevance and authority signals?
- How quickly are synthetic-content farms reshaping citation graphs, search results, and future training corpora in practice?
- What minimum reservoir of verified human-generated data is needed to keep recursive training from erasing tail knowledge in large production systems?

---

## Output

- Type: knowledge
- Description: A structured research synthesis arguing that recursive corpus contamination is the web-scale trusting-trust analogue for AI-generated content, with explicit limits on current prevalence claims and practical implications for provenance and verification.
- Links:
  - https://www.cs.cmu.edu/afs/cs/academic/class/15712-f08/www/lectures/Thompson84lecture.pdf
  - https://www.nature.com/articles/s41586-024-07566-y
  - https://arxiv.org/abs/2504.08755