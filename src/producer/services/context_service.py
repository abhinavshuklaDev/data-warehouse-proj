"""
Context Service
"""

from random import choice

import pandas as pd

from src.producer.models.event_context import EventContext
from src.producer.events.base_event import BaseEvent
from src.producer.reference_data.event_sources import EVENT_SOURCES


class ContextService:
    """
    Creates event contexts.
    """

    def __init__(
        self,
        customers: pd.DataFrame,
        products: pd.DataFrame,
    ):
        self.customers = customers
        self.products = products

    def create(self) -> EventContext:
        """
        Create one realistic browsing context.
        """

        customer = self.customers.sample().iloc[0]

        product = self.products.sample().iloc[0]

        return EventContext(
            customer_id=customer["customer_id"],
            product_id=product["product_id"],
            warehouse_id=product["warehouse_id"],
            supplier_id=product["supplier_id"],
            session_id=BaseEvent.generate_session_id(),
            source=choice(EVENT_SOURCES),
        )