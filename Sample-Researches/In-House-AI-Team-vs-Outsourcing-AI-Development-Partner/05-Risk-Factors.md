# 5. Risk Factors

This is where outsourcing's advantages get counterbalanced most seriously.

## Data security & third-party breach exposure

- The global average cost of a data breach reached **$4.88 million** in 2024. ([IBM Cost of a Data Breach Report 2024](https://www.ibm.com/think/insights/whats-new-2024-cost-of-a-data-breach-report))
- Verizon's **2025 Data Breach Investigations Report** found third-party involvement in breaches **doubled from ~15% to 30%** year-over-year — with high-profile examples (Change Healthcare, CDK Global, Blue Yonder) showing how a vendor breach can cascade into major operational downtime for the client. ([Verizon](https://www.verizon.com/about/news/2025-data-breach-investigations-report), [Help Net Security summary](https://www.helpnetsecurity.com/2025/04/23/verizon-2025-data-breach-investigations-report-dbir/))
- Critically: **a data breach or compliance failure at your outsourcing vendor is still your legal responsibility.**

## IP ownership and protection

- Roughly **43%** of companies that outsource software development report concerns about IP theft or data breaches (per a 2024 industry survey cited by [ValueCoders](https://www.valuecoders.com/blog/software-engineering/guide-to-safeguarding-your-intellectual-property-when-outsourcing/)).
- Common failure mode: contracts that don't clearly assign ownership of derivative works, model weights, or fine-tuned outputs — leading to disputes later.
- Subcontracting is a hidden multiplier of this risk: some outsourcing firms pass work to freelancers or other companies, which multiplies exposure and blurs accountability.

## Vendor lock-in

- Building critical operations entirely on one proprietary vendor/model creates fragility: if the vendor changes terms, deprecates an API, or raises prices, your operations can be disrupted with little warning. ([Ability.ai](https://www.ability.ai/blog/ai-vendor-lock-in-risks))
- More than half of organizations report they **cannot rebuild an outsourced capability quickly** if the relationship ends unexpectedly — a serious continuity risk for anything business-critical.

## Compliance & data residency

- Under GDPR, even *accessing* EU-resident data from an offshore location (e.g., an outsourced QA analyst viewing data from outside the EEA) can constitute a regulated cross-border transfer, requiring Standard Contractual Clauses, Binding Corporate Rules, or an adequacy decision. ([PreMI.io](https://www.premai.io/blog/ai-data-residency-requirements-by-region-the-complete-enterprise-compliance-guide/), [Truto](https://truto.one/blog/how-to-handle-eu-data-residency-and-gdpr-compliance-for-mcp-servers/))
- GDPR penalties can reach up to a percentage of global turnover for serious violations — a real financial tail risk if an outsourcing arrangement mishandles EU personal data.
- If your vendor is US-headquartered, the US CLOUD Act can compel data access regardless of where the servers physically sit — worth knowing if data sovereignty is a hard requirement.

## Mitigations (if you do outsource)

Per [Futureproofing.dev](https://www.futureproofing.dev/resources/build-vs-outsource/outsource-ai-development-guide): choose a managed-team model over unstructured "body-shop" staffing, contractually lock in IP ownership and work-for-hire assignment, and require a security attestation plus a data processing agreement before data ever changes hands.
