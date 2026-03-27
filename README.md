# CloudComplexity: The API Tax Benchmark

CloudComplexity is a data-driven CLI tool designed to quantify the "API Complexity Tax" overhead of modern cloud infrastructure. It benchmarks the surface area of cloud APIs across 14 providers—ranging from legacy IaaS to modern "zero-infrastructure" PaaS—providing a clear metric for the cognitive load required to manage equivalent cloud services.

## The 100,000-Attribute Tax
Modern cloud providers (Hyperscalers) have seen an explosion in API surface area. Every attribute represents a configuration choice, a potential bug, and a cognitive burden. CloudComplexity identifies this "Tax" by measuring:
- **Total APIs**: Distinct operations per service.
- **Total Verbs**: HTTP methods (GET, POST, etc.) or distinct actions.
- **Total Attributes**: The sum of all configurable parameters/request inputs.

---

## Supported Providers & Categories

### 14 Supported Cloud Providers
- **Hyper-Cloud**: AWS, GCP, Microsoft Azure, Alibaba Cloud.
- **Enterprise/HCI**: VMWare vSphere, Nutanix.
- **Modern PaaS**: Heroku, Render, Fly.io, Railway.
- **Serverless/Edge**: Vercel, Netlify.
- **Infrastructure**: DigitalOcean, Generic VPS.

### 8 Service Categories
1. **Compute**: VMs (EC2, Droplets) and App Services.
2. **Managed Kubernetes**: EKS, GKE, AKS, ACK, DOKS, FKS.
3. **Database**: Managed SQL (RDS, Cloud SQL) and NoSQL.
4. **Networking**: VPC, Subnets, Private Networking, Service Mesh.
5. **Block Storage**: Volumes/Persistent Disks.
6. **Object Storage**: S3, GCS, Blob, Spaces.
7. **File Storage**: Managed NFS (EFS).
8. **Serverless**: Lambda, Cloud Functions, Vercel/Netlify.

---

## Quick Reference Documentation
For a deep dive into the benchmark data and service mappings, refer to:
- [**Benchmark Results**](./docs/benchmark_results.md): Live tables showing the "Complexity Tax" for all categories.
- [**Feature Audit (Ground Truth)**](./docs/feature_audit.md): Service descriptions and official documentation references for all 14 providers.
- [**Strategic Analysis**](./docs/blog/strategic_analysis.md): High-level analysis of "Aggressive Subtraction" in cloud design.

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/senthill/cloud-complexity.git
   cd cloud-complexity
   ```

2. **Setup Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Generate Specs**:
   ```bash
   python scripts/generate_private_specs.py
   ```

---

## Usage

Benchmark all categories across all providers:
```bash
python -m src.main all
```

Benchmark a specific category:
```bash
python -m src.main compute
python -m src.main database
python -m src.main storage
```

---

## Project Structure
- `src/`: Core analysis logic and provider implementations.
- `specs/`: Organized by provider, containing OpenAPI/Discovery specifications.
- `docs/`: Comprehensive benchmark results, feature audits, and blog drafts.
- `scripts/`: Tools for generating organized mock specifications for PaaS providers.
- `tests/`: Automated unit tests for metric calculation.

---

## Strategic Methodology
CloudComplexity categorizes providers into two camps:
- **Builders (High Tax)**: Providers like AWS/Azure that expose the "Lego bricks," resulting in >1,000 attributes for simple services.
- **Users (Low Tax)**: Providers like Render/Fly.io that expose "Intent-based APIs," reducing cognitive load by 95%+.

This data serves as the foundation for our "Complexity Tax" series, advocating for a shift towards zero-infrastructure abstractions.
