import lyricsgenius, re, pprint, csv, time
from .config import genius_api_key
from .translate import translate_verse
from multiprocessing.dummy import Pool as ThreadPool
from .lyricstranslate import lyricstranslate

pool = ThreadPool(8)
genius = lyricsgenius.Genius(genius_api_key)

def get_lyrics_list(song_title, author):
    try:
        lyrics = genius.search_song(song_title, artist=author).lyrics
    except:
        return None
    regx = re.compile(r'\[.*\]|')
    #TODO: Handle weird text on lyrics like URLCopyEmbedCopy
    #      To reproduce the error use main function with "Auslander"
    cleaned_lyrics = re.sub(regx, '', lyrics.replace('\u2005', ' '))
    lyrics_list = cleaned_lyrics.split('\n')
    return [verse.strip() for verse in lyrics_list if verse]

def get_lyrics_dict(song_title, author, trans_lang='english'):
    lang_dict = {
        'español': ' (traducción al español)',
        'english': ' (english translation)'
    }
    songs = [song_title, song_title + lang_dict[trans_lang]]
    lyrics = [get_lyrics_list(song, author) for song in songs]
    is_invalid = lambda lyrics: not lyrics[1] or not len(lyrics[0]) == len(lyrics[1])
    if not lyrics[0]:
        print(f'No lyrics found for "{song_title}"\n')
        return None
    if is_invalid(lyrics):
        print('\nSearching song on lyricstranslate...')
        lyrics[1] = lyricstranslate(author, song_title, trans_lang)
        if is_invalid(lyrics):
            print('\nTranslating song...')
            lyrics[1] = pool.map(translate_verse, lyrics[0])
        
    res = list(zip(lyrics[0], lyrics[1]))
    return res

if __name__ == "__main__":
    print(get_lyrics_dict("AUSLÄNDER", 'Rammstein', trans_lang='english'))
