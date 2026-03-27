# CloudComplexity: Provider Feature Audit (Detailed)

This document provides the "Ground Truth" for all service mappings used in the API Complexity Tax benchmarks. Each entry includes service descriptions, key offerings, and verified documentation links.

---

## 1. Hyper-Cloud Providers (IaaS & PaaS)

### [AWS (Amazon Web Services)](https://docs.aws.amazon.com/)
| Category | Service | Description | High-Level Offerings | Docs Link |
| :--- | :--- | :--- | :--- | :--- |
| **Compute** | **EC2** | Virtual servers in the cloud. | Intel, AMD, & Graviton instances; Spot/On-Demand; Auto Scaling. | [EC2 Docs](https://docs.aws.amazon.com/ec2/) |
| **Database** | **RDS** | Managed relational databases. | MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, Aurora. | [RDS Docs](https://docs.aws.amazon.com/rds/) |
| **Kubernetes** | **EKS** | Managed K8s service. | Fargate support; IAM integration; Managed node groups. | [EKS Docs](https://docs.aws.amazon.com/eks/) |
| **Serverless** | **Lambda** | Event-driven compute. | Node.js, Python, Java, Go, Ruby, .NET, Custom Runtimes. | [Lambda Docs](https://docs.aws.amazon.com/lambda/) |
| **Storage** | **EBS/S3** | Block and Object storage. | EBS Volumes (GP3, IO2); S3 Standard, Glacier, Intelligent-Tiering. | [S3 Docs](https://docs.aws.amazon.com/s3/) |

### [GCP (Google Cloud Platform)](https://cloud.google.com/docs)
| Category | Service | Description | High-Level Offerings | Docs Link |
| :--- | :--- | :--- | :--- | :--- |
| **Compute** | **GCE** | VM instances on Google infra. | N2, E2, Tau T2A (ARM); Preemptible VMs; Sole-tenant nodes. | [GCE Docs](https://cloud.google.com/compute/docs) |
| **Database** | **Cloud SQL** | Managed SQL databases. | MySQL, PostgreSQL, SQL Server; High Availability; Read Replicas. | [Cloud SQL Docs](https://cloud.google.com/sql/docs) |
| **Kubernetes** | **GKE** | Managed K8s (Autopilot/Standard). | Autopilot mode; Multicluster Ingress; Binary Authorization. | [GKE Docs](https://cloud.google.com/kubernetes-engine/docs) |
| **Serverless** | **Functions** | Event-driven functions. | Cloud Functions (1st/2nd gen); Cloud Run (Container-based). | [Functions Docs](https://cloud.google.com/functions/docs) |

### [Azure (Microsoft)](https://learn.microsoft.com/en-us/azure/)
| Category | Service | Description | High-Level Offerings | Docs Link |
| :--- | :--- | :--- | :--- | :--- |
| **Compute** | **VMs** | Scalable virtual machines. | Linux/Windows VMs; B-Series; Proximity Placement Groups. | [VM Docs](https://learn.microsoft.com/en-us/azure/virtual-machines/) |
| **Database** | **Azure SQL** | Family of SQL cloud databases. | SQL Database, SQL Managed Instance, SQL on VMs. | [Azure SQL Docs](https://learn.microsoft.com/en-us/azure/azure-sql/) |
| **Kubernetes** | **AKS** | Managed K8s service. | Azure AD integration; Serverless K8s via Virtual Nodes. | [AKS Docs](https://learn.microsoft.com/en-us/azure/aks/) |
| **Serverless** | **Functions** | Serverless code execution. | Consumption, Premium, and Dedicated plans. | [Functions Docs](https://learn.microsoft.com/en-us/azure/azure-functions/) |

### [Alibaba Cloud](https://www.alibabacloud.com/help)
| Category | Service | Description | High-Level Offerings | Docs Link |
| :--- | :--- | :--- | :--- | :--- |
| **Compute** | **ECS** | Elastic Compute Service. | x86, ARM, & Bare Metal; GPU instances; Savings Plans. | [ECS Docs](https://www.alibabacloud.com/help/product/25280.htm) |
| **Database** | **RDS** | Relational Database Service. | MySQL, PostgreSQL, SQL Server, MariaDB, PolarDB. | [RDS Docs](https://www.alibabacloud.com/help/product/26090.htm) |
| **Kubernetes** | **ACK** | Container Service for K8s. | Managed K8s, Serverless K8s, Edge K8s. | [ACK Docs](https://www.alibabacloud.com/help/product/85222.htm) |

---

## 2. Infrastructure & HCI Providers

| Provider | Service | Description | Key Features | Docs Link |
| :--- | :--- | :--- | :--- | :--- |
| **VMWare** | **vSphere** | Enterprise Cloud Computing. | vCenter, ESXi Hypervisor, DRS, vMotion. | [vSphere Docs](https://docs.vmware.com/en/VMware-vSphere/index.html) |
| **Nutanix** | **AHV** | Enterprise Hypervisor. | One-click upgrades, Distributed Resource Scheduler. | [AHV Docs](https://www.nutanix.com/products/hyperconverged-infrastructure/ahv) |
| **DigitalOcean**| **Droplets** | SSD-based Cloud Servers. | Basic, General Purpose, CPU-Optimized, Memory-Optimized. | [Droplet Docs](https://docs.digitalocean.com/products/droplets/) |

---

## 3. Modern PaaS & App Platforms

| Provider | Service | Description | Offerings / Details | Docs Link |
| :--- | :--- | :--- | :--- | :--- |
| **Heroku** | **Dynos** | Isolated Linux containers. | Web, Worker, and One-off Dynos; Autoscaling. | [Dynos Docs](https://devcenter.heroku.com/articles/dynos) |
| **Render** | **Services** | Unified Cloud for Apps & DBs. | Web Services, Private Services, Cron Jobs, Background Workers. | [Render Docs](https://render.com/docs/web-services) |
| **Fly.io** | **Machines** | Fast-starting Firecracker VMs. | Global Anycast; Private Networking; Persistent Volumes. | [Fly Machine Docs](https://fly.io/docs/machines/) |
| **Railway** | **Services** | Orchestrated App deployment. | Automatic Builds; Secret Management; Shared Volumes. | [Railway Docs](https://docs.railway.app/develop/services) |

---

## 4. Managed Services (PaaS Focus)

| Category | Provider | Service | Details | Docs Link |
| :--- | :--- | :--- | :--- | :--- |
| **Database** | **Heroku** | **Managed DB** | Heroku Postgres, Heroku Data for Redis. | [Postgres Docs](https://devcenter.heroku.com/articles/heroku-postgresql) |
| | **Render** | **Postgres** | Fully managed PostgreSQL (v11-v16). | [Render DB Docs](https://render.com/docs/databases) |
| | **Railway** | **Databases** | Postgres, MySQL, Redis, MongoDB. | [Railway DB Docs](https://docs.railway.app/database) |
| | **Dig.Ocean** | **Managed DB** | MySQL, PostgreSQL, Redis, MongoDB. | [DO DB Docs](https://docs.digitalocean.com/products/databases/) |
| **Kubernetes** | **DigitalOcean**| **DOKS** | Managed K8s with DO Volumes & LBs. | [DOKS Docs](https://docs.digitalocean.com/products/kubernetes/) |
| | **Fly.io** | **FKS** | Hybrid Fly Machines + Kubernetes (Alpha). | [FKS Docs](https://fly.io/docs/reference/kubernetes/) |
| **Serverless** | **Vercel** | **Edge Functions**| Deployments, Serverless Functions, Edge Middleware. | [Vercel Docs](https://vercel.com/docs/rest-api) |
| | **Netlify** | **Functions** | Sites, Edge Functions, Background Functions. | [Netlify Docs](https://docs.netlify.com/functions/overview/) |
