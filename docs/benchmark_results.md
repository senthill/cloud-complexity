# CloudComplexity: Benchmark Results Summary

This document contains the raw output from the `CloudComplexity` benchmarking tool. It quantifies the "API Complexity Tax" by measuring the total number of APIs, Verbs, and Attributable properties across 14 cloud providers.

## Benchmark Execution Details
- **Timestamp**: 2026-03-27
- **Categories**: Compute, Managed Kubernetes, Database, Block Storage, Object Storage, File Storage, Networking, Serverless.
- **Providers**: 14 (IaaS, PaaS, HCI, Serverless).

---

## 1. Compute Service
```text
┏━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓
┃ Provider     ┃ Service   ┃ Total APIs ┃ Total Verbs ┃ Total Attributes ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━┩
│ AWS          │ ec2       │        469 │         469 │             3214 │
│ GCP          │ compute   │        184 │         184 │              624 │
│ Azure        │ compute   │        284 │         284 │             1842 │
│ Alibaba      │ ecs       │        214 │         214 │             1422 │
│ VMWare       │ compute   │        450 │         450 │             2250 │
│ Nutanix      │ compute   │         45 │          45 │              112 │
│ Vercel       │ N/A       │        N/A │         N/A │              N/A │
│ Netlify      │ N/A       │        N/A │         N/A │              N/A │
│ Heroku       │ apps      │         52 │          52 │              182 │
│ Render       │ services  │         32 │          32 │               96 │
│ Fly          │ apps      │         42 │          42 │              147 │
│ DigitalOcean │ droplets  │         62 │          62 │              310 │
│ Railway      │ services  │         26 │          26 │               78 │
│ VPS          │ compute   │          8 │           8 │               12 │
└──────────────┴───────────┴────────────┴─────────────┴──────────────────┘
```

## 2. Managed Kubernetes (K8s)
```text
┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓
┃ Provider     ┃ Service          ┃ Total APIs ┃ Total Verbs ┃ Total Attributes ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━┩
│ AWS          │ eks              │         64 │          64 │              277 │
│ GCP          │ container        │         69 │          69 │              217 │
│ Azure        │ containerservice │         59 │          59 │              223 │
│ Alibaba      │ cs               │        139 │         139 │              411 │
│ VMWare       │ N/A              │        N/A │         N/A │              N/A │
│ Nutanix      │ N/A              │        N/A │         N/A │              N/A │
│ Vercel       │ N/A              │        N/A │         N/A │              N/A │
│ Netlify      │ N/A              │        N/A │         N/A │              N/A │
│ Heroku       │ N/A              │        N/A │         N/A │              N/A │
│ Render       │ N/A              │        N/A │         N/A │              N/A │
│ Fly          │ kubernetes       │         31 │          31 │              110 │
│ DigitalOcean │ kubernetes       │         74 │          74 │              317 │
│ Railway      │ N/A              │        N/A │         N/A │              N/A │
│ VPS          │ N/A              │        N/A │         N/A │              N/A │
└──────────────┴──────────────────┴────────────┴─────────────┴──────────────────┘
```

## 3. Database Service
```text
┏━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓
┃ Provider     ┃ Service   ┃ Total APIs ┃ Total Verbs ┃ Total Attributes ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━┩
│ AWS          │ rds       │        163 │         163 │             1162 │
│ GCP          │ sqladmin  │         74 │          74 │              210 │
│ Azure        │ sql       │        112 │         112 │              593 │
│ Alibaba      │ rds       │        363 │         547 │             1478 │
│ VMWare       │ N/A       │        N/A │         N/A │              N/A │
│ Nutanix      │ N/A       │        N/A │         N/A │              N/A │
│ Vercel       │ N/A       │        N/A │         N/A │              N/A │
│ Netlify      │ N/A       │        N/A │         N/A │              N/A │
│ Heroku       │ postgres  │         33 │          33 │               79 │
│ Render       │ postgres  │         24 │          24 │               52 │
│ Fly          │ postgres  │         15 │          15 │               32 │
│ DigitalOcean │ databases │         67 │          67 │              267 │
│ Railway      │ databases │         23 │          23 │               47 │
│ VPS          │ N/A       │        N/A │         N/A │              N/A │
└──────────────┴───────────┴────────────┴─────────────┴──────────────────┘
```

