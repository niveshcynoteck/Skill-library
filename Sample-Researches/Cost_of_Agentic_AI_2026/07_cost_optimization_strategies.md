# Cost Optimization Strategies for Agentic AI

## 1. Prompt / Context Caching

Agentic sessions repeatedly resend the same system prompt, tool schemas, and conversation history on every turn. Caching stores that static prefix and bills re-reads at a steep discount.

- **Anthropic (Claude):** cache reads billed at **0.1x base input price** (a 90% discount); cache writes cost 1.25x (5-min TTL) or 2x (1-hour TTL) as a one-time premium. Real-world case: one company raised its cache-hit rate from 7% to 84% and cut total LLM spend by 59–70%.
- **OpenAI:** automatic prompt caching applies to repeated prefixes within a short time window; cached portions billed at a fraction of standard input cost (reported ~75% off for newer models), applied automatically.
- **Google Gemini:** cached input tokens billed at ~10% of the standard input rate, plus an hourly storage fee. Break-even requires roughly one cache read per hour to offset storage; minimum cacheable content is 32,768 tokens.

Net effect for multi-turn agents: the more turns share a fixed context, the closer realized savings approach the ~90% per-token discount — though total bill reduction depends on actual cache-hit rate, not just the discount rate.

## 2. Model Routing

Instead of running every step through one flagship model, a router sends simple sub-tasks (classification, extraction, formatting) to small/cheap models and reserves frontier models for steps needing deep reasoning.

- Reported outcomes vary widely by source quality: multiple engineering write-ups cite **40–85% bill reduction** from tuned routing layers, and one cited result claims up to 98% cost reduction versus always calling the best model, at comparable quality.
- The price gap motivating this is large: roughly **100x** separates the cheapest usable models (~$0.44/M input) from top-tier models (~$30/M input, ~$180/M output).
- Typical architecture: Tier 1 (small/fast) for retrieval/formatting/simple Q&A; Tier 2 (mid-tier) for standard coding/writing; Tier 3 (frontier) reserved for high-stakes reasoning and orchestration.

Caveat: these percentage figures come mostly from vendor/consultancy blogs rather than peer-reviewed benchmarks — treat as directional.

## 3. Batching

For agentic workloads that don't need synchronous responses (bulk labeling, nightly reports, offline evaluation):

- **OpenAI Batch API:** flat **50% cost discount** versus the synchronous API, ~24-hour completion window.
- **Anthropic Message Batches API:** same 50% discount structure, up to 10,000 requests per batch, results within 24 hours.
- Batching stacks with caching — combining batch (50% off) with prompt caching (up to 90% off cached tokens) can compound toward a reported ~95% combined reduction for eligible workloads.

The clear limitation: batching is unusable for latency-sensitive, interactive agent loops — it only helps offline/asynchronous portions of a pipeline.

## 4. Open-Source / Self-Hosted Models

Self-hosting open-weight models (Llama, DeepSeek V3, Mistral Large, etc.) trades per-token API fees for fixed GPU infrastructure and DevOps overhead.

- Break-even estimates vary by source: one analysis puts it near $4,200/month of equivalent API spend; another frames it as ~500M tokens/month before self-hosting undercuts APIs (self-hosted infra typically running $1,500–5,000/month).
- Where volume justifies it, self-hosted open models can cut per-token cost by an estimated **60–80%** versus GPT-4o-class API pricing.
- Trade-offs: frontier-only capabilities (top-tier reasoning, latest agentic tool-use quality) are not available to self-host; self-hosting shifts cost from variable per-token billing to fixed capacity, favoring steady/high-volume workloads over bursty ones, and adds operational burden a managed API absorbs.

## Sources

- [Prompt Caching (official docs)](https://platform.claude.com/docs/en/docs/build-with-claude/prompt-caching) — Anthropic — cache write/read pricing multipliers
- [Batch API Guide (official docs)](https://developers.openai.com/api/docs/guides/batch) — OpenAI — official 50% Batch API discount statement
- [Gemini API Pricing (official page)](https://ai.google.dev/gemini-api/docs/pricing) — Google — cached vs. standard input token prices
- [Context caching — Gemini API docs](https://ai.google.dev/gemini-api/docs/caching) — Google — caching mechanics, minimum cache size
- [How We Cut LLM Costs by 59% With Prompt Caching](https://projectdiscovery.io/blog/how-we-cut-llm-cost-with-prompt-caching) — ProjectDiscovery — real-world case study
- [Why Most Teams Overpay 40-85% for AI: The Routing Cost Math](https://www.mindstudio.ai/blog/best-ai-model-routers-multi-provider-llm-cost-011e6) — MindStudio — routing bill reduction range
- [AI Agent Cost Optimization: Cut LLM Spend by 80% with Routing](https://www.requesty.ai/blog/ai-agent-cost-optimization-how-to-cut-llm-spend-by-80-percent-with-routing) — Requesty — routing tiers, cited 98% reduction result
- [LLM Model Routing in 2026: Cost-Quality Optimization](https://www.digitalapplied.com/blog/llm-model-routing-2026-cost-quality-optimization-engineering-guide) — Digital Applied — pricing gap, tiered routing architecture
- [Anthropic Message Batches API: 50% Off Claude for Async Jobs](https://www.respan.ai/articles/anthropic-message-batches-api) — Respan — batch discount structure
- [Self-Host LLM vs API: Real Cost Breakdown 2026](https://devtk.ai/en/blog/self-hosting-llm-vs-api-cost-2026/) — DevTk.AI — break-even volume/cost estimates
- [Self-Hosted LLM vs API: The $4,200/mo Break-Even Point](https://www.braincuber.com/blog/self-hosted-llms-vs-api-based-llms-cost-performance-analysis) — Braincuber — alternative break-even estimate
- [Agentic AI with Open Source: Building a Self-Hosted LLM Agent Stack](https://callsphere.ai/blog/agentic-ai-open-source-self-hosted-llm-stack-guide) — CallSphere — frontier-capability gap discussion

*Note: official vendor documentation (Anthropic, OpenAI, Google) verifies all core discount percentages. Model-routing and self-hosting break-even figures come from third-party engineering/consultancy blogs — directionally useful but not independently peer-reviewed.*
