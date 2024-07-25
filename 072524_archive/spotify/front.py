import os
import json

"""
[Page 1]
Song     Artist    Genre     Duration    Date
Africa   Toto      Classic   1:23        09/23/23
Africa   Toto      Classic   1:23        09/23/23
Africa   Toto      Classic   1:23        09/23/23
Africa   Toto      Classic   1:23        09/23/23
Africa   Toto      Classic   1:23        09/23/23
* type song name to select
[P]rev Page  [N]ext Page  [G]oto page #
>>> 
"""

# UI Variables
SONG_GAP = 15
ARTIST_GAP = 10
GENRE_GAP = 10
DURATION_GAP = 10
DATE_GAP = 10


def flatten_entry(data):
    NAME = data.get("song", "N/A")
    ARTIST = data.get("artist", "N/A")
    GENRE = data.get("genre", "N/A")
    DURATION = data.get("duration", "N/A")
    DATE = data.get("date", "N/A")
    return f"{NAME:<{SONG_GAP}}{ARTIST:<{ARTIST_GAP}}{GENRE:<{GENRE_GAP}}{DURATION:<{DURATION_GAP}}{DATE:<{DATE_GAP}}"


def songs_page(data):
    page = f"{'Song':<{SONG_GAP}}{'Artist':<{ARTIST_GAP}}{'Genre':<{GENRE_GAP}}{'Duration':<{DURATION_GAP}}{'Date':<{DATE_GAP}}"
    for entry in data:
        new_line = flatten_entry(entry)
        page += f"\n{new_line}"

    return page


# App Variables
CURRENT_PAGE = 0

SINGLE_ENTRY = None
SAMPLE_DATA = None

# Load Data
with open('sample_data.json', 'r') as sample_data:
    SAMPLE_DATA = json.load(sample_data)

SINGLE_ENTRY = SAMPLE_DATA[0]


def app():
    print(songs_page(SAMPLE_DATA))


if __name__ == "__main__":
    app()
