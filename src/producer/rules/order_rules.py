"""
Business rules for Order events.
"""

from random import randint

from src.producer.constants.order_status import (
    ORDER_CREATED,
)


class OrderRules:

    MIN_QUANTITY = 1
    MAX_QUANTITY = 3

    @staticmethod
    def quantity() -> int:
        return randint(
            OrderRules.MIN_QUANTITY,
            OrderRules.MAX_QUANTITY,
        )

    @staticmethod
    def total(
        quantity: int,
        unit_price: float,
    ) -> float:

        return round(
            quantity * unit_price,
            2,
        )

    @staticmethod
    def status() -> str:
        return ORDER_CREATED