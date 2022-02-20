import os

import time
import datetime

import yfinance as yf

from typing import List, Dict

from utils.helpers import clean_df_value, date_time_parse, save_json, load_json


class StockData:
    """
    Todo: Log how many are loaded vs. created for the first time
    """
    def __init__(self, ticker_symbol):
        self.file_path = f"{ticker_symbol}.json"
        self.symbol = ticker_symbol

        self.data = {}
        self.keys = None

        self.load_data()
        
    def __str__(self) -> str:
        text = f"[{self.symbol}]"
        for date, obj in self.data.items():
            sub_text=""
            for cat, val in obj.items():
                sub_text += f"\n\t\t{cat}: {val}"
            text += f"\n\t{date}: {sub_text}"
        return text

    def extract_data(self, ticker_data, skip_dates=None):
        # Create new Dict
        cleaned = {}

        # Extract Columns(Should always be the same)
        all_columns = [c for c in ticker_data.columns]
        # Extract all Included dates(sometimes redundant on purpose)
        all_dates = [d for d in ticker_data[all_columns[0]].keys()]

        for date in all_dates:
            new_date = date_time_parse(date)

            if skip_dates is not None and new_date in skip_dates:
                continue
            
            # Create new Object for this dates data
            new_date_data = {}
            for col in all_columns:
                value = ticker_data[col][date]

                # Add data to date dict
                new_date_data[col] = clean_df_value(value)

            # Add date dict to final dict
            cleaned[new_date] = new_date_data

        return cleaned

    def load_data(self):
        # Create new Ticker obj
        current_stock = yf.Ticker(self.symbol)
        
        # Check json for already existing values
        loaded_data = load_json(self.file_path)

        if loaded_data:
            self.keys = [d for d in loaded_data.keys()]
       
        # Get 5 Day DataFrame, in case some are missing
        new_df = current_stock.history('5d')

        # Extract into dict skipping already existing data
        extracted_data = self.extract_data(new_df, self.keys)

        load_length = len(loaded_data)
        extract_length = len(extracted_data)

        print(f"Loaded: {load_length}")
        print(f"Extracted: {extract_length}")

        # Combine Loaded Data and New Data
        self.data = {**loaded_data, **extracted_data}
        
        # Save all data into json
        save_json(self.data, self.file_path)



if __name__ == "__main__":
    my_stocks = [
        "MSFT",
        "TSLA"
    ]
    
    for ticker_symbol in my_stocks:
        # Create new Ticker obj
        current_stock = StockData(ticker_symbol)
        print(current_stock)
        # Pause for the vibes
        time.sleep(.15)


    # msft_data = load_json("MSFT.json")
    # tsla_data = load_json("TSLA.json")

    # print(msft_data)
    # print(tsla_data)


