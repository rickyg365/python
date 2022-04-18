import datetime
from dataclasses import dataclass

# Models
from models.airport import Airport

# Custom Functions
from utils.helper import parse_seconds


"""  

"""


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
    
    def to_dict(self):
        datetime_format = f"%m/%d/%y %I:%M %p"

        new_dict = {
            "airline": self.airline,
            "price": self.price,
            "departure": self.departure.to_dict(),
            "departure_time": self.departure_time.strftime(datetime_format),
            "arrival": self.arrival.to_dict(),
            "arrival_time": self.arrival_time.strftime(datetime_format)
        }
        
        return new_dict

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
