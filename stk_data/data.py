import os
import json

import datetime
from textwrap import indent

import pandas as pd
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


class StockData:
    def __init__(self, ticker_symbol: str):
        self.symbol = ticker_symbol
   
        self.current_time = datetime.datetime.now().strftime('%m_%d_%Y')

        self.json_file = f"{self.symbol}.json"

        self.ticker = yf.Ticker(ticker_symbol)

        self.data_frame = self.get_data()
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
        
    def parsed_python(self) -> Dict[str, any]:
        cleaned = {}
        # Convert to Json, pandas return it as a string json so use loads instead of load
        new_json_string = self.data_frame.to_json(indent=4)

        # Load as python obj
        raw_py_obj = json.loads(new_json_string)

        # Get Keys
        obj_keys = [k for k in raw_py_obj.keys()]

        # Print Values for each key
        for key in obj_keys:
            value = [x for x in raw_py_obj[key].values()][0]  # Should only be 1 value
            cleaned[key] = value

        return cleaned        

    def save_json(self):
        try:
            with open(self.json_file, 'w') as out_json:
                json.dump(self.py_obj, out_json, indent=4)
        except Exception as e:
            print(e)
    
    def load_json(self):
        with open(self.json_file, 'r') as in_json:
            data = json.load(in_json)
        return data


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

