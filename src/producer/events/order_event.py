"""
Order Event
"""

from dataclasses import dataclass
from uuid import uuid4

from src.producer.constants.event_types import ORDER
from src.producer.constants.order_status import ORDER_CREATED
from src.producer.events.base_event import BaseEvent
from src.producer.models.event_context import EventContext
from src.producer.rules.order_rules import OrderRules
from src.producer.schemas.order_schema import OrderSchema


@dataclass(slots=True)
class OrderEvent(BaseEvent):

    order_id: str

    warehouse_id: str

    supplier_id: str

    quantity: int

    unit_price: float

    total_amount: float

    order_status: str

    @classmethod
    def create(
        cls,
        context: EventContext,
        repository,
    ):

        product = repository.get_product(
            context.product_id
        )

        quantity = OrderRules.quantity()

        unit_price = float(
            product["unit_price"]
        )

        event = cls(
            event_id=cls.generate_event_id(),
            event_type=ORDER,
            event_timestamp=cls.generate_timestamp(),
            customer_id=context.customer_id,
            product_id=context.product_id,
            session_id=context.session_id,
            source=context.source,
            order_id=f"ORD-{uuid4().hex[:10].upper()}",
            warehouse_id=context.warehouse_id,
            supplier_id=context.supplier_id,
            quantity=quantity,
            unit_price=unit_price,
            total_amount=OrderRules.total(
                quantity,
                unit_price,
            ),
            order_status=OrderRules.status(),
        )

        return event.validate(
            OrderSchema
        )