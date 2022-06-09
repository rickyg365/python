import os

import time
import datetime

import pandas as pd

import pickle
import json
from utils.load_save import save_json

from models.stock import Stock
from source.yahoo import get_raw_data, get_data, extract_df

from typing import List

"""

Each Stock Gets its own file

Each file has a Dict of the stock data on diff dates

[MSFT] -> 
{
    "date1": {
        ...
    },
    "date2": {
        ...
    },
    ...
}

"""


'''
stocks_to_track = [
    "MSFT",
    "TSLA",    
]

stockTracker class

'''

class StockDataPoint:
    def __init__():
        pass
        


class StockTracker:
    """
    Load Raw Data at the start
    Hydrate Models as needed and keep them in a cache


    entries: {
        ticker_symbol: {
            date: {
                data
            },
            date: {
                data
            },
            date: {
                data
            },
            ...
        }
    }

    To Access
    self.entries[ticker_symbol][date]
    """
    def __init__(self, tickers_to_track: List[str]=None, raw_path="raw_data.json", model_path="model_data.pickle", list_path="ticker_tracker.json") -> None:
        if tickers_to_track is None:
            tickers_to_track = []

        self.raw_path = raw_path
        self.list_path = list_path
        self.model_path = model_path
        
        self.stocks = tickers_to_track  # List of Tickers
        self.raw_data = {} # { ticker: { date: data, ... }, ... }
        self.models = {}  # { ticker: { date: Stock(**data), ... }, ... }
        
        # Load Data
        self.load_raw_data(raw_path)
        

    def __str__(self) -> str:
        txt = f""
        return txt

    def save_ticker_list(self, custom_filepath=None):
        if custom_filepath is None:
            custom_filepath = self.list_path

        with open(custom_filepath, 'w') as out_json:
            json.dump(self.stocks, out_json)
        return True

    def save_raw_data(self, custom_filepath=None):
        if custom_filepath is None:
            custom_filepath = self.raw_path
            
        with open(custom_filepath, 'w') as out_json:
            json.dump(self.raw_data, out_json, indent=4)
        return True

    def save_models(self, custom_filepath=None):
        if custom_filepath is None:
            custom_filepath = self.model_path
            
        with open(custom_filepath, 'wb') as out_pick:
            pickle.dump(self.models, out_pick)
        return True

    def load_raw_data(self, filepath="raw_data.json"):
        with open(filepath, 'r') as in_json:
            self.raw_data = json.load(in_json)
        return True
    
    def load_models(self, filepath="model_data.pickle"):
        with open(filepath, 'rb') as in_pick:
            self.models = pickle.load(in_pick)
        return True

    def hydrate_model(self, chosen_ticker: str, chosen_date: str):
        """ (ticker, date) -> Stock(**raw_data[ticker][date]) """
        return Stock(**self.raw_data[chosen_ticker][chosen_date])

    def hydrate_ticker_models(self, chosen_ticker: str):
        # Method #1
        # for date, data in self.raw_data[chosen_ticker].items():
        #     self.models[chosen_ticker][date] = Stock(**data)

        # Method #2
        for date in self.raw_data[chosen_ticker]:
            self.models[chosen_ticker][date] = self.hydrate_model(chosen_ticker, date)
         
    def hydrate_all_models(self):
        # Make sure the raw data is loaded
        for ticker, ticker_data in self.raw_data.items():
            for date, data in ticker_data.items():
                self.models[ticker][date] = Stock(**data)

 
def main():
    # Variables
    stock_symbol = "MSFT"
    period = "5d"

    # Get Data, (stock_symbol, period) -> pd.DataFrame
    new_data = get_raw_data(stock_symbol, period)  # pd.DataFrame
    
    # Extract data, pd.DataFrame -> { date: data }
    extracted_data = extract_df(stock_symbol, new_data)  # { date: data }
    
    # Convert Data into Model, { date: data } -> Stock(**data)
    modeled_data = [Stock(**data) for data in extracted_data.values()]  # [Stock(**data)]

    # Save data, ({ date: data }, filepath) -> output file
    save_json(extracted_data, f"{stock_symbol}.json")

    # Display Data
    print(f"""
Pandas Dataframe
{40*'-'}
{new_data}
{40*'-'}


Extracted Data
{40*'-'}
{extracted_data}
{40*'-'}


Modeled Data
{40*'-'}
{modeled_data}    
{40*'-'}

""")


if __name__ == '__main__':
    # main()
