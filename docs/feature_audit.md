# CloudComplexity: Provider Feature Audit

This document serves as the "Ground Truth" for the service mappings used in our API Complexity Tax benchmarks. It ensures every category is justified by official provider documentation.

## 1. Hyper-Cloud IaaS & PaaS
| Provider | Coverage | Reference Docs | Notes |
| :--- | :--- | :--- | :--- |
| **AWS** | Full Suite | [AWS Documentation](https://docs.aws.amazon.com/) | Benchmarked via `botocore` models. |
| **GCP** | Full Suite | [GCP Discovery API](https://cloud.google.com/discovery) | Benchmarked via Discovery Service APIs. |
| **Azure** | Full Suite | [Azure REST API](https://learn.microsoft.com/en-us/rest/api/azure/) | Benchmarked via OpenAPI specs. |
| **Alibaba** | Full Suite | [Alibaba Cloud API](https://www.alibabacloud.com/help/doc-detail/27325.htm) | Standardized on ECS, RDS, OSS, VPC. |

## 2. Infrastructure & HCI
| Provider | Category | Service | Reference |
| :--- | :--- | :--- | :--- |
| **VMWare** | Compute / Storage | vSphere / vSAN | [VMWare API Explorer](https://developer.broadcom.com/x-api/) |
| **Nutanix** | Compute / Networking | AHV / Flow | [Nutanix Dev Portal](https://www.nutanix.dev/api-reference/) |
| **VPS** | Compute | Generic VPS | Industry standard (DigitalOcean, Linode equivalents). |

## 3. Modern PaaS & App Platforms
| Provider | Feature | Service Name | Documentation Reference |
| :--- | :--- | :--- | :--- |
| **Heroku** | Compute | Dynos | [Heroku Dynos](https://devcenter.heroku.com/articles/dynos) |
| | Database | Postgres / Redis | [Heroku Data](https://devcenter.heroku.com/categories/data) |
| | Networking | Private Spaces | [Heroku Private Spaces](https://devcenter.heroku.com/articles/private-spaces) |
| **Render** | Compute | Web Services | [Render Services](https://render.com/docs/web-services) |
| | Storage | Persistent Disks | [Render Disks](https://render.com/docs/disks) |
| | Networking | Private Networking | [Render Networking](https://render.com/docs/networking) |
| **Fly.io** | Compute | Machines / Apps | [Fly Machines](https://fly.io/docs/machines/) |
| | Storage | Fly Volumes | [Fly Volumes](https://fly.io/docs/reference/volumes/) |
| | Networking | Anycast/IPv6 | [Fly Private Networking](https://fly.io/docs/reference/private-networking/) |
| | Kubernetes | Fly K8s | [Fly Kubernetes (Alpha)](https://fly.io/docs/reference/kubernetes/) |
| **DigitalOcean** | Compute | Droplets | [DO Droplets](https://docs.digitalocean.com/products/droplets/) |
| | Storage | Block / Spaces | [DO Volumes](https://docs.digitalocean.com/products/volumes/) |
| | Networking | VPC / Firewalls | [DO VPC](https://docs.digitalocean.com/products/networking/vpc/) |
| | Kubernetes | DOKS | [DigitalOcean K8s](https://docs.digitalocean.com/products/kubernetes/) |
| **Railway** | Compute | Services | [Railway Services](https://docs.railway.app/develop/services) |
| | Storage | Volumes | [Railway Volumes](https://docs.railway.app/develop/volumes) |
| | Database | Managed DBs | [Railway Databases](https://docs.railway.app/database) |
| | Networking | Service Mesh | [Railway Networking](https://docs.railway.app/develop/networking) |
| **Vercel** | Serverless | Deployments | [Vercel API](https://vercel.com/docs/rest-api) |
| **Netlify** | Serverless | Sites / Functions | [Netlify API](https://open-api.netlify.com/) |

## 4. Exclusion Rationale (N/A)
| Provider | Category | Reason for N/A |
| :--- | :--- | :--- |
| **Vercel / Netlify** | Networking | Abstracted entirely; no user-managed VPC/Subnet API. |
| **Heroku / Railway** | Kubernetes | Custom orchestrators; don't expose a raw K8s API. |
| **VPS** | Database | Unmanaged; users install their own DB on the instance. |
