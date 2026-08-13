"""
Business rules for Return events.
"""

from random import random

from src.producer.constants.return_status import (
    RETURN_REQUESTED,
)
from src.producer.rules.conversion_rules import (
    ORDER_RETURN,
)


class ReturnRules:

    @staticmethod
    def should_return() -> bool:
        return random() < ORDER_RETURN

    @staticmethod
    def status() -> str:
        return RETURN_REQUESTED