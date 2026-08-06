"""
Producer Engine

Coordinates session generation and event publishing.
"""

import time

from src.common.logger import logger
from src.config.config import config
from src.producer.publishers.kafka_publisher import KafkaPublisher
from src.producer.serializers.event_serializer import EventSerializer
from src.producer.services.session_simulator import SessionSimulator


class ProducerEngine:

    def __init__(
        self,
        simulator: SessionSimulator,
        topic: str = "events",
    ) -> None:

        self.simulator = simulator

        self.publisher = KafkaPublisher(
            topic=topic
        )

    def run(self):

        logger.info(
            "Producer Engine Started..."
        )

        while True:

            events = self.simulator.generate()

            for event in events:

                event_json = EventSerializer.to_dict(
                    event
                )

                self.publisher.publish(
                    event_json
                )

            self.publisher.flush()

            logger.info(
                f"Published {len(events)} events."
            )

            time.sleep(
                1 / config.config.producer.events_per_second
            )