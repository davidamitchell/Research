---
title: "Hardware load and Large Language Model (LLM) inference performance: implications for agent reliability"
added: 2026-05-12T03:27:57+00:00
status: reviewing
priority: medium  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [llm, agentic-ai, evaluation, ai-platform]
started: 2026-05-12T18:38:07+00:00
completed: ~
output: [knowledge]  # skill | tool | agent | knowledge | backlog-item
cites:
  - 2026-05-09-llm-determinism-limits-temperature-zero
  - 2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring
related:
  - 2026-04-26-ai-governance-cost-performance-delivery-impact
  - 2026-05-08-integrated-cascading-failure-agentic-vs-generative-ai-risk
  - 2026-05-09-governance-policy-determinism-vs-stochastic-llm
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# Hardware load and Large Language Model (LLM) inference performance: implications for agent reliability

## Research Question

How does hardware resource load, Central Processing Unit (CPU), Graphics Processing Unit (GPU), and memory pressure, affect Large Language Model (LLM) inference performance, specifically latency, throughput, and output quality consistency, and what are the practical implications for Artificial Intelligence (AI) agent reliability in production deployments?

## Scope

**In scope:**
- GPU and CPU utilisation effects on LLM inference latency and throughput
- Hardware memory pressure, GPU Video Random Access Memory (VRAM) contention and CPU Random Access Memory (RAM) pressure, and its effect on inference output quality and token sampling consistency
- Behaviour of inference serving systems, vLLM, Text Generation Inference (TGI), Ollama, and llama.cpp, under resource contention
- Empirical benchmarks and published measurements of LLM inference performance variance under load
- Practical implications for AI agent orchestration, including whether load-dependent performance variability requires architectural mitigations

**Out of scope:**
- Model training performance and hardware requirements
- Non-LLM inference, classical Machine Learning (ML), computer vision, and similar workloads
- Cloud provider pricing models and Service Level Agreement (SLA) comparisons
- Specific vendor hardware benchmarks unrelated to load contention

**Constraints:** Focus on self-hosted and cloud LLM inference; academic papers, inference serving documentation, and practitioner benchmarks are all valid source types; no specific time horizon.

## Context

