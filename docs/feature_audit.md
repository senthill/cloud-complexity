# CloudComplexity: Provider Feature Audit (Visualized)

$\textsf{\color{blue}{The "Ground Truth" for Service Mappings}}$

---

## 1. Hyper-Cloud Providers (IaaS & PaaS)

### ![AWS](https://img.shields.io/badge/-AWS-orange?style=flat-square&logo=amazon-aws&logoColor=white) 
| Category | Service | High-Level Offerings | Docs Link |
| :--- | :--- | :--- | :--- |
| **Compute** | **EC2** | x86, ARM, & Graviton; Spot/On-Demand. | [EC2 Docs](https://docs.aws.amazon.com/ec2/) |
| **Database** | **RDS** | MySQL, PostgreSQL, Oracle, SQL Server, Aurora. | [RDS Docs](https://docs.aws.amazon.com/rds/) |
| **Kubernetes** | **EKS** | Fargate; Managed Node Groups; IAM. | [EKS Docs](https://docs.aws.amazon.com/eks/) |

### ![GCP](https://img.shields.io/badge/-Google_Cloud-blue?style=flat-square&logo=google-cloud&logoColor=white)
| Category | Service | High-Level Offerings | Docs Link |
| :--- | :--- | :--- | :--- |
| **Compute** | **GCE** | VM instances; Tau T2A (ARM); Preemptible. | [GCE Docs](https://cloud.google.com/compute/docs) |
| **Database** | **Cloud SQL** | MySQL, PostgreSQL, SQL Server; HA. | [Cloud SQL Docs](https://cloud.google.com/sql/docs) |
| **Kubernetes** | **GKE** | Autopilot; Multicluster Ingress. | [GKE Docs](https://cloud.google.com/kubernetes-engine/docs) |

### ![Azure](https://img.shields.io/badge/-Microsoft_Azure-0078D4?style=flat-square&logo=microsoft-azure&logoColor=white)
| Category | Service | High-Level Offerings | Docs Link |
| :--- | :--- | :--- | :--- |
| **Compute** | **VMs** | Linux/Windows VMs; Proximity Placement. | [VM Docs](https://learn.microsoft.com/en-us/azure/virtual-machines/) |
| **Database** | **Azure SQL** | SQL Database, Managed Instances. | [Azure SQL Docs](https://learn.microsoft.com/en-us/azure/azure-sql/) |
| **Kubernetes** | **AKS** | Azure AD integration; Serverless Nodes. | [AKS Docs](https://learn.microsoft.com/en-us/azure/aks/) |

---

## 2. Infrastructure & HCI Providers

| Provider | Service | Key Features | Docs Link |
| :--- | :--- | :--- | :--- |
| **VMWare** | **vSphere** | vCenter, ESXi, DRS, vMotion. | [vSphere Docs](https://docs.vmware.com/en/VMware-vSphere/index.html) |
| **Nutanix** | **AHV** | One-click upgrades, Distributed Scaling. | [AHV Docs](https://www.nutanix.com/products/hyperconverged-infrastructure/ahv) |
| **Dig.Ocean**| **Droplets** | Basic, Gen Purpose, CPU-Optimized. | [Droplet Docs](https://docs.digitalocean.com/products/droplets/) |

---

## 3. Modern PaaS & App Platforms

| Provider | Service | Offerings / Details | Docs Link |
| :--- | :--- | :--- | :--- |
| **Heroku** | **Dynos** | Web, Worker, and One-off Containers. | [Dynos Docs](https://devcenter.heroku.com/articles/dynos) |
| **Render** | **Services** | Web/Private Services, Cron Jobs. | [Render Docs](https://render.com/docs/web-services) |
| **Fly.io** | **Machines** | Fast-starting Firecracker VMs; Anycast. | [Fly Machine Docs](https://fly.io/docs/machines/) |
| **Railway** | **Services** | Orchestrated deployments; Auto Builds. | [Railway Docs](https://docs.railway.app/develop/services) |

---

## 4. Managed Services (PaaS Focus)

| Category | Provider | Service | Details | Docs Link |
| :--- | :--- | :--- | :--- | :--- |
| **Database** | **Heroku** | **Postgres** | Managed PostgreSQL & Redis. | [Postgres Docs](https://devcenter.heroku.com/articles/heroku-postgresql) |
| | **Render** | **Postgres** | Fully managed PostgreSQL (v11-v16). | [Render DB Docs](https://render.com/docs/databases) |
| | **Dig.Ocean** | **Managed** | MySQL, Postgres, Redis, MongoDB. | [DO DB Docs](https://docs.digitalocean.com/products/databases/) |
| **Kubernetes** | **DigitalOcean**| **DOKS** | Managed K8s with DO Volumes. | [DOKS Docs](https://docs.digitalocean.com/products/kubernetes/) |
| **Serverless** | **Vercel** | **Edge** | Edge Functions & Serverless Logic. | [Vercel Docs](https://vercel.com/docs/rest-api) |
| | **Netlify** | **Functions** | Site hosting + Background Functions. | [Netlify Docs](https://docs.netlify.com/functions/overview/) |
