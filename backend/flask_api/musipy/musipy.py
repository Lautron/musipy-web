from .sp_playlist import get_songs_data
from .lyrics import get_lyrics_dict

class Musipy:
    @staticmethod
    def get_songs(playlist_id):
        return get_songs_data(playlist_id)

    @staticmethod
    def get_lyrics(song_title, author, trans_lang):
        return get_lyrics_dict(song_title, author, trans_lang='en')

if __name__ == "__main__":
    test = Musipy()
    print(test.get_songs('https://open.spotify.com/playlist/4zBVGR3eBYD1UcL24ytABt?si=JFl3NkkbTaWhVMOINJ85AQ'))
    print(test.get_lyrics("AUSLÄNDER", 'Rammstein', trans_lang='en'))

