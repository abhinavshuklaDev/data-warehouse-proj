"""
Event Factory

Creates business events.
"""

from src.producer.events.cart_event import CartEvent
from src.producer.events.inventory_event import InventoryEvent
from src.producer.events.product_view_event import ProductViewEvent
from src.producer.events.return_event import ReturnEvent
from src.producer.repository.master_data_repository import MasterDataRepository
from src.producer.services.context_service import ContextService
from src.producer.events.order_event import OrderEvent
from src.producer.events.payment_event import PaymentEvent

class EventFactory:

    def __init__(
        self,
        repository: MasterDataRepository,
    ) -> None:

        self.repository = repository

        self.context_service = ContextService(
            repository
        )

    def new_session(self):
        return self.context_service.create()


    def product_view(self,context):
        return ProductViewEvent.create(
            context
        )


    def cart(self,context):
        product = self.repository.get_product(
            context.product_id
        )
        return CartEvent.create(
            context,
            product,
        )

    def order(self,context):
        return OrderEvent.create(
            context,
            self.repository,
        )

    def payment(self,context,order):
        return PaymentEvent.create(
            context,
            order,
        )
    
    def inventory(self,context,order):
        return InventoryEvent.create(
            context,
            order,
            self.repository,
        )

    def return_event(self,context,order):
        return ReturnEvent.create(
            context,
            order,
        )