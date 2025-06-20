import json

from yhkee0404 import example_greeting as greeting
from yhkee0404.example_log import get_logger

logger = get_logger("greet-aws-lambda-logger")


def handler(event: dict, context: dict) -> dict:
    logger.info("The Lambda handler was invoked.")

    body = {"message": greeting.hello_world()}

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body),
    }
