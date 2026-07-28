"""
Brand Generator
"""

from src.common.logger import logger
from src.master_data.models.brand import Brand
from src.master_data.reference_data.brands import BRANDS
from src.master_data.services.brand_service import BrandService


class BrandGenerator:
    """
    Generates brand master data.
    """

    def generate(self):
        logger.info("Generating brand master data...")

        brands = [
            Brand(
                brand_id=item["brand_id"],
                brand_name=item["brand_name"],
                category_id=item["category_id"],
                is_active=True,
            )
            for item in BRANDS
        ]

        dataframe = BrandService.to_dataframe(brands)

        BrandService.save(dataframe)

        logger.success(f"{len(dataframe)} brands generated successfully.")

        return dataframe