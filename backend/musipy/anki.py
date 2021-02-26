import genanki, random
from test import test_dict

my_model = genanki.Model(
  1106024766,
  'Musipy Model',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Question}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    },
  ])


def make_anki_deck(name, song_dict):
    decks = []
    for song in song_dict.keys():
        print(f'Creating {song} deck...')
        my_deck = genanki.Deck(
        random.randrange(1 << 30, 1 << 31),
        song)
        for verse, trans in song_dict[song]['lyrics'].items():
            my_note = genanki.Note(
            model=my_model,
            fields=[verse, trans])
            my_deck.add_note(my_note)
        decks.append(my_deck)
    print('Writing package...')
    genanki.Package(decks).write_to_file(f'{name.replace(" ", "-")}.apkg')
    print('Done')

if __name__ == "__main__":
    make_anki_deck('Rammstein Crack', test_dict)
