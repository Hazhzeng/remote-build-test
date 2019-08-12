from typing import List, Dict
from datetime import datetime
import azure.functions as func
import json


def main(req: func.HttpRequest) -> func.HttpResponse:
    content = {}
    content['name'] = 'PythonAzureRequirements'
    content['timestamp'] = datetime.utcnow().isoformat()
    
    content['tests'] = []
    append_azure_blob_test(content['tests'])

    return func.HttpResponse(
        mimetype="application/json",
        status_code=200,
        body=json.dumps(content)
    )


def append_azure_blob_test(tests: List[Dict[str, str]]) -> List[Dict[str, str]]:
    test = {
        "name": "azure_blob_test",
        "expected_status_code": "200",
    }
    tests.append(test)
    return tests