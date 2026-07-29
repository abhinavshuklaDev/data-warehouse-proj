"""
Master Data Generation Entry Point
"""

from src.common.logger import logger
from src.master_data.generators.category_generator import CategoryGenerator
from src.master_data.generators.customer_generator import CustomerGenerator
from src.master_data.generators.brand_generator import BrandGenerator
from src.master_data.generators.supplier_generator import SupplierGenerator
from src.master_data.generators.warehouse_generator import WarehouseGenerator
from src.master_data.generators.product_generator import ProductGenerator

def main():

    logger.info("Starting Master Data Generation")

    logger.info("Generating Categories...")
    CategoryGenerator().generate()

    logger.info("Generating Brands...")
    BrandGenerator().generate()

    logger.info("Generating Suppliers...")
    SupplierGenerator().generate()

    logger.info("Generating Warehouses...")
    WarehouseGenerator().generate()

    logger.info("Generating Customers...")
    CustomerGenerator().generate()

    logger.info("Generating Products...")
    ProductGenerator().generate()

    logger.success("Master Data Generation Completed Successfully")


if __name__ == "__main__":
    main()