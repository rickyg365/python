import os
import pandas as pd

from typing import List

# External
import yfinance as yf

# Models
from models.stock import Stock

# Utils
from utils.df_type_parser import clean_dataframe_value


def convert_df_to_list(ticker_symbol:str, input_data: pd.DataFrame) -> Stock:
    """ Convert dataframe into a list of dicts, seperating stock by date """
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
            key = f"{col}".strip().replace(" ", "_").lower()
            value = input_data[col][date]

            # Parse value from numpy into standard python obj
            cleaned_value = clean_dataframe_value(value)

            # Add Parsed value to dict
            new_data[key] = cleaned_value
            #! DEBUG
            #! print(f"{col}: {type(cleaned_value)}")
        # Add stock to final list
        stocks.append(Stock(ticker_symbol, new_date, **new_data))
    return stocks


def get_data(ticker_symbol: str, days:str="1d") -> List[Stock]:
    # Get New Dataframe
    new_ticker_data = yf.Ticker(ticker_symbol).history(days)

    # Extract Data
    new_stocks = convert_df_to_list(ticker_symbol, new_ticker_data)

    return new_stocks

def main():
    # new_data = get_data("TSLA", "5d") 
    # print(get_data("MSFT"))
    # print(new_data)
    # print(new_data[0].export())
    return

if __name__ == "__main__":
    main()