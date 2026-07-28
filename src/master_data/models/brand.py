"""
Brand model.
"""

from dataclasses import asdict, dataclass


@dataclass(slots=True)
class Brand:
    """
    Brand domain model.
    """

    brand_id: str
    brand_name: str
    category_id: str
    is_active: bool

    def to_dict(self) -> dict:
        return asdict(self)