from typing import Dict, List
from dataclasses import dataclass, field


@dataclass
class Stock:
    entry_id: str
    open: float = field(compare=False)
    high: float = field(compare=False)
    low: float = field(compare=False)
    close: float = field(compare=False)
    volume: int = field(compare=False)
    dividends: int = field(compare=False)
    stock_splits: int = field(compare=False)

    def __str__(self) -> str:
        txt = f"[{self.entry_id.replace('_', ' ')}]: "
        return txt

    def export(self) -> Dict[str, any]:
        """ Should this also return the date? """
        return {
            "entry_id": self.entry_id,
            "open": self.open,
            "high": self.high,
            "low": self.low,
            "close": self.close,
            "volume": self.volume,
            "dividends": self.dividends,
            "stock_splits": self.stock_splits
        }
