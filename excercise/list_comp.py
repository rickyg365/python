import os
import random

from enum import Enum

from typing import List, Dict
from dataclasses import dataclass, field


# Enums
class TemperatureUnit(Enum):
    celsius = "C"
    fahrenheit = "F"

# Object
@dataclass
class Temperature:
    value: float
    unit: TemperatureUnit
    
    def __str__(self) -> str:
        txt = f"{self.value}{self.unit.value}"
        return txt

# Functions
def convert_celsius_fahrenheit(celsius_temp: float):
    """ Celsius to Fahrenheit """
    return (celsius_temp/(5/9)) + 32


def convert_fahrenheit_celsius(fahrenheit_temp: float):
    """ Fahrenheit to Celsius """ 
    return (fahrenheit_temp - 32) * 5/9


def generate_random_temp():
    u_num = random.randint(1, 100)
    unit = TemperatureUnit.fahrenheit if u_num <= 50 else TemperatureUnit.celsius
    
    temp_value = random.randint(30, 212)
    return Temperature(temp_value, unit)

def generate_random_list(list_length: int):
    return [generate_random_temp() for _ in range(list_length)]




class PriorityQueue:
    '''
    Rank: Where to insert
    Count: How many copies currently
    Position: Current Position
    '''
    def __init__(self):
        self.data = []  # Should be sorted
        self.counter = {}
        

# Main Loop
def main():
    # Test Unit Conversion

    # Temperature Object
    new_temperature = Temperature(90, TemperatureUnit.fahrenheit)
    print(new_temperature)

    # Generate List
    new_list = generate_random_list(5)
    # print(new_list)
    for item in new_list:
        print(item)

   


if __name__ == '__main__':
    main()
