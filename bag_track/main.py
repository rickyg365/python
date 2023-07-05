import os

DATABASE = []
SAMPLE_INPUT = {
    "amount": 20.00,
    "date": "05/05/05",
    "days": "1111010",
    "hours": 33
}


AVERAGE_PER_HR = 0
AVERAGE_PER_PERIOD = 0
AVERAGE_HR_PER_WEEK = 0
AVERAGE_DAYS_PER_HR = 0


TOTAL_BAG = 0
TOTAL_HRS = 0
TOTAL_DAYS = 0
TOTAL_WEEKS = 0

CHANCES = {
    "mon": 0,
    "tue": 0,
    "wed": 0,
    "thu": 0,
    "fri": 0,
    "sat": 0,
    "sun": 0,
}


for i, s in enumerate(DATABASE):

    amt = s.get("amount", 0)
    date = s.get("date", "N/A")
    days = s.get("days", "0000000")
    hrs = s.get("hours", 0)

    # Udpate values
    TOTAL_BAG += amt
    TOTAL_HRS += hrs
    TOTAL_DAYS += sum([int(x) for x in list(days)])
    TOTAL_WEEKS += 2


def main():
    return


if __name__ == "__main__":
    main()
