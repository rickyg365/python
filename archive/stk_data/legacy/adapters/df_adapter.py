import os

import numpy as np
import pandas as pd

from typing import Dict, List


# def clean_dataframe_value(raw_data):
#     """ Converts raw df value from numpy to standard python ints and floats """
#     parsed_data = raw_data
#     # Parsing
#     match type(raw_data):
#         case np.int64:
#             parsed_data = int(raw_data)
#         case np.float64:
#             parsed_data = float(raw_data)
#         case _:
#             pass
#     return parsed_data

def stock_df_to_list(ticker_symbol:str, input_data: pd.DataFrame) ->  Dict[str, any]:
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
    final_data = []
    all_dates = input_data.index

    # Iterate Dates
    for date in all_dates:
        # Convert to String (raw obj is datetime obj from pd.dataframe)
        new_date = date.date().strftime("%m-%d-%Y")
        
        cleaned_date_data = {
            "ticker_symbol": ticker_symbol,
            "date": new_date,
            "open": float(input_data['Open'][date]),
            "high": float(input_data['High'][date]),
            "low": float(input_data['Low'][date]),
            "close": float(input_data['Close'][date]),
            "volume": int(input_data['Volume'][date]),
            "dividends": int(input_data['Dividends'][date]),
            "stock_splits": int(input_data['Stock Splits'][date]),
        }

        # Add stock to final list
        final_data.append(cleaned_date_data)
 
    return final_data


def main():
    return

if __name__ == '__main__':
    main()
