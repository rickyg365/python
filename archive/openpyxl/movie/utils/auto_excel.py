import os

from typing import List
from datetime import datetime

from openpyxl import Workbook, load_workbook

""" 
Program: Move Excel automater
Author: Rickyg3
Date: 03/22/22
"""

def create_workbook(sheet_names: List[str], custom_colors: List[str]=None):    
    # Early Escape Checks
    use_color = False

    if custom_colors is not None and len(custom_colors) == len(sheet_names):
        use_color = True
    else:
        # Can give feedback on error here
        pass

    # Create new workbook
    new_workbook = Workbook()
   
    for _, sheet_name in enumerate(sheet_names):
        new_workbook.create_sheet(sheet_name, _)
        if use_color:
            new_workbook[sheet_name].sheet_properties.tabColor = custom_colors[_]

    return new_workbook

def test_no_color_wb():
    list_of_sheetnames = ["WS A", "WS B", "WS C", "WS D"]

    new_workbook = create_workbook(list_of_sheetnames)
    new_workbook.save("output/no_color_test.xlsx")


def test_color_wb():
    list_of_sheetnames = ["WS A", "WS B", "WS C", "WS D"]
    list_of_colors = ["28536B", "C2948A", "7EA8BE", "28536B"]

    new_workbook = create_workbook(list_of_sheetnames, list_of_colors)
    new_workbook.save("output/color_test.xlsx")


if __name__ == '__main__':
    test_color_wb()
    test_no_color_wb()

