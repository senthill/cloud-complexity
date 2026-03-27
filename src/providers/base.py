import abc
from typing import Optional
from src.schema import APIMetrics

class ProviderAnalyzer(abc.ABC):
    def __init__(self, specs_dir: str = "specs"):
        self.specs_dir = specs_dir
        
    @abc.abstractmethod
    def get_name(self) -> str:
        """Return the display name of the provider."""
        pass

    @abc.abstractmethod
    def analyze_service(self, service_name: str, filter_keywords: Optional[list] = None) -> Optional[APIMetrics]:
        """
        Analyze a specific service and return its API metrics.
        Returns None if the service is not found or unsupported.
        """
        pass
