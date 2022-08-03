from .helpers import get_soup_obj
from .get_languages_data import get_language_ids

def get_song_link(url: str):
    soup = get_soup_obj(url)
    domain = "https://lyricstranslate.com"
    song_links = soup.select('td.ltsearch-songtitle a', limit=1)
    return domain + song_links[0].get('href')

def get_lyrics(url: str):
    soup = get_soup_obj(url)
    verses = soup.select('div.ltf div div')
    return [verse.text.strip('\n') for verse in verses if verse]

def lyricstranslate(author: str, title: str, trans_lang: str):
    languages: dict = get_language_ids()
    url = f"https://lyricstranslate.com/en/translations/0/{languages[trans_lang]}/{author}/{title}/none/0/0/0/0"
    link: str = get_song_link(url)
    lyrics: list = get_lyrics(link)
    return lyrics
    
if __name__ == "__main__":
    lyricstranslate("Rammstein", "Deutschland", "english")
