from models.base import ID
from dataclasses import dataclass

@dataclass
class Item(ID):
    brand: str = None
    flavor: str = None

    def __str__(self) -> str:
        txt = f""
        return txt

    def export(self):
        return {
            "id": self.id,
            "name": self.name,
            "brand": self.brand,
            "flavor": self.flavor
        }

