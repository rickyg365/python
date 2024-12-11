import os
import time
import requests
from rich import print as pprint

from dataclasses import dataclass

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
class Alert:
    area_desc: str=None
    sent: str=None
    effective: str=None
    ends: str=None
    status: str=None
    severity: str=None
    certainty: str=None
    urgency: str=None
    event: str=None
    sender_name: str=None
    headline: str=None
    description: str=None
    instructions: str=None

    def __str__(self):
        return f"""
[{self.severity}] - {self.event} - {self.urgency} - {self.certainty}
{self.sender_name} - {self.sent}

START: {self.effective}
END: {self.ends}

{self.area_desc}

[ DETAILS ]
{self.headline}


{self.description}

[ INSTRUCTIONS ]
{self.instructions}

"""
    def from_data(self, raw_data):
        self.area_desc = raw_data.get('areaDesc', None)
        self.sent = raw_data.get('sent', None)
        self.effective = raw_data.get('effective', None)
        self.ends = raw_data.get('ends', None)
        self.status = raw_data.get('status', None)
        self.severity = raw_data.get('severity', None)
        self.certainty = raw_data.get('certainty', None)
        self.urgency = raw_data.get('urgency', None)
        self.event = raw_data.get('event', None)
        self.sender_name = raw_data.get('senderName', None)
        self.headline = raw_data.get('headline', None)
        self.description = raw_data.get('description', None)
        self.instructions = raw_data.get('instructions', None)
        
        return self
            

@dataclass
class Forecast:
    name: str


@dataclass
class HourlyForecast:
    name: str



class WeatherApp:
    BASE_URL = 'https://api.weather.gov/points/'
    ALERT_URL = 'https://api.weather.gov/alerts/active?area='
    def __init__(self, lattitude: float=None, longitude: float=None, state: str=None, city: str=None):
        self.lat = lattitude
        self.lon = longitude

        self.gridx = None
        self.gridy = None
        self.grid_id = None

        self.state = state
        self.city = city

        self.forecast = None
        self.hourly_forecast = None
        self.grid_forecast = None

    def __str__(self):
        txt = f"""[{self.lat:.2f}, {self.lon:.2f}] {self.city}, {self.state}
Hourly: {self.hourly_forecast}
Forecast: {self.forecast}
Grid Forecast: {self.grid_forecast}
{self.gridx} {self.gridy} | {self.grid_id}
"""
        return txt
    
    def get_alerts(self, state: str):
        self.state = state

        r = requests.get(self.ALERT_URL + state)
        if r.status_code != 200:
            print(r)
            return None
        
        raw_data = r.json()

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
        self.lat = lattitude
        self.lon = longitude
        r = requests.get(f"{self.BASE_URL}{lattitude},{longitude}")

        if r.status_code != 200:
            print(r.status_code)
            return None
        
        raw_data = r.json()

        props = raw_data.get('properties')
        if props is None:
            print("something is wrong")

        rel_loc = props['relativeLocation']

        self.grid_id = props['gridId']
        self.gridx = props['gridX']
        self.gridy = props['gridY']

        self.forecast = props['forecast']
        self.hourly_forecast = props['forecastHourly']
        self.grid_forecast = props['forecastGridData']

        self.city = rel_loc['properties']['city']
        self.state = rel_loc['properties']['state']


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

