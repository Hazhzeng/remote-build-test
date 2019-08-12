import logging
import json
from datetime import datetime

import azure.functions as func
from azure.storage import blob

import azure
import azure.storage as store


def main(req: func.HttpRequest) -> func.HttpResponse:
    content = {}
    content['name'] = 'azure_blob_test'
    content['timestamp'] = datetime.utcnow().isoformat()
    content['blob_file'] = str(blob.__file__)
    content['func_file'] = str(func.__file__)
    content['azure_path'] = str(azure.__path__)
    content['store_file'] = str(store.__path__)
    content['blob_path'] = str(blob.__path__)

    return func.HttpResponse(
        mimetype="application/json",
        status_code=200,
        body=json.dumps(content)
    )
