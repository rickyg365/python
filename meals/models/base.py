from dataclasses import dataclass

@dataclass(kw_only=True)
class ID:
    id: int
    name: str
