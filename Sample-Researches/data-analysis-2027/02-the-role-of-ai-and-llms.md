# 2. The Role of AI & LLMs

Generative AI (GenAI) and large language models (LLMs) are the single biggest force reshaping data analysis workflows between 2025 and 2027.

## How AI changes the analyst's workflow

| Traditional workflow | 2027 AI-assisted workflow |
|---|---|
| Write SQL manually | Ask questions in natural language; AI generates SQL |
| Manually build dashboards and reports | AI drafts summaries, narratives, and visualizations |
| Analysts detect anomalies by inspection | Agents monitor data continuously and flag anomalies proactively |
| 50–70% of time on data cleanup and SQL | More time on interpretation and business judgment |
| Static weekly/monthly reports | Continuous, adaptive insights |

## Key facts and predictions

- **75% of new analytics content** will be contextualized for intelligent applications through GenAI by 2027 (Gartner). [3]
- By **2028, GenAI-powered narratives and dynamic visualizations will replace 60% of traditional dashboards** (Gartner). [10]
- Over 50% of analytics/AI leaders already use AI tools for automated insights and natural-language queries (Gartner survey, Oct–Dec 2024). [3]
- **Small, task-specific AI models will outpace general-purpose LLMs by 3x by 2027** — a shift toward leaner, cheaper, domain-focused models. [10]

## From chatbots to agentic analytics

- **Agentic analytics** is a category where LLM-based agents autonomously decompose a business question into sub-tasks, retrieve context from a **semantic layer**, execute queries against the warehouse, evaluate results, and return a reasoned answer with a visible reasoning trace. [11]
- The **Model Context Protocol (MCP)** has emerged as an open standard for connecting agents to data systems, forming the orchestration layer of agentic stacks. [11] [12]
- Academic research confirms the trend: a 2025 survey on "LLM/Agent-as-Data-Analyst" documents natural-language interfaces (NL2SQL), semantic analysis, and autonomous pipeline orchestration as the new paradigm. [13]
- Real enterprise tooling already embeds this: **Microsoft Fabric + Copilot, Snowflake Cortex AI, Databricks AI/BI Genie, and ThoughtSpot Sage** are flagship examples of conversational/agentic BI. [14]

## Important caveat

AI agents are **not infallible**. Gartner warns that agents "must be used collectively with effective governance and risk management." [2] Independent research notes agents fail on data tasks without well-defined business terms and governed data — the semantic layer is the make-or-break component. [11]

## Visual

See `visuals/agentic-analytics-workflow.mmd` for an architecture diagram of the 2027 agentic analytics stack.
