from src.producer.events.inventory_event import (
    InventoryEvent,
)
from src.producer.events.order_event import (
    OrderEvent,
)
from src.producer.repository.master_data_repository import (
    MasterDataRepository,
)
from src.producer.services.context_service import (
    ContextService,
)


def test_inventory_event():

    repository = MasterDataRepository()

    context = ContextService(
        repository
    ).create()

    order = OrderEvent.create(
        context,
        repository,
    )

    inventory = InventoryEvent.create(
        context,
        order,
        repository,
    )

    assert inventory.event_type == "INVENTORY"

    assert inventory.order_id == order.order_id

    assert inventory.quantity_reserved == order.quantity

    assert inventory.remaining_stock >= 0