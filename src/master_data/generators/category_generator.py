"""
Category Generator
"""

from src.common.logger import logger
from src.master_data.models.category import Category
from src.master_data.reference_data.categories import CATEGORIES
from src.master_data.services.category_service import CategoryService


class CategoryGenerator:

    def generate(self):

        logger.info("Generating categories")

        categories = [
            Category(
                category_id=item["category_id"],
                category_name=item["category_name"],
                description=item["description"],
                is_active=True,
            )
            for item in CATEGORIES
        ]

        dataframe = CategoryService.to_dataframe(categories)

        CategoryService.save(dataframe)

        logger.success(
            f"{len(dataframe)} categories generated."
        )

        return dataframe