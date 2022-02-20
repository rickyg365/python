import os
import json

import pandas as pd
import yfinance as yf

from data import StockData



def explore_dataframe():
    main_df = yf.Ticker("MSFT").history('5d')

    # Equivilant oooooop
    keys = main_df.keys()
    columns = main_df.columns

    parsed_data = {}

    all_columns = [c for c in main_df.columns]
    all_dates = [d for d in main_df[all_columns[0]].keys()]

    for date in all_dates:
        new_date_data = {}
        for col in all_columns:
            value = main_df[col][date]
            new_date_data[col] = value
    parsed_data[f"{date}"] = new_date_data
    print(parsed_data)
    print(len(parsed_data))

    return



def main():
    explore_dataframe()
    return

if __name__ == "__main__":
    main()

