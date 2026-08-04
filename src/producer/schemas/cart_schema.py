"""
Cart Event Schema
"""

from src.producer.schemas.base_schema import BaseEventSchema


class CartSchema(BaseEventSchema):
    """
    Cart event schema.
    """

    quantity: int