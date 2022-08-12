import os
import json

import pandas as pd


def extract_data(raw_data):
    return {
        "ID": raw_data.get("ID", None),
        "Name": raw_data.get("Name", None),
        "Species": raw_data.get("Species", None),
        "Variant": raw_data.get("Variant", None),
        "Generation": raw_data.get("Generation", None),
        "Rarity": raw_data.get("Rarity", None),
        "Evolves_from": raw_data.get("Evolves_from", None),
        "Type1": raw_data.get("Type1", None),
        "Type2": raw_data.get("Type2", None),
        "Total": raw_data.get("Total", None),
        "HP": raw_data.get("HP", None),
        "Attack": raw_data.get("Attack", None),
        "Defense": raw_data.get("Defense", None),
        "Sp. Atk": raw_data.get("Sp. Atk", None),
        "Sp. Def": raw_data.get("Sp. Def", None),
        "Speed": raw_data.get("Speed", None)
    }

def extract_dataframe(**raw_data):
    return {
        "ID": raw_data.get("ID", None),
        "Name": raw_data.get("Name", None),
        "Species": raw_data.get("Species", None),
        "Variant": raw_data.get("Variant", None),
        "Generation": raw_data.get("Generation", None),
        "Rarity": raw_data.get("Rarity", None),
        "Evolves_from": raw_data.get("Evolves_from", None),
        "Type1": raw_data.get("Type1", None),
        "Type2": raw_data.get("Type2", None),
        "Total": raw_data.get("Total", None),
        "HP": raw_data.get("HP", None),
        "Attack": raw_data.get("Attack", None),
        "Defense": raw_data.get("Defense", None),
        "Sp. Atk": raw_data.get("Sp. Atk", None),
        "Sp. Def": raw_data.get("Sp. Def", None),
        "Speed": raw_data.get("Speed", None)
    }




def main():
    filepath = "df_pokemon.csv"
        
    wanted_keys = [
        "ID",
        "Name",
        "Species",
        "Variant",
        "Generation",
        "Rarity",
        "Evolves_from",
        "Has_gender_diff",
        "Type1",
        "Type2",
        "Total",
        "HP",
        "Attack",
        "Defense",
        "Sp. Atk",
        "Sp. Def",
        "Speed"
    ]
    
    data = pd.read_csv(filepath)  # .set_index("ID"), Gigantamax and Megas dont have unique ID's
    j_data = json.loads(data.to_json())

    cols = [c for c in data.columns]

    # print(cols)
    # print(len(data))

    pokedex = {}

    for _ in range(5):
        print(f"# {_}")
        pokedex[_] = {}
        for col in data:
            if col in wanted_keys:
                pokedex[_][col] = data[col][_]
                print(data[col][_])
            
    # print(j_data.keys())
    # print(extract_data(j_data))
    print(pokedex)



if __name__ == '__main__':
    main()
