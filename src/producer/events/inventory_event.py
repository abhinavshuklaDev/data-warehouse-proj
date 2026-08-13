"""
Inventory Event
"""

from dataclasses import dataclass
from uuid import uuid4

from src.producer.constants.event_types import INVENTORY
from src.producer.events.base_event import BaseEvent
from src.producer.models.event_context import EventContext
from src.producer.rules.inventory_rules import InventoryRules
from src.producer.schemas.inventory_schema import InventorySchema


@dataclass(slots=True)
class InventoryEvent(BaseEvent):

    inventory_id: str

    order_id: str

    warehouse_id: str

    quantity_reserved: int

    remaining_stock: int

    inventory_status: str

    @classmethod
    def create(
        cls,
        context: EventContext,
        order,
        repository,
    ):

        product = repository.get_product(
            context.product_id
        )

        current_stock = int(
            product["stock_quantity"]
        )

        event = cls(
            event_id=cls.generate_event_id(),
            event_type=INVENTORY,
            event_timestamp=cls.generate_timestamp(),

            customer_id=context.customer_id,
            product_id=context.product_id,
            session_id=context.session_id,
            source=context.source,

            inventory_id=f"INV-{uuid4().hex[:10].upper()}",

            order_id=order.order_id,

            warehouse_id=context.warehouse_id,

            quantity_reserved=order.quantity,

            remaining_stock=InventoryRules.remaining_stock(
                current_stock,
                order.quantity,
            ),

            inventory_status=InventoryRules.status(),
        )

        return event.validate(
            InventorySchema
        )