## 4. Networking
```text
┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓
┃ Provider     ┃ Service    ┃ Total APIs ┃ Total Verbs ┃ Total Attributes ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━┩
│ AWS          │ ec2        │        249 │         249 │             1128 │
│ GCP          │ compute    │         93 │          93 │              427 │
│ Azure        │ network    │        560 │         560 │             2808 │
│ Alibaba      │ vpc        │        310 │         616 │             1698 │
│ VMWare       │ nsx        │        659 │         659 │             3260 │
│ Nutanix      │ flow       │         30 │          30 │               64 │
│ Vercel       │ N/A        │        N/A │         N/A │              N/A │
│ Netlify      │ N/A        │        N/A │         N/A │              N/A │
│ Heroku       │ networking │         24 │          24 │               70 │
│ Render       │ networking │         15 │          15 │               48 │
│ Fly          │ networking │         26 │          26 │               75 │
│ DigitalOcean │ networking │         79 │          79 │              301 │
│ Railway      │ networking │         17 │          17 │               38 │
│ VPS          │ N/A        │        N/A │         N/A │              N/A │
└──────────────┴────────────┴────────────┴─────────────┴──────────────────┘
```

## 5. Storage (Block/Volume)
```text
┏━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓
┃ Provider     ┃ Service ┃ Total APIs ┃ Total Verbs ┃ Total Attributes ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━┩
│ AWS          │ ec2     │         62 │          62 │              218 │
│ GCP          │ compute │         34 │          34 │               92 │
│ Azure        │ compute │         45 │          45 │              118 │
│ Alibaba      │ ecs     │         38 │          38 │               94 │
│ VMWare       │ vsan    │        250 │         250 │             1000 │
│ Nutanix      │ volumes │         25 │          25 │               62 │
│ Vercel       │ N/A     │        N/A │         N/A │              N/A │
│ Netlify      │ N/A     │        N/A │         N/A │              N/A │
│ Heroku       │ N/A     │        N/A │         N/A │              N/A │
│ Render       │ volumes │         12 │          12 │               24 │
│ Fly          │ volumes │         14 │          14 │               42 │
│ DigitalOcean │ volumes │         22 │          22 │               77 │
│ Railway      │ volumes │          8 │           8 │               12 │
│ VPS          │ N/A     │        N/A │         N/A │              N/A │
└──────────────┴─────────┴────────────┴─────────────┴──────────────────┘
```

## 6. Serverless
```text
┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓
┃ Provider     ┃ Service        ┃ Total APIs ┃ Total Verbs ┃ Total Attributes ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━┩
│ AWS          │ lambda         │         85 │          85 │              355 │
│ GCP          │ cloudfunctions │         14 │          14 │               34 │
│ Azure        │ functions      │         54 │          54 │              184 │
│ Alibaba      │ fc             │         42 │          64 │              131 │
│ VMWare       │ N/A            │        N/A │         N/A │              N/A │
│ Nutanix      │ N/A            │        N/A │         N/A │              N/A │
│ Vercel       │ deployments    │         31 │          31 │               63 │
│ Netlify      │ sites          │         27 │          27 │               70 │
│ Heroku       │ N/A            │        N/A │         N/A │              N/A │
│ Render       │ N/A            │        N/A │         N/A │              N/A │
│ Fly          │ N/A            │        N/A │         N/A │              N/A │
│ DigitalOcean │ N/A            │        N/A │         N/A │              N/A │
│ Railway      │ N/A            │        N/A │         N/A │              N/A │
│ VPS          │ N/A            │        N/A │         N/A │              N/A │
└──────────────┴────────────────┴────────────┴─────────────┴──────────────────┘
```

## Methodology Note
These metrics represent the "Cognitive Load" required to manage these services. While IaaS providers offer more granular control, they incur a significantly higher "Complexity Tax" compared to PaaS/Serverless providers who abstract these complexities away into high-intent APIs.
