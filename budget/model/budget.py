import os

from typing import List
from dataclasses import dataclass

# Models
from item import Item

@dataclass
class Budget:
    target_price: float
    total_price: float = 0.00
    items: List[Item] = None

    def __post_init__(self):
        if self.items is None or len(self.items) <= 0:
            self.items = []
        return

        # Get initial total, based on passed items
        total = 0.00
        for item in self.items:
            total += item.price
        self.total_price = total
    
    @property
    def price_difference(self):
        return self.target_price - self.total_price

    def get_item_by_id(self, ref_id: str) -> Item | None:
        # def check_id(item_id):
        #     if item_id == ref_id:
        #         return True
        #     return False

        # Lambda Version
        check_id = lambda x: True if x.id == ref_id else False
        
        # Filter
        # print(list(filter(check_id, self.items)))
        
        # Loop
        for item in self.items:
            # Assuming id is unique we return as soon as we hit a match
            if check_id(item):
                return item

        return None

    def add_item(self, new_item):
        # Update total as we add new items
        self.total_price += new_item.price
        self.items.append(new_item)

    def remove_item(self, item_id):
        # Get item
        chosen_item = self.get_item_by_id(item_id)

        # Update total as we remove new items
        self.items.remove(chosen_item)
        self.total_price -= chosen_item.price

        return True

        

def main():
    new_budget = Budget(100.00)
    new_budget.add_item(Item("1", "test", 0.10))

    print(new_budget)
    print(new_budget.price_difference)
    new_budget.get_item_by_id("1")

if __name__ == '__main__':
    main()
