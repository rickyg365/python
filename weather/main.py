import os
import time
import requests
from rich import print as pprint

from dataclasses import dataclass

from models.alert import Alert
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


@dataclass
class Forecast:
    name: str


@dataclass
class HourlyForecast:
    name: str



class WeatherApp:
    def __init__(self, lattitude: float=None, longitude: float=None, state: str=None, city: str=None):
        self.api = WeatherAPI()

    def __str__(self):
        txt = f"""[{self.api.lat:.2f}, {self.api.lon:.2f}] {self.api.city}, {self.api.state}
Hourly: {self.api.hourly_forecast}
Forecast: {self.api.forecast}
Grid Forecast: {self.api.grid_forecast}
{self.api.gridx} {self.api.gridy} | {self.api.grid_id}
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
        raw_data = self.api.get_forecast_data(lattitude, longitude)

        # fixed_data = {
        #     'grid_id': props['gridId'],
        #     'grid_x': props['gridX'],
        #     'grid_y': props['gridY'],
        #     'forecast': props['forecast'],
        #     'forecast_hourly': props['forecastHourly'],
        #     'forecast_grid_data': props['forecastGridData'],
        #     'location': {
        #         'city': rel_loc['properties']['city'],
        #         'state': rel_loc['properties']['state']
        #     }
        # }
        
        return r.json() 





if __name__ == "__main__":
    COLS, ROWS = os.get_terminal_size()
    app = WeatherApp()  

    # a = app.get_alerts("CA")

    # line = f"{'_'*COLS}\n"
    # alerts_string = line.join([f"{alert}" for alert in a])
    # print(alerts_string)

    # time.sleep(1)
    f_data = app.get_forecast_data(34.12555414232492, -118.27979565480962)
    # pprint(f_data)
    print(app)

