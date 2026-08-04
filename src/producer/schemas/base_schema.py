"""
Base Event Schema
"""

from pydantic import BaseModel, ConfigDict


class BaseEventSchema(BaseModel):
    """
    Base schema for all events.
    """

    model_config = ConfigDict(
        extra="forbid",
        frozen=True,
    )

    event_id: str

    event_type: str

    event_timestamp: str

    customer_id: str

    product_id: str

    session_id: str

    source: str