from models.base import ID
from dataclasses import dataclass

@dataclass
class Store(ID):
    distance: str = None

    def __str__(self) -> str:
        txt = f""
        return txt

    def export(self):
        return {
            "id": self.id,
            "name": self.name,
            "distance": self.distance
        }

