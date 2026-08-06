"""
Session Simulator
"""

from random import random, randint

from src.producer.rules.session_rules import (
    ADD_TO_CART_PROBABILITY,
    PRODUCT_VIEWS_MAX,
    PRODUCT_VIEWS_MIN,
)
from src.producer.services.event_factory import EventFactory


class SessionSimulator:

    def __init__(
        self,
        factory: EventFactory,
    ):

        self.factory = factory

    def generate(self):

        context = self.factory.new_session()

        events = []

        number_of_views = randint(
            PRODUCT_VIEWS_MIN,
            PRODUCT_VIEWS_MAX,
        )

        for _ in range(number_of_views):

            events.append(
                self.factory.product_view(
                    context
                )
            )

        if random() < ADD_TO_CART_PROBABILITY:

            events.append(
                self.factory.cart(
                    context
                )
            )

        return events