import os
import json

import numpy as np
import pandas as pd

import yfinance as yf

from typing import List, Dict


def save(data, filepath):
        with open(filepath, 'w') as out_file:
            json.dump(data, out_file, indent=4)


class App:
    ''' 
    manage ticker data
    can return indv ticker data
    '''
    def __init__(self, tickers: List[str]=None):
        self.metadata = None

        self.init_metadata(tickers)


    def __str__(self) -> str:
        txt = ""
        return txt
    
    def init_metadata(self, new_tickers: List[str]):
        # Load metadata
        meta_path = "data/metadata.json"
        if os.path.exists(meta_path):
            with open(meta_path) as in_data:
                self.metadata = json.load(in_data)

            current_tickers = self.metadata['tickers']
            for ticker in new_tickers:
                if ticker in current_tickers:
                    continue
                current_tickers.append(ticker)
                
        else:
            # Create metadata
            self.metadata = {
                "tickers": new_tickers
            }
    
    def generate_dirs(self):
        """ Generate dirs for metadata tickers if they dont exists """
        current_tickers = self.metadata.get("tickers", [])

        for tick in current_tickers:
            dir_path = f"data/{tick.lower()}"
            if os.path.exists(dir_path):
                continue                
            os.mkdir(dir_path)
            

    def run(self):
        return


def main():
    tick_list = [
        "MSFT",
        "TSLA"
    ]

    # Load metadata
    # metadata = None
    # with open("data/metadata.json") as in_data:
    #     metadata = json.load(in_data)

    # if metadata is None:
    #     # Create metadata
    #     metadata = {
    #         "tickers": []
    #     }

    for ticker in tick_list:
        # Add to Metadata, assuming its a new ticker
        # metadata['tickers'].append(ticker) 

        # New Path, create if folder doesnt exist
        path = f"data/{ticker.lower()}"

        if not os.path.exists(path):
            os.mkdir(path)

        # Get Data
        new_t = yf.Ticker(ticker)
        
        info = new_t.info  # Dict[]
        data = new_t.history('1d').to_json()  # DF
        qtr = new_t.quarterly_financials.to_json()  # DF    

        # Save Data
        save(info, f"{path}/info.json")
        save(data, f"{path}/day.json")
        save(qtr, f"{path}/qtrly.json")

    # Save Metadata
    # save(metadata, "data/metadata.json")

    # new_app = App(tick_list)
    # new_app.run()
    return

if __name__ == '__main__':
    main()
