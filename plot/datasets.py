import os
import pandas as pd
import numpy

def get_dataset_path(choice: str):
    """
    + anime
    + climate
    + nasa
    + netflix
    + pokemon
    + stores
    
    """
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
        new_data = data_sets[choice][0]
    return new_data



class Handle:
    def __init__(self, data_path: str):
        self.filepath = data_path
        self.data = pd.read_csv(data_path)
        
        self.length = len(self.data)
        self.columns = [c for c in self.data.columns]
        
        # search_term: index
        self.previous_search = {}


    def __str__(self) -> str:
        txt = f"[{self.length}] {self.filepath} \n{self.columns}"
        return txt

    def search(self, search_term: str, attr: str="name"):
        # Check if Searched before
        seen_before = self.previous_search.get(search_term, None)
        if seen_before is not None:
            return self.data.iloc[seen_before]

        # Search for Value
        for _ in range(len(self.data[attr])):
            check_value = self.data[attr][_]

            if type(check_value) is numpy.int64:
                if search_term == check_value:
                    self.previous_search[search_term] = _
                    return self.data.iloc[_]
            else:
                if search_term in check_value:
                    self.previous_search[search_term] = _
                    return self.data.iloc[_]
        return None


def main():
    '''
    Columns:
        - anime_id
        - name
        - genre
        - type
        - episodes
        - rating
        - members
    '''

    path = get_dataset_path("anime")

    # Load Data - Pandas
    data = pd.read_csv(path)
    data.set_index("anime_id")

    # Load Data - Custom Handler
    handler = Handle(path)
    print(handler)

    # Search - by Name
    search_term = "Gint"
    wanted_item = handler.search(search_term=search_term, attr='name')

    print(wanted_item)

    # Search - by Id
    search = 11061
    want = handler.search(search, attr="anime_id")
    
    print(want)

    # Previous Searches
    print(handler.previous_search)

if __name__ == '__main__':
    main()
