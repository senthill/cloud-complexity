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

    # Serverless Native Cloud Specs (Mocks for Azure/Alibaba for simplicity)
    azure_functions_spec = generate_mock_openapi_spec("azure_functions", 35, (1, 2), (2, 5))
    with open("specs/azure_functions.json", "w") as f:
        json.dump(azure_functions_spec, f, indent=2)

    alibaba_fc_spec = generate_mock_alibaba_spec("alibaba_fc", 42, (1, 2), (2, 6))
    with open("specs/alibaba_fc.json", "w") as f:
        json.dump(alibaba_fc_spec, f, indent=2)
    print("Generated Serverless Cloud specs")

if __name__ == "__main__":
    main()
