"""
A simplistic example implementation of a Kafka Consumer,
with the basics as described in the Confluent Python Client Getting Started guides.
"""

from functools import cache
from typing import Callable

from confluent_kafka import Consumer

from yhkee0404 import example_log as log
from yhkee0404.example_kafka.core import fetch_consumer_config, fetch_default_config
from yhkee0404.example_kafka.parser import parse_message

logger = log.get_logger("Kafka-Consumer-logger")


@cache
def get_consumer() -> Consumer:
    logger.info("a new instance of a Kafka Consumer")

    config = fetch_default_config() | fetch_consumer_config()

    return Consumer(config)


def consume(topic: str, callback: Callable[[str, str, str], None]) -> None:
    consumer = get_consumer()

    consumer.subscribe([topic])

    try:
        while True:
            msg = consumer.poll(1.0)

            if msg is None:
                continue

            if msg.error():
                logger.error(msg.error())
            else:
                topic, key, value = parse_message(msg)
                callback(topic, key, value)
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()
