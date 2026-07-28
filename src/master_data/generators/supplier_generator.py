"""
Supplier Generator
"""

from src.common.logger import logger
from src.master_data.models.supplier import Supplier
from src.master_data.reference_data.suppliers import SUPPLIERS
from src.master_data.services.supplier_service import SupplierService


class SupplierGenerator:
    """
    Generates supplier master data.
    """

    def generate(self):
        logger.info("Generating supplier master data...")

        suppliers = [
            Supplier(
                supplier_id=item["supplier_id"],
                supplier_name=item["supplier_name"],
                country=item["country"],
                contact_email=item["contact_email"],
                is_active=True,
            )
            for item in SUPPLIERS
        ]

        dataframe = SupplierService.to_dataframe(suppliers)

        SupplierService.save(dataframe)

        logger.success(
            f"{len(dataframe)} suppliers generated successfully."
        )

        return dataframe