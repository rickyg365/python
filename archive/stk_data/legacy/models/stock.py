
import datetime

from enum import Enum

from typing import List, Dict
from dataclasses import dataclass, field


"""
TBI: 
- Overide addition so that you can add data together!
- Overide equality to check if symbol and date are the same!



Ideas for refactor

class Ticker:
    name: str
    data: [
        {
            date,
            open,
            high,
            low,
            close,
            volume,
            dividends,
            stock_splits
        },
        StockDataPoint
    ]


class StockDataPoint:
    date
    open
    high
    low
    close
    volume
    dividends
    stock_splits
    

"""

@dataclass
class Stock:
    ticker_symbol: str
    date: str  # datetime.date  # str
    open: float = field(compare=False)
    high: float = field(compare=False)
    low: float = field(compare=False)
    close: float = field(compare=False)
    volume: int = field(compare=False)
    dividends: int = field(compare=False)
    stock_splits: int = field(compare=False)

    def __str__(self) -> str:
        txt = f"{self.date} [{self.ticker_symbol}]: "
        return txt

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

        
