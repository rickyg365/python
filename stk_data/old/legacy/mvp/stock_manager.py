import os
from load_data import StockData
from typing import List

class StockManager:
    def __init__(self, stock_symbols:List[str]=None):
        if stock_symbols is None:
            stock_symbols = []

        self.stocks = []
        self.raw_stock_data = {}

        self.add_stocks(stock_symbols)

    def __str__(self) -> str:
        for stock in self.stocks:
            self.show_stock_data(stock)
        return ""

    def add_stock(self, new_ticker_symbol):
        self.stocks.append(new_ticker_symbol)
        self.add_stock_data(new_ticker_symbol)

    def add_stocks(self, list_of_tickers):
        if len(list_of_tickers) < 1:
            return False
        
        for ticker in list_of_tickers:
            if ticker not in self.stocks:
                self.stocks.append(ticker)
            self.add_stock_data(ticker)

        return True

    def show_stock_data(self, stock_symbol):
        # Stock Ticker Symbol
        text = f"[{stock_symbol}]"

        data = self.raw_stock_data.get(stock_symbol)

        # Iterate through dates
        for date, obj in data.items():
            sub_text=""

            # Iterate through each days data
            for cat, val in obj.items():
                # Add to individual days string
                sub_text += f"\n\t\t{cat}: {val}"
                
            # add Day to overall string
            text += f"\n\t{date}: {sub_text}"
        print(text)
        return text

    def add_stock_data(self, new_ticker_symbol):
        self.raw_stock_data[new_ticker_symbol] = StockData(new_ticker_symbol).data


if __name__ == "__main__":
    my_stock_list = [
        "MSFT",
        "TSLA"
    ]
    my_stocks = StockManager(my_stock_list)
    print(my_stocks)

    # all_data = my_stocks.raw_stock_data

    # print(my_stocks.stocks)
    # print(all_data)

    # print(all_data["TSLA"]["02-18-2022"])
    # print(all_data["MSFT"])

