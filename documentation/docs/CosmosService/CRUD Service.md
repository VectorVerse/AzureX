# CRUD Service

- Base Code to get started with CRUD Service:

```
from azurex.cosmos import CosmosCRUDService

cosmos_service = CosmosCRUDService(
    "TestDB", ["/id", "/partition_key1", "/partition_key2"], "TestContainer"
)
```

## Create an Item:

```
item1 = cosmos_service.create_item(
        item={
            "id": "1",
            "partition_key1": "value1",
            "partition_key2": "value2",
            "TestKey": "TestValue",
        }
    )
```

---

## Query Items

```
query = "SELECT * FROM C"
items = cosmos_service.query_items(query=query)
# Returns: List of items matching the query
```

---

## Update an Item

```
updated_item = {
    "id": "1",
    "partition_key1": "value1",
    "partition_key2": "value2",
    "TestKey": "NewTestValue",
    "TempKey": "TempValue",
}
item = cosmos_service.update_item(item_id="1", updated_item=updated_item)
# Returns: The updated item as a dictionary
```

---

## Delete an Item

```
result = cosmos_service.delete_item(item_id="1")
# Returns: "Item Deleted Successfully" or "Item not found"
```

---

!!! tip
    - Delete an Item with Partition Keys

    ```
    result = cosmos_service.create_item(
        item={
            "id": "2",
            "partition_key1": "value1",
            "partition_key2": "value2",
            "TestKey": "TestValue",
        }
    )
    # result: "Item Created Successfully" or "Item already exists"

    delete_result = cosmos_service.delete_item(item_id="2")
    # delete_result: "Item Deleted Successfully" or "Item not found"
    ```

    !!! Note
        - Providing the partition key values directly when deleting an item significantly improves performance. If you omit them, the service must first perform an additional lookup to determine the partition keys, which can slow down the operation. Supplying the partition keys up front ensures a faster and more efficient deletion process.

---

## String Representation

```
print(str(cosmos_service))
# Output:
# CosmosCRUDService(database_name=TestDB, container_name=TestContainer,partition_key_path=['/id', '/partition_key1', '/partition_key2'])
```

---

## Notes

- Ensure your Cosmos DB instance and container are properly configured.
- Partition keys must match the structure defined during service initialization.
- All methods return informative messages or data structures for easy integration and error handling.

---
