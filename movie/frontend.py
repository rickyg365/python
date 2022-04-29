import os

# Utils
from utils.utils import save, load

# Models
from models.model import Movie, Show
from models.data_input import input_item, parse_item
from models.working_cache import WorkingCache


"""
"""

class Frontend:
    def __init__(self) -> None:
        
        return
    
    def __str__(self) -> str:
        txt = ""
        return txt


# For Displaying

# For Editing/ Deleting

# For INput
def run():
    # Load Data before we start so we dont overwrite when we save
    new_data = load("data/test_frontend.json")
    working_data = [parse_item(i) for i in new_data]
    
    movie_cache = WorkingCache()
    for w in working_data:
        movie_cache.add(Movie(**w))

    for i in range(5):
        os.system('cls')        
        new_item = input_item()
        # print(new_item)

        # Convert to Movie
        new_movie = Movie(**new_item)
        # print(new_movie)

        # Add to Cache
        movie_cache.add(new_movie)

    # Save New Data
    save(movie_cache.export(), "data/test_frontend.json")



def main():
    run()
    


if __name__ == '__main__':
    main()
