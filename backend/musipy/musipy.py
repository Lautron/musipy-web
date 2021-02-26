from .sp_playlist import get_song_dict
from .lyrics import get_lyrics_trans
import time, pprint, csv

def write_csv(data, filename='test'):
    with open(f'{filename}.csv', 'a', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for track in data.keys():
            writer.writerow([' ', ' '])
            writer.writerow([track, ' '])
            if data[track]['lyrics']:
                for verse, trans in data[track]['lyrics'].items():
                    row = [verse, trans]
                    writer.writerow(row)

def musipy(playlist_id):
#    if not link:
#        link = input('Paste playlist URL...\n')

    song_dict = get_song_dict(playlist_id)
    song_vocab_dict = {}
    start = time.time()
    for song in song_dict.keys():
        verse_dict = get_lyrics_trans(song, song_dict[song]['artist'])
        song_vocab_dict.update({
            song: {'lyrics': verse_dict,
                    'artist': song_dict[song]['artist']}
                })

#    with open('test.py', 'w') as f:
#        f.write('test_dict = ' + pprint.pformat(song_vocab_dict))
#
#    write_csv(song_vocab_dict)
    ex_time = time.time() - start

    print(f'The program took {ex_time} seconds\n{ex_time // len(song_vocab_dict)} seconds per song') 
    return song_vocab_dict

if __name__ == "__main__":
    musipy('https://open.spotify.com/playlist/7gw9ny2d3Gzka2ag550fbo?si=5Apb9fJ1TV23yk44_Vf-8Q')

