import os
import json

import numpy as np
import pandas as pd

import yfinance as yf


"""
metadata
{
    tickers: [],
}


Sample Data - Choose Ticker
# TICKER_SYMBOL
{
    "mm-dd-yyyy": {
        "open": int,
        "high": int,
        "low": int,
        "close": int,
        "volume": int,
        "dividends": int,
        "stock_splits": int
    },
    ...
}




"""

def save_data(data, filepath):
    with open(filepath, 'w') as out_file:
        json.dump(data, out_file, indent=4)


def create_dir(dir_path: str):
    """ if dir doesnt exist create it """
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)


def main():
    # Load Metadata
    metadata = None
    with open("data/metadata.json", 'r') as in_file:
        metadata = json.load(in_file)

    tickers = metadata.get("tickers", None)
    tick = tickers[0]
    basepath = f"data/{tick.lower()}"
    create_dir(basepath)

    msft = yf.Ticker(tick)

    new_data = msft.news

    print(new_data)

    # Save Dataframe
    # save_data(new_data.to_json(), "data/msft/msft_qrtly.json")

    # Save if not a dataframe
    # save_data(new_data, "data/msft/msft_info.json")
    
    
    # Download Data
    t = yf.Ticker(tick).history('5d')  # Good for Ticker object
    
    # Good for Ticker Data w/out all the extra stuff
    d = yf.download(
        tickers=tick,
        period="5d"
        )

    print(t)
    print(d)
    
    # Save Metadata
    # metadata = {
    #     "tickers": [tick]
    # }

    # save_data(metadata, "data/metadata.json")

    return

if __name__ == '__main__':
    main()
