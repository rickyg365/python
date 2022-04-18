import os
import datetime


def create_test_date(date_data, date_format):
    current_time = datetime.datetime(**date_data)

    return current_time.strftime(date_format)


def main():
    # Date Test
    date_format = f"%m/%d/%y %I:%M %p"

    # Date Data    
    date1 = {
        "year": 2022,
        "month": 4,
        "day": 17
    }
    date2 = {
        "year": 2022,
        "month": 4,
        "day": 15,
        "hour": 3
    }
    
    now = create_test_date(date1, date_format)
    past = create_test_date(date2, date_format)

    print(now)
    print(past)


if __name__ == '__main__':
    main()
