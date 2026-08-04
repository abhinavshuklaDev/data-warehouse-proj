"""
Kafka Configuration
"""

KAFKA_CONFIG = {
    "bootstrap.servers": "localhost:9092",
    "client.id": "ecommerce-producer",
    "acks": "all",
    "enable.idempotence": True,
    "compression.type": "snappy",
}