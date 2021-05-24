from flask import render_template, jsonify
from .musipy import Musipy
from backend import app

mpy = Musipy()

@app.route('/')
def index():
    return '<h1>Hello there!</h1>'

@app.route('/songs/<playlist_id>')
def get_songs_data(playlist_id):
    return jsonify(Musipy.get_songs(playlist_id))

@app.route('/lyrics/<title>/<author>/<trans_lang>')
def get_lyrics_data(title, author, trans_lang):
    return jsonify(Musipy.get_lyrics(title, author, trans_lang))
