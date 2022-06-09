import pandas as pd

from typing import Dict, List

# External
import yfinance as yf


"""  
# Sample Clean MSFT Data #
{
    "06-07-2022": {
        "entry_id": "MSFT_2022-06-07",
        "open": 266.6400146484375,
        "high": 273.1300048828125,
        "low": 265.94000244140625,
        "close": 272.5,
        "volume": 22838600,
        "dividends": 0,
        "stock_splits": 0
    },
    "06-08-2022": {
        "entry_id": "MSFT_2022-06-08",
        "open": 271.7099914550781,
        "high": 273.0,
        "low": 270.6199951171875,
        "close": 270.9549865722656,
        "volume": 8407756,
        "dividends": 0,
        "stock_splits": 0
    },
    ...
}
"""

def extract_df(ticker_symbol: str, raw_dataframe: pd.DataFrame):
    """ Convert dataframe into a dict, pd.DataFrame -> { date: data } """
    final_data = {}
    all_dates = raw_dataframe.index

    # Iterate Dates
    for date in all_dates:
        # Convert {pd.dataframe Datetime} -> String 
        parsed_date = date.date().strftime("%m-%d-%Y")
        id_date = date.date().strftime("%Y-%m-%d")

        entry_id = f"{ticker_symbol}_{id_date}"
        
        # Add date data for stock as entry in final dict
        final_data[parsed_date] = {
            "entry_id": entry_id,
            "open": float(raw_dataframe['Open'][date]),
            "high": float(raw_dataframe['High'][date]),
            "low": float(raw_dataframe['Low'][date]),
            "close": float(raw_dataframe['Close'][date]),
            "volume": int(raw_dataframe['Volume'][date]),
            "dividends": int(raw_dataframe['Dividends'][date]),
            "stock_splits": int(raw_dataframe['Stock Splits'][date]),
        }
    return final_data

def get_raw_data(ticker_symbol: str, period:str="1d") -> pd.DataFrame:
    """ Download data(Pandas DataFrame) for given Ticker and Number of Days """
    # Return pd.DataFrame
    return yf.Ticker(ticker_symbol).history(period)

# Test Method with toggle
def get_data(ticker_symbol: str, period:str="1d", extract=False) -> pd.DataFrame | Dict[str, any]:
    """ Download data(Pandas DataFrame) for given Ticker and Number of Days """
    raw_data = yf.Ticker(ticker_symbol).history(period)
    if extract:
        # Returns { date: data, ... }
        return extract_df(ticker_symbol, raw_data)
    # Return pd.DataFrame
    return raw_data


