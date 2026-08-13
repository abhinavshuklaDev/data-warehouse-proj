from src.producer.repository.master_data_repository import (
    MasterDataRepository,
)


def test_repository_lookup():

    repository = MasterDataRepository()

    customer = repository.customers.iloc[0]

    product = repository.products.iloc[0]

    supplier = repository.suppliers.iloc[0]

    warehouse = repository.warehouses.iloc[0]

    assert (
        repository.get_customer(
            customer["customer_id"]
        )["customer_id"]
        == customer["customer_id"]
    )

    assert (
        repository.get_product(
            product["product_id"]
        )["product_id"]
        == product["product_id"]
    )

    assert (
        repository.get_supplier(
            supplier["supplier_id"]
        )["supplier_id"]
        == supplier["supplier_id"]
    )

    assert (
        repository.get_warehouse(
            warehouse["warehouse_id"]
        )["warehouse_id"]
        == warehouse["warehouse_id"]
    )