
from typing import Dict
from dataclasses import dataclass

from item import Item, QuantizedItem


@dataclass(kw_only=True)
class InventoryItem(QuantizedItem):
    purchase_date: str
    storage_location: str
    amount: int = 1
    unit: str = 'ct'

    def __str__(self) -> str:
        return f"{super().__str__()} | {self.storage_location} | {self.purchase_date}"

    def export(self) -> Dict[str, any]:
        export_data = {
            **super().export(),
            "purchase_date": self.purchase_date,
            "storage_location": self.storage_location
        }
        return export_data

