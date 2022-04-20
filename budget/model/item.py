import os

from typing import List
from dataclasses import dataclass

@dataclass
class Item:
    id: str
    name: str
    price: float
    tags: List[str] = None
    brand: str = None
    flavor: str = None
    cache_path: str = "data/grocery_item_cache/items.json"

    def __str__(self) -> str:
        txt = f"{self.name} (${self.price:.2f})"
        return txt

    def cache(self):
        new_dict = {
            "name": self.name,
            "price": self.price,
            "tags": self.tags,
            "brand": self.brand,
            "flavor": self.flavor
        }
        return new_dict

    

def main():
    return

if __name__ == '__main__':
    main()
