"""
Customer Journey Builder
"""

from random import random

from src.producer.rules.conversion_rules import (
    CHECKOUT_PROBABILITY,
)
from src.producer.rules.return_rules import (
    ReturnRules,
)


class CustomerJourney:

    def __init__(
        self,
        factory,
    ):

        self.factory = factory

    def generate(
        self,
        context,
        repository,
    ):

        events = []

        # Customer views product

        events.append(
            self.factory.product_view(
                context
            )
        )

        # Customer adds to cart

        events.append(
            self.factory.cart(
                context
            )
        )

        # Checkout

        if random() <= CHECKOUT_PROBABILITY:

            order = self.factory.order(
                context
            )

            events.append(
                order
            )

            payment = self.factory.payment(
                context,
                order,
            )

            events.append(
                payment
            )

            inventory = self.factory.inventory(
                context,
                order,
                repository,
            )

            events.append(
                inventory
            )

            if ReturnRules.should_return():

                events.append(

                    self.factory.return_event(
                        context,
                        order,
                    )

                )

        return events