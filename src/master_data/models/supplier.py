"""
Supplier model.
"""

from dataclasses import asdict, dataclass


@dataclass(slots=True)
class Supplier:
    """
    Supplier domain model.
    """

    supplier_id: str
    supplier_name: str
    country: str
    contact_email: str
    is_active: bool

    def to_dict(self) -> dict:
        return asdict(self) 