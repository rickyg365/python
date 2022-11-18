import os
import json

from typing import Dict
from models.items import Item

# Todo: Should probably move the input and run functions into a seperate class that's a view, or state manager that takes in and input Inventory

class Inventory:
    def __init__(self, default_path: str="data/my_inventory.json"):
        # Meta Data
        self.total_size = 0
        self.total_price = 0
        self.default_path = default_path
        
        # Item Storage
        self.cached_items: Dict[str, Item] = {}
        self.update_cache()
        
    def __str__(self) -> str:
        txt = ""
        for item in self.cached_items.values():
            txt += f"\n{item}"
        txt += f"\n\nTotal: {self.total_size} items, ${self.total_price:.2f}"
        return txt

    def update_cache(self, new_path: str=None):
        # Check for custom path
        if new_path is None:
            new_path = self.default_path

        # Check if default path exists
        if not os.path.exists(new_path):
            print(f"{new_path} does not exist!")
            return

        self.cached_items = self.load(new_path)
        self.total_size = len(self.cached_items)
        self.total_price = sum([x.price for x in self.cached_items.values()])
        
    def add_item(self, name: str, price: float, quantity: str):
        new_item = Item(name, price, quantity)
        self.cached_items[name] = new_item
        self.total_size += 1
        self.total_price += price

        return new_item  # return item for chaining?
    
    def input_item(self):
        item_name = input("Name: ")
        item_price = float(input("Price: "))
        item_quantity = input("Quantity: ")
        
        return self.add_item(item_name, item_price, item_quantity)
    
    def input_multiple_items(self, amount: int, custom_savepath: str=None):
        for _ in range(amount):
            print(f"\n[ Item #{_ + 1} ]")
            self.input_item()
            print(f"\nAdded!")
        return
    
    def remove_item(self, item_name: str):
        if item_name in self.cached_items.keys():
            chosen_item = self.cached_items[item_name] 
            self.total_price -= chosen_item.price
            del chosen_item
            self.total_size -= 1
        
        return self
    
    def modify_item(self, item_key: str, new_name: str=False, new_price: float=False, new_quantity: str=False):
        # Create new and delete old or actually modfy item
        chosen_item = self.cached_items.get(item_key, Item())
        
        if new_name:
            chosen_item.name = new_name
        
        if new_price:
            old_price = chosen_item.price
            self.total_price += (new_price - old_price)

            chosen_item.price = new_price

        if new_quantity:
            chosen_item.quantity = new_quantity

        # OR
        return self
    
    def save(self, savepath: str=None):
        # Check for custom path
        if savepath is None:
            savepath = self.default_path
        
        save_data = [x.export() for x in self.cached_items.values()]

        with open(savepath, 'w') as save_file:
            json.dump(save_data, save_file, indent=4)
        return self

    def load(self, loadpath: str=None):
        # Check for custom path
        if loadpath is None:
            loadpath = self.default_path
        
        # Check if path exists
        if not os.path.exists(loadpath):
            return

        with open(loadpath, 'r') as load_file:
            loaded_data = json.load(load_file)
        
        # converted_data = [Item(**x) for x in loaded_data]

        # Convert into dict
        final_data = {}
        for item in loaded_data:
            new_item = Item(**item)
            final_data[item.get('name', 'error')] = new_item

        return final_data
    
    def run(self):
        # Preview
        print(self)

        # Add X Items
        num = int(input("\n\nHow many Items to add?: "))
        self.input_multiple_items(num)

        # Final Display
        print("\nFinal Inventory")
        print(self)

        # Optional Save
        u_input = input("\nSave?: ")
        if u_input == 'y':
            self.save()
        return


if __name__ == '__main__':
    sample_item_data = {
        "name": "Yerba Mate - Tropical Uprising",
        "price": 3.29,
        "quantity": "1 can"
    }

    new_inventory = Inventory()
    new_inventory.add_item(**sample_item_data)
    print(new_inventory)

