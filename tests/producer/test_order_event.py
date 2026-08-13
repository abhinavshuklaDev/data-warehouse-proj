from src.producer.repository.master_data_repository import (
    MasterDataRepository,
)
from src.producer.services.context_service import (
    ContextService,
)
from src.producer.events.order_event import (
    OrderEvent,
)


def test_order_event():

    repository = MasterDataRepository()

    context = ContextService(
        repository
    ).create()

    event = OrderEvent.create(
        context,
        repository,
    )

    assert event.event_type == "ORDER"

    assert event.quantity > 0

    assert event.total_amount > 0