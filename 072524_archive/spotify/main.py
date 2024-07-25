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
    QUERY = "pokemon"
    SEARCH_TYPES = ["album", "track", "artist"]

    url = build_search(QUERY, types=SEARCH_TYPES)

    # Make sure you use keyword to assign headers
    r = requests.get(url, headers=header)
    r_data = r.json()

    # Explore Results
    for track in r_data['tracks']['items']:
        print(f"""
name: {track['name']}
duration: {track['duration_ms']}
album name: {track['album']['name']}
release date: {track['album']['release_date']}
id: {track['id']}
uri: {track['uri']}
        """)
        print("Artists:")
        for artist in track['artists']:
            print(artist['name'])
