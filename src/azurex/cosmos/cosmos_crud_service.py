"""
The Service class for CRUD operations on Azure Cosmos DB.
"""

import os

from azure.cosmos import CosmosClient, PartitionKey, exceptions
from typing import List, Dict, Union
from dotenv import load_dotenv

load_dotenv()


class CosmosCRUDService:
    """The class CosmosCRUDService is a wrapper for Azure Cosmos DB which provides CRUD operations."""

    def __init__(
        self, database_name: str, partition_key: Union[str, List], container_name: str
    ):
        self.database_name = database_name
        self.partition_key_path = partition_key
        self.container_name = container_name
        self.client, self.db, self.container = self._get_database_clients()
        if isinstance(self.partition_key_path, str):
            self.partition_key = PartitionKey(path=self.partition_key_path, kind="Hash")
        elif isinstance(self.partition_key, list):
            self.partition_key = PartitionKey(
                path=self.partition_key_path, kind="MultiHash"
            )
        else:
            raise TypeError("partition_key_path must be str or list of str.")

    def _get_database_clients(self):
        """It is Private method to get the database clients."""
        try:
            client = CosmosClient.from_connection_string(
                conn_str=os.getenv("AZURE_COSMOS_CONNECTION_STRING")
            )
            database = client.create_database_if_not_exists(self.database_name)

            container = database.create_container_if_not_exists(
                self.container_name, partition_key=self.partition_key
            )
        except Exception as e:
            print(f"Error creating database or container: {e}")
            raise e
        return client, database, container

    def create_item(self, item: Dict) -> str:
        """Create an item in the container.
        ## Parameters:
            item (dict): The SQL-like query to execute.
        ## Returns:
            list: A list of items matching the query.
        """
        try:
            self.container.create_item(body=item)
        except Exception as e:
            print(f"Error creating item: {e}")
            raise e
        return "Item Created Successfully"

    def query_items(self, query: str) -> List:
        """Query items in the container using SQL-like syntax.
        ## Parameters:
            query (str): The SQL-like query to execute.
        ## Returns:
            list: A list of items matching the query.
        """
        try:
            items = list(
                self.container.query_items(
                    query=query, enable_cross_partition_query=True
                )
            )
        except Exception as e:
            print(f"Error querying items: {e}")
            return []
        return items

    def update_item(self, item_id: str, updated_item: Dict) -> Dict:
        """Update an item in the container.
        ## Parameters:
            item_id (str): The ID of the item to update.
            updated_item (dict): The updated item data.
        ## Returns:
            str: A message indicating the result of the operation.
        """
        try:
            item = self.container.read_item(
                item=item_id, partition_key=self.partition_key_path
            )
            for key, value in updated_item.items():
                item[key] = value
            self.container.replace_item(body=updated_item)
        except Exception as e:
            print(f"Error updating item: {e}")
            raise e
        return item

    def delete_item(self, item_id: str) -> str:
        """Delete an item in the container.
        ## Parameters:
            item_id (str): The ID of the item to delete.
        ## Returns:
            str: A message indicating the result of the operation.
        """
        try:
            self.container.delete_item(
                item=item_id, partition_key=self.partition_key_path
            )
        except exceptions.CosmosHttpResponseError as e:
            print(f"Error deleting item: {e}")
            raise e
        return "Item Deleted Successfully"

    def __str__(self):
        return "CosmosCRUDService(database_name={}, container_name={})".format(
            self.database_name, self.container_name
        )
