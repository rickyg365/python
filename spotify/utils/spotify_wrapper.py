import requests

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


def authorize(client_id: str, client_secret: str) -> str:
    auth_url = "https://accounts.spotify.com/api/token"

    auth_data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }

    # Send auth request
    auth_response = requests.post(auth_url, auth_data)
    response_data = auth_response.json()

    # Get Access Token
    access_token = response_data.get('access_token', None)

    return access_token


def build_search(string_query: str="", filter: str="", types:str="", limit: int=15, offset: int=0):
    """ Build a search url for use with spotify api """
    base_search_url = "https://api.spotify.com/v1/search?"

    # Build Final URL
    query_url = f"q={string_query}"
    # filters = ""
    types_url = f"type={','.join(types)}"

    return f"{base_search_url}{query_url}&{types_url}"


