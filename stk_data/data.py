import os
import json

import datetime

import pandas as pd
import numpy as np
import yfinance as yf

from typing import List, Dict

"""
Data we want to store

all_stocks = {
   "stk1": {
       "dt1": [max, min, avg],
       "dt2": [max, min, avg],
   },
   "stk2": {
       "dt1": [max, min, avg],
       "dt2": [max, min, avg],
   },
   "stk3": {
       "dt1": [max, min, avg],
       "dt2": [max, min, avg],
   }
}

"""

sample_live_data = {
   "stk1": {
       "dt1": [max, min, 22.1],
       "dt2": [max, min, 22.1],
   },
   "stk2": {
       "dt1": [max, min, 22.1],
       "dt2": [max, min, 22.1],
   },
   "stk3": {
       "dt1": [max, min, 22.1],
       "dt2": [max, min, 22.1],
   }
}
# ? or
live_data = [

]



class StockData:
    def __init__(self, ticker_symbol: str):
        self.symbol = ticker_symbol
   
        self.current_time = datetime.datetime.now().strftime('%m_%d_%Y')

        self.json_file = f"{self.symbol}.json"

        self.ticker = yf.Ticker(ticker_symbol)

        self.data_frame = self.get_data("5d")  # self.load_json()
        self.py_obj = self.parsed_python()
        self.json_text = json.dumps(self.py_obj, indent=4)

    def __str__(self) -> str:
        text = f"""[{self.symbol}]: {self.json_file}
{self.data_frame}

{self.json_text}

{self.py_obj}
"""
        return text

    def get_data(self, days="1d"):
        data = self.ticker.history(days)
        return data
        
    def parsed_python(self):
        cleaned = {}

        all_columns = [c for c in self.data_frame.columns]
        all_dates = [d for d in self.data_frame[all_columns[0]].keys()]

        for date in all_dates:
            new_date_data = {}
            for col in all_columns:
                value = self.data_frame[col][date]

                # Parsing
                match type(value):
                    case np.int64:
                        value = int(value)
                    case np.float64:
                        value = float(value)
                    case _:
                        break

                new_date_data[col] = value
        cleaned[f"{date}"] = new_date_data
        
        # print(cleaned)
        # print(len(cleaned))

        return cleaned        

    def save_json(self):
        try:
            with open(self.json_file, 'w') as out_json:
                json.dump(self.py_obj, out_json, indent=4, separators=(',', ': '))
        except Exception as e:
            print(e)
    
    def load_json(self) -> pd.DataFrame:
        try:
            with open(self.json_file, 'r') as in_json:
                data = json.load(in_json)
            return pd.DataFrame(data, index=[k for k in data.keys()])
        except FileNotFoundError:
            return self.get_data("1d")


if __name__ == "__main__":
    my_stocks = [
        "MSFT",
        "TSLA"
    ]

    for stock in my_stocks:
        new_stock = StockData(stock)
        print(new_stock.get_data('5d'))
        print(new_stock)
        new_stock.save_json()


# Get Initial Data from yahoo as DF
# Convert to Dict and Parse
# Save Json (File) from dict
# lOad Json (File) to dict

