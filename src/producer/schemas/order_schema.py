"""
Order Event Schema
"""

from pydantic import Field

from src.producer.schemas.base_schema import (
    BaseEventSchema,
)


class OrderSchema(BaseEventSchema):

    order_id: str

    warehouse_id: str

    supplier_id: str

    quantity: int = Field(gt=0)

    unit_price: float = Field(gt=0)

    total_amount: float = Field(gt=0)

    order_status: str