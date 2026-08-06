from src.producer.publishers.kafka_publisher import (
    KafkaPublisher,
)


def test_kafka_publisher():

    publisher = KafkaPublisher(
        "events"
    )

    publisher.publish(
        {
            "message": "hello kafka"
        }
    )

    publisher.flush()

    assert True