import spotipy, pprint, re
from spotipy.oauth2 import SpotifyClientCredentials
from .config import sp_id, sp_secret

sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=sp_id,
        client_secret=sp_secret)
        )

def get_plst_by_link(link):
    playlist_id = re.compile(r'/(\w{22})')\
                    .search(link)\
                    .group(1)
    return playlist_id

def get_plst_by_name(name, author):
    found = False
    results = sp.search(name, limit=50, type="playlist")
    for playlist in results['playlists']['items']:
        if playlist['owner']['display_name'] == author:
            found = True
            return playlist['id']

    if not found:
        print("Couldn't find playlist. Try searching by link instead.")

def get_playlist_songs(playlist_id):
    song_dict = {}
    playlist = sp.playlist(playlist_id)
    for song in playlist['tracks']['items']:
        song_dict.update({ song['track']['name']: {'artist': song['track']['artists'][0]['name']}})
    return song_dict

def get_song_dict(playlist_id):
#    playlist_id = get_plst_by_link(link)
    song_dict = get_playlist_songs(playlist_id)
    return song_dict 

if __name__ == "__main__":
    print(get_song_dict('https://open.spotify.com/playlist/4zBVGR3eBYD1UcL24ytABt?si=JFl3NkkbTaWhVMOINJ85AQ'))
