"""
ID Generator
"""

from itertools import count


class IDGenerator:
    """
    Generates sequential business IDs.
    """

    _order = count(1)

    _payment = count(1)

    _return = count(1)

    _shipment = count(1)

    @classmethod
    def order_id(cls):

        return f"ORD{next(cls._order):08d}"

    @classmethod
    def payment_id(cls):

        return f"PAY{next(cls._payment):08d}"

    @classmethod
    def return_id(cls):

        return f"RET{next(cls._return):08d}"

    @classmethod
    def shipment_id(cls):

        return f"SHP{next(cls._shipment):08d}"