from src.master_data.generators.product_generator import ProductGenerator


def test_product_generator():

    dataframe = ProductGenerator().generate()

    assert len(dataframe) > 0

    assert dataframe["product_id"].is_unique

    assert dataframe["sku"].is_unique

    assert dataframe["unit_price"].min() > 0