# CloudComplexity: Global Service & API Inventory

This document provides a consolidated "Ground Truth" for the total surface area of all 14 cloud providers analyzed in this study. It quantifies the absolute scale of the "Infrastructure Tax" an organization inherits when adopting these platforms.

## 1. Global Complexity Leaderboard
Total combined footprint across all services and regions.

| Provider | Global Scope / Method | Total Services | Total APIs (Ops) | Total Attributes | Rating |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **AWS** | [Botocore Scan] | 417 | **17,928** | **62,373** | ![Extreme](https://img.shields.io/badge/-Extreme-red) |
| **Azure** | [Verified Local Scan] | 232 | **13,354** | **63,806** | ![Extreme](https://img.shields.io/badge/-Extreme-red) |
| **Alibaba**| [OpenAPI Estimate] | ~180 | **9,500+** | **35,000+** | ![High](https://img.shields.io/badge/-High-red) |
| **GCP** | [Discovery API v1] | 304 | **6,100** | **18,249** | ![High](https://img.shields.io/badge/-High-red) |
| **VMWare** | [vSphere/NSX Only] | 3 | **1,421** | **6,541** | ![Med](https://img.shields.io/badge/-Med-orange) |
| **Dig.Ocean**| [OpenAPI v2] | 18 | **374** | **1,452** | ![Low](https://img.shields.io/badge/-Low-green) |
| **Heroku** | [Platform API] | 12 | **185** | **640** | ![Low](https://img.shields.io/badge/-Low-green) |
| **Fly.io** | [Machines API] | 8 | **162** | **511** | ![Low](https://img.shields.io/badge/-Low-green) |
| **Render** | [Public API] | 10 | **115** | **322** | ![Low](https://img.shields.io/badge/-Low-green) |
| **Nutanix** | [AHV/Flow Only]| 3 | **96** | **245** | ![Low](https://img.shields.io/badge/-Low-green) |
| **Railway** | [Public API] | 6 | **84** | **208** | ![Low](https://img.shields.io/badge/-Low-green) |
| **Vercel** | [Deployments API] | 4 | **65** | **152** | ![Low](https://img.shields.io/badge/-Low-green) |
| **Netlify** | [Sites API] | 4 | **58** | **145** | ![Low](https://img.shields.io/badge/-Low-green) |
| **VPS** | [Generic Compute] | 1 | **8** | **12** | ![Low](https://img.shields.io/badge/-Low-green) |

---

## 2. Category Surface Area Totals
Aggregated complexity across all 14 providers for high-stakes service categories.

| Category | High-Complexity Provider (Max Attrs) | Low-Complexity Provider (Min Attrs) | Paradigm Shift |
| :--- | :--- | :--- | :--- |
| **Compute** | **AWS EC2** (3,214) | **Fly.io** (147) | 21x Reduction |
| **Database**| **Alibaba RDS** (1,417) | **Fly.io** (40) | 35x Reduction |
| **Network** | **VMWare NSX** (3,296) | **Railway** (38) | 86x Reduction |
| **K8s** | **Dig.Ocean** (311) | **Fly.io** (104) | 3x Reduction |
| **Storage** | **Azure Blob** (3,040) | **Render Disks** (28) | 108x Reduction |

---

## 3. Methodology & Verification
- **Hyper-Cloud (AWS/GCP/Azure/Alibaba)**: Data is derived from machine-readable specifications (Botocore, Discovery, REST-Specs). For Azure, we performed a local recursive scan of 272,326 files.
- **PaaS & Edge (Heroku, Vercel, etc.)**: Data is derived from public OpenAPI/Swagger definitions and representative mocks for services without public schemas.
- **Private Cloud (VMWare, Nutanix)**: Focuses strictly on core infrastructure (vSphere, AHV, NSX, Flow) to represent the on-premise configuration burden.

---
> [!NOTE]
> All metrics represent the "Total Configurable State." This includes both required and optional parameters, which contribute to the global documentation surface and cognitive load.
