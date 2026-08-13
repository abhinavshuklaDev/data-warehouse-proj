"""
Business rules for Inventory events.
"""

from src.producer.constants.inventory_status import RESERVED


class InventoryRules:

    @staticmethod
    def remaining_stock(
        current_stock: int,
        ordered_quantity: int,
    ) -> int:

        return max(
            0,
            current_stock - ordered_quantity,
        )

    @staticmethod
    def status() -> str:
        return RESERVED