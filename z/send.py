import os
from dataclasses import dataclass, field

"""
Raw Data -> Model -> Raw Data

raw_data = {
    "name": "Yerba Mate",
    "price": 2.99,
    "brand": "Yerba Mate",
    "flavor": "Sparkling Cranberry",
    "tags": "energy drink"
}

"""

@dataclass
class GroceryItem:
    name: str
    price: float
    tags: str=None
    brand: str=None
    flavor: str=None

    def __str__(self) -> str:
        opt_flavor = "" if self.flavor is None else f"- {self.flavor}"
        txt = f"[${self.price:.02f}] {self.name} {opt_flavor}"
        return txt
    
    def full_txt(self):
        opt_brand = "" if self.brand is None else self.brand
        opt_tags = "" if self.tags is None else "|".join(self.tags.split(" "))
        return f"{self}\n{opt_brand}\n{opt_tags}"


def main():
    raw_data = {
        "name": "Yerba Mate",
        "price": 2.99,
        "brand": "Yerba Mate",
        "flavor": "Sparkling Cranberry",
        "tags": "energy drink"
    }

    new_item = GroceryItem(**raw_data)

    print(new_item)


    print(new_item.full_txt())

    return

if __name__ == '__main__':
    main()
