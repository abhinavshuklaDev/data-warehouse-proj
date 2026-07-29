"""
Warehouse Generator
"""

from src.common.logger import logger
from src.master_data.models.warehouse import Warehouse
from src.master_data.reference_data.warehouses import WAREHOUSES
from src.master_data.services.warehouse_service import WarehouseService


class WarehouseGenerator:
    """
    Generates warehouse master data.
    """

    def generate(self):
        logger.info("Generating warehouse master data...")

        warehouses = [
            Warehouse(
                warehouse_id=item["warehouse_id"],
                warehouse_name=item["warehouse_name"],
                city=item["city"],
                state=item["state"],
                country=item["country"],
                capacity=item["capacity"],
                is_active=True,
            )
            for item in WAREHOUSES
        ]

        dataframe = WarehouseService.to_dataframe(warehouses)

        WarehouseService.save(dataframe)

        logger.success(
            f"{len(dataframe)} warehouses generated successfully."
        )

        return dataframe