import os
import requests
from typing import Optional
from src.providers.base import ProviderAnalyzer
from src.schema import APIMetrics
from src.providers.openapi import parse_openapi_spec

class AlibabaAnalyzer(ProviderAnalyzer):
    def __init__(self, specs_dir: str = "specs"):
        super().__init__(specs_dir)
        os.makedirs(self.specs_dir, exist_ok=True)

    def _get_spec_path(self, service_name: str) -> str:
        return os.path.join(self.specs_dir, f"alibaba_{service_name}.json")

    def _fetch_spec_if_missing(self, service_name: str):
        spec_path = self._get_spec_path(service_name)
        if os.path.exists(spec_path):
            return
            
        # Example URL for Alibaba Cloud OpenAPI specs if known. Needs manual download otherwise.
        # Alternatively, downloading their generic swagger file:
        print(f"Please manually download the Alibaba Swagger/OpenAPI spec for {service_name} to {spec_path}")

    def analyze_service(self, service_name: str, filter_keywords: Optional[list] = None) -> Optional[APIMetrics]:
        self._fetch_spec_if_missing(service_name)
        spec_path = self._get_spec_path(service_name)
        
        import json
        import collections
        
        try:
            with open(spec_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception as e:
            print(f"Error loading Alibaba spec {spec_path}: {e}")
            return None

        apis = data.get("apis", {})
        total_apis = len(apis)
        verbs_count = collections.defaultdict(int)
        total_attributes = 0
        
        for api_name, api_info in apis.items():
            if filter_keywords:
                if not any(k.lower() in api_name.lower() for k in filter_keywords):
                    continue
                    
            methods = api_info.get("methods", ["POST"])
            for m in methods:
                verbs_count[m.upper()] += 1
            
            params = api_info.get("parameters", [])
            total_attributes += len(params)
            
        return APIMetrics(
            provider="Alibaba",
            service_name=service_name,
            total_apis=total_apis,
            total_verbs=sum(verbs_count.values()),
            verbs_count=dict(verbs_count),
            total_attributes=total_attributes
        )
