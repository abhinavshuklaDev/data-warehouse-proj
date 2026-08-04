"""
Event Context

Represents the context shared by a sequence of events.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class EventContext:
    """
    Shared context for all events in a session.
    """

    customer_id: str
    product_id: str
    warehouse_id: str
    supplier_id: str
    session_id: str
    source: str