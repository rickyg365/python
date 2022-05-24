import os

import json

from typing import List, Dict
from dataclasses import dataclass

from models.stock import Stock
from fetcher.yahoo_finance import stock_data
from adapters.df_adapter import stock_df_to_list

""" """
''' 
Want:
- find by stock symbol
- find by date
'''

class StockWatchList:
    def __init__(self, init_path: str="data/watchlist/memory.json"):
        self.path = init_path
        self.watchlist = []  # stock_symbol
        # stock_symbol: data_path
        self.data = {}
    
    def __str__(self) -> str:
        txt = f"size: {len(self.watchlist)}"
        return txt
    
    def save(self):
        # Save Watchlist
        with open(self.path, 'w') as save_file:
            json.dump(self.watchlist, save_file, indent=4)
        
        # Save indv data
        for stock_symbol, data in self.data.items():
            print(data)
            new_filepath = f"data/tickers/{stock_symbol}.json"
            export_data = [item.export() for item in data]

            with open(new_filepath, "w") as out_file:
                json.dump(export_data, out_file, indent=4)
    
    def load(self):
        # Load Watchlist
        with open(self.path, 'r') as load_file:
            self.watchlist = json.load(load_file)

        # Load indv Data

        return

    def add_stock_data(self, stock_symbol: str, new_data: List[Stock]):
        self.data[f"{stock_symbol}"] = new_data # List of stocks
        self.watchlist.append(stock_symbol)
        return
    
    def update_stock_data(self, stock_symbol: str, new_data: List[Stock] | Stock):
        if type(new_data) is Stock:
            print("worked")
            self.data[stock_symbol].append(new_data)
            return
        self.data[stock_symbol].extend(new_data)
        return
    
    def get_stock_data(self, stock_symbol: str):
        # Method #1 - Walrus Operator LOL redundant
        # if stock_data:=self.watchlist.get(stock_symbol, False):
        #     return stock_data

        # Method #2 - Variable not necessary for this case but still including it in case of future updates
        stock_data = self.data.get(stock_symbol, None)
        return stock_data


def main():
    def get_parsed_data(ticker: str, period: str="1d") -> List[Stock]:
        df = stock_data(ticker, period)
        parsed_data = stock_df_to_list(ticker, df)
        return parsed_data

    tickers = [
        "MSFT",
        "TSLA",
        "SI=F",z
        "BTC-USD",
        "EURUSD=X"
    ]

    new_list = StockWatchList()


    for ticker in tickers:
        raw_data = get_parsed_data(ticker, "5d")
        parsed_data = [Stock(**x) for x in raw_data]

        new_list.add_stock_data(ticker, parsed_data)
        
    print(new_list)
    new_list.save()
    return

if __name__ == '__main__':
    main()
