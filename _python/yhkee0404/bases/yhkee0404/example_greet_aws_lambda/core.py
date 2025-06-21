import json
from typing import Any

from yhkee0404 import example_greeting as greeting
from yhkee0404.example_log import get_logger

logger = get_logger("greet-aws-lambda-logger")


def handler(_event: dict[str, Any], _context: dict[str, Any]) -> dict[str, Any]:
    logger.info("The Lambda handler was invoked.")

    body = {"message": greeting.hello_world()}

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body),
    }
