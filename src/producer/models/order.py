from dataclasses import dataclass


@dataclass
class Order:

    order_id: str

    customer_id: str

    product_id: str

    warehouse_id: str

    supplier_id: str

    quantity: int

    unit_price: float

    total_amount: float

    payment_method: str

    channel: str

    status: str

    event_timestamp: str