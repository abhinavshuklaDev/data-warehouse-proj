"""
Payment Event
"""

from dataclasses import dataclass
from uuid import uuid4

from src.producer.constants.event_types import PAYMENT
from src.producer.events.base_event import BaseEvent
from src.producer.models.event_context import EventContext
from src.producer.rules.payment_rules import PaymentRules
from src.producer.schemas.payment_schema import PaymentSchema


@dataclass(slots=True)
class PaymentEvent(BaseEvent):

    payment_id: str

    order_id: str

    payment_method: str

    payment_status: str

    transaction_amount: float

    @classmethod
    def create(
        cls,
        context: EventContext,
        order,
    ):

        event = cls(
            event_id=cls.generate_event_id(),
            event_type=PAYMENT,
            event_timestamp=cls.generate_timestamp(),

            customer_id=context.customer_id,
            product_id=context.product_id,
            session_id=context.session_id,
            source=context.source,

            payment_id=f"PAY-{uuid4().hex[:10].upper()}",

            order_id=order.order_id,

            payment_method=PaymentRules.method(),

            payment_status=PaymentRules.status(),

            transaction_amount=order.total_amount,
        )

        return event.validate(
            PaymentSchema
        )