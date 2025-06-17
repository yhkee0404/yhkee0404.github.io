from yhkee0404 import example_greeting as greeting, example_log as log

logger = log.get_logger("The DEV logger")
data = greeting.hello_world()

logger.info(data)
