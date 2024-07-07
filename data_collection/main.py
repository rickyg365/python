import os

"""
Items
Store

Store -> Items


Items are what drives the data, so they have all their fields input each time an item is created
    but only price and date really fluctuate, the item name, brand and id can be static
Stores are just used for reference and should not be changing often, frequency of addition doesnt matter

Receipts group a collection of items based off of store and date


# Input new Receipt

Store?: 
Date?: 

>> Input Items
name
price
brand


# autogen
store_id
receipt_id

"""


def dict_str(data):
    txt = ""
    for k, v in data.items():
        txt += f"{k}: {v}\n"
    return txt


class ItemEntry:
    def __init__(self, name: str, brand: str):
        self.name = name
        self.brand = brand

        self.price = dict()  # Dict => date: [prices]
        self.store_id = list()  # List

    def __str__(self):
        txt = f"""
name: {self.name}
brand: {self.brand}
"""
        return txt

    def export(self):
        # Add data type check, so that any time you export data it fixes
        data = {
            "name": {self.name},
            "price": {self.price},
            "brand": {self.brand},
            "store_id": {self.store_id},
        }
        return data


class Item(ItemEntry):
    def __init__(self, name: str, price: float, brand: str, date: str, store_id: int):
        super().__init__(name, brand)

        self.price = price
        self.date = date
        self.store_id = store_id

    def __str__(self):
        txt = f"""
name: {self.name}
price: {self.price}
brand: {self.brand}
date: {self.date}
store_id: {self.store_id}
"""
        return txt

    def export(self):
        # Add data type check, so that any time you export data it fixes
        data = {
            "name": {self.name},
            "price": {self.price},
            "brand": {self.brand},
            "date": {self.date},
            "store_id": {self.store_id},
        }
        return data


class Store:
    def __init__(self, name: str, id: str):
        self.name = name
        self.id = id

    def __str__(self):
        txt = f""
        return txt

    def export(self):
        pass


class StoreDatabase:
    def __init__(self):
        self.stores = []  # Store ids in a list
        self.data = None
        self.data_location = ""  # File url

    def __str__(self):
        txt = f""
        return txt

    def save():
        return

    def load():
        return

    def export(self):
        pass


class ItemDatabase:
    def __init__(self):
        self.items = []  # Item ids
        self.data = None
        self.data_location = ""  # File url

    def __str__(self):
        txt = f""
        return txt

    def save():
        return

    def load():
        return

    def export(self):
        pass


def main():
    # Create new base item
    sunny_d = ItemEntry("Sunny Delight", "Kroger")

    # Add to base item database

    # Create receipt input loop
    store = input("Store?: ")
    date = input("Date?: ")

    while True:
        u_in = input(">>> ")


if __name__ == "__main__":
    main()
