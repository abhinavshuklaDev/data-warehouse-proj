from src.producer.schemas.base_schema import (
    BaseEventSchema,
)


class CartSchema(
    BaseEventSchema
):

    cart_id: str

    quantity: int

    unit_price: float

    cart_total: float