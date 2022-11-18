
from typing import Dict
from dataclasses import dataclass

from models.item import Item, QuantizedItem


@dataclass(kw_only=True)
class GroceryItem(QuantizedItem):
    amount: int = 0
    unit: str = 'ct'

    purchase_date: str = "Create auto datetime"
    expiration_date: str = ""

    def __str__(self) -> str:
        data = f"{self.purchase_date} -> {self.expiration_date}"

        return f"{super().__str__()} | {data}"

    def export(self) -> Dict[str, any]:
        export_data = {
            **super().export(),
            "purchase_date": self.purchase_date,
            "expiration_date": self.expiration_date
        }
        return export_data



