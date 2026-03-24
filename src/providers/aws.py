import collections
from typing import Optional
import botocore.session
from botocore.model import ServiceModel, OperationModel
from src.providers.base import ProviderAnalyzer
from src.schema import APIMetrics

class AWSAnalyzer(ProviderAnalyzer):
    def __init__(self, specs_dir: str = "specs"):
        super().__init__(specs_dir)
        self.session = botocore.session.get_session()

    def analyze_service(self, service_name: str, filter_keywords: Optional[list] = None) -> Optional[APIMetrics]:
        try:
            # We use an arbitrary region just to instantiate the client and get the model
            client = self.session.create_client(service_name, region_name='us-east-1')
            service_model: ServiceModel = client.meta.service_model
        except Exception as e:
            print(f"Error loading AWS service {service_name}: {e}")
            return None

        operations = service_model.operation_names
        total_apis = 0
        
        verbs_count = collections.defaultdict(int)
        total_attributes = 0

        for op_name in operations:
            if filter_keywords:
                if not any(k.lower() in op_name.lower() for k in filter_keywords):
                    continue
                    
            total_apis += 1
            op_model: OperationModel = service_model.operation_model(op_name)
            
            # Count HTTP verbs
            http_method = op_model.http.get('method', 'UNKNOWN')
            verbs_count[http_method] += 1
            
            # Count input attributes
            input_shape = op_model.input_shape
            if input_shape is not None:
                # members is a dict of parameter names to their shape
                total_attributes += len(input_shape.members)

        return APIMetrics(
            provider="AWS",
            service_name=service_name,
            total_apis=total_apis,
            total_verbs=total_apis, # Usually 1 verb per operation in AWS
            verbs_count=dict(verbs_count),
            total_attributes=total_attributes
        )
