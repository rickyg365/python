import datetime

# Models
from models.flight import Flight
from models.airport import Airport

# Views
# from views.flight_view import FullDetailView, SimplifiedView

# Custom
from utils.load_save import load, save


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

    # save(flight1.to_dict(), "data/flight.json")


if __name__ == '__main__':
    main()
