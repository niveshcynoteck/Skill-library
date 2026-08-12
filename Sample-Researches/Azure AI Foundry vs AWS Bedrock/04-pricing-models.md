# Pricing Models

| | Azure AI Foundry | AWS Bedrock |
|---|---|---|
| **Structure** | Each service/product (Models, Agent Service, Tools) has its **own separate billing model** — no single unified price page; users are directed to per-service pricing pages and the Azure Pricing Calculator ([Microsoft Learn - AI Foundry pricing page](https://azure.microsoft.com/en-us/pricing/details/ai-foundry/)) | Officially documented tiers: **On-Demand** (pay-per-token), **Batch** (50% lower than on-demand for select models), **Provisioned Throughput** (hourly, with 1-month/6-month/no-commitment options), and **Service Tiers** — Standard, Flex (50% discount), Priority (75% premium for lower latency) ([AWS Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/)) |
| **Reserved/commitment options** | Microsoft Agent Pre-Purchase Plan: 1-year metered commitment with tiered discounts (5% at 20,000 ACUs, 10% at 100,000 ACUs, 15% at 500,000 ACUs) | Provisioned Throughput commitments (1-month or 6-month) for predictable high-volume workloads |
| **Storage costs** | Not detailed in official pricing overview page | Knowledge base storage priced at $5/GB/month (per AWS docs) |

## Third-Party Cost Estimates (unverified against official rate cards — treat as industry estimates)

- GPT-4o on Azure: ~$2.50/M input tokens, $10/M output tokens
- Claude 3.5 Sonnet on Bedrock: ~$3/M input tokens, $15/M output tokens
- For 10–50M tokens/month, some analyses suggest Bedrock costs 15–25% lower; Azure becomes more competitive at scale (150–200M tokens/month) with reserved capacity (Provisioned Throughput Units)
