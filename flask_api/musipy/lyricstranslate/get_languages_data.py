from .helpers import get_soup_obj

def get_language_ids():
    soup = get_soup_obj('https://lyricstranslate.com/en/translations')
    languages = soup.select("#edit-formtree-ltsearchlanguageto optgroup option")
    language_dict = { language.text.lower(): language.get('value') for language in languages}
    return language_dict

if __name__ == "__main__":
    print(get_language_dict())
