import os

from stock_object import Stock

from stock_data import get_data
from handle_json import load_json, save_json


class StockManager:
    def __init__(self, data_filepath:str="stock_data.json"):
        self.filepath = data_filepath
        self.stocks = []

        self.load()

    def add_stock(self, new_ticker_symbol: str):
        """"""        
        new_stock = get_data(new_ticker_symbol)

        if not new_stock:
            return False
        
        self.stocks.append(*new_stock)
        return True

    def remove_stock(self, comparison_obj, comparison_type="ticker"):
        chosen_comparison = None
        match comparison_type:
            case "ticker":
                compare_by_ticker = lambda x: x.ticker_symbol != comparison_obj
                chosen_comparison = compare_by_ticker
            case "date":
                compare_by_date = lambda x: x.date != comparison_obj
                chosen_comparison = compare_by_date

        new_list = list(filter(chosen_comparison, self.stocks))
        print(new_list)
        self.stocks = new_list
        return True
    
    def update_stock(self, ticker_symbol):
        """ Checks previous 30 days of data and updates adds """
        new_stock = get_data(ticker_symbol, '1mo')

        if not new_stock:
            return False
        
        for stock in new_stock:
            self.stocks.append(stock)
        return

    def load(self):
        # Loaded stocks
        if os.path.isfile(self.filepath):
            new_stocks = load_json(self.filepath)
            output = []
            for stock in new_stocks:
                # Spread Data
                ticker_symbol = stock['ticker_symbol']
                new_date = stock['date']
                new_data = { **stock }

                output.append(Stock(ticker_symbol, new_date, new_data))
            self.stocks = output
        
    def save(self):
        json_list = []
        for stock in self.stocks:
            json_list.append(stock.export())
            
        save_json(self.filepath, json_list)


def main():
    new_stock_manager = StockManager()

    # new_stock_manager.add_stock("TSLA")
    # new_stock_manager.add_stock("MSFT")

    # new_stock_manager.update_stock("MSFT")
    print(new_stock_manager.stocks)
    
    new_stock_manager.remove_stock("MSFT")
    new_stock_manager.save()


if __name__ == '__main__':
    main()


