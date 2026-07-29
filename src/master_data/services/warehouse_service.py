"""
Warehouse Service
"""

from src.master_data.services.base_service import BaseService


class WarehouseService(BaseService):
    """
    Service for warehouse master data.
    """

    OUTPUT_DIR = "data/master/warehouses"

    FILE_NAME = "warehouses.csv"