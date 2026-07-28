"""
Category Service
"""

from src.master_data.services.base_service import BaseService


class CategoryService(BaseService):

    OUTPUT_DIR = "data/master/categories"

    FILE_NAME = "categories.csv"