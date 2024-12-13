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
    
    def get_alerts(self, state: str):
        
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

    def get_forecast_data(self, lattitude: float, longitude: float):
        self.api.load_initial_data(lattitude, longitude)

        raw_data1 = self.api.get_forecast()

        forecast_data = raw_data1['properties']['periods']
        forecasts = []

        for f in forecast_data:
            new_forecast = Forecast(**f)
            print(new_forecast)
            forecasts.append(new_forecast)

        # raw_data2 = self.api.get_hourly_forecast()
        # raw_data3 = self.api.get_grid_forecast()

        # return raw_data1, raw_data2, raw_data3


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
    app.get_forecast_data(LATITUDE, LONGITUDE)
    # pprint(f_data)
    print(app)

