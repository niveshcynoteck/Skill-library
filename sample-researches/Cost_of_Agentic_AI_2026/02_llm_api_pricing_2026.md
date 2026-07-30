# LLM API & Token Pricing Landscape (2026)

All prices are USD per million tokens, official first-party pricing (compiled 2026-07-29).

## Anthropic — Claude

*Confirmed directly from Anthropic's official pricing documentation.*

| Model | Input | 5m Cache Write | 1h Cache Write | Cache Read | Output |
|---|---|---|---|---|---|
| Claude Opus 5 | $5 | $6.25 | $10 | $0.50 | $25 |
| Claude Sonnet 5 (through Aug 31, 2026) | $2 | $2.50 | $4 | $0.20 | $10 |
| Claude Sonnet 5 (from Sep 1, 2026) | $3 | $3.75 | $6 | $0.30 | $15 |
| Claude Haiku 4.5 | $1 | $1.25 | $2 | $0.10 | $5 |

## OpenAI — GPT

| Model | Tier | Input | Cached Input | Output |
|---|---|---|---|---|
| GPT-5.6 Sol (≤272K context) | Flagship | $5.00 | $0.50 | $30.00 |
| GPT-5.6 Sol (>272K context) | Flagship, long-context | $10.00 | $1.00 | $45.00 |
| GPT-5.6 Terra | Mid-tier | $2.50 | $0.25 | $15.00 |
| GPT-5.6 Luna | Budget/high-volume | $1.00 | $0.10 | $6.00 |
| GPT-5 mini | Prior-gen small | $0.25 | $0.025 | $2.00 |
| GPT-5 nano | Cheapest legacy | $0.05 | $0.005 | $0.40 |
| o3 | Reasoning | $2.00 | $0.50 | $8.00 |

## Google — Gemini

| Model | Tier | Input | Cached Input | Output |
|---|---|---|---|---|
| Gemini 3.1 Pro Preview (≤200K context) | Flagship | $2.00 | $0.20 | $12.00 |
| Gemini 3.1 Pro Preview (>200K context) | Flagship, long-context | $4.00 | $0.40 | $18.00 |
| Gemini 3.6 Flash | Mid-tier | $1.50 | $0.15 + storage | $7.50 |
| Gemini 3.5 Flash-Lite | Budget | $0.30 | $0.03 + storage | $2.50 |
| Gemini 2.5 Pro | Prior-gen | $1.25 | $0.125 | $10.00 |

## 2026 Pricing Trends

1. **Long-context surcharges are now standard.** OpenAI (>272K tokens) and Google (>200K tokens) both roughly double flagship input/output pricing past a threshold — directly relevant to agents accumulating large tool-history contexts.
2. **A new "ultra-budget" tier emerged** beneath mini/flash (OpenAI's Luna, Google's Flash-Lite) targeting high-volume, low-stakes agent steps at a fraction of flagship cost.
3. **Time-boxed introductory discounts exist even on flagships.** Anthropic's Claude Sonnet 5 intro pricing ($2/$10) reverts to standard ($3/$15) on September 1, 2026 — "current" pricing can include limited-time layers on top of list price.
4. **Cache-read pricing converges near 10% of input cost** across all three providers — a first-order cost-design constraint for agent harnesses not structured for cache-prefix stability.
5. **Batch processing remains a flat 50% discount** across OpenAI and Anthropic for latency-insensitive workloads — not applicable to live agent loops.

## Sources

- [Claude API Pricing (official)](https://platform.claude.com/docs/en/about-claude/pricing) — Anthropic — full official per-model pricing table, cache multipliers, batch discounts *(corrected link — original URL 404'd during validation; this replacement was fetched directly and used to verify every figure above)*
- [OpenAI API Pricing](https://developers.openai.com/api/docs/pricing) — OpenAI — official pricing for GPT-5.6 Sol/Terra/Luna, GPT-5 mini/nano, o-series
- [Gemini API Pricing](https://ai.google.dev/gemini-api/docs/pricing) — Google — official pricing for Gemini 3.6 Flash, 3.5 Flash-Lite, 3.1 Pro Preview, and prior-gen models
- [GPT-5.6 Pricing Breakdown](https://apidog.com/blog/gpt-5-6-pricing/) — Apidog — secondary cross-check confirming Sol/Terra/Luna rates and the 272K long-context threshold
- [Gemini Pricing in 2026](https://www.cloudzero.com/blog/gemini-pricing/) — CloudZero — secondary cross-check on Gemini 3-series pricing tiers
