import os
import json

import pandas as pd
import yfinance as yf

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


# Stock Symbols
msft = 'MSFT'

# Get Data
msft_data = yf.Ticker(msft)

# Get the historical prices
msft_DF = msft_data.history(period='1d') 

# Get DF Columns
msft_columns = msft_DF.columns

# Print Values for Columns
for key in msft_columns:
    value = msft_DF[f"{key}"]

    print(f"{key}: \n{value.values[0]}\n")


# Convert to Json, pandas return it as a string json so use loads instead of load
msft_JSON = msft_DF.to_json(indent=4)

# Load as python obj
msft_python = json.loads(msft_JSON)

# Get Keys
msft_json_keys = [k for k in msft_python.keys()]

print(msft_json_keys)

# Print Values for each key
for key in msft_json_keys:
    value = [x for x in msft_python[key].values()][0]  # Should only be 1 value

    print(f"{key}: {value}")


print(msft_JSON)

print(msft_python)

print(msft_columns)



class StockData:
    def __init__(self, ticker_symbol=None):
        self.symbol = ticker_symbol
        self.ticker = yf.Ticker(ticker_symbol)

        self.latest_df = self.historical()
        self.latest_json = self.json()
        self.live_data = self.python_obj()

    def __str__(self) -> str:
        pass

    def historical(self, period='1d', start=None, end=None) -> pd.DataFrame:
        return self.ticker.history(period=period, start=start, end=end)
    
    def raw_json(self):
        # Get Updated Historical
        raw_df = self.historical()

        # Convert to Json, pandas return it as a string json so use loads instead of load
        new_json_string = raw_df.to_json(indent=4)

        # Load as python obj
        msft_python = json.loads(new_json_string)

        # Get Keys
        msft_json_keys = [k for k in msft_python.keys()]

        print(msft_json_keys)

        # Print Values for each key
        for key in msft_json_keys:
            value = [x for x in msft_python[key].values()][0]  # Should only be 1 value

            print(f"{key}: {value}")
        
    def raw_python_obj(self):
         # Get Updated Historical
        raw_df = self.historical()

        # Convert to Json, pandas return it as a string json so use loads instead of load
        new_json_string = raw_df.to_json(indent=4)

        # Load as python obj
        return json.loads(new_json_string)

    



print(StockData("MSFT").historical('5d'))





















