import os
import json

from typing import List, Dict
from dataclasses import dataclass, field


"""
# Default
[$3.99] 01 Yerba Mate - Tropical Uprising

[01 Can] @3.99 Yerba Mate - Tropical Uprising

# More Details
category, quantity, unit,  extra details

[$3.99] 01 Yerba Mate - Tropical Uprising 
| Drink
| 1 can
| 90mg Caffeine 


# Database
cheapest price and store, all prices and stores, average product price over time, estimated product price now and future

"""


@dataclass
class GroceryItem:
    name: str
    specifics: str  # Flavor or specific brand
    price: float
    quantity: int
    unit: str
    category: str
    details: str

    def __str__(self) -> str:
        txt = f"[${self.price}] {self.quantity:02} {self.name.title()} - {self.specifics}"
        return txt

    def txt(self) -> str:
        txt = f"""
[${self.price}] {self.name.title()} - {self.specifics} | {self.category} | {self.quantity} {self.unit} | {self.details} |
"""
        return txt
    
    def edit_attr(self, attr: str, new_value: any):
        match attr:
            case "name":
                self.name = new_value
            case "price":
                self.price = new_value
            case "specifics":
                self.specifics = new_value
            case "quantity":
                self.quantity = new_value
            case "unit":
                self.unit = new_value
            case "category":
                self.category = new_value
            case "details":
                self.details = new_value
            case _:
                print("Attr not found!")
        return
    
    def export(self):
        return {
        "name": self.name,
        "price": self.price,
        "specifics": self.specifics,  # Flavor or specific brand
        "quantity": self.quantity,
        "unit": self.unit,
        "category": self.category,
        "details": self.details
    }


class GroceryList:
    def __init__(self, starting_data: List[GroceryItem]=None):
        if starting_data is None:
            starting_data = []

        self.length = len(starting_data)
        self.data = starting_data

    def __str__(self) -> str:
        return f"{self.length}"

    def get_data(self) -> List[GroceryItem]:
        return self.data

    def export(self):
        return [item.export() for item in self.data]


def main():
    sample_item = {
        "name": "Yerba Mate",
        "price": 3.99,
        "specifics": "Tropical Uprising",  # Flavor or specific brand
        "quantity": 1,
        "unit": "can",
        "category": "Drink",
        "details": "90mg Caffeine",
    }

    new_grocery_item = GroceryItem(**sample_item)
    print(new_grocery_item)
    print(new_grocery_item.export())


    # Grocery List
    shopping_list = GroceryList([new_grocery_item, new_grocery_item, new_grocery_item, new_grocery_item])
    print(shopping_list)
    print(shopping_list.data)
    print(shopping_list.export())

    for item in shopping_list.data:
        print(item)


if __name__ == '__main__':
    main()
