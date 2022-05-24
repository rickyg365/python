import os

def compare_date(date_str1: str, date_str2: str) -> int:
    """ date_str = '2022-05-23' """
    year1, month1, day1 = map(int, date_str1.split('-'))
    year2, month2, day2 = map(int, date_str2.split('-'))

    # Differences
    # year_delta = year2 - year1
    # month_delta = month2 - month1
    # day_delta = day2 - day1
    
    # print(f"{day_delta} days | {month_delta} months | {year_delta} years")
   
    # Add weights to coeficients 
    total_days = 365*(year2 - year1) + 30*(month2 - month1) + (day2 - day1)
    # Total days = 1*day_delta + 30*month_delta + 365*year_delta

    print(f"Total Days: {total_days}")
    return total_days



def main():
    return

if __name__ == '__main__':
    main()
