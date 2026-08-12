# 4. Architectures & Data Platforms

## Two separate decisions, not five competing options

A common confusion is treating warehouse, lake, lakehouse, fabric, and mesh as alternatives. Experts argue they address **two different dimensions**: [20]

| Dimension | Options | What you decide |
|---|---|---|
| **Platform** (where data lives) | Data warehouse → Data lake → **Data lakehouse** | Storage technology and compute model |
| **Operating pattern** (governance & ownership) | Data fabric, Data mesh | Integration, governance, and ownership model |

## Platform evolution: why lakehouse wins for AI

| Feature | Warehouse | Data lake | Lakehouse |
|---|---|---|---|
| Storage cost | High (compute-optimized) | Low (object storage) | Low |
| ACID transactions | Yes | No (data swamp risk) | Yes (via table formats like Iceberg/Delta) |
| Schema | Strict | Flexible | Structured + flexible |
| ML-ready | Limited | Yes | Yes (analytics + ML) |
| Best for | BI, reports | ML training, exploration | **AI-ready modern stack** |

*Table adapted from Addepto's comparison.* [20]

## Data fabric vs. data mesh

- **Data fabric** is an evolutionary, technology-led approach: it connects and governs existing systems using metadata, knowledge graphs, and a semantic layer, without requiring organizational change. [21]
- **Data mesh** is a revolutionary, organization-led approach: it decentralizes ownership to business domains, treats **data as a product**, and requires cultural change. [21]
- **Trend for 2027: convergence.** Forecasts point to hybrid models combining domain ownership (mesh) with unified oversight and connectivity (fabric). [22] Academic analysis likewise observes mature enterprises "borrowing concepts across architectural boundaries" rather than adhering to one paradigm. [23]

## Real-time and edge computing

- Streaming platforms (Apache Kafka, Flink, Pinot) and event-driven architectures power dynamic pricing, fraud detection, and predictive maintenance. [4]
- IDC forecasts more than **60% of enterprises will deploy unified edge frameworks by 2027**, cutting latency from 60–100 ms (cloud) to under 10 ms (edge). [24]
- Microsoft Fabric has emerged as an end-to-end consolidation play — lakehouse storage, pipelines, Power BI, and governance under one license. [25] [20]

## Visual

See `visuals/platform-evolution.mmd` for a timeline of the data platform evolution.
