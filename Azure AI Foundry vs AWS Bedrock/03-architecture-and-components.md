# Architecture & Key Components

| Component | Azure AI Foundry | AWS Bedrock |
|---|---|---|
| **Model catalog** | 1,900+ models from Microsoft, OpenAI, Anthropic, Meta, and others ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/foundry/what-is-foundry)) | A curated catalog including Claude, Llama 4, Mistral, Cohere, AI21, Titan, Nova, Stability, and (per industry sources) OpenAI models now available too |
| **Agents** | **Foundry Agent Service** — declarative "prompt agents" or "hosted agents" running custom code; hosted agents expected to reach GA around July 2026 | **Bedrock AgentCore** (GA late 2025) — end-to-end agent platform with its own runtime, gateway, memory, identity management, policy engine, code interpreter, browser tool, evaluations, and observability |
| **Tools/integration** | Tools tab connects to MCP servers, A2A endpoints, Azure AI Search, SharePoint, Fabric, and 1,400+ business systems | Native integration with IAM, KMS, VPC endpoints, CloudWatch, CloudTrail |
| **Knowledge/RAG** | Built-in memory (procedural, user, session — public preview) and retrieval tools | **Bedrock Knowledge Bases** — managed RAG: point at an S3 bucket, choose parsing/chunking, embedding model, and vector store |
| **Safety/governance** | Content filters, Microsoft Entra ID, RBAC, network isolation, Azure Policy, under one control plane | **Bedrock Guardrails** — six configurable safety policies: content filters, denied topics, word filters, PII redaction, contextual grounding checks, and automated-reasoning fact validation |
| **Observability** | Built-in tracing, monitoring, evaluation dashboards | Evaluations and observability built into AgentCore |
