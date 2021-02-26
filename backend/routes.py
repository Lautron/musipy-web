from flask import render_template, jsonify
from .musipy import musipy
from backend import app

@app.route('/')
def index():
    return '<h1>Hello there!</h1>'

@app.route('/<playlist_id>')
def get_playlist_json(playlist_id):
    if len(playlist_id) != 22:
        return '<h1>Incorrect id</h1>'
    songs_json = jsonify(musipy(playlist_id))
    return songs_json

