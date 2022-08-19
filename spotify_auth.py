#   Extra:
from venv import create
from webbrowser import get
from dotenv import load_dotenv
import os
load_dotenv()
SPOTIPY_CLIENT_ID = os.getenv("client_id")
SPOTIPY_CLIENT_SECRET = os.getenv("client_secret")

#   Required
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util


client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def create_playlist(username):

    playlist_name = input('Enter playlist name: ')

    token = util.prompt_for_user_token(username=username, scope='playlist-modify-public', client_id=SPOTIPY_CLIENT_ID,
                                       client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri="https://example.com")
    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        playlists = sp.user_playlist_create(username, playlist_name)
        return playlists['id']

def get_song_id(songs,artists,albums):
    song_ids = []
    ex_albums = []
    ex_songs = []
    final_ids = []
    while len(songs) > 1:
        print(songs)
        print(artists)
        song_id = sp.search(q='artist:' + artists[0] + ' track:' + songs[0], type='track')
        for songID in song_id['tracks']['items']:
            song_ids.append(songID['id'])
        if not song_ids:
            ex_albums.append(albums[0])
            ex_songs.append(songs[0])
        else:
            final_ids.append(song_ids[0])
        song_ids = []
        del songs[0]
        del artists [0]
        del albums[0]

    print("Finished")
    return final_ids

def add_songs(username, song_ids, pl_id):
    token = util.prompt_for_user_token(username=username, scope='playlist-modify-public', client_id=SPOTIPY_CLIENT_ID,
                                    client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri="https://example.com")
    
    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        results = sp.user_playlist_add_tracks(username, pl_id, song_ids)
        print('Finished transferring playlist')
        return results
