import os

from typing import Dict, List
from dataclasses import dataclass


"""
# Necessary
album
artists
available_markets
duration_ms
explicit
id
is_playable
name
popularity
preview_url
track_number
type
uri

# Not Necessary
external_ids
external_urls
href

linked_from
restrictions

is_local
disc_number
"""

def parse_data(raw_data):
    wanted_data = {
        "album": raw_data['album'],
        "artists": raw_data['artists'],
        "available_markets": raw_data['available_markets'],
        "duration_ms": raw_data['duration_ms'],
        "explicit": raw_data['explicit'],
        "id": raw_data['id'],
        "is_playable": raw_data['is_playable'],
        "name": raw_data['name'],
        "popularity": raw_data['popularity'],
        "preview_url": raw_data['preview_url'],
        "track_number": raw_data['track_number'],
        "type": raw_data['type'],
        "uri": raw_data['uri']
    }

    return wanted_data


@dataclass
class Track:
    album: Dict[str, any]
    artists: List[any]
    available_markets: List[str]
    duration_ms: int
    explicit: bool
    id: str
    is_playable: bool
    name: str
    popularity: int
    preview_url: str
    track_number: int
    type: str
    uri: str

    def __str__(self) -> str:
        pass

def main():

    return

if __name__ == '__main__':
    main()
