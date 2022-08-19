import spotify_auth as sa
import applemusic_xl as amx

songs = amx.find_name()
print(songs)
artists = amx.find_artist()
print(artists)
albums = amx.find_album()
username = input("What is your Spotify username?")
playlistid = sa.create_playlist(username)
song_ids = sa.get_song_id(songs,artists,albums)
sa.add_songs(username,song_ids,playlistid)