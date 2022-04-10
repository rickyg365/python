import json
from textwrap import indent
import requests

from typing import Dict, List

"""
Base URL: https://earthquake.usgs.gov/fdsnws/event/1/
Example: https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2014-01-01&endtime=2014-01-02

#* Formats
- csv
- geojson
- text

#* Time [Default]
NOTE: All times use ISO8601 Date/Time format.
- endtime: str [present time], limit to events on or before the specified end time. 
- starttime: str [Now - 30 days], limit to events on or after the specified start time.
- updatedafter: str [null], limits events to after specified time.

#* Location [Default] 
#? Rectangle
- minlatitude: float [-90] 
- minlongitude: float [-180]
- maxlatitude: float [90]
- maxlongitude: float [180]

#? Circle
- latitude: float [null]
- longitude: float [null]
- maxradius: float [180]
- maxradiuskm: float [20001.6]


#* Other
- limit: int [null], Limit the results to the specified number of events.
- mindepth: float [-100], Limit to events with depth more than the specified minimum.
- maxdepth: float [1000], Limit to events with depth less than the specified maximum.
- minmagnitude: float [null], Limit to events with a magnitude larger than the specified minimum.
- maxmagnitude: float [null], Limit to events with a magnitude smaller than the specified maximum.
- eventid: str [null]
- includeallmagnitudes: bool [false]
- includeallorigins: bool [false]
- orderby: str [time], [time] order by origin descending time
                       [time-asc] order by origin ascending time
                       [magnitude] order by descending magnitude
                       [magnitude-asc] order by ascending magnitude


Example: https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2014-01-01&endtime=2014-01-02

"""

def download_eq_data(options: Dict[str, any]):
    """ 
    Options:
    - Format
    - Time
    - Location
    - Other
    """
    valid_params = [
        "format",
        "endtime",
        "starttime",
        "updatedafter",
        "minlatitude",
        "minlongitude",
        "maxlatitude",
        "maxlongitude",
        "latitude",
        "longitude",
        "maxradius",
        "maxradiuskm",
        "limit",
        "mindepth",
        "maxdepth",
        "minmagnitude",
        "maxmagnitude",
        "eventid",
        "includeallmagnitudes",
        "includeallorigins",
        "orderby",
        ]
    base_url = "https://earthquake.usgs.gov/fdsnws/event/1/"
    query = "query?"
    for param_name, param_value in options.items():
        if param_name in valid_params:
            query += f"{param_name}={param_value}&"

    response = requests.get(f"{base_url}{query}")

    raw_json_data = response.json()
    for k, v in raw_json_data.items():
        if type(v) is not list and type(v) is not dict:
            print(k, v)

    # print(raw_json_data)




def main():
    sample_options = {
        "format": "geojson",
        "starttime": "2018-01-01",
        "endtime": "2018-01-02"
    }

    download_eq_data(sample_options)

    return

if __name__ == '__main__':
    main()
