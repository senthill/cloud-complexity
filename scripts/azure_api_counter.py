import requests
import json
import base64
import time
from typing import Dict, List, Optional

class AzureAPICounter:
    def __init__(self, token: Optional[str] = None):
        self.base_url = "https://api.github.com/repos/Azure/azure-rest-api-specs/contents"
        self.headers = {"Accept": "application/vnd.github.v3+json"}
        if token:
            self.headers["Authorization"] = f"token {token}"
        self.stats = {}

    def get_contents(self, path: str):
        url = f"{self.base_url}/{path}"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 403:
            print("Rate limit exceeded. Please provide a GITHUB_TOKEN.")
            return []
        return response.json()

    def count_ops_in_file(self, download_url: str):
        response = requests.get(download_url)
        if response.status_code != 200:
            return 0, 0
        
        try:
            spec = response.json()
            paths = spec.get("paths", {})
            total_ops = 0
            total_attrs = 0
            
            for path, methods in paths.items():
                for method, details in methods.items():
                    if method.lower() in ["get", "post", "put", "delete", "patch"]:
                        total_ops += 1
                        # Count parameters
                        params = details.get("parameters", [])
                        total_attrs += len(params)
                        # Count request body properties if applicable
                        # (Simple heuristic: count properties in definitions if referenced)
            
            return total_ops, total_attrs
        except:
            return 0, 0

    def analyze_provider(self, provider_name: str):
        print(f"Analyzing Provider: {provider_name}...")
        results = {"apis": 0, "attributes": 0, "services": []}
        
        # Path: specification/{provider}/resource-manager
        path = f"specification/{provider_name}/resource-manager"
        services = self.get_contents(path)
        
        if not isinstance(services, list):
            return results

        # For brevity in this tool, we analyze the first 3 sub-services found
        for service in services[:3]:
            if service["type"] != "dir":
                continue
            
            service_name = service["name"]
            # Find 'stable' folder
            stable_path = f"{path}/{service_name}/stable"
            versions = self.get_contents(stable_path)
            
            if not isinstance(versions, list) or not versions:
                continue
            
            # Use the latest stable version
            latest_version = sorted([v["name"] for v in versions if v["type"] == "dir"])[-1]
            version_path = f"{stable_path}/{latest_version}"
            files = self.get_contents(version_path)
            
            if not isinstance(files, list):
                continue
                
            for f in files:
                if f["name"].endswith(".json") and "client" not in f["name"].lower():
                    ops, attrs = self.count_ops_in_file(f["download_url"])
                    results["apis"] += ops
                    results["attributes"] += attrs
                    results["services"].append({
                        "name": service_name,
                        "version": latest_version,
                        "apis": ops,
                        "attributes": attrs
                    })
        
        return results

if __name__ == "__main__":
    # Example usage: Analyze Microsoft.Compute
    import sys
    token = sys.argv[1] if len(sys.argv) > 1 else None
    counter = AzureAPICounter(token)
    
    # Analyze a few core providers
    core_providers = ["Microsoft.Compute", "Microsoft.Network", "Microsoft.Storage"]
    
    total_summary = {"apis": 0, "attributes": 0}
    for provider in core_providers:
        res = counter.analyze_provider(provider)
        total_summary["apis"] += res["apis"]
        total_summary["attributes"] += res["attributes"]
        print(json.dumps(res, indent=2))
        
    print("\n--- GLOBAL SUMMARY (CORE 3) ---")
    print(json.dumps(total_summary, indent=2))
