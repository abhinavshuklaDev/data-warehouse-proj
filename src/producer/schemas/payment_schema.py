"""
Payment Event Schema
"""

from pydantic import Field

from src.producer.schemas.base_schema import (
    BaseEventSchema,
)


class PaymentSchema(BaseEventSchema):

    payment_id: str

    order_id: str

    payment_method: str

    payment_status: str

    transaction_amount: float = Field(
        gt=0
    )