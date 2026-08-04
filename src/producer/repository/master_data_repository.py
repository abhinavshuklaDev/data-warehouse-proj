"""
Master Data Repository

Loads all generated master data into memory.
"""

from pathlib import Path

import pandas as pd


class MasterDataRepository:
    """
    Repository for master datasets.
    """

    def __init__(self):

        base = Path("data/master")

        self.customers = pd.read_csv(
            base / "customers/customers.csv"
        )

        self.products = pd.read_csv(
            base / "products/products.csv"
        )

        self.categories = pd.read_csv(
            base / "categories/categories.csv"
        )

        self.brands = pd.read_csv(
            base / "brands/brands.csv"
        )

        self.suppliers = pd.read_csv(
            base / "suppliers/suppliers.csv"
        )

        self.warehouses = pd.read_csv(
            base / "warehouses/warehouses.csv"
        )