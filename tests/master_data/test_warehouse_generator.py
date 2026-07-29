from src.master_data.generators.warehouse_generator import WarehouseGenerator


def test_warehouse_generator():

    dataframe = WarehouseGenerator().generate()

    assert len(dataframe) == 5

    assert dataframe["warehouse_id"].is_unique

    assert "capacity" in dataframe.columns
    