from src.producer.events.order_event import (
    OrderEvent,
)
from src.producer.events.return_event import (
    ReturnEvent,
)
from src.producer.repository.master_data_repository import (
    MasterDataRepository,
)
from src.producer.services.context_service import (
    ContextService,
)


def test_return_event():

    repository = MasterDataRepository()

    context = ContextService(
        repository
    ).create()

    order = OrderEvent.create(
        context,
        repository,
    )

    event = ReturnEvent.create(
        context,
        order,
    )

    assert event.event_type == "RETURN"

    assert event.order_id == order.order_id

    assert event.refund_amount == order.total_amount