import functions_framework
from flask import Request

from yhkee0404 import example_greeting as greeting
from yhkee0404.example_log import get_logger

logger = get_logger("greet-gcp-function-logger")


@functions_framework.http  # type: ignore[reportUnknownMemberType]
def handler(_request: Request) -> str:
    return greeting.hello_world()
