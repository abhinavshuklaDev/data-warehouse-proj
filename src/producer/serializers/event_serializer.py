"""
Event Serializer

Converts events into dictionaries and JSON.
"""

import json
from dataclasses import asdict, is_dataclass


class EventSerializer:
    """
    Utility class for serializing events.
    """

    @staticmethod
    def to_dict(event) -> dict:
        """
        Convert a dataclass event into a dictionary.
        """

        if not is_dataclass(event):
            raise TypeError(
                "Expected a dataclass instance."
            )

        return asdict(event)

    @staticmethod
    def to_json(event) -> str:
        """
        Convert event into JSON.
        """

        return json.dumps(
            EventSerializer.to_dict(event),
            ensure_ascii=False,
        )