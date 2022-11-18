from dataclasses import dataclass
import os
import json

import time
import datetime
from textwrap import indent

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


def load_json(filepath="default.json"):
    new_data = None
    try:
        with open(filepath, 'r') as in_json:
            new_data = json.load(in_json)            
        # return pd.DataFrame(data, index=[k for k in data.keys()])
    except FileNotFoundError:
        new_data = {}
    return new_data

def save_json(data, filepath="default.json"):
    try:
        with open(filepath, 'w') as out_json:
            json.dump(data, out_json, indent=4, separators=(',', ': '))
    except Exception as e:
        print(e)

    
def date_time_parse(raw_datetime):
    # new_dt = datetime.datetime(raw_string)
    return raw_datetime.date().strftime("%m-%d-%Y")

def extract_data(ticker_data, skip_dates=None):
    # print("Running_Extraction")
    cleaned = {}

    all_columns = [c for c in ticker_data.columns]
    all_dates = [d for d in ticker_data[all_columns[0]].keys()]

    for date in all_dates:
        new_date = date_time_parse(date)

        if skip_dates is not None and new_date in skip_dates:
            continue

        new_date_data = {}
        for col in all_columns:
            value = ticker_data[col][date]

            # Parsing
            match type(value):
                case np.int64:
                    value = int(value)
                case np.float64:
                    value = float(value)
                case _:
                    break

            new_date_data[col] = value
        cleaned[new_date] = new_date_data
    # print(cleaned)
    return cleaned



if __name__ == "__main__":
    my_stocks = [
        "MSFT",
        "TSLA"
    ]

    

    for ticker_symbol in my_stocks:
        # Create new Ticker obj
        current_stock = yf.Ticker(ticker_symbol)
        
        # Check json for already existing values
        loaded_data = load_json(f"{ticker_symbol}.json")
        loaded_cache = None

        if loaded_data:
            print(f"Loaded: {ticker_symbol}")
            loaded_cache = [d for d in loaded_data.keys()]

        # Make New dict from data frame and save as json
       
        # Get 5 Day DataFrame
        new_df = current_stock.history('5d')

        # Extract into dict skipping already existing data
        extracted_data = extract_data(new_df, loaded_cache)

        # Combine Loaded Data and New Data
        new_data = {**loaded_data, **extracted_data}
        
        # Save all data into json
        save_json(new_data, f"{ticker_symbol}.json")
        
        # Pause for the vibes
        time.sleep(1)


    msft_data = load_json("MSFT.json")
    tsla_data = load_json("TSLA.json")

    print(msft_data)
    print(tsla_data)


