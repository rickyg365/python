import os
import datetime

from typing import List, Dict
from dataclasses import dataclass

def parse_seconds(total_seconds: float):
    # Time in hours
    hours = total_seconds//3600
    
    # Time in minutes leftover from conversion to hour
    total_minutes = total_seconds%3600  # 1500
    
    # Full minutes
    minutes = total_minutes//60
    
    # Seconds 
    seconds = total_minutes%60

    return hours, minutes, seconds


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
        time_delta = self.arrival_time - self.departure_time
        total_time = time_delta.total_seconds()
        # Divide by - for 
        # 60 - minutes
        # 60 60 - hours
        # 60 60 24 - days
        self.duration = total_time

    def __str__(self) -> str:
        # Format Time
        date_format = f"%m/%d/%y %I:%M %p"

        d_time = self.departure_time.strftime(date_format)
        a_time = self.arrival_time.strftime(date_format)

        total_hours, total_minutes, total_seconds = parse_seconds(self.duration)

        txt = f"""[{self.airline}] {self.departure.code:^5} -> {self.arrival.code:^5}
>{d_time:^19}  {self.departure.name:^10}
>{a_time:^19}  {self.arrival.name:^10}
Total Duration:  {total_hours:.0f}hr {total_minutes:.0f}min {total_seconds:.0f}sec"""
        return txt

def main():
    # Airport
    sfo_data = {
        "name": "San Francisco",
        "code": "SFO"
    }
    vancouver_data = {
        "name": "Vancouver International Airport",
        "code": "YVR"
    }

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
