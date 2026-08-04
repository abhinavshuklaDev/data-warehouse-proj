"""
Publisher Interface
"""

from abc import ABC, abstractmethod


class Publisher(ABC):
    """
    Abstract publisher.
    """

    @abstractmethod
    def publish(self, event: dict) -> None:
        """
        Publish an event.
        """
        raise NotImplementedError