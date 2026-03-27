from typing import Optional
import os

from src.schema import APIMetrics
from src.providers.base import ProviderAnalyzer
from src.providers.openapi import parse_openapi_spec

class HerokuAnalyzer(ProviderAnalyzer):
    def get_name(self) -> str:
        return "Heroku"

    def analyze_service(self, service_name: str, filter_keywords: Optional[list] = None) -> Optional[APIMetrics]:
        spec_path = os.path.join("specs", f"heroku_{service_name}.json")
        
        if not os.path.exists(spec_path):
            return None
            
        return parse_openapi_spec("Heroku", service_name, spec_path, filter_keywords=filter_keywords)
