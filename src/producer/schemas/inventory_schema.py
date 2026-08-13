"""
Inventory Event Schema
"""

from pydantic import Field

from src.producer.schemas.base_schema import (
    BaseEventSchema,
)


class InventorySchema(BaseEventSchema):

    inventory_id: str

    order_id: str

    warehouse_id: str

    quantity_reserved: int = Field(gt=0)

    remaining_stock: int = Field(ge=0)

    inventory_status: str