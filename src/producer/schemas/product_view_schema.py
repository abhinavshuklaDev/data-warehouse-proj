from src.producer.schemas.base_schema import (
    BaseEventSchema,
)


class ProductViewSchema(BaseEventSchema):
    """
    Product view schema.
    """

    view_duration_seconds: int