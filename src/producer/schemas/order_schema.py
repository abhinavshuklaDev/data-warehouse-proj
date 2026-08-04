from src.producer.schemas.base_schema import (
    BaseEventSchema,
)


class OrderSchema(BaseEventSchema):

    order_id: str

    quantity: int

    unit_price: float

    total_amount: float