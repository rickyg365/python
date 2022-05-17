import os
import json

import datetime
from typing import List, Dict

from dataclasses import dataclass, field


def save_grocery_data(input_data, filepath: str):
    with open(filepath, 'w') as out_file:
        json.dump(input_data, out_file, indent=4)
    return

def load_grocery_data(filepath: str):
    with open(filepath, 'r') as in_file:
        new_data = json.load(in_file)
    return new_data


def input_raw_grocery_data():
    name = input("Name: ")
    price = input("Price: ")
    quantity = input("Quantity: ")
    unit = input("Unit: ")
    expiration_date = input("Expiration Date: ")
    purchase_date = datetime.datetime.now().strftime("%D")  # Todays date

    return {
        "name": name,
        "price": price,
        "quantity": quantity,
        "unit": unit,
        "expiration_date": expiration_date,
        "purchase_date": purchase_date
    }


@dataclass
class GroceryItem:
    name: str
    price: float = 0.00
    quantity: int = 1
    unit: str = "" # Possible enum?
    expiration_date: str = ""  # Datetime?
    purchase_date: str = ""  # Datetime?

    def __str__(self) -> str:
        txt = f"[${self.price}]: {self.name} - {self.quantity} {self.unit}"
        return txt

    def full_txt(self) -> str:
        return

    def export(self) -> Dict[str, any]:
        return {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "unit": self.unit,
            "expiration_date": self.expiration_date,
            "purchase_date": self.purchase_date,
        }


class ItemList:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.items = []
        self.length = 0

    def __str__(self) -> str:
        txt = ""
        return txt
    
    def load_data(self):
        raw_data = load_grocery_data(self.filepath)

        self.items = [GroceryItem(**item) for item in raw_data]

    def save_data(self):
        export_data = self.export()
        save_grocery_data(export_data, self.filepath)

    def export(self):
        # for item in self.items:
        #     export_list.append(item.export())
        # return export_list
        return [item.export() for item in self.items]
        


def main():
    return

if __name__ == '__main__':
    main()
