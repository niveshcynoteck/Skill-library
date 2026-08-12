# Compute & Infrastructure Costs

## GPU/Accelerator Rental Pricing (2026)

- **H100 (Hopper):** On-demand rental prices vary from roughly $1.49–$6.98/GPU-hr across providers. Full 8-GPU nodes run about $55–60/hr on AWS, $80–90/hr on Google Cloud, and ~$98/hr on Azure — Azure is consistently the priciest of the three hyperscalers, AWS the cheapest.
- **H200:** AWS raised H200 pricing ~15% in January 2026 — its first GPU price hike in roughly two decades. The p5e.48xlarge (8×H200) instance went from $34.61 to **$39.80/hr**.
- **Blackwell (B200/GB200):** B200 rental averages ~$6.25/hr (range ~$3.35–$14.24/hr depending on provider); some analysts expect it to settle around $2.50–3.00/hr by Q4 2026 as TSMC ramps supply. The GB200 superchip commands a premium, averaging ~$18.79/hr.
- **Availability:** Lead times for data-center GPUs are reported at **36–52 weeks**, with Blackwell-class orders slipping into Q1 2027. The shortage stems from hyperscalers consuming ~75% of available supply (having committed $600–630B in AI infrastructure capex) and TSMC's CoWoS packaging capacity being sold out through 2025–2026 — a structural, not cyclical, constraint expected to persist through 2026–2027.

## API Consumption vs. Self-Hosting

**API pricing (frontier models, 2026):** roughly $1–10/million input tokens and $5–50/million output tokens depending on model tier. Output tokens consistently cost ~5x input tokens. Cached input tokens cost ~10% of base rate; batch processing gets ~50% off.

**Self-hosting economics:** Running a self-hosted open-weight model only decisively beats a *frontier* API at roughly 160–256 million tokens/month, at 60–70% GPU utilization. Against *budget* open-weight API providers (DeepSeek, Together, DeepInfra, priced ~$0.14–0.50/million tokens), self-hosting rarely wins on raw cost — break-even runs into the billions of tokens/month, "effectively unreachable" for smaller operators. A rented GPU costs the same idle or busy: at 10% utilization, per-token self-hosted cost runs roughly 10x higher than at full load. Hidden costs (ops time, model updates, VRAM surprises) can multiply true self-hosting costs by 1.3–5x beyond naive calculations.

**Practical tradeoff for agentic workloads:** agents needing frontier-level reasoning/tool-use for complex, multi-step tasks effectively require API access to top-tier models — no viable self-hosted substitute matches quality at comparable cost. A common hybrid pattern: route the large majority of high-volume, lower-complexity agent steps to a self-hosted or budget model, and reserve frontier API calls for the harder subset of decisions.

## Cost at Scale (Agent-Hours, Parallel Instances)

Figures here are directional industry estimates, not standardized benchmarks:
- Token costs reportedly dominate agent operating budgets (~64% of spend), with infrastructure (~13%), vector DB/memory (~13%), and monitoring (~8%) making up the rest.
- Reported monthly costs for production agent deployments range from ~$3,200–13,000/month at enterprise conversational-agent scale.

## Key Takeaway

At small-to-medium scale, API consumption is cheaper and operationally simpler. Self-hosting becomes economically attractive only at high sustained volume with disciplined GPU utilization, and even then only decisively beats *budget* API providers, not frontier ones. GPU scarcity is itself inflating both rental and ownership costs through 2026, reinforcing the API route as the lower-risk default for most agentic deployments unless volume is very large and predictable.

## Sources

- [H100 Rental Prices Compared](https://intuitionlabs.ai/articles/h100-rental-prices-cloud-comparison) — IntuitionLabs — H100 rental price range across 15+ providers
- [AWS Raises GPU Prices 15%](https://www.devzero.io/blog/aws-quietly-raises-gpu-prices-15-over-the-weekend-what-engineering-leaders-need-to-know) — DevZero — AWS H200 price increase details (Jan 2026)
- [EC2 GPU Instances Guide (July 2026)](https://www.thundercompute.com/blog/ec2-gpu-instances) — Thunder Compute — AWS p5/p5e H100/H200 pricing breakdown
- [Cloud GPU Pricing Comparison: AWS vs Azure vs GCP](https://www.cloudzero.com/blog/cloud-gpu-pricing-comparison/) — CloudZero — cross-provider H100 node pricing
- [NVIDIA B200 Cloud Pricing 2026](https://www.spheron.network/blog/nvidia-b200-cloud-pricing-2026/) — Spheron — B200 rental price range and averages
- [GB200 Cloud Pricing: Compare 8+ Providers](https://getdeploying.com/gpus/nvidia-gb200) — GetDeploying — GB200 superchip pricing
- [GPU Shortage 2026](https://www.spheron.network/blog/gpu-shortage-2026/) — Spheron — GPU supply constraints, lead times, HBM shortage
- [The GPU Supply Chain Crisis](https://www.vamsitalkstech.com/ai/the-gpu-supply-chain-crisis-what-every-enterprise-cio-must-know-in-2026/) — Vamsi Talks Tech — Blackwell lead times, structural supply constraints
- [Anthropic API Pricing 2026](https://www.cloudzero.com/blog/claude-api-pricing/) — CloudZero — Claude model per-token pricing tiers
- [Self-Hosting an LLM vs. API: Real Cost Math (2026)](https://cloudzy.com/blog/self-hosting-open-weight-llm-gpu-vps-cost/) — Cloudzy — break-even token volume analysis by API tier, utilization impact
- [Self-Host LLM vs API 2026: Break-Even at $20K/Month](https://tokenmix.ai/blog/self-host-llm-vs-api) — Tokenmix — alternative break-even threshold and hybrid routing strategy
- [Cost to Run AI Agents at Scale: Full TCO Breakdown 2026](https://atlan.com/know/ai-agent/cost-to-run-ai-agents-at-scale/) — Atlan — agent-hour infrastructure costs, cost-category breakdown

*Note: Many figures above come from industry blogs rather than official cloud-provider pricing calculators and vary by source; treat exact dollar figures as directional estimates.*
