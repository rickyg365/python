import os
import requests
from rich import print


class WeatherAPI:
    BASE_URL = 'https://api.weather.gov/points/'
    ALERT_URL = 'https://api.weather.gov/alerts/active?area='
    
    def __init__(self):
        self.lat = None
        self.lon = None

        self.city = None
        self.state = None

        self.grid_x = None
        self.grid_y = None
        self.grid_id = None

        self.forecast_url = None
        self.hourly_forecast_url = None
        self.grid_forecast_url = None

        self.forecast_data = None
        self.hourly_forecast_data = None
        self.grid_forecast_data = None

        self.has_data = False

    def __str__(self):
        return f"""
lat: {self.lat}
lon: {self.lon}
city: {self.city}
state: {self.state}
grid_x: {self.grid_x}
grid_y: {self.grid_y}
grid_id: {self.grid_id}
forecast_url: {self.forecast_url}
hourly_forecast_url: {self.hourly_forecast_url}
grid_forecast_url: {self.grid_forecast_url}        
"""

    def export(self):
        return {
            "lat": self.lat,
            "lon": self.lon,
            "city": self.city,
            "state": self.state,
            "grid_x": self.grid_x,
            "grid_y": self.grid_y,
            "grid_id": self.grid_id,
            "forecast_url": self.forecast_url,
            "hourly_forecast_url": self.hourly_forecast_url,
            "grid_forecast_url": self.grid_forecast_url,
        }

    def make_request(self, url: str):
        r = requests.get(url)

        if r.status_code == 200:
            return r.json()

        # Error
        print(r)
        return None

    
    def get_alerts(self, state: str=None):
        # Set State
        if state is not None:
            self.state = state
        
        if self.state is None:
            return

        # Make Request
        raw_data = self.make_request(self.ALERT_URL + state)
        return raw_data
        
    
    def get_forecast(self, grid_id: str=None, grid_x: str=None, grid_y: str=None):
        url = self.forecast_url
        if grid_id is not None and grid_x is not None and grid_y is not None:
            url = f"https://api.weather.gov/gridpoints/{grid_id}/{grid_x},{grid_y}/forecast"

        self.forecast_data = self.make_request(url)
        return self.forecast_data
    
    def get_hourly_forecast(self):
        # Make Request
        self.hourly_forecast_data = self.make_request(self.hourly_forecast_url)
        return self.hourly_forecast_data
        
    def get_grid_forecast(self):
        # Make Request
        self.grid_forecast_data = self.make_request(self.grid_forecast_url)
        return self.grid_forecast_data
        
    def load_initial_data(self, latitude: float, longitude: float):
        # Update data
        self.lat = latitude
        self.lon = longitude

        # Make Requests
        raw_data = self.make_request(f"{self.BASE_URL}{latitude},{longitude}")

        props = raw_data.get('properties', None)
        if props is None:
            print("something is wrong")
            return

        rel_loc = props['relativeLocation']

        self.grid_id = props['gridId']
        self.grid_x = props['gridX']
        self.grid_y = props['gridY']

        self.forecast_url = props['forecast']
        self.hourly_forecast_url = props['forecastHourly']
        self.grid_forecast_url = props['forecastGridData']

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
        
        self.has_data = True
        return raw_data
    
    




if __name__ == "__main__":    
    LATITUDE = 34.12555414232492
    LONGITUDE = -118.27979565480962

    api = WeatherAPI()
    api.load_initial_data(LATITUDE, LONGITUDE)

    # Forecast
    # f_data = api.get_forecast()
    # print(f_data)

    # Hourly Forecast
    h_data = api.get_hourly_forecast()
    print(h_data)

    # Grid Forecast
    # g_data = api.get_grid_forecast()
    # print(g_data)

