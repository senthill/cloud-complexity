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
| **Block Storage** | **EBS** | NVMe SSD (GP3, IO2); Snapshots. | [EBS Docs](https://docs.aws.amazon.com/ebs/) |
| **Object Storage**| **S3** | Standard, Infrequent Access, Glacier. | [S3 Docs](https://docs.aws.amazon.com/s3/) |
| **File Storage** | **EFS** | Managed NFS for Linux; Bursting/Elastic. | [EFS Docs](https://docs.aws.amazon.com/efs/) |

### ![GCP](https://img.shields.io/badge/-Google_Cloud-blue?style=flat-square&logo=google-cloud&logoColor=white)
| Category | Service | High-Level Offerings | Docs Link |
| :--- | :--- | :--- | :--- |
| **Compute** | **GCE** | VM instances; Tau T2A (ARM); Preemptible. | [GCE Docs](https://cloud.google.com/compute/docs) |
| **Database** | **Cloud SQL** | MySQL, PostgreSQL, SQL Server; HA. | [Cloud SQL Docs](https://cloud.google.com/sql/docs) |
| **Kubernetes** | **GKE** | Autopilot; Multicluster Ingress. | [GKE Docs](https://cloud.google.com/kubernetes-engine/docs) |
| **Block Storage** | **PD** | Persistent Disk (Balanced, SSD, Extreme). | [PD Docs](https://cloud.google.com/compute/docs/disks) |
| **Object Storage**| **GCS** | Standard, Nearline, Coldline, Archive. | [GCS Docs](https://cloud.google.com/storage/docs) |

### ![Azure](https://img.shields.io/badge/-Microsoft_Azure-0078D4?style=flat-square&logo=microsoft-azure&logoColor=white)
| Category | Service | High-Level Offerings | Docs Link |
| :--- | :--- | :--- | :--- |
| **Compute** | **VMs** | Linux/Windows VMs; Proximity Placement. | [VM Docs](https://learn.microsoft.com/en-us/azure/virtual-machines/) |
| **Database** | **Azure SQL** | SQL Database, Managed Instances. | [Azure SQL Docs](https://learn.microsoft.com/en-us/azure/azure-sql/) |
| **Kubernetes** | **AKS** | Azure AD integration; Serverless Nodes. | [AKS Docs](https://learn.microsoft.com/en-us/azure/aks/) |
| **Object Storage**| **Blob** | Block, Page, and Append Blobs; Hot/Cool. | [Blob Docs](https://learn.microsoft.com/en-us/azure/storage/blobs/) |

### ![Alibaba](https://img.shields.io/badge/-Alibaba_Cloud-FF6A00?style=flat-square&logo=alibaba-cloud&logoColor=white)
| Category | Service | High-Level Offerings | Docs Link |
| :--- | :--- | :--- | :--- |
| **Compute** | **ECS** | x86, ARM, & Bare Metal; GPU instances. | [ECS Docs](https://www.alibabacloud.com/help/product/25280.htm) |
| **Database** | **RDS** | MySQL, PostgreSQL, SQL Server, PolarDB. | [RDS Docs](https://www.alibabacloud.com/help/product/26090.htm) |
| **Kubernetes** | **ACK** | Managed K8s, Serverless K8s, Edge K8s. | [ACK Docs](https://www.alibabacloud.com/help/product/85222.htm) |
| **Object Storage**| **OSS** | Standard, IA, Archive, Cold Archive. | [OSS Docs](https://www.alibabacloud.com/help/product/31815.htm) |

---

## 2. Infrastructure & HCI Providers

| Provider | Service | Category | Key Features | Docs Link |
| :--- | :--- | :--- | :--- | :--- |
| **VMWare** | **vSphere** | Compute | vCenter, ESXi, DRS, vMotion. | [vSphere Docs](https://docs.vmware.com/en/VMware-vSphere/index.html) |
| **VMWare** | **vSAN** | Block Storage | Software-defined shared storage for VMs. | [vSAN Docs](https://docs.vmware.com/en/VMware-vSAN/index.html) |
| **Nutanix** | **AHV** | Compute | One-click upgrades, Distributed Scaling. | [AHV Docs](https://www.nutanix.com/products/hyperconverged-infrastructure/ahv) |
| **Nutanix** | **Volumes** | Block Storage | Scale-out block storage via i组/SCSI. | [Volumes Docs](https://www.nutanix.com/products/volumes) |
| **Dig.Ocean**| **Droplets** | Compute | Basic, Gen Purpose, CPU-Optimized. | [Droplet Docs](https://docs.digitalocean.com/products/droplets/) |
| **Dig.Ocean**| **Volumes** | Block Storage | SSD-based network-attached block drives. | [Volumes Docs](https://docs.digitalocean.com/products/volumes/) |

---

## 3. Modern PaaS & App Platforms

| Provider | Service | Category | Offerings / Details | Docs Link |
| :--- | :--- | :--- | :--- | :--- |
| **Heroku** | **Dynos** | Compute | Web, Worker, and One-off Containers. | [Dynos Docs](https://devcenter.heroku.com/articles/dynos) |
| **Render** | **Services** | Compute | Web/Private Services, Cron Jobs. | [Render Docs](https://render.com/docs/web-services) |
| **Render** | **Disks** | Block Storage | Persistent SSD storage for Web Services. | [Render Disk Docs](https://render.com/docs/disks) |
| **Fly.io** | **Machines** | Compute | Fast-starting Firecracker VMs; Anycast. | [Fly Machine Docs](https://fly.io/docs/machines/) |
| **Fly.io** | **Volumes** | Block Storage | Local NVMe SSD storage for Fly Machines. | [Fly Volumes Docs](https://fly.io/docs/reference/volumes/) |
| **Railway** | **Services** | Compute | Orchestrated deployments; Auto Builds. | [Railway Docs](https://docs.railway.app/develop/services) |
| **Railway** | **Volumes** | Block Storage | Durable storage mounted to Railway services. | [Railway Vol Docs](https://docs.railway.app/develop/volumes) |

---

## 4. Managed Services Summary

| Category | Provider | Service | Details | Docs Link |
| :--- | :--- | :--- | :--- | :--- |
| **Database** | **Heroku** | **Postgres** | Managed PostgreSQL & Redis. | [Postgres Docs](https://devcenter.heroku.com/articles/heroku-postgresql) |
| | **Render** | **Postgres** | Fully managed PostgreSQL (v11-v16). | [Render DB Docs](https://render.com/docs/databases) |
| | **Railway** | **Databases** | Postgres, MySQL, Redis, MongoDB. | [Railway DB Docs](https://docs.railway.app/database) |
| | **Dig.Ocean** | **Managed** | MySQL, Postgres, Redis, MongoDB. | [DO DB Docs](https://docs.digitalocean.com/products/databases/) |
| **Block Storage**| **Render** | **Disks** | Managed SSD volumes (Persistent). | [Render Disks](https://render.com/docs/disks) |
| | **Fly.io** | **Volumes** | Local NVMe storage for containers. | [Fly Volumes](https://fly.io/docs/reference/volumes/) |
| | **Railway** | **Volumes** | Persistent storage for Railway apps. | [Railway Vol](https://docs.railway.app/develop/volumes) |
| **Object Storage**| **Dig.Ocean** | **Spaces** | S3-compatible object storage + CDN. | [Spaces Docs](https://docs.digitalocean.com/products/spaces/) |
| **Kubernetes** | **DigitalOcean**| **DOKS** | Managed K8s with DO Volumes. | [DOKS Docs](https://docs.digitalocean.com/products/kubernetes/) |
| **Serverless** | **Vercel** | **Edge** | Edge Functions & Serverless Logic. | [Vercel Docs](https://vercel.com/docs/rest-api) |
| | **Netlify** | **Functions** | Site hosting + Background Functions. | [Netlify Docs](https://docs.netlify.com/functions/overview/) |
