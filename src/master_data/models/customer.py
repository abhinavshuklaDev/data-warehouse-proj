"""
Customer model.

Represents a customer in the e-commerce platform.
"""

from dataclasses import asdict, dataclass


@dataclass(slots=True)
class Customer:
    """
    Customer domain model.
    """

    customer_id: str
    first_name: str
    last_name: str
    email: str
    phone_number: str
    gender: str
    date_of_birth: str
    city: str
    state: str
    country: str
    postal_code: str
    loyalty_tier: str
    registration_date: str
    is_active: bool

    def to_dict(self) -> dict:
        """
        Convert the Customer object into a dictionary.
        """
        return asdict(self)