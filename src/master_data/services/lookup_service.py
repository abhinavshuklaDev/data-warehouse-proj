"""
Lookup Service

Provides helper methods for retrieving related
master data used by generators.
"""

from random import choice

from src.master_data.reference_data.brands import BRANDS
from src.master_data.reference_data.product_catalog import PRODUCT_CATALOG
from src.master_data.reference_data.suppliers import SUPPLIERS
from src.master_data.reference_data.warehouses import WAREHOUSES


class LookupService:
    """
    Helper methods for master data lookups.
    """

    @staticmethod
    def get_brands(category_id: str) -> list[dict]:
        """
        Return all brands for a category.
        """
        return [
            brand
            for brand in BRANDS
            if brand["category_id"] == category_id
        ]

    @staticmethod
    def get_products(
        category_id: str,
        brand_name: str,
    ) -> list[str]:
        """
        Return all products for a brand.
        """
        return PRODUCT_CATALOG[category_id][brand_name]

    @staticmethod
    def get_supplier(supplier_id: str) -> dict:
        """
        Return supplier by supplier_id.
        """

        for supplier in SUPPLIERS:
            if supplier["supplier_id"] == supplier_id:
                return supplier

        raise ValueError(
            f"Supplier '{supplier_id}' not found."
        )

    @staticmethod
    def get_random_warehouse() -> dict:
        """
        Return a random warehouse.
        """
        return choice(WAREHOUSES)