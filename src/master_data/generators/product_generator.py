"""
Product Generator
"""

from random import choice, randint, uniform

from src.common.logger import logger
from src.master_data.models.product import Product
from src.master_data.reference_data.brands import BRANDS
from src.master_data.reference_data.product_attributes import (
    PRODUCT_ATTRIBUTES,
)
from src.master_data.reference_data.product_catalog import (
    PRODUCT_CATALOG,
)
from src.master_data.services.lookup_service import LookupService
from src.master_data.services.product_service import ProductService


class ProductGenerator:
    """
    Generates product master data.
    """

    def generate(self):

        logger.info("Generating product master data...")

        products: list[Product] = []

        product_number = 1

        for brand in BRANDS:

            category_id = brand["category_id"]

            brand_id = brand["brand_id"]

            supplier_id = brand["supplier_id"]

            brand_name = brand["brand_name"]

            warehouse = LookupService.get_random_warehouse()

            rules = PRODUCT_ATTRIBUTES[category_id]

            for product_name in PRODUCT_CATALOG[
                category_id
            ][brand_name]:

                selling_price = round(
                    uniform(*rules["selling_price"]),
                    2,
                )

                cost_ratio = uniform(
                    *rules["cost_ratio"]
                )

                cost_price = round(
                    selling_price * cost_ratio,
                    2,
                )

                weight = round(
                    uniform(*rules["weight"]),
                    2,
                )

                stock = randint(
                    *rules["stock"]
                )

                reorder_level = randint(
                    *rules["reorder_level"]
                )

                sku = (
                    brand_name[:3].upper()
                    + "-"
                    + str(product_number).zfill(5)
                )

                product = Product(
                    product_id=f"PROD{product_number:06d}",
                    product_name=product_name,
                    category_id=category_id,
                    brand_id=brand_id,
                    supplier_id=supplier_id,
                    warehouse_id=warehouse[
                        "warehouse_id"
                    ],
                    sku=sku,
                    unit_price=selling_price,
                    cost_price=cost_price,
                    stock_quantity=stock,
                    reorder_level=reorder_level,
                    weight_kg=weight,
                    is_active=True,
                )

                products.append(product)

                product_number += 1

        dataframe = ProductService.to_dataframe(
            products
        )

        ProductService.save(dataframe)

        logger.success(
            f"{len(dataframe)} products generated successfully."
        )

        return dataframe