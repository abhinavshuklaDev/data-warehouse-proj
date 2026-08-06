import random

import pandas as pd

from src.common.logger import logger


class MasterDataRepository:
    """
    Repository responsible for loading master data once
    and serving it from memory.
    """

    def __init__(self) -> None:

        self.customers = self._load(
            "data/master/customers/customers.csv"
        )

        self.products = self._load(
            "data/master/products/products.csv"
        )

        self.categories = self._load(
            "data/master/categories/categories.csv"
        )

        self.brands = self._load(
            "data/master/brands/brands.csv"
        )

        self.suppliers = self._load(
            "data/master/suppliers/suppliers.csv"
        )

        self.warehouses = self._load(
            "data/master/warehouses/warehouses.csv"
        )

        logger.success("Master data loaded successfully.")

    def _load(self, path: str) -> pd.DataFrame:
        """
        Load CSV into memory.
        """
        logger.info(f"Loading {path}")

        return pd.read_csv(path)

    def get_random_customer(self) -> dict:
        return self.customers.sample(1).iloc[0].to_dict()

    def get_random_product(self) -> dict:
        return self.products.sample(1).iloc[0].to_dict()

    def get_random_supplier(self) -> dict:
        return self.suppliers.sample(1).iloc[0].to_dict()

    def get_random_brand(self) -> dict:
        return self.brands.sample(1).iloc[0].to_dict()

    def get_random_category(self) -> dict:
        return self.categories.sample(1).iloc[0].to_dict()

    def get_random_warehouse(self) -> dict:
        return self.warehouses.sample(1).iloc[0].to_dict()

    def get_customer(self, customer_id: str) -> dict | None:

        customer = self.customers[
            self.customers["customer_id"] == customer_id
        ]

        if customer.empty:
            return None

        return customer.iloc[0].to_dict()

    def get_product(self, product_id: str) -> dict | None:

        product = self.products[
            self.products["product_id"] == product_id
        ]

        if product.empty:
            return None

        return product.iloc[0].to_dict()