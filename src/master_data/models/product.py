"""
Product model.
"""

from dataclasses import asdict, dataclass


@dataclass(slots=True)
class Product:
    """
    Product domain model.
    """

    product_id: str
    product_name: str
    category_id: str
    brand_id: str
    supplier_id: str
    warehouse_id: str
    sku: str
    unit_price: float
    cost_price: float
    stock_quantity: int
    reorder_level: int
    weight_kg: float
    is_active: bool

    def to_dict(self) -> dict:
        return asdict(self)