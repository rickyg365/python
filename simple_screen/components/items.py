import os
from dataclasses import dataclass


"""

15G Sword   
15G Shield 

[15G] Sword   
[15G] Shield 

<15G> Sword   
<15G> Shield 

(15G) Sword   
(15G) Shield 


Sword   15G
Shield  15G

Sword   [15G]
Shield  [15G]

Sword   (15G)
Shield  (15G)

Sword   <15G>
Shield  <15G>

"""


@dataclass
class Item:
    name: str
    description: str
    price: int

    def __str__(self) -> str:
        txt = f"{self.name:<15}  {self.price}G"
        return txt
    
    def show_stats(self):
        return 
    
    def export(self):
        return {
            "name": self.name,
            "description": self.description,
            "price": self.price
        }


class InventoryItem(Item):
    def __init__(self, name: str, description: str, price: int, amount: int=1):
        super().__init__(name=name, description=description, price=price)
        self.amount = amount
    
    def __str__(self) -> str:
        txt = f"[{self.amount}] {self.name}"
        return txt


    def update_amount(self, new_amount: int):
        self.amount = new_amount   


class Inventory:
    def __init__(self):
        self.items = []  # item_object
        self.quick_access_by_name = {}  # name: item_object    
        # self.quick_access_by_id = {}  # ID: item_object

        self.max_str_width = 20

    def __str__(self) -> str:
        txt = f"\nInventory\n{'-'*20}\n"
        for item_obj in self.items:
            txt += f"{item_obj}\n"
        return txt

    def add(self, new_item: Item):
        item_data = new_item.export()
        
        new_inventory_item = InventoryItem(**item_data)
        
        self.items.append(new_inventory_item)
        self.quick_access_by_name[new_item.name] = new_inventory_item
    

    def add_multiple(self, list_of_items):
        for item in list_of_items:
            self.add(item)
        
    def remove(self, item_name: str):
        chosen_item = self.quick_access_by_name[item_name]

        self.items.remove(chosen_item)
        del self.quick_access_by_name[item_name]

    def remove_multi(self, list_to_remove):
        for item in list_to_remove:
            self.remove(item)


def main():
    # Item Data
    item_data = {
        "name": "Item Name",
        "description": "A sample item description",
        "price": 1.23
    }

    # Create New Items
    i1 = Item("Sword", "A small pointy blade, used for attacking", 15)
    i2 = Item("Shield", "A small round lid, used for defending", 12)
    i3 = Item("Potion", "A small potion, heals 20 HP", 10)

    # Create List
    new_items = [
        i1,
        i2,
        i3
    ]

    # Create Inventory
    new_inventory = Inventory()
    new_inventory.add_multiple(new_items)
    new_inventory.items[2].update_amount(15)

    print(new_inventory)

    return

if __name__ == '__main__':
    main()
