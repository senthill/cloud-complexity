# Map a generic service category to provider-specific service names
# Categories: compute, storage, object storage, file storage, kubernetes service, database service
SERVICE_MAPPINGS = {
    "compute": {
        "aws": "ec2",
        "gcp": "compute",
        "azure": "compute",
        "alibaba": "ecs",
        "vmware": "compute",
        "nutanix": "compute",
        "vercel": "deployments",
        "netlify": "sites",
        "heroku": "apps",
        "render": "services",
        "fly": "apps",
        "digitalocean": "droplets",
        "railway": "services",
        "vps": "compute"
    },
    "storage": {
        "aws": "s3",
        "gcp": "storage",
        "azure": "storage",
        "alibaba": "oss",
        "vmware": "vsan",
        "nutanix": "volumes"
    },
    "object storage": {
        "aws": "s3",
        "gcp": "storage",
        "azure": "storage",
        "alibaba": "oss"
    },
    "file storage": {
        "aws": "efs",
        "gcp": "file",
        "azure": "storage",
        "alibaba": "nas"
    },
    "kubernetes service": {
        "aws": "eks",
        "gcp": "container",
        "azure": "containerservice",
        "alibaba": "cs"
    },
    "database service": {
        "aws": "rds",
        "gcp": "sqladmin",
        "azure": "sql",
        "alibaba": "rds",
        "heroku": "postgres",
        "render": "postgres",
        "fly": "postgres",
        "digitalocean": "databases",
        "railway": "databases"
    },
    "networking": {
        "aws": {"service": "ec2", "filter_keywords": ["vpc", "subnet", "securitygroup", "routetable", "internetgateway", "natgateway", "networkinterface", "networkacl", "vpn", "customergateway", "transitgateway"]},
        "gcp": {"service": "compute", "filter_keywords": ["networks", "subnetworks", "firewalls", "routes", "routers", "vpngateways", "forwardingrules"]},
        "azure": "network",
        "alibaba": "vpc",
        "vmware": "nsx",
        "nutanix": "flow"
    },
    "serverless": {
        "aws": "lambda",
        "gcp": "cloudfunctions",
        "azure": "functions",
        "alibaba": "fc",
        "vercel": "deployments",
        "netlify": "sites"
    }
}
