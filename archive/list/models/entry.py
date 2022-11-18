from typing import List, Dict
from dataclasses import dataclass, field

ENTRY_CONFIG = {
            "name": str,
            "size": int,
            "data": list
        }
@dataclass
class Entry:
    name: str
    size: int = 0
    data: List[str] = field(default_factory=lambda: ["No Data"])

    def __str__(self) -> str:
        data = " | ".join(self.data)
        
        txt = f"\n{self.name}\n[{self.size}]\n| {data} |"
        return txt

    # def config(self):
    #     return {
    #         "name": str,
    #         "size": int,
    #         "data": list
    #     }

    def export(self):
        return {
            "name": self.name,
            "size": self.size,
            "data": self.data
        }

