import os

import time
import datetime

import pandas as pd

from utils.load_save import save_json

from models.stock import Stock
from source.yahoo import get_raw_data, get_data, extract_df

        
def main():
    # Variables
    stock_symbol = "MSFT"
    period = "5d"

    # Get Data, (stock_symbol, period) -> pd.DataFrame
    new_data = get_raw_data(stock_symbol, period)  # pd.DataFrame
    
    # Extract data, pd.DataFrame -> { date: data }
    extracted_data = extract_df(stock_symbol, new_data)  # { date: data }
    
    # Convert Data into Model, { date: data } -> Stock(**data)
    modeled_data = [Stock(**data) for data in extracted_data.values()]  # [Stock(**data)]

    # Save data, ({ date: data }, filepath) -> output file
    save_json(extracted_data, f"{stock_symbol}.json")

    # Display Data
    print(f"""
Pandas Dataframe
{40*'-'}
{new_data}
{40*'-'}


Extracted Data
{40*'-'}
{extracted_data}
{40*'-'}


Modeled Data
{40*'-'}
{modeled_data}    
{40*'-'}

""")


if __name__ == '__main__':
    main()
