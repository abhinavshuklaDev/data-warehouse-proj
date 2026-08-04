"""
Base Event

Contains common metadata shared by every event.
"""

from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from uuid import uuid4


@dataclass(slots=True)
class BaseEvent:
    """
    Parent class for all streaming events.
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
        """
        Generate a unique event ID.
        """
        return f"EVT-{uuid4().hex.upper()}"

    @staticmethod
    def generate_timestamp() -> str:
        """
        Generate an ISO-8601 UTC timestamp.
        """
        return datetime.now(UTC).isoformat()

    @staticmethod
    def generate_session_id() -> str:
        """
        Generate a session identifier.
        """
        return f"SES-{uuid4().hex[:12].upper()}"

    def to_dict(self) -> dict:
        """
        Convert event to dictionary.
        """
        return asdict(self)