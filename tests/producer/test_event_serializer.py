from src.producer.events.product_view_event import (
    ProductViewEvent,
)
from src.producer.repository.master_data_repository import (
    MasterDataRepository,
)
from src.producer.serializers.event_serializer import (
    EventSerializer,
)
from src.producer.services.context_service import (
    ContextService,
)


def test_event_serializer():

    repository = MasterDataRepository()

    context = ContextService(
        repository
    ).create()

    event = ProductViewEvent.create(
        context
    )

    event_dict = EventSerializer.to_dict(
        event
    )

    event_json = EventSerializer.to_json(
        event
    )

    assert isinstance(
        event_dict,
        dict,
    )

    assert isinstance(
        event_json,
        str,
    )

    assert "PRODUCT_VIEW" in event_json