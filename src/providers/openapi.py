import json
import collections
from typing import Optional
from src.schema import APIMetrics

def parse_openapi_spec(provider: str, service_name: str, spec_path: str, filter_keywords: Optional[list] = None) -> Optional[APIMetrics]:
    try:
        with open(spec_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Spec file not found at {spec_path}. Please download the OpenAPI spec for {provider} {service_name} and place it there.")
        return None
    except Exception as e:
        print(f"Error reading spec file {spec_path}: {e}")
        return None

    paths = data.get("paths", {})
    total_apis = 0
    verbs_count = collections.defaultdict(int)
    total_attributes = 0

    for path, path_item in paths.items():
        if filter_keywords:
            if not any(k.lower() in path.lower() for k in filter_keywords):
                continue
                
        if not isinstance(path_item, dict):
            continue
            
        for verb, operation in path_item.items():
            if verb.lower() not in ['get', 'post', 'put', 'patch', 'delete', 'options', 'head']:
                continue
                
            total_apis += 1
            verbs_count[verb.upper()] += 1
            
            # Count parameters
            params = operation.get("parameters", [])
            total_attributes += len(params)
            
            # Simple attribute count for request body if available
            # Doing a full schema depth calculation requires `$ref` chasing, 
            # for baseline we just count top-level properties or the body param itself
            if "requestBody" in operation:
                total_attributes += 1

    return APIMetrics(
        provider=provider,
        service_name=service_name,
        total_apis=total_apis,
        total_verbs=total_apis,
        verbs_count=dict(verbs_count),
        total_attributes=total_attributes
    )
