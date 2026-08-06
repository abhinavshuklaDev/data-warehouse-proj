from src.producer.events.product_view_event import (
    ProductViewEvent,
)
from src.producer.repository.master_data_repository import (
    MasterDataRepository,
)
from src.producer.services.context_service import (
    ContextService,
)


def test_product_view_creation():

    repository = MasterDataRepository()

    context = ContextService(
        repository
    ).create()

    event = ProductViewEvent.create(
        context
    )

    assert event.event_type == "PRODUCT_VIEW"

    assert event.customer_id

    assert event.product_id

    assert event.session_id

    assert event.view_duration_seconds > 0