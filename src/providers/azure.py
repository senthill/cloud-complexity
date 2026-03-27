import os
import requests
from typing import Optional
from src.providers.base import ProviderAnalyzer
from src.schema import APIMetrics
from src.providers.openapi import parse_openapi_spec

class AzureAnalyzer(ProviderAnalyzer):
    def __init__(self, specs_dir: str = "specs"):
        super().__init__(specs_dir)
        os.makedirs(self.specs_dir, exist_ok=True)

    def _get_spec_path(self, service_name: str) -> str:
        return os.path.join(self.specs_dir, f"azure_{service_name}.json")

    def _fetch_spec_if_missing(self, service_name: str):
        spec_path = self._get_spec_path(service_name)
        if os.path.exists(spec_path):
            return

        # known stable urls for some services
        KNOWN_URLS = {
            "compute": "https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/compute/resource-manager/Microsoft.Compute/ComputeRP/stable/2024-03-01/compute.json"
        }
        
        url = KNOWN_URLS.get(service_name)
        if url:
            print(f"Downloading Azure {service_name} spec from {url}...")
            try:
                response = requests.get(url)
                response.raise_for_status()
                with open(spec_path, 'w') as f:
                    f.write(response.text)
            except Exception as e:
                print(f"Failed to download Azure spec: {e}")

    def get_name(self) -> str:
        return "Azure"

    def analyze_service(self, service_name: str, filter_keywords: Optional[list] = None) -> Optional[APIMetrics]:
        self._fetch_spec_if_missing(service_name)
        spec_path = self._get_spec_path(service_name)
        return parse_openapi_spec("Azure", service_name, spec_path, filter_keywords=filter_keywords)
