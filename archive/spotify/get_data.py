import os
import requests

from dotenv import load_dotenv

import spotipy
from spotipy.oauth2 import SpotifyOAuth

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


var CLIENT_ID
var REDIRECT_URI

function getLoginURL(scopes) {
        return 'https://accounts.spotify.com/authorize?client_id=' + CLIENT_ID +
            '&redirect_uri=' + encodeURIComponent(REDIRECT_URI) +
            '&scope=' + encodeURIComponent(scopes.join(' ')) +
            '&response_type=token';


 var url = getLoginURL([
            'user-read-email'
        ]);


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="YOUR_APP_CLIENT_ID",
                                                           client_secret="YOUR_APP_CLIENT_SECRET"))

results = sp.search(q='weezer', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])
With user authentication
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="YOUR_APP_CLIENT_ID",
                                               client_secret="YOUR_APP_CLIENT_SECRET",
                                               redirect_uri="YOUR_APP_REDIRECT_URI",
                                               scope="user-library-read"))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " - ", track['name'])

"""

def build_search(string_query: str="", filter: str="", types:str="", limit: int=15, offset: int=0):
    base_search_url = "https://api.spotify.com/v1/search?"

    # Build Final URL
    query_url = f"q={string_query}"
    # filters = ""
    types_url = f"type={','.join(types)}"


    final_url = f"{base_search_url}{query_url}&{types_url}"

    return final_url

def main():
    # spotify_authorization()
    auth_url = "https://accounts.spotify.com/api/token"
    # Load in AUTH env
    load_dotenv('AUTH.env')

    # Client ID
    CLIENT_ID = os.getenv('client_id')

    # Client Secret
    CLIENT_SECRET = os.getenv('client_secret')

    auth_data = {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }

    # Response Data
    auth_response = requests.post(auth_url, auth_data)
    response_data = auth_response.json()

    # Save Access Token
    access_token = response_data.get('access_token', None)

    # Setup Header w/ authorization token
    header = {
        'Authorization': f'Bearer {access_token}'
    }   

    url = build_search('pokemon', types=["album", "track", "artist"])

    # Make sure you use keyword to assign headers
    r = requests.get(url, headers=header)
    r_data = r.json()

    for k, v in r_data.items():
        print(k)
        print(v)
    
    return

if __name__ == '__main__':
    main()
