"""
Event Factory

Creates business events.
"""

from src.producer.events.cart_event import CartEvent
from src.producer.events.product_view_event import (
    ProductViewEvent,
)
from src.producer.repository.master_data_repository import (
    MasterDataRepository,
)
from src.producer.services.context_service import (
    ContextService,
)


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