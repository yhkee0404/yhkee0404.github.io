import functions_framework
from yhkee0404 import example_greeting as greeting
from yhkee0404.example_log import get_logger

logger = get_logger("greet-gcp-function-logger")


@functions_framework.http
def handler(_request):
    return greeting.hello_world()
