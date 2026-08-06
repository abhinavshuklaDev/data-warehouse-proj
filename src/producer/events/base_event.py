"""
Base Event

Common functionality for all streaming events.
"""

from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from uuid import uuid4

from pydantic import BaseModel


@dataclass(slots=True)
class BaseEvent:
    """
    Parent class for all events.
    """

    event_id: str
    event_type: str
    event_timestamp: str
    customer_id: str
    product_id: str
    session_id: str
    source: str

    @staticmethod
    def generate_event_id() -> str:
        return f"EVT-{uuid4().hex.upper()}"

    @staticmethod
    def generate_timestamp() -> str:
        return datetime.now(
            UTC
        ).isoformat()

    @staticmethod
    def generate_session_id() -> str:
        return f"SES-{uuid4().hex[:12].upper()}"

    def to_dict(self) -> dict:
        """
        Convert event into dictionary.
        """
        return asdict(self)

    def validate(
        self,
        schema: type[BaseModel],
    ):
        """
        Validate event using Pydantic schema.
        """
        schema(
            **self.to_dict()
        )

        return self