
import datetime

import numpy as np
import pandas as pd

from typing import Dict, List

"""

"""

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

def stock_df_to_dict(ticker_symbol:str, input_data: pd.DataFrame) ->  Dict[str, any]:
    """ Convert dataframe into a list of dicts, seperating stock by date """
    '''  # Sample Output #
    {
        'symbol': 'TSLA', 
        'data': {
            '05-11-2022': {
                'open': 795.0, 
                'high': 809.77001953125, 
                'low': 727.2000122070312, 
                'close': 734.0, 
                'volume': 32408200, 
                'dividends': 0, 
                'stock_splits': 0
            }, 
            '05-12-2022': {
                'open': 701.0, 
                'high': 759.6599731445312, 
                'low': 680.0, 
                'close': 728.0, 
                'volume': 46771000, 
                'dividends': 0, 
                'stock_splits': 0
            },
            ...
        }
    }
    '''
    output = { "symbol": ticker_symbol, "data": None }
    # Extract Columns(Should always be the same)
    all_columns = [c for c in input_data.columns]
    # Extract all Included dates(sometimes only a single date)
    all_dates = [d for d in input_data[all_columns[0]].keys()]

    # Iterate Dates
    new_data = {}
    for date in all_dates:
        # Convert to String (raw obj is datetime obj from pd.dataframe)
        new_date = date.date().strftime("%m-%d-%Y")

        current_date_data = {}
        # Iterate columns (Open, High, Close...) can hard code this 
        # if we assume these will remain the same in the forseable future
        for col in all_columns:
            # Raw Value
            key = f"{col}".strip().replace(" ", "_").lower()
            value = input_data[col][date]

            # Parse value from numpy into standard python obj
            cleaned_value = clean_dataframe_value(value)

            # Add Parsed value to dict
            current_date_data[key] = cleaned_value
            #! DEBUG
            #! print(f"{col}: {type(cleaned_value)}")
        
        # Add stock to final list
        new_data[new_date] = current_date_data
    output["data"] = new_data

    return output

def ticker_dict_to_object_list(ticker_dict: Dict[str, any]):
    cleaned_data = []
    ticker_symbol = ticker_dict.get("symbol")
    ticker_data = ticker_dict.get('data')  # Dict

    for date, date_data in ticker_data.items():

        cleaned_date_data = {            
            "ticker_symbol": ticker_symbol,
            "date": date,
            "open": date_data.get('open'),
            "high": date_data.get('high'),
            "low": date_data.get('low'),
            "close": date_data.get('close'),
            "volume": date_data.get('volume'),
            "dividends": date_data.get('dividends'),
            "stock_splits": date_data.get('stock_splits'),
        }

        cleaned_data.append(cleaned_date_data)

    return cleaned_data


def main():
    # new_data = pd.DataFrame()    
    # Extract Data
    # ticker_data = stock_df_to_dict(stock_symbol, new_data)
    # new_stocks = ticker_dict_to_object_list(ticker_data)
    return

if __name__ == '__main__':
    main()
