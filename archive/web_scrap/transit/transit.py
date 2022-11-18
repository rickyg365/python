import os

from utils.utility import get_data, move_file

"""
Author: rickyg3
Program: Get Transit Data
"""


def main():
    # move_file("test.txt")
    new_data_path = "data/bears/"
    get_data("bear_gtfs.zip", new_data_path)

if __name__ == '__main__':
    main()

