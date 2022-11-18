import os
from urllib import response

import requests

from dotenv import load_dotenv
from typing import Dict, List


"""
Program: Movie/Show Companion
Author: Rickyg3
Date: 04/24/22
"""

def test_response(api_key):
    # Response Sample Url
    sample_url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query=Jack+Reacher"

    response = requests.get(sample_url)
    print(response.status_code)
    print(type(response.status_code))

    if response.status_code != 200:
        return False

    print(response.json())
    return True


class MovieFetcher:
    def __init__(self, api_key: str):
        self.base_url = "https://api.themoviedb.org/3/"
        self.api_key = api_key

    def __str__(self) -> str:
        txt = ""
        return txt
    
    def get_details(self, item_type: str, item_id: int):
        detail_url = f"{self.base_url}{item_type}/{item_id}?api_key={self.api_key}"

        response = requests.get(detail_url)

        if response.status_code != 200:
            return

        return response.json()

    def search(self, search_type: str, search_query: str) -> List[any]:
        # Validate Item Type
        valid_items = [
            "movie",
            "tv"
        ]
        if search_type not in valid_items:
            return

        # Parse Item Name
        cleaned_search_query = search_query.replace(' ', '+')

        search_url = f"{self.base_url}search/{search_type}?api_key={self.api_key}&query={cleaned_search_query}"

        response = requests.get(search_url)

        if response.status_code != 200:
            return []

        return response.json()


def main():
    # Load ENV File
    load_dotenv()

    api_key = os.getenv('API_KEY')

    # Test Response
    # test_response(api_key)

    # Create New MovieFetcher Object
    new_data_fetcher = MovieFetcher(api_key)

    # Search up a movie
    movie_search_data = new_data_fetcher.search("movie", "pokemon")
    print(movie_search_data)



  

    return


if __name__ == '__main__':
    main()
