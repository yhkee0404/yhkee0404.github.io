from yhkee0404 import example_kafka as kafka
from yhkee0404 import example_log as log

logger = log.get_logger("Consumer-app-logger")


def parse_message(topic: str, key: str, value: str) -> None:
    logger.info("Consumed message with topic=%s, key=%s, value=%s", topic, key, value)


def main() -> None:
    topic = kafka.get_topic("message")

    kafka.consumer.consume(topic, parse_message)
