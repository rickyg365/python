import os

import json

from typing import List

from utils.stock_object import Stock
from utils.stock_data import get_data


"""
Todo: sort data before save and during load or when you add
TODO: Updates values as the day goes by make a day tracker that scans for an update every hour! 
! IDEA
!   Each ticker symbol is its own stock object
!       With a dict
!            key: data
*            datetime: {data}
!

self.stocks = Dict[ticker_symbol, Stocks]

to find specific stock, by datetime
    self.stocks[ticker][datetime] = data



"""

class StockAPI:
    def __init__(self, input_filepath="data/stock_data.json"):
        self.filepath = input_filepath

        # For Quick Access
        self.stock_symbols = set()

        # Data
        self.stocks = self.load()

    def __repr__(self):
        text = f"""
Tickers: {self.stock_symbols}
Entries: {len(self.stocks)}
Filepath: {self.filepath}"""
        
        return text

    def add_stock(self, new_ticker_symbol: str):
        """ Adds new stock or provides update for most recent data """
        if new_ticker_symbol in self.stock_symbols:
            print("UPDATE")
            self.update_stock(new_ticker_symbol, '1d')
            return

        new_stock = get_data(new_ticker_symbol)

        if not new_stock:
            # Failed to get data
            return False

        # Add Symbol and Stock Object/s to the stock list
        self.stock_symbols.add(new_ticker_symbol)
        self.stocks.append(*new_stock)
        return True

    def remove_stock(self, comparison_obj, comparison_type="ticker"):
        chosen_comparison = None

        match comparison_type:
            case "ticker":
                # Compare by Ticker
                chosen_comparison = lambda x: x.ticker_symbol != comparison_obj

            case "date":
                # Compare by Date
                chosen_comparison = lambda x: x.date != comparison_obj

        self.stocks = list(filter(chosen_comparison, self.stocks))
        return True

    def remove_multi(self, ticker_list):
        # Clear Stock Manager
        for symbol in ticker_list:
            self.remove_stock(symbol)
            self.stock_symbols.remove(symbol)

    def update_stock(self, ticker_symbol, days='5d'):
        """ Checks previous 30 days of data and updates adds """
        new_stocks = get_data(ticker_symbol, days)

        if not new_stocks:
            return False

        # Only stocks w/ same ticker
        filtered_stocks = list(filter(lambda x: x.ticker_symbol == ticker_symbol, self.stocks))
        
        # Only stocks not in filtered stocks
        final_list = list(filter(lambda x: x not in filtered_stocks, new_stocks))

        for stock_data in final_list:
            self.stocks.append(stock_data)
        return

    def check_date(self, new_date):
        """ Check a dates data or if it doesnt exist retrieve it from yf  """
        return

    def load(self) -> List[Stock]:
        """ Load stock data as a list of Stock objects """
        output_data = []

        # If file Exists Load Stocks
        if os.path.isfile(self.filepath):
            # Read in Raw File Data    
            with open(self.filepath, 'r') as in_json:
                new_data = json.load(in_json)
            
            # Parse Data
            for stock in new_data:
                # Split Data
                ticker_symbol = stock['ticker_symbol']
                new_date = stock['date']

                # Could use .pop() above to also remove value but for now we'll leave this redundancy, for ease of export
                new_data = { **stock }

                if ticker_symbol not in self.stock_symbols:
                    self.stock_symbols.add(ticker_symbol)
                
                # Create new Stock obj and add to list
                output_data.append(Stock(ticker_symbol, new_date, new_data))
            
        return output_data
            
        # self.stocks = load_data(self.filepath)
        
    def save(self):
        json_list = []
        for stock in self.stocks:
            json_list.append(stock.export())        

        # save_data(self.filepath, json_list)
        with open(self.filepath, 'w') as out_json:
            json.dump(json_list , out_json, indent=4)


def main():
    new_stock_manager = StockAPI()
    print(new_stock_manager)

    all_sym = [*new_stock_manager.stock_symbols]

    # Clear Stock Manager
    new_stock_manager.remove_multi(all_sym)

    # Add new Stocks
    new_stocks = [
        "TSLA",
        "MSFT"
    ]

    for new_stock_ticker in new_stocks:
        # If already in, check for update
        new_stock_manager.add_stock(new_stock_ticker)

    # new_stock_manager.update_stock("MSFT")
    print(new_stock_manager.stocks)

    new_stock_manager.save()


if __name__ == '__main__':
    main()


