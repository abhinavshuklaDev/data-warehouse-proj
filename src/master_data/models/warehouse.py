"""
Warehouse model.
"""

from dataclasses import asdict, dataclass


@dataclass(slots=True)
class Warehouse:
    """
    Warehouse domain model.
    """

    warehouse_id: str
    warehouse_name: str
    city: str
    state: str
    country: str
    capacity: int
    is_active: bool

    def to_dict(self) -> dict:
        return asdict(self)
    