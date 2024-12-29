import os
import time
import requests
from rich import print as pprint

from dataclasses import dataclass

from models.alert import Alert
from models.forecast import Forecast, HourlyForecast
from weather_wrapper import WeatherAPI



"""
Goal:
Waether api wrapper
weather App Interface




Forecast data from Lat, Lon
https://api.weather.gov/points/{latitude},{longitude}
    forecast - forecast for 12h periods over the next seven days
    forecastHourly - forecast for hourly periods over the next seven days
    forecastGridData - raw forecast data over the next seven days


Detailed Forecast
https://api.weather.gov/gridpoints/{office}/{gridX},{gridY}/forecast


Alerts
https://api.weather.gov/alerts/active?area={state}




__________________________________________________________________________________________________
[Moderate] - Beach Hazards Statement - Expected - Likely
AREAS: Coastal Del Norte; Northern Humboldt Coast; Southwestern Humboldt
NWS Eureka CA - 2024-12-09T20:39:00-08:00

START: 2024-12-09T20:39:00-08:00
END: 2024-12-11T12:00:00-08:00
____________________________________________________________________________________________________
Beach Hazards Statement issued December 9 at 8:39PM PST until December 11 at 12:00PM PST by NWS Eureka CA

Description:
* WHAT...Increased threat of sneaker waves expected.

* WHERE...Coastal Del Norte, Northern Humboldt Coast and
Southwestern Humboldt Counties.

* WHEN...From 5 AM PST Tuesday through Wednesday morning. .

* IMPACTS...Large, unexpected waves can sweep across the beach
without warning, sweeping people into the sea from rocks,
jetties, and beaches. These sneaker waves can also move large
objects such as logs, crushing anyone caught underneath.


Instructions:
None

_____________________________________________________________________________________________________
"""




class WeatherApp:
    def __init__(self, lattitude: float=None, longitude: float=None, state: str=None, city: str=None):
        self.api = WeatherAPI()
        self.forecasts = None
        self.hourly_forecasts = None
        self.location_loaded = False

    def __str__(self):
        if not self.api.has_data:
            return f"No Data"
            
        txt = f"""[{self.api.lat:.2f}, {self.api.lon:.2f}] {self.api.city}, {self.api.state}
{self.api.grid_x} {self.api.grid_y} | {self.api.grid_id}
Hourly: {self.api.hourly_forecast_url}
Forecast: {self.api.forecast_url}
Grid Forecast: {self.api.grid_forecast_url}
"""
        return txt

    def load_location(self, latitude: float, longitude: float):
        self.location_loaded = True
        self.api.load_initial_data(latitude=latitude, longitude=longitude)
    
    def get_alerts(self, state: str=None):
        if state is None and self.location_loaded:
            state = self.api.state
        
        raw_data = self.api.get_alerts(state)

        fixed_data = []
        print(raw_data['title'])
        for feature in raw_data['features']:
            props = feature.get('properties', None)
            if props is None:
                print("something is wrong")
                continue
            new_alert = Alert().from_data(props)
            fixed_data.append(new_alert)

        return fixed_data

    def get_forecast_data(self, lattitude: float=None, longitude: float=None):
        if not self.location_loaded and lattitude is not None:
            self.load_location(lattitude, longitude)

        raw_data1 = self.api.get_forecast()

        forecast_data = raw_data1['properties']['periods']
        self.forecasts = []

        for f in forecast_data:
            new_forecast = Forecast(**f)
            self.forecasts.append(new_forecast)            

        return raw_data1

    def get_hourly_forecast_data(self):
        if not self.location_loaded:
            return
        
        self.hourly_forecasts = []
        raw_data = self.api.get_hourly_forecast()

        
        forecast_data = raw_data['properties']['periods']

        for f in forecast_data:
            new_forecast = HourlyForecast(**f)
            self.hourly_forecasts.append(new_forecast)

        return raw_data

    def show_forecast(self, amount: int=None):
        if amount is None:
            amount = len(self.forecasts)

        for _ in range(amount):
            forecast = self.forecasts[_]
            print(forecast)

        return

    def show_hourly(self, amount: int=None):
        if amount is None:
            amount = len(self.hourly_forecasts)

        for _ in range(amount):
            forecast = self.hourly_forecasts[_]
            print(forecast)

        return

if __name__ == "__main__":
    COLS, ROWS = os.get_terminal_size()

    LATITUDE = 34.12555414232492
    LONGITUDE = -118.27979565480962

    app = WeatherApp()  

    # a = app.get_alerts("CA")

    # line = f"{'_'*COLS}\n"
    # alerts_string = line.join([f"{alert}" for alert in a])
    # print(alerts_string)

    # time.sleep(1)
    
    app.load_location(LATITUDE, LONGITUDE)
    
    app.get_forecast_data()
    # app.get_forecast_data(LATITUDE, LONGITUDE)
    # pprint(f_data)
    print(app)

    print(f"Forecasts:")
    app.show_forecast(2)

    hd = app.get_hourly_forecast_data()    

    print("Hourly Forecasts:")
    app.show_hourly()


