from src.producer.schemas.base_schema import (
    BaseEventSchema,
)


class ProductViewSchema(BaseEventSchema):

    view_duration_seconds: int

    device_type: str

    referrer: str

    page_number: int

    search_keyword: str