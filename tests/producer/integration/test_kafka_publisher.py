import socket

from src.producer.publishers.kafka_publisher import (
    KafkaPublisher,
)


def kafka_available() -> bool:

    connection = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
    )

    connection.settimeout(2)

    try:

        connection.connect(
            ("localhost", 9092)
        )

        return True

    except OSError:

        return False

    finally:

        connection.close()


def test_kafka_publisher():

    if not kafka_available():

        return

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