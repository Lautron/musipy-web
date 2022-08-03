# musipy-web
## Installation
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
## Usage
### Get songs in playlist
#### Request
```http
GET /songs/<playlist_id>
```

| Parameter     | Type     | Description                                         |
| :--------     | :------- | :----------                                         |
| `playlist_id` | `string` | Spotify Playlist ID, commonly found on playlist URL |

#### Response
List containing song title and band name for each song in the playlist
```
[
  [
    "song_title", 
    "band_name"
  ], 
  ...
]
```
### Get song lyrics
#### Request
```http
GET /lyrics/<title>/<author>/<trans_lang>
```
| Parameter    | Type     | Description                 |
| :--------    | :------- | :----------                 |
| `title`      | `string` | Song title                  |
| `author`     | `string` | Song author                 |
| `trans_lang` | `string` | Two letter code for target translation language |

#### Response
List containing original version and translated version for each verse in the song
```
[
  [
    "original_verse", 
    "translated_verse"
  ], 
  ...
]
```
## TODO
- Add better error handling
- Follow general API conventions
- Add route to generate anki flashcards from song lyrics


