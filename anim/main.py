import os
from pathlib import Path
import anipy_cli as anime

from copy import deepcopy

"""   
Edit Download Path

find module path 
    print(anime.__file__)

go into config and follow instrcuctions form github


print(Path.home() / 'anime' / 'naruto')

"""


def fill_entry(anime_name: str):
    empty_entry = anime.entry()
    
    # Query
    query_results = anime.query(anime_name, empty_entry)
    result_names, result_links = query_results.get_links()

    # BReak condition
    if query_results.get_links() == 0:
        return False

    # print(empty_entry)
    # print(result_names, result_links)
    # print(query_results)

    
    # Fill Data
    show_entry = query_results.pick_show()

    # Episode Handling
    ep_class = anime.epHandler(show_entry)
    show_entry = ep_class.pick_ep()

    # Video URL    
    url_class = anime.videourl(show_entry, 'best')
    url_class.stream_url()

    filled_entry = url_class.get_entry()

    return filled_entry


def download_entries(quality: str="best", ffmpeg:bool=False):
    print("[ Download ]")

    show_entry = anime.entry()

    searches = []
    show_entries = []
    
    find = "y"
    while find == "y":
        searches.append(input("Search: "))
        find = input("Add another search: (y|n)\n")

    for search in searches:
        links = 0
        query_class = None

        print("\nCurrent: ", search)
        query_class = anime.query(search, show_entry)
        query_class.get_pages()
        links = query_class.get_links()

        if links == 0:
            print("No Links")
            continue

        show_entry = query_class.pick_show()
        
        ep_class = anime.epHandler(show_entry)
        ep_list = ep_class.pick_range()
        
        show_entries.append(
            {
                "show_entry": deepcopy(show_entry), 
                "ep_list": deepcopy(ep_list)
            }
        )
        
    for ent in show_entries:
        show_entry = ent["show_entry"]
        ep_list = ent["ep_list"]
        for i in ep_list:
            show_entry.ep = int(i)
            show_entry.embed_url = ""
            ep_class = anime.epHandler(show_entry)
            show_entry = ep_class.gen_eplink()
            url_class = anime.videourl(show_entry, quality)
            url_class.stream_url()
            show_entry = url_class.get_entry()
            anime.download(show_entry, ffmpeg).download()


def main():
    # print(fill_entry("naruto"))
    download_entries()
    return

if __name__ == '__main__':
    main()
