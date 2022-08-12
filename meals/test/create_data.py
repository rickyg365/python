# Models
from models.item import Item
from models.store import Store
from models.transaction import Transaction

# Custom Utils
from utils.custom_json import save_json


def create_item(test_path: str = "data/test"):
    # Item
    new_item_data = {
        "id": 1,
        "name": "Yerba Mate",
        "brand": "Yerba Mate",
        "flavor": "Tropical Uprising"
    }

    new_item = Item(**new_item_data)
    save_json([new_item.export()], f"{test_path}/items.json")
    return

def create_store(test_path: str = "data/test"):
    # Store
    new_store_data = {
        "id": 1,
        "name": "Bargain Plus",
        "distance": "2 miles"
    }

    new_store = Store(**new_store_data)
    save_json([new_store.export()], f"{test_path}/stores.json")
    return

def create_transaction(test_path: str = "data/test"):
    # Transaction
    new_transaction_data = {
        "id": 1,
        "item_id": 1,
        "store_id": 1,
        "quantity": 2,
        "unit": "Each",
        "unit_price": 1.00,
        "total_price": 2.00
    }

    new_transaction = Transaction(**new_transaction_data)
    save_json([new_transaction.export()], f"{test_path}/transactions.json")
    return


def create_test_data():
    test_path = "data/test"

    # Item
    create_item(test_path)


    # Store
    create_store(test_path)

    # Transaction
    create_transaction(test_path)
    return
