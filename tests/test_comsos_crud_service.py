from azurex.cosmos import CosmosCRUDService

cosmos_service = CosmosCRUDService(
    "TestDB", ["/id", "/partition_key1", "/partition_key2"], "TestContainer"
)


def test_create_item():
    item1 = cosmos_service.create_item(
        item={
            "id": "1",
            "partition_key1": "value1",
            "partition_key2": "value2",
            "TestKey": "TestValue",
        }
    )

    assert item1 == "Item Created Successfully"


def test_str_representation():
    assert (
        str(cosmos_service)
        == "CosmosCRUDService(database_name=TestDB, container_name=TestContainer,partition_key_path=['/id', '/partition_key1', '/partition_key2'])"
    )
