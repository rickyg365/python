from typing import Dict
from dataclasses import dataclass

"""
class ItemBase(ABC):
    def __str__(self) -> str:
        pass
    
    @abstractmethod
    def export(self) -> Dict[str, any]:
        pass
"""

@dataclass 
class Item:
    name: str
    price: float

    def __str__(self) -> str:
        # Price and Quantity
        price = f"[${self.price:.2f}]"

        return f"{self.name.title():<18} {price:>8}"

    def export(self) -> Dict[str, any]:
        export_data = {
            "name": self.name,
            "price": self.price
        }
        return export_data


@dataclass(kw_only=True)
class QuantizedItem(Item):
    amount: int
    unit: str

    def __str__(self) -> str:
        # Can redefine here if we need more control but the property works fine for now
        quantity = f"{self.amount:>2} {self.unit}"
        return f"{super().__str__()} @ {quantity}"

    def export(self) -> Dict[str, any]:
        export_data = {
            **super().export(),
            "amount": self.amount,
            "unit": self.unit,
        }
        return export_data

    @property
    def quantity(self):
        return f"{self.amount} {self.unit}"

    @quantity.setter
    def quantity(self, new_quantity: str):        
        # Parse Value
        quantity_data = new_quantity.split(" ")
        
        if len(quantity_data) != 2:
            raise Exception
        
        new_amount, new_unit = int(quantity_data[0]), quantity_data[1]
        # Check Values
        # if new_unit not in ['oz', 'ct']:
        #     raise Exception
        # Set Values
        self.unit = new_unit
        self.amount = new_amount
    
