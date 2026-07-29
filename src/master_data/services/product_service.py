"""
Product Service
"""

from src.master_data.services.base_service import BaseService


class ProductService(BaseService):
    """
    Service for product master data.
    """

    OUTPUT_DIR = "data/master/products"

    FILE_NAME = "products.csv"