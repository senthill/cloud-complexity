# CloudComplexity: Benchmarking the Infrastructure Tax

`CloudComplexity` is a data-driven tool designed to quantify the cognitive overhead of modern cloud platforms. By analyzing the REST API surface area (total operations and configurable attributes) across 14 providers, it highlights the "Infrastructure Tax" paid by engineers in the pursuit of "cloud-native" architectures.

## Core Findings (Global Cloud Scope)

| Provider | Scope | Total APIs (Ops) | Total Attributes | Complexity Rating |
| :--- | :--- | :--- | :--- | :--- |
| **Microsoft Azure** | 232 Resource Providers | **13,354** | **63,806** | ![High](https://img.shields.io/badge/-Extreme-red) |
| **Amazon Web Services** | 417 Services | **17,928** | **62,373** | ![High](https://img.shields.io/badge/-High-red) |
| **Google Cloud** | 304 APIs | **6,100** | **18,249** | ![Med](https://img.shields.io/badge/-Med-orange) |
| **Alibaba Cloud** | Core IaaS/PaaS | **>9,500*** | **>35,000*** | ![Med](https://img.shields.io/badge/-Med-orange) |

*\*Alibaba metrics are refined estimates based on a subset of OpenAPI specifications.*

## Verified Methodology
Unlike generic "service counts," our metrics are derived from direct parsing of official cloud-provider specifications:
1.  **AWS**: Parsed from `botocore` service models.
2.  **GCP**: Fetched dynamically via Google Discovery API (v1).
3.  **Azure**: **Verified via local scan** of the `azure-rest-api-specs` repository (March 2026), filtering for the latest stable version of every resource provider.
4.  **PaaS/Edge**: Based on public OpenAPI/Swagger definitions (e.g., DigitalOcean, Vercel).

## Supported Categories
We compare 14 providers across 8 high-stakes service categories:
- **Compute**: VM and App Container management.
- **Storage**: Block, Object, and File storage surface areas.
- **Databases**: Managed SQL and NoSQL configuration depth.
- **Kubernetes**: Managed K8s (EKS, AKS, GKE, DOKS).
- **Networking**: VPC, Firewalls, and Load Balancing complexity.
- **Serverless**: Function and deployment triggering surface.

## Quick Start
```bash
# Analyze all categories
python -m src.main all

# Compare compute surface across all providers
python -m src.main compute

# View detailed inventory for Azure (requires local spec clone)
python scripts/azure_local_scanner.py azure-specs/specification
```

## Documentation
- [Benchmark Results](./docs/benchmark_results.md) - Consolidated findings and color-coded complexity tax.
- [Feature Audit](./docs/feature_audit.md) - Service-to-Doc mapping for "Ground Truth" verification.
- [Azure Deep Dive](./docs/azure_deep_dive.md) - Analysis of Azure's 270,000-file specification repository.
- [Strategic Blog Series](./docs/blog/strategic_analysis.md) - Thought leadership on the shift to Intent-Based APIs.

---
Developed by Senthil as part of the `CloudPorter` suite.
