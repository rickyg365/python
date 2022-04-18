import os

import datetime

from main import parse_seconds

from main import Airport, Flight

def test_create_airport():
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

    print(sfo)
    print(yvr)
    
    return 

def test_create_flight(airport1, airport2):
    flight_data1 = {
        "airline": "flair airlines",
        "price": 66.15,
        "departure": airport1,
        "arrival": airport2,
        "departure_time": datetime.datetime(year=2022, month=4, day=17, hour=9, minute=15),
        "arrival_time": datetime.datetime(year=2022, month=4, day=17, hour=11, minute=40)
    }

    return Flight(**flight_data1)

def main():
    # Global Variables
    

    # Flight
    flight1 = test_create_flight(sfo, yvr)
    print(flight1)

    return

if __name__ == '__main__':
    main()
