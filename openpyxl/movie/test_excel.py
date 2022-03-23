import os

from utils.auto_excel import create_workbook


def test_no_color_wb():
    list_of_sheetnames = ["WS A", "WS B", "WS C", "WS D"]

    new_workbook = create_workbook(list_of_sheetnames)
    new_workbook.save("output/test_output/no_color_test.xlsx")


def test_color_wb():
    list_of_sheetnames = ["WS A", "WS B", "WS C", "WS D"]
    list_of_colors = ["28536B", "C2948A", "7EA8BE", "28536B"]

    new_workbook = create_workbook(list_of_sheetnames, list_of_colors)
    new_workbook.save("output/test_output/color_test.xlsx")


if __name__ == '__main__':
    test_color_wb()
    test_no_color_wb()

