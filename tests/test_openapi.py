import json
import os
import pytest
from src.providers.openapi import parse_openapi_spec

def test_openapi_parser(tmp_path):
    spec_data = {
        "paths": {
            "/api/v1/resource": {
                "get": {
                    "parameters": [{"name": "id"}, {"name": "filter"}]
                },
                "post": {
                    "parameters": [],
                    "requestBody": {"content": {}}
                }
            },
            "/api/v1/other": {
                "delete": {
                    "parameters": [{"name": "id"}]
                }
            }
        }
    }
    
    spec_file = tmp_path / "dummy_spec.json"
    with open(spec_file, 'w') as f:
        json.dump(spec_data, f)
        
    metrics = parse_openapi_spec("TestProvider", "TestService", str(spec_file))
    
    assert metrics is not None
    assert metrics.provider == "TestProvider"
    assert metrics.service_name == "TestService"
    
    # 3 total paths/methods (get, post, delete)
    assert metrics.total_apis == 3
    assert metrics.total_verbs == 3
    
    # get: 2 params
    # post: 0 params, 1 requestBody = 1 attribute
    # delete: 1 param
    # total attributes = 2 + 1 + 1 = 4
    assert metrics.total_attributes == 4
    
    assert metrics.verbs_count == {"GET": 1, "POST": 1, "DELETE": 1}