Shared-serving stacks already expose queueing, batching, and memory-management controls because LLM inference performance changes materially when concurrent demand alters batch shape, key-value (KV) cache pressure, meaning the serving-time memory used to store prior token states, or model placement across CPU and GPU memory. [fact; source: https://docs.vllm.ai/en/latest/configuration/optimization/; https://huggingface.co/docs/text-generation-inference/main/en/architecture; https://docs.ollama.com/faq; https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md]

For agent reliability, meaning whether a production agent stays inside its response-time and decision-stability envelope, those infrastructure effects matter because multi-step workflows amplify latency tails, retries, and occasional token-level drift into larger orchestration failures. [inference; source: https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring.html; https://davidamitchell.github.io/Research/research/2026-05-08-integrated-cascading-failure-agentic-vs-generative-ai-risk.html; https://davidamitchell.github.io/Research/research/2026-05-09-llm-determinism-limits-temperature-zero.html]

## Approach

1. What is the relationship between GPU utilisation level and LLM inference latency and throughput? Are these degradation curves linear, step-function, or threshold-based?
2. Does hardware memory pressure, GPU VRAM saturation and CPU RAM pressure, affect LLM output quality, token sampling distribution, or consistency of outputs beyond just speed?
3. How do inference serving systems, vLLM, TGI, Ollama, and llama.cpp, handle resource contention, and what degradation modes, queueing behaviours, and failure modes exist under load?
4. Are there published empirical benchmarks measuring LLM inference performance variance under load, and what do they show?
5. What are the practical implications for AI agent orchestration, and does load-dependent variability require architectural mitigations such as request routing, load shedding, or quality monitoring?

## Sources

- [x] [vLLM OpenAI-Compatible Server](https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html)
- [x] [vLLM Optimization and Tuning](https://docs.vllm.ai/en/latest/configuration/optimization/)
- [x] [vLLM Frequently Asked Questions](https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html)
- [x] [Hugging Face Text Generation Inference](https://huggingface.co/docs/text-generation-inference/en/index)
- [x] [Hugging Face Text Generation Inference Architecture](https://huggingface.co/docs/text-generation-inference/main/en/architecture)
- [x] [Kwon et al. (2023) Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180)
- [x] [Agrawal et al. (2024) Taming Throughput-Latency Tradeoff in Large Language Model Inference with Sarathi-Serve](https://arxiv.org/abs/2403.02310)
- [x] [Yuan et al. (2025) Understanding and Mitigating Numerical Sources of Nondeterminism in Large Language Model Inference](https://arxiv.org/abs/2506.09501)
- [x] [Vellaisamy et al. (2025) Characterizing and Optimizing Large Language Model Inference Workloads on CPU-GPU Coupled Architectures](https://arxiv.org/abs/2504.11750)
- [x] [Thinking Machines Lab (2025) Defeating nondeterminism in Large Language Model inference](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/)
- [x] [Ollama Frequently Asked Questions](https://docs.ollama.com/faq)
- [x] [Ollama envconfig/config.go](https://github.com/ollama/ollama/blob/main/envconfig/config.go)
- [x] [ggml-org llama.cpp HTTP Server README](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)
- [x] [ggml-org llama-bench README](https://github.com/ggml-org/llama.cpp/tree/master/tools/llama-bench)

## Related

- [Mitchell (2026) Practical Limits of Large Language Model (LLM) Determinism: Temperature Zero, Fixed Seeds, and Constrained Prompts](https://davidamitchell.github.io/Research/research/2026-05-09-llm-determinism-limits-temperature-zero.html)
- [Mitchell (2026) Universal Entity Lifecycle Governance Framework (UELGF) extension: agentic Artificial Intelligence (AI)-specific risks and runtime monitoring for non-deterministic behaviour](https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring.html)
- [Mitchell (2026) What is the cost, performance, and delivery impact of governance controls on AI and low-code development?](https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-cost-performance-delivery-impact.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0 to 5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: how does hardware resource load affect LLM inference latency, throughput, and output consistency, and what does that imply for production agent reliability?
- Scope: GPU and CPU contention, memory pressure, serving-system behavior, empirical performance variance, and practical deployment mitigations.
- Constraints: self-hosted and cloud inference only, official documentation and research papers first, practitioner material only where it sharpens an implementation detail not covered by a primary source.
- Output: knowledge.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-09-llm-determinism-limits-temperature-zero.html; https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-cost-performance-delivery-impact.html] Prior completed items in this repository already establish that serving-path changes can affect output stability, that runtime monitoring must watch precursor signals rather than only end failures, and that governance should be assessed against delivery performance, so this item focuses on the underlying hardware and serving mechanisms behind those conclusions.

### §1 Question Decomposition

- **Root question:** which hardware-load mechanisms materially change LLM serving behavior, and which of those changes matter for agent reliability rather than only for raw benchmark speed?
- **A. Latency and throughput under load**
  - A1. Which parts of inference are GPU-compute-bound, memory-bandwidth-bound, or CPU-coordination-bound?
  - A2. Are latency and throughput trade-offs linear, or do they shift when batching and scheduling policies cross thresholds?
- **B. Memory pressure and output consistency**
  - B1. What happens when KV cache space or VRAM headroom becomes insufficient?
  - B2. Does memory-saving or batch-changing behavior alter output tokens, not only response time?
- **C. Serving-system contention handling**
  - C1. How does vLLM handle concurrent load and memory contention?
  - C2. How does TGI handle request buffering, batching, and concurrency caps?
  - C3. How do Ollama and llama.cpp expose queueing, parallelism, and memory controls?
- **D. Empirical benchmark evidence**
  - D1. What measured throughput and latency gains or losses are reported under different scheduling and memory-management designs?
  - D2. What measured output-variance evidence exists when batch size, GPU count, or precision changes?
- **E. Reliability synthesis**
  - E1. Which load signals should production agents treat as reliability signals?
  - E2. Which mitigations are justified directly by the evidence?

### §2 Investigation

#### A. Latency and throughput under load are mainly scheduler- and threshold-driven

- [fact; source: https://arxiv.org/abs/2403.02310] Agrawal et al. say each LLM serving request has a prompt-processing prefill phase, which processes the full prompt before the first generated token, and a token-by-token decode phase, which generates later tokens one at a time, which makes batching valuable for throughput but risky for latency if the phases are mixed poorly.
- [fact; source: https://docs.vllm.ai/en/latest/configuration/optimization/] vLLM says chunked prefill is enabled by default where possible, prioritizes decode requests ahead of prefills, and lets operators trade inter-token latency (ITL), time to first token (TTFT), and throughput by changing `max_num_batched_tokens`.
- [fact; source: https://huggingface.co/docs/text-generation-inference/main/en/architecture] TGI says its router buffers requests, applies queues and schedulers, and exposes explicit router controls such as `--max-concurrent-requests`, `--max-batch-prefill-tokens`, `--max-batch-total-tokens`, and `--waiting-served-ratio`.
- [fact; source: https://arxiv.org/abs/2403.02310] Agrawal et al. report that Sarathi-Serve improves serving capacity by 2.6 times for Mistral-7B on one A100 GPU, up to 3.7 times for Yi-34B on two A100 GPUs, and up to 5.6 times for Falcon-180B with pipeline parallelism under tail-latency constraints.
- [inference; source: https://arxiv.org/abs/2403.02310; https://docs.vllm.ai/en/latest/configuration/optimization/; https://huggingface.co/docs/text-generation-inference/main/en/architecture] The degradation curve under load is therefore best understood as threshold-based and scheduler-mediated rather than as a smooth percentage-of-utilization slowdown, because the dominant transitions appear when batch composition, token budgets, and queueing policy change.

#### B. Memory pressure is a first-order performance bottleneck, and can also change output stability when it changes the numerical path

- [fact; source: https://arxiv.org/abs/2309.06180] Kwon et al. say KV cache memory for each request is large and dynamic, that poor management wastes memory through fragmentation and duplication, and that vLLM's PagedAttention achieves near-zero KV-cache waste and 2 to 4 times higher throughput at the same latency than prior serving systems.
- [fact; source: https://docs.vllm.ai/en/latest/configuration/optimization/] vLLM says that when KV cache space is insufficient for all batched requests, the system preempts requests and recomputes them later, which preserves robustness but harms end-to-end latency.
- [fact; source: https://docs.vllm.ai/en/latest/configuration/optimization/] vLLM recommends increasing `gpu_memory_utilization`, reducing `max_num_seqs` or `max_num_batched_tokens`, or increasing tensor or pipeline parallelism to leave more memory for KV cache, while warning that more parallelism can introduce synchronization or latency penalties.
- [fact; source: https://docs.ollama.com/faq] Ollama says parallel request processing increases required memory in proportion to `OLLAMA_NUM_PARALLEL * OLLAMA_CONTEXT_LENGTH`, requires new models to fit entirely in VRAM for concurrent model loads on GPU inference, and queues new requests when memory is insufficient.
- [fact; source: https://docs.ollama.com/faq] Ollama says quantizing the KV cache to `q8_0` roughly halves memory relative to `f16`, while `q4_0` uses about one quarter of the memory with a small-to-medium precision loss that can become more noticeable at higher context sizes.
- [fact; source: https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html] vLLM says identical prompts can produce different outputs when batching changes, because different concurrent traffic or speculative-decoding batch expansion changes log probabilities slightly and those differences can accumulate into different sampled tokens.
- [fact; source: https://arxiv.org/abs/2506.09501] Yuan et al. report that changing evaluation batch size, GPU count, or GPU version can produce up to 9 percent accuracy variation and 9,000 tokens of response-length difference under greedy decoding, especially in reasoning models under limited precision.
- [fact; source: https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/] Thinking Machines Lab says practical inference nondeterminism mainly appears when batch size or sequence context changes numerical accumulation order, and that fixed configuration on one device can be deterministic even though production serving rarely keeps that fixed.
- [inference; source: https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html; https://arxiv.org/abs/2506.09501; https://docs.ollama.com/faq; https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/] In the consulted sources, output-consistency evidence comes from memory-saving modes, changed batch composition, and changed hardware or precision paths that alter logits enough to change sampled tokens or downstream task accuracy.

#### C. CPU load remains relevant even in GPU-heavy inference stacks

- [fact; source: https://arxiv.org/abs/2504.11750] Vellaisamy et al. report that a Grace Hopper 200 (GH200) closely coupled CPU-GPU system outperforms loosely coupled systems at large batch sizes, but remains CPU-bound up to four times larger batch sizes than loosely coupled systems, with kernel-launch and queuing overhead contributing to higher low-batch latency.
- [fact; source: https://docs.vllm.ai/en/latest/configuration/optimization/] vLLM provides Non-Uniform Memory Access (NUMA) binding for multi-socket GPU servers because CPU execution and memory allocation drifting away from the GPU's nearest NUMA node can reduce performance.
- [fact; source: https://github.com/ggml-org/llama.cpp/tree/master/tools/llama-bench] llama-bench exposes thread count, batch size, GPU-layer offload, and NUMA options, and its documented examples show prompt-processing and text-generation throughput changing materially with thread count and GPU-layer placement.
- [inference; source: https://arxiv.org/abs/2504.11750; https://docs.vllm.ai/en/latest/configuration/optimization/; https://github.com/ggml-org/llama.cpp/tree/master/tools/llama-bench] GPU inference is therefore not purely a GPU-capacity problem, because CPU launch overhead, NUMA placement, and thread scheduling still shape low-batch latency and can delay or negate the benefit of more accelerator capacity.

#### D. Serving systems expose different contention controls, but all of them make load management explicit

- [fact; source: https://docs.vllm.ai/en/latest/configuration/optimization/; https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html] vLLM exposes batch-token budgets, preemption metrics, parallelism strategies, and request-header tracing, and also warns that model `generation_config.json` defaults can override serving defaults unless the operator disables that behavior.
- [fact; source: https://huggingface.co/docs/text-generation-inference/en/index; https://huggingface.co/docs/text-generation-inference/main/en/architecture] TGI provides continuous batching, tensor parallelism, Prometheus metrics, OpenTelemetry tracing, and a router-model-server split where the router is responsible for request buffering and batching policy.
- [fact; source: https://docs.ollama.com/faq; https://github.com/ollama/ollama/blob/main/envconfig/config.go] Ollama exposes `OLLAMA_NUM_PARALLEL`, `OLLAMA_MAX_LOADED_MODELS`, `OLLAMA_MAX_QUEUE`, `OLLAMA_KEEP_ALIVE`, `OLLAMA_GPU_OVERHEAD`, and `OLLAMA_KV_CACHE_TYPE`, which makes concurrency, memory headroom, queue length, and model residency operator-visible control surfaces.
- [fact; source: https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md] llama.cpp's HTTP server advertises parallel decoding with multi-user support, continuous batching, monitoring endpoints, JavaScript Object Notation (JSON)-schema-constrained output, configurable server slots, GPU offload, KV offload, and multi-GPU split modes.
- [inference; source: https://docs.vllm.ai/en/latest/configuration/optimization/; https://huggingface.co/docs/text-generation-inference/main/en/architecture; https://docs.ollama.com/faq; https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md] The common pattern is that mature serving systems do not hide load handling behind a single "utilization" metric; they surface queue depth, batching limits, memory budgets, or concurrency slots because those are the real failure surfaces under contention.

#### E. Empirical benchmarks show large gains from better memory and scheduler design, and measurable output drift when batch or hardware changes

- [fact; source: https://arxiv.org/abs/2309.06180] Kwon et al. show that better KV-cache memory management alone can deliver 2 to 4 times higher throughput than prior systems at similar latency.
- [fact; source: https://arxiv.org/abs/2403.02310] Agrawal et al. show that chunked-prefill scheduling can materially raise serving capacity without paying the full latency penalty usually associated with larger batches.
- [fact; source: https://arxiv.org/abs/2504.11750] Vellaisamy et al. show that hardware coupling and CPU behavior change where the CPU-bound to GPU-bound transition occurs, which means the same model can hit different bottlenecks on different platform designs.
- [fact; source: https://github.com/ggml-org/llama.cpp/tree/master/tools/llama-bench] llama-bench example runs show prompt-processing throughput rising from 1,436.51 tokens per second at batch size 128 to 2,498.61 tokens per second at batch size 1024, and text-generation throughput rising sharply as more layers are offloaded to the GPU.
- [inference; source: https://arxiv.org/abs/2506.09501; https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html] In the consulted evidence, the clearest output-variance results are tied to changed batch size, hardware count, or precision, because both Yuan et al. and vLLM attribute token divergence to numerically different batched execution paths.
- [inference; source: https://arxiv.org/abs/2309.06180; https://arxiv.org/abs/2403.02310; https://arxiv.org/abs/2504.11750; https://arxiv.org/abs/2506.09501; https://github.com/ggml-org/llama.cpp/tree/master/tools/llama-bench] The evidence base is strong for "load changes performance" and moderate for "load changes outputs," with the second claim becoming strong only when load is operationalized as changed batch shape, precision mode, or hardware path rather than as a generic high-utilization state.

#### F. Practical implications for agent reliability center on capacity classes, observability, and deterministic external control

- [fact; source: https://docs.vllm.ai/en/latest/configuration/optimization/; https://huggingface.co/docs/text-generation-inference/main/en/architecture; https://docs.ollama.com/faq; https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md] All four serving stacks examined expose explicit controls for concurrency, batching, queueing, memory residency, or instrumentation.
- [inference; source: https://docs.vllm.ai/en/latest/configuration/optimization/; https://huggingface.co/docs/text-generation-inference/main/en/architecture; https://docs.ollama.com/faq; https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md] Because those controls are operator-visible, production teams can monitor and tune the surfaces that most directly affect reliability.
- [inference; source: https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html; https://arxiv.org/abs/2506.09501; https://davidamitchell.github.io/Research/research/2026-05-09-llm-determinism-limits-temperature-zero.html] High-consequence agent steps should not rely on raw model output as a deterministic authority, because the same prompt can change tokens when batch composition, hardware path, or precision changes under live serving conditions.
- [inference; source: https://docs.vllm.ai/en/latest/configuration/optimization/; https://docs.ollama.com/faq; https://huggingface.co/docs/text-generation-inference/main/en/architecture; https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring.html] Agent fleets therefore need load-aware routing, bounded concurrency per workload class, memory-headroom policies, preemption and queue-depth monitoring, and fallback or retry strategies that do not blindly amplify the load spike they are responding to.

### §3 Reasoning

- [inference; source: https://arxiv.org/abs/2309.06180; https://arxiv.org/abs/2403.02310; https://arxiv.org/abs/2504.11750; https://docs.vllm.ai/en/latest/configuration/optimization/] The supported causal chain for performance degradation is queueing, batching, KV-cache pressure, and CPU or GPU coordination overhead, not a generic claim that higher utilization percentages directly reduce model capability.
- [inference; source: https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html; https://arxiv.org/abs/2506.09501; https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/] The supported causal chain for output inconsistency is changed batch shape, hardware path, or numerical precision, which can slightly perturb logits and then amplify through autoregressive decoding.
- [inference; source: https://docs.ollama.com/faq; https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html; https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html] Memory-saving or configuration-changing mitigations can protect throughput while making outputs less stable, so performance tuning and reproducibility tuning are related but not identical objectives.
- [assumption; source: https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring.html; https://davidamitchell.github.io/Research/research/2026-05-08-integrated-cascading-failure-agentic-vs-generative-ai-risk.html] This item assumes that agent reliability is defined by bounded latency and bounded decision drift rather than by byte-identical string replay, because production agents usually fail through missed orchestration envelopes or changed action choices before exact text replay becomes the primary operational concern.

### §4 Consistency Check

- [fact; source: https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html; https://arxiv.org/abs/2506.09501] The consulted sources do support the claim that load can affect outputs, but only when load changes the numerical execution path through batching, hardware, or precision.
- [fact; source: https://arxiv.org/abs/2309.06180; https://arxiv.org/abs/2403.02310; https://arxiv.org/abs/2504.11750; https://github.com/ggml-org/llama.cpp/tree/master/tools/llama-bench] The consulted sources strongly support the claim that hardware load affects latency and throughput across serving stacks and hardware designs.
- [inference; source: https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html; https://arxiv.org/abs/2506.09501; https://docs.ollama.com/faq] The apparent contradiction between "load affects quality" and "load affects only speed" is resolved by distinguishing raw utilization from load-induced configuration changes, because the consulted evidence ties semantic drift to the latter rather than the former.

### §5 Depth and Breadth Expansion

- [inference; source: https://huggingface.co/docs/text-generation-inference/en/index; https://huggingface.co/docs/text-generation-inference/main/en/architecture; https://docs.vllm.ai/en/latest/configuration/optimization/] Through a technical lens, the main operator levers are scheduler policy, batch-token limits, memory-headroom policy, and hardware topology, because those levers directly determine whether a request waits, recomputes, or runs on a changed numerical path.
- [inference; source: https://arxiv.org/abs/2403.02310; https://docs.vllm.ai/en/latest/configuration/optimization/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-cost-performance-delivery-impact.html] Through an economic lens, maximizing global throughput without class-based latency targets can be locally efficient but operationally expensive for agent workloads that miss deadlines or trigger retries when tail latency widens.
- [inference; source: https://docs.ollama.com/faq; https://docs.vllm.ai/en/latest/configuration/optimization/; https://davidamitchell.github.io/Research/research/2026-05-08-integrated-cascading-failure-agentic-vs-generative-ai-risk.html] Through a behavioural lens, naive retry loops and overloaded shared infrastructure can reinforce each other, because queue growth or preemption lengthens latency, which can trigger more retries or wider orchestration failure.
- [inference; source: https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html; https://arxiv.org/abs/2506.09501; https://davidamitchell.github.io/Research/research/2026-05-09-governance-policy-determinism-vs-stochastic-llm.html] Through a governance lens, any agent action with threshold-sensitive consequences still needs deterministic checks outside the model, because live serving conditions can change generated tokens even when the prompt and nominal decoding policy stay fixed.

### §6 Synthesis

**Executive summary:**

Hardware load does affect LLM inference reliability, but it does so mainly by pushing serving systems across batching, memory, and numerical-precision thresholds that inflate latency and sometimes change generated tokens, not by making models semantically worse merely because GPU utilization is high. [inference; source: https://docs.vllm.ai/en/latest/configuration/optimization/; https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html; https://arxiv.org/abs/2506.09501; https://arxiv.org/abs/2403.02310]

The consulted evidence shows that throughput and latency degrade in threshold-like steps when schedulers rebalance prefill and decode work, when KV cache space becomes scarce, or when CPU coordination remains the bottleneck despite abundant GPU capacity. [inference; source: https://docs.vllm.ai/en/latest/configuration/optimization/; https://arxiv.org/abs/2403.02310; https://arxiv.org/abs/2504.11750]

Output consistency risk is real, but the consulted evidence ties it to batch- or hardware-dependent numerical divergence, including changed batch composition, changed precision mode, or changed accelerator path, rather than to utilization telemetry by itself. [inference; source: https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html; https://arxiv.org/abs/2506.09501; https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/]

For production agents, the practical answer is to monitor queue depth, preemption, batch shape, context growth, precision mode, and model pinning as first-class reliability signals, while keeping deterministic policy enforcement outside raw model outputs for consequential actions. [inference; source: https://docs.vllm.ai/en/latest/configuration/optimization/; https://docs.ollama.com/faq; https://huggingface.co/docs/text-generation-inference/main/en/architecture; https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring.html; https://davidamitchell.github.io/Research/research/2026-05-09-llm-determinism-limits-temperature-zero.html]

**Key findings:**

1. **Under load, Large Language Model serving slows in threshold-like jumps that follow scheduler changes between prefill and decode work, not a smooth linear decline tied to Graphics Processing Unit utilization percentages.** ([inference]; high confidence; source: https://arxiv.org/abs/2403.02310; https://docs.vllm.ai/en/latest/configuration/optimization/; https://huggingface.co/docs/text-generation-inference/main/en/architecture)
2. **Key-value cache pressure becomes a major concurrent-serving bottleneck once batch demand outruns available memory, and vLLM responds by preempting and recomputing requests after space is freed.** ([fact]; high confidence; source: https://arxiv.org/abs/2309.06180; https://docs.vllm.ai/en/latest/configuration/optimization/)
3. **Even GPU-heavy inference stacks stay sensitive to Central Processing Unit launch and placement overhead, so low-batch latency can remain CPU-bound long after accelerator capacity appears available.** ([fact]; medium confidence; source: https://arxiv.org/abs/2504.11750; https://docs.vllm.ai/en/latest/configuration/optimization/; https://github.com/ggml-org/llama.cpp/tree/master/tools/llama-bench)
4. **TGI, Ollama, vLLM, and llama.cpp all expose contention as explicit queueing, batching, and concurrency settings, which makes operator tuning part of reliable serving rather than an optional optimization.** ([fact]; high confidence; source: https://huggingface.co/docs/text-generation-inference/main/en/architecture; https://docs.ollama.com/faq; https://github.com/ollama/ollama/blob/main/envconfig/config.go; https://docs.vllm.ai/en/latest/configuration/optimization/; https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)
5. **Load-sensitive output drift appears when batch shape or hardware path changes the numerical execution path, and the reviewed evidence documents changed sampled tokens plus measurable accuracy shifts under those conditions.** ([fact]; high confidence; source: https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html; https://arxiv.org/abs/2506.09501)
6. **No consulted source shows that raw utilization percentages alone degrade semantic quality once the numerical path is held fixed; the documented quality risk comes from changed precision modes, quantized caches, or altered live batching.** ([inference]; medium confidence; source: https://docs.ollama.com/faq; https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html; https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/)
7. **Reliable agent deployments need workload-class isolation, bounded concurrency, warm model residency, and deterministic external checks, since latency spikes and occasional token drift can compound across multi-step workflows.** ([inference]; medium confidence; source: https://docs.vllm.ai/en/latest/configuration/optimization/; https://docs.ollama.com/faq; https://huggingface.co/docs/text-generation-inference/main/en/architecture; https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring.html; https://davidamitchell.github.io/Research/research/2026-05-08-integrated-cascading-failure-agentic-vs-generative-ai-risk.html; https://davidamitchell.github.io/Research/research/2026-05-09-llm-determinism-limits-temperature-zero.html)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Load-induced slowdown is threshold-based and scheduler-mediated rather than smoothly linear. | https://arxiv.org/abs/2403.02310; https://docs.vllm.ai/en/latest/configuration/optimization/; https://huggingface.co/docs/text-generation-inference/main/en/architecture | high | Prefill-decode tradeoff |
| [fact] KV-cache pressure is a major concurrent-serving bottleneck. | https://arxiv.org/abs/2309.06180; https://docs.vllm.ai/en/latest/configuration/optimization/ | high | Preemption and recompute |
| [fact] CPU coordination remains a material bottleneck in some GPU-serving regimes. | https://arxiv.org/abs/2504.11750; https://docs.vllm.ai/en/latest/configuration/optimization/; https://github.com/ggml-org/llama.cpp/tree/master/tools/llama-bench | medium | Low-batch sensitivity |
| [fact] The studied inference systems expose explicit queueing and concurrency controls. | https://huggingface.co/docs/text-generation-inference/main/en/architecture; https://docs.ollama.com/faq; https://github.com/ollama/ollama/blob/main/envconfig/config.go; https://docs.vllm.ai/en/latest/configuration/optimization/; https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md | high | Operator-visible levers |
| [fact] Batch-sensitive numerical divergence can change tokens and measured task accuracy. | https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html; https://arxiv.org/abs/2506.09501 | high | Output drift evidence |
| [inference] High utilization alone is weaker evidence for semantic degradation than changed precision or changed execution path. | https://docs.ollama.com/faq; https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html; https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/ | medium | Mechanism separation |
| [inference] Agent reliability depends on capacity controls plus deterministic external checks. | https://docs.vllm.ai/en/latest/configuration/optimization/; https://docs.ollama.com/faq; https://huggingface.co/docs/text-generation-inference/main/en/architecture; https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring.html; https://davidamitchell.github.io/Research/research/2026-05-08-integrated-cascading-failure-agentic-vs-generative-ai-risk.html; https://davidamitchell.github.io/Research/research/2026-05-09-llm-determinism-limits-temperature-zero.html | medium | Operational synthesis |

**Assumptions:**

- [assumption; source: https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring.html; https://davidamitchell.github.io/Research/research/2026-05-08-integrated-cascading-failure-agentic-vs-generative-ai-risk.html] Agent reliability is defined here as staying inside bounded latency and bounded decision-drift envelopes rather than reproducing byte-identical text, because multi-step production agents usually fail first through missed orchestration deadlines or changed action choices.

**Analysis:**

I weighted official serving documentation and system papers highest for claims about queueing, batching, memory pressure, and hardware bottlenecks, because those sources describe the actual control surfaces used in production inference stacks. [fact; source: https://docs.vllm.ai/en/latest/configuration/optimization/; https://huggingface.co/docs/text-generation-inference/main/en/architecture; https://docs.ollama.com/faq; https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md; https://arxiv.org/abs/2309.06180; https://arxiv.org/abs/2403.02310; https://arxiv.org/abs/2504.11750]

For output-consistency claims, I weighted direct evidence of batch- or hardware-sensitive divergence above anecdotal operator reports, because Yuan et al. and the vLLM frequently asked questions page both tie changed execution paths to changed tokens or task outcomes. [fact; source: https://arxiv.org/abs/2506.09501; https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html]

The main interpretive choice was to separate "high hardware load" from "changed numerical path," because the consulted sources strongly support the second as a mechanism for output drift and only indirectly support the first. [inference; source: https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html; https://docs.ollama.com/faq; https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/]

A plausible alternative explanation is that hardware load is only a service-speed problem and not an output-quality problem. I reject that broader claim because vLLM and Yuan et al. both tie changed execution paths to changed sampled tokens or measured task accuracy, even though the evidence remains strongest when load is expressed as changed batch or hardware state rather than as utilization alone. [inference; source: https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html; https://arxiv.org/abs/2506.09501]

That separation narrows the recommendation to concrete operational controls: operators should monitor queue depth, preemption count, batch size, context growth, and precision mode instead of treating a single utilization percentage as a sufficient reliability diagnosis. [inference; source: https://docs.vllm.ai/en/latest/configuration/optimization/; https://huggingface.co/docs/text-generation-inference/main/en/architecture; https://docs.ollama.com/faq; https://github.com/ollama/ollama/blob/main/envconfig/config.go]

**Risks, gaps, uncertainties:**

- Few consulted primary sources measure complete multi-step agent task success under controlled hardware-load sweeps, so most direct evidence stops at latency, throughput, token divergence, or single-task accuracy variance. [fact; source: https://arxiv.org/abs/2309.06180; https://arxiv.org/abs/2403.02310; https://arxiv.org/abs/2504.11750; https://arxiv.org/abs/2506.09501]
- TGI documentation describes its control surfaces, but the consulted official pages provide fewer public head-to-head benchmark numbers than the vLLM and Sarathi-Serve sources, so cross-system performance ranking remains partial. [fact; source: https://huggingface.co/docs/text-generation-inference/en/index; https://huggingface.co/docs/text-generation-inference/main/en/architecture]
- Ollama and llama.cpp official sources document concurrency and memory controls but do not provide equally strong primary studies of output drift under production load, so cross-stack conclusions about quality variance remain medium confidence. [fact; source: https://docs.ollama.com/faq; https://github.com/ollama/ollama/blob/main/envconfig/config.go; https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md; https://github.com/ggml-org/llama.cpp/tree/master/tools/llama-bench]
- The numerical-drift evidence is strongest for specific models, hardware, and precisions, especially reasoning models under limited precision, so portability to every inference stack and model family should be treated as an informed but not universal conclusion. [inference; source: https://arxiv.org/abs/2506.09501; https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/]

**Open questions:**

- Which queue-depth, preemption, or batch-shape thresholds best predict real agent task failure rather than only slower response times?
- How much output drift remains in production-serving stacks that adopt batch-invariant kernels or full 32-bit floating-point inference?
- Can prompt-length-aware routing and capacity classes outperform global concurrency caps for mixed fleets of short-chat and long-horizon agent workloads?

### §7 Recursive Review

- Result: all sections populated.
- Claim audit: factual and inferential claims labeled in Research Skill Output.
- Acronym audit: first-use expansions checked for LLM, AI, CPU, GPU, RAM, VRAM, KV, TGI, TTFT, and ITL.
- Domain-term audit: agent reliability, prefill, decode, KV cache, and NUMA explained or grounded at first use.
- Mirror check: §6 Synthesis and Findings aligned.

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

Hardware load does affect LLM inference reliability, but it does so mainly by pushing serving systems across batching, memory, and numerical-precision thresholds that inflate latency and sometimes change generated tokens, not by making models semantically worse merely because GPU utilization is high. [inference; source: https://docs.vllm.ai/en/latest/configuration/optimization/; https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html; https://arxiv.org/abs/2506.09501; https://arxiv.org/abs/2403.02310]

The consulted evidence shows that throughput and latency degrade in threshold-like steps when schedulers rebalance prefill and decode work, when KV cache space becomes scarce, or when CPU coordination remains the bottleneck despite abundant GPU capacity. [inference; source: https://docs.vllm.ai/en/latest/configuration/optimization/; https://arxiv.org/abs/2403.02310; https://arxiv.org/abs/2504.11750]

Output consistency risk is real, but the consulted evidence ties it to batch- or hardware-dependent numerical divergence, including changed batch composition, changed precision mode, or changed accelerator path, rather than to utilization telemetry by itself. [inference; source: https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html; https://arxiv.org/abs/2506.09501; https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/]

For production agents, the practical answer is to monitor queue depth, preemption, batch shape, context growth, precision mode, and model pinning as first-class reliability signals, while keeping deterministic policy enforcement outside raw model outputs for consequential actions. [inference; source: https://docs.vllm.ai/en/latest/configuration/optimization/; https://docs.ollama.com/faq; https://huggingface.co/docs/text-generation-inference/main/en/architecture; https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring.html; https://davidamitchell.github.io/Research/research/2026-05-09-llm-determinism-limits-temperature-zero.html]

### Key Findings

1. **Under load, Large Language Model serving slows in threshold-like jumps that follow scheduler changes between prefill and decode work, not a smooth linear decline tied to Graphics Processing Unit utilization percentages.** ([inference]; high confidence; source: https://arxiv.org/abs/2403.02310; https://docs.vllm.ai/en/latest/configuration/optimization/; https://huggingface.co/docs/text-generation-inference/main/en/architecture)
2. **Key-value cache pressure becomes a major concurrent-serving bottleneck once batch demand outruns available memory, and vLLM responds by preempting and recomputing requests after space is freed.** ([fact]; high confidence; source: https://arxiv.org/abs/2309.06180; https://docs.vllm.ai/en/latest/configuration/optimization/)
3. **Even GPU-heavy inference stacks stay sensitive to Central Processing Unit launch and placement overhead, so low-batch latency can remain CPU-bound long after accelerator capacity appears available.** ([fact]; medium confidence; source: https://arxiv.org/abs/2504.11750; https://docs.vllm.ai/en/latest/configuration/optimization/; https://github.com/ggml-org/llama.cpp/tree/master/tools/llama-bench)
4. **TGI, Ollama, vLLM, and llama.cpp all expose contention as explicit queueing, batching, and concurrency settings, which makes operator tuning part of reliable serving rather than an optional optimization.** ([fact]; high confidence; source: https://huggingface.co/docs/text-generation-inference/main/en/architecture; https://docs.ollama.com/faq; https://github.com/ollama/ollama/blob/main/envconfig/config.go; https://docs.vllm.ai/en/latest/configuration/optimization/; https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)
5. **Load-sensitive output drift appears when batch shape or hardware path changes the numerical execution path, and the reviewed evidence documents changed sampled tokens plus measurable accuracy shifts under those conditions.** ([fact]; high confidence; source: https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html; https://arxiv.org/abs/2506.09501)
6. **No consulted source shows that raw utilization percentages alone degrade semantic quality once the numerical path is held fixed; the documented quality risk comes from changed precision modes, quantized caches, or altered live batching.** ([inference]; medium confidence; source: https://docs.ollama.com/faq; https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html; https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/)
7. **Reliable agent deployments need workload-class isolation, bounded concurrency, warm model residency, and deterministic external checks, since latency spikes and occasional token drift can compound across multi-step workflows.** ([inference]; medium confidence; source: https://docs.vllm.ai/en/latest/configuration/optimization/; https://docs.ollama.com/faq; https://huggingface.co/docs/text-generation-inference/main/en/architecture; https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring.html; https://davidamitchell.github.io/Research/research/2026-05-08-integrated-cascading-failure-agentic-vs-generative-ai-risk.html; https://davidamitchell.github.io/Research/research/2026-05-09-llm-determinism-limits-temperature-zero.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Load-induced slowdown is threshold-based and scheduler-mediated rather than smoothly linear. | https://arxiv.org/abs/2403.02310; https://docs.vllm.ai/en/latest/configuration/optimization/; https://huggingface.co/docs/text-generation-inference/main/en/architecture | high | Prefill-decode tradeoff |
| [fact] KV-cache pressure is a major concurrent-serving bottleneck. | https://arxiv.org/abs/2309.06180; https://docs.vllm.ai/en/latest/configuration/optimization/ | high | Preemption and recompute |
| [fact] CPU coordination remains a material bottleneck in some GPU-serving regimes. | https://arxiv.org/abs/2504.11750; https://docs.vllm.ai/en/latest/configuration/optimization/; https://github.com/ggml-org/llama.cpp/tree/master/tools/llama-bench | medium | Low-batch sensitivity |
| [fact] The studied inference systems expose explicit queueing and concurrency controls. | https://huggingface.co/docs/text-generation-inference/main/en/architecture; https://docs.ollama.com/faq; https://github.com/ollama/ollama/blob/main/envconfig/config.go; https://docs.vllm.ai/en/latest/configuration/optimization/; https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md | high | Operator-visible levers |
| [fact] Batch-sensitive numerical divergence can change tokens and measured task accuracy. | https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html; https://arxiv.org/abs/2506.09501 | high | Output drift evidence |
| [inference] High utilization alone is weaker evidence for semantic degradation than changed precision or changed execution path. | https://docs.ollama.com/faq; https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html; https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/ | medium | Mechanism separation |
| [inference] Agent reliability depends on capacity controls plus deterministic external checks. | https://docs.vllm.ai/en/latest/configuration/optimization/; https://docs.ollama.com/faq; https://huggingface.co/docs/text-generation-inference/main/en/architecture; https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring.html; https://davidamitchell.github.io/Research/research/2026-05-08-integrated-cascading-failure-agentic-vs-generative-ai-risk.html; https://davidamitchell.github.io/Research/research/2026-05-09-llm-determinism-limits-temperature-zero.html | medium | Operational synthesis |

### Assumptions

- **Assumption:** Agent reliability is defined here as staying inside bounded latency and bounded decision-drift envelopes rather than reproducing byte-identical text. **Justification:** multi-step production agents usually fail first through missed orchestration deadlines or changed action choices. [assumption; source: https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring.html; https://davidamitchell.github.io/Research/research/2026-05-08-integrated-cascading-failure-agentic-vs-generative-ai-risk.html]

### Analysis

I weighted official serving documentation and system papers highest for claims about queueing, batching, memory pressure, and hardware bottlenecks, because those sources describe the actual control surfaces used in production inference stacks. [fact; source: https://docs.vllm.ai/en/latest/configuration/optimization/; https://huggingface.co/docs/text-generation-inference/main/en/architecture; https://docs.ollama.com/faq; https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md; https://arxiv.org/abs/2309.06180; https://arxiv.org/abs/2403.02310; https://arxiv.org/abs/2504.11750]

For output-consistency claims, I weighted direct evidence of batch- or hardware-sensitive divergence above anecdotal operator reports, because Yuan et al. and the vLLM frequently asked questions page both tie changed execution paths to changed tokens or task outcomes. [fact; source: https://arxiv.org/abs/2506.09501; https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html]

The main interpretive choice was to separate "high hardware load" from "changed numerical path," because the consulted sources strongly support the second as a mechanism for output drift and only indirectly support the first. [inference; source: https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html; https://docs.ollama.com/faq; https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/]

A plausible alternative explanation is that hardware load is only a service-speed problem and not an output-quality problem. I reject that broader claim because vLLM and Yuan et al. both tie changed execution paths to changed sampled tokens or measured task accuracy, even though the evidence remains strongest when load is expressed as changed batch or hardware state rather than as utilization alone. [inference; source: https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html; https://arxiv.org/abs/2506.09501]

That separation narrows the recommendation to concrete operational controls: operators should monitor queue depth, preemption count, batch size, context growth, and precision mode instead of treating a single utilization percentage as a sufficient reliability diagnosis. [inference; source: https://docs.vllm.ai/en/latest/configuration/optimization/; https://huggingface.co/docs/text-generation-inference/main/en/architecture; https://docs.ollama.com/faq; https://github.com/ollama/ollama/blob/main/envconfig/config.go]

### Risks, Gaps, and Uncertainties

- Few consulted primary sources measure complete multi-step agent task success under controlled hardware-load sweeps, so most direct evidence stops at latency, throughput, token divergence, or single-task accuracy variance. [fact; source: https://arxiv.org/abs/2309.06180; https://arxiv.org/abs/2403.02310; https://arxiv.org/abs/2504.11750; https://arxiv.org/abs/2506.09501]
- TGI documentation describes its control surfaces, but the consulted official pages provide fewer public head-to-head benchmark numbers than the vLLM and Sarathi-Serve sources, so cross-system performance ranking remains partial. [fact; source: https://huggingface.co/docs/text-generation-inference/en/index; https://huggingface.co/docs/text-generation-inference/main/en/architecture]
- Ollama and llama.cpp official sources document concurrency and memory controls but do not provide equally strong primary studies of output drift under production load, so cross-stack conclusions about quality variance remain medium confidence. [fact; source: https://docs.ollama.com/faq; https://github.com/ollama/ollama/blob/main/envconfig/config.go; https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md; https://github.com/ggml-org/llama.cpp/tree/master/tools/llama-bench]
- The numerical-drift evidence is strongest for specific models, hardware, and precisions, especially reasoning models under limited precision, so portability to every inference stack and model family should be treated as an informed but not universal conclusion. [inference; source: https://arxiv.org/abs/2506.09501; https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/]

### Open Questions

- Which queue-depth, preemption, or batch-shape thresholds best predict real agent task failure rather than only slower response times?
- How much output drift remains in production-serving stacks that adopt batch-invariant kernels or full 32-bit floating-point inference?
- Can prompt-length-aware routing and capacity classes outperform global concurrency caps for mixed fleets of short-chat and long-horizon agent workloads?

---

## Output

- Type: knowledge
- Description: This item shows that production agent reliability depends on controlling queueing, memory headroom, batch shape, and numerical configuration, not just watching aggregate hardware utilization. [inference; source: https://docs.vllm.ai/en/latest/configuration/optimization/; https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html; https://arxiv.org/abs/2506.09501]
- Links:
  - https://docs.vllm.ai/en/latest/configuration/optimization/
  - https://arxiv.org/abs/2309.06180
  - https://arxiv.org/abs/2506.09501
