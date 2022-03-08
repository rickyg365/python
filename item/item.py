import json

from abc import ABC, abstractmethod
from enum import Enum, auto

from typing import List, Dict
from dataclasses import dataclass

"""

Milk - 1 ct [$3.99]

class ItemBase(ABC):
    def __str__(self) -> str:
        pass
    
    @abstractmethod
    def export(self) -> Dict[str, any]:
        pass
"""

@dataclass 
class Item:
    name: str
    price: float

    def __str__(self) -> str:
        # Price and Quantity
        price = f"[${self.price:.2f}]"

        return f"{self.name.title():<18} {price:>8}"

    def export(self) -> Dict[str, any]:
        export_data = {
            "name": self.name,
            "price": self.price
        }
        return export_data


@dataclass(kw_only=True)
class QuantizedItem(Item):
    amount: int
    unit: str

    def __str__(self) -> str:
        # Can redefine here if we need more control but the property works fine for now
        quantity = f"{self.amount:>2} {self.unit}"
        return f"{super().__str__()} @ {quantity}"

    def export(self) -> Dict[str, any]:
        export_data = {
            **super().export(),
            "amount": self.amount,
            "unit": self.unit,
        }
        return export_data

    @property
    def quantity(self):
        return f"{self.amount} {self.unit}"

    @quantity.setter
    def quantity(self, new_quantity: str):        
        # Parse Value
        quantity_data = new_quantity.split(" ")
        
        if len(quantity_data) != 2:
            raise Exception
        
        new_amount, new_unit = int(quantity_data[0]), quantity_data[1]
        # Check Values
        if new_unit not in ['oz', 'ct']:
            raise Exception
        # Set Values
        self.unit = new_unit
        self.amount = new_amount
    

@dataclass(kw_only=True)
class GroceryItem(QuantizedItem):
    purchase_date: str
    expiration_date: str = ""
    amount: int = 0
    unit: str = 'ct'

    def __str__(self) -> str:
        data = f"{self.purchase_date} -> {self.expiration_date}"

        return f"{super().__str__()} | {data}"

    def export(self) -> Dict[str, any]:
        export_data = {
            **super().export(),
            "purchase_date": self.purchase_date,
            "expiration_date": self.expiration_date
        }
        return export_data


@dataclass(kw_only=True)
class ElectronicItem(QuantizedItem):
    purchase_date: str
    amount: int = 1
    unit: str = 'ct'

    def __str__(self) -> str:
        data = f"{self.purchase_date} -> {self.expiration_date}"

        return f"{super().__str__()} | {data}"

    def export(self) -> Dict[str, any]:
        export_data = {
            **super().export(),
            "purchase_date": self.purchase_date,
            "expiration_date": self.expiration_date
        }
        return export_data


def main():
    ...
    # # Sample Recipe Data
    # test_item = {
    #     "name": "Milk",
    #     "price": 3.99
    # }
    # # Create Recipe Object
    # new_item = Item(**test_item)

    # print(new_item)
    # print(json.dumps(new_item.export(), indent=4))


    # # Sample Recipe Data
    # test_shopping_item = {
    #     "name": "Milk",
    #     "price": 3.99,
    #     "amount": 1,
    #     "unit": "ct",
    #     "purchase_date": "02-28-22",
    #     "expiration_date": "03-12-22"
    # }
    # # Create Recipe Object
    # new_shopping_item = ShoppingItem(**test_shopping_item)

    # print(new_shopping_item)
    # print(json.dumps(new_shopping_item.export(), indent=4))
    # print(new_shopping_item.quantity)

if __name__ == '__main__':
    main()
