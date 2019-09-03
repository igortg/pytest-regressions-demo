from datetime import datetime

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from serialchemy.func import dump

from flask_conf_tutorial.app import Base
from flask_conf_tutorial.player_char import PlayerChar, ClasseChar, RacaChar


@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    conn = engine.connect()
    Base.metadata.create_all(bind=conn)
    Session = sessionmaker(bind=conn)
    yield Session()
    conn.close()


def test_level_up(session):
    player_char = PlayerChar(nome="Yennefer", classe=ClasseChar.Xama, raca=RacaChar.Human)
    session.add(player_char)
    session.commit()

    player_char.level_up()

    assert player_char.data_ultimo_level_up == datetime.now()
    assert player_char.forca == 10.5
    assert player_char.resistencia == 10.8
    assert player_char.inteligencia == 12.0
    assert player_char.habilidade == 11.5
    assert player_char.pontos_de_vida == 1200.0
    assert player_char.pontos_de_mana == 912.0
    assert player_char.modificador_espada == 0.21
    assert player_char.modificador_machado == 0.315


def test_level_up_regression(session, data_regression):
    player_char = PlayerChar(nome="Yennefer", classe=ClasseChar.Xama, raca=RacaChar.Human)
    session.add(player_char)
    session.commit()

    player_char.level_up()

    data_regression.check(dump(player_char))

