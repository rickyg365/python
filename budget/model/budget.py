import os

from dataclasses import dataclass
from typing import List


@dataclass
class Budget:
    target_price: float
    total_price: float = 0.00
    items: List[any] = None

    def __post_init__(self):
        if self.items is None or len(self.items) <= 0:
            return

        total = 0.00
        for item in self.items:
            total += item.price
        self.total_price = total
    
    @property
    def price_difference(self):
        return self.target_price - self.total_price

    def add_item(self, new_item):
        self.total_price += new_item.price
        self.items.append(new_item)
        

def main():
    new_budget = Budget(100.00)
    print(new_budget)
    print(new_budget.price_difference)

if __name__ == '__main__':
    main()
