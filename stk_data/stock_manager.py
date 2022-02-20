import os
from load_data import StockData


class StockManager:
    def __init__(self) -> None:
        self.stocks = []

    def __str__(self) -> str:
        pass

    def add_stocks(self, new_ticker_symbol):
        self.stocks.append(new_ticker_symbol)




def main():
    return

if __name__ == "__main__":
    main()
