import os

from utils.utils import load, save
from models.model import Movie, Show


class WorkingCache:
    def __init__(self):
        # Size
        self.cache_count = 0
        
        # Item ID: Item
        self.items = {}
        
    def __str__(self) -> str:
        txt = f"Count: {self.cache_count}"
        return txt
    
    def export(self):
        """ Assumes item has to_dict() method """
        # Method #1
        new_list = []
        
        for id, item in self.items.items():
            new_list.append(item.to_dict())

        # Method #2
        # new_list = [x.to_dict() for x in self.items.values()]

        return new_list
    
    def add(self, item_obj):
        """ Overwrites on collision """
        self.items[item_obj.id] = item_obj
        self.cache_count += 1

    def delete(self, item_id: int):
        """ Delete Item """
        del self.items[item_id]
        self.cache_count -= 1


def main():
    # Create Movie and Show object
    new_movie = Movie(1, "Test Movie")
    new_show = Show(1, "Test Show")

    # Display
    print(new_movie)
    print(new_show)

    # Create working memory cache(python obj's)
    movie_cache = WorkingCache()
    anime_cache = WorkingCache()

    # Add items to cache
    movie_cache.add(new_movie)
    anime_cache.add(new_show)

    # Print Cache
    print(movie_cache)
    print(anime_cache)

    # Export and save movie data
    movie_data = movie_cache.export()
    save(movie_data, "data/movies.json")

    # Export and save show data
    show_data = anime_cache.export()
    save(show_data, "data/show.json")


if __name__ == '__main__':
    main()
