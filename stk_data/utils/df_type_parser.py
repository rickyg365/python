import numpy as np


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

def main():
    return

if __name__ == '__main__':
    main()
