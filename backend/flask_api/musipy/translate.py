from deep_translator import GoogleTranslator

def translate_verse(verse, desti='en'):
    translation = GoogleTranslator(source='auto', target=desti).translate(verse)
    if type(translation) is list:
        translation = translation[0]
    return translation
