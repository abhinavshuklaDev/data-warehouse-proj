"""
Product View Event
"""

from dataclasses import dataclass
from random import choice, randint
from src.producer.reference_data.search_keywords import (
    SEARCH_KEYWORDS,
)
from src.producer.events.base_event import BaseEvent
from src.producer.models.event_context import EventContext
from src.producer.reference_data.event_sources import (
    EVENT_SOURCES,
)
from src.producer.reference_data.referrers import (
    REFERRERS,
)
from src.producer.reference_data.event_types import (
    PRODUCT_VIEW,
)
from src.producer.schemas.product_view_schema import (
    ProductViewSchema,
)


@dataclass(slots=True)
class ProductViewEvent(BaseEvent):

    view_duration_seconds: int

    device_type: str

    referrer: str

    page_number: int

    search_keyword: str

    @classmethod
    def create(
        cls,
        context: EventContext,
    ):

        event = cls(
            event_id=cls.generate_event_id(),
            event_type=PRODUCT_VIEW,
            event_timestamp=cls.generate_timestamp(),
            customer_id=context.customer_id,
            product_id=context.product_id,
            session_id=context.session_id,
            source=context.source,
            view_duration_seconds=randint(5, 300),
            device_type=choice(
                EVENT_SOURCES
            ),
            referrer=choice(
                REFERRERS
            ),
            page_number=randint(1, 10),
            search_keyword=choice(
                SEARCH_KEYWORDS
            ),
        )
        return event.validate(
            ProductViewSchema
        )