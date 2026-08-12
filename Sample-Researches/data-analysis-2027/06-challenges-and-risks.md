# 6. Challenges & Risks

## Data quality and trust

- **26% of enterprise data is considered untrustworthy**, and data volumes grow ~25% a year — trust does not scale automatically. [7]
- **62% of organizations cite lack of data governance as the main blocker to AI initiatives.** [8]
- Data is often fragmented across dozens of systems, and poor metadata starves AI models of context. [32]

## AI risks in analytics

| Risk | What it is | Mitigation |
|---|---|---|
| **Hallucination** | AI invents or misstates facts/numbers | Grounding with RAG, citations, human validation |
| **Silent transformation errors** | AI produces plausible but wrong output | Testing built into pipelines (data-as-code) |
| **Over-reliance on autonomy** | Automated actions taken without validation | Human-in-the-loop guardrails; "guardian agents" [3] |
| **Synthetic data failures** | Fabricated data that misrepresents reality | 60% of D&A leaders expected to face critical failures by 2027; needs metadata management [2] |
| **Bias** | Models inherit training-data bias → discrimination | Diverse datasets, fairness audits |
| **Privacy breaches** | Sensitive/PII data leaked via AI systems | Access controls, masking, compliance (GDPR/CPRA/HIPAA) [32] |
| **Security attacks** | Prompt injection, data poisoning, denial-of-wallet | Strong security foundations and permissions [33] |

## The adoption paradox

- Gartner predicts **over 40% of agentic AI projects will be canceled by end of 2027** due to escalating costs, unclear business value, or inadequate risk controls — with many vendors guilty of "agent washing." [34]
- MIT research cited by insightsoftware claims **95% of organizations see zero return on their AI investment** — a sharp counterpoint to the hype. [35]
- The **quality vs. privacy tradeoff**: measures like data masking can degrade data quality and model accuracy, so governance must balance both. [32]
