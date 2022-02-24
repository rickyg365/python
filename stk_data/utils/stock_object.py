
import datetime

import pandas as pd
from typing import List, Dict
from dataclasses import dataclass, field

@dataclass
class Stock:
    ticker_symbol: str
    date: datetime.date
    open: float = field(compare=False)
    high: float = field(compare=False)
    low: float = field(compare=False)
    close: float = field(compare=False)
    volume: int = field(compare=False)
    dividends: int = field(compare=False)
    stock_splits: int = field(compare=False)

    def export(self) -> Dict[str, any]:
        export_dict = {
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
        # for key, value in export_dict.items():
        #     print(type(value), key, value)

        return export_dict
