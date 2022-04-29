import os

from models.model import save, load, Movie, Show, WorkingCache


"""
Test
---------------------------------------------------------
[x] Create Obj
[x] Create Working Cache
[ ] Convert between storage format and active/parsed format
[ ] Add item to cache
[ ] Display Cache
[ ] export cache
[ ] save/load data
"""

# Global Data
raw_movie_data = {
    "id": 1,
    "name": "Test Movie"
}
raw_show_data = {
    "id": 1,
    "name": "Test Show"
}

def test_movie_create():
    new_movie_obj = Movie(**raw_movie_data)

    assert new_movie_obj.id == raw_movie_data['id']
    assert new_movie_obj.name == raw_movie_data['name']

def test_show_create():
    new_show_obj = Show(**raw_show_data)

    assert new_show_obj.id == raw_show_data['id']
    assert new_show_obj.name == raw_show_data['name']


def test_working_cache():
    new_cache = WorkingCache()

    new_cache.add_item(Movie(**raw_movie_data))
    new_cache.add_item(Show(**raw_show_data))
    
    assert new_cache.cache_count == 2


def main():
    return

if __name__ == '__main__':
    main()
