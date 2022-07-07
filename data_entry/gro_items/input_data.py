import os

from utils.save_load import save_json, load_json
from utils.config import input_data, input_raw_config, get_config, parse_raw_config


def main():
    # Variables
    config_path = "data/grocery/config.json"

    store_name = input("Store Name: ")
    data_path = f"data/grocery/{store_name}/items.json"

    if not os.path.exists(data_path):
        os.mkdir(f"data/grocery/{store_name}")
    # new permanent config to save
    # save_json(input_raw_config(), config_path)

    # Load Config
    config = get_config(config_path)
    # print(config)

    # Load data
    load_data = load_json(data_path)

    # Inpute New Data
    new_data = input_data(config)

    final_data = [*load_data, *new_data]
    # Save New Data
    save_json(final_data, data_path)
    return

if __name__ == '__main__':
    main()
