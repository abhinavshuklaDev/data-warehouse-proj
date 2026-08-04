"""
Inventory Event Schema
"""

from src.producer.schemas.base_schema import BaseEventSchema


class InventorySchema(BaseEventSchema):
    """
    Inventory event schema.
    """

    warehouse_id: str

    quantity_change: int

    reason: str