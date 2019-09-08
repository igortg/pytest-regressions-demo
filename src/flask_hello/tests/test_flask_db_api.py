from freezegun import freeze_time

from sqlalchemy_hello.player_char import PlayerChar, ClasseChar, Espada


@freeze_time("2019-09-08")
def test_flask_api_player_char(client, data_regression):
    from sqlalchemy_hello.app import init_db

    init_db()
    seed_db()

    resp = client.get('/api/player-char/1')
    assert resp.status_code == 200
    data_regression.check(resp.get_json())


def seed_db():
    from sqlalchemy_hello.app import db_session

    espada_nilfgaardian = Espada(nome="Nilfgaardian longsword", dano=36, min_level=3)
    character = PlayerChar(
        id=1,
        nome="Dandelion",
        classe=ClasseChar.Druida,
        pontos_xp=1200,
        level=1,
        forca=8,
        inteligencia=14,
        pontos_de_vida=850,
        pontos_de_mana=200,
        modificador_espada = 0.03,
        modificador_machado = -0.02,
        modificador_arco = 0,
        arma_primaria=espada_nilfgaardian,
    )
    session = db_session()
    session.add(character)
    session.commit()


