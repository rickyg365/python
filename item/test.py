import os
import json
import pytest

from item import Item, QuantizedItem, GroceryItem


def test_inspect_item():
    # Sample Recipe Data
    test_item = {
        "name": "Milk",
        "price": 3.99
    }
    # Create Recipe Object
    new_item = Item(**test_item)

    print(new_item)
    print(json.dumps(new_item.export(), indent=4))


def test_inspect_grocery_item():
    # Sample grocery Data
    test_grocery_item = {
        "name": "Milk",
        "price": 3.99,
        "amount": 1,
        "unit": "ct",
        "purchase_date": "02-28-22",
        "expiration_date": "03-12-22"
    }
    # Create Recipe Object
    test_grocery_item = GroceryItem(**test_grocery_item)

    print(test_grocery_item)
    print(json.dumps(test_grocery_item.export(), indent=4))
    

""" For each Class """
# Test Name
# Test Price
# Test Amount
# Test Unit
# Test Quantity setter/getter
# Test purchase date
# Test Expiration date
# Test Export

if __name__ == '__main__':
    test_inspect_item()
    test_inspect_grocery_item()
