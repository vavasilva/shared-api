import json


def http_response(data, status_code=200):
    return {
        'statusCode': status_code,
        'body': json.dumps(data),
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Content-Type": "application/json"
        }
    }
