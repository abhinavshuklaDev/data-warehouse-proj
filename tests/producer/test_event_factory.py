from src.producer.repository.master_data_repository import (
    MasterDataRepository,
)
from src.producer.services.event_factory import (
    EventFactory,
)


def test_event_factory():

    repository = MasterDataRepository()

    factory = EventFactory(
        repository
    )

    context = factory.new_session()

    view = factory.product_view(
        context
    )

    cart = factory.cart(
        context
    )

    assert (
        view.customer_id
        == cart.customer_id
    )

    assert (
        view.product_id
        == cart.product_id
    )

    assert (
        view.session_id
        == cart.session_id
    )