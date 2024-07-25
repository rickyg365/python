import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from dotenv import load_dotenv

# Load env Variables
load_dotenv('.env')

C_ID = os.getenv("CLIENT_ID")
C_SECRET = os.getenv("CLIENT_SECRET")

client_credential_manager = SpotifyClientCredentials(client_id=C_ID, client_secret=C_SECRET)

spotify_client = spotipy.Spotify(client_credentials_manager=client_credential_manager)


# Get a search
user = spotify_client.current_user()
top_tracks = spotify_client.current_user_top_tracks()

print(f"""
{user}


{top_tracks}
""")


# spotify_client.user_playlist_create
# spotify_client.playlist_add_items




def main():
    return

if __name__ == "__main__":
    main()