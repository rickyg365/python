from typing import List, Dict
from dataclasses import dataclass

"""   
Add item config file 
so that custom item objects can be made!!!!
"""

@dataclass
class Item:
    name: str = "No Name"
    price: float = 0.00
    quantity: str = "No Quantity"

    def __str__(self):
        # Text Chunks
        price = f"${self.price:.2f}"
        quantity = f"{self.quantity}"
        name = f"{self.name.title()}"
        
        # Spacing
        txt = f"| {price:^9} | {quantity:^9} | {name}"
        return txt
    
    def export(self):
        """ Export all attributes as a Dict { attr_name: attr_value } """
        return {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }


if __name__ == '__main__':
    sample_item_data = {
        "name": "Yerba Mate - Tropical Uprising",
        "price": 3.29,
        "quantity": "1 can"
    }

    new_item = Item(**sample_item_data)

    print(new_item)
