"""
Supplier Service
"""

from src.master_data.services.base_service import BaseService


class SupplierService(BaseService):
    """
    Service for supplier master data.
    """

    OUTPUT_DIR = "data/master/suppliers"

    FILE_NAME = "suppliers.csv"