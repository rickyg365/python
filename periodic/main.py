import os

from model import PeriodicElement
from handle_data import load_periodic_data
from view import Display


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

    # new_display = Display(list(converted_data.values()))
    new_display = Display(list(converted_data.values()), use_keyboard=False)
    new_display.run()


if __name__ == '__main__':
    main()
