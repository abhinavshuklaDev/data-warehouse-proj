"""
Return Event Schema
"""

from src.producer.schemas.base_schema import BaseEventSchema


class ReturnSchema(BaseEventSchema):
    """
    Return event schema.
    """

    return_id: str

    order_id: str

    reason: str