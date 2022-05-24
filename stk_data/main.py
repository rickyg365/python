import os
import pandas as pd

from typing import List

# Models
from models.stock import Stock

# Data Fetchers
from fetcher.yahoo_finance import stock_data

# Adapters
from adapters.df_adapter import stock_df_to_list
# from adapters.stock_data_adapters import stock_df_to_dict, ticker_dict_to_object_list

# Utils

""" 
Stock Model flattens the raw data we get!
"""


def main():
    # symbol = "^GSPC"
    symbol = "^IXIC"
    new_data = stock_data(symbol, "5d")

    print("\nNew: ")
    print(new_data)
    
    # Method #1 - Hard Coded Data
    extracted_data = stock_df_to_list(symbol, new_data)
    print(extracted_data)

    new_stock_data = [Stock(**data) for data in extracted_data]
    for stock in new_stock_data:
        print(stock)
    

    # Method #2 - Adaptable column and index, more complex not necessarily better
    # First layer of extraction/parsing, 
    # I guess tiny bit better for storage but not worth?
    # save_data = stock_df_to_dict(symbol, new_data)

    # print("\nAdapted: ")
    # print(save_data)


    # parsed_data = ticker_dict_to_object_list(save_data)

    # print("\nParsed: ")
    # print(parsed_data)

    # final_data = []
    # for raw_obj_dict in parsed_data:
    #     final_data.append(Stock(**raw_obj_dict))

    # print("\nFinal: ")
    # print(final_data)

    # print("\nStocks: ")
    # for stock in final_data:
    #     print(stock)


if __name__ == '__main__':
    main()
