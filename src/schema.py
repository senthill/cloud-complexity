from pydantic import BaseModel
from typing import List, Dict

class APIMetrics(BaseModel):
    provider: str
    service_name: str
    total_apis: int
    total_verbs: int
    verbs_count: Dict[str, int]
    total_attributes: int

class ServiceComparison(BaseModel):
    service_category: str
    metrics: List[APIMetrics]
