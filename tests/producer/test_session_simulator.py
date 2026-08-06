from src.producer.repository.master_data_repository import (
    MasterDataRepository,
)
from src.producer.services.event_factory import (
    EventFactory,
)
from src.producer.services.session_simulator import (
    SessionSimulator,
)


def test_session_simulator():

    repository = MasterDataRepository()

    factory = EventFactory(
        repository
    )

    simulator = SessionSimulator(
        factory
    )

    events = simulator.generate()

    assert len(events) >= 1

    assert events[0].event_type == "PRODUCT_VIEW"

    session_id = events[0].session_id

    for event in events:

        assert event.session_id == session_id