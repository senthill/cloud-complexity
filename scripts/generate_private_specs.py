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

def main():
    os.makedirs("specs", exist_ok=True)
    
    # VMWare: High complexity, many endpoints, mimicking legacy heavy models similar to AWS
    vmware_spec = generate_mock_openapi_spec("vmware_compute", 450, (1, 3), (2, 8))
    with open("specs/vmware_compute.json", "w") as f:
        json.dump(vmware_spec, f, indent=2)
    print("Generated specs/vmware_compute.json")

    # Nutanix: Low complexity, intent-driven, highly concise
    nutanix_spec = generate_mock_openapi_spec("nutanix_compute", 45, (1, 2), (1, 4))
    with open("specs/nutanix_compute.json", "w") as f:
        json.dump(nutanix_spec, f, indent=2)
    print("Generated specs/nutanix_compute.json")

    # Storage specs
    vmware_vsan_spec = generate_mock_openapi_spec("vmware_vsan", 250, (1, 3), (2, 6))
    with open("specs/vmware_vsan.json", "w") as f:
        json.dump(vmware_vsan_spec, f, indent=2)
    print("Generated specs/vmware_vsan.json")

    nutanix_volumes_spec = generate_mock_openapi_spec("nutanix_volumes", 25, (1, 2), (1, 4))
    with open("specs/nutanix_volumes.json", "w") as f:
        json.dump(nutanix_volumes_spec, f, indent=2)
    print("Generated specs/nutanix_volumes.json")

    # Networking specs
    vmware_nsx_spec = generate_mock_openapi_spec("vmware_nsx", 320, (1, 3), (2, 8))
    with open("specs/vmware_nsx.json", "w") as f:
        json.dump(vmware_nsx_spec, f, indent=2)

    nutanix_flow_spec = generate_mock_openapi_spec("nutanix_flow", 20, (1, 2), (1, 3))
    with open("specs/nutanix_flow.json", "w") as f:
        json.dump(nutanix_flow_spec, f, indent=2)

    azure_network_spec = generate_mock_openapi_spec("azure_network", 280, (1, 3), (3, 7))
    with open("specs/azure_network.json", "w") as f:
        json.dump(azure_network_spec, f, indent=2)

    alibaba_vpc_spec = generate_mock_alibaba_spec("alibaba_vpc", 310, (1, 3), (3, 8))
    with open("specs/alibaba_vpc.json", "w") as f:
        json.dump(alibaba_vpc_spec, f, indent=2)
    print("Generated Networking specs")

    netlify_spec = generate_mock_openapi_spec("netlify_sites", 18, (1, 2), (1, 4))
    with open("specs/netlify_sites.json", "w") as f:
        json.dump(netlify_spec, f, indent=2)
    print("Generated PaaS specs")

    # New Providers (PaaS & Cloud)
    # Heroku
    with open("specs/heroku_apps.json", "w") as f:
        json.dump(generate_mock_openapi_spec("heroku_apps", 52, (1, 2), (2, 5)), f, indent=2)
    with open("specs/heroku_postgres.json", "w") as f:
        json.dump(generate_mock_openapi_spec("heroku_postgres", 22, (1, 2), (1, 4)), f, indent=2)

    # Render
    with open("specs/render_services.json", "w") as f:
        json.dump(generate_mock_openapi_spec("render_services", 32, (1, 2), (2, 4)), f, indent=2)
    with open("specs/render_postgres.json", "w") as f:
        json.dump(generate_mock_openapi_spec("render_postgres", 16, (1, 2), (1, 3)), f, indent=2)

    # Fly.io
    with open("specs/fly_apps.json", "w") as f:
        json.dump(generate_mock_openapi_spec("fly_apps", 42, (1, 2), (2, 5)), f, indent=2)
    with open("specs/fly_postgres.json", "w") as f:
        json.dump(generate_mock_openapi_spec("fly_postgres", 12, (1, 2), (1, 3)), f, indent=2)

    # DigitalOcean
    with open("specs/do_droplets.json", "w") as f:
        json.dump(generate_mock_openapi_spec("do_droplets", 62, (1, 3), (3, 7)), f, indent=2)
    with open("specs/do_databases.json", "w") as f:
        json.dump(generate_mock_openapi_spec("do_databases", 45, (1, 2), (2, 6)), f, indent=2)

    # Railway
    with open("specs/railway_services.json", "w") as f:
        json.dump(generate_mock_openapi_spec("railway_services", 26, (1, 2), (2, 4)), f, indent=2)
    with open("specs/railway_databases.json", "w") as f:
        json.dump(generate_mock_openapi_spec("railway_databases", 14, (1, 2), (1, 3)), f, indent=2)

    # VPS (Generic)
    with open("specs/vps_compute.json", "w") as f:
        json.dump(generate_mock_openapi_spec("vps_compute", 8, (1, 1), (1, 2)), f, indent=2)

    print("Generated all modern PaaS and Cloud specs")

if __name__ == "__main__":
    main()
