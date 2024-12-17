from dataclasses import dataclass
from typing import Dict


"""
1] Today - day

Chance of Precipitation: None %
64 F
5 mph SSW

Start: 2024-12-13T09:00:00-08:00
End: 2024-12-13T18:00:00-08:00

Mostly Sunny
Mostly sunny, with a high near 64. South southwest wind around 5 mph.

"""

class Forecast:
    UNIT_MAP = {
        'percent': '%',
        'degC': 'C',
        'degF': 'F',
        'm': 'm',
    }

    def __init__(self, number: int, name: str, startTime: str, endTime: str, isDaytime: bool, temperature: int, temperatureUnit: str, probabilityOfPrecipitation: str, windSpeed: str, windDirection: str, shortForecast: str, detailedForecast: str, **kwargs):
        self.number: int = number
        self.name: str = name
        self.startTime: str = startTime
        self.endTime: str = endTime
        self.isDaytime: bool = isDaytime
        self.temperature: int = temperature
        self.temperatureUnit: str = temperatureUnit
        self.probabilityOfPrecipitation: str = probabilityOfPrecipitation
        self.windSpeed: str = windSpeed
        self.windDirection: str = windDirection
        self.shortForecast: str = shortForecast
        self.detailedForecast: str = detailedForecast

        self.precipitation = self.extract_unit_val_from_dict(self.probabilityOfPrecipitation)


    def __str__(self):
        day = 'day' if self.isDaytime else 'night'
        return f"""
{self.number}] {self.name} - {self.shortForecast}
{self.temperature} {self.temperatureUnit} | {self.precipitation} | {self.windSpeed} {self.windDirection}

{self.detailedForecast}

Start: {self.startTime}
End: {self.endTime}
"""
    def extract_unit_val_from_dict(self, dictionary: Dict) -> str:
        v = dictionary.get('value', 0)
        raw_unit = dictionary.get('unitCode', ':?')

        u = raw_unit.split(':')[-1]
        unit = self.UNIT_MAP.get(u, u)
        value = 0 if v is None else v        
        return f"{value} {unit}"

@dataclass
class HourlyForecast:
    number: int
    name: str
    startTime: str
    endTime: str
    isDaytime: bool
    temperature: int
    temperatureUnit: str
    probabilityOfPrecipitation: str
    windSpeed: str
    windDirection: str
    shortForecast: str
    detailedForecast: str

    def __post_init__(self):
        unit_map = {
            'percent': '%',
            'degC': 'C',
            'degF': 'F',
            'm': 'm',
        }

        def extract_unit_val_from_dict(dictionary: Dict):
            value = dictionary.get('value', 0)
            raw_unit = dictionary.get('unitCode', ':?')

            u = raw_unit.split(':')[-1]
            unit = unit_map.get(u, u)

            return f"{value} {unit}"

        self.precipitation = extract_unit_val_from_dict(self.probabilityOfPrecipitation)


    def __str__(self):
        day = 'day' if self.isDaytime else 'night'
        return f"""
{self.number}] {self.name} - {day}

Chance of Precipitation: {self.precipitation}
{self.temperature} {self.temperatureUnit}
{self.windSpeed} {self.windDirection}

Start: {self.startTime}
End: {self.endTime}

{self.shortForecast}
{self.detailedForecast}
"""

