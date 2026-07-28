"""
Customer Service
"""

from src.master_data.services.base_service import BaseService


class CustomerService(BaseService):

    OUTPUT_DIR = "data/master/customers"

    FILE_NAME = "customers.csv"