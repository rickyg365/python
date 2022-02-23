import os
import json

from stock_object import Stock


def save_data(filepath, data):
    
    with open(filepath, 'w') as out_json:
        json.dump(data , out_json, indent=4)
    return

def load_data(filepath):
    # Loaded stocks
    if os.path.isfile(filepath):
        # Read in File    
        with open(filepath, 'r') as in_json:
            new_data = json.load(in_json)
        
        # Parse Data
        output_data = []

        for stock in new_data:
            # Spread Data
            ticker_symbol = stock['ticker_symbol']
            new_date = stock['date']
            new_data = { **stock }

            output_data.append(Stock(ticker_symbol, new_date, new_data))
        return output_data

    return None
