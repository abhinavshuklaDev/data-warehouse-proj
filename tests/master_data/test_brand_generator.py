from src.master_data.generators.brand_generator import BrandGenerator


def test_brand_generator():

    dataframe = BrandGenerator().generate()

    assert len(dataframe) == 19

    assert dataframe["brand_id"].is_unique

    assert "category_id" in dataframe.columns