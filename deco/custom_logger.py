import os
import datetime

import logging

from utils.file import compare_date


def check_in_logs(target_filepath: str):
    try:
        if os.path.isfile(target_filepath):
            return True
    except Exception as e:
        print(e)
    return False


def main():
    # On Start up
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    filename = f"logs/recent/{current_date.replace('-', '_')}.log"
    
    
    # Check if file with todays date exists
    log_exists = check_in_logs(filename)

    # log already exist?
    write_mode = 'w'
    if log_exists:
        print("apend")
        write_mode = "a"


    # Setup Logging
    
    config = {
        "filename": filename,
        "filemode": write_mode,
        "format": '[%(asctime)s] - %(levelname)s - %(message)s',
        "datefmt": '%H:%M:%S',
        "level": logging.DEBUG
    }

    logging.basicConfig(**config)

 
    date_diff = compare_date( "2021-05-22", "2022-03-19")  # Returns diff in days, true if date1 is before date 2

    logging.debug(f"{date_diff}")
    logging.warning("Hi")
    return

if __name__ == '__main__':
    main()
