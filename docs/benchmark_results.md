# CloudComplexity: Benchmark Results Summary

This document contains the consolidated findings from the `CloudComplexity` benchmarking tool. It quantifies the "API Complexity Tax" by measuring the total number of APIs, Verbs, and Attributes across 14 cloud providers.

## Key Metrics Definition
- $\textsf{\color{red}{High Complexity}}$: > 1,000 attributes (Extreme configuration burden)
- $\textsf{\color{orange}{Medium Complexity}}$: 200 - 1,000 attributes (Moderate overhead)
- $\textsf{\color{green}{Low Complexity}}$: < 200 attributes (Lean/Intent-based)

---

## 1. Compute Service Comparison
Focus: Raw Virtual Machine / App Container management API surface area.

| Provider | Service | Total APIs | Total Attributes | Complexity Rating |
| :--- | :--- | :--- | :--- | :--- |
| **AWS** | EC2 | 469 | 3,214 | ![High](https://img.shields.io/badge/-High-red) |
| **GCP** | Compute | 184 | 624 | ![Med](https://img.shields.io/badge/-Med-orange) |
| **Azure** | Compute | 284 | 1,842 | ![High](https://img.shields.io/badge/-High-red) |
| **Alibaba** | ECS | 214 | 1,422 | ![High](https://img.shields.io/badge/-High-red) |
| **VMWare** | vSphere | 450 | 2,250 | ![High](https://img.shields.io/badge/-High-red) |
| **Nutanix** | AHV | 45 | 112 | ![Low](https://img.shields.io/badge/-Low-green) |
| **Heroku** | Apps | 52 | 182 | ![Low](https://img.shields.io/badge/-Low-green) |
| **Render** | Services | 32 | 96 | ![Low](https://img.shields.io/badge/-Low-green) |
| **Fly.io** | Machines | 42 | 147 | ![Low](https://img.shields.io/badge/-Low-green) |
| **Dig.Ocean**| Droplets | 62 | 310 | ![Med](https://img.shields.io/badge/-Med-orange) |
| **Railway** | Services | 26 | 78 | ![Low](https://img.shields.io/badge/-Low-green) |
| **VPS** | Compute | 8 | 12 | ![Low](https://img.shields.io/badge/-Low-green) |

---

## 2. Managed Database Service
Focus: Configuration surface for SQL/NoSQL managed instances.

| Provider | Service | Total APIs | Total Attributes | Complexity Rating |
| :--- | :--- | :--- | :--- | :--- |
| **AWS** | RDS | 163 | 1,162 | ![High](https://img.shields.io/badge/-High-red) |
| **GCP** | SQLAdmin | 74 | 210 | ![Med](https://img.shields.io/badge/-Med-orange) |
| **Azure** | Azure SQL | 112 | 593 | ![Med](https://img.shields.io/badge/-Med-orange) |
| **Alibaba** | RDS | 363 | 1,478 | ![High](https://img.shields.io/badge/-High-red) |
| **Heroku** | Postgres | 33 | 79 | ![Low](https://img.shields.io/badge/-Low-green) |
| **Render** | Postgres | 24 | 52 | ![Low](https://img.shields.io/badge/-Low-green) |
| **Fly.io** | Postgres | 15 | 32 | ![Low](https://img.shields.io/badge/-Low-green) |
| **Dig.Ocean**| Databases | 67 | 267 | ![Med](https://img.shields.io/badge/-Med-orange) |
| **Railway** | Databases | 23 | 47 | ![Low](https://img.shields.io/badge/-Low-green) |

---

## 3. Managed Kubernetes (K8s)
Focus: Cluster, node pool, and network integration API surface.

| Provider | Service | Total APIs | Total Attributes | Complexity Rating |
| :--- | :--- | :--- | :--- | :--- |
| **AWS** | EKS | 64 | 277 | ![Med](https://img.shields.io/badge/-Med-orange) |
| **GCP** | GKE | 69 | 217 | ![Med](https://img.shields.io/badge/-Med-orange) |
| **Azure** | AKS | 59 | 223 | ![Med](https://img.shields.io/badge/-Med-orange) |
| **Alibaba** | ACK | 139 | 411 | ![Med](https://img.shields.io/badge/-Med-orange) |
| **Fly.io** | FKS | 31 | 110 | ![Low](https://img.shields.io/badge/-Low-green) |
| **Dig.Ocean**| DOKS | 74 | 317 | ![Med](https://img.shields.io/badge/-Med-orange) |

---

## 4. Storage Benchmarks (Block, Object, File)

### 4.1 Block Storage (Volumes/Disks)
| Provider | Service | Total APIs | Total Attributes | Complexity Rating |
| :--- | :--- | :--- | :--- | :--- |
| **AWS** | EBS (EC2) | 62 | 218 | ![Med](https://img.shields.io/badge/-Med-orange) |
| **GCP** | Disks (Compute) | 34 | 92 | ![Low](https://img.shields.io/badge/-Low-green) |
| **Azure** | Disks (Compute) | 45 | 118 | ![Low](https://img.shields.io/badge/-Low-green) |
| **VMWare** | vSAN | 495 | 2,007 | ![High](https://img.shields.io/badge/-High-red) |
| **Nutanix** | Volumes | 41 | 110 | ![Low](https://img.shields.io/badge/-Low-green) |
| **Render** | Volumes | 12 | 23 | ![Low](https://img.shields.io/badge/-Low-green) |
| **Fly.io** | Volumes | 22 | 71 | ![Low](https://img.shields.io/badge/-Low-green) |
| **Dig.Ocean**| Volumes | 33 | 116 | ![Low](https://img.shields.io/badge/-Low-green) |
| **Railway** | Volumes | 8 | 11 | ![Low](https://img.shields.io/badge/-Low-green) |

### 4.2 Object Storage (S3/GCS/Blob/OSS)
| Provider | Service | Total APIs | Total Attributes | Complexity Rating |
| :--- | :--- | :--- | :--- | :--- |
| **AWS** | S3 | 111 | 714 | ![Med](https://img.shields.io/badge/-Med-orange) |
| **GCP** | Cloud Storage | 82 | 417 | ![Med](https://img.shields.io/badge/-Med-orange) |
| **Azure** | Blob Storage | 872 | 7,347 | ![High](https://img.shields.io/badge/-High-red) |
| **Alibaba** | OSS | 185 | 1,383 | ![High](https://img.shields.io/badge/-High-red) |
| **Dig.Ocean**| Spaces | 21 | 59 | ![Low](https://img.shields.io/badge/-Low-green) |

### 4.3 File Storage (EFS/NAS/Filestore)
| Provider | Service | Total APIs | Total Attributes | Complexity Rating |
| :--- | :--- | :--- | :--- | :--- |
| **AWS** | EFS | 31 | 79 | ![Low](https://img.shields.io/badge/-Low-green) |
| **GCP** | Filestore | 26 | 66 | ![Low](https://img.shields.io/badge/-Low-green) |
| **Azure** | Azure Files | 872 | 7,347 | ![High](https://img.shields.io/badge/-High-red) |
| **Alibaba** | NAS | 72 | 429 | ![Med](https://img.shields.io/badge/-Med-orange) |

---

## 5. Serverless & Functions
Focus: Deployment and event triggering surface area.

| Provider | Service | Total APIs | Total Attributes | Complexity Rating |
| :--- | :--- | :--- | :--- | :--- |
| **AWS** | Lambda | 85 | 355 | ![Med](https://img.shields.io/badge/-Med-orange) |
| **GCP** | Functions | 14 | 34 | ![Low](https://img.shields.io/badge/-Low-green) |
| **Azure** | Functions | 54 | 184 | ![Low](https://img.shields.io/badge/-Low-green) |
| **Alibaba** | FC | 42 | 131 | ![Low](https://img.shields.io/badge/-Low-green) |
| **Vercel** | Deployments | 31 | 63 | ![Low](https://img.shields.io/badge/-Low-green) |
| **Netlify** | Sites | 27 | 70 | ![Low](https://img.shields.io/badge/-Low-green) |

---

## 6. Networking Comparison
Focus: VPC, Subnet, Firewall, and Service Mesh configuration.

| Provider | Service | Total APIs | Total Attributes | Complexity Rating |
| :--- | :--- | :--- | :--- | :--- |
| **AWS** | EC2/VPC | 249 | 1,128 | ![High](https://img.shields.io/badge/-High-red) |
| **Azure** | Network | 560 | 2,808 | ![High](https://img.shields.io/badge/-High-red) |
| **Alibaba** | VPC | 310 | 1,698 | ![High](https://img.shields.io/badge/-High-red) |
| **VMWare** | NSX | 659 | 3,260 | ![High](https://img.shields.io/badge/-High-red) |
| **Nutanix** | Flow | 30 | 64 | ![Low](https://img.shields.io/badge/-Low-green) |
| **Heroku** | Private Sp. | 24 | 70 | ![Low](https://img.shields.io/badge/-Low-green) |
| **Fly.io** | Networking | 26 | 75 | ![Low](https://img.shields.io/badge/-Low-green) |

---
> [!NOTE]
> All metrics are generated using the `CloudComplexity` tool. Attributes include both required and optional parameters, representing the total configurable state for a given service.
