import os
import json


# Parsing Variables
# raw_name, python_attr_name
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

# Parsing Variables
# raw_name, data_type_conversion_func
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