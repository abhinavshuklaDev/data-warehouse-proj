"""
Category model.

Represents a product category.
"""

from dataclasses import asdict, dataclass


@dataclass(slots=True)
class Category:
    """
    Category domain model.
    """

    category_id: str
    category_name: str
    description: str
    is_active: bool

    def to_dict(self) -> dict:
        """
        Convert the Category object into a dictionary.
        """
        return asdict(self)