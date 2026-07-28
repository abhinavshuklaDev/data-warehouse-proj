from src.master_data.generators.category_generator import CategoryGenerator


def test_category_generator():

    dataframe = CategoryGenerator().generate()

    assert len(dataframe) == 8

    assert "category_id" in dataframe.columns

    assert dataframe["category_id"].is_unique