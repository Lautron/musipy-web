import spotipy, pprint, re
from spotipy.oauth2 import SpotifyClientCredentials
from .config import sp_id, sp_secret

sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=sp_id,
        client_secret=sp_secret)
        )

def get_songs_data(playlist_id):
    songs_data = []
    playlist = sp.playlist(playlist_id)
    for song in playlist['tracks']['items']:
        songs_data.append((song['track']['name'], song['track']['artists'][0]['name']))
    return songs_data


if __name__ == "__main__":
    print(get_song_dict('https://open.spotify.com/playlist/4zBVGR3eBYD1UcL24ytABt?si=JFl3NkkbTaWhVMOINJ85AQ'))
