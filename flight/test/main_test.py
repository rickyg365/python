import os

# Models
from models.flight import Flight
from models.airport import Airport

# Helper
from utils.load_save import load, save
from utils.helper import parse_seconds


""" 
Airport Test
- Object Creation
- Object Parser

Flight Test
- Object Creation
- Object Parser

Utils Test
1. helper
    - parse_seconds

2. load_save
    - Load
    - Save

"""

def test_create_airport():
    # Airport
    test_airport_data = load("data/test_data/airport.json")

    cleaned_data = []
    for data_point in test_airport_data:
        cleaned_data.append(Airport(**data_point))
        print(cleaned_data)
    return True

def test_create_flight(airport1, airport2):
    test_flight_data = load("data/test_data/flight.json")

    data_point = Flight(**test_flight_data)
    print(data_point)
    return True

def main():
    return

if __name__ == '__main__':
    main()
