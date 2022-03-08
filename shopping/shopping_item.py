from typing import List, Dict
from dataclasses import dataclass

"""

Milk - 1 ct [$3.99]

"""

@dataclass
class ShoppingItem:
    name: str
    price: float
    quantity_amount: int = 0
    quantity_unit: str = "ct"
    max_width: int = 35

    def __str__(self) -> str:
        # Name and Description
        price = f"[${self.price:.2f}]"
        text=f"{self.name.title():<18} {price:>8} | {self.quantity_amount:<3} {self.quantity_unit:<3}"

        return text
    
    def export(self) -> Dict[str, any]: 
        return {
            "name": self.name,
            "price": self.price,
            "quantity_amount": self.quantity_amount,
            "quantity_unit": self.quantity_unit,
        }

def main():
    # Sample Recipe Data
    test_shopping_item = {
        "name": "Milk",
        "price": 3.99,
        "quantity_amount": 1,
        "quantity_unit": "ct"
    }
    # Create Recipe Object
    new_shopping_item = ShoppingItem(**test_shopping_item)

    # Display | str() Method
    # print(json.dumps(new_recipe.export(), indent=4))
    print(new_shopping_item)

if __name__ == '__main__':
    main()
