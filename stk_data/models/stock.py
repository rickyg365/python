
import datetime

from typing import List, Dict
from dataclasses import dataclass, field

@dataclass
class Stock:
    ticker_symbol: str
    date: datetime.date  # str
    open: float = field(compare=False)
    high: float = field(compare=False)
    low: float = field(compare=False)
    close: float = field(compare=False)
    volume: int = field(compare=False)
    dividends: int = field(compare=False)
    stock_splits: int = field(compare=False)

    def export(self) -> Dict[str, any]:
        return {
            "ticker_symbol": self.ticker_symbol,
            "date": self.date,
            "open": self.open,
            "high": self.high,
            "low": self.low,
            "close": self.close,
            "volume": self.volume,
            "dividends": self.dividends,
            "stock_splits": self.stock_splits
        }

        
