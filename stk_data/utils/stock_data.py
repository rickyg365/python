import datetime

import numpy as np
import pandas as pd

import yfinance as yf
from typing import List, Dict

from utils.stock_object import Stock


def clean_dataframe_value(raw_data):
    """ Converts raw df value from numpy to standard python ints and floats """
    parsed_data = raw_data
    # Parsing
    match type(raw_data):
        case np.int64:
            parsed_data = int(raw_data)
        case np.float64:
            parsed_data = float(raw_data)
        case _:
            pass
    return parsed_data


def extract_data(ticker_symbol:str, input_data: pd.DataFrame) -> Stock:
    stocks = []
    # Extract Columns(Should always be the same)
    all_columns = [c for c in input_data.columns]
    # Extract all Included dates(sometimes redundant on purpose)
    all_dates = [d for d in input_data[all_columns[0]].keys()]

    for date in all_dates:
        # Convert to String (raw obj is datetime obj from pd.dataframe)
        new_date = date.date().strftime("%m-%d-%Y")

        new_data = {}
        # Iterate columns (Open, High, Close...)
        for col in all_columns:
            # Raw Value
            value = input_data[col][date]

            # Parse
            cleaned_value = clean_dataframe_value(value)

            # Add Parsed value to dict
            new_data[col] = cleaned_value
            #! DEBUG
            #! print(f"{col}: {type(cleaned_value)}")
        # Add stock to final list
        stocks.append(Stock(ticker_symbol, new_date, new_data))
    return stocks


def get_data(ticker_symbol: str, days:str="1d") -> List[Stock]:
    # Get New Dataframe
    new_ticker_data = yf.Ticker(ticker_symbol).history(days)

    # Extract Data
    new_stocks = extract_data(ticker_symbol, new_ticker_data)

    return new_stocks

def main():
    # new_data = get_data("TSLA", "5d") 
    # print(get_data("MSFT"))
    # print(new_data)
    # print(new_data[0].export())
    return

if __name__ == "__main__":
    main()


