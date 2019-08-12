from datetime import datetime
import azure.functions as func
import json


def main(req: func.HttpRequest) -> func.HttpResponse:
    content = {}
    content['name'] = 'PythonNoRequirements'
    content['timestamp'] = datetime.utcnow().isoformat()
    content['tests'] = []
    return func.HttpResponse(
        mimetype="application/json",
        status_code=200,
        body=json.dumps(content)
    )
