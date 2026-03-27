from typing import Optional
import os

from src.schema import APIMetrics
from src.providers.base import ProviderAnalyzer
from src.providers.openapi import parse_openapi_spec

class DigitalOceanAnalyzer(ProviderAnalyzer):
    def get_name(self) -> str:
        return "DigitalOcean"

    def analyze_service(self, service_name: str, filter_keywords: Optional[list] = None) -> Optional[APIMetrics]:
        spec_path = os.path.join(self.specs_dir, "do", f"{service_name}.json")
        
        if not os.path.exists(spec_path):
            return None
            
        return parse_openapi_spec("DigitalOcean", service_name, spec_path, filter_keywords=filter_keywords)
