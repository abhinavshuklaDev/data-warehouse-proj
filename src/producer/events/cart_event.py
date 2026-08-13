"""
Cart Event
"""

from dataclasses import dataclass
from random import randint
from uuid import uuid4

from src.producer.events.base_event import BaseEvent
from src.producer.models.event_context import (
    EventContext,
)
from src.producer.reference_data.cart_rules import (
    MIN_CART_QUANTITY,
    MAX_CART_QUANTITY,
)
from src.producer.constants.event_types import (
    CART,
)
from src.producer.schemas.cart_schema import (
    CartSchema,
)


@dataclass(slots=True)
class CartEvent(BaseEvent):

    cart_id: str

    quantity: int

    unit_price: float

    cart_total: float

    @classmethod
    def create(
        cls,
        context: EventContext,
        product: dict,
    ):

        quantity = randint(
            MIN_CART_QUANTITY,
            MAX_CART_QUANTITY,
        )

        unit_price = float(
            product["unit_price"]
        )

        cart_total = round(
            quantity * unit_price,
            2,
        )

        event = cls(
            event_id=cls.generate_event_id(),
            event_type=CART,
            event_timestamp=cls.generate_timestamp(),
            customer_id=context.customer_id,
            product_id=context.product_id,
            session_id=context.session_id,
            source=context.source,
            cart_id=f"CART-{uuid4().hex[:10].upper()}",
            quantity=quantity,
            unit_price=unit_price,
            cart_total=cart_total,
        )

        return event.validate(
            CartSchema
        )