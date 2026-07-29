"""
Brand model.
"""

from dataclasses import asdict, dataclass


@dataclass(slots=True)
class Brand:

    brand_id: str
    brand_name: str
    category_id: str
    supplier_id: str
    is_active: bool

    def to_dict(self):
        return asdict(self)