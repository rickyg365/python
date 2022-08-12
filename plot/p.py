import os

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns


data_sets = {
    "anime": ["data/anime/anime.csv", "data/anime/rating.csv"],
    "climate": ["data/climate/DailyDelhiClimateTest.csv", "data/climate/DailyDelhiClimateTrain.csv"],
    "nasa": ["data/nasa_neo/neo.csv", "data/nasa_neo/neo_v2.csv"],
    "netflix": ["data/netflix/netflix.csv"],
    "pokemon": ["data/pokemon/df_pokemon.csv", "data/pokemon/df_abilities.csv"],
    "stores": ["data/stores/Stores.csv"],
}




def load_data_set(choice: str):
    new_data = None
    data_sets = {
        "anime": ["data/anime/anime.csv", "data/anime/rating.csv"],
        "climate": ["data/climate/DailyDelhiClimateTest.csv", "data/climate/DailyDelhiClimateTrain.csv"],
        "nasa": ["data/nasa_neo/neo.csv", "data/nasa_neo/neo_v2.csv"],
        "netflix": ["data/netflix/netflix.csv"],
        "pokemon": ["data/pokemon/df_pokemon.csv", "data/pokemon/df_abilities.csv"],
        "stores": ["data/stores/Stores.csv"],
    }

    if choice in data_sets.keys():
        new_data = pd.read_csv(data_sets[choice][0], parse_dates=True)
    return new_data

def explore_dataset(dataframe: pd.DataFrame | pd.Series):
    print(dataframe.head())
    print(dataframe.columns, "\n")
    print(dataframe.describe())
    print(dataframe.shape)


def main():
    # anime_data_path = data_sets['anime'][0]
    # anime_data = pd.read_csv(anime_data_path)
    # print(anime_data.head())

    data = load_data_set("anime")

    # Row Labels
    print(data.columns)
    data_w_index = data.set_index(data.columns[0])  # Can also use inplace param to not create new object
    
    # explore_dataset(data_w_index)

    # Set the width and height of the figure
    plt.figure(figsize=(10,6))

    # Line chart showing how FIFA rankings evolved over time
    # sns.lineplot(data=data_w_index)
    # sns.lineplot(data=data_w_index["Volume"], label="Volume")
    sns.jointplot(data=data_w_index, x="episodes", y="rating")

    plt.show()


if __name__ == '__main__':
    main()
