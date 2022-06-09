import pandas as pd

# External
import yfinance as yf

"""
TBI:
- make function for retrieving single day of data that is more optimized
- Getting the column names is cool for a dynamic database, but 
  im guessing the cost is inefficency, maybe write a version assuming 
  that the column names wont change, that is more optimized/hard coded.

"""
 
def stock_data(ticker_symbol: str, days:str="1d") -> pd.DataFrame:
    """ check Valid entries for days """
    # Get New Dataframe
    new_ticker_data = yf.Ticker(ticker_symbol).history(days)

    return new_ticker_data


def main():
    # Variables
    stock_symbol = "MSFT"
    period = "5d"

    # Get Data
    # new_data = stock_data(stock_symbol) 
    new_data = stock_data(stock_symbol, period)
    
    print(new_data)


if __name__ == "__main__":
    main()