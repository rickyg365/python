# Models
from models.item import Item
from models.store import Store
from models.transaction import Transaction

# Custom Utils
from utils.custom_json import load_json

"""
Tests

Todo: add test data path as a fixture
Todo: add test data path as a fixture
"""

def test_create_item():
    """
    id: int
    name:  str
    brand:  str
    flavor:  str
    """
    # Raw Data
    new_item_data = load_json("data/test/items.json")[0]

    # Model
    new_item = Item(**new_item_data)

    assert type(new_item) == Item
    

def test_create_store():
    """
    id: int
    name: str
    distance: str
    """
    # Raw Data
    new_store_data = load_json("data/test/stores.json")[0]
    
    # Model
    new_store = Store(**new_store_data)

    assert type(new_store) == Store
    

def test_create_transaction():
    """
    id: int
    item_id: int
    store_id: int
    quantity: int 
    unit: int
    unit_price: float
    total_price: float
    """
    # Raw Data
    new_transaction_data = load_json("data/test/transactions.json")[0]
    
    # Model
    new_transaction = Transaction(**new_transaction_data)

    assert type(new_transaction) == Transaction
    

def run_test():
    print("Starting Test Run!")
    test_create_item()
    test_create_store()
    test_create_transaction()
    print("Test Successful!")
  

if __name__ == '__main__':
    run_test()