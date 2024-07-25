import os
import requests

from dotenv import load_dotenv

from utils.spotify_wrapper import authorize, build_search


"""
base_url = "https://api.spotify.com/v1"

# Searching

# filters
- artist | albums, artists, and tracks |
- album and year | album and tracks |
- genre | tracks and artists |
- isrc and track | tracks |
- upc, tag:new and tag:hipster | albums | new:past 2 weeks, hipster only lowest 10%

# Types, ? q=name:abacab&type=album,track ?
- album
- artist
- playlist
- track
- show
- episode

# Limit, 0-50

# Market, country code

# Offset, index of first item returned, starts w/ 0
- Use to get next page

"""


def pprint(obj, indent_level: int = 0):
    def is_dict(x): return type(x) is dict
    def is_list(x): return type(x) is list

    if is_dict(obj):
        for k, v in obj.items():
            print(f'{k}: ')
            if is_dict(v) or is_list(v):
                pprint(v, indent_level + 1)
            else:
                print(f"{(indent_level + 1) * '  '}{v}")
        return

    if is_list(obj):
        for i in obj:
            if is_dict(i) or is_list(i):
                pprint(i, indent_level)
            else:
                print(f"{(indent_level + 1) * '  '}{i}")

        return

    else:
        print(f"{indent_level * ' '}{obj}")


def run_search(header):
    # Search
    QUERY = input("Search: ")
    SEARCH_TYPES = ["album", "track", "artist"]

    url = build_search(QUERY, types=SEARCH_TYPES)

    # Make sure you use keyword to assign headers
    r = requests.get(url, headers=header)
    r_data = r.json()

    return r_data


def break_down_track(track):
    track_data = {
        "name": track['name'],
        "duration": track['duration_ms'],
        "album_name": track['album']['name'],
        "release_date": track['album']['release_date'],
        "id": track['id'],
        "uri": track['uri'],
        "artists": [a['name'] for a in track['artists']]
    }
    return track_data


if __name__ == '__main__':
    #! Authorization
    # Load in AUTH env
    load_dotenv('.env')

    # Client ID/Secret
    CLIENT_ID = os.getenv('CLIENT_ID')
    CLIENT_SECRET = os.getenv('CLIENT_SECRET')

    # Get access token
    access_token = authorize(CLIENT_ID, CLIENT_SECRET)

    # Setup Header w/ authorization token
    header = {
        'Authorization': f'Bearer {access_token}'
    }

    #! Use header to perform spotify api actions
    # Search
    # QUERY = "pokemon"
    # SEARCH_TYPES = ["album", "track", "artist"]

    QUERY = "monodrama"
    SEARCH_TYPES = ["track"]

    url = build_search(QUERY, types=SEARCH_TYPES)

    # Make sure you use keyword to assign headers
    r = requests.get(url, headers=header)
    r_data = r.json()

    # Explore Results
    # for track in r_data['tracks']['items']:
    #     wanted_data = break_down_track(track)
    #     pprint(wanted_data)
    #     print(40*"-")

    last_track = r_data['tracks']['items'][0]

    # ? Play song on spotify
    # print(last_track['external_urls']['spotify'])

    # ? Link to song w/ auth
    # print(last_track['href'])

    # ? Request specific song data
    # song_data = requests.get(last_track['href'], headers=header)

    # song_data = song_data.json()
    # print(song_data)

    # https: //api.spotify.com/v1/audio-features?ids=7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B
    # ? Request specific song feature data
    song_data = requests.get(
        f"https://api.spotify.com/v1/audio-features?ids={last_track['id']}", headers=header)

    song_data = song_data.json()

    # print(song_data)
    pprint(song_data)
