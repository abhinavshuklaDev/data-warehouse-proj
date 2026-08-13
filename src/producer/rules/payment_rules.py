"""
Business rules for Payment events.
"""

from random import choices

from src.producer.constants.payment_status import (
    PAYMENT_SUCCESS,
    PAYMENT_FAILED,
    PAYMENT_PENDING,
)
from src.producer.reference_data.payment_methods import (
    PAYMENT_METHODS,
)


class PaymentRules:

    STATUS = [
        PAYMENT_SUCCESS,
        PAYMENT_FAILED,
        PAYMENT_PENDING,
    ]

    WEIGHTS = [
        92,
        3,
        5,
    ]

    @staticmethod
    def status() -> str:
        return choices(
            PaymentRules.STATUS,
            weights=PaymentRules.WEIGHTS,
            k=1,
        )[0]

    @staticmethod
    def method() -> str:
        return choices(
            PAYMENT_METHODS,
            k=1,
        )[0]