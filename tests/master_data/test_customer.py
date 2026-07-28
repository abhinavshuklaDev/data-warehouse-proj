from src.master_data.models.customer import Customer


def test_customer_creation():

    customer = Customer(
        customer_id="C000001",
        first_name="Abhinav",
        last_name="Shukla",
        email="abhinav@example.com",
        phone_number="9876543210",
        gender="Male",
        date_of_birth="2001-11-18",
        city="Ahmedabad",
        state="Gujarat",
        country="India",
        postal_code="380001",
        loyalty_tier="Gold",
        registration_date="2026-01-01",
        is_active=True,
    )

    assert customer.customer_id == "C000001"

    assert customer.first_name == "Abhinav"

    assert customer.loyalty_tier == "Gold"

    assert customer.is_active is True