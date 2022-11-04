from enum import Enum

from dataclasses import dataclass

# Container Types
class Pan(Enum):
    HOTEL = "Hotel Pan"
    DEEP = "Deep Pan"
    SHALLOW = "Shallow Pan"

class Bowl(Enum):
    BIG = "Big Bowl"
    SMALL = "Small Bowl"

# Container Class
@dataclass
class Container():
    type: Bowl | Pan = None

    def __repr__(self) -> str:
        txt = f"{self.type.value}"
        return txt


if __name__ == "__main__":
    
    small_bowl = Container(Bowl.SMALL)
    big_bowl = Container(Bowl.BIG)
    
    hotel_pan = Container(Pan.HOTEL)
    deep_pan = Container(Pan.DEEP)
    shallow_pan = Container(Pan.SHALLOW)
    
    
    print(f"{small_bowl = }")
    print(f"{big_bowl = }")

    print(f"{hotel_pan = }")
    print(f"{deep_pan = }")
    print(f"{shallow_pan = }")
