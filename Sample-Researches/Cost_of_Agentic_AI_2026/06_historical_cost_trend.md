# Historical Cost Trend (2023 → 2026) and the Reasons Behind It

## The Cost-Per-Token Trend

**Verified fact:** cost per token for a fixed capability level has fallen dramatically since 2021, and the decline has *accelerated* since early 2024. Epoch AI's analysis found a **median decline of ~50x per year** across performance thresholds (2021–2025), with the range spanning 9x/year (basic capability) to 900x/year (top-tier capability). Restricted to the 2024–2025 window alone, the median rate rose to roughly **200x per year**. For a fixed benchmark — matching GPT-4's score on GPQA Diamond — price fell about **40x per year**.

a16z's independent "LLMflation" analysis, focused on matching fixed MMLU performance tiers, found a similar pattern (~10x/year average):
- GPT-3-level performance: $60/million tokens (Nov 2021) → ~$0.06/million tokens within ~3 years (~1,000x decline).
- GPT-4-level performance: roughly a **62x price decline in ~1.5 years** — from ~$20/million tokens (late 2022) to ~$0.40/million tokens.

By 2025–2026, competitive pressure — especially from Chinese open-weight labs like DeepSeek — pushed pricing lower still: DeepSeek's R1 was reported to run 20–50x cheaper than comparable OpenAI models, with DeepSeek V3.2/V4 landing around $0.03–0.14 per million input tokens.

**Bottom line:** cost-per-token for a fixed capability level has fallen sharply and consistently from 2023 through 2026, at rates far exceeding historical semiconductor cost curves, even as usage volume and task complexity rose substantially.

## Drivers Behind Falling Per-Token Prices

1. **Model/algorithmic efficiency gains (major driver).** Smaller models now match the performance of previous years' much larger frontier models — driven by better training data curation, architecture improvements (e.g., mixture-of-experts routing), and post-training techniques (RLHF/DPO).
2. **Inference-side optimizations.** Quantization (16-bit → 4-bit/FP4), speculative decoding, KV/prompt caching, and batching materially cut serving cost per token.
3. **Hardware improvements (moderate contribution).** GPU generations H100 → H200 → Blackwell delivered large throughput gains, but raw cost-per-FLOP improvement is estimated at a more modest ~30–50%/year — implying hardware alone explains only part of the overall price decline.
4. **Competitive pricing pressure (strong driver).** Open-weight releases (Llama, Mistral, and especially DeepSeek) forced closed-lab providers to compress margins and cut list prices.
5. **Economies of scale.** Rising usage volumes let providers amortize fixed infrastructure costs — plausible but harder to isolate quantitatively.

## Countervailing Force: Agentic Workloads Use Far More Tokens Per Task

**Caveat on source quality:** the figures below come from industry/vendor blogs rather than academic sources, and should be treated as directional/illustrative.

- Agentic workflows reportedly use **5x–30x more tokens per task** than a simple chatbot exchange, due to multi-step reasoning, tool calls, retries, and self-correction loops.
- A cited example: a simple 2023-style workflow costing ~$0.04/interaction versus a 2026 agentic/orchestrated workflow costing ~$1.20/interaction — roughly **30x higher total cost per task**, despite per-token prices having fallen by 1–2 orders of magnitude over the same period.

**Key tension for 2026:** falling per-token prices have been substantially offset — sometimes overwhelmed — by rising token consumption per task in agentic systems, so real-world total spend on AI can rise even as unit economics improve.

## Sources

- [LLM inference prices have fallen rapidly but unequally across tasks](https://epoch.ai/data-insights/llm-inference-price-trends) — Epoch AI — core verified data on decline rates
- [Welcome to LLMflation: LLM inference cost is going down fast](https://a16z.com/llmflation-llm-inference-cost/) — a16z — GPT-3/GPT-4 equivalent price-decline figures and drivers
- [Inference economics of language models](https://epoch.ai/blog/inference-economics-of-language-models) — Epoch AI — background on inference cost structure and efficiency drivers
- [DeepSeek's Low Inference Cost Explained: MoE & Strategy](https://intuitionlabs.ai/articles/deepseek-inference-cost-explained) — IntuitionLabs — DeepSeek's cost advantage and MoE architecture
- [DeepSeek-V3.2 Matches GPT-5 at 10x Lower Cost](https://introl.com/blog/deepseek-v3-2-open-source-ai-cost-advantage) — Introl — DeepSeek V3.2 pricing vs. GPT-5
- [GPU Cost: definition, the H100/B200 economics](https://www.startups.com/lexicon/gpu-cost) — Startups.com — H100 vs. B200 cost-per-FLOP comparison
- [Nvidia Blackwell Perf TCO Analysis](https://newsletter.semianalysis.com/p/nvidia-blackwell-perf-tco-analysis) — SemiAnalysis — Blackwell TCO and performance analysis
- [Agentic AI Inference Cost: Why Agents Burn 5–30x Tokens](https://www.spheron.network/blog/agentic-ai-inference-cost-2026/) — Spheron — countervailing agentic token-consumption trend
- [The Hidden Cost Driver in Agentic Coding Sessions in 2026](https://www.vantage.sh/blog/agentic-coding-costs) — Vantage — supporting data on rising agentic token/cost consumption

*Note: per-token price-decline statistics (Epoch AI, a16z) are corroborated across independent research-oriented sources. The agentic-workload token-multiplier figures come from industry/marketing blogs and were not independently cross-verified against a research organization's data — treat as illustrative, not consensus.*
