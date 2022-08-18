#   Extra:
from venv import create
from dotenv import load_dotenv
import os
load_dotenv()
SPOTIPY_CLIENT_ID = os.getenv("client_id")
SPOTIPY_CLIENT_SECRET = os.getenv("client_secret")
redirect = os.getenv("redirect_url")

#   Required
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util


client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def create_playlist(username):

    username = "squidnugget77"
    playlist_name = input('Enter playlist name: ')

    token = util.prompt_for_user_token(username=username, scope='playlist-modify-public', client_id=SPOTIPY_CLIENT_ID,
                                       client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri="https://example.com")
    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        playlists = sp.user_playlist_create(username, playlist_name)
        return playlists['id']

print(create_playlist("squidnugget77"))