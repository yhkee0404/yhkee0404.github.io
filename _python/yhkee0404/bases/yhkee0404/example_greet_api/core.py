from fastapi import FastAPI

from yhkee0404 import example_greeting as greeting
from yhkee0404.example_log import get_logger

logger = get_logger("greet-FastAPI-logger")
app = FastAPI()


@app.get("/")
def root() -> dict[str, str]:
    logger.info("The FastAPI root endpoint was called.")
    logger.debug("This is a debug message")

    return {"message": greeting.hello_world()}
