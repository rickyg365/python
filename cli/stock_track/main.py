import os

from datetime import datetime

from typing import List, Dict

class Stock:
    def __init__(self, name: str, ticker: str=None):
        self.name = name
        self.ticker = ticker

    def __str__(self):
        s = f'{self.name}'
        return s
    
    def export(self):
        return {
            'name': self.name,
            'ticker': self.ticker
        }


class HeldStock(Stock):
    DATETIME_KEY_FORMAT = f'%m%d%y_%I%M%S'
    DATETIME_VIEW_FORMAT = f'%m/%d/%y %I:%M:%S'
    def __init__(self, name: str, ticker: str=None, entry: float=None, low_exit: float=None, high_exit: float=None, history: List[Dict]=None):
        super().__init__(name, ticker)

        # Meta
        self.entry = entry
        self.low_exit = low_exit
        self.high_exit = high_exit

        # Status
        self.last_update = None  # datetime
        self.last_price = None  # price
        self.history = history  # { datetime, price }
        
        if self.history is None:
            self.history = dict()

        self.get_update() # Initial update/entry

    def __str__(self):
        s = f'[{self.ticker}] {self.name} | {self.last_price} | {self.last_update}'
        return s
    
    def check_threshold(self):
        pre_warning = 1
        if self.last_price >= self.low_exit + pre_warning:
            print("Reaching Low Exit Threshold...")
        
        if self.last_price <= self.high_exit - pre_warning:
            print("Reaching High Exit Threshold...")

        return
    
    def get_update(self):
        raw_date = datetime.now()
        dt = raw_date.strftime(self.DATETIME_KEY_FORMAT)

        print(dt)
        price = 447.42 # Pull data

        # Update status
        if self.entry is None:
            self.entry = price

        self.last_update = raw_date
        self.last_price = price

        # Update history
        self.history[dt] = price
        
        # Notifications
        self.check_threshold()
        return

    def export(self):
        return {
            **super().export(),
            'entry': self.entry,
            'low_exit': self.low_exit,
            'high_exit': self.high_exit,
            'history': self.history
        }



if __name__ == "__main__":
    RAW_STOCK_DATA = {
        'name': 'Microsoft',
        'ticker': 'MSFT'
    }

    RAW_HELD_DATA = [
        {
            'name': 'Microsoft',
            'ticker': 'MSFT',
            'entry': 444.12,
            'low_exit': 400.00,
            'high_exit': 528.00
        }
    ]


    s = Stock(**RAW_STOCK_DATA)
    hs = HeldStock(**RAW_HELD_DATA[0])

    print(s)

    print(hs)
