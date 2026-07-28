from src.master_data.generators.customer_generator import CustomerGenerator


def test_customer_generator():

    generator = CustomerGenerator()

    dataframe = generator.generate()

    assert len(dataframe) > 0

    assert "customer_id" in dataframe.columns

    assert "email" in dataframe.columns

    assert dataframe["customer_id"].is_unique