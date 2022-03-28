import os

import json

from typing import List, Dict
from dataclasses import dataclass

from model import PeriodicElement

from view import Display

# Parsing Variables
key_map = {
    "AtomicNumber": "atomic_number",
    "Symbol": "symbol",
    "Name": "name",
    "AtomicMass": "atomic_mass",
    "CPKHexColor": "cpk_hex_color",
    "ElectronConfiguration": "electron_configuration",
    "Electronegativity": "electro_negativity",
    "AtomicRadius": "atomic_radius",
    "IonizationEnergy": "ionization_energy",
    "ElectronAffinity": "electron_affinity",
    "OxidationStates": "oxidation_states",
    "StandardState": "standard_state",
    "MeltingPoint": "melting_point",
    "BoilingPoint": "boiling_point",
    "Density": "density",
    "GroupBlock": "chemical_group_block",
    "YearDiscovered": "year_discovered"
}

convert_float = lambda x: float(x)
convert_int = lambda x: int(x)

parsing_map = {
    "AtomicNumber": lambda x: int(x),
    "AtomicMass": lambda x: float(x),
    "Electronegativity": lambda x: float(x),
    "Density": lambda x: float(x),
    "AtomicRadius": lambda x: int(x),
    "IonizationEnergy": lambda x: float(x),
    "ElectronAffinity": lambda x: float(x),
    "MeltingPoint": lambda x: float(x),
    "BoilingPoint": lambda x: float(x),
    "YearDiscovered": lambda x: int(x) if x != 'Ancient' else x
}


def load_periodic_data(file_name: str="periodic_data.json"):
    # Open file and load into dict
    with open(file_name, 'r') as in_json:
        new_data = json.load(in_json)

    output_data = {}
    # Attribute Names
    data_points = new_data['Table']['Columns']['Column']
    table_data = new_data['Table']['Row']

    # list of objects
    for raw_entry in table_data:
        current_data = raw_entry['Cell']
        # Each Element
        cleaned_data = {}

        for _, value in enumerate(current_data):
            # Match column name and data value
            key = data_points[_]

            # Parse Value
            if key in parsing_map and value != '':
                value = parsing_map[key](value)

            # Edit Key
            if key in key_map:
                key = key_map[key]
            
            cleaned_data[key] = value
        
        output_data[cleaned_data['name'].lower()] = cleaned_data
    
    return output_data


def main():
    # Partial Data Element
    hydrogen_basic_data = {
        "name": "Hydrogen",
        "symbol": "H",
        "atomic_number": 1,
        "atomic_mass": 1.0080
    }
    hydrogen_element = PeriodicElement(**hydrogen_basic_data)
    print(hydrogen_element)

    # Load all periodic data
    filename = "periodic_data.json"
    all_data = load_periodic_data(filename)

    # Get Hydrogen data
    hydrogen_data = all_data['hydrogen']
    # print(hydrogen_data)
    full_hydrogen = PeriodicElement(**all_data['hydrogen'])
    print(full_hydrogen)

    # Convert raw data into dict of Elements, Dict[name, python obj]
    converted_data = {}
    for ele_name, ele_data in all_data.items():
        converted_data[ele_name] = PeriodicElement(**ele_data)

    # Display each element and also keep track of the max
    max_width = 0
    max_element = ""
    for ele in converted_data.values():
        # Update max value
        if ele.width > max_width:
            max_width = ele.width
            max_element = ele.name
        
        # Display Element
        # os.system('cls')
        # print(ele)
        # input("Next >")

    # print(converted_data['Hydrogen'].to_dict())
    print(max_element, max_width)

    new_display = Display(list(converted_data.values()))
    new_display.run()


if __name__ == '__main__':
    main()
