"""
Return Event Schema
"""

from pydantic import Field

from src.producer.schemas.base_schema import (
    BaseEventSchema,
)


class ReturnSchema(BaseEventSchema):

    return_id: str

    order_id: str

    reason: str

    refund_amount: float = Field(
        gt=0
    )

    return_status: str