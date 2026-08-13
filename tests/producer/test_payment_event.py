from src.producer.events.order_event import OrderEvent
from src.producer.events.payment_event import PaymentEvent
from src.producer.repository.master_data_repository import (
    MasterDataRepository,
)
from src.producer.services.context_service import (
    ContextService,
)


def test_payment_event():

    repository = MasterDataRepository()

    context = ContextService(
        repository
    ).create()

    order = OrderEvent.create(
        context,
        repository,
    )

    payment = PaymentEvent.create(
        context,
        order,
    )

    assert payment.event_type == "PAYMENT"

    assert payment.order_id == order.order_id

    assert (
        payment.transaction_amount
        == order.total_amount
    )