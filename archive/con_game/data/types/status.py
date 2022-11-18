from enum import Enum

class StatusCondition(Enum):
    burn: str = "BURNED"
    freeze: str = "FROZEN"
    paralyze: str = "PARALYZED"
    confuse: str = "CONFUSED"

