import os

from typing import List
from dataclasses import dataclass

@dataclass
class Item:
    name: str
    price: float
    tags: List[str]
    brand: str
    flavor: str
    cache_path: str = "data/grocery_item_cache/items.json"

    def __str__(self) -> str:
        txt = f"{self.name} (${self.price})"
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
