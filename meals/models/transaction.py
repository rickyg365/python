from dataclasses import dataclass


@dataclass
class Transaction:
    id: int
    item_id: int
    store_id: int
    quantity: int
    unit: str
    unit_price: float
    total_price: float

    def __str__(self) -> str:
        txt = f""
        return txt

    def export(self):
        return {
            "id": 1,
            "item_id": 1,
            "store_id": 1,
            "quantity": 2,
            "unit": "Each",
            "unit_price": 1.00,
            "total_price": 2.00
        }

