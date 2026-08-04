"""
Event Factory
"""

from random import random

from src.producer.events.product_view_event import ProductViewEvent
from src.producer.events.cart_event import CartEvent
from src.producer.events.order_event import OrderEvent
from src.producer.events.payment_event import PaymentEvent
from src.producer.events.return_event import ReturnEvent
from src.producer.services.context_service import ContextService


class EventFactory:
    """
    Generates a realistic customer journey.
    """

    def __init__(self, context_service: ContextService):
        self.context_service = context_service

    def generate(self) -> list[dict]:
        """
        Generate a complete customer journey.
        """

        context = self.context_service.create()

        events = []

        # Product View (always happens)
        product_view = ProductViewEvent.create(context)
        events.append(product_view.to_dict())

        # Add To Cart (70%)
        if random() <= 0.70:

            cart = CartEvent.create(context)
            events.append(cart.to_dict())

            # Order (60% of carts)
            if random() <= 0.60:

                order = OrderEvent.create(context)
                events.append(order.to_dict())

                # Payment
                payment = PaymentEvent.create(context)

                events.append(payment.to_dict())

                # Return (2%)
                if (
                    payment.status == "SUCCESS"
                    and random() <= 0.02
                ):
                    returned = ReturnEvent.create(
                        context,
                        order.order_id,
                    )

                    events.append(
                        returned.to_dict()
                    )

        return events