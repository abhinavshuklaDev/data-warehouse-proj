"""
Customer Generator

Responsibilities:
- Generate realistic customer objects
"""

from random import choices
from uuid import uuid4

from faker import Faker

from src.common.logger import logger
from src.config.config import config
from src.master_data.models.customer import Customer
from src.master_data.services.customer_service import CustomerService
from src.master_data.reference_data.loyalty import (
    LOYALTY_TIERS,
    LOYALTY_WEIGHTS,
)

class CustomerGenerator:

    def __init__(self) -> None:
        self.fake = Faker("en_AU")

    def generate(self):
        """
        Generate customer master data.

        Returns:
            pandas.DataFrame
        """

        logger.info("Generating customer master data...")

        customers: list[Customer] = []

        for _ in range(config.config.master_data.customers):

            gender = self.fake.random_element(
                elements=("Male", "Female")
            )

            customer = Customer(
                customer_id=f"C{uuid4().hex[:8].upper()}",
                first_name=self.fake.first_name_male()
                if gender == "Male"
                else self.fake.first_name_female(),
                last_name=self.fake.last_name(),
                email=self.fake.unique.email(),
                phone_number=self.fake.phone_number(),
                gender=gender,
                date_of_birth=str(
                    self.fake.date_of_birth(
                        minimum_age=18,
                        maximum_age=80,
                    )
                ),
                city=self.fake.city(),
                state=self.fake.state(),
                country="Australia",
                postal_code=self.fake.postcode(),
                loyalty_tier=choices(
                    LOYALTY_TIERS,
                    weights=LOYALTY_WEIGHTS,
                    k=1,
                )[0],
                registration_date=str(
                    self.fake.date_between("-5y", "today")
                ),
                is_active=self.fake.boolean(
                    chance_of_getting_true=90
                ),
            )

            customers.append(customer)

        dataframe = CustomerService.to_dataframe(customers)

        CustomerService.save(dataframe)

        logger.success(
            f"{len(dataframe)} customers generated successfully."
        )

        return dataframe