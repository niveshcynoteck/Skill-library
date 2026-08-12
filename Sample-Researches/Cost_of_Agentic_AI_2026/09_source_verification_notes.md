# Source Verification Notes

## Methodology

This report was compiled from eight independent research passes (Background/Definitions, LLM API Pricing, Compute Infrastructure, Workflow Cost Drivers, Enterprise Spend, Historical Cost Trend, Cost Optimization, Market Forecasts). Each pass was instructed to prioritize official vendor documentation and reputable analyst sources, cross-verify key figures across at least two sources where possible, and explicitly flag unverifiable or vendor-blog-only statistics rather than presenting them as settled fact.

## Link Validation

All reference URLs collected across the eight sections (~75 total) were programmatically checked for reachability via automated HTTP requests, followed by manual spot-checks (WebFetch) on anomalies.

**Results:**

| Outcome | Explanation |
|---|---|
| 200 OK (majority) | Verified reachable, including all official vendor pricing pages (Anthropic, OpenAI, Google), Epoch AI, arXiv, and most industry blogs |
| 403 (Gartner ×4, Bloomberg, my.idc.com, openai.com) | Known bot-blocking behavior on these domains — confirmed via manual spot-check, not evidence of broken pages |
| Timeout (McKinsey ×2) | Could not be independently re-confirmed in this pass; likely bot-throttling given the domain's reputable standing, but flagged rather than assumed valid |
| 404 (Anthropic pricing page) | Genuinely broken — the original URL cited by the pricing research agent no longer resolves. **Corrected** to [platform.claude.com/docs/en/about-claude/pricing](https://platform.claude.com/docs/en/about-claude/pricing), fetched directly and used to verify every Claude pricing figure in Section 2 |
| 404 (informationmatters.net) | Genuinely broken. This was only a secondary cross-check pointer in the market-forecast research (not load-bearing for any cited figure) and has been **dropped** from the reference list |
| 429 (startups.com) | Rate-limited on automated check; manually confirmed live |
| Connection error (cloudzy.com) | Transient failure on automated check; manually confirmed live and functional |
| 406 (vamsitalkstech.com) | Manually confirmed live and functional — the 406 response was specific to the automated checker's request headers |

## Figures Flagged as Unverified or Directional

The following statistics appear in the report but originate from vendor/consultancy blogs rather than primary research, and are explicitly flagged as such in their respective sections:

- Specific token-multiplier figures beyond Anthropic's own published ~4x/~15x (e.g., "5–30x," "$0.04 vs $1.20 per task")
- Model-routing cost-reduction percentages (40–85%, up to 98%)
- Self-hosting break-even thresholds (which vary by source: $4,200/month, ~500M tokens/month, 160–256M tokens/month depending on comparison API tier)
- Per-employee AI spend benchmarks (~$2,068/employee) — could not be traced to a named primary study
- The 5–30x "pilot vs. production" token gap attributed to Gartner (cited secondhand, not from a primary Gartner document)

## Facts Confirmed Against Primary/Official Sources

- All Anthropic, OpenAI, and Google per-token pricing figures (Section 2) — confirmed directly against each vendor's official pricing documentation
- Epoch AI's and a16z's per-token cost-decline rates (Section 6) — corroborated across two independent, research-oriented sources
- Gartner's headline 2026 market-spend figures ($2.59T, $206.5B) — confirmed via the primary press release plus independent secondary coverage
- The Rutgers University arXiv preprint on retry/context-contamination effects (Section 4) — a primary academic source, directly fetched
