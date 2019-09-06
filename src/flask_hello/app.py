from datetime import datetime

from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('hello.html', name='Flask Conf 2019')


@app.route('/api/heroes')
def heroes_collection():
    return jsonify(HEROES)


@app.route('/api/heroes/<int:hero_id>')
def heroes_item(hero_id):
    for hero in HEROES:
        if hero_id == hero['id']:
            return jsonify(hero)
    else:
        return "Error", 404


HEROES = [
    {'id': 11, 'name': 'Mr. Nice', 'Birth': datetime(2000, 10, 19)},
    {'id': 12, 'name': 'Narco', 'Birth': datetime(1984, 4, 23)},
    {'id': 13, 'name': 'Bombasto', 'Birth': datetime(1996, 11, 3)},
    {'id': 14, 'name': 'Celeritas', 'Birth': datetime(2003, 4, 30)},
    {'id': 15, 'name': 'Magneta', 'Birth': datetime(1980, 12, 9)},
    {'id': 16, 'name': 'RubberMan', 'Birth': datetime(1985, 9, 17)},
    {'id': 17, 'name': 'Dynama', 'Birth': datetime(1992, 2, 8)},
    {'id': 18, 'name': 'Dr IQ', 'Birth': datetime(1998, 3, 18)},
    {'id': 19, 'name': 'Magma', 'Birth': datetime(2001, 6, 25)},
    {'id': 20, 'name': 'Tornado', 'Birth': datetime(1997, 4, 12)}
];


@app.route('/api/player-char/<int:player_id>')
def player_char_item(player_char_id):
    from sqlalchemy_hello.app import init_db
    from sqlalchemy_hello.player_char import PlayerChar, PlayerCharSerializer

    session = init_db()
    player_char = session.query(PlayerChar).get(player_char_id)
    serialized = PlayerCharSerializer(PlayerChar).dump(player_char)
    return serialized
