import os
import datetime

import logging

from utils.file import compare_date, check_in_logs


# Print Decorator
def print_return(func):
    print("Before inner def")
    def inner(*args, **kwargs):
        # Before func
        print("Before function")

        # During func
        print(func(*args, **kwargs))

        # After Func
        print("After function")
    print("right before inner return")
    return inner


@print_return
def add_xy(x, y):
    return x + y


def main():
    # print("Function is called")
    # add_xy(2, 3)


    # On Start up
    # Get todays date
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # Check if file with todays date exists
    log_exists = check_in_logs(current_date, base_path="logs")

    # log already exist?
    write_mode = 'w'
    if log_exists:
        write_mode = "a"


    # Setup Logging
    config = {
        "filename": f"logs/recent/{current_date.replace('-', '_')}.log",
        "filemode": write_mode,
        "format": '[%(asctime)s] - %(levelname)s - %(message)s',
        "datefmt": '%H:%M:%S',
        "level": logging.DEBUG
    }

    logging.basicConfig(**config)

    # day, month, year = current_date.day, current_date.month, current_date.year

    date_diff = compare_date( "2021-05-22", "2022-03-19")  # Returns diff in days, true if date1 is before date 2

    logging.debug(f"{date_diff}")
    logging.warning("Hi")
    return

if __name__ == '__main__':
    main()
