"""
Context Service

Creates a realistic customer session context.
"""

from random import choice

from src.producer.models.event_context import EventContext
from src.producer.reference_data.event_sources import EVENT_SOURCES
from src.producer.repository.master_data_repository import (
    MasterDataRepository,
)
from src.producer.events.base_event import BaseEvent


class ContextService:
    """
    Creates realistic event contexts.
    """

    def __init__(
        self,
        repository: MasterDataRepository,
    ) -> None:

        self.repository = repository

    def create(self) -> EventContext:
        """
        Create a customer session.
        """

        customer = (
            self.repository.get_random_customer()
        )

        product = (
            self.repository.get_random_product()
        )

        return EventContext(
            customer_id=customer["customer_id"],
            product_id=product["product_id"],
            warehouse_id=product["warehouse_id"],
            supplier_id=product["supplier_id"],
            session_id=BaseEvent.generate_session_id(),
            source=choice(EVENT_SOURCES),
        )