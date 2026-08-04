"""
Payment Event Schema
"""

from src.producer.schemas.base_schema import BaseEventSchema


class PaymentSchema(BaseEventSchema):
    """
    Payment event schema.
    """

    payment_id: str

    order_id: str

    payment_method: str

    payment_status: str

    amount: float   