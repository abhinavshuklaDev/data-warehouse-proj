"""
Master Data Generation Entry Point
"""

from src.common.logger import logger
from src.master_data.generators.category_generator import CategoryGenerator
from src.master_data.generators.customer_generator import CustomerGenerator
from src.master_data.generators.brand_generator import BrandGenerator
from src.master_data.generators.supplier_generator import SupplierGenerator

def main():

    logger.info("Starting Master Data Generation")

    logger.info("Generating Categories...")
    CategoryGenerator().generate()

    logger.info("Generating Brands...")
    BrandGenerator().generate()

    logger.info("Generating Suppliers...")
    SupplierGenerator().generate()

    logger.info("Generating Customers...")
    CustomerGenerator().generate()

    logger.success("Master Data Generation Completed Successfully")


if __name__ == "__main__":
    main()