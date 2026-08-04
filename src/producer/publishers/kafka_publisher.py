"""
Kafka Publisher
"""

import json

from confluent_kafka import Producer
from src.common.logger import logger
from src.producer.config.kafka_config import KAFKA_CONFIG
from src.producer.publishers.publisher import Publisher


class KafkaPublisher(Publisher):
    """
    Publishes events to Kafka.
    """

    def __init__(self, topic: str):

        self.topic = topic

        self.producer = Producer(KAFKA_CONFIG)

    @staticmethod
    def delivery_report(err, msg):
        """
        Callback invoked once Kafka acknowledges delivery.
        """

        if err:
            logger.error(
                "Kafka delivery failed: %s",
                err,
            )
        else:
            logger.info(
                "Message delivered to %s [%d] offset %d",
                msg.topic(),
                msg.partition(),
                msg.offset(),
            )

    def publish(
        self,
        event: dict,
    ) -> None:

        self.producer.produce(
            topic=self.topic,
            value=json.dumps(event),
            callback=self.delivery_report,
        )

        self.producer.poll(0)

    def flush(self):

        self.producer.flush()