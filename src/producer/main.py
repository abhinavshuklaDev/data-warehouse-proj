"""
Producer Application Entry Point.
"""

from src.producer.engine.producer_engine import (
    ProducerEngine,
)
from src.producer.repository.master_data_repository import (
    MasterDataRepository,
)
from src.producer.services.event_factory import (
    EventFactory,
)
from src.producer.services.session_simulator import (
    SessionSimulator,
)


def main():

    repository = MasterDataRepository()

    factory = EventFactory(
        repository
    )

    simulator = SessionSimulator(
        factory
    )

    engine = ProducerEngine(
        simulator
    )

    engine.run()


if __name__ == "__main__":
    main()