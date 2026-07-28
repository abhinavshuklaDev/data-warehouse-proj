from src.master_data.generators.supplier_generator import SupplierGenerator


def test_supplier_generator():

    dataframe = SupplierGenerator().generate()

    assert len(dataframe) == 8

    assert dataframe["supplier_id"].is_unique

    assert "supplier_name" in dataframe.columns