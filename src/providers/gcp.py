import os
import json
import collections
import requests
from typing import Optional
from src.providers.base import ProviderAnalyzer
from src.schema import APIMetrics

class GCPAnalyzer(ProviderAnalyzer):
    def __init__(self, specs_dir: str = "specs"):
        super().__init__(specs_dir)
        os.makedirs(self.specs_dir, exist_ok=True)

    def _get_spec_path(self, service_name: str) -> str:
        return os.path.join(self.specs_dir, f"gcp_{service_name}.json")

    def _fetch_spec(self, service_name: str) -> Optional[dict]:
        spec_path = self._get_spec_path(service_name)
        
        # Load locally if available
        if os.path.exists(spec_path):
            with open(spec_path, 'r') as f:
                return json.load(f)

        # Map some common names to their Discovery API name and version
        # You may need to expand this based on actual mappings
        SERVICE_DEFAULTS = {
            "compute": ("compute", "v1"),
            "storage": ("storage", "v1"),
            "cloudfunctions": ("cloudfunctions", "v1")
        }
        
        mapping = SERVICE_DEFAULTS.get(service_name)
        if not mapping:
            print(f"Unknown Google API details for service: {service_name}")
            return None
            
        api_name, api_version = mapping
        url = f"https://www.googleapis.com/discovery/v1/apis/{api_name}/{api_version}/rest"
        
        try:
            print(f"Downloading GCP {service_name} spec from {url}...")
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            # Save locally
            with open(spec_path, 'w') as f:
                json.dump(data, f, indent=2)
            return data
        except Exception as e:
            print(f"Error fetching GCP spec for {service_name}: {e}")
            return None

    def _count_methods_and_attributes(self, resources: dict, filter_keywords: Optional[list] = None) -> tuple:
        # Returns (total_apis, verbs_count, total_attributes)
        total_apis = 0
        verbs_count = collections.defaultdict(int)
        total_attributes = 0
        
        if not resources:
            return 0, verbs_count, 0

        for resource_name, resource_obj in resources.items():
            matches_filter = False
            if not filter_keywords:
                matches_filter = True
            elif any(k.lower() in resource_name.lower() for k in filter_keywords):
                matches_filter = True

            # Process methods in this resource
            methods = resource_obj.get("methods", {})
            if matches_filter:
                for method_name, method_obj in methods.items():
                    total_apis += 1
                    verb = method_obj.get("httpMethod", "UNKNOWN")
                    verbs_count[verb] += 1
                    
                    # Count input parameters (path, query)
                    params = method_obj.get("parameters", {})
                    total_attributes += len(params)
                
                # Count payload properties if present
                request = method_obj.get("request", {})
                if request:
                    # Let's add 1 attribute for the request body to keep it simple
                    total_attributes += 1 

            # Recursively process sub-resources
            sub_resources = resource_obj.get("resources")
            if sub_resources:
                sub_apis, sub_verbs, sub_attrs = self._count_methods_and_attributes(
                    sub_resources,
                    None if matches_filter else filter_keywords
                )
                total_apis += sub_apis
                total_attributes += sub_attrs
                for k, v in sub_verbs.items():
                    verbs_count[k] += v
                    
        return total_apis, verbs_count, total_attributes

    def analyze_service(self, service_name: str, filter_keywords: Optional[list] = None) -> Optional[APIMetrics]:
        data = self._fetch_spec(service_name)
        if not data:
            return None

        resources = data.get("resources", {})
        total_apis, verbs_count, total_attributes = self._count_methods_and_attributes(resources, filter_keywords)
        
        # In Google APIs, some top-level methods might exist without resources (uncommon but possible)
        top_level_methods = data.get("methods", {})
        if top_level_methods and not filter_keywords:
            tl_apis, tl_verbs, tl_attrs = self._count_methods_and_attributes({"_top": {"methods": top_level_methods}})
            total_apis += tl_apis
            total_attributes += tl_attrs
            for k, v in tl_verbs.items():
                verbs_count[k] += v

        return APIMetrics(
            provider="GCP",
            service_name=service_name,
            total_apis=total_apis,
            total_verbs=total_apis,
            verbs_count=dict(verbs_count),
            total_attributes=total_attributes
        )
