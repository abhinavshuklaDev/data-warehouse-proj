"""
Console Publisher
"""

import json

from src.producer.publishers.publisher import Publisher


class ConsolePublisher(Publisher):
    """
    Prints events to the console.
    """

    def publish(self, event: dict) -> None:
        """
        Print the event as formatted JSON.
        """
        print(
            json.dumps(
                event,
                indent=4,
                default=str,
            )
        )