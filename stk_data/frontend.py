import os

from stock_object import Stock

from stock_data import get_data
from handle_json import load_json, save_json


class StockManager:
    def __init__(self, data_filepath:str="stock_data.json"):
        self.filepath = data_filepath
        self.stocks = {}

        self.load()

    def add_stock(self, new_ticker_symbol: str):
        """"""        
        new_stock = get_data(new_ticker_symbol)

        if not new_stock:
            return False
        
        self.stocks[new_ticker_symbol] = new_stock
        return True

    def remove_stock(self, ticker_symbol: str):
        print(self.stocks)
        if ticker_symbol not in self.stocks.keys():
            return False

        # del self.stocks[ticker_symbol]
        removed_data = self.stocks.pop(ticker_symbol)
        # print(f"Removed: {removed_data}")

        return True
    
    def update_stock(self, ticker_symbol):
        """ Checks previous 30 days of data and updates adds """
        new_stock = get_data(ticker_symbol, '1mo')

        if not new_stock:
            return False
        
        self.stocks[ticker_symbol] = [ *self.stocks[ticker_symbol], *new_stock]
        return

    def load(self):
        # Loaded stocks
        if os.path.isfile(self.filepath):
            new_stocks = load_json(self.filepath)
            def parse_func(raw_data):
                output = {}
                for ticker_symbol, stocks in raw_data.items():
                    new_list = []
                    for stock in stocks:
                        removed_symbol = stock.pop('ticker')
                        new_date = stock.pop('date')

                        new_data = { **stock }
                        new_list.append(Stock(removed_symbol, new_date, new_data))
                    output[ticker_symbol] = new_list
                return output
            self.stocks = parse_func(new_stocks)

    def save(self):
        json_dict = {}
        for ticker_symbol, company_data in self.stocks.items():
            json_list = []
            for stock in company_data:
                json_list.append(stock.export())
            json_dict[ticker_symbol] = json_list
        save_json(self.filepath, json_dict)


def main():
    new_stock_manager = StockManager()

    # new_stock_manager.add_stock("TSLA")
    # new_stock_manager.add_stock("MSFT")

    # new_stock_manager.update_stock("MSFT")
    # new_stock_manager.save()
    print(new_stock_manager.stocks)
    # new_stock_manager.remove_stock("MSFT")
    new_stock_manager.save()


if __name__ == '__main__':
    main()


