"""
Kafka Publisher

Publishes events to Kafka.
"""

import json

from confluent_kafka import Producer

from src.common.logger import logger
from src.config.config import config


class KafkaPublisher:

    def __init__(
        self,
        topic: str,
    ) -> None:

        self.topic = topic

        self.producer = Producer(
            {
                "bootstrap.servers": config.config.kafka.bootstrap_servers,
                "client.id": "data-warehouse-producer",
            }
        )

    @staticmethod
    def delivery_report(
        err,
        msg,
    ):

        if err:

            logger.error(
                f"Delivery failed: {err}"
            )

        else:

            logger.info(
                f"Delivered to {msg.topic()} "
                f"partition={msg.partition()} "
                f"offset={msg.offset()}"
            )

    def publish(
        self,
        event: dict,
    ):

        self.producer.produce(
            self.topic,
            value=json.dumps(event),
            callback=self.delivery_report,
        )

        self.producer.poll(0)

    def flush(self):

        self.producer.flush()