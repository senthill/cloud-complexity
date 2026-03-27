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
| **Azure** | Compute | 223 | 1,071 | ![High](https://img.shields.io/badge/-High-red) |
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
| **Azure** | SQL | 538 | 3,140 | ![High](https://img.shields.io/badge/-High-red) |
| **Alibaba** | RDS | 363 | 1,417 | ![High](https://img.shields.io/badge/-High-red) |
| **Heroku** | Postgres | 32 | 80 | ![Low](https://img.shields.io/badge/-Low-green) |
| **Render** | Postgres | 27 | 44 | ![Low](https://img.shields.io/badge/-Low-green) |
| **Fly.io** | Postgres | 21 | 40 | ![Low](https://img.shields.io/badge/-Low-green) |
| **Dig.Ocean**| Databases | 66 | 268 | ![Med](https://img.shields.io/badge/-Med-orange) |
| **Railway** | Databases | 21 | 41 | ![Low](https://img.shields.io/badge/-Low-green) |

---

## 3. Managed Kubernetes (K8s)
Focus: Cluster, node pool, and network integration API surface.

| Provider | Service | Total APIs | Total Attributes | Complexity Rating |
| :--- | :--- | :--- | :--- | :--- |
| **AWS** | EKS | 64 | 277 | ![Med](https://img.shields.io/badge/-Med-orange) |
| **GCP** | GKE | 69 | 217 | ![Med](https://img.shields.io/badge/-Med-orange) |
| **Azure** | AKS | 99 | 478 | ![Med](https://img.shields.io/badge/-Med-orange) |
| **Alibaba** | ACK | 139 | 411 | ![Med](https://img.shields.io/badge/-Med-orange) |
| **Fly.io** | FKS | 31 | 104 | ![Low](https://img.shields.io/badge/-Low-green) |
| **Dig.Ocean**| DOKS | 67 | 311 | ![Med](https://img.shields.io/badge/-Med-orange) |

---

## 4. Storage Benchmarks (Block, Object, File)

### 4.1 Block Storage (Volumes/Disks)
| Provider | Service | Total APIs | Total Attributes | Complexity Rating |
| :--- | :--- | :--- | :--- | :--- |
| **AWS** | EBS (EC2) | 62 | 218 | ![Med](https://img.shields.io/badge/-Med-orange) |
| **GCP** | Disks (Compute) | 34 | 92 | ![Low](https://img.shields.io/badge/-Low-green) |
| **Azure** | Disks (Compute) | 45 | 118 | ![Low](https://img.shields.io/badge/-Low-green) |
| **VMWare** | vSAN | 501 | 2,044 | ![High](https://img.shields.io/badge/-High-red) |
| **Nutanix** | Volumes | 38 | 91 | ![Low](https://img.shields.io/badge/-Low-green) |
| **Render** | Volumes | 12 | 28 | ![Low](https://img.shields.io/badge/-Low-green) |
| **Fly.io** | Volumes | 22 | 64 | ![Low](https://img.shields.io/badge/-Low-green) |
| **Dig.Ocean**| Volumes | 34 | 111 | ![Low](https://img.shields.io/badge/-Low-green) |
| **Railway** | Volumes | 8 | 12 | ![Low](https://img.shields.io/badge/-Low-green) |

### 4.2 Object Storage (S3/GCS/Blob/OSS)
| Provider | Service | Total APIs | Total Attributes | Complexity Rating |
| :--- | :--- | :--- | :--- | :--- |
| **AWS** | S3 | 111 | 714 | ![Med](https://img.shields.io/badge/-Med-orange) |
| **GCP** | Cloud Storage | 82 | 417 | ![Med](https://img.shields.io/badge/-Med-orange) |
| **Azure** | Storage (Account) | 116 | 592 | ![Med](https://img.shields.io/badge/-Med-orange) |
| **Alibaba** | OSS | 185 | 1,408 | ![High](https://img.shields.io/badge/-High-red) |
| **Dig.Ocean**| Spaces | 23 | 72 | ![Low](https://img.shields.io/badge/-Low-green) |

### 4.3 File Storage (EFS/NAS/Filestore)
| Provider | Service | Total APIs | Total Attributes | Complexity Rating |
| :--- | :--- | :--- | :--- | :--- |
| **AWS** | EFS | 31 | 79 | ![Low](https://img.shields.io/badge/-Low-green) |
| **GCP** | Filestore | 26 | 66 | ![Low](https://img.shields.io/badge/-Low-green) |
| **Azure** | Storage (Account) | 116 | 592 | ![Med](https://img.shields.io/badge/-Med-orange) |
| **Alibaba** | NAS | 72 | 452 | ![Med](https://img.shields.io/badge/-Med-orange) |

---

## 5. Serverless & Functions
Focus: Deployment and event triggering surface area.

| Provider | Service | Total APIs | Total Attributes | Complexity Rating |
| :--- | :--- | :--- | :--- | :--- |
| **AWS** | Lambda | 85 | 355 | ![Med](https://img.shields.io/badge/-Med-orange) |
| **GCP** | Functions | 14 | 34 | ![Low](https://img.shields.io/badge/-Low-green) |
| **Azure** | Web (App Service) | 692 | 3,606 | ![High](https://img.shields.io/badge/-High-red) |
| **Alibaba** | FC | 42 | 120 | ![Low](https://img.shields.io/badge/-Low-green) |
| **Vercel** | Deployments | 33 | 65 | ![Low](https://img.shields.io/badge/-Low-green) |
| **Netlify** | Sites | 28 | 67 | ![Low](https://img.shields.io/badge/-Low-green) |

---

## 6. Networking Comparison
Focus: VPC, Subnet, Firewall, and Service Mesh configuration.

| Provider | Service | Total APIs | Total Attributes | Complexity Rating |
| :--- | :--- | :--- | :--- | :--- |
| **AWS** | EC2/VPC | 249 | 1,128 | ![High](https://img.shields.io/badge/-High-red) |
| **GCP** | Compute/VPC | 93 | 427 | ![Med](https://img.shields.io/badge/-Med-orange) |
| **Azure** | Network | 747 | 3,075 | ![High](https://img.shields.io/badge/-High-red) |
| **Alibaba** | VPC | 310 | 1,710 | ![High](https://img.shields.io/badge/-High-red) |
| **VMWare** | NSX | 652 | 3,296 | ![High](https://img.shields.io/badge/-High-red) |
| **Nutanix** | Flow | 31 | 69 | ![Low](https://img.shields.io/badge/-Low-green) |
| **Dig.Ocean**| Networking | 84 | 324 | ![Med](https://img.shields.io/badge/-Med-orange) |
| **Heroku** | Private Sp. | 20 | 62 | ![Low](https://img.shields.io/badge/-Low-green) |
| **Render** | Networking | 13 | 33 | ![Low](https://img.shields.io/badge/-Low-green) |
| **Fly.io** | Networking | 29 | 75 | ![Low](https://img.shields.io/badge/-Low-green) |
| **Railway** | Networking | 16 | 38 | ![Low](https://img.shields.io/badge/-Low-green) |

---
> [!NOTE]
> All metrics are generated using the `CloudComplexity` tool and verified via local scan of Azure Specifications (Stable/Latest). Attributes include both required and optional parameters, representing the total configurable state for a given service.
