import os
import requests


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

    def __str__(self):
        return f""
    
    def get_alerts(self, state: str):
        # Set State
        self.state = state

        # Make Request
        r = requests.get(self.ALERT_URL + state)
        
        if r.status_code == 200:
            return r.json()
        
        # Error
        print(r)
        return None
        
    
    def get_forecast(self, grid_id: str=None, grid_x: str=None, grid_y: str=None):
        
        url = self.forecast_url
        if grid_id is not None and grid_x is not None and grid_y is not None:
            url = f"https://api.weather.gov/gridpoints/{grid_id}/{grid_x},{grid_y}/forecast"

        r = requests.get(url)

        if r.status_code == 200:
            return r.json()

        print(r)        
        return None
    
    def get_hourly_forecast(self):
        # Make Request
        r = requests.get(self.hourly_forecast_url)
        
        if r.status_code == 200:
            return r.json()
        
        # Error
        print(r)
        return None
        
    def get_grid_forecast(self):
        # Make Request
        r = requests.get(self.grid_forecast_url)
        
        if r.status_code == 200:
            return r.json()
        
        # Error
        print(r)
        return None
        
    def get_forecast_data(self, latitude: float, longitude: float):
        # Update data
        self.lat = latitude
        self.lon = longitude

        # Make Requests
        r = requests.get(f"{self.BASE_URL}{latitude},{longitude}")

        if r.status_code != 200:
            return

        raw_data = r.json()
    
        props = raw_data.get('properties')
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
        return raw_data
    
    




if __name__ == "__main__":
    ...