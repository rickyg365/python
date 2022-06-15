


def input_anime_entry_data():
    """  
    Key: input_type -> return_type

    return {
        name: str 
        release_date: str
        genres: "str str str" -> [str]
        notes: str
    }
    """
    check_empty = lambda x: "N/A" if x == "" else x

    print("\n[ Input New Anime ] ")
    name = input("Name: ")  # str
    release_date = input("Release Date: ")  # str -> Date
    genres = input("Genre/s: ").split(" ")  # List
    notes = input("Notes: ")  # str (multiline?)

    return {
        "name": name,
        "release_date": check_empty(release_date),
        "genres": genres,
        "notes": check_empty(notes)
    }

