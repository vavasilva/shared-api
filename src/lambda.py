import logging

from libraries.utils import http_response

logging.getLogger().setLevel(logging.INFO)


def lambda_handler(event, context):
    logging.info(f"event {event}")
    return http_response("OK")
