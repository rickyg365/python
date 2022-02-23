
import datetime
from typing import List, Dict
from dataclasses import dataclass

@dataclass
class Stock:
    ticker_symbol: str
    date: datetime.date
    data: Dict[str, int]

    def __post_init__(self):
        return

    def export(self) -> Dict[str, any]:
        export_dict = {
            "ticker_symbol": self.ticker_symbol,
            "date": self.date,
        }

        for stock_attr, attr_value in self.data.items():
            export_dict[stock_attr] = attr_value

        return export_dict
