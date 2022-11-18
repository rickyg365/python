import os
import datetime

from typing import List, Dict
from dataclasses import dataclass

def split_time(raw_total, factor):
    """ Lmao is this just the divmod func thats built in, that one is 100% implemented bettter lmao """
    return raw_total//factor, raw_total%factor

def parse_seconds(total_seconds: float):
    # Defaults
    seconds_per_hour = 60 * 60
    seconds_per_day = seconds_per_hour * 24

    day = 0
    hour = 0
    minute = 0
    seconds = 0

    #! Method 1 - Floor Division and Modulus Operator
    # # Full Days, Time left in seconds
    # days, time_left = total_seconds//seconds_per_day, total_seconds%seconds_per_day

    # # Full hours
    # hours, total_minutes = time_left//seconds_per_hour, time_left%seconds_per_hour

    # # Full minutes
    # minutes, seconds = total_minutes//60, total_minutes%60

    #! Method 2 - DivMod
    # Full Days, Time left in seconds
    days, time_left = divmod(total_seconds, seconds_per_day)

    # Full hours, Time left in seconds
    hours, total_minutes = divmod(time_left,seconds_per_hour)

    # Full minutes, Time left in seconds
    minutes, seconds = divmod(total_minutes, 60)


    #! Method 3 - Custom Function
    # days, time_left = split_time(total_seconds, seconds_per_day)
    # hours, time_left = split_time(time_left, seconds_per_hour)
    # minutes, seconds = split_time(time_left, 60)  # seconds per minute

    return days, hours, minutes, seconds


@dataclass
class Airport:
    name: str
    code: str

@dataclass
class Flight:
    airline: str
    price: float

    departure: Airport
    departure_time: datetime.datetime
    
    arrival: Airport
    arrival_time: datetime.datetime

    def __post_init__(self):
        # Difference between arrival and departure time
        time_delta = self.arrival_time - self.departure_time

        # Convert time delta into total seconds
        self.duration = time_delta.total_seconds()

    def __str__(self) -> str:
        # Format Time
        date_format = f"%m/%d/%y %I:%M %p"

        d_time = self.departure_time.strftime(date_format)
        a_time = self.arrival_time.strftime(date_format)

        total_days, total_hours, total_minutes, total_seconds = parse_seconds(self.duration)

        txt = f"""\n[ {self.airline} ]: {self.departure.code:^5} -> {self.arrival.code:^5}
{'-'*60}
[{d_time:^17}]  {self.departure.name:^10}
[{a_time:^17}]  {self.arrival.name:^10}
{'-'*60}
Total Duration:  {total_hours:.0f}hr {total_minutes:.0f}min {total_seconds:.0f}sec"""
        return txt

def main():
    # Airport Data
    sfo_data = {
        "name": "San Francisco",
        "code": "SFO"
    }
    vancouver_data = {
        "name": "Vancouver International Airport",
        "code": "YVR"
    }

    # Airport Objects
    sfo = Airport(**sfo_data)
    yvr = Airport(**vancouver_data)

    # Flight
    flight_data1 = {
        "airline": "flair airlines",
        "price": 66.15,
        "departure": sfo,
        "arrival": yvr,
        "departure_time": datetime.datetime(year=2022, month=4, day=17, hour=9, minute=15),
        "arrival_time": datetime.datetime(year=2022, month=4, day=17, hour=11, minute=40)
    }

    flight1 = Flight(**flight_data1)
    print(flight1)


if __name__ == '__main__':
    main()
