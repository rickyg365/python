from typing import List, Dict
from dataclasses import dataclass

"""

Milk - 1 ct [$3.99]

"""

@dataclass
class ShoppingItem:
    name: str
    price: float
    amount: int = 0
    unit: str = "ct"
    
    def __str__(self) -> str:
        # Name and Description
        price = f"[${self.price:.2f}]"
        text=f"{self.name.title():<18} {price:>8} | {self.amount:<3} {self.unit:<3}"

        return text
    
    def export(self) -> Dict[str, any]: 
        return {
            "name": self.name,
            "price": self.price,
            "amount": self.amount,
            "unit": self.unit,
        }

def main():
    # Sample Recipe Data
    test_shopping_item = {
        "name": "Milk",
        "price": 3.99,
        "amount": 1,
        "unit": "ct"
    }
    # Create Recipe Object
    new_shopping_item = ShoppingItem(**test_shopping_item)

    # Display | str() Method
    # print(json.dumps(new_recipe.export(), indent=4))
    print(new_shopping_item)

if __name__ == '__main__':
    main()
