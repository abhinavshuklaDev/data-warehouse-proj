"""
File Publisher
"""

import json
from pathlib import Path

from src.producer.publishers.publisher import Publisher


class FilePublisher(Publisher):
    """
    Writes events as JSON Lines.
    """

    def __init__(
        self,
        output_file: str = "data/events/events.jsonl",
    ):
        self.output_file = Path(output_file)

        self.output_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

    def publish(self, event: dict) -> None:

        with self.output_file.open(
            "a",
            encoding="utf-8",
        ) as file:

            file.write(
                json.dumps(
                    event,
                    default=str,
                )
            )

            file.write("\n")