"""
Brand Service
"""

from src.master_data.services.base_service import BaseService


class BrandService(BaseService):
    """
    Service for brand master data.
    """

    OUTPUT_DIR = "data/master/brands"

    FILE_NAME = "brands.csv"