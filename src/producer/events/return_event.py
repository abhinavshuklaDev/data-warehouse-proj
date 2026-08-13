"""
Return Event
"""

from dataclasses import dataclass
from random import choice
from uuid import uuid4

from src.producer.constants.event_types import RETURN
from src.producer.events.base_event import BaseEvent
from src.producer.models.event_context import EventContext
from src.producer.reference_data.return_reasons import (
    RETURN_REASONS,
)
from src.producer.rules.return_rules import (
    ReturnRules,
)
from src.producer.schemas.return_schema import (
    ReturnSchema,
)


@dataclass(slots=True)
class ReturnEvent(BaseEvent):

    return_id: str

    order_id: str

    reason: str

    refund_amount: float

    return_status: str

    @classmethod
    def create(
        cls,
        context: EventContext,
        order,
    ):

        event = cls(
            event_id=cls.generate_event_id(),
            event_type=RETURN,
            event_timestamp=cls.generate_timestamp(),

            customer_id=context.customer_id,
            product_id=context.product_id,
            session_id=context.session_id,
            source=context.source,

            return_id=f"RET-{uuid4().hex[:10].upper()}",

            order_id=order.order_id,

            reason=choice(
                RETURN_REASONS
            ),

            refund_amount=order.total_amount,

            return_status=ReturnRules.status(),
        )

        return event.validate(
            ReturnSchema
        )