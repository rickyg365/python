import os
import json

import datetime
import numpy as np


def date_time_parse(raw_datetime: datetime.datetime) -> str:
    # new_dt = datetime.datetime(raw_string)
    return raw_datetime.date().strftime("%m-%d-%Y")


def clean_df_value(raw_data):
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


def save_json(data, filepath="default.json"):
    filepath = f"data/{filepath}"
    try:
        with open(filepath, 'w') as out_json:
            json.dump(data, out_json, indent=4, separators=(',', ': '))
    except Exception as e:
        print(e)

def load_json(filepath="default.json"):
    filepath = f"data/{filepath}"
    new_data = None
    try:
        with open(filepath, 'r') as in_json:
            new_data = json.load(in_json)
    except FileNotFoundError:
        new_data = {}
    return new_data





