import os
import json
import random

def generate_mock_openapi_spec(name, num_paths, verbs_per_path_range, attributes_per_verb_range):
    paths = {}
    methods = ["get", "post", "put", "delete", "patch"]
    
    # Use a fixed seed for deterministic output
    random.seed(hash(name))
    
    for i in range(num_paths):
        path_name = f"/api/v1/{name}/resource_{i}"
        path_item = {}
        num_verbs = random.randint(*verbs_per_path_range)
        chosen_methods = random.sample(methods, min(num_verbs, len(methods)))
        
        for verb in chosen_methods:
            verb_item = {}
            num_attributes = random.randint(*attributes_per_verb_range)
            parameters = []
            for j in range(num_attributes):
                parameters.append({"name": f"param_{j}", "in": "query", "description": "mock param"})
            verb_item["parameters"] = parameters
            path_item[verb] = verb_item
            
        paths[path_name] = path_item
        
    return {"openapi": "3.0.0", "info": {"title": f"{name} API", "version": "1.0"}, "paths": paths}

def generate_mock_alibaba_spec(name, num_paths, verbs_per_path_range, attributes_per_verb_range):
    apis = {}
    methods = ["get", "post", "put", "delete", "patch"]
    random.seed(hash(name))
    
    for i in range(num_paths):
        api_name = f"Action_{i}"
        num_verbs = random.randint(*verbs_per_path_range)
        chosen_methods = random.sample(methods, min(num_verbs, len(methods)))
        
        num_attributes = random.randint(*attributes_per_verb_range)
        parameters = [{"name": f"param_{j}"} for j in range(num_attributes)]
        
        apis[api_name] = {
            "methods": chosen_methods,
            "parameters": parameters
        }
    return {"apis": apis}

def save_mock_spec(provider: str, service_name: str, num_endpoints: int, verbs_range: tuple, attrs_range: tuple, is_alibaba: bool = False):
    provider_dir = os.path.join("specs", provider)
    os.makedirs(provider_dir, exist_ok=True)
    
    if is_alibaba:
        spec = generate_mock_alibaba_spec(f"{provider}_{service_name}", num_endpoints, verbs_range, attrs_range)
    else:
        spec = generate_mock_openapi_spec(f"{provider}_{service_name}", num_endpoints, verbs_range, attrs_range)
        
    file_path = os.path.join(provider_dir, f"{service_name}.json")
    
    with open(file_path, "w") as f:
        json.dump(spec, f, indent=2)
    print(f"Generated {file_path}")

def main():
    os.makedirs("specs", exist_ok=True)
    
    # 1. IaaS & HCI
    save_mock_spec("vmware", "compute", 450, (1, 3), (2, 8))
    save_mock_spec("vmware", "vsan", 250, (1, 3), (2, 6))
    save_mock_spec("vmware", "nsx", 320, (1, 3), (2, 8))
    
    save_mock_spec("nutanix", "compute", 45, (1, 2), (1, 4))
    save_mock_spec("nutanix", "volumes", 25, (1, 2), (1, 4))
    save_mock_spec("nutanix", "flow", 20, (1, 2), (1, 3))
    
    save_mock_spec("vps", "compute", 8, (1, 1), (1, 2))

    # 2. Modern PaaS & Edge
    save_mock_spec("netlify", "sites", 18, (1, 2), (1, 4))
    save_mock_spec("vercel", "deployments", 22, (1, 2), (1, 3))

    # Heroku
    save_mock_spec("heroku", "apps", 52, (1, 2), (2, 5))
    save_mock_spec("heroku", "postgres", 22, (1, 2), (1, 4))
    save_mock_spec("heroku", "networking", 15, (1, 2), (2, 4))

    # Render
    save_mock_spec("render", "services", 32, (1, 2), (2, 4))
    save_mock_spec("render", "postgres", 16, (1, 2), (1, 3))
    save_mock_spec("render", "volumes", 12, (1, 1), (1, 3))
    save_mock_spec("render", "networking", 10, (1, 2), (2, 4))

    # Fly.io
    save_mock_spec("fly", "apps", 42, (1, 2), (2, 5))
    save_mock_spec("fly", "postgres", 12, (1, 2), (1, 3))
    save_mock_spec("fly", "volumes", 14, (1, 2), (2, 4))
    save_mock_spec("fly", "kubernetes", 20, (1, 2), (2, 5))
    save_mock_spec("fly", "networking", 18, (1, 2), (2, 4))

    # DigitalOcean
    save_mock_spec("do", "droplets", 62, (1, 3), (3, 7))
    save_mock_spec("do", "databases", 45, (1, 2), (2, 6))
    save_mock_spec("do", "volumes", 22, (1, 2), (2, 5))
    save_mock_spec("do", "spaces", 15, (1, 2), (2, 4))
    save_mock_spec("do", "kubernetes", 42, (1, 2), (3, 6))
    save_mock_spec("do", "networking", 38, (1, 3), (2, 6))

    # Railway
    save_mock_spec("railway", "services", 26, (1, 2), (2, 4))
    save_mock_spec("railway", "databases", 14, (1, 2), (1, 3))
    save_mock_spec("railway", "volumes", 8, (1, 1), (1, 2))
    save_mock_spec("railway", "networking", 10, (1, 2), (1, 4))

    # 3. Cloud Provider Overrides (for testing/mocking where real specs are missing or very large)
    save_mock_spec("azure", "network", 280, (1, 3), (3, 7))
    save_mock_spec("azure", "containerservice", 59, (1, 1), (2, 6))
    save_mock_spec("azure", "sql", 112, (1, 1), (2, 8))
    save_mock_spec("azure", "functions", 54, (1, 1), (2, 5))
    save_mock_spec("azure", "storage", 220, (3, 5), (5, 12))

    save_mock_spec("alibaba", "vpc", 310, (1, 3), (3, 8), is_alibaba=True)
    save_mock_spec("alibaba", "cs", 139, (1, 1), (2, 4), is_alibaba=True)
    save_mock_spec("alibaba", "rds", 363, (1, 2), (2, 6), is_alibaba=True)
    save_mock_spec("alibaba", "fc", 42, (1, 2), (2, 4), is_alibaba=True)
    save_mock_spec("alibaba", "oss", 185, (3, 5), (5, 10), is_alibaba=True)
    save_mock_spec("alibaba", "nas", 72, (2, 4), (4, 8), is_alibaba=True)

    print("\nAll organizational specs generated successfully.")

if __name__ == "__main__":
    main()